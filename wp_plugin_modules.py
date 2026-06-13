#!/usr/bin/env python3
"""Extended plugin-focused slide modules for WordPress Management course."""
from wp_slide_framework import (
    slide_section, slide_content, slide_two_col, slide_bullets,
    slide_diagram, slide_workshop, slide_summary, callout, esc,
)

PLUGIN_TITLES = [
    "Plugin Install & Config",      # 16
    "Rank Math Deep Dive",          # 17
    "Yoast SEO Deep Dive",          # 18
    "Security Plugins",             # 19
    "Backup Plugins",               # 20
    "Cache & Speed Plugins",        # 21
    "Forms & CRM Plugins",          # 22
    "WooCommerce Extensions",       # 23
    "API & Automation Integrations", # 24
]

PLUGIN_TOC = [
    "Module 16 — Installing & Configuring Plugins (Hands-On)",
    "Module 17 — Rank Math: Setup, Usage & Integrations",
    "Module 18 — Yoast SEO: Setup, Usage & Rank Math vs Yoast",
    "Module 19 — Wordfence, Solid Security & Hardening Plugins",
    "Module 20 — UpdraftPlus, WPvivid & Backup Plugin Usage",
    "Module 21 — LiteSpeed Cache, WP Rocket & Performance Plugins",
    "Module 22 — WPForms, Fluent Forms & CRM Integrations",
    "Module 23 — WooCommerce Extension Plugins Ecosystem",
    "Module 24 — Plugin API Integrations: Webhooks, Zapier & n8n",
]


def expanded_module_6_slides(m, mt, n):
    """Extra slides to append inside Module 6."""
    return [
        slide_content(m, "How to Install Plugins — 4 Methods", """
<ol class="steps">
<li><strong>Plugin Directory</strong> — Plugins → Add New → search → Install → Activate</li>
<li><strong>Upload ZIP</strong> — Add New → Upload Plugin (premium/purchased plugins)</li>
<li><strong>FTP/SFTP</strong> — extract to <code>/wp-content/plugins/plugin-folder/</code></li>
<li><strong>WP-CLI</strong> — <code>wp plugin install wordfence --activate</code></li>
</ol>
<div class="callout"><strong>Rule</strong>Only install from WordPress.org, official vendor sites, or trusted marketplaces (Envato, WooCommerce.com). Never nulled/cracked plugins.</div>
""", mt, n()),
        slide_diagram(m, "Plugin Lifecycle on Your Site", """
  DISCOVER → EVALUATE → INSTALL → ACTIVATE → CONFIGURE → INTEGRATE → MONITOR → UPDATE
      │          │          │         │           │            │          │         │
   Research   Reviews    ZIP/repo   Enable    Settings    Connect    Logs    Staging
   needs      + compat   upload     hooks     wizard      CRM/API    audit   first
""", [
            "Document every plugin in your inventory BEFORE activation",
            "Configure immediately after activate — defaults are rarely optimal",
            "Set calendar reminder for update review every Tuesday",
        ], mt, n()),
        slide_two_col(m, "Activate vs Deactivate vs Delete",
                      "Deactivate", [
                          "Plugin code stays on server",
                          "Settings often preserved in DB",
                          "Use for conflict testing",
                          "Safe rollback during debug",
                          "Reactivate restores most settings",
                      ],
                      "Delete", [
                          "Removes plugin files completely",
                          "May leave orphan DB tables/options",
                          "Use Uninstall hook if plugin provides it",
                          "Always backup before delete",
                          "Check Site Health after removal",
                      ], mt, n()),
        slide_content(m, "Plugin Settings Screens — What to Expect", """
<ul>
<li><strong>Top-level menu</strong> — Rank Math, WooCommerce, Wordfence add sidebar items</li>
<li><strong>Settings submenus</strong> — General, Advanced, Integrations tabs</li>
<li><strong>Setup wizards</strong> — run fully on first install (Rank Math, Yoast, Wordfence)</li>
<li><strong>Metaboxes in editor</strong> — SEO, custom fields appear below content</li>
<li><strong>Tools → Site Health</strong> — shows plugin-related warnings</li>
</ul>
<div class="callout callout-tip"><strong>Manager Habit</strong>Screenshot each plugin's final settings page → paste into client documentation folder.</div>
""", mt, n()),
        slide_bullets(m, "Troubleshooting Plugin Conflicts", [
            "<strong>White screen (WSOD)</strong> — rename plugin folder via FTP to disable all",
            "<strong>Binary search</strong> — deactivate half of plugins, test, repeat",
            "<strong>Health Check plugin</strong> — troubleshoot mode (disable all plugins for your session only)",
            "<strong>Enable WP_DEBUG</strong> — staging only: log errors to debug.log",
            "<strong>PHP error log</strong> — hosting panel shows fatal error + plugin name",
            "<strong>Rollback</strong> — restore backup OR use WP Rollback plugin",
        ], mt, n()),
        slide_content(m, "Plugin License & Premium Key Management", """
<table class="data"><tr><th>Plugin Type</th><th>License Location</th><th>Manager Action</th></tr>
<tr><td>Freemium (Rank Math Pro)</td><td>Plugin → Connect account</td><td>Store license in client vault</td></tr>
<tr><td>Annual (WP Rocket)</td><td>Settings → License key field</td><td>Track renewal date in spreadsheet</td></tr>
<tr><td>WooCommerce.com</td><td>WooCommerce → Extensions</td><td>One key per site or subscription</td></tr>
<tr><td>Envato</td><td>Envato Market plugin</td><td>Link buyer account once</td></tr>
</table>
<ul>
<li>Never share license keys in Slack/email — use 1Password, Bitwarden</li>
<li>Expired license = no updates = security risk</li>
</ul>
""", mt, n()),
    ]


def module_16():
    m, mt = 16, PLUGIN_TITLES[0]
    sn = [0]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(16, "Installing & Configuring Plugins",
                      "Hands-on: search, install, activate, configure, and verify every essential plugin."),
        slide_bullets(m, "Before You Install Anything", [
            "<strong>Define the job</strong> — \"I need contact forms\" not \"I'll try 5 form plugins\"",
            "<strong>Check compatibility</strong> — PHP version, WP version on plugin page",
            "<strong>Read Active installs</strong> — 50K+ minimum for critical functions",
            "<strong>Staging first</strong> — never test unknown plugins on live client site",
            "<strong>One plugin per job</strong> — two SEO plugins = conflict guaranteed",
        ], mt, n()),
        slide_content(m, "Step-by-Step: Install from WordPress Directory", """
<ol class="steps">
<li>Login → <strong>Plugins → Add New Plugin</strong></li>
<li>Search exact name: \"Rank Math SEO\"</li>
<li>Click <strong>Install Now</strong> → wait for success message</li>
<li>Click <strong>Activate</strong></li>
<li>Follow setup wizard — do NOT skip</li>
<li>Visit plugin settings → verify green/connected status</li>
<li>Add to plugin inventory spreadsheet</li>
</ol>
""", mt, n()),
        slide_content(m, "Step-by-Step: Upload Premium Plugin ZIP", """
<ol class="steps">
<li>Download ZIP from vendor (WP Rocket, ACF Pro, Gravity Forms)</li>
<li>Plugins → Add New → <strong>Upload Plugin</strong></li>
<li>Choose file → Install Now → Activate</li>
<li>Enter license key in plugin settings</li>
<li>Confirm updates appear in Dashboard → Updates</li>
</ol>
<div class="callout callout-warn"><strong>Common Error</strong>\"Package could not be installed\" — you uploaded a theme ZIP or unzipped folder. Must be .zip of plugin root.</div>
""", mt, n()),
        slide_diagram(m, "Post-Install Configuration Checklist", """
  ┌─────────────────────────────────────────────────────────┐
  │  AFTER EVERY PLUGIN INSTALL                              │
  ├─────────────────────────────────────────────────────────┤
  │  ☐  Setup wizard completed                               │
  │  ☐  License connected (if premium)                       │
  │  ☐  Test core site pages still load                      │
  │  ☐  Test checkout/forms if WooCommerce/forms plugin      │
  │  ☐  Screenshot settings → client docs                    │
  │  ☐  Add to inventory: name, version, purpose, renewal    │
  │  ☐  Schedule first update review                         │
  └─────────────────────────────────────────────────────────┘
""", [], mt, n()),
        slide_workshop(m, "Workshop: Install Your Core Plugin Stack", [
            "Install Rank Math (or Yoast) — complete wizard",
            "Install UpdraftPlus — connect remote storage (Google Drive)",
            "Install Wordfence OR Solid Security — enable 2FA",
            "Install WPForms OR Fluent Forms — create test form",
            "Install Redirection — add one 301 redirect",
            "Fill plugin inventory spreadsheet for all 5 plugins",
        ], "5 plugins installed, configured, documented in inventory sheet", mt, n()),
        slide_summary(m, [
            "Install plugins via directory, upload, FTP, or WP-CLI",
            "Complete setup wizards and license activation immediately",
            "Verify site functionality after every install",
            "Document all plugins in a centralized inventory",
        ], mt, n()),
    ]


def module_17():
    m, mt = 17, PLUGIN_TITLES[1]
    sn = [0]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(17, "Rank Math — Setup, Usage & Integrations",
                      "Configure Rank Math from wizard to daily post optimization."),
        slide_bullets(m, "Rank Math Setup Wizard — Step by Step", [
            "<strong>Step 1:</strong> Start wizard → choose site type (business/blog/shop)",
            "<strong>Step 2:</strong> Connect Google Search Console + Analytics (optional)",
            "<strong>Step 3:</strong> Sitemap — enable post, page, category sitemaps",
            "<strong>Step 4:</strong> Schema — Organization on homepage, Article on posts",
            "<strong>Step 5:</strong> Role Manager — limit SEO settings to Editors+",
            "<strong>Step 6:</strong> 404 + Redirection module — enable monitor",
        ], mt, n()),
        slide_two_col(m, "Rank Math — Key Settings Screens",
                      "General Settings", [
                          "Links → strip category base (optional)",
                          "Breadcrumbs → enable + shortcode",
                          "Images → add missing alt attributes auto",
                          "Others → noindex empty categories/tags",
                          "Watch for duplicate SEO plugins!",
                      ],
                      "Titles & Meta", [
                          "Homepage title + description template",
                          "Post title: %title% %sep% %sitename%",
                          "Noindex: archives, search, paginated",
                          "Social → Facebook + Twitter OG tags",
                          "Product schema if WooCommerce active",
                      ], mt, n()),
        slide_content(m, "Using Rank Math in the Post Editor", """
<ul>
<li><strong>Focus keyword</strong> — enter primary keyword; follow traffic light checklist</li>
<li><strong>Snippet preview</strong> — edit SEO title and meta description</li>
<li><strong>Schema type</strong> — Article, FAQ, HowTo, Product per post</li>
<li><strong>Internal links</strong> — Rank Math suggests link opportunities</li>
<li><strong>FAQ block</strong> — add FAQ schema directly in content</li>
</ul>
<div class="callout callout-tip"><strong>Daily usage</strong>Every publish: keyword → title → meta → schema → internal link. 2 minutes per post.</div>
""", mt, n()),
        slide_content(m, "Rank Math Integrations", """
<table class="data"><tr><th>Integration</th><th>How to Connect</th><th>Benefit</th></tr>
<tr><td>Google Search Console</td><td>Rank Math → General → Search Console → Connect</td><td>Index status in WP admin</td></tr>
<tr><td>Google Analytics</td><td>Connect GA4 property</td><td>Traffic in dashboard module</td></tr>
<tr><td>Elementor / Divi</td><td>Auto-detected</td><td>SEO panel in page builders</td></tr>
<tr><td>WooCommerce</td><td>Enable product schema module</td><td>Rich product snippets</td></tr>
<tr><td>Redirection</td><td>Built-in 404 monitor</td><td>Fix broken links in admin</td></tr>
<tr><td>Instant Indexing</td><td>IndexNow API key</td><td>Faster Bing/Yandex indexing</td></tr>
</table>
""", mt, n()),
        slide_workshop(m, "Workshop: Rank Math End-to-End", [
            "Run Rank Math setup wizard completely",
            "Connect Search Console (or manual verification)",
            "Configure title templates for posts and pages",
            "Optimize 3 existing posts using Rank Math checklist",
            "Enable sitemap → submit URL in Google Search Console",
            "Enable 404 monitor → fix one broken link",
        ], "Rank Math configured + 3 optimized posts + sitemap submitted", mt, n()),
        slide_summary(m, [
            "Complete Rank Math wizard with schema and sitemap",
            "Use editor metabox for every published post",
            "Connect GSC and Analytics for in-dashboard reporting",
            "Enable redirection and 404 monitoring modules",
        ], mt, n()),
    ]


def module_18():
    m, mt = 18, PLUGIN_TITLES[2]
    sn = [0]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(18, "Yoast SEO — Setup & Comparison",
                      "Configure Yoast SEO and understand when to choose Yoast vs Rank Math."),
        slide_bullets(m, "Yoast SEO Configuration Workflow", [
            "<strong>General → Features</strong> — enable/disable SEO analysis, readability",
            "<strong>Search Appearance</strong> — title templates per content type",
            "<strong>Social</strong> — Facebook + X default image and site name",
            "<strong>Tools</strong> — import from other SEO plugins",
            "<strong>Integrations</strong> — Semrush, Wincher, Elementor, WooCommerce",
            "<strong>Workouts</strong> — guided orphan content + cornerstone setup",
        ], mt, n()),
        slide_content(m, "Yoast Metabox — Daily Usage", """
<ul>
<li><strong>Focus keyphrase</strong> — Yoast analyzes keyword in title, intro, meta, URL</li>
<li><strong>SEO title + slug + meta</strong> — Google preview snippet editor</li>
<li><strong>Readability analysis</strong> — sentence length, passive voice, subheadings</li>
<li><strong>Schema</strong> — Yoast Premium: advanced schema graph</li>
<li><strong>Cornerstone content</strong> — mark pillar pages for internal linking priority</li>
</ul>
""", mt, n()),
        slide_two_col(m, "Rank Math vs Yoast — Manager's Guide",
                      "Choose Rank Math if", [
                          "Want more free features (redirects, 404)",
                          "Prefer modern UI + setup wizard",
                          "Need built-in keyword tracking (GSC)",
                          "Running WooCommerce + need product SEO",
                          "Agency managing many sites (free multi-site)",
                      ],
                      "Choose Yoast if", [
                          "Client already trained on Yoast",
                          "Need Yoast Premium readability + support",
                          "Using Semrush/Wincher integration heavily",
                          "Enterprise requires Yoast-specific SOPs",
                          "Legacy site with years of Yoast data",
                      ], mt, n()),
        slide_content(m, "Migrating Between SEO Plugins", """
<ol class="steps">
<li>Export settings from old plugin (if available)</li>
<li>Install new plugin — use import tool (Rank Math imports Yoast data)</li>
<li>Verify title/meta on 10 sample posts</li>
<li>Check sitemap URL changed → resubmit in GSC</li>
<li>Deactivate old plugin — NEVER run both simultaneously</li>
<li>Monitor GSC for indexing errors for 2 weeks</li>
</ol>
<div class="callout callout-warn"><strong>Critical</strong>Running Rank Math + Yoast together breaks meta output — duplicate titles, schema errors.</div>
""", mt, n()),
        slide_workshop(m, "Workshop: Yoast OR Rank Math Mastery", [
            "Pick ONE SEO plugin — install and complete setup",
            "Configure search appearance for posts, pages, products",
            "Optimize homepage SEO title and meta description",
            "Mark one page as Cornerstone (Yoast) or Pillar (Rank Math)",
            "Submit sitemap and verify in Search Console",
        ], "Fully configured SEO plugin + homepage + 2 posts optimized", mt, n()),
        slide_summary(m, [
            "Configure Yoast Search Appearance and social settings",
            "Use focus keyphrase workflow on every post",
            "Choose one SEO plugin — never two",
            "Migrate SEO data safely when switching plugins",
        ], mt, n()),
    ]


def module_19():
    m, mt = 19, PLUGIN_TITLES[3]
    sn = [0]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(19, "Security Plugins — Wordfence & Solid Security",
                      "Install, configure, and operate security plugins day-to-day."),
        slide_content(m, "Wordfence — Initial Setup", """
<ol class="steps">
<li>Install Wordfence → enter email for security alerts</li>
<li>Run first scan — review critical/high/medium findings</li>
<li>Enable <strong>Web Application Firewall (WAF)</strong> — Learning Mode 1 week</li>
<li>Switch WAF to <strong>Enabled and Protecting</strong></li>
<li>Enable <strong>Two-Factor Authentication</strong> for Administrator role</li>
<li>Configure login security: limit attempts, block admin username</li>
</ol>
""", mt, n()),
        slide_two_col(m, "Wordfence Daily & Weekly Tasks",
                      "Daily (automated)", [
                          "Email alert on lockout/block",
                          "Failed login threshold triggered",
                          "File change detection notification",
                          "Review Wordfence dashboard widget",
                      ],
                      "Weekly (5 min)", [
                          "Run full malware scan",
                          "Review blocked IP list",
                          "Check for plugin/theme vulnerabilities",
                          "Verify firewall status green",
                          "Update Wordfence before other plugins",
                      ], mt, n()),
        slide_content(m, "Solid Security (iThemes) — Key Features", """
<ul>
<li><strong>Security checklist</strong> — guided hardening score 0–100%</li>
<li><strong>404 detection</strong> — ban IPs scanning for vulnerabilities</li>
<li><strong>Two-factor</strong> — TOTP app, email, backup codes</li>
<li><strong>Password requirements</strong> — enforce strong passwords by role</li>
<li><strong>Database backups</strong> — scheduled DB export (use with UpdraftPlus)</li>
<li><strong>User logging</strong> — track admin actions for client audits</li>
</ul>
<div class="callout"><strong>Pick one</strong>Wordfence OR Solid Security as primary — not both firewalls simultaneously.</div>
""", mt, n()),
        slide_bullets(m, "Security Plugin Integrations", [
            "<strong>reCAPTCHA</strong> — Wordfence login + WPForms integration",
            "<strong>Central management</strong> — Wordfence Central for multi-site dashboard",
            "<strong>Slack/email alerts</strong> — configure in plugin notification settings",
            "<strong>Hide wp-login</strong> — Solid Security custom login URL feature",
            "<strong>Sucuri alternative</strong> — cloud WAF if host doesn't include one",
        ], mt, n()),
        slide_workshop(m, "Workshop: Secure Site with Security Plugin", [
            "Install Wordfence OR Solid Security",
            "Complete security setup wizard / checklist to 80%+",
            "Enable 2FA on your admin account — test login",
            "Run first scan — fix or document every critical issue",
            "Configure email alerts for lockouts and scan results",
        ], "Security plugin active + 2FA working + scan report screenshot", mt, n()),
        slide_summary(m, [
            "Configure WAF, scan, and login protection on day one",
            "Enable 2FA for all administrator accounts",
            "Run weekly scans and review alerts promptly",
            "Use one primary security plugin per site",
        ], mt, n()),
    ]


def module_20():
    m, mt = 20, PLUGIN_TITLES[4]
    sn = [0]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(20, "Backup Plugins — UpdraftPlus & WPvivid",
                      "Configure automated backups, remote storage, and restore procedures."),
        slide_content(m, "UpdraftPlus — Complete Configuration", """
<ol class="steps">
<li>Settings → UpdraftPlus → choose schedule: <strong>Daily DB + Weekly files</strong></li>
<li>Retain: 4 backups minimum (adjust for storage costs)</li>
<li>Remote storage: <strong>Google Drive, S3, Dropbox</strong> — authorize OAuth</li>
<li>Select components: plugins, themes, uploads, others, database</li>
<li>Run <strong>Backup Now</strong> — verify file appears in remote storage</li>
<li>Test restore on staging — non-negotiable quarterly drill</li>
</ol>
""", mt, n()),
        slide_two_col(m, "UpdraftPlus vs WPvivid",
                      "UpdraftPlus", [
                          "Most popular — 3M+ installs",
                          "Granular component selection",
                          "Migrator add-on for site moves",
                          "Incremental backups (Premium)",
                          "Works on budget shared hosting",
                      ],
                      "WPvivid", [
                          "One-click staging + migration",
                          "Clean UI for beginners",
                          "Auto backup before updates",
                          "White-label for agencies",
                          "Good for client handoff packages",
                      ], mt, n()),
        slide_content(m, "Backup Plugin Integrations", """
<ul>
<li><strong>Google Drive / S3</strong> — off-site storage (required for real backups)</li>
<li><strong>Email reports</strong> — backup success/failure notification</li>
<li><strong>UpdraftCentral</strong> — manage backups of 10+ sites from one dashboard</li>
<li><strong>Before-update hook</strong> — WPvivid auto-backup before plugin updates</li>
<li><strong>n8n integration</strong> — webhook on backup complete → Slack alert</li>
</ul>
<div class="callout callout-warn"><strong>Backup on server only ≠ backup</strong>If hosting account is compromised, local backups are lost too.</div>
""", mt, n()),
        slide_diagram(m, "Restore Workflow", """
  INCIDENT DETECTED
        │
        ▼
  ┌─────────────┐     NO      ┌──────────────┐
  │ Recent      │────────────▶│ Full restore │
  │ backup OK?  │             │ from remote  │
  └──────┬──────┘             └──────────────┘
         │ YES
         ▼
  ┌─────────────┐
  │ Restore DB  │  OR  Restore files only  OR  Selective plugin rollback
  │ only        │
  └─────────────┘
        │
        ▼
  Verify site → document incident → update client
""", [], mt, n()),
        slide_workshop(m, "Workshop: Backup & Restore Drill", [
            "Configure UpdraftPlus or WPvivid with Google Drive",
            "Schedule daily database + weekly full backup",
            "Run manual backup — confirm file in cloud storage",
            "Clone site to staging subdomain",
            "Restore backup on staging — verify homepage + admin login",
        ], "Backup config screenshot + successful restore test on staging", mt, n()),
        slide_summary(m, [
            "Configure scheduled backups with remote off-site storage",
            "Test restore quarterly on staging environment",
            "Choose UpdraftPlus or WPvivid based on agency needs",
            "Integrate backup alerts into monitoring workflow",
        ], mt, n()),
    ]


def module_21():
    m, mt = 21, PLUGIN_TITLES[5]
    sn = [0]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(21, "Cache & Performance Plugins",
                      "LiteSpeed Cache, WP Rocket — configure without breaking WooCommerce."),
        slide_bullets(m, "Cache Plugin Selection Guide", [
            "<strong>LiteSpeed Cache</strong> — free, best if host runs LiteSpeed server",
            "<strong>WP Rocket</strong> — premium, works everywhere, easiest UI",
            "<strong>W3 Total Cache</strong> — powerful but complex — expert users only",
            "<strong>SiteGround Optimizer</strong> — only on SiteGround hosting",
            "<strong>Rule:</strong> ONE cache plugin only — conflicts cause random bugs",
        ], mt, n()),
        slide_content(m, "WP Rocket — Recommended Settings", """
<table class="data"><tr><th>Setting</th><th>Recommendation</th></tr>
<tr><td>Cache mobile separately</td><td>ON if mobile layout differs</td></tr>
<tr><td>Minify CSS/JS</td><td>ON — test checkout after enabling</td></tr>
<tr><td>LazyLoad images</td><td>ON — exclude above-fold hero if CLS issues</td></tr>
<tr><td>Delay JavaScript</td><td>ON for blogs — OFF or exclude for WooCommerce cart</td></tr>
<tr><td>CDN</td><td>Enable if using Cloudflare/Bunny CDN</td></tr>
<tr><td>Exclude URLs</td><td>/cart/, /checkout/, /my-account/, /wp-admin/</td></tr>
</table>
""", mt, n()),
        slide_content(m, "LiteSpeed Cache — Key Configuration", """
<ul>
<li><strong>General → Enable Cache</strong> — ON after confirming LiteSpeed server</li>
<li><strong>Cache → Exclude</strong> — WooCommerce cart, checkout, logged-in users</li>
<li><strong>Page Optimization</strong> — CSS/JS minify + combine (test carefully)</li>
<li><strong>Image Optimization</strong> — WebP generation + lazy load</li>
<li><strong>Crawler</strong> — warm cache automatically on schedule</li>
<li><strong>Integration:</strong> QUIC.cloud CDN for non-LiteSpeed hosts (limited free tier)</li>
</ul>
""", mt, n()),
        slide_two_col(m, "Cache + Other Plugin Compatibility",
                      "Safe combinations", [
                          "WP Rocket + ShortPixel (images)",
                          "LiteSpeed + Rank Math (no conflict)",
                          "WP Rocket + Wordfence (exclude admin)",
                          "Cache + Object Cache Pro (Redis)",
                      ],
                      "Purge cache when", [
                          "Publishing new post or page",
                          "Updating WooCommerce product",
                          "Changing menus or widgets",
                          "Plugin or theme update",
                          "Client reports \"old version\" showing",
                      ], mt, n()),
        slide_workshop(m, "Workshop: Configure Cache Plugin", [
            "Install WP Rocket OR LiteSpeed Cache (match your host)",
            "Enable page cache + browser cache",
            "Add WooCommerce URL exclusions",
            "Run PageSpeed before/after — record scores",
            "Publish test post — verify cache purges automatically",
            "Break checkout intentionally — fix exclusion rules",
        ], "Cache configured + PageSpeed improvement doc + exclusion list", mt, n()),
        slide_summary(m, [
            "Install exactly one cache plugin per site",
            "Exclude cart, checkout, and account pages always",
            "Test WooCommerce checkout after every optimization change",
            "Purge cache after content and plugin updates",
        ], mt, n()),
    ]


def module_22():
    m, mt = 22, PLUGIN_TITLES[6]
    sn = [0]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(22, "Forms & CRM Plugin Integrations",
                      "WPForms, Fluent Forms — connect leads to email, CRM, and automation."),
        slide_content(m, "WPForms — Build & Configure a Contact Form", """
<ol class="steps">
<li>WPForms → Add New → choose Simple Contact Form template</li>
<li>Customize fields: name, email, message, phone (optional)</li>
<li>Enable <strong>anti-spam</strong> — hCaptcha or Akismet</li>
<li>Notifications → send to client@business.com</li>
<li>Confirmations → thank you message or redirect URL</li>
<li>Embed via block: \"WPForms\" → select form → publish page</li>
<li>Submit test entry — verify email received in 60 seconds</li>
</ol>
""", mt, n()),
        slide_two_col(m, "WPForms vs Fluent Forms",
                      "WPForms", [
                          "Easiest drag-drop for beginners",
                          "Large addon library (PayPal, Stripe)",
                          "Conversational forms addon",
                          "Entry storage in WP admin",
                          "Marketing: Mailchimp, Constant Contact",
                      ],
                      "Fluent Forms", [
                          "More free features (conditional logic)",
                          "Built-in CRM (FluentCRM integration)",
                          "Payment without addon (Stripe/PayPal)",
                          "Webhook native — great for n8n",
                          "Better for complex multi-step forms",
                      ], mt, n()),
        slide_content(m, "CRM & Email Marketing Integrations", """
<table class="data"><tr><th>Service</th><th>Plugin Connection</th><th>Use Case</th></tr>
<tr><td>Mailchimp</td><td>WPForms / Fluent Forms addon</td><td>Newsletter signup → audience tag</td></tr>
<tr><td>HubSpot</td><td>HubSpot plugin OR form webhook</td><td>Lead capture → CRM pipeline</td></tr>
<tr><td>FluentCRM</td><td>Native Fluent Forms integration</td><td>All-in-one WP CRM stack</td></tr>
<tr><td>Google Sheets</td><td>Uncanny Automator / n8n webhook</td><td>Simple lead log spreadsheet</td></tr>
<tr><td>Slack</td><td>Form webhook → n8n → Slack channel</td><td>Instant lead notification</td></tr>
<tr><td>Zapier</td><td>WPForms Zapier addon</td><td>Connect 5000+ apps no-code</td></tr>
</table>
""", mt, n()),
        slide_diagram(m, "Form Submission → CRM Flow", """
  VISITOR fills form on WordPress
            │
            ▼
  ┌─────────────────┐
  │ WPForms / Fluent│
  └────────┬────────┘
           │
     ┌─────┴─────┬─────────────┬──────────────┐
     ▼           ▼             ▼              ▼
  Email       Webhook      Mailchimp      Entry DB
  notify      → n8n        tag add        (WP admin)
              → HubSpot
              → Slack
""", [
            "Always test form after cache plugin changes",
            "GDPR: add privacy checkbox for EU sites",
        ], mt, n()),
        slide_workshop(m, "Workshop: Form + Integration Pipeline", [
            "Create contact form with WPForms or Fluent Forms",
            "Configure email notification to your inbox",
            "Add webhook URL (use webhook.site for testing)",
            "Connect Mailchimp OR log entries to Google Sheets via n8n",
            "Embed form on Contact page — submit 3 test entries",
        ], "Live form + working email + webhook log screenshot", mt, n()),
        slide_summary(m, [
            "Build forms with WPForms or Fluent Forms templates",
            "Configure spam protection and email notifications",
            "Connect forms to CRM, email, and automation tools",
            "Test form delivery after every site change",
        ], mt, n()),
    ]


def module_23():
    m, mt = 23, PLUGIN_TITLES[7]
    sn = [0]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(23, "WooCommerce Extension Plugins",
                      "Payments, shipping, subscriptions, and essential WooCommerce add-ons."),
        slide_bullets(m, "Essential WooCommerce Extensions", [
            "<strong>WooCommerce Payments / Stripe</strong> — credit card processing",
            "<strong>PayPal Payments</strong> — alternative checkout option",
            "<strong>Table Rate Shipping</strong> — complex shipping rules by weight/zone",
            "<strong>PDF Invoices</strong> — automatic invoice emails to customers",
            "<strong>Product Add-Ons</strong> — customization options (gift wrap, engraving)",
            "<strong>Subscriptions</strong> — recurring billing for memberships",
        ], mt, n()),
        slide_content(m, "Stripe / WooCommerce Payments Setup", """
<ol class="steps">
<li>WooCommerce → Settings → Payments → Enable Stripe or WooPayments</li>
<li>Click <strong>Connect</strong> or enter API keys (test mode first)</li>
<li>Test card: 4242 4242 4242 4242 — any future date, any CVC</li>
<li>Place test order → verify order status + payment in Stripe dashboard</li>
<li>Switch to <strong>Live mode</strong> only after client approval</li>
<li>Enable Apple Pay / Google Pay if supported by gateway</li>
</ol>
<div class="callout callout-warn"><strong>Cache conflict</strong>Exclude checkout and cart URLs from cache plugin or payments fail silently.</div>
""", mt, n()),
        slide_two_col(m, "Shipping & Tax Extensions",
                      "Shipping plugins", [
                          "Table Rate Shipping — rules by weight/price",
                          "ShipStation — fulfillment integration",
                          "Local Pickup Plus — store pickup slots",
                          "Flexible Shipping — zone-based rates",
                          "Print shipping labels via extensions",
                      ],
                      "Tax plugins", [
                          "WooCommerce Tax (free, automated US)",
                          "TaxJar — multi-state + international",
                          "VAT MOSS for EU digital goods",
                          "Avalara — enterprise tax compliance",
                          "Configure nexus in WooCommerce settings",
                      ], mt, n()),
        slide_content(m, "WooCommerce Plugin Integrations", """
<ul>
<li><strong>Rank Math / Yoast</strong> — product schema, Open Graph for products</li>
<li><strong>Mailchimp for WooCommerce</strong> — sync customers to email lists</li>
<li><strong>Google Listings & Ads</strong> — sync products to Google Merchant Center</li>
<li><strong>Facebook for WooCommerce</strong> — product catalog sync</li>
<li><strong>Points and Rewards</strong> — loyalty program plugin</li>
<li><strong>Advanced Coupons</strong> — BOGO, store credit, auto-apply rules</li>
</ul>
""", mt, n()),
        slide_workshop(m, "Workshop: WooCommerce Extension Stack", [
            "Enable Stripe or WooPayments in test mode",
            "Install PDF Invoices — customize invoice template",
            "Configure Table Rate or Flat Rate shipping zone",
            "Connect one marketing integration (Mailchimp or Google Listings)",
            "Complete test purchase end-to-end — verify all emails",
        ], "Test order screenshot + 3 configured Woo extensions documented", mt, n()),
        slide_summary(m, [
            "Configure payment gateways in test mode before going live",
            "Install shipping and tax extensions matching business model",
            "Integrate WooCommerce with email marketing and product feeds",
            "Document every Woo extension in plugin inventory",
        ], mt, n()),
    ]


def module_24():
    m, mt = 24, PLUGIN_TITLES[8]
    sn = [0]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(24, "Plugin API Integrations",
                      "REST API, webhooks, Zapier, Uncanny Automator, and n8n — connect everything."),
        slide_diagram(m, "WordPress Integration Architecture", """
  ┌──────────────────────────────────────────────────────────────┐
  │                    WORDPRESS PLUGINS                          │
  │  WPForms ──webhook──▶ n8n ──▶ Slack / Sheets / HubSpot       │
  │  WooCommerce ──REST──▶ Mobile app / fulfillment API           │
  │  Rank Math ──GSC API──▶ Index data in dashboard               │
  │  UpdraftPlus ──hook──▶ Backup complete → email alert          │
  │  Uncanny Automator ──trigger──▶ WP action → external service  │
  └──────────────────────────────────────────────────────────────┘
         ▲                              ▲
         │                              │
   Application Password            Zapier / Make.com
   (REST API auth)                 (no-code connectors)
""", [], mt, n()),
        slide_content(m, "REST API + Application Passwords", """
<ol class="steps">
<li>Users → Your Profile → <strong>Application Passwords</strong></li>
<li>Name: \"n8n integration\" → Generate → copy password (shown once)</li>
<li>Test endpoint: <code>GET /wp-json/wp/v2/posts?per_page=1</code></li>
<li>Auth: Basic — username + application password (not login password)</li>
<li>Use in n8n WordPress node, custom scripts, mobile apps</li>
</ol>
<div class="callout"><strong>Security</strong>Revoke application passwords when automation is decommissioned.</div>
""", mt, n()),
        slide_two_col(m, "No-Code Integration Tools",
                      "Uncanny Automator", [
                          "WordPress-native triggers + actions",
                          "\"User submits form → enroll in course\"",
                          "500+ integrations inside WP admin",
                          "No external server needed",
                          "Great for non-technical managers",
                      ],
                      "Zapier / Make.com", [
                          "Connect WP to 5000+ external apps",
                          "WPForms → Zapier → Google Sheets row",
                          "New order → Slack + accounting software",
                          "Requires webhook or plugin bridge",
                          "Usage-based pricing at scale",
                      ], mt, n()),
        slide_content(m, "High-Value n8n + Plugin Workflows", """
<table class="data"><tr><th>Trigger (Plugin)</th><th>n8n Action</th><th>Business Value</th></tr>
<tr><td>WPForms webhook</td><td>Add row to Google Sheets + Slack alert</td><td>Instant lead response</td></tr>
<tr><td>WooCommerce new order</td><td>Send to fulfillment API</td><td>Automated shipping</td></tr>
<tr><td>Wordfence lockout</td><td>Email admin + log incident</td><td>Security monitoring</td></tr>
<tr><td>UpdraftPlus backup done</td><td>Confirm in client report sheet</td><td>Compliance proof</td></tr>
<tr><td>New post published</td><td>Post to LinkedIn/X via API</td><td>Social distribution</td></tr>
<tr><td>404 spike (Rank Math)</td><td>Create Trello fix card</td><td>Proactive SEO maintenance</td></tr>
</table>
""", mt, n()),
        slide_bullets(m, "Webhook Setup — Generic Steps", [
            "<strong>1.</strong> In form/plugin settings → find Webhooks or Integrations tab",
            "<strong>2.</strong> Copy n8n Webhook URL (POST method)",
            "<strong>3.</strong> Map fields: email, name, message → JSON payload",
            "<strong>4.</strong> Test submission → check n8n execution log",
            "<strong>5.</strong> Add error handling node → email if workflow fails",
            "<strong>6.</strong> Document webhook URL in client integration doc",
        ], mt, n()),
        slide_workshop(m, "Workshop: Build 3 Plugin Integrations", [
            "Create Application Password — test REST API with browser or Postman",
            "WPForms/Fluent webhook → n8n → Google Sheets row on submit",
            "Schedule n8n workflow: daily check Site Health via REST",
            "Optional: Uncanny Automator recipe — form → welcome email",
            "Document all integrations in client tech stack diagram",
        ], "3 working integrations + exported n8n workflow JSON", mt, n()),
        slide_summary(m, [
            "Use Application Passwords for secure REST API access",
            "Connect forms and WooCommerce to external tools via webhooks",
            "Choose Uncanny Automator (in-WP) or n8n/Zapier (external)",
            "Document and test every integration after site changes",
        ], mt, n()),
    ]


def get_all_plugin_modules():
    """Return all plugin-focused module slide lists."""
    return [
        module_16(), module_17(), module_18(), module_19(), module_20(),
        module_21(), module_22(), module_23(), module_24(),
    ]


def get_plugin_toc():
    return PLUGIN_TOC


def get_expanded_module_6(m, mt, n):
    return expanded_module_6_slides(m, mt, n)
