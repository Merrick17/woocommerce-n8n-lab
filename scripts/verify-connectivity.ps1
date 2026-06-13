#!/usr/bin/env pwsh
# Verify n8n <-> WordPress connectivity after stack is up.
$ErrorActionPreference = "Stop"

function Wait-HttpOk {
    param([string]$Url, [int]$MaxAttempts = 60)
    for ($i = 1; $i -le $MaxAttempts; $i++) {
        try {
            $r = Invoke-WebRequest -Uri $Url -UseBasicParsing -TimeoutSec 5
            if ($r.StatusCode -ge 200 -and $r.StatusCode -lt 500) { return $true }
        } catch {}
        Start-Sleep -Seconds 2
    }
    return $false
}

Write-Host "Waiting for WordPress..."
if (-not (Wait-HttpOk "http://localhost:8080")) {
    Write-Error "WordPress not reachable on http://localhost:8080"
}

Write-Host "Waiting for n8n..."
if (-not (Wait-HttpOk "http://localhost:5678")) {
    Write-Error "n8n not reachable on http://localhost:5678"
}

Write-Host "`n--- n8n -> WordPress (REST API) ---"
docker exec n8n wget -qO- "http://wordpress:80/wp-json/" 2>&1 | Select-Object -First 3

Write-Host "`n--- WordPress -> n8n (internal network) ---"
docker exec woocommerce_wp curl -fsS -o /dev/null -w "HTTP %{http_code}`n" "http://n8n:5678/" 2>&1

Write-Host "`n--- WooCommerce API keys (if WooCommerce active) ---"
docker exec woocommerce_wp php -r "
require '/var/www/html/wp-load.php';
if (!function_exists('get_option')) { echo 'WP not ready'; exit(1); }
\$k = get_option('local_docker_n8n_consumer_key');
\$s = get_option('local_docker_n8n_consumer_secret');
if (\$k && \$s) {
    echo \"Consumer Key: \$k\nConsumer Secret: \$s\n\";
    echo \"WooCommerce URL for n8n: http://wordpress:80\n\";
} else {
    echo \"Keys not created yet — install and activate WooCommerce, then re-run.\n\";
}
" 2>&1

Write-Host "`nStack verification complete."
