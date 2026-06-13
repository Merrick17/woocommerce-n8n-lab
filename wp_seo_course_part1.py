#!/usr/bin/env python3
"""
SEO / AEO / GEO on WordPress — complete slide course for non-coders.
All techniques applied via plugins — zero coding required.
"""
from wp_slide_framework import (
    slide_cover, slide_toc, slide_section, slide_content, slide_two_col,
    slide_bullets, slide_diagram, slide_workshop, slide_summary, callout,
    wrap_deck, esc,
)

AUDIENCE = "No coding experience required — every technique uses WordPress plugins and click-by-click settings."

TOC = [
    "Module 1 — SEO, AEO & GEO Explained (Beginner Friendly)",
    "Module 2 — WordPress Essentials for Non-Coders",
    "Module 3 — Install & Configure Your SEO Plugin (Rank Math / Yoast)",
    "Module 4 — On-Page SEO Using Plugins Only",
    "Module 5 — Technical SEO Without Writing Code",
    "Module 6 — Keyword Research & Content Planning in WordPress",
    "Module 7 — Local SEO with WordPress Plugins",
    "Module 8 — AEO: Answer Engine Optimization on WordPress",
    "Module 9 — Featured Snippets, FAQ & People Also Ask",
    "Module 10 — Google AI Overviews & SGE Optimization",
    "Module 11 — GEO: ChatGPT, Perplexity & Gemini Visibility",
    "Module 12 — WooCommerce SEO for Non-Coders",
    "Module 13 — Image, Video & Media SEO Plugins",
    "Module 14 — Internal Linking & Content Clusters (Plugin-Assisted)",
    "Module 15 — Analytics: Search Console & Rank Math Dashboard",
    "Module 16 — AI Content Tools Inside WordPress",
    "Module 17 — No-Code SEO Automation (n8n, Zapier, Automator)",
    "Module 18 — Capstone: Complete SEO/AEO/GEO WordPress Site",
    "Appendix — Checklists, Glossary & Certification",
]

MOD = [
    "SEO AEO GEO Intro", "WP for Non-Coders", "SEO Plugin Setup",
    "On-Page SEO", "Technical SEO", "Keywords & Content",
    "Local SEO", "AEO Basics", "Snippets & FAQ", "AI Overviews",
    "GEO Mastery", "WooCommerce SEO", "Media SEO", "Linking & Clusters",
    "Analytics", "AI Content Tools", "No-Code Automation", "Capstone",
]


def _n(sn):
    sn[0] += 1
    return sn[0]


def mod1(sn):
    m, mt = 1, MOD[0]
    return [
        slide_section(m, "SEO, AEO & GEO Explained", AUDIENCE),
        slide_bullets(m, "Three Ways People Find Your Website Today", [
            "<strong>SEO</strong> — Search Engine Optimization → Google blue links",
            "<strong>AEO</strong> — Answer Engine Optimization → featured snippets, voice answers",
            "<strong>GEO</strong> — Generative Engine Optimization → ChatGPT, Perplexity, Gemini citations",
            "Your WordPress site can rank in <strong>all three</strong> using plugins — no code",
            "This course teaches <strong>what to click</strong>, not what to code",
        ], mt, _n(sn)),
        slide_diagram(m, "Traditional SEO vs AEO vs GEO", """
  USER QUESTION: "best wordpress seo plugin 2026"
         │
    ┌────┴────┬────────────┬─────────────┐
    ▼         ▼            ▼             ▼
  GOOGLE    GOOGLE       CHATGPT     PERPLEXITY
  organic   AI Overview  synthesizes  cites sources
  #1-#10    answer box   an answer    with links
    │         │            │             │
    └─────────┴────────────┴─────────────┘
              YOUR WORDPRESS SITE
         (optimized with Rank Math / Yoast)
""", [
            "SEO = get on page 1 of Google",
            "AEO = become THE answer Google shows at top",
            "GEO = become a source AI tools cite and recommend",
        ], mt, _n(sn)),
        slide_two_col(m, "What Non-Coders CAN Do in WordPress",
                      "With plugins you can", [
                          "Write SEO titles & meta descriptions",
                          "Create XML sitemaps automatically",
                          "Add FAQ schema with a block click",
                          "Speed up site with cache plugin toggles",
                          "Connect Google Search Console in 2 clicks",
                          "Build answer-first content with templates",
                      ],
                      "You do NOT need to", [
                          "Edit PHP or theme files",
                          "Write robots.txt manually",
                          "Code JSON-LD schema by hand",
                          "Use FTP or command line",
                          "Understand HTML/CSS (helpful but optional)",
                          "Hire a developer for basic SEO setup",
                      ], mt, _n(sn)),
        slide_content(m, "Your Non-Coder Plugin Toolkit", """
<table class="data"><tr><th>Goal</th><th>Plugin (pick one per row)</th><th>What it does for you</th></tr>
<tr><td>SEO hub</td><td>Rank Math OR Yoast SEO</td><td>Titles, meta, sitemap, schema — all in editor</td></tr>
<tr><td>Speed</td><td>LiteSpeed Cache OR WP Rocket</td><td>Toggle settings → faster pages</td></tr>
<tr><td>FAQ / AEO</td><td>Rank Math FAQ Block OR Yoast FAQ</td><td>FAQ schema without code</td></tr>
<tr><td>Forms + leads</td><td>WPForms OR Fluent Forms</td><td>Contact pages for local SEO</td></tr>
<tr><td>Redirects</td><td>Rank Math Redirection OR Redirection</td><td>Fix broken links in admin</td></tr>
<tr><td>Local SEO</td><td>Rank Math Local OR Yoast Local</td><td>LocalBusiness schema wizard</td></tr>
<tr><td>AI writing</td><td>Rank Math Content AI OR AI Engine</td><td>Draft content inside WordPress</td></tr>
</table>
""", mt, _n(sn)),
        slide_workshop(m, "Workshop: Map Your SEO/AEO/GEO Goals", [
            "Write down your website type (blog, business, shop, local service)",
            "List 5 questions your customers ask (these become AEO/GEO targets)",
            "Install WordPress locally or use your existing site",
            "Verify you can login to wp-admin and find Plugins menu",
            "Screenshot your empty dashboard — your 'before' state",
        ], "1-page goal sheet: 5 target questions + site type", mt, _n(sn)),
        slide_summary(m, [
            "Explain SEO, AEO, and GEO in plain language",
            "Know which plugins replace coding tasks",
            "Understand this course is 100% click-based WordPress admin",
            "Identify your site's primary search channels",
        ], mt, _n(sn)),
    ]


def mod2(sn):
    m, mt = 2, MOD[1]
    return [
        slide_section(m, "WordPress Essentials for Non-Coders", "Only what you need in wp-admin to do SEO — nothing extra."),
        slide_bullets(m, "WordPress Admin — 6 Areas You Will Use", [
            "<strong>Posts</strong> — blog articles (most SEO content lives here)",
            "<strong>Pages</strong> — About, Services, Contact (static SEO pages)",
            "<strong>Media</strong> — upload images, add alt text for image SEO",
            "<strong>Plugins</strong> — install Rank Math, cache, forms",
            "<strong>Settings → Permalinks</strong> — set to \"Post name\" once",
            "<strong>Appearance → Menus</strong> — navigation (helps internal linking)",
        ], mt, _n(sn)),
        slide_content(m, "One-Time WordPress Settings for SEO", """
<ol class="steps">
<li><strong>Settings → General</strong> — correct site title and tagline</li>
<li><strong>Settings → Permalinks</strong> — select <strong>Post name</strong> → Save</li>
<li><strong>Settings → Reading</strong> — set homepage (static page or blog)</li>
<li><strong>Settings → Privacy</strong> — ensure \"Discourage search engines\" is OFF on live site</li>
<li><strong>Install SSL</strong> — hosting panel → Force HTTPS (most hosts: one click)</li>
</ol>
<div class="callout callout-tip"><strong>Non-coder rule</strong>If a setting isn't listed above or in your SEO plugin, you probably don't need to touch it.</div>
""", mt, _n(sn)),
        slide_two_col(m, "Posts vs Pages — SEO Perspective",
                      "Use Posts for", [
                          "Blog articles targeting keywords",
                          "How-to guides (AEO gold)",
                          "News and updates",
                          "FAQ-style content",
                          "Content clusters / topic hubs",
                      ],
                      "Use Pages for", [
                          "Homepage (main keyword target)",
                          "About (E-E-A-T trust signals)",
                          "Service pages (local + commercial SEO)",
                          "Contact (local NAP consistency)",
                          "Pillar / cornerstone content",
                      ], mt, _n(sn)),
        slide_bullets(m, "The Block Editor — SEO Content Without Code", [
            "<strong>Heading block</strong> — one H1 per page, H2/H3 for sections",
            "<strong>Paragraph block</strong> — write answer-first intro (AEO)",
            "<strong>FAQ block</strong> — Rank Math or Yoast adds schema automatically",
            "<strong>Image block</strong> — always fill Alt Text field on right panel",
            "<strong>List block</strong> — numbered steps win featured snippets",
            "<strong>Table block</strong> — comparisons rank well in AI Overviews",
        ], mt, _n(sn)),
        slide_workshop(m, "Workshop: Configure WordPress for SEO", [
            "Set permalinks to Post name",
            "Create 3 pages: Home, About, Contact",
            "Create 1 blog post with H1, 2 H2s, and an image with alt text",
            "Assign homepage under Settings → Reading",
            "Verify site loads with https://",
        ], "3 pages + 1 post published with correct permalink structure", mt, _n(sn)),
        slide_summary(m, [
            "Navigate wp-admin confidently as a non-coder",
            "Apply one-time SEO-friendly WordPress settings",
            "Choose posts vs pages for different content types",
            "Use blocks instead of code for structured content",
        ], mt, _n(sn)),
    ]


def mod3(sn):
    m, mt = 3, MOD[2]
    return [
        slide_section(m, "Install & Configure Your SEO Plugin", "Rank Math or Yoast — complete setup wizard, zero code."),
        slide_content(m, "Install Rank Math — Click by Click", """
<ol class="steps">
<li>Plugins → <strong>Add New</strong> → search \"Rank Math SEO\"</li>
<li>Install Now → <strong>Activate</strong></li>
<li>Click <strong>Start Wizard</strong> — do not skip</li>
<li>Choose site type: Business / Blog / Shop</li>
<li>Connect Google Search Console (optional but recommended)</li>
<li>Enable Sitemap, Schema, Redirection modules</li>
<li>Finish wizard → go to Rank Math → Dashboard</li>
</ol>
<div class="callout callout-warn"><strong>Important</strong>Install ONLY Rank Math OR Yoast — never both. They conflict.</div>
""", mt, _n(sn)),
        slide_content(m, "Rank Math — Essential Settings (No Code)", """
<table class="data"><tr><th>Menu</th><th>What to set</th><th>Why it matters</th></tr>
<tr><td>General Settings → Edit robots.txt</td><td>Use default — don't block site</td><td>Lets Google crawl you</td></tr>
<tr><td>Sitemap Settings</td><td>Enable posts, pages, categories</td><td>Auto XML sitemap</td></tr>
<tr><td>Titles & Meta → Homepage</td><td>Write title + meta description</td><td>Google SERP appearance</td></tr>
<tr><td>Titles & Meta → Posts</td><td>Template: %title% %sep% %sitename%</td><td>Auto titles for all posts</td></tr>
<tr><td>Schema → Homepage</td><td>Organization or LocalBusiness</td><td>Knowledge panel signals</td></tr>
<tr><td>404 Monitor</td><td>Turn ON</td><td>Find broken links to fix</td></tr>
</table>
""", mt, _n(sn)),
        slide_two_col(m, "Yoast SEO Alternative Setup",
                      "Yoast wizard steps", [
                          "Install Yoast SEO from plugin directory",
                          "Run First-time configuration",
                          "Set Organization vs Person",
                          "Configure Search Appearance → Content Types",
                          "Enable XML sitemap (on by default)",
                          "Connect Site Kit for GSC (optional)",
                      ],
                      "Yoast daily use", [
                          "Edit post → scroll to Yoast metabox",
                          "Set focus keyphrase",
                          "Edit SEO title + meta description",
                          "Follow green bullet checklist",
                          "Add FAQ block (Yoast Premium or free FAQ plugin)",
                          "Check Search Appearance preview",
                      ], mt, _n(sn)),
        slide_content(m, "Connect Google Search Console (2-Minute Plugin Method)", """
<ol class="steps">
<li>Rank Math → General Settings → <strong>Search Console</strong></li>
<li>Click <strong>Connect Google Account</strong></li>
<li>Authorize Rank Math to read your GSC data</li>
<li>Alternatively: Yoast → General → Webmaster Tools → paste verification meta tag</li>
<li>Or use plugin <strong>Site Kit by Google</strong> — one-click GSC + Analytics</li>
</ol>
<p class="lead">Search Console shows which queries bring traffic — your SEO report card. No code needed.</p>
""", mt, _n(sn)),
        slide_workshop(m, "Workshop: Complete SEO Plugin Setup", [
            "Install Rank Math OR Yoast — finish entire wizard",
            "Write homepage SEO title (60 chars) and meta description (155 chars)",
            "Enable XML sitemap — copy sitemap URL",
            "Submit sitemap in Google Search Console (search.google.com/search-console)",
            "Configure Organization schema on homepage",
            "Screenshot Rank Math/Yoast dashboard showing green status",
        ], "SEO plugin fully configured + GSC sitemap submitted", mt, _n(sn)),
        slide_summary(m, [
            "Install and complete SEO plugin wizard without code",
            "Configure sitemap, titles, schema via plugin menus",
            "Connect Google Search Console through plugin",
            "Choose one SEO plugin and master its interface",
        ], mt, _n(sn)),
    ]


def mod4(sn):
    m, mt = 4, MOD[3]
    return [
        slide_section(m, "On-Page SEO Using Plugins Only", "Optimize every page from the WordPress editor — no HTML required."),
        slide_bullets(m, "The Non-Coder On-Page SEO Checklist (Per Page)", [
            "<strong>Focus keyword</strong> — enter in Rank Math/Yoast metabox",
            "<strong>SEO title</strong> — compelling, under 60 characters",
            "<strong>Meta description</strong> — 150–155 chars, includes keyword + CTA",
            "<strong>URL slug</strong> — short, readable: /wordpress-seo-guide/",
            "<strong>H1</strong> — one main heading matching intent",
            "<strong>H2/H3</strong> — logical sections (plugin analyzes these)",
            "<strong>Internal links</strong> — link to 2–3 related pages on your site",
            "<strong>Featured image</strong> — with keyword-rich alt text",
        ], mt, _n(sn)),
        slide_content(m, "Using Rank Math in the Post Editor", """
<ul>
<li><strong>General tab</strong> — focus keyword, pillar content toggle</li>
<li><strong>Advanced tab</strong> — robots meta (usually leave default), canonical URL</li>
<li><strong>Schema tab</strong> — Article, FAQ, HowTo, Product (dropdown — no code)</li>
<li><strong>Social tab</strong> — Facebook/Twitter preview image and title</li>
<li><strong>Traffic light score</strong> — follow suggestions until green/orange</li>
</ul>
<div class="callout callout-tip"><strong>AEO tip</strong>Write a 40–60 word direct answer paragraph immediately after H1 — this targets featured snippets.</div>
""", mt, _n(sn)),
        slide_two_col(m, "Title & Meta Formulas (Copy-Paste Templates)",
                      "Blog post title templates", [
                          "How to [Keyword] in [Year] (Step-by-Step)",
                          "[Number] Best [Keyword] for [Audience]",
                          "What Is [Keyword]? Complete Guide",
                          "[Keyword] vs [Alternative]: Which to Choose?",
                      ],
                      "Meta description template", [
                          "Learn [keyword] with our [year] guide.",
                          "Covers [benefit 1], [benefit 2], and [benefit 3].",
                          "Perfect for [audience]. [CTA: Read now / Get started]",
                          "Keep under 155 characters total",
                      ], mt, _n(sn)),
        slide_content(m, "Schema Types — Select from Dropdown (No JSON-LD Coding)", """
<table class="data"><tr><th>Content type</th><th>Schema to select</th><th>Rich result</th></tr>
<tr><td>Blog tutorial</td><td>Article or HowTo</td><td>How-to rich results</td></tr>
<tr><td>FAQ page</td><td>FAQ (use FAQ block)</td><td>FAQ accordion in Google</td></tr>
<tr><td>Product page</td><td>Product</td><td>Price, availability in SERP</td></tr>
<tr><td>Local business page</td><td>LocalBusiness</td><td>Local pack signals</td></tr>
<tr><td>Recipe blog</td><td>Recipe</td><td>Recipe card in search</td></tr>
<tr><td>Review/comparison</td><td>Article + FAQ block</td><td>AI Overview + PAA</td></tr>
</table>
""", mt, _n(sn)),
        slide_workshop(m, "Workshop: Optimize 3 WordPress Pages", [
            "Pick 3 pages/posts on your site (or create new ones)",
            "Apply full on-page checklist to each in Rank Math/Yoast",
            "Add answer-first paragraph to one post (AEO prep)",
            "Set schema type appropriate to each page",
            "Preview Google snippet in plugin — screenshot all 3",
        ], "3 fully optimized pages with plugin scores documented", mt, _n(sn)),
        slide_summary(m, [
            "Apply per-page SEO checklist entirely within WordPress editor",
            "Use plugin metabox for titles, meta, schema — no code",
            "Write answer-first intros for AEO compatibility",
            "Select schema types from plugin dropdown menus",
        ], mt, _n(sn)),
    ]


def mod5(sn):
    m, mt = 5, MOD[4]
    return [
        slide_section(m, "Technical SEO Without Writing Code", "Sitemaps, speed, mobile, HTTPS — all handled by plugins."),
        slide_bullets(m, "Technical SEO Tasks → Plugin Solution", [
            "<strong>XML Sitemap</strong> → Rank Math / Yoast (automatic)",
            "<strong>Robots.txt</strong> → Rank Math → Edit robots.txt (visual editor)",
            "<strong>HTTPS/SSL</strong> → Hosting panel or Really Simple SSL plugin",
            "<strong>Page speed</strong> → LiteSpeed Cache or WP Rocket (toggle ON)",
            "<strong>Image compression</strong> → ShortPixel or Imagify plugin",
            "<strong>Broken links</strong> → Rank Math 404 Monitor + Redirection plugin",
            "<strong>Mobile-friendly</strong> → choose mobile-responsive theme (Astra, Kadence)",
        ], mt, _n(sn)),
        slide_content(m, "Speed Plugin Settings — Non-Coder Presets", """
<p class="lead">Install LiteSpeed Cache (free) OR WP Rocket (paid). Enable these toggles:</p>
<ul>
<li>✅ Enable Cache</li>
<li>✅ Browser Cache</li>
<li>✅ Lazy Load Images</li>
<li>✅ Minify CSS (test site after — disable if layout breaks)</li>
<li>✅ Minify JavaScript (same — test checkout if WooCommerce)</li>
<li>❌ Exclude: /cart/, /checkout/, /my-account/ from cache</li>
</ul>
<div class="callout"><strong>Test after enabling</strong>Visit site in incognito. Run PageSpeed Insights (Google, free). Target 80+ mobile score.</div>
""", mt, _n(sn)),
        slide_diagram(m, "Non-Coder Technical SEO Stack", """
  ┌─────────────────────────────────────────────────────────┐
  │           TECHNICAL SEO — PLUGIN ONLY                    │
  ├──────────────┬──────────────┬──────────────┬─────────────┤
  │ Rank Math    │ LiteSpeed    │ ShortPixel   │ Really      │
  │ Sitemap      │ Cache        │ Image compress│ Simple SSL  │
  │ Schema       │ Page speed   │ WebP convert │ HTTPS fix   │
  │ 404 Monitor  │ Lazy load    │ Bulk optimize│ Mixed content│
  └──────────────┴──────────────┴──────────────┴─────────────┘
         │              │              │              │
         └──────────────┴──────────────┴──────────────┘
                    NO CODE REQUIRED
""", [], mt, _n(sn)),
        slide_content(m, "Fix Common Issues Using Plugins Only", """
<table class="data"><tr><th>Problem in GSC</th><th>Plugin fix (no code)</th></tr>
<tr><td>Page not indexed</td><td>Rank Math → check noindex toggle on page → turn OFF</td></tr>
<tr><td>Duplicate title tags</td><td>Rank Math Titles & Meta → unique templates per type</td></tr>
<tr><td>404 errors</td><td>Rank Math 404 Monitor → Redirection → add 301 redirect</td></tr>
<tr><td>Slow LCP score</td><td>ShortPixel compress hero image + LiteSpeed cache ON</td></tr>
<tr><td>Not HTTPS</td><td>Really Simple SSL → Activate → Enable SSL</td></tr>
<tr><td>Missing schema</td><td>Rank Math Schema tab → select type on each page</td></tr>
</table>
""", mt, _n(sn)),
        slide_workshop(m, "Workshop: Technical SEO Plugin Sprint", [
            "Confirm sitemap live at yoursite.com/sitemap_index.xml",
            "Install cache plugin — enable recommended preset",
            "Install ShortPixel or Imagify — compress 10 images",
            "Check Search Console Coverage — fix 1 error using plugin",
            "Run PageSpeed before/after — record scores",
        ], "Technical SEO checklist completed + PageSpeed before/after", mt, _n(sn)),
        slide_content(m, "Site Kit by Google — All Google Tools in WordPress Sidebar", """
<ol class="steps">
<li>Plugins → Add New → install <strong>Site Kit by Google</strong></li>
<li>Activate → Start setup → connect Google account</li>
<li>Enable: Search Console, Analytics, PageSpeed modules</li>
<li>View GSC data on WordPress Dashboard — no tab switching</li>
<li>Use PageSpeed module to test URLs from wp-admin</li>
</ol>
<p class="lead">Best free plugin for non-coders who want Google data inside WordPress.</p>
""", mt, _n(sn)),
        slide_bullets(m, "Really Simple SSL + HTTPS (One-Click Fix)", [
            "Install <strong>Really Simple SSL</strong> from plugin directory",
            "Activate → click <strong>Go ahead, activate SSL!</strong>",
            "Plugin detects SSL certificate and configures WordPress",
            "Fixes mixed content warnings automatically",
            "Enables HTTPS redirect site-wide — no .htaccess editing",
            "Verify: padlock icon in browser address bar on your site",
        ], mt, _n(sn)),
        slide_summary(m, [
            "Handle technical SEO entirely through plugin settings",
            "Configure cache and image plugins with safe presets",
            "Fix GSC errors using SEO plugin tools",
            "Never edit code for standard technical SEO tasks",
        ], mt, _n(sn)),
    ]
