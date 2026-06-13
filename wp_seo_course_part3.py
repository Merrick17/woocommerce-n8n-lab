#!/usr/bin/env python3
"""SEO/AEO/GEO WordPress course — modules 13-18 + appendix + builder."""
from wp_slide_framework import (
    slide_cover, slide_toc, slide_section, slide_content, slide_two_col,
    slide_bullets, slide_diagram, slide_workshop, slide_summary, callout,
    wrap_deck, esc,
)
from wp_seo_course_part1 import mod1, mod2, mod3, mod4, mod5, TOC, MOD, AUDIENCE, _n
from wp_seo_course_part2 import get_modules_6_12


def mod13(sn):
    m, mt = 13, MOD[12]
    return [
        slide_section(m, "Image, Video & Media SEO", "Alt text, compression, and video embeds — all in WordPress admin."),
        slide_bullets(m, "Image SEO for Non-Coders", [
            "<strong>Before upload:</strong> rename file descriptively: blue-running-shoes.jpg",
            "<strong>Alt text field</strong> — Media Library → click image → fill Alt Text (required)",
            "<strong>Compress plugin</strong> — ShortPixel or Imagify → auto-compress on upload",
            "<strong>WebP conversion</strong> — enable in ShortPixel settings toggle",
            "<strong>Lazy load</strong> — on by default in WordPress 5.5+ and cache plugins",
            "<strong>Image SEO in Rank Math</strong> — auto-adds alt attributes if missing (toggle ON)",
        ], mt, _n(sn)),
        slide_content(m, "Video SEO Without Hosting Video on Your Server", """
<ol class="steps">
<li>Upload video to <strong>YouTube</strong> (free, Google-owned = SEO benefit)</li>
<li>In WordPress editor → Add block → <strong>YouTube</strong> → paste URL</li>
<li>Write keyword-rich text <strong>around</strong> the embed (Google indexes surrounding text)</li>
<li>Add FAQ block below video answering questions the video covers</li>
<li>YouTube: fill title, description, tags with target keywords</li>
<li>Link from WordPress post to YouTube and vice versa</li>
</ol>
""", mt, _n(sn)),
        slide_workshop(m, "Workshop: Media SEO Audit", [
            "Install ShortPixel or Imagify — enable auto-compress",
            "Audit 20 images — fill all missing alt text",
            "Enable Rank Math → Image SEO → Add missing alt attributes",
            "Embed one YouTube video in a post with keyword-rich context",
            "Run PageSpeed — record image-related improvements",
        ], "20 images optimized + 1 video embed post published", mt, _n(sn)),
        slide_content(m, "Rank Math Image SEO Module — Bulk Fix Alt Text", """
<ol class="steps">
<li>Rank Math → General Settings → <strong>Images</strong> tab</li>
<li>Enable <strong>Add missing ALT attributes</strong></li>
<li>Enable <strong>Add missing TITLE attributes</strong> (optional)</li>
<li>Rank Math uses focus keyword as alt fallback on new uploads</li>
<li>For existing images: Media Library → bulk select → use plugin bulk tools</li>
<li>Pair with ShortPixel for compression + Rank Math for alt = full image SEO</li>
</ol>
""", mt, _n(sn)),
        slide_summary(m, [
            "Optimize images using Media Library alt text and compression plugins",
            "Never skip alt text — critical for image SEO and accessibility",
            "Embed YouTube videos instead of self-hosting large files",
            "Use Rank Math Image SEO module for bulk alt attribute fixes",
        ], mt, _n(sn)),
    ]


def mod14(sn):
    m, mt = 14, MOD[13]
    return [
        slide_section(m, "Internal Linking & Content Clusters", "Connect content for topical authority — plugin-assisted, no code."),
        slide_bullets(m, "Why Internal Links Matter for SEO/AEO/GEO", [
            "Help Google discover and understand your content hierarchy",
            "Pass authority from popular pages to new pages",
            "Keep visitors on site longer (behavioral SEO signal)",
            "Help AI tools understand your site as a topic authority",
            "WordPress method: manual links + Link Whisper or Rank Math suggestions",
        ], mt, _n(sn)),
        slide_diagram(m, "Topic Cluster in WordPress", """
              PILLAR PAGE (WordPress Page)
              "Complete WordPress SEO Guide"
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   Cluster Post    Cluster Post    Cluster Post
   "SEO Titles"    "XML Sitemap"   "FAQ Schema"
        │               │               │
        └───────────────┴───────────────┘
              All link back to Pillar
              Pillar links to all cluster posts
""", [
            "Create pillar as WordPress Page (evergreen)",
            "Create clusters as Posts (specific subtopics)",
            "Link every cluster post to pillar in first 2 paragraphs",
        ], mt, _n(sn)),
        slide_two_col(m, "Internal Linking Tools for Non-Coders",
                      "Free methods", [
                          "Manual link while writing (Ctrl+K in editor)",
                          "Rank Math → Link Suggestions in sidebar",
                          "WordPress \"Related Posts\" plugin",
                          "Table of Contents with anchor links",
                          "Navigation menu linking pillar pages",
                      ],
                      "Premium helpers", [
                          "Link Whisper — AI link suggestions in editor",
                          "Rank Math PRO — internal link counter",
                          "Yoast Premium — internal linking tool",
                          "Internal Link Juicer (automated rules)",
                          "All work inside WordPress editor — no code",
                      ], mt, _n(sn)),
        slide_workshop(m, "Workshop: Build One Topic Cluster", [
            "Choose one main topic for your site",
            "Create 1 pillar Page (1500+ words, comprehensive)",
            "Create 4 cluster Posts (500+ words each, specific subtopics)",
            "Add internal link from each cluster to pillar (in intro)",
            "Add links from pillar to all 4 cluster posts",
            "Use Rank Math Link Suggestions to find 3 more link opportunities",
        ], "1 pillar + 4 cluster posts fully interlinked", mt, _n(sn)),
        slide_summary(m, [
            "Build topic clusters using WordPress pages and posts",
            "Use plugin link suggestions instead of manual site audits",
            "Connect pillar and cluster content with internal links",
            "Establish topical authority for SEO, AEO, and GEO",
        ], mt, _n(sn)),
    ]


def mod15(sn):
    m, mt = 15, MOD[14]
    return [
        slide_section(m, "Analytics & Monitoring", "Google Search Console and Rank Math — read your SEO results without code."),
        slide_bullets(m, "Google Search Console — What to Check Weekly", [
            "<strong>Performance</strong> — clicks, impressions, average position trending up?",
            "<strong>Pages</strong> — which WordPress URLs get most traffic?",
            "<strong>Queries</strong> — unexpected keywords to create content for?",
            "<strong>Indexing → Pages</strong> — any \"Not indexed\" errors to fix?",
            "<strong>Experience → Core Web Vitals</strong> — any poor URLs? → fix with cache plugin",
            "<strong>Sitemaps</strong> — sitemap submitted and processed?",
        ], mt, _n(sn)),
        slide_content(m, "Rank Math Analytics Dashboard (No Code Reporting)", """
<ul>
<li><strong>Rank Math → Analytics → Dashboard</strong> — traffic overview in WP admin</li>
<li><strong>Keyword Manager</strong> — track ranking positions for target keywords</li>
<li><strong>SEO Score</strong> — sitewide content optimization percentage</li>
<li><strong>Google Site Kit plugin</strong> — alternative: GSC + Analytics in WP sidebar</li>
<li><strong>Monthly routine:</strong> export GSC Performance CSV → share with client/stakeholder</li>
</ul>
<div class="callout callout-tip"><strong>Non-coder KPIs</strong>Clicks up? Impressions up? Average position improving? Pages indexed increasing? That's SEO success.</div>
""", mt, _n(sn)),
        slide_two_col(m, "Fix Indexing Issues Using Plugins Only",
                      "GSC error", [
                          "Discovered — not indexed",
                          "Duplicate without canonical",
                          "Excluded by noindex tag",
                          "Crawled — currently not indexed",
                          "Soft 404",
                      ],
                      "Plugin fix", [
                          "Improve content length + request indexing",
                          "Rank Math → set canonical on duplicate",
                          "Rank Math Advanced → remove noindex checkbox",
                          "Add internal links + update content quality",
                          "301 redirect via Rank Math Redirection module",
                      ], mt, _n(sn)),
        slide_workshop(m, "Workshop: Monthly SEO Report from WordPress", [
            "Open Google Search Console Performance — last 28 days",
            "Record: total clicks, impressions, avg position, top 5 pages",
            "Check Indexing report — fix 1 issue using Rank Math",
            "Check Rank Math SEO Score — optimize lowest-scoring page",
            "Create 1-page monthly report in Google Docs with screenshots",
        ], "Monthly SEO report template filled with real GSC data", mt, _n(sn)),
        slide_summary(m, [
            "Monitor SEO performance weekly in Google Search Console",
            "Use Rank Math or Site Kit dashboard inside WordPress",
            "Fix indexing errors using plugin settings only",
            "Produce simple monthly SEO reports for clients or stakeholders",
        ], mt, _n(sn)),
    ]


def mod16(sn):
    m, mt = 16, MOD[15]
    return [
        slide_section(m, "AI Content Tools Inside WordPress", "Draft and optimize content with AI plugins — human review required."),
        slide_two_col(m, "AI Plugins for WordPress Non-Coders",
                      "Rank Math Content AI", [
                          "Generate SEO titles and meta descriptions",
                          "Suggest focus keywords",
                          "Write FAQ questions for your topic",
                          "Expand bullet points into paragraphs",
                          "Built into Rank Math — no extra install",
                      ],
                      "AI Engine / AI Power", [
                          "ChatGPT-style writing in WP editor",
                          "Generate full blog post drafts",
                          "Create product descriptions (WooCommerce)",
                          "Requires OpenAI API key (paid, low cost)",
                          "Always human-edit before publishing",
                      ], mt, _n(sn)),
        slide_content(m, "Safe AI Content Workflow for SEO/AEO/GEO", """
<ol class="steps">
<li><strong>Human:</strong> Choose keyword and search intent</li>
<li><strong>AI plugin:</strong> Generate outline or first draft</li>
<li><strong>Human:</strong> Add real examples, facts, and brand voice</li>
<li><strong>Human:</strong> Add answer-first paragraph (AEO)</li>
<li><strong>Human:</strong> Add FAQ block with verified answers</li>
<li><strong>Rank Math:</strong> Optimize title, meta, schema</li>
<li><strong>Human:</strong> Final read — publish</li>
</ol>
<div class="callout callout-warn"><strong>Never publish raw AI content</strong>Google and AI tools penalize unedited, generic AI pages. Always add human expertise.</div>
""", mt, _n(sn)),
        slide_workshop(m, "Workshop: AI-Assisted SEO Article", [
            "Pick target keyword from your content calendar",
            "Use Rank Math Content AI to generate title + meta + FAQ ideas",
            "Draft post body with AI Engine OR write manually with AI outline",
            "Human-edit: add answer box, statistics, personal insight",
            "Complete Rank Math checklist → publish",
            "Submit to Search Console → Request Indexing",
        ], "1 AI-assisted, human-edited, fully optimized WordPress post", mt, _n(sn)),
        slide_summary(m, [
            "Use AI plugins to accelerate WordPress content creation",
            "Always human-edit AI drafts for E-E-A-T and accuracy",
            "Combine AI tools with Rank Math optimization workflow",
            "Maintain AEO/GEO structure even on AI-assisted content",
        ], mt, _n(sn)),
    ]


def mod17(sn):
    m, mt = 17, MOD[16]
    return [
        slide_section(m, "No-Code SEO Automation", "n8n, Zapier, and Uncanny Automator — automate SEO tasks without coding."),
        slide_bullets(m, "SEO Tasks You Can Automate (No Code)", [
            "<strong>New post published</strong> → auto-post to social media (Uncanny Automator)",
            "<strong>Form submitted</strong> → add row to Google Sheets (WPForms + Zapier)",
            "<strong>Weekly GSC report</strong> → email via n8n scheduled workflow",
            "<strong>404 detected</strong> → Slack alert (Wordfence + n8n webhook)",
            "<strong>New WooCommerce product</strong> → notify team in Slack",
            "<strong>Backup complete</strong> → log date in maintenance spreadsheet",
        ], mt, _n(sn)),
        slide_content(m, "Uncanny Automator — SEO Recipes (Inside WordPress)", """
<p class="lead">Install Uncanny Automator — build recipes with dropdowns, zero code:</p>
<ul>
<li><strong>Recipe 1:</strong> User publishes post → Send email to editor for review</li>
<li><strong>Recipe 2:</strong> WPForms submission → Add user to Mailchimp list</li>
<li><strong>Recipe 3:</strong> Post published → Post to Facebook Page</li>
<li><strong>Recipe 4:</strong> Rank Math score reaches 80 → Notify admin (advanced)</li>
</ul>
<div class="callout"><strong>Best for non-coders</strong>Uncanny Automator lives inside wp-admin — no external servers needed.</div>
""", mt, _n(sn)),
        slide_diagram(m, "n8n + WordPress SEO Automation (Visual, No Code)", """
  WordPress                    n8n (visual builder)           Output
  ─────────                    ────────────────────           ──────
  WPForms webhook    ──▶      Parse submission      ──▶     Google Sheet row
  New post (REST)    ──▶      Filter by category    ──▶     LinkedIn post
  Schedule trigger   ──▶      Check site URL        ──▶     Email if down
  Rank Math sitemap  ──▶      Weekly schedule       ──▶     SEO report email
""", [
            "n8n uses drag-and-drop nodes — no programming",
            "Connect WordPress via Application Password (Users → Profile)",
            "Use WPForms/Fluent Forms webhook nodes for form automation",
        ], mt, _n(sn)),
        slide_workshop(m, "Workshop: Build One SEO Automation", [
            "Option A: Install Uncanny Automator → create \"post published → email\" recipe",
            "Option B: WPForms webhook → n8n → Google Sheets on form submit",
            "Test automation 3 times — verify it fires correctly",
            "Document automation in your site management doc",
            "Screenshot workflow/recipe as proof of setup",
        ], "1 working no-code automation documented with screenshot", mt, _n(sn)),
        slide_summary(m, [
            "Automate repetitive SEO tasks without writing code",
            "Use Uncanny Automator for in-WordPress automations",
            "Connect WordPress to n8n/Zapier via webhooks and Application Passwords",
            "Document all automations for site maintenance records",
        ], mt, _n(sn)),
    ]


def mod18(sn):
    m, mt = 18, MOD[17]
    return [
        slide_section(m, "Capstone: Complete SEO/AEO/GEO WordPress Site", "Apply everything — plugins only, zero code."),
        slide_content(m, "Capstone Requirements (Non-Coder Track)", """
<ul>
<li><strong>WordPress site live</strong> with HTTPS, Post name permalinks</li>
<li><strong>Rank Math OR Yoast</strong> — fully configured wizard + GSC connected</li>
<li><strong>1 topic cluster</strong> — 1 pillar page + 4 interlinked posts</li>
<li><strong>3 AEO posts</strong> — answer-first + FAQ block + schema verified</li>
<li><strong>1 GEO-optimized guide</strong> — comparison table + FAQ + author box</li>
<li><strong>Local SEO OR WooCommerce SEO</strong> — one track completed</li>
<li><strong>Cache + image plugin</strong> — PageSpeed mobile 70+ minimum</li>
<li><strong>1 no-code automation</strong> — Automator or n8n workflow</li>
<li><strong>Monthly SEO report</strong> — GSC screenshot + narrative</li>
</ul>
""", mt, _n(sn)),
        slide_two_col(m, "Capstone Deliverables",
                      "Submit", [
                          "Live site URL",
                          "5-min screen recording walking through wp-admin SEO setup",
                          "Plugin list with purpose of each",
                          "GSC Performance screenshot (28 days)",
                          "Rich Results Test screenshot for FAQ page",
                          "GEO test: Perplexity query + citation result",
                      ],
                      "Graded on", [
                          "SEO plugin configuration completeness",
                          "On-page optimization quality (Rank Math scores)",
                          "AEO structure (answer box + FAQ schema)",
                          "GEO content template applied correctly",
                          "Technical SEO (speed, sitemap, indexing)",
                          "Documentation and report professionalism",
                      ], mt, _n(sn)),
        slide_content(m, "4-Week Capstone Schedule for Non-Coders", """
<table class="data"><tr><th>Week</th><th>Focus</th><th>Plugins used</th></tr>
<tr><td>Week 1</td><td>WP setup + SEO plugin wizard + GSC</td><td>Rank Math, Site Kit</td></tr>
<tr><td>Week 2</td><td>On-page SEO + topic cluster content</td><td>Rank Math, Link Whisper</td></tr>
<tr><td>Week 3</td><td>AEO posts + GEO guide + local/woo track</td><td>Rank Math FAQ, ShortPixel</td></tr>
<tr><td>Week 4</td><td>Speed plugins + automation + report + present</td><td>LiteSpeed, Automator/n8n</td></tr>
</table>
<div class="callout callout-tip"><strong>You never need to code</strong>Every capstone requirement is achievable using only WordPress admin and plugins.</div>
""", mt, _n(sn)),
        slide_summary(m, [
            "Deliver a complete SEO/AEO/GEO optimized WordPress site",
            "Prove all techniques applied via plugins without code",
            "Present capstone with GSC data and AI citation tests",
            "Earn certification as a WordPress SEO/AEO/GEO practitioner",
        ], mt, _n(sn)),
    ]


def appendix(sn):
    m, mt = 25, "Appendix"
    seo_chk = [
        "Rank Math or Yoast installed — wizard complete, only ONE active",
        "Google Search Console connected and sitemap submitted",
        "Permalinks set to Post name",
        "Homepage SEO title and meta description written",
        "Every post has focus keyword, title, meta, and alt text on images",
        "XML sitemap loading at /sitemap_index.xml",
        "Cache plugin enabled with WooCommerce exclusions if applicable",
        "Image compression plugin active (ShortPixel/Imagify)",
        "404 monitor ON — broken links redirected",
        "Site loads on HTTPS",
    ]
    aeo_chk = [
        "Answer-first paragraph (40–60 words) on every how-to post",
        "FAQ block added to all guide posts (minimum 3 questions)",
        "FAQ schema verified in Google Rich Results Test",
        "H1 matches target question for AEO posts",
        "Numbered lists used for all step-by-step content",
        "People Also Ask questions covered as H2 or FAQ items",
        "Table of Contents on posts over 1500 words",
        "Author name and bio visible on all posts",
    ]
    geo_chk = [
        "Comparison tables on all 'best of' and 'vs' pages",
        "Clear definitions ('X is...') on all 'what is' pages",
        "Content updated with current year in titles",
        "E-E-A-T: About page with credentials and experience",
        "Test monthly in Perplexity and ChatGPT — track citations",
        "Internal links connect all related content",
        "No thin pages under 500 words targeting competitive terms",
        "Statistics and sources cited in content (with links)",
    ]
    glossary = [
        ("AEO", "Answer Engine Optimization — optimizing to appear in featured snippets and direct answers"),
        ("GEO", "Generative Engine Optimization — optimizing to be cited by AI tools like ChatGPT"),
        ("SERP", "Search Engine Results Page — what Google shows after a search"),
        ("Featured Snippet", "Answer box at top of Google — position zero"),
        ("Schema", "Structured data — plugin adds this automatically via FAQ/Article blocks"),
        ("Sitemap", "XML file listing all your pages — Rank Math creates it automatically"),
        ("Focus Keyword", "Main search term you want a page to rank for — set in Rank Math/Yoast"),
        ("Meta Description", "Short summary under title in Google — write in SEO plugin metabox"),
        ("NAP", "Name, Address, Phone — must match everywhere for local SEO"),
        ("E-E-A-T", "Experience, Expertise, Authoritativeness, Trust — show via author bios and About page"),
        ("GSC", "Google Search Console — free tool showing your search performance"),
        ("Noindex", "Tells Google not to show a page in results — toggle in Rank Math Advanced tab"),
        ("Canonical", "Preferred URL when duplicates exist — set automatically by SEO plugin"),
        ("Internal Link", "Link from one page on your site to another page on your site"),
        ("Topic Cluster", "One pillar page + related posts all interlinked on one subject"),
    ]
    gl = "".join(f"<tr><td><strong>{esc(t)}</strong></td><td>{esc(d)}</td></tr>" for t, d in glossary)
    s = "".join(f"<li>{esc(c)}</li>" for c in seo_chk)
    a = "".join(f"<li>{esc(c)}</li>" for c in aeo_chk)
    g = "".join(f"<li>{esc(c)}</li>" for c in geo_chk)

    return [
        slide_section(m, "Appendix — Checklists & Glossary", "Print these — use on every WordPress SEO project."),
        slide_content(m, "SEO Checklist (Plugin-Based, No Code)", f"<ul class='checklist'>{s}</ul>", mt, _n(sn)),
        slide_content(m, "AEO Checklist — Featured Snippets & FAQ", f"<ul class='checklist'>{a}</ul>", mt, _n(sn)),
        slide_content(m, "GEO Checklist — AI Citation Optimization", f"<ul class='checklist'>{g}</ul>", mt, _n(sn)),
        slide_content(m, "Glossary for Non-Coders", f"<table class='data'><tr><th>Term</th><th>Plain English Definition</th></tr>{gl}</table>", mt, _n(sn)),
        slide_content(m, "Your Non-Coder Plugin Stack — Final Reference", """
<table class="data"><tr><th>Need</th><th>Plugin</th><th>Free?</th></tr>
<tr><td>SEO hub</td><td>Rank Math SEO</td><td>Yes (Pro optional)</td></tr>
<tr><td>Alternative SEO</td><td>Yoast SEO</td><td>Yes (Premium optional)</td></tr>
<tr><td>Google data in WP</td><td>Site Kit by Google</td><td>Yes</td></tr>
<tr><td>Speed</td><td>LiteSpeed Cache</td><td>Yes</td></tr>
<tr><td>Images</td><td>ShortPixel</td><td>Freemium</td></tr>
<tr><td>SSL fix</td><td>Really Simple SSL</td><td>Yes</td></tr>
<tr><td>Forms</td><td>WPForms Lite</td><td>Yes</td></tr>
<tr><td>Automation</td><td>Uncanny Automator</td><td>Freemium</td></tr>
<tr><td>Author box</td><td>Simple Author Box</td><td>Yes</td></tr>
<tr><td>Table of contents</td><td>Easy Table of Contents</td><td>Yes</td></tr>
</table>
<p class="lead">Install only what you need. One plugin per job. No coding at any step.</p>
""", mt, _n(sn)),
    ]


def build_all_slides():
    sn = [0]
    slides = [
        slide_cover(
            "SEO, AEO & GEO on WordPress",
            "Apply Search Optimization with Plugins — No Coding Required",
            [
                "For Non-Coders · Freelancers · Marketers · Entrepreneurs · Content Creators",
                "Rank Math · Yoast · FAQ Schema · Local SEO · AI Overviews · GEO Citations",
                "18 Modules · 125+ Slides · Plugin-Only Hands-On Workshops",
            ],
        ),
        slide_toc(TOC),
    ]
    builders = [
        mod1, mod2, mod3, mod4, mod5,
        lambda s: get_modules_6_12(s),
        mod13, mod14, mod15, mod16, mod17, mod18,
        appendix,
    ]
    for fn in builders:
        slides.extend(fn(sn))
    slides.append(slide_cover(
        "Congratulations!",
        "You Can SEO Any WordPress Site — Without Writing Code",
        ["Certification · Capstone Review · Advanced Plugin Modules"],
    ))
    return wrap_deck("\n".join(slides), "SEO, AEO & GEO on WordPress — Non-Coder Course")
