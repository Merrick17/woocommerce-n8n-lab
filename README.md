# WooCommerce + n8n Local Lab

A Docker Compose stack for running **WordPress**, **WooCommerce**, and **n8n** locally, with networking fixes so webhooks work between containers.

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- Ports **8080** (WordPress) and **5678** (n8n) available on your machine

## Project structure

```
woocommerce-n8n-lab/
├── docker-compose.yml          # Stack definition
├── php-custom.ini              # PHP memory & upload limits for WordPress
├── mu-plugins/
│   └── local-docker.php        # Docker networking + WooCommerce REST API bootstrap
└── README.md
```

All three config files are required. `docker-compose.yml` alone is not enough — the mu-plugin handles webhook URL rewriting.

## Quick start

```powershell
cd woocommerce-n8n-lab
docker compose up -d
```

Verify four containers are running:

| Container | Service |
|---|---|
| `woocommerce_db` | MySQL 8 |
| `woocommerce_wp` | WordPress |
| `woocommerce_wp_cron` | WP-Cron runner (every 60s) |
| `n8n` | n8n automation |

### Access URLs

| Service | URL | Credentials |
|---|---|---|
| WordPress | http://localhost:8080 | Set during first-time install |
| n8n | http://localhost:5678 | `admin` / `admin123` |

### First-time WordPress setup

1. Open http://localhost:8080
2. Complete the WordPress installation wizard
3. Install and activate the **WooCommerce** plugin
4. Finish the WooCommerce setup wizard

## Connecting WooCommerce to n8n

### WooCommerce → n8n (outgoing webhooks)

1. In **n8n**, create a workflow with a **Webhook** trigger node
2. **Activate** the workflow (toggle in the top-right)
3. Copy the production webhook URL, e.g. `http://localhost:5678/webhook/abc-123`
4. In **WooCommerce → Settings → Advanced → Webhooks → Add webhook**:
   - **Name:** any label
   - **Status:** Active
   - **Topic:** e.g. Order created
   - **Delivery URL:** paste the n8n URL as-is (`http://localhost:5678/...` is fine)
   - **Secret:** optional, match it in n8n if you validate signatures
5. Save the webhook

### n8n → WooCommerce (REST API / WooCommerce node)

Create API keys in **WooCommerce → Settings → Advanced → REST API → Add key** (Read/Write, assigned to your admin user).

In n8n, create **WooCommerce API** credentials:

| Field | Value |
|---|---|
| WooCommerce URL | `http://wordpress:80` |
| Consumer Key | from WooCommerce (starts with `ck_`) |
| Consumer Secret | from WooCommerce (starts with `cs_`) |
| Include Credentials in Query | **ON** (recommended for Docker) |

Important:

- Always include the protocol: `http://wordpress:80` — not `wordpress:80` or `host.docker.internal:8080`
- Paste keys with WooCommerce’s **Copy** button (no trailing spaces)
- The credential **Test** button may fail even when the node works — try **Product → Get All → Execute step**

For HTTP Request nodes, use the Docker-internal base URL — **not** `localhost:8080`:

```
{{ $env.WOOCOMMERCE_URL }}/wp-json/wc/v3/orders
{{ $env.WOOCOMMERCE_URL }}/wp-json/wc/v3/products
```

The mu-plugin auto-enables pretty permalinks, Apache rewrite rules, and the WooCommerce REST API so `/wp-json/` works out of the box after `docker compose up`.

## How local Docker networking works

Inside Docker, `localhost` refers to the container itself — not your PC and not other services. This stack solves that in two ways:

### 1. Mu-plugin bootstrap (`mu-plugins/local-docker.php`)

On each WordPress load, the mu-plugin:

- Enables **pretty permalinks** and writes **Apache rewrite rules** (fixes `/wp-json/` 404)
- Enables the **WooCommerce REST API** if it was turned off
- Allows **API key auth over HTTP** so n8n can connect without HTTPS
- Rewrites `localhost` URLs to Docker service names for outbound requests:

When WordPress makes an HTTP request, `localhost` URLs are rewritten to Docker service names:

| Configured URL | Actually called |
|---|---|
| `http://localhost:5678/...` | `http://n8n:5678/...` |
| `http://localhost:8080/...` | `http://wordpress:80/...` |

You can paste n8n webhook URLs directly from the n8n UI into WooCommerce.

### 2. WP-Cron sidecar (`wp-cron` service)

WooCommerce queues webhook delivery via Action Scheduler, which depends on WP-Cron. The built-in cron loopback fails in Docker (WordPress tries to reach `localhost:8080` from inside the container). This stack:

- Sets `DISABLE_WP_CRON` in WordPress
- Runs a sidecar that hits `http://wordpress/wp-cron.php` every 60 seconds

Webhooks are delivered within about a minute of the triggering event.

### Internal vs browser URLs

| From your browser | Between containers |
|---|---|
| `http://localhost:8080` | `http://wordpress:80` |
| `http://localhost:5678` | `http://n8n:5678` |

## Useful commands

```powershell
# Start the stack
docker compose up -d

# Stop the stack
docker compose down

# Stop and remove all data (fresh start)
docker compose down -v

# View logs
docker compose logs -f wordpress
docker compose logs -f n8n
docker compose logs -f wp-cron

# Manually trigger WP-Cron (don't wait 60s)
docker exec woocommerce_wp curl -s "http://127.0.0.1/wp-cron.php?doing_wp_cron"
```

## Testing webhooks

1. Ensure the n8n workflow is **Active**
2. Create a test order in WooCommerce (or trigger the webhook topic you configured)
3. Wait up to 60 seconds
4. Check:
   - **n8n → Executions** — workflow should have run
   - **WooCommerce → Settings → Advanced → Webhooks → Delivery logs** — should show HTTP 200

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Webhook never fires | n8n workflow not active | Toggle workflow to **Active** |
| Delivery log shows connection error | Missing mu-plugin | Ensure `mu-plugins/local-docker.php` exists and restart: `docker compose up -d` |
| Webhook delayed ~60s | Normal — cron runs every minute | Wait, or run the manual cron command above |
| n8n can't reach WooCommerce | Using `localhost:8080` in n8n | WooCommerce URL: `http://wordpress:80` |
| `Unsupported protocol host.docker.internal:` | Missing `http://` in n8n URL | Use `http://wordpress:80` |
| n8n auth failed (401) | Trailing space in secret, or REST API off | Re-paste keys; enable **Include Credentials in Query**; mu-plugin enables REST API automatically |
| `/wp-json/` returns 404 | Plain permalinks / missing rewrite rules | Restart stack — mu-plugin fixes this on boot |
| Port already in use | Another app on 8080 or 5678 | Change ports in `docker-compose.yml` (e.g. `"8081:80"`) |
| Containers won't start | Docker Desktop not running | Start Docker Desktop, then `docker compose up -d` |

## Configuration reference

### WordPress memory

- PHP: `1024M` via `php-custom.ini`
- WordPress: `1024M` via `WP_MEMORY_LIMIT` / `WP_MAX_MEMORY_LIMIT`

### Database credentials (local dev only)

| Setting | Value |
|---|---|
| Database | `wordpress` |
| User | `wp_user` |
| Password | `wp_pass` |
| Root password | `root` |

### n8n environment variables

| Variable | Value | Usage |
|---|---|---|
| `WEBHOOK_URL` | `http://localhost:5678/` | Webhook URLs shown in n8n UI |
| `WORDPRESS_URL` | `http://wordpress:80` | `{{ $env.WORDPRESS_URL }}` in workflows |
| `WOOCOMMERCE_URL` | `http://wordpress:80` | `{{ $env.WOOCOMMERCE_URL }}` in workflows |
