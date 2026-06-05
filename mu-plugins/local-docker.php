<?php
/**
 * Local Docker networking fixes for WooCommerce webhooks and WP HTTP requests.
 */

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
