<?php
/**
 * Local Docker networking and WooCommerce REST API fixes.
 *
 * Handles:
 * - Container URL rewriting for webhooks
 * - REST API auth over HTTP (required for n8n WooCommerce node)
 * - Pretty permalinks + Apache rewrite rules (required for /wp-json/)
 * - WooCommerce REST API enabled by default
 */

// WooCommerce only accepts API key auth when is_ssl() is true. WP 7+ no longer filters is_ssl().
$uri = $_SERVER['REQUEST_URI'] ?? '';
if (str_contains($uri, '/wp-json/')) {
    $_SERVER['HTTPS'] = 'on';

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

add_action('init', function () {
    static $bootstrapped = false;

    if ($bootstrapped) {
        return;
    }

    $bootstrapped = true;
    $needs_flush = false;

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

    $internal_url = str_replace(
        [
            'http://localhost:5678',
            'https://localhost:5678',
            'http://host.docker.internal:5678',
            'https://host.docker.internal:5678',
            'http://localhost:8080',
            'https://localhost:8080',
            'http://host.docker.internal:8080',
            'https://host.docker.internal:8080',
        ],
        [
            'http://n8n:5678',
            'http://n8n:5678',
            'http://n8n:5678',
            'http://n8n:5678',
            'http://wordpress:80',
            'http://wordpress:80',
            'http://wordpress:80',
            'http://wordpress:80',
        ],
        $url
    );

    if ($internal_url === $url) {
        return $preempt;
    }

    $rewriting = true;
    $response = wp_remote_request($internal_url, $parsed_args);
    $rewriting = false;

    return $response;
}, 10, 3);

add_filter('woocommerce_webhook_http_args', function ($http_args) {
    $http_args['timeout'] = 30;
    $http_args['sslverify'] = false;

    return $http_args;
});
