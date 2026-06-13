#!/usr/bin/env python3
"""WordPress Management course — all slide content."""
from wp_slide_framework import (
    slide_cover, slide_toc, slide_section, slide_content, slide_two_col,
    slide_bullets, slide_diagram, slide_workshop, slide_summary, callout,
    icon_cards, wrap_deck, esc,
)
from wp_plugin_modules import (
    get_all_plugin_modules, get_plugin_toc, get_expanded_module_6,
)

MOD_TITLES = [
    "Admin & Dashboard",
    "Content Management",
    "Media Library",
    "Users & Roles",
    "Themes & Design",
    "Plugin Management",
    "WooCommerce Ops",
    "Security",
    "Backups & Staging",
    "Performance",
    "SEO Management",
    "n8n Automation",
    "AI for WordPress",
    "Client Management",
    "Capstone Project",
]

TOC = [
    "Module 1 — WordPress Admin & Dashboard Mastery",
    "Module 2 — Content Management (Posts, Pages, Blocks)",
    "Module 3 — Media Library & Digital Assets",
    "Module 4 — Users, Roles & Permissions",
    "Module 5 — Themes, Customizer & Site Identity",
    "Module 6 — Plugin Management & Maintenance (Expanded)",
    *get_plugin_toc(),
    "Module 7 — WooCommerce Store Management",
    "Module 8 — Security Hardening & Monitoring",
    "Module 9 — Backups, Staging & Migrations",
    "Module 10 — Performance, Caching & Hosting",
    "Module 11 — SEO Management on WordPress",
    "Module 12 — n8n Automation for WordPress",
    "Module 13 — AI Tools for WordPress Management",
    "Module 14 — Client Site Management & Reporting",
    "Module 15 — Capstone: Managed WordPress Site",
    "Appendix — Checklists, Glossary & Certification",
]


def module_1():
    m, mt = 1, MOD_TITLES[0]
    sn = [0]
    def n():
        sn[0] += 1
        return sn[0]

    slides = [
        slide_section(1, "WordPress Admin & Dashboard Mastery",
                      "Navigate, configure, and control your WordPress site like a professional site manager."),
        slide_bullets(m, "What Is WordPress Management?", [
            "<strong>Site manager</strong> — day-to-day operations, not just publishing",
            "<strong>Admin dashboard</strong> — command center for content, users, settings",
            "<strong>Self-hosted vs WordPress.com</strong> — full control lives on self-hosted",
            "<strong>Your role</strong> — keep site secure, fast, updated, and usable",
        ], mt, n(), "WordPress powers 43%+ of the web. Managing it well is a high-value skill."),
        slide_diagram(m, "WordPress Architecture at a Glance", """
┌─────────────────────────────────────────────────────┐
│                  WORDPRESS STACK                     │
├─────────────┬─────────────┬─────────────┬─────────────┤
│  Browser    │  wp-admin   │  Database   │  Server     │
│  (Visitor)  │  (Manager)  │  (MySQL)    │  (PHP/Host) │
└──────┬──────┴──────┬──────┴──────┬──────┴──────┬──────┘
       │             │             │             │
       ▼             ▼             ▼             ▼
   Front-end     Dashboard     Posts/Users    Apache/Nginx
   Theme View    Settings      Options        + PHP 8.x
""", [
            "Core files live in /wp-admin/ and /wp-includes/",
            "Your content lives in the database + /wp-content/uploads/",
            "Never edit core — use themes, plugins, child themes",
        ], mt, n()),
        slide_bullets(m, "The Admin Dashboard Tour", [
            "<strong>Dashboard home</strong> — At a Glance, Activity, Quick Draft",
            "<strong>Posts / Pages</strong> — all published and draft content",
            "<strong>Media</strong> — images, PDFs, videos in the library",
            "<strong>Appearance</strong> — themes, menus, widgets, customizer",
            "<strong>Plugins & Tools</strong> — extensions, imports, health",
            "<strong>Settings</strong> — site title, permalinks, reading, privacy",
        ], mt, n()),
        slide_two_col(m, "Essential Settings to Configure First",
                      "General", [
                          "Site Title & Tagline",
                          "WordPress Address (URL)",
                          "Site Address (URL)",
                          "Timezone & Date Format",
                          "Admin Email (monitor this!)",
                      ],
                      "Reading & Permalinks", [
                          "Homepage: static page vs blog",
                          "Posts page assignment",
                          "Permalink: Post name (/%postname%/)",
                          "Discourage search engines (staging only!)",
                          "Privacy policy page link",
                      ], mt, n()),
        slide_bullets(m, "Screen Options & Admin UX", [
            "<strong>Screen Options</strong> — show/hide columns and panels per screen",
            "<strong>Help tabs</strong> — contextual docs on every admin page",
            "<strong>Admin bar</strong> — front-end quick edit when logged in",
            "<strong>Keyboard shortcuts</strong> — Editor: Ctrl+K (link), Ctrl+S (save draft)",
            "<strong>Collapse menu</strong> — more workspace on small screens",
        ], mt, n(), callout("callout-tip", "Pro Tip", "Create a 'Site Launch Checklist' doc and tick off each Settings screen before going live.")),
        slide_content(m, "Site Health & WordPress Updates", """
<p class="lead">Tools → Site Health shows critical issues before they become outages.</p>
<ul>
<li><strong>PHP version</strong> — use 8.1+ for security and speed</li>
<li><strong>HTTPS</strong> — required; fix mixed-content warnings</li>
<li><strong>Background updates</strong> — enable minor core auto-updates</li>
<li><strong>Plugin/theme updates</strong> — weekly review schedule</li>
</ul>
<div class="callout callout-warn"><strong>Never update everything at once on production</strong>Test updates on staging first. One change at a time makes rollback easy.</div>
""", mt, n()),
        slide_workshop(m, "Workshop: Configure a Fresh WordPress Install", [
            "Install WordPress locally (Local WP, Docker, or hosting panel)",
            "Complete General, Reading, Permalink, and Discussion settings",
            "Set timezone, site title, and static homepage",
            "Run Site Health — fix all red and orange items",
            "Create an admin checklist document with screenshots",
        ], "Settings audit PDF with 10 configured items documented", mt, n()),
        slide_summary(m, [
            "Navigate the full WordPress admin confidently",
            "Configure essential settings before publishing",
            "Understand the WordPress file + database architecture",
            "Use Site Health as your weekly management dashboard",
            "Follow a staged update process for core, themes, and plugins",
        ], mt, n()),
    ]
    return slides


def module_2():
    m, mt = 2, MOD_TITLES[1]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(2, "Content Management", "Posts, pages, the Block Editor, and editorial workflows."),
        slide_bullets(m, "Posts vs Pages — When to Use Each", [
            "<strong>Posts</strong> — dated, blog/news, categories & tags, RSS feeds",
            "<strong>Pages</strong> — static: About, Contact, Services, legal pages",
            "<strong>Hierarchy</strong> — pages support parent/child (e.g. Services → Web Design)",
            "<strong>Templates</strong> — page templates control layout (full-width, landing)",
            "<strong>Revisions</strong> — both store edit history; restore anytime",
        ], mt, n()),
        slide_content(m, "The Block Editor (Gutenberg)", """
<p class="lead">WordPress 6.x uses blocks for all content — think LEGO for pages.</p>
""" + icon_cards([
            ("📝", "Paragraph", "Text, headings, lists"),
            ("🖼️", "Image", "Media with alt text"),
            ("📦", "Group / Row", "Layout containers"),
            ("🔘", "Buttons", "CTAs with links"),
            ("❓", "FAQ / Schema", "SEO-friendly blocks"),
            ("📋", "Columns", "Multi-column layouts"),
        ]) + """
<ul>
<li><strong>Patterns</strong> — pre-built block layouts (hero, pricing, team)</li>
<li><strong>Reusable blocks</strong> — sync CTAs across pages from one source</li>
<li><strong>Full Site Editing (FSE)</strong> — block themes edit headers/footers too</li>
</ul>
""", mt, n()),
        slide_two_col(m, "Categories, Tags & Taxonomies",
                      "Categories", [
                          "Broad topics — hierarchical",
                          "Example: Recipes → Desserts",
                          "One primary category per post (best practice)",
                          "Appear in URL structures optionally",
                          "Use 5–15 categories max on most sites",
                      ],
                      "Tags", [
                          "Specific descriptors — flat",
                          "Example: gluten-free, 30-minute",
                          "Don't duplicate categories as tags",
                          "Avoid tag bloat (hurts UX and crawl)",
                          "Merge or noindex tag archives if unused",
                      ], mt, n()),
        slide_bullets(m, "Editorial Workflow Best Practices", [
            "<strong>Draft → Review → Publish</strong> — use User Roles (Module 4)",
            "<strong>Scheduled posts</strong> — plan content calendar in advance",
            "<strong>Sticky posts</strong> — pin important announcements",
            "<strong>Excerpt field</strong> — control archive/blog card text",
            "<strong>Featured image</strong> — required for every post (social + SEO)",
            "<strong>Slug editing</strong> — short, keyword-clear URLs before publish",
        ], mt, n()),
        slide_diagram(m, "Content Workflow Diagram", """
  IDEA → BRIEF → DRAFT → REVIEW → SCHEDULE → PUBLISH → PROMOTE
    │       │       │        │         │          │         │
    ▼       ▼       ▼        ▼         ▼          ▼         ▼
  Trello  Doc    WP      Editor    WP Cron    Live     Social/
  Sheet   Template Draft   QA      Queue      Site     Email
""", [
            "Document your workflow — clients expect consistency",
            "Use Editorial Calendar plugins for team visibility",
            "Never publish without preview on mobile",
        ], mt, n()),
        slide_content(m, "Bulk Management & Content Tools", """
<ul>
<li><strong>Posts → All Posts</strong> — bulk edit categories, status, author</li>
<li><strong>Quick Edit</strong> — inline title, slug, category changes</li>
<li><strong>Export/Import</strong> — Tools → Export for migrations</li>
<li><strong>Duplicate Post plugins</strong> — clone landing page templates fast</li>
<li><strong>Redirection plugin</strong> — manage URL changes when slugs update</li>
</ul>
<div class="callout"><strong>Case Study</strong>A marketing agency reduced publish time 40% using reusable block patterns for every client landing page.</div>
""", mt, n()),
        slide_workshop(m, "Workshop: Build a Complete Page from Blocks", [
            "Create a Services page with hero, 3-column features, testimonial, CTA",
            "Save the CTA as a Reusable Block",
            "Create a blog post with category, featured image, excerpt, internal link",
            "Schedule a post for next week",
            "Use Preview on desktop and mobile before publishing",
        ], "Published Services page + 1 scheduled blog post + reusable CTA block", mt, n()),
        slide_summary(m, [
            "Choose posts vs pages correctly for each content type",
            "Build layouts efficiently with blocks, patterns, and reusable blocks",
            "Manage categories and tags without creating SEO clutter",
            "Run a professional draft-review-publish workflow",
            "Use bulk tools for ongoing site maintenance",
        ], mt, n()),
    ]


def module_3():
    m, mt = 3, MOD_TITLES[2]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(3, "Media Library & Digital Assets", "Upload, organize, optimize, and deliver images and files professionally."),
        slide_bullets(m, "Media Library Fundamentals", [
            "<strong>Grid vs List view</strong> — toggle in Media → Library",
            "<strong>Attachment details</strong> — title, alt text, caption, description",
            "<strong>File types</strong> — JPG, PNG, WebP, SVG (careful), PDF, MP4",
            "<strong>Storage path</strong> — /wp-content/uploads/YEAR/MONTH/",
            "<strong>Max upload size</strong> — controlled by hosting PHP limits",
        ], mt, n()),
        slide_two_col(m, "Image Optimization for Managers",
                      "On Upload", [
                          "Resize before upload (max 2000px wide)",
                          "Use WebP via plugin (ShortPixel, Imagify)",
                          "Always fill Alt Text field",
                          "Descriptive filenames: blue-widget.jpg",
                          "Remove EXIF if privacy-sensitive",
                      ],
                      "Ongoing", [
                          "Bulk compress existing library quarterly",
                          "Delete unused media (Media Cleaner plugin)",
                          "Lazy load enabled (default in WP 5.5+)",
                          "CDN for media (Cloudflare, Bunny)",
                          "Regenerate thumbnails after theme change",
                      ], mt, n()),
        slide_bullets(m, "Alt Text, Captions & Accessibility", [
            "<strong>Alt text</strong> — describes image for screen readers + image SEO",
            "<strong>Good alt:</strong> \"Red leather handbag on white background\"",
            "<strong>Bad alt:</strong> \"IMG_4521\" or keyword stuffing",
            "<strong>Decorative images</strong> — leave alt empty (alt=\"\")",
            "<strong>Captions</strong> — visible text under image; optional but helpful",
        ], mt, n(), callout("callout-warn", "Common Mistake", "Uploading 5MB photos from a phone camera — slows entire site. Resize first.")),
        slide_content(m, "Organizing Media at Scale", """
<ul>
<li><strong>Media folders plugins</strong> — virtual folders (FileBird, Real Media Library)</li>
<li><strong>Categories for attachments</strong> — filter by client or campaign</li>
<li><strong>Featured images</strong> — set once, used in blog cards and social shares</li>
<li><strong>PDF management</strong> — link directly or embed with block</li>
<li><strong>Video</strong> — host on YouTube/Vimeo; embed (don't self-host large files)</li>
</ul>
<table class="data"><tr><th>Asset Type</th><th>Best Practice</th></tr>
<tr><td>Hero images</td><td>1920×1080 WebP, &lt;200KB</td></tr>
<tr><td>Blog featured</td><td>1200×630 (OG ratio), alt text required</td></tr>
<tr><td>Logos</td><td>SVG or PNG, Site Identity + media library</td></tr>
<tr><td>Icons</td><td>SVG sprite or icon font via theme</td></tr></table>
""", mt, n()),
        slide_workshop(m, "Workshop: Media Audit & Optimization", [
            "Audit 20 media items — fill missing alt text on all",
            "Install an image optimization plugin and compress library",
            "Rename 5 poorly named files (understanding URL impact)",
            "Create folder/category structure for one client scenario",
            "Measure page weight before/after with GTmetrix or PageSpeed",
        ], "Media audit spreadsheet: filename, alt, size, action taken", mt, n()),
        slide_summary(m, [
            "Manage the Media Library with consistent naming and alt text",
            "Optimize images on upload and in bulk",
            "Organize assets for multi-client or large sites",
            "Follow accessibility standards for all visual content",
            "Choose correct delivery strategy for video and PDFs",
        ], mt, n()),
    ]


def module_4():
    m, mt = 4, MOD_TITLES[3]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(4, "Users, Roles & Permissions", "Control who can do what — essential for teams and client sites."),
        slide_content(m, "WordPress User Roles Explained", """
<table class="data"><tr><th>Role</th><th>Can Do</th><th>Typical User</th></tr>
<tr><td><strong>Administrator</strong></td><td>Everything including plugins, themes, users</td><td>Site owner, lead dev</td></tr>
<tr><td><strong>Editor</strong></td><td>Publish/edit all posts & pages</td><td>Content manager</td></tr>
<tr><td><strong>Author</strong></td><td>Publish own posts only</td><td>Blog contributor</td></tr>
<tr><td><strong>Contributor</strong></td><td>Write but not publish</td><td>Guest writer</td></tr>
<tr><td><strong>Subscriber</strong></td><td>Read profile only</td><td>Membership sites</td></tr>
</table>
<p class="lead" style="margin-top:12px">Principle of least privilege — give minimum role needed.</p>
""", mt, n()),
        slide_bullets(m, "User Management Best Practices", [
            "<strong>Never share admin accounts</strong> — one user per person",
            "<strong>Strong passwords + 2FA</strong> — Wordfence, Solid Security, WP 2FA",
            "<strong>Remove inactive users</strong> — quarterly audit",
            "<strong>Application Passwords</strong> — for API/n8n integrations (not main password)",
            "<strong>Custom roles</strong> — Members, User Role Editor plugins",
        ], mt, n()),
        slide_diagram(m, "Team Permission Model", """
                    ┌─────────────┐
                    │   ADMIN     │  ← 1-2 people max
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌────────────┐  ┌────────────┐  ┌────────────┐
    │  EDITOR    │  │  SHOP MGR  │  │  DEVELOPER │
    │  (content) │  │ (WooCommerce)│ │ (staging) │
    └─────┬──────┘  └────────────┘  └────────────┘
          ▼
    ┌────────────┐
    │ AUTHOR /   │
    │ CONTRIBUTOR│
    └────────────┘
""", [
            "Document role assignments in client onboarding",
            "Shop Manager role for WooCommerce without full admin",
            "Never give clients Administrator unless they insist in writing",
        ], mt, n()),
        slide_workshop(m, "Workshop: Set Up a Team on WordPress", [
            "Create users: 1 Editor, 2 Authors, 1 Contributor",
            "Enable 2FA for Administrator account",
            "Test Contributor cannot publish — Editor approves",
            "Create Application Password for API test",
            "Document roles in a 1-page access policy",
        ], "Team access policy document + 4 configured user accounts", mt, n()),
        slide_summary(m, [
            "Assign WordPress roles using least-privilege principle",
            "Secure accounts with unique logins and 2FA",
            "Use Application Passwords for automation integrations",
            "Audit user list regularly on managed client sites",
        ], mt, n()),
    ]


def module_5():
    m, mt = 5, MOD_TITLES[4]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(5, "Themes, Customizer & Site Identity", "Control look, feel, and brand without breaking the site."),
        slide_bullets(m, "Choosing & Managing Themes", [
            "<strong>Active vs installed</strong> — only one theme active; keep default as fallback",
            "<strong>Block themes (FSE)</strong> — Site Editor for templates + styles",
            "<strong>Classic themes</strong> — Customizer + widget areas",
            "<strong>Child themes</strong> — safe place for CSS/custom functions",
            "<strong>Never edit parent theme</strong> — updates wipe custom code",
        ], mt, n()),
        slide_content(m, "Site Identity & Customizer", """
<ul>
<li><strong>Appearance → Customize</strong> — logo, site icon, colors, menus</li>
<li><strong>Site Icon</strong> — 512×512 favicon for browser tabs + mobile</li>
<li><strong>Menus</strong> — assign to header, footer, mobile locations</li>
<li><strong>Widgets</strong> — sidebar/footer blocks (classic themes)</li>
<li><strong>Additional CSS</strong> — small tweaks without child theme</li>
</ul>
<div class="callout callout-tip"><strong>Manager Tip</strong>Before switching themes, full backup + staging test. Theme changes affect layouts, widgets, and menus.</div>
""", mt, n()),
        slide_two_col(m, "Theme Maintenance",
                      "Do", [
                          "Read changelog before updating",
                          "Test on staging with real content",
                          "Keep parent + child theme updated",
                          "Document custom CSS in client file",
                          "Check mobile after every theme change",
                      ],
                      "Don't", [
                          "Install nulled/pirated themes",
                          "Activate 20 themes 'just in case'",
                          "Edit parent theme PHP files",
                          "Switch themes on Black Friday",
                          "Ignore deprecated theme warnings",
                      ], mt, n()),
        slide_workshop(m, "Workshop: Brand a WordPress Site", [
            "Upload logo and site icon in Customizer",
            "Configure primary menu with 5 items",
            "Apply brand colors via theme settings or Additional CSS",
            "Create child theme OR document Customizer changes",
            "Preview and screenshot desktop + mobile homepage",
        ], "Branded homepage screenshot + menu structure doc", mt, n()),
        slide_summary(m, [
            "Select themes based on speed, support, and FSE needs",
            "Configure Site Identity for professional branding",
            "Use child themes or Additional CSS for safe customization",
            "Follow staged process for theme updates",
        ], mt, n()),
    ]


def module_6():
    m, mt = 6, MOD_TITLES[5]
    sn = [0]
    def n(): sn[0] += 1; return sn[0]

    core = [
        slide_section(6, "Plugin Management & Maintenance", "Install, evaluate, update, integrate, and troubleshoot plugins safely."),
        slide_bullets(m, "The Plugin Ecosystem", [
            "<strong>60,000+ free plugins</strong> on WordPress.org repository",
            "<strong>Premium plugins</strong> — WooCommerce extensions, ACF Pro, WP Rocket",
            "<strong>Must-use (MU) plugins</strong> — auto-loaded from /wp-content/mu-plugins/",
            "<strong>Plugin conflicts</strong> — #1 cause of white-screen errors",
            "<strong>Less is more</strong> — audit quarterly, remove unused",
        ], mt, n()),
        slide_content(m, "Essential Plugin Stack for Managers", """
<table class="data"><tr><th>Category</th><th>Plugin</th><th>Daily Use</th></tr>
<tr><td>SEO</td><td>Rank Math / Yoast</td><td>Meta, sitemap, schema per post</td></tr>
<tr><td>Security</td><td>Wordfence / Solid Security</td><td>Scan, firewall, 2FA</td></tr>
<tr><td>Backup</td><td>UpdraftPlus / WPvivid</td><td>Scheduled remote backups</td></tr>
<tr><td>Cache</td><td>LiteSpeed / WP Rocket</td><td>Page speed, exclusions</td></tr>
<tr><td>Forms</td><td>WPForms / Fluent Forms</td><td>Leads → email/CRM</td></tr>
<tr><td>Redirect</td><td>Redirection / Rank Math</td><td>301s, 404 monitor</td></tr>
<tr><td>Automation</td><td>Uncanny Automator / n8n</td><td>Webhooks, REST API</td></tr>
</table>
<p class="lead">Modules 16–24 cover each plugin category hands-on.</p>
""", mt, n()),
        slide_diagram(m, "Safe Plugin Update Process", """
  1. BACKUP     ──▶  2. STAGING TEST  ──▶  3. PRODUCTION
       │                    │                      │
       ▼                    ▼                      ▼
  UpdraftPlus          Apply update           Apply ONE
  snapshot             Check critical         plugin update
                       pages + checkout       Monitor 24h
                       + forms                Rollback if needed
""", [
            "Never bulk-update 15 plugins on Friday afternoon",
            "Read changelog — breaking changes happen",
            "Keep a 'plugin inventory' spreadsheet per client",
        ], mt, n()),
        slide_bullets(m, "Evaluating Plugins Before Install", [
            "<strong>Active installs</strong> — 100K+ usually means stable",
            "<strong>Last updated</strong> — within 6 months preferred",
            "<strong>PHP compatibility</strong> — matches your server",
            "<strong>Support reviews</strong> — read 1-star reviews for patterns",
            "<strong>Performance impact</strong> — test with Query Monitor plugin",
        ], mt, n()),
    ]
    expanded = get_expanded_module_6(m, mt, n)
    tail = [
        slide_workshop(m, "Workshop: Plugin Audit & Cleanup", [
            "List all installed plugins with version and purpose",
            "Deactivate + delete 2 unused plugins",
            "Install and configure one essential plugin (backup or security)",
            "Run Site Health after changes",
            "Create plugin inventory spreadsheet template",
        ], "Plugin inventory sheet for a sample client site", mt, n()),
        slide_summary(m, [
            "Maintain a lean, documented plugin stack",
            "Install via directory, upload, FTP, or WP-CLI",
            "Follow backup → staging → production update workflow",
            "Troubleshoot conflicts with binary search method",
            "Continue to Modules 16–24 for hands-on plugin labs",
        ], mt, n()),
    ]
    return core + expanded + tail


def module_7():
    m, mt = 7, MOD_TITLES[6]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(7, "WooCommerce Store Management", "Run products, orders, payments, and store settings day-to-day."),
        slide_bullets(m, "WooCommerce Admin Overview", [
            "<strong>Products</strong> — simple, variable, grouped, virtual, downloadable",
            "<strong>Orders</strong> — processing, completed, refunded lifecycle",
            "<strong>Customers</strong> — accounts, order history, GDPR export",
            "<strong>Marketing</strong> — coupons, campaigns (with extensions)",
            "<strong>Reports</strong> — sales, stock, taxes, downloads",
            "<strong>Settings</strong> — store address, currency, shipping, payments",
        ], mt, n(), "WooCommerce turns WordPress into a full e-commerce platform."),
        slide_two_col(m, "Product Management",
                      "Simple Products", [
                          "Single price and SKU",
                          "Inventory tracking on/off",
                          "Weight/dimensions for shipping",
                          "Product image gallery",
                          "Short + long description",
                      ],
                      "Variable Products", [
                          "Attributes: size, color",
                          "Variation-specific SKU/price",
                          "Variation images",
                          "Stock per variation",
                          "Default form values",
                      ], mt, n()),
        slide_content(m, "Orders, Payments & Shipping", """
<ul>
<li><strong>Order statuses</strong> — Pending → Processing → Completed (know each trigger)</li>
<li><strong>Payment gateways</strong> — Stripe, PayPal, WooPayments — test in sandbox</li>
<li><strong>Shipping zones</strong> — flat rate, free shipping, local pickup by region</li>
<li><strong>Tax settings</strong> — WooCommerce Tax or TaxJar for compliance</li>
<li><strong>Emails</strong> — WooCommerce → Settings → Emails (customize templates)</li>
</ul>
<div class="callout"><strong>Case Study</strong>Store lost $12K/month from broken checkout after plugin update. Fix: staging test + monitor order notifications daily.</div>
""", mt, n()),
        slide_bullets(m, "WooCommerce Maintenance Tasks", [
            "<strong>Daily</strong> — check new orders, failed payments, low stock alerts",
            "<strong>Weekly</strong> — review abandoned carts, update product info",
            "<strong>Monthly</strong> — test checkout flow, review shipping rates",
            "<strong>Quarterly</strong> — extension updates on staging, clean expired coupons",
            "<strong>HPOS</strong> — High-Performance Order Storage (enable when ready)",
        ], mt, n()),
        slide_workshop(m, "Workshop: Launch a Mini WooCommerce Store", [
            "Install WooCommerce and run setup wizard",
            "Add 5 products (2 variable with attributes)",
            "Configure shipping zone and payment gateway (test mode)",
            "Place test order — walk through full order lifecycle",
            "Customize one transactional email template",
        ], "Working test store with 5 products + completed test order", mt, n()),
        slide_summary(m, [
            "Manage products, orders, and customers in WooCommerce admin",
            "Configure payments, shipping, and tax correctly",
            "Run daily/weekly/monthly store maintenance routines",
            "Test checkout after every plugin or theme update",
        ], mt, n()),
    ]


def module_8():
    m, mt = 8, MOD_TITLES[7]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(8, "Security Hardening & Monitoring", "Protect WordPress sites from attacks, malware, and breaches."),
        slide_bullets(m, "WordPress Security Threats", [
            "<strong>Brute force</strong> — automated login attempts on /wp-login.php",
            "<strong>Plugin vulnerabilities</strong> — outdated code = entry point",
            "<strong>Nulled plugins</strong> — often contain backdoors",
            "<strong>XML-RPC attacks</strong> — disable if not needed",
            "<strong>File permission issues</strong> — wp-config.php must not be public",
        ], mt, n()),
        slide_content(m, "Security Hardening Checklist", """
<ul class="checklist">
<li>Change default 'admin' username</li>
<li>Enforce strong passwords + 2FA for all admins</li>
<li>Limit login attempts (Wordfence, Limit Login Attempts)</li>
<li>Hide wp-login or use custom login URL</li>
<li>Disable file editing: DISALLOW_FILE_EDIT in wp-config</li>
<li>Set correct file permissions (755 dirs, 644 files)</li>
<li>Use HTTPS everywhere — force SSL in settings</li>
<li>Keep core, themes, plugins updated</li>
<li>Regular malware scans (Wordfence, Sucuri)</li>
<li>Off-site backups (Module 9)</li>
</ul>
""", mt, n()),
        slide_two_col(m, "wp-config.php Security Constants",
                      "Add These", [
                          "DISALLOW_FILE_EDIT — true",
                          "FORCE_SSL_ADMIN — true",
                          "WP_DEBUG — false on production",
                          "Unique authentication keys (api.wordpress.org/secret-key)",
                          "Custom table prefix (on new installs)",
                      ],
                      "Monitor These", [
                          "Failed login alerts",
                          "File change detection",
                          "Google Search Console security issues",
                          "SSL certificate expiry",
                          "Admin user creation events",
                          "Unexpected plugin activations",
                      ], mt, n()),
        slide_workshop(m, "Workshop: Harden a WordPress Site", [
            "Install security plugin and run full scan",
            "Enable 2FA for administrator accounts",
            "Add DISALLOW_FILE_EDIT to wp-config.php",
            "Configure login rate limiting",
            "Document security baseline in client handoff doc",
        ], "Security audit checklist — all items green", mt, n()),
        slide_summary(m, [
            "Identify common WordPress attack vectors",
            "Implement hardening checklist on every managed site",
            "Configure monitoring and alert workflows",
            "Respond to security incidents with backup rollback plan",
        ], mt, n()),
    ]


def module_9():
    m, mt = 9, MOD_TITLES[8]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(9, "Backups, Staging & Migrations", "Never lose a site — backup, clone, and move WordPress safely."),
        slide_diagram(m, "The 3-2-1 Backup Rule for WordPress", """
  3 copies of data  │  2 different media  │  1 off-site
  
  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
  │ Production  │   │ Local NAS   │   │ Cloud S3    │
  │ (live site) │   │ or USB      │   │ (UpdraftPlus)│
  └─────────────┘   └─────────────┘   └─────────────┘
         ▲                  ▲                  ▲
         └──────────────────┴──────────────────┘
                    Automated daily backup
""", [
            "Test restores quarterly — backup untested = no backup",
            "Include database AND wp-content/uploads",
            "Store backups off-server (hosting fire = lost backups too)",
        ], mt, n()),
        slide_bullets(m, "Staging Environments", [
            "<strong>Why staging</strong> — test updates without breaking live site",
            "<strong>Tools</strong> — WP Staging, InstaWP, hosting staging (SiteGround, Kinsta)",
            "<strong>Push/pull</strong> — sync DB + files carefully (don't overwrite orders!)",
            "<strong>Search-replace</strong> — update URLs when cloning (Better Search Replace)",
            "<strong>Discourage indexing</strong> — staging must block Google",
        ], mt, n()),
        slide_content(m, "Migration Workflow", """
<ol class="steps">
<li>Export content or full backup from source site</li>
<li>Set up fresh WordPress on destination hosting</li>
<li>Import files + database</li>
<li>Run URL search-replace (http→https, old domain→new)</li>
<li>Regenerate permalinks (Settings → Permalinks → Save)</li>
<li>Test all pages, forms, checkout, and redirects</li>
<li>Update DNS and monitor Search Console</li>
</ol>
<div class="callout callout-warn"><strong>Critical</strong>Always create 301 redirect map BEFORE changing URLs. Traffic loss is preventable.</div>
""", mt, n()),
        slide_workshop(m, "Workshop: Clone Site to Staging", [
            "Create full backup with UpdraftPlus or host tool",
            "Clone to staging subdomain",
            "Verify staging blocks search engines",
            "Make one test change and confirm live site unaffected",
            "Perform test restore from backup file",
        ], "Staging URL + successful restore test documented", mt, n()),
        slide_summary(m, [
            "Implement 3-2-1 backup strategy on every site",
            "Use staging for all risky changes",
            "Execute migrations with URL replace and redirect maps",
            "Test restore procedures regularly",
        ], mt, n()),
    ]


def module_10():
    m, mt = 10, MOD_TITLES[9]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(10, "Performance, Caching & Hosting", "Make WordPress fast — hosting choices, cache, and Core Web Vitals."),
        slide_bullets(m, "Hosting Decisions for Managers", [
            "<strong>Shared hosting</strong> — budget sites, low traffic",
            "<strong>Managed WordPress</strong> — Kinsta, WP Engine, Flywheel (best for agencies)",
            "<strong>VPS/Cloud</strong> — DigitalOcean, AWS — needs technical admin",
            "<strong>PHP 8.2+</strong> — non-negotiable for speed + security",
            "<strong>Server location</strong> — close to primary audience",
        ], mt, n()),
        slide_two_col(m, "Caching Layers",
                      "Page Cache", [
                          "LiteSpeed Cache, WP Rocket",
                          "Serves static HTML to visitors",
                          "Exclude: cart, checkout, my-account",
                          "Purge on content update",
                          "Mobile + desktop cache rules",
                      ],
                      "Object + Opcode", [
                          "Redis/Memcached object cache",
                          "Reduces database queries",
                          "PHP OPcache on server",
                          "CDN for static assets",
                          "Database cleanup (WP-Optimize)",
                      ], mt, n()),
        slide_content(m, "Core Web Vitals for WordPress Managers", """
<table class="data"><tr><th>Metric</th><th>Target</th><th>WordPress Fix</th></tr>
<tr><td>LCP (Largest Contentful Paint)</td><td>&lt; 2.5s</td><td>Optimize hero image, cache, CDN</td></tr>
<tr><td>INP (Interaction to Next Paint)</td><td>&lt; 200ms</td><td>Reduce JS, defer scripts</td></tr>
<tr><td>CLS (Cumulative Layout Shift)</td><td>&lt; 0.1</td><td>Set image dimensions, stable fonts</td></tr>
</table>
<ul>
<li>Test with PageSpeed Insights and GTmetrix monthly</li>
<li>Don't install 5 performance plugins — they conflict</li>
</ul>
""", mt, n()),
        slide_workshop(m, "Workshop: Speed Optimization Sprint", [
            "Run PageSpeed before score — screenshot baseline",
            "Install/configure one cache plugin properly",
            "Compress top 10 heaviest images",
            "Enable lazy load + font optimization",
            "Re-test and document improvement",
        ], "Before/after PageSpeed report with 3 optimizations listed", mt, n()),
        slide_summary(m, [
            "Choose appropriate hosting for site needs",
            "Configure page cache and exclusions for WooCommerce",
            "Monitor Core Web Vitals monthly",
            "Follow one-plugin-per-job performance strategy",
        ], mt, n()),
    ]


def module_11():
    m, mt = 11, MOD_TITLES[10]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(11, "SEO Management on WordPress", "Manage SEO from WordPress admin — not theory, but daily operations."),
        slide_bullets(m, "SEO Plugin Setup (Rank Math / Yoast)", [
            "<strong>Site verification</strong> — connect Google Search Console",
            "<strong>Sitemap</strong> — enable, submit to GSC",
            "<strong>Title templates</strong> — %title% %sep% %sitename%",
            "<strong>Schema defaults</strong> — Organization, Article, Product",
            "<strong>Noindex</strong> — tag archives, thin pages, staging",
        ], mt, n()),
        slide_two_col(m, "On-Page SEO Tasks in WP Admin",
                      "Per Post/Page", [
                          "Focus keyword set",
                          "SEO title + meta description",
                          "URL slug optimized",
                          "Internal links added (2-3 min)",
                          "Featured image + alt text",
                          "Schema type selected",
                      ],
                      "Site-Wide", [
                          "XML sitemap submitted",
                          "robots.txt verified",
                          "Redirect plugin for 404s",
                          "Breadcrumbs enabled",
                          "Canonical URLs correct",
                          "Local SEO schema (if applicable)",
                      ], mt, n()),
        slide_content(m, "Search Console Workflow for Managers", """
<ul>
<li><strong>Weekly</strong> — check Coverage errors, fix indexing issues</li>
<li><strong>Monthly</strong> — review Performance report, top queries</li>
<li><strong>After migration</strong> — submit sitemap, monitor 404 spike</li>
<li><strong>Core updates</strong> — watch for schema plugin conflicts</li>
</ul>
<div class="callout callout-tip"><strong>Manager Mindset</strong>SEO on WordPress is operational — titles, links, speed, and indexation. Check GSC like you check orders.</div>
""", mt, n()),
        slide_workshop(m, "Workshop: SEO Setup on WordPress", [
            "Install Rank Math or Yoast — complete setup wizard",
            "Configure sitemap and connect Search Console",
            "Optimize 3 pages: title, meta, slug, internal links",
            "Fix 5 redirect/404 issues from GSC export",
            "Create monthly SEO maintenance checklist",
        ], "SEO setup doc + 3 optimized pages + GSC connected", mt, n()),
        slide_summary(m, [
            "Configure SEO plugin for site-wide defaults",
            "Execute per-page SEO checklist on all content",
            "Use Search Console as weekly management tool",
            "Integrate SEO into content publishing workflow",
        ], mt, n()),
    ]


def module_12():
    m, mt = 12, MOD_TITLES[11]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(12, "n8n Automation for WordPress", "Automate publishing, monitoring, and reporting with n8n workflows."),
        slide_diagram(m, "WordPress + n8n Integration Architecture", """
  ┌──────────────┐     REST API      ┌──────────────┐
  │   n8n        │◀────────────────▶│  WordPress   │
  │  Workflows   │  Application     │  wp-json/wp/v2│
  └──────┬───────┘  Password        └──────────────┘
         │
    ┌────┴────┬──────────┬──────────┐
    ▼         ▼          ▼          ▼
  Slack    Google     OpenAI    Schedule
  Alerts   Sheets     Content   Trigger
""", [
            "WordPress REST API enables post CRUD, media upload, user mgmt",
            "Application Passwords for secure n8n authentication",
            "Webhook triggers for form submissions → CRM",
        ], mt, n()),
        slide_bullets(m, "High-Value WordPress + n8n Workflows", [
            "<strong>Auto-publish</strong> — Google Doc approved → draft post in WP",
            "<strong>Form to CRM</strong> — WPForms webhook → HubSpot/Sheets",
            "<strong>Backup alerts</strong> — backup complete → Slack notification",
            "<strong>Uptime monitor</strong> — site down → SMS + create ticket",
            "<strong>SEO monitor</strong> — GSC error → email + Trello card",
            "<strong>WooCommerce</strong> — new order → fulfillment spreadsheet row",
        ], mt, n()),
        slide_content(m, "Building Your First Workflow", """
<ol class="steps">
<li>In WordPress: create Application Password (Users → Profile)</li>
<li>In n8n: add WordPress node with site URL + credentials</li>
<li>Test: GET /wp/v2/posts?per_page=1</li>
<li>Add Schedule Trigger → check Site Health endpoint or RSS</li>
<li>Add IF node → condition → Slack/Email notification</li>
<li>Save, activate, document workflow purpose</li>
</ol>
<div class="callout"><strong>Lab Environment</strong>Use this course's Docker WordPress + n8n stack for safe testing.</div>
""", mt, n()),
        slide_workshop(m, "Workshop: Build an Autonomous WP Monitor", [
            "Set up Application Password on WordPress",
            "Create n8n workflow: hourly check if homepage returns 200",
            "If down: send Slack/email alert with timestamp",
            "Add node: log result to Google Sheet",
            "Export workflow JSON for documentation",
        ], "Active n8n workflow JSON + test alert screenshot", mt, n()),
        slide_summary(m, [
            "Connect n8n to WordPress via REST API",
            "Build monitoring and notification workflows",
            "Automate repetitive publishing and reporting tasks",
            "Document all automations for client handoff",
        ], mt, n()),
    ]


def module_13():
    m, mt = 13, MOD_TITLES[12]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(13, "AI Tools for WordPress Management", "Use AI responsibly for content, support, and site operations."),
        slide_two_col(m, "AI for WordPress Managers",
                      "Good Uses", [
                          "Draft blog outlines and first drafts",
                          "Generate alt text suggestions",
                          "Write meta descriptions at scale",
                          "Summarize support tickets",
                          "Create FAQ content from docs",
                          "Code snippets for functions.php",
                      ],
                      "Bad Uses", [
                          "Publish unedited AI content",
                          "Bulk-generate thin product pages",
                          "Trust AI for legal/medical content",
                          "Skip fact-checking statistics",
                          "Ignore client brand voice",
                          "Replace human QA entirely",
                      ], mt, n()),
        slide_bullets(m, "AI Content Workflow in WordPress", [
            "<strong>1. Brief</strong> — keyword, intent, outline (human)",
            "<strong>2. Draft</strong> — AI generates section-by-section",
            "<strong>3. Edit</strong> — human fixes facts, tone, E-E-A-T",
            "<strong>4. Optimize</strong> — SEO plugin checklist pass",
            "<strong>5. Publish</strong> — schedule with featured image",
            "<strong>6. Monitor</strong> — GSC performance after 30 days",
        ], mt, n()),
        slide_content(m, "AI Plugins & Integrations", """
<ul>
<li><strong>AI Engine / AI Power</strong> — content generation inside WP editor</li>
<li><strong>Rank Math Content AI</strong> — titles, meta, FAQs</li>
<li><strong>n8n + OpenAI node</strong> — automated brief → draft pipeline</li>
<li><strong>Support bots</strong> — train on site docs, embed via plugin</li>
</ul>
<div class="callout callout-warn"><strong>Policy</strong>Disclose AI-assisted content when client or industry requires it. Maintain editorial accountability.</div>
""", mt, n()),
        slide_workshop(m, "Workshop: AI-Assisted Article Pipeline", [
            "Write a 1-page content brief for a blog post",
            "Generate draft with AI — paste into WordPress block editor",
            "Human-edit: add examples, fix facts, improve headings",
            "Complete SEO plugin checklist before publish",
            "Document time saved vs quality score (1-10 self-rating)",
        ], "Published AI-assisted post + workflow documentation", mt, n()),
        slide_summary(m, [
            "Apply AI to accelerate, not replace, WordPress management",
            "Follow human-in-the-loop content workflow",
            "Evaluate AI plugins for your stack",
            "Maintain quality and E-E-A-T standards",
        ], mt, n()),
    ]


def module_14():
    m, mt = 14, MOD_TITLES[13]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(14, "Client Site Management & Reporting", "Run multiple WordPress sites professionally — SOPs, reporting, retainers."),
        slide_diagram(m, "Managed WordPress Service Stack", """
  CLIENT SITE
      │
      ├── Maintenance Retainer ($99-499/mo)
      │     ├── Weekly updates + backups
      │     ├── Uptime monitoring
      │     └── Monthly report
      │
      ├── Content Retainer
      │     ├── X posts/month
      │     └── SEO optimization
      │
      └── Support Hours
            └── Ad-hoc fixes + training
""", [
            "Productize services — clients buy outcomes, not hours",
            "Use ManageWP, MainWP, or InfiniteWP for multi-site dashboard",
        ], mt, n()),
        slide_bullets(m, "Monthly Client Report Contents", [
            "<strong>Updates applied</strong> — core, plugins, themes with dates",
            "<strong>Uptime %</strong> — from UptimeRobot or Pingdom",
            "<strong>Backup status</strong> — last successful backup date",
            "<strong>Security scan</strong> — clean or issues resolved",
            "<strong>Performance score</strong> — PageSpeed trend",
            "<strong>SEO snapshot</strong> — GSC clicks/impressions vs last month",
            "<strong>Content published</strong> — list of new/updated pages",
            "<strong>Recommendations</strong> — 2-3 actionable next steps",
        ], mt, n()),
        slide_content(m, "Standard Operating Procedures (SOPs)", """
<ul>
<li><strong>Onboarding SOP</strong> — access, backup, inventory, baseline audit</li>
<li><strong>Update SOP</strong> — backup → staging → test → production → verify</li>
<li><strong>Incident SOP</strong> — detect → assess → restore → report → postmortem</li>
<li><strong>Offboarding SOP</strong> — export, transfer credentials, final report</li>
</ul>
<div class="callout callout-tip"><strong>Agency Tip</strong>Template everything in Notion/Google Docs. New team members onboard in days, not weeks.</div>
""", mt, n()),
        slide_workshop(m, "Workshop: Create a Client Management Kit", [
            "Build plugin/theme inventory template",
            "Write monthly report template (Google Doc)",
            "Create update SOP with 8 steps",
            "Draft maintenance retainer scope (what's in/out)",
            "Set up one monitoring tool for a test site",
        ], "Client Management Kit: 4 templates ready to use", mt, n()),
        slide_summary(m, [
            "Structure managed WordPress services into retainers",
            "Deliver professional monthly reports",
            "Document SOPs for consistent team delivery",
            "Use multi-site tools for agency efficiency",
        ], mt, n()),
    ]


def module_15():
    m, mt = 15, MOD_TITLES[14]
    sn = [1]
    def n(): sn[0] += 1; return sn[0]

    return [
        slide_section(15, "Capstone: Managed WordPress Site", "Integrate everything — build and document a fully managed WordPress operation."),
        slide_content(m, "Capstone Project Requirements", """
<p class="lead">Deliver a complete managed WordPress site with documentation proving professional management capability.</p>
<ul>
<li><strong>Live WordPress site</strong> — configured settings, branded theme, 10+ pages/posts</li>
<li><strong>WooCommerce</strong> — 5+ products with working test checkout (optional track: brochure only)</li>
<li><strong>Security</strong> — 2FA, security plugin, hardened wp-config</li>
<li><strong>Backups</strong> — automated daily, tested restore</li>
<li><strong>Performance</strong> — cache configured, PageSpeed 80+ mobile</li>
<li><strong>SEO</strong> — plugin configured, GSC connected, 3 optimized pages</li>
<li><strong>Automation</strong> — one n8n workflow monitoring the site</li>
<li><strong>Client kit</strong> — SOPs, inventory, monthly report sample</li>
</ul>
""", mt, n()),
        slide_two_col(m, "Deliverables & Grading",
                      "Submit", [
                          "Live site URL + admin walkthrough video (5 min)",
                          "Site Management Documentation (PDF)",
                          "Plugin inventory spreadsheet",
                          "n8n workflow export JSON",
                          "Monthly report sample",
                          "Before/after performance screenshot",
                      ],
                      "Graded On", [
                          "Settings & configuration completeness",
                          "Content quality and organization",
                          "Security and backup implementation",
                          "Performance optimization results",
                          "Automation functionality",
                          "Documentation professionalism",
                      ], mt, n()),
        slide_bullets(m, "4-Week Capstone Timeline", [
            "<strong>Week 1</strong> — Install, configure, theme, content structure",
            "<strong>Week 2</strong> — WooCommerce, users, security, backups",
            "<strong>Week 3</strong> — Performance, SEO, media optimization",
            "<strong>Week 4</strong> — n8n automation, docs, report, presentation",
        ], mt, n()),
        slide_content(m, "Certification & Next Steps", """
<div class="callout callout-tip"><strong>Congratulations!</strong>You now have the skills to manage WordPress sites professionally — from daily operations to automation and client delivery.</div>
<ul>
<li>Continue learning: WordPress.org documentation, WooCommerce docs</li>
<li>Join WordPress meetups and WordCamps</li>
<li>Build your agency SOP library after every client project</li>
<li>Explore advanced topics: multisite, headless WP, custom blocks</li>
</ul>
""", mt, n()),
        slide_summary(m, [
            "Deliver a production-ready managed WordPress site",
            "Document all management processes professionally",
            "Demonstrate automation and monitoring capability",
            "Present capstone for certification evaluation",
        ], mt, n()),
    ]


def appendix():
    m, mt = 25, "Appendix"
    sn = [0]
    def n(): sn[0] += 1; return sn[0]

    glossary_terms = [
        ("Admin Bar", "Top toolbar when logged in — quick links to edit pages"),
        ("Application Password", "WP credential for API access without main password"),
        ("Block Editor", "Gutenberg — drag-and-drop content builder in WP 5+"),
        ("Canonical URL", "Preferred version of a page for search engines"),
        ("Child Theme", "Sub-theme inheriting parent — safe customization layer"),
        ("Core Web Vitals", "Google UX metrics: LCP, INP, CLS"),
        ("Cron", "WP scheduled tasks — publish later, update checks"),
        ("Customizer", "Live preview settings for themes"),
        ("Database", "MySQL storage for all WP content and settings"),
        ("Fluent Forms", "Form builder plugin with native webhooks and CRM integration"),
        ("FSE", "Full Site Editing — block-based theme customization"),
        ("Hook", "Action/filter point plugins use to modify WP behavior"),
        ("HPOS", "WooCommerce High-Performance Order Storage"),
        ("LiteSpeed Cache", "Server-aware cache plugin — best on LiteSpeed hosts"),
        ("MU-Plugin", "Must-use plugin — auto-loaded, can't be deactivated"),
        ("Permalink", "Pretty URL structure — /%postname%/ recommended"),
        ("Rank Math", "SEO plugin — sitemap, schema, redirects, GSC integration"),
        ("REST API", "wp-json endpoints for programmatic WP management"),
        ("Robots.txt", "Crawler instructions — don't block CSS/JS"),
        ("Schema", "Structured data markup for rich search results"),
        ("Shortcode", "Bracket code embedding features: [gallery]"),
        ("Slug", "URL-friendly post name: /my-blog-post/"),
        ("Staging", "Copy of site for safe testing before production"),
        ("Transient", "Temporary cached data in WP database"),
        ("Uncanny Automator", "WordPress automation plugin — triggers and actions in admin"),
        ("UpdraftPlus", "Backup plugin — scheduled backups to cloud storage"),
        ("Webhook", "URL that receives POST data when a plugin event fires"),
        ("Wordfence", "Security plugin — firewall, malware scan, 2FA"),
        ("WP Rocket", "Premium cache plugin — page speed optimization"),
        ("WPForms", "Drag-and-drop form builder with email and CRM addons"),
        ("Yoast SEO", "SEO plugin — readability, schema, Search Appearance settings"),
        ("wp-config.php", "Main configuration file — DB credentials, constants"),
    ]

    gl_items = "".join(f"<tr><td><strong>{esc(t)}</strong></td><td>{esc(d)}</td></tr>" for t, d in glossary_terms)

    wp_checklist = [
        "General settings configured (title, timezone, URLs)",
        "Permalinks set to Post name",
        "Site Health — all critical issues resolved",
        "Admin accounts secured with 2FA",
        "Backup plugin installed — daily schedule active",
        "Security plugin installed and scanning",
        "Cache plugin configured with WooCommerce exclusions",
        "SEO plugin connected to Search Console",
        "Staging environment available",
        "Plugin inventory documented",
        "Theme + child theme updated",
        "SSL/HTTPS forced site-wide",
        "File editing disabled in wp-config",
        "Monthly report template ready",
        "n8n or monitoring workflow active",
    ]

    plugin_checklist = [
        "Only ONE plugin per function (SEO, cache, security, backup)",
        "All premium licenses connected and renewal dates tracked",
        "Setup wizards completed for every active plugin",
        "Plugin settings screens saved in client docs",
        "Form plugins tested — email + webhook delivery verified",
        "Rank Math or Yoast — sitemap submitted to Search Console",
        "Wordfence/Solid — weekly scan scheduled, 2FA enabled",
        "UpdraftPlus/WPvivid — remote storage connected, restore tested",
        "WP Rocket/LiteSpeed — cart/checkout URLs excluded from cache",
        "WooCommerce payment gateway tested in sandbox mode",
        "Application Passwords created for API integrations only",
        "Webhooks documented in integration diagram",
        "No deactivated unused plugins left installed",
        "Update SOP followed — backup before every plugin update",
    ]

    chk = "".join(f"<li>{esc(c)}</li>" for c in wp_checklist)
    pchk = "".join(f"<li>{esc(c)}</li>" for c in plugin_checklist)

    exam_sample = [
        ("What is the recommended permalink structure?", ["?p=123", "/%postname%/", "/%category%/%postname%/", "/%year%/%monthnum%/"], 1),
        ("Which role can publish and edit ALL posts?", ["Author", "Contributor", "Editor", "Subscriber"], 2),
        ("Where are uploaded media files stored?", ["/wp-admin/uploads/", "/wp-content/uploads/", "/wp-includes/media/", "/uploads/"], 1),
        ("What does DISALLOW_FILE_EDIT do?", ["Disables comments", "Prevents theme/plugin editing from admin", "Blocks REST API", "Disables updates"], 1),
        ("Best practice for plugin updates?", ["Update all at once on live", "Backup, test staging, then production", "Never update plugins", "Only update monthly on live"], 1),
    ]

    exam_html = ""
    for i, (q, opts, ans) in enumerate(exam_sample, 1):
        opts_html = "".join(f"<li>({chr(65+j)}) {esc(o)}</li>" for j, o in enumerate(opts))
        exam_html += f"<li><strong>Q{i}.</strong> {esc(q)}<ul>{opts_html}</ul></li>"

    return [
        slide_section(m, "Appendix — Reference Materials", "Glossary, checklists, exam sample, and certification rubric."),
        slide_content(m, "WordPress Management Glossary", f"<table class='data'><tr><th>Term</th><th>Definition</th></tr>{gl_items}</table>", mt, n()),
        slide_content(m, "Master WordPress Management Checklist", f"<ul class='checklist'>{chk}</ul>", mt, n()),
        slide_content(m, "Plugin Integration & Usage Checklist", f"<ul class='checklist'>{pchk}</ul><div class='callout callout-tip'><strong>Print this slide</strong>Use before every client site launch and monthly maintenance review.</div>", mt, n()),
        slide_two_col(m, "Daily & Weekly Manager Routines",
                      "Daily (5 min)", [
                          "Check site loads correctly",
                          "Review new WooCommerce orders",
                          "Check security plugin alerts",
                          "Verify backup completed overnight",
                      ],
                      "Weekly (30 min)", [
                          "Apply tested plugin updates",
                          "Review Search Console errors",
                          "Check disk space and uptime report",
                          "Publish/schedule planned content",
                          "Scan for broken links",
                      ], mt, n()),
        slide_content(m, "Certification Exam Sample Questions", f"<ol>{exam_html}</ol><p><em>Full 100-question exam available in instructor materials. Passing score: 80%.</em></p>", mt, n()),
        slide_content(m, "Certification Project Rubric", """
<table class="data"><tr><th>Criteria</th><th>Points</th><th>Excellent (90%+)</th></tr>
<tr><td>Site configuration</td><td>20</td><td>All settings optimal, Site Health clean</td></tr>
<tr><td>Content & structure</td><td>15</td><td>10+ quality pages, clear navigation</td></tr>
<tr><td>Security & backups</td><td>20</td><td>2FA, hardened config, tested restore</td></tr>
<tr><td>Performance</td><td>15</td><td>PageSpeed 80+ mobile, cache configured</td></tr>
<tr><td>SEO setup</td><td>10</td><td>GSC connected, sitemap, optimized pages</td></tr>
<tr><td>Automation</td><td>10</td><td>Working n8n workflow documented</td></tr>
<tr><td>Documentation</td><td>10</td><td>Professional client-ready kit</td></tr>
</table>
<p><strong>Pass:</strong> 70+ points · <strong>Merit:</strong> 80+ · <strong>Distinction:</strong> 90+</p>
""", mt, n()),
    ]


def build_all_slides():
    slides = []
    slides.append(slide_cover(
        "WordPress Management Mastery",
        "Plugins, Integrations & Daily Operations — The Complete Manager's Course",
        [
            "Plugin Setup · Rank Math · Yoast · Wordfence · UpdraftPlus · WP Rocket",
            "Forms · CRM · WooCommerce Extensions · REST API · n8n Webhooks",
            "24 Modules · 200+ Slides · Hands-On Plugin Workshops",
        ],
    ))
    slides.append(slide_toc(TOC))

    # Core modules 1–6 (plugin management expanded)
    for mod_fn in [module_1, module_2, module_3, module_4, module_5, module_6]:
        slides.extend(mod_fn())

    # Plugin deep-dive modules 16–24
    for plugin_mod in get_all_plugin_modules():
        slides.extend(plugin_mod)

    # Remaining modules 7–15 + appendix
    for mod_fn in [module_7, module_8, module_9, module_10, module_11, module_12,
                   module_13, module_14, module_15, appendix]:
        slides.extend(mod_fn())

    slides.append(slide_cover(
        "Thank You",
        "Master WordPress Plugins & Integrations",
        ["Questions · Certification · Plugin Lab Resources"],
    ))
    return wrap_deck("\n".join(slides), "WordPress Management Mastery — Slide Deck")


if __name__ == "__main__":
    html = build_all_slides()
    from pathlib import Path
    out = Path(__file__).parent / "wordpress-management-course.html"
    out.write_text(html, encoding="utf-8")
    print(f"Generated {out} ({len(html):,} chars, ~{html.count('class=\"slide\"')} slides)")
