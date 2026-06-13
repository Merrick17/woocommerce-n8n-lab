#!/usr/bin/env python3
"""SEO/AEO/GEO WordPress course — modules 6-12."""
from wp_slide_framework import (
    slide_section, slide_content, slide_two_col, slide_bullets,
    slide_diagram, slide_workshop, slide_summary, callout,
)
from wp_seo_course_part1 import MOD, AUDIENCE, _n


def mod6(sn):
    m, mt = 6, MOD[5]
    return [
        slide_section(m, "Keyword Research & Content Planning", "Find what to write — plan in spreadsheets, publish in WordPress."),
        slide_bullets(m, "Free Keyword Research Tools (No Coding)", [
            "<strong>Google Search Console</strong> — queries you already rank for",
            "<strong>Google autocomplete</strong> — type keyword, note suggestions",
            "<strong>People Also Ask</strong> — every question = one blog post or FAQ",
            "<strong>AlsoAsked.com</strong> — free PAA question trees",
            "<strong>AnswerThePublic</strong> — question-based keyword ideas",
            "<strong>Rank Math Keyword Manager</strong> — track keywords in WP admin",
        ], mt, _n(sn)),
        slide_content(m, "Turn Keywords into WordPress Content Plan", """
<ol class="steps">
<li>Export top 20 queries from Google Search Console (Performance report)</li>
<li>Group similar queries into <strong>topic clusters</strong> in Google Sheets</li>
<li>Assign one <strong>pillar page</strong> (WordPress Page) per cluster</li>
<li>Assign <strong>supporting posts</strong> (WordPress Posts) for long-tail queries</li>
<li>In Rank Math → Keyword Manager → add target keywords per page</li>
<li>Schedule posts using WordPress built-in Schedule button</li>
</ol>
""", mt, _n(sn)),
        slide_two_col(m, "Search Intent → WordPress Content Type",
                      "Informational queries", [
                          "Create: How-to blog post",
                          "Format: H2 steps, numbered list",
                          "AEO: answer box in first paragraph",
                          "Plugin: FAQ block at bottom",
                          "Example: \"what is wordpress seo\"",
                      ],
                      "Commercial queries", [
                          "Create: Comparison or Best-of page",
                          "Format: Table block comparing options",
                          "GEO: clear pros/cons AI can cite",
                          "Plugin: Product schema if affiliate",
                          "Example: \"best seo plugin wordpress\"",
                      ], mt, _n(sn)),
        slide_workshop(m, "Workshop: Build a 30-Day Content Calendar", [
            "Research 10 keywords using GSC + People Also Ask",
            "Create Google Sheet: keyword | intent | page type | publish date",
            "Create 1 pillar Page in WordPress for main topic",
            "Outline 5 supporting Posts linked to pillar",
            "Add all keywords to Rank Math Keyword Manager",
        ], "Content calendar sheet + 1 pillar page draft in WordPress", mt, _n(sn)),
        slide_summary(m, [
            "Research keywords using free non-coder tools",
            "Map keywords to WordPress pages and posts",
            "Plan content clusters without any coding",
            "Track keywords in SEO plugin dashboard",
        ], mt, _n(sn)),
        slide_content(m, "Rank Math Keyword Manager — Track Rankings in WP Admin", """
<ol class="steps">
<li>Rank Math → <strong>Keyword Manager</strong> (enable module in Dashboard first)</li>
<li>Click <strong>Add Keyword</strong> → enter target keyword</li>
<li>Assign keyword to specific post or page from dropdown</li>
<li>Connect GSC — Rank Math shows position and clicks per keyword</li>
<li>Review monthly: keywords stuck on page 2 → optimize that post</li>
</ol>
<div class="callout callout-tip"><strong>Non-coder insight</strong>If GSC shows impressions but no clicks — rewrite meta description in Rank Math to be more compelling.</div>
""", mt, _n(sn)),
        slide_bullets(m, "Free Keyword Sources — No Tools to Buy", [
            "<strong>Google Search Console</strong> → Performance → Queries (your real data)",
            "<strong>Google autocomplete</strong> — type keyword letter by letter, note suggestions",
            "<strong>Related searches</strong> — bottom of Google results page",
            "<strong>People Also Ask</strong> — expand each question for more ideas",
            "<strong>Competitor pages</strong> — view their H2 headings for topic ideas (manual)",
            "<strong>Rank Math Content AI</strong> — suggest related keywords (edit before using)",
        ], mt, _n(sn)),
    ]


def mod7(sn):
    m, mt = 7, MOD[6]
    return [
        slide_section(m, "Local SEO with WordPress Plugins", "Rank in Google Maps — plugin wizards, no code."),
        slide_bullets(m, "Local SEO Stack for WordPress Non-Coders", [
            "<strong>Google Business Profile</strong> — claim listing (outside WordPress, essential)",
            "<strong>Rank Math Local SEO</strong> OR <strong>Yoast Local SEO</strong> — schema wizard",
            "<strong>NAP consistency</strong> — same Name, Address, Phone on Contact page + GBP",
            "<strong>WPForms contact page</strong> — embed map + local keywords",
            "<strong>LocalBusiness schema</strong> — filled via plugin form fields",
            "<strong>Review plugins</strong> — WP Business Reviews or Elfsight widget",
        ], mt, _n(sn)),
        slide_content(m, "Rank Math Local SEO — Click-by-Click", """
<ol class="steps">
<li>Rank Math → Dashboard → enable <strong>Local SEO</strong> module</li>
<li>Rank Math → Titles & Meta → Local → enter business name, address, phone</li>
<li>Select business type: LocalBusiness, Restaurant, Dentist, etc.</li>
<li>Add opening hours, price range, service area in form fields</li>
<li>Rank Math auto-adds LocalBusiness JSON-LD — you never see the code</li>
<li>Create Contact page with embedded Google Map block + matching NAP text</li>
</ol>
""", mt, _n(sn)),
        slide_two_col(m, "Local SEO Content in WordPress",
                      "Pages to create", [
                          "Location page: \"Plumber in [City]\"",
                          "Service area pages (one per neighborhood)",
                          "About page with local trust signals",
                          "Contact page with map + NAP + form",
                          "Testimonials page with schema",
                      ],
                      "Plugin helpers", [
                          "Rank Math → Local SEO module",
                          "Schema Pro → LocalBusiness (alternative)",
                          "Google Maps block in editor",
                          "WPForms → contact + lead capture",
                          "TrustIndex → Google reviews widget",
                      ], mt, _n(sn)),
        slide_workshop(m, "Workshop: Optimize Local WordPress Site", [
            "Enable Local SEO module in Rank Math/Yoast",
            "Fill all LocalBusiness fields in plugin wizard",
            "Create Contact page with map, NAP, and contact form",
            "Create one location-specific service page",
            "Verify local schema with Google Rich Results Test (paste URL)",
        ], "Local SEO plugin configured + Contact page + Rich Results Test screenshot", mt, _n(sn)),
        slide_summary(m, [
            "Configure LocalBusiness schema via plugin wizard only",
            "Maintain NAP consistency across WordPress and Google Business",
            "Create location pages using standard WordPress pages",
            "Validate schema with Google's free testing tool",
        ], mt, _n(sn)),
    ]


def mod8(sn):
    m, mt = 8, MOD[7]
    return [
        slide_section(m, "Answer Engine Optimization (AEO)", "Become the answer Google and voice assistants read aloud."),
        slide_bullets(m, "What Is AEO? (Plain English)", [
            "AEO = optimizing so search engines <strong>quote your content</strong> as the answer",
            "Targets: featured snippets, People Also Ask, voice search results",
            "WordPress method: structure content + FAQ schema via plugins",
            "No code — use headings, lists, FAQ blocks, and schema dropdowns",
            "AEO content answers ONE question clearly in the first paragraph",
        ], mt, _n(sn)),
        slide_diagram(m, "AEO Content Structure in WordPress", """
  H1: How to Install Rank Math on WordPress
  │
  ├── ANSWER BOX (40-60 words) ← AEO critical
  │     "To install Rank Math, go to Plugins → Add New,
  │      search Rank Math, click Install and Activate..."
  │
  ├── H2: Step 1 — Install the Plugin
  │     └── Numbered list block
  ├── H2: Step 2 — Run Setup Wizard
  ├── H2: Step 3 — Configure Sitemap
  └── FAQ Block (Rank Math) ← FAQ schema auto-added
        Q: Is Rank Math free?
        Q: Rank Math vs Yoast?
""", [
            "Answer box = featured snippet target",
            "Numbered lists win 'how to' snippets",
            "FAQ block adds schema without coding",
        ], mt, _n(sn)),
        slide_content(m, "AEO Writing Rules for Non-Coders", """
<ul>
<li><strong>Question as H1</strong> — match exactly what users search</li>
<li><strong>Direct answer first</strong> — 40–60 words, no fluff before the answer</li>
<li><strong>Numbered steps</strong> — use List block (ordered) for processes</li>
<li><strong>Definition paragraphs</strong> — \"X is...\" for \"what is X\" queries</li>
<li><strong>Comparison tables</strong> — Table block for \"X vs Y\" queries</li>
<li><strong>FAQ section</strong> — minimum 3 questions at bottom of every guide</li>
</ul>
<div class="callout callout-tip"><strong>Plugin assist</strong>Rank Math Content AI can generate FAQ questions — review and edit before publishing.</div>
""", mt, _n(sn)),
        slide_workshop(m, "Workshop: Write One Answer-First Article", [
            "Pick one 'how to' or 'what is' question from People Also Ask",
            "Create WordPress post — H1 = exact question",
            "Write 50-word direct answer as first paragraph",
            "Add 5+ numbered steps as H2 sections",
            "Add Rank Math FAQ block with 3 related questions at bottom",
            "Set schema: HowTo or FAQ — test in Rich Results Test",
        ], "1 AEO-optimized post published with FAQ schema verified", mt, _n(sn)),
        slide_content(m, "Voice Search AEO — Optimize Without Code", """
<ul>
<li><strong>Conversational H1s</strong> — \"How do I install an SEO plugin on WordPress?\" not \"SEO Plugin Install\"</li>
<li><strong>Short answers</strong> — voice reads one paragraph; keep answer box under 30 words for voice</li>
<li><strong>FAQ block</strong> — mirrors how people ask Alexa/Siri/Google Assistant</li>
<li><strong>Local voice queries</strong> — \"near me\" pages with LocalBusiness schema via Rank Math Local</li>
<li><strong>Speakable schema</strong> — Rank Math PRO adds speakable markup automatically</li>
</ul>
<div class="callout"><strong>Test it</strong>Ask your phone's Google Assistant your target question. See which site it reads. Match that format.</div>
""", mt, _n(sn)),
        slide_bullets(m, "AEO Plugin Quick Reference", [
            "<strong>Rank Math FAQ Block</strong> — FAQPage schema, free",
            "<strong>Rank Math HowTo schema</strong> — Schema tab → HowTo on tutorial posts",
            "<strong>Yoast FAQ block</strong> — Yoast Premium or Structured Content plugin",
            "<strong>Easy Accordion</strong> — visual FAQ layout + pair with Rank Math schema",
            "<strong>Table of Contents</strong> — Easy TOC plugin for long AEO guides",
            "<strong>Rich Results Test</strong> — search.google.com/test/rich-results (free validation)",
        ], mt, _n(sn)),
        slide_summary(m, [
            "Structure WordPress content for featured snippets",
            "Write answer-first paragraphs without coding",
            "Use FAQ blocks for automatic schema markup",
            "Apply AEO template to every how-to and what-is post",
        ], mt, _n(sn)),
    ]


def mod9(sn):
    m, mt = 9, MOD[8]
    return [
        slide_section(m, "Featured Snippets, FAQ & People Also Ask", "Win position zero using WordPress blocks and plugins."),
        slide_content(m, "Add FAQ Schema — Rank Math FAQ Block (No Code)", """
<ol class="steps">
<li>Edit any post or page in WordPress block editor</li>
<li>Click <strong>+</strong> → search \"Rank Math FAQ\"</li>
<li>Add Question → type question → Add Answer → type answer</li>
<li>Repeat for 3–8 questions</li>
<li>Publish — Rank Math adds FAQPage schema automatically</li>
<li>Test: Google Rich Results Test → paste URL → see FAQ detected</li>
</ol>
<p class="lead">Yoast users: Yoast FAQ block (Premium) or free plugin \"Structured Content\" works similarly.</p>
""", mt, _n(sn)),
        slide_two_col(m, "Snippet Type → WordPress Format",
                      "Paragraph snippet", [
                          "40–60 word definition after H1",
                          "Bold key term once",
                          "Use \"is defined as\" or \"refers to\"",
                          "Rank Math: mark as definitional content",
                      ],
                      "List / Table snippet", [
                          "Ordered list for steps (HowTo)",
                          "Unordered list for 'best tools' lists",
                          "Table block for comparisons",
                          "Keep list items parallel in structure",
                      ], mt, _n(sn)),
        slide_bullets(m, "People Also Ask (PAA) Strategy in WordPress", [
            "<strong>Step 1:</strong> Google your target keyword → copy all PAA questions",
            "<strong>Step 2:</strong> Each PAA question = one H2 in your post OR one FAQ item",
            "<strong>Step 3:</strong> Answer each in 2–3 sentences under its H2",
            "<strong>Step 4:</strong> Also add all as FAQ block items for schema",
            "<strong>Plugin:</strong> AlsoAsked export → paste into WordPress outline",
            "<strong>Result:</strong> one comprehensive post targets 10+ related questions",
        ], mt, _n(sn)),
        slide_workshop(m, "Workshop: PAA Domination Post", [
            "Google one target keyword — copy 8 People Also Ask questions",
            "Create WordPress post targeting main keyword",
            "Write H2 for each PAA question with 2-sentence answer",
            "Add all 8 as Rank Math FAQ block items too",
            "Submit URL to Google Search Console → Request Indexing",
        ], "1 PAA-optimized post covering 8 related questions", mt, _n(sn)),
        slide_summary(m, [
            "Add FAQ schema using Rank Math FAQ block — zero code",
            "Format content for paragraph, list, and table snippets",
            "Use PAA questions as content outline in WordPress",
            "Validate rich results with Google's free test tool",
        ], mt, _n(sn)),
    ]


def mod10(sn):
    m, mt = 10, MOD[9]
    return [
        slide_section(m, "Google AI Overviews Optimization", "Get cited in Google's AI-generated answers."),
        slide_bullets(m, "How AI Overviews Choose Sources", [
            "Google AI Overviews pull from pages already ranking well",
            "Prefer <strong>clear, factual, well-structured</strong> content",
            "Lists, tables, and definitions are heavily cited",
            "E-E-A-T signals matter — author bio, About page, credentials",
            "WordPress fix: structure + schema via plugins, not code",
        ], mt, _n(sn)),
        slide_content(m, "WordPress Checklist for AI Overview Eligibility", """
<ul class="checklist">
<li>Page indexed in Google (check Search Console)</li>
<li>Rank Math score green/orange on target page</li>
<li>Answer-first paragraph present (40–60 words)</li>
<li>FAQ schema on page (FAQ block)</li>
<li>Author name + bio visible (Author box plugin or theme)</li>
<li>Page loads fast (cache plugin enabled, PageSpeed 80+)</li>
<li>Content updated within last 12 months (show current year in title)</li>
<li>Internal links from other indexed pages on your site</li>
</ul>
""", mt, _n(sn)),
        slide_two_col(m, "Content Formats AI Overviews Prefer",
                      "High citation formats", [
                          "Step-by-step tutorials (HowTo schema)",
                          "Comparison tables (Table block)",
                          "Definition + expanded explanation",
                          "Statistics with cited sources",
                          "Expert quotes with attribution",
                      ],
                      "WordPress plugins to help", [
                          "Rank Math HowTo schema (dropdown)",
                          "Tableberg or native Table block",
                          "Simple Author Box plugin",
                          "Easy Table of Contents plugin",
                          "Last Updated date plugin (shows freshness)",
                      ], mt, _n(sn)),
        slide_workshop(m, "Workshop: Optimize One Page for AI Overviews", [
            "Pick your highest-traffic WordPress page from GSC",
            "Add answer-first paragraph + update year in title",
            "Add HowTo or FAQ schema via Rank Math",
            "Add author bio box at bottom of post",
            "Add Table of Contents plugin for long content",
            "Re-submit URL in Search Console",
        ], "Before/after screenshot of optimized page + schema test result", mt, _n(sn)),
        slide_summary(m, [
            "Understand what makes WordPress content AI Overview eligible",
            "Apply non-coder checklist for AI-friendly structure",
            "Use schema plugins for HowTo and FAQ markup",
            "Maintain E-E-A-T signals with author and freshness plugins",
        ], mt, _n(sn)),
    ]


def mod11(sn):
    m, mt = 11, MOD[10]
    return [
        slide_section(m, "GEO — Generative Engine Optimization", "Get cited by ChatGPT, Perplexity, Gemini, and Claude."),
        slide_bullets(m, "GEO vs SEO — What's Different for WordPress Users?", [
            "<strong>SEO</strong> = rank high on Google results page",
            "<strong>GEO</strong> = be the website AI tools quote and link to",
            "AI tools retrieve from authoritative, clear, structured pages",
            "WordPress advantage: publish detailed guides AI can parse easily",
            "No special GEO plugin needed — Rank Math + great content structure",
        ], mt, _n(sn)),
        slide_diagram(m, "Why AI Cites Some WordPress Sites and Ignores Others", """
  AI RETRIEVAL PREFERENCES
  ─────────────────────────────────────────────────────
  ✅ CITED                    ❌ IGNORED
  ─────────────────────────────────────────────────────
  Clear H2/H3 structure       Wall of text, no headings
  Defined terms upfront       Vague marketing fluff
  Author + date visible       Anonymous, outdated content
  FAQ with direct answers     No structured Q&A
  Comparison tables           Thin affiliate pages
  .edu/.gov + major brands    Unknown domains (until authority built)
  Regularly updated           Last modified 2019
  ─────────────────────────────────────────────────────
""", [
            "GEO is earned through content quality and structure",
            "Plugins help with schema, TOC, author box — not magic buttons",
        ], mt, _n(sn)),
        slide_content(m, "GEO Content Template for WordPress (Copy This Structure)", """
<ol class="steps">
<li><strong>H1:</strong> Clear topic title with year</li>
<li><strong>Intro:</strong> 2-sentence summary of what page covers (AI quotable)</li>
<li><strong>H2: What is [Topic]?</strong> — 3-sentence definition</li>
<li><strong>H2: Key Features / Benefits</strong> — bullet list</li>
<li><strong>H2: [Topic] vs [Alternative]</strong> — comparison table</li>
<li><strong>H2: How to [Action]</strong> — numbered steps</li>
<li><strong>H2: FAQ</strong> — Rank Math FAQ block, 5+ questions</li>
<li><strong>Author box + last updated date</strong> — E-E-A-T signals</li>
</ol>
""", mt, _n(sn)),
        slide_two_col(m, "Test Your GEO Visibility (Free, No Code)",
                      "Manual tests monthly", [
                          "Ask ChatGPT (browse on): your target question",
                          "Ask Perplexity: same question — note cited URLs",
                          "Ask Gemini: who does it recommend?",
                          "Record: Are you cited? Which competitor is?",
                          "Track in Google Sheet monthly",
                      ],
                      "Improve if not cited", [
                          "Add comparison table to existing post",
                          "Expand FAQ section to 8+ questions",
                          "Add author credentials on About page",
                          "Update publish date + add new statistics",
                          "Build internal links from other posts",
                      ], mt, _n(sn)),
        slide_workshop(m, "Workshop: GEO Audit & Content Upgrade", [
            "Pick 3 target questions relevant to your WordPress site",
            "Test all 3 in Perplexity — record who gets cited",
            "Upgrade your WordPress page using GEO template above",
            "Add FAQ block + comparison table + author box",
            "Re-test in 7 days — document citation changes",
        ], "GEO tracking sheet + 1 upgraded page with full template", mt, _n(sn)),
        slide_content(m, "GEO Plugins & WordPress Settings That Help", """
<ul>
<li><strong>Rank Math FAQ block</strong> — Q&A format AI tools love to parse</li>
<li><strong>Easy Table of Contents</strong> — clear document structure for AI retrieval</li>
<li><strong>Simple Author Box</strong> — E-E-A-T: show who wrote the content</li>
<li><strong>WP Last Modified Info</strong> — display \"Updated [date]\" for freshness signals</li>
<li><strong>Rank Math Schema → Article</strong> — author, datePublished, dateModified auto-added</li>
<li><strong>No GEO plugin replaces bad content</strong> — structure + depth win citations</li>
</ul>
""", mt, _n(sn)),
        slide_bullets(m, "Content Patterns AI Tools Cite Most Often", [
            "<strong>\"Best X for Y\" lists</strong> — use Table block with pros/cons columns",
            "<strong>Step-by-step guides</strong> — HowTo schema + numbered List block",
            "<strong>Definitions</strong> — \"[Term] is...\" in first sentence under H2",
            "<strong>Statistics</strong> — cite source with link (AI verifies claims)",
            "<strong>Expert quotes</strong> — blockquote block with attribution",
            "<strong>Original data</strong> — even simple surveys your brand ran",
        ], mt, _n(sn)),
        slide_summary(m, [
            "Explain GEO and how it differs from traditional SEO",
            "Apply GEO content template in WordPress without code",
            "Test AI citation visibility monthly across ChatGPT and Perplexity",
            "Improve structure and E-E-A-T to increase AI citations",
        ], mt, _n(sn)),
    ]


def mod12(sn):
    m, mt = 12, MOD[11]
    return [
        slide_section(m, "WooCommerce SEO for Non-Coders", "Product pages, categories, and shop SEO via plugins."),
        slide_bullets(m, "WooCommerce + Rank Math — Product SEO Checklist", [
            "<strong>Product title</strong> — include product name + key attribute",
            "<strong>Short description</strong> — 1–2 sentences with main keyword",
            "<strong>Long description</strong> — H2 sections, benefits, FAQ block",
            "<strong>Product schema</strong> — Rank Math auto-adds when SEO plugin active",
            "<strong>Product image alt text</strong> — describe product in Media Library",
            "<strong>Category descriptions</strong> — WooCommerce → Products → Categories → write SEO text",
        ], mt, _n(sn)),
        slide_content(m, "WooCommerce SEO Plugin Settings", """
<ul>
<li><strong>Rank Math → General → WooCommerce</strong> — remove /product-category/ base (optional, cleaner URLs)</li>
<li><strong>Rank Math → Schema → Product</strong> — enable product rich snippets</li>
<li><strong>Noindex cart/checkout</strong> — Rank Math → Titles & Meta → Cart/Checkout → noindex ON</li>
<li><strong>Product SEO metabox</strong> — same as posts: focus keyword, title, meta per product</li>
<li><strong>Google Listings & Ads plugin</strong> — sync products to Google Merchant Center (free)</li>
</ul>
<div class="callout callout-warn"><strong>Cache reminder</strong>Exclude /cart/ and /checkout/ in cache plugin or payments break.</div>
""", mt, _n(sn)),
        slide_workshop(m, "Workshop: Optimize 5 WooCommerce Products", [
            "Install Rank Math + verify WooCommerce module active",
            "Optimize 5 products: title, short desc, long desc, alt text",
            "Write SEO description for 2 product categories",
            "Enable product schema — test one URL in Rich Results Test",
            "Noindex cart and checkout pages in Rank Math",
        ], "5 optimized products + category descriptions + schema test", mt, _n(sn)),
        slide_summary(m, [
            "Apply SEO plugin checklist to WooCommerce products",
            "Configure product schema and URL settings via plugin",
            "Noindex non-SEO WooCommerce system pages",
            "Sync products to Google with Listings & Ads plugin",
        ], mt, _n(sn)),
    ]


def get_modules_6_12(sn):
    return (
        mod6(sn) + mod7(sn) + mod8(sn) + mod9(sn) +
        mod10(sn) + mod11(sn) + mod12(sn)
    )
