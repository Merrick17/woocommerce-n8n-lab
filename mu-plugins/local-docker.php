<?php
/**
 * Local Docker networking and WooCommerce REST API fixes.
 *
 * Handles:
 * - Force HTTP (no HTTPS redirects or SSL requirements in local Docker)
 * - Container URL rewriting for webhooks
 * - REST API auth over HTTP (required for n8n WooCommerce node)
 * - Pretty permalinks + Apache rewrite rules (required for /wp-json/)
 * - WooCommerce REST API enabled by default
 * - Auto-provisioned n8n API credentials
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Normalize any https:// URL to http:// for local Docker hosts.
 */
function local_docker_force_http_url(string $url): string
{
    if (!str_starts_with($url, 'https://')) {
        return $url;
    }

    $host = (string) parse_url($url, PHP_URL_HOST);

    $local_hosts = [
        'localhost',
        '127.0.0.1',
        'wordpress',
        'n8n',
        'host.docker.internal',
    ];

    if (!in_array($host, $local_hosts, true)) {
        return $url;
    }

    return 'http://' . substr($url, 8);
}

/**
 * Map browser / host URLs to Docker service names for outbound requests.
 */
function local_docker_rewrite_internal_url(string $url): string
{
    $url = local_docker_force_http_url($url);

    $internal_url = str_replace(
        [
            'http://localhost:5678',
            'http://host.docker.internal:5678',
            'http://localhost:8080',
            'http://host.docker.internal:8080',
            'http://127.0.0.1:5678',
            'http://127.0.0.1:8080',
            'http://wordpress:443',
            'https://wordpress',
            'https://n8n:5678',
            'https://n8n',
        ],
        [
            'http://n8n:5678',
            'http://n8n:5678',
            'http://wordpress:80',
            'http://wordpress:80',
            'http://n8n:5678',
            'http://wordpress:80',
            'http://wordpress:80',
            'http://wordpress:80',
            'http://n8n:5678',
            'http://n8n:5678',
        ],
        $url
    );

    return $internal_url;
}

/**
 * True when the request comes from another container (n8n, cron, etc.).
 */
function local_docker_is_internal_request(): bool
{
    $host = strtolower((string) ($_SERVER['HTTP_HOST'] ?? ''));
    if ($host === 'wordpress' || str_starts_with($host, 'wordpress:')) {
        return true;
    }

    $remote = (string) ($_SERVER['REMOTE_ADDR'] ?? '');
    if ($remote !== '' && preg_match('/^172\.(1[6-9]|2[0-9]|3[0-1])\./', $remote)) {
        return true;
    }

    return false;
}

/**
 * Rewrite localhost URLs inside REST payloads so n8n follow-up calls stay internal.
 *
 * @param mixed $value
 * @return mixed
 */
function local_docker_deep_rewrite_urls($value)
{
    if (is_string($value)) {
        return local_docker_rewrite_internal_url($value);
    }

    if (!is_array($value)) {
        return $value;
    }

    foreach ($value as $key => $item) {
        $value[$key] = local_docker_deep_rewrite_urls($item);
    }

    return $value;
}

// WooCommerce only accepts API key Basic Auth when is_ssl() is true (WP 7+ removed the old filter).
// Enable SSL only during REST authentication, then revert so permalinks stay HTTP.
add_filter('rest_authentication_errors', function ($result) {
    if (str_contains($_SERVER['REQUEST_URI'] ?? '', '/wp-json/')) {
        $_SERVER['HTTPS'] = 'on';
    }

    return $result;
}, 0);

add_filter('rest_authentication_errors', function ($result) {
    if (isset($_SERVER['HTTPS'])) {
        unset($_SERVER['HTTPS']);
    }

    return $result;
}, 100);

$uri = $_SERVER['REQUEST_URI'] ?? '';
$is_api_request = str_contains($uri, '/wp-json/')
    || str_contains($uri, '/wc-api/')
    || str_contains($uri, 'rest_route=');

if ($is_api_request) {
    // Apache often strips Authorization; n8n sends consumer key/secret as Basic Auth.
    if (empty($_SERVER['PHP_AUTH_USER'])) {
        $auth = $_SERVER['HTTP_AUTHORIZATION'] ?? $_SERVER['REDIRECT_HTTP_AUTHORIZATION'] ?? '';

        if (!$auth && function_exists('apache_request_headers')) {
            $headers = apache_request_headers();
            $auth = $headers['Authorization'] ?? $headers['authorization'] ?? '';
        }

        if (str_starts_with($auth, 'Basic ')) {
            $decoded = base64_decode(substr($auth, 6), true);

            if ($decoded && str_contains($decoded, ':')) {
                [$user, $pass] = explode(':', $decoded, 2);
                $_SERVER['PHP_AUTH_USER'] = $user;
                $_SERVER['PHP_AUTH_PW'] = $pass;
            }
        }
    }
}

// Prevent WordPress from treating proxied/local requests as HTTPS.
if (!empty($_SERVER['HTTP_X_FORWARDED_PROTO']) && $_SERVER['HTTP_X_FORWARDED_PROTO'] === 'https') {
    unset($_SERVER['HTTP_X_FORWARDED_PROTO']);
}

add_filter('pre_option_siteurl', function ($value) {
    if (is_string($value) && $value !== '') {
        return local_docker_force_http_url($value);
    }

    return 'http://localhost:8080';
});

add_filter('pre_option_home', function ($value) {
    if (is_string($value) && $value !== '') {
        return local_docker_force_http_url($value);
    }

    return 'http://localhost:8080';
});

add_filter('redirect_canonical', function ($redirect_url) {
    if ($redirect_url && str_starts_with((string) $redirect_url, 'https://')) {
        return local_docker_force_http_url((string) $redirect_url);
    }

    return $redirect_url;
}, 1);

add_filter('wp_redirect', function ($location) {
    if (is_string($location) && str_starts_with($location, 'https://')) {
        return local_docker_force_http_url($location);
    }

    return $location;
}, 1);

add_filter('woocommerce_force_ssl_checkout', '__return_false');
add_filter('wc_ajax_force_ssl_checkout', '__return_false');

foreach (['home_url', 'site_url', 'post_link', 'page_link', 'post_type_link', 'rest_url'] as $url_filter) {
    add_filter($url_filter, function ($url) {
        if (!is_string($url)) {
            return $url;
        }

        $url = local_docker_force_http_url($url);

        if (local_docker_is_internal_request()) {
            return local_docker_rewrite_internal_url($url);
        }

        return $url;
    }, 999);
}

add_filter('rest_pre_echo_response', function ($result, $server, $request) {
    if (!local_docker_is_internal_request()) {
        return $result;
    }

    return local_docker_deep_rewrite_urls($result);
}, 10, 3);

add_action('init', function () {
    static $bootstrapped = false;

    if ($bootstrapped) {
        return;
    }

    $bootstrapped = true;
    $needs_flush = false;

    foreach (['siteurl', 'home'] as $option) {
        $current = get_option($option);

        if (is_string($current) && str_starts_with($current, 'https://')) {
            update_option($option, local_docker_force_http_url($current));
        }
    }

    if (get_option('permalink_structure') === '') {
        update_option('permalink_structure', '/%postname%/');
        $needs_flush = true;
    }

    $htaccess = ABSPATH . '.htaccess';
    $contents = is_readable($htaccess) ? (string) file_get_contents($htaccess) : '';

    if (!str_contains($contents, 'RewriteEngine On')) {
        require_once ABSPATH . 'wp-admin/includes/misc.php';

        insert_with_markers(
            $htaccess,
            'WordPress',
            [
                '<IfModule mod_rewrite.c>',
                'RewriteEngine On',
                'RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]',
                'RewriteBase /',
                'RewriteRule ^index\.php$ - [L]',
                'RewriteCond %{REQUEST_FILENAME} !-f',
                'RewriteCond %{REQUEST_FILENAME} !-d',
                'RewriteRule . /index.php [L]',
                '</IfModule>',
            ]
        );
        $needs_flush = true;
    }

    if ($needs_flush) {
        flush_rewrite_rules(false);
    }
}, 1);

add_action('woocommerce_init', function () {
    if (get_option('woocommerce_api_enabled') !== 'yes') {
        update_option('woocommerce_api_enabled', 'yes');
    }
});

add_filter('pre_http_request', function ($preempt, $parsed_args, $url) {
    static $rewriting = false;

    if ($rewriting) {
        return $preempt;
    }

    $internal_url = local_docker_rewrite_internal_url($url);

    if ($internal_url === $url) {
        return $preempt;
    }

    $rewriting = true;
    $parsed_args['sslverify'] = false;
    $response = wp_remote_request($internal_url, $parsed_args);
    $rewriting = false;

    return $response;
}, 10, 3);

add_filter('http_request_args', function ($args, $url) {
    $internal_url = local_docker_rewrite_internal_url($url);

    if ($internal_url !== $url) {
        $args['sslverify'] = false;
    }

    $host = (string) parse_url($url, PHP_URL_HOST);

    if (in_array($host, ['localhost', '127.0.0.1', 'wordpress', 'n8n', 'host.docker.internal'], true)) {
        $args['sslverify'] = false;
        $args['reject_unsafe_urls'] = false;
    }

    return $args;
}, 10, 2);

add_filter('woocommerce_webhook_http_args', function ($http_args) {
    $http_args['timeout'] = 30;
    $http_args['sslverify'] = false;
    $http_args['reject_unsafe_urls'] = false;

    return $http_args;
});
