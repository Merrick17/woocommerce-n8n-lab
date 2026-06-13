#!/bin/sh
# Idempotent bootstrap: WordPress + WooCommerce auto-install.
set -e

WP="wp --path=/var/www/html --allow-root --skip-plugins --skip-themes"

log() {
  printf '[bootstrap] %s\n' "$*"
}

wait_http() {
  url="$1"
  max="${2:-90}"
  attempt=0

  while [ "$attempt" -lt "$max" ]; do
    if wget -q --spider "$url" 2>/dev/null || curl -fsS -o /dev/null "$url" 2>/dev/null; then
      return 0
    fi
    attempt=$((attempt + 1))
    sleep 2
  done

  log "Timed out waiting for ${url}"
  return 1
}

bootstrap_wordpress() {
  log "Waiting for WordPress..."
  wait_http "http://wordpress/"

  if ! $WP core is-installed >/dev/null 2>&1; then
    log "Installing WordPress..."
    $WP core install \
      --url="http://localhost:8080" \
      --title="WooCommerce n8n Lab" \
      --admin_user=admin \
      --admin_password=admin123 \
      --admin_email=admin@local.test \
      --skip-email
  else
    log "WordPress already installed"
  fi

  log "Ensuring WooCommerce is installed and active..."
  if ! $WP plugin is-installed woocommerce >/dev/null 2>&1; then
    $WP plugin install woocommerce --activate
  elif ! $WP plugin is-active woocommerce >/dev/null 2>&1; then
    $WP plugin activate woocommerce
  fi

  $WP option update woocommerce_onboarding_profile '{"skipped":true}' --format=json >/dev/null 2>&1 || true
  $WP option update woocommerce_task_list_hidden yes >/dev/null 2>&1 || true
  $WP option update woocommerce_extended_task_list_hidden yes >/dev/null 2>&1 || true

  log "Bootstrapping mu-plugin hooks (API keys + webhook)..."
  curl -fsS "http://wordpress/wp-json/" >/dev/null 2>&1 || true
  $WP eval 'if (function_exists("WC")) { do_action("woocommerce_init"); }' >/dev/null 2>&1 || true
}

main() {
  bootstrap_wordpress
  log "WordPress side ready."
  log "  WordPress -> http://localhost:8080 (admin / admin123)"
  log "  n8n       -> http://localhost:5678 (admin / admin123)"
  log "  Webhook   -> http://localhost:5678/webhook/wc-order-created"
}

main "$@"
