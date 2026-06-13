#!/usr/bin/env python3
"""Course modules 2-8 HTML content for the SEO/AEO/GEO mastery course."""
import html as html_lib


def esc(s):
    return html_lib.escape(str(s))


def diagram(text):
    return f'<pre class="diagram">{esc(text)}</pre>'


def lesson(num, title, body):
    return f'<h3>Lesson {num}: {esc(title)}</h3>\n{body}\n'


def case_study(title, content):
    return f'<div class="case-study"><strong>Case Study: {esc(title)}</strong>{content}</div>'


def mistake(content):
    return f'<div class="mistake"><strong>Mistakes to Avoid:</strong>{content}</div>'


def tip(content):
    return f'<div class="tip"><strong>Expert Tip:</strong>{content}</div>'


def module_html(mid, title, objectives, lesson_titles, lessons_body, workshop, notes, exercises, homework, quiz, outcomes):
    obj_li = "".join(f"<li>{esc(o)}</li>" for o in objectives)
    list_li = "".join(f"<li>{esc(l)}</li>" for l in lesson_titles)
    return f'''
<section class="module" id="module{mid}">
<h1>Module {mid}: {esc(title)}</h1>
<div class="objectives"><strong>Learning Objectives</strong><ul>{obj_li}</ul></div>
<h2>Lesson List</h2>
<ol>{list_li}</ol>
<h2>Detailed Lesson Content</h2>
{lessons_body}
{workshop}
<div class="notes"><strong>Instructor Notes</strong>{notes}</div>
<div class="exercise"><strong>Student Exercises</strong>{exercises}</div>
<div class="homework"><strong>Homework</strong>{homework}</div>
<div class="quiz"><strong>Quiz Questions</strong>{quiz}</div>
<div class="outcomes"><strong>Expected Outcomes</strong>{outcomes}</div>
</section>
'''


def _module_2():
    lessons = (
        lesson(1, "WordPress Architecture Explained", """
<p>WordPress is a PHP-based content management system (CMS) that stores content in a MySQL or MariaDB database and renders pages through a theme layer. Understanding this stack is essential before touching SEO plugins or automation.</p>

<h4>Core Components</h4>
<ul>
<li><strong>Core files</strong> — WordPress engine in <code>/wp-admin/</code>, <code>/wp-includes/</code></li>
<li><strong>Database</strong> — Posts, pages, users, options, taxonomy tables</li>
<li><strong>Theme</strong> — Controls HTML output, templates, and styling</li>
<li><strong>Plugins</strong> — Extend functionality without editing core</li>
<li><strong>Uploads</strong> — Media library stored in <code>/wp-content/uploads/</code></li>
</ul>
""" + diagram("""
WORDPRESS REQUEST FLOW
══════════════════════════════════════════════════════════════
  Browser requests: https://example.com/blog/seo-guide/
         │
         ▼
  ┌──────────────┐
  │ .htaccess /  │  → Pretty permalinks rewrite to index.php
  │ Web Server   │
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │ index.php    │  → Loads wp-load.php → wp-settings.php
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │ Query Parser │  → Resolves URL to post type + slug
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐     ┌─────────────┐
  │ Theme        │────▶│ Plugins     │ → Rank Math, WooCommerce
  │ (single.php) │     │ (hooks)     │
  └──────┬───────┘     └─────────────┘
         │
         ▼
  HTML response → Browser → Googlebot crawls same HTML
══════════════════════════════════════════════════════════════
""") + case_study("Agency Migration Audit", """
<p>A local dental clinic migrated from Wix to WordPress. Their developer copied pages but left default <code>?p=123</code> permalinks. Organic traffic dropped 62% in 30 days because every URL changed without redirects. After implementing 301 redirects, restoring pretty permalinks, and resubmitting the sitemap, traffic recovered to 95% of pre-migration levels within 8 weeks.</p>
<p><strong>Lesson:</strong> Architecture decisions (permalinks, redirects) directly affect SEO. Plan migrations as SEO projects, not just design projects.</p>
""") + """
<h4>Implementation Steps</h4>
<ol>
<li>Document current URL structure before any change</li>
<li>Map old URLs to new URLs in a spreadsheet</li>
<li>Install Redirection plugin before go-live</li>
<li>Verify <code>wp-config.php</code> has correct site URL constants</li>
<li>Test one page end-to-end: publish → view source → Search Console URL Inspection</li>
</ol>
""" + tip("<p>Draw the request flow on a whiteboard during Lesson 1. Students who understand hooks (<code>the_content</code>, <code>wp_head</code>) later grasp why SEO plugins inject meta tags without editing theme files.</p>") + mistake("<ul><li>Editing theme files for SEO meta tags instead of using a plugin</li><li>Installing plugins on production without staging tests</li><li>Ignoring database prefix and backup strategy</li></ul>"))
        + lesson(2, "Themes: Selection and SEO Impact", """
<p>Your theme determines HTML structure, heading hierarchy defaults, schema markup support, and page speed. A beautiful theme with bloated JavaScript can destroy Core Web Vitals.</p>

<h4>What to Evaluate in a Theme</h4>
<ul>
<li>Semantic HTML5 (header, nav, main, article, footer)</li>
<li>Single H1 per page template</li>
<li>Mobile responsiveness without layout shift</li>
<li>Compatibility with Rank Math or Yoast</li>
<li>Minimal render-blocking resources</li>
<li>Accessibility (WCAG) for better UX signals</li>
</ul>

<h4>WordPress Example</h4>
<p>GeneratePress + Rank Math is a common SEO stack for agencies. Block themes (Twenty Twenty-Four) suit full-site editing but require more training. Avoid themes bundled with page builders you do not need—they add 200–400 KB of CSS/JS per page.</p>
""" + diagram("""
THEME SEO CHECKLIST
────────────────────────────────────────
[ ] Valid HTML5 document outline
[ ] One H1 in single post template
[ ] Breadcrumbs supported or pluggable
[ ] Schema-ready (Article, Organization)
[ ] LCP image not lazy-loaded incorrectly
[ ] No H1 in site logo area on inner pages
[ ] Footer links crawlable (not JS-only)
────────────────────────────────────────
""") + """
<h4>AI Search Example</h4>
<p>Ask ChatGPT: "What WordPress theme do SEO agencies recommend in 2026?" Note cited sources—usually WPBeginner, ThemeIsle, and official theme directories. Themes with strong documentation and developer reputation get cited; nulled/pirated themes never appear.</p>
""" + case_study("Theme Switch Recovery", """
<p>An ecommerce blog switched from a multipurpose theme to a lightweight theme. CLS improved from 0.35 to 0.05, and organic traffic rose 18% over 90 days without new content—purely from Core Web Vitals gains and faster mobile rendering.</p>
""") + mistake("<ul><li>Choosing themes based on demo aesthetics alone</li><li>Using H1 for logo text site-wide</li><li>Blocking theme updates indefinitely (security risk)</li></ul>") + tip("<p>Run Google PageSpeed Insights on the theme demo URL before purchase. If demo scores below 70 mobile, expect work.</p>"))
        + lesson(3, "Plugins: Power, Risk, and SEO Stack", """
<p>Plugins extend WordPress but add HTTP requests, database queries, and security surface area. The average SEO-focused site needs 8–15 plugins—not 40.</p>

<h4>Essential SEO Plugin Stack</h4>
<table>
<tr><th>Plugin</th><th>Purpose</th></tr>
<tr><td>Rank Math or Yoast SEO</td><td>Meta tags, sitemap, schema, redirects</td></tr>
<tr><td>LiteSpeed Cache or WP Rocket</td><td>Caching, minification, lazy load</td></tr>
<tr><td>Redirection</td><td>301/302 management</td></tr>
<tr><td>Wordfence or Solid Security</td><td>Firewall, login protection</td></tr>
<tr><td>UpdraftPlus</td><td>Automated backups</td></tr>
</table>

<h4>Implementation Steps</h4>
<ol>
<li>Install SEO plugin and run setup wizard</li>
<li>Connect Google Search Console and Analytics</li>
<li>Enable XML sitemap; disable WordPress core sitemap if duplicate</li>
<li>Configure Organization schema with logo and social profiles</li>
<li>Audit plugin list quarterly—deactivate unused plugins</li>
</ol>
""" + diagram("""
PLUGIN LOAD ORDER (SIMPLIFIED)
────────────────────────────────────────
wp-config.php loads
    → mu-plugins (must-use)
    → active plugins alphabetically
    → theme functions.php
    → hook: init, wp_enqueue_scripts, wp_head
SEO meta appears in wp_head at priority 1–999
Cache plugins run at shutdown or via server rules
────────────────────────────────────────
""") + mistake("<ul><li>Installing two SEO plugins simultaneously (Yoast + Rank Math)</li><li>Leaving inactive plugins installed</li><li>Using outdated plugins with known CVEs</li></ul>") + tip("<p>Before adding a plugin, search '[plugin name] site:wordpress.org/support' for unresolved critical bugs.</p>"))
        + lesson(4, "Categories, Tags, and Taxonomy Strategy", """
<p>WordPress categories are hierarchical (parent/child); tags are flat. Both create archive pages that Google may index—often causing duplicate or thin content problems.</p>

<h4>Best Practice Structure</h4>
<ul>
<li><strong>Categories</strong> — 5–12 broad buckets (e.g., SEO, WordPress, Analytics)</li>
<li><strong>Tags</strong> — Use sparingly or disable indexing</li>
<li><strong>One primary category</strong> per post for clear site architecture</li>
</ul>

<h4>WordPress Example</h4>
<p>In Rank Math → Titles &amp; Meta → Categories: set to <code>noindex</code> if archive pages duplicate content. Alternatively, write unique 150-word category descriptions and index them as hub pages.</p>
""" + diagram("""
SITE ARCHITECTURE: BLOG TAXONOMY
────────────────────────────────────────
                    [Blog Home]
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
   [Category: SEO]  [Category: WP]   [Category: AI]
        │                │                │
   ┌────┴────┐      ┌────┴────┐      ┌────┴────┐
   Post A    Post B  Post C   Post D  Post E   Post F

Tags: use for admin only OR noindex tag archives
────────────────────────────────────────
""") + case_study("Tag Bloat Cleanup", """
<p>A tech blog had 2,400 tag archive pages indexed, many with 1–2 posts. Crawl budget was wasted and duplicate titles triggered soft 404 patterns. After noindexing tags and consolidating to 8 categories, indexed pages dropped 30% but organic traffic increased 22%—quality over quantity.</p>
""") + """
<h4>AI Search Example</h4>
<p>Perplexity query: "WordPress categories vs tags for SEO" — notice answers cite clear hierarchical explanations. Structure your own taxonomy docs the same way for potential AI citation.</p>
""" + mistake("<ul><li>Creating a new category for every post</li><li>Using tags identical to category names</li><li>Allowing /tag/ pages to index with thin content</li></ul>"))
        + lesson(5, "URL Structures and Permalinks", """
<p>Permalinks are the foundation of URL-based SEO. WordPress supports Plain, Day and name, Month and name, Numeric, Post name, and Custom structures.</p>

<h4>Recommended Settings</h4>
<ul>
<li><strong>Blog/content sites:</strong> Post name — <code>/blog-post-title/</code></li>
<li><strong>Ecommerce (WooCommerce):</strong> Product base <code>/product/</code>, categories in breadcrumbs not necessarily URL</li>
<li><strong>Large sites:</strong> Category in URL only if categories are stable — <code>/%category%/%postname%/</code></li>
</ul>

<h4>Implementation Steps</h4>
<ol>
<li>Settings → Permalinks → select Post name before publishing content</li>
<li>Never change permalinks without 301 redirect map</li>
<li>Keep URLs lowercase, hyphen-separated, under 75 characters when possible</li>
<li>Exclude stop words only if URLs become unwieldy</li>
<li>Use Redirection plugin for bulk 301s after slug changes</li>
</ol>
""" + diagram("""
URL STRUCTURE COMPARISON
────────────────────────────────────────
BAD:  /?p=847
BAD:  /2026/06/09/how-to-do-seo-on-wordpress-fast-guide-tips/
GOOD: /wordpress-seo-guide/
GOOD: /seo/on-page-optimization/

Trailing slashes: match server config consistently
HTTPS: force via plugin or .htaccess
────────────────────────────────────────
""") + tip("<p>When teaching WooCommerce, show how product URLs interact with variable products and attribute permalinks—common source of duplicate URLs.</p>") + mistake("<ul><li>Changing slug after backlinks exist without redirects</li><li>Uppercase URLs mixed with lowercase</li><li>Date-based URLs on evergreen content</li></ul>"))
        + lesson(6, "Hosting, Performance, and Environment", """
<p>Hosting affects crawl rate, uptime, TTFB, and security—all ranking factors. Shared hosting may work for small blogs; serious SEO projects need managed WordPress or VPS.</p>

<h4>Hosting Checklist for SEO</h4>
<ul>
<li>PHP 8.2+ with OPcache enabled</li>
<li>HTTP/2 or HTTP/3 support</li>
<li>Free SSL (Let's Encrypt) with auto-renewal</li>
<li>Server-level caching (LiteSpeed, NGINX FastCGI)</li>
<li>Staging environment included</li>
<li>Daily backups with off-site storage</li>
</ul>

<h4>WordPress Example</h4>
<p>Move from $5/month shared hosting to managed WordPress (Kinsta, WP Engine, Cloudways). TTFB dropped from 890ms to 180ms; crawl stats in Search Console showed 40% more pages crawled per day within 3 weeks.</p>
""" + diagram("""
HOSTING STACK FOR SEO
══════════════════════════════════════════════════════════════
  CDN (Cloudflare) ──▶ Edge cache static assets
         │
         ▼
  Web Server (LiteSpeed/NGINX) ──▶ Page cache
         │
         ▼
  PHP + WordPress ──▶ Object cache (Redis optional)
         │
         ▼
  MySQL ──▶ Optimized tables, limited autoloaded options
══════════════════════════════════════════════════════════════
""") + case_study("Downtime During Launch", """
<p>A retailer launched a sale during Black Friday on overloaded shared hosting. 6 hours of 503 errors caused Google to temporarily reduce crawl rate; product pages deindexed for 11 days. Cost: est. $47,000 revenue. Lesson: load-test before peak traffic.</p>
""") + mistake("<ul><li>Skipping staging for plugin updates</li><li>No monitoring/uptime alerts</li><li>Autoloaded options bloat from abandoned plugins</li></ul>"))
        + lesson(7, "WordPress Security for SEO", """
<p>Hacked sites get deindexed, flagged in browsers, and lose trust. Security is an SEO requirement, not an IT afterthought.</p>

<h4>Core Security Measures</h4>
<ol>
<li>Strong admin passwords + two-factor authentication</li>
<li>Limit login attempts; change default <code>/wp-admin/</code> URL optionally</li>
<li>Keep core, themes, and plugins updated within 7 days of security releases</li>
<li>File integrity monitoring via Wordfence</li>
<li>Disable file editing: <code>define('DISALLOW_FILE_EDIT', true);</code></li>
<li>Least-privilege user roles for contributors</li>
</ol>

<h4>WordPress Example</h4>
<p>After a pharma client site was injected with Japanese keyword spam, Search Console showed "Security Issues" and organic traffic fell to zero. Cleanup + reconsideration request took 19 days. Prevention would have cost 2 hours of hardening.</p>
""" + diagram("""
ATTACK SURFACE MAP
────────────────────────────────────────
/wp-login.php      → Brute force (use 2FA + limit)
/xmlrpc.php        → Disable if unused
/wp-json/          → Restrict sensitive endpoints
uploads/*.php      → Block PHP execution in uploads
nulled plugins     → Backdoors (never use)
────────────────────────────────────────
""") + """
<h4>AI Search Example</h4>
<p>Query Gemini: "signs WordPress site is hacked SEO" — use this list in client audits; AI tools aggregate the same signals Google Safe Browsing uses.</p>
""" + tip("<p>Run weekly Search Console Security Issues check as part of SEO reporting—not just rankings.</p>") + mistake("<ul><li>Admin username 'admin'</li><li>Publicly exposing phpMyAdmin</li><li>SEO spam in footer injected via compromised plugin</li></ul>"))
        + lesson(8, "Building Your WordPress SEO Foundation", """
<p>Module 2 culminates in a repeatable launch checklist that connects architecture to measurable SEO readiness.</p>

<h4>Pre-Launch Checklist</h4>
<ol>
<li>Post name permalinks configured</li>
<li>SEO plugin installed with sitemap submitted</li>
<li>SSL active; HTTP → HTTPS redirects</li>
<li>Theme passes mobile PageSpeed 80+</li>
<li>Categories planned; tags policy defined</li>
<li>Backup and security plugins active</li>
<li>Staging mirrors production plugin set</li>
<li>robots.txt allows crawling; admin disallowed</li>
<li>Privacy policy and cookie consent if EU traffic</li>
<li>Google Search Console property verified</li>
</ol>

<h4>Real-World Workflow</h4>
<p>Agencies use a "Site Birth Certificate" document: hosting specs, plugin list, taxonomy map, URL conventions, and baseline Core Web Vitals. Every future SEO change references this doc—critical when staff turnover occurs.</p>
""" + diagram("""
WORDPRESS SEO FOUNDATION MATURITY MODEL
────────────────────────────────────────
Level 1: Installed WordPress + default theme
Level 2: SEO plugin + permalinks + SSL
Level 3: Optimized theme, taxonomy, caching
Level 4: Staging, monitoring, security hardened
Level 5: Automated audits via n8n (Module 13)
────────────────────────────────────────
""") + case_study("Greenfield Launch", """
<p>A SaaS startup launched on WordPress with GeneratePress, Rank Math, and Cloudflare from day one. First indexed page within 48 hours; 50 pages indexed by week 6. Competitors on Wix took 4 months to reach the same indexation count due to limited technical control.</p>
""") + mistake("<ul><li>Launching without Search Console verification</li><li>Deferring security until after launch</li><li>No documented baseline before marketing spend</li></ul>") + tip("<p>Assign students the workshop before this lesson—they will appreciate each checklist item viscerally.</p>"))
    )

    workshop = """
<div class="workshop">
<strong>Workshop: Create a WordPress Website from Scratch</strong>
<h4>Duration:</h4> 3 hours (can split across two sessions)
<h4>Materials:</h4> Domain name, hosting account, laptop, browser, notepad for URL map
<h4>Instructions:</h4>
<ol>
<li>Register domain and provision managed WordPress hosting with SSL</li>
<li>Install WordPress; complete site title, tagline, and timezone settings</li>
<li>Configure Post name permalinks; verify HTTPS works</li>
<li>Install and configure Rank Math or Yoast: connect Search Console, enable sitemap</li>
<li>Install lightweight theme (GeneratePress or block theme); delete unused default themes</li>
<li>Create 5 categories aligned to business topics; write 100-word description for each</li>
<li>Publish 3 posts (800+ words each) with proper H1, featured image, internal links</li>
<li>Install caching plugin; run PageSpeed Insights; fix one performance issue</li>
<li>Install Wordfence; enable 2FA on admin account</li>
<li>Submit sitemap in Search Console; inspect one URL for index eligibility</li>
</ol>
<h4>Deliverable:</h4> Live WordPress site URL + Site Birth Certificate PDF (hosting, plugins, taxonomy, baseline PageSpeed score)
</div>
"""

    notes = """
<ul>
<li>Pair students with weaker technical skills alongside confident developers</li>
<li>Common failure: students publish before setting permalinks—fix immediately</li>
<li>Budget 20 minutes for DNS propagation questions</li>
<li>Demonstrate staging if host provides it; otherwise use Local WP for practice</li>
<li>Emphasize deleting Hello Dolly and unused themes (security hygiene)</li>
</ul>
"""

    exercises = """<ol>
<li>Label the WordPress database tables that store posts and taxonomy relationships.</li>
<li>Compare two themes using the theme SEO checklist from Lesson 2.</li>
<li>Design a category hierarchy for a fictional bakery with 20 planned blog posts.</li>
<li>Write three URL slug options for a post titled "10 WordPress Security Tips for Small Business" and defend your choice.</li>
</ol>"""

    homework = """<p>Document your workshop site in a 750-word report covering: architecture choices, plugin rationale, taxonomy map, and one PageSpeed improvement you made. Include a screenshot of Search Console URL Inspection for your best post.</p>"""

    quiz = """<ol>
<li>What database does WordPress typically use?</li>
<li>Name the four main components of WordPress architecture.</li>
<li>Why should you avoid two SEO plugins at once?</li>
<li>What is the difference between categories and tags?</li>
<li>Which permalink structure is recommended for most blogs?</li>
<li>Name three hosting factors that affect SEO.</li>
<li>What file should block /wp-admin/ from crawlers but allow AJAX?</li>
<li>Why are tag archive pages often set to noindex?</li>
<li>What happens if you change permalinks without redirects?</li>
<li>Name two security measures that protect SEO visibility.</li>
</ol>
<p><strong>Answer Key:</strong> 1) MySQL/MariaDB 2) Core, database, theme, plugins (uploads acceptable) 3) Duplicate/conflicting meta tags and sitemaps 4) Categories hierarchical; tags flat 5) Post name 6) TTFB, uptime, SSL, crawl rate (any three) 7) robots.txt 8) Thin/duplicate content 9) 404 errors, lost rankings/backlinks 10) 2FA, updates, firewall (any two)</p>"""

    outcomes = """<ul>
<li>Explain WordPress architecture and request flow</li>
<li>Select SEO-friendly themes and plugin stacks</li>
<li>Design taxonomy and URL structures that prevent duplicate content</li>
<li>Evaluate hosting for performance and crawl efficiency</li>
<li>Harden WordPress security to protect search visibility</li>
<li>Launch a production-ready WordPress site from scratch</li>
</ul>"""

    return module_html(
        2, "WordPress Foundations",
        [
            "Explain WordPress architecture and how pages are rendered",
            "Evaluate themes and plugins for SEO impact",
            "Design category, tag, and URL structures",
            "Configure hosting and performance for crawlability",
            "Implement WordPress security best practices",
            "Complete a full WordPress site launch",
        ],
        [
            "WordPress Architecture Explained",
            "Themes: Selection and SEO Impact",
            "Plugins: Power, Risk, and SEO Stack",
            "Categories, Tags, and Taxonomy Strategy",
            "URL Structures and Permalinks",
            "Hosting, Performance, and Environment",
            "WordPress Security for SEO",
            "Building Your WordPress SEO Foundation",
        ],
        lessons, workshop, notes, exercises, homework, quiz, outcomes,
    )


def _module_3():
    lessons = (
        lesson(1, "Understanding Search Intent", """
<p>Search intent is the <em>why</em> behind a query. Google classifies intent into informational, navigational, commercial investigation, and transactional. Matching intent is the first gate for ranking.</p>

<h4>Intent Types with Examples</h4>
<table>
<tr><th>Intent</th><th>Example Query</th><th>Best Content Format</th></tr>
<tr><td>Informational</td><td>what is canonical tag</td><td>Guide, definition, video</td></tr>
<tr><td>Navigational</td><td>rank math login</td><td>Brand homepage, docs</td></tr>
<tr><td>Commercial</td><td>best seo plugin wordpress</td><td>Comparison, review roundup</td></tr>
<tr><td>Transactional</td><td>buy rank math pro</td><td>Product page, pricing</td></tr>
</table>
""" + diagram("""
SEARCH INTENT DECISION FLOW
══════════════════════════════════════════════════════════════
  Query: "wordpress seo plugin"
         │
         ▼
  Contains "best", "vs", "review"? ──YES──▶ Commercial
         │ NO
         ▼
  Contains "buy", "price", "coupon"? ──YES──▶ Transactional
         │ NO
         ▼
  Brand name only? ──YES──▶ Navigational
         │ NO
         ▼
  Default ──▶ Informational (how-to, what-is)
══════════════════════════════════════════════════════════════
""") + case_study("Intent Mismatch", """
<p>A law firm published a 3,000-word blog post targeting "divorce lawyer Chicago" with purely educational content about divorce law. It never ranked. Competitors with service pages (transactional/local intent) dominated. Rewriting as a location service page with FAQs and schema moved them to local pack visibility within 6 weeks.</p>
""") + """
<h4>WordPress Example</h4>
<p>Map each planned URL in Rank Math's content analysis to one intent type. Informational posts go in /blog/; commercial comparisons in /reviews/; transactional pages as standalone pages with clear CTAs.</p>
""" + tip("<p>Teach students to SERP-check every target keyword—Google's current results reveal inferred intent better than any tool.</p>") + mistake("<ul><li>Targeting keywords without checking SERP format</li><li>Using blog posts for purely transactional queries</li><li>Mixing multiple intents on one page</li></ul>"))
        + lesson(2, "Keyword Research Foundations", """
<p>Keyword research discovers what your audience searches, how often, and how hard it is to rank. Start with seed topics from business goals—not random volume hunting.</p>

<h4>Research Workflow</h4>
<ol>
<li>List 5–10 seed topics from products, services, and customer questions</li>
<li>Expand with Google Autocomplete, People Also Ask, Related Searches</li>
<li>Pull metrics from Ahrefs, Semrush, or free alternatives (Ubersuggest, GSC)</li>
<li>Filter by relevance first, then volume, then difficulty</li>
<li>Map keywords to existing or planned URLs</li>
</ol>

<h4>Metrics Explained</h4>
<ul>
<li><strong>Search volume</strong> — Monthly average searches (directional, not precise)</li>
<li><strong>Keyword difficulty</strong> — Competitive estimate (varies by tool)</li>
<li><strong>CPC</strong> — Commercial value indicator</li>
<li><strong>SERP features</strong> — Snippets, PAA, local pack presence</li>
</ul>
""" + diagram("""
KEYWORD RESEARCH PIPELINE
────────────────────────────────────────
Business Goals → Seed Topics → Expand
      → Filter (relevance/volume/KD)
      → Intent Label → URL Assignment
      → Content Brief → Publish → GSC Validate
────────────────────────────────────────
""") + """
<h4>AI Search Example</h4>
<p>Ask Perplexity: "What questions do small businesses ask about local SEO?" Use the cited questions as PAA-style subheadings in your content briefs.</p>
""" + case_study("Zero-Volume Win", """
<p>A B2B SaaS targeted "woocommerce subscription churn analytics"—zero volume in Ahrefs but high product fit. The post ranked #2 within 8 weeks and drove 14 qualified demos in Q1 because intent was precise.</p>
""") + mistake("<ul><li>Chasing high volume irrelevant keywords</li><li>Ignoring long-tail clusters</li><li>Trusting volume data as exact</li></ul>"))
        + lesson(3, "User Journeys and the Marketing Funnel", """
<p>SEO does not exist in isolation. Users move from awareness → consideration → decision. Map keywords to funnel stages so content nurtures—not just attracts.</p>

<h4>Funnel Mapping</h4>
<ul>
<li><strong>Top (Awareness):</strong> "what is technical seo" — educational blogs</li>
<li><strong>Middle (Consideration):</strong> "yoast vs rank math" — comparisons</li>
<li><strong>Bottom (Decision):</strong> "hire seo agency pricing" — service pages, case studies</li>
<li><strong>Retention:</strong> "how to fix crawl errors" — support docs, tutorials</li>
</ul>
""" + diagram("""
USER JOURNEY: LOCAL GYM EXAMPLE
══════════════════════════════════════════════════════════════
Awareness     "how to lose weight after 40"
     │              ↓ organic blog visit
Consideration "best gym near me reviews"
     │              ↓ comparison / GBP
Decision      "crossfit downtown austin membership"
     │              ↓ landing page + booking
Retention     "crossfit recovery exercises"
                    ↓ email + member portal
══════════════════════════════════════════════════════════════
""") + """
<h4>Implementation Steps</h4>
<ol>
<li>Interview sales/support for top 20 customer questions</li>
<li>Assign funnel stage to each question</li>
<li>Audit existing WordPress content for funnel gaps</li>
<li>Prioritize bottom-funnel gaps if revenue is urgent</li>
<li>Add internal links connecting funnel stages</li>
</ol>
""" + tip("<p>Visualize journeys on Miro or FigJam—students remember stories better than spreadsheets alone.</p>") + mistake("<ul><li>Publishing only top-funnel content for a sales-driven site</li><li>No internal links between funnel stages</li><li>Ignoring post-conversion search queries</li></ul>"))
        + lesson(4, "Content Mapping to Keywords", """
<p>Content mapping assigns one primary keyword (and supporting secondaries) to each URL. Prevents keyword cannibalization and clarifies site architecture.</p>

<h4>Content Map Template</h4>
<table>
<tr><th>URL</th><th>Primary KW</th><th>Intent</th><th>Funnel</th><th>Status</th></tr>
<tr><td>/wordpress-seo/</td><td>wordpress seo</td><td>Informational</td><td>TOFU</td><td>Published</td></tr>
<tr><td>/rank-math-review/</td><td>rank math review</td><td>Commercial</td><td>MOFU</td><td>Draft</td></tr>
</table>

<h4>WordPress Example</h4>
<p>Use a custom field or spreadsheet linked to post ID. Rank Math focus keyword should match map exactly—one focus keyword per post.</p>
""" + diagram("""
CONTENT MAP ARCHITECTURE
────────────────────────────────────────
[Pillar: WordPress SEO Guide]
    ├── /wordpress-seo-basics/
    ├── /wordpress-seo-plugins/
    ├── /wordpress-seo-speed/
    └── /wordpress-seo-schema/

Each child targets ONE primary keyword
Parent targets broad head term
────────────────────────────────────────
""") + case_study("Cannibalization Fix", """
<p>Two posts targeted "schema markup wordpress" with similar content. Both ranked page 3. Merged into one definitive guide with 301 redirect from weaker post. Combined URL hit position 4 within 5 weeks.</p>
""") + mistake("<ul><li>Multiple posts targeting identical primary keywords</li><li>No content map updated after site grows</li><li>Focus keyword different from title intent</li></ul>"))
        + lesson(5, "Keyword Clustering", """
<p>Keyword clustering groups semantically related terms that share the same intent and can be served by one URL—or a hub with spokes.</p>

<h4>Clustering Methods</h4>
<ol>
<li><strong>SERP similarity:</strong> If top 10 URLs overlap 60%+, same cluster</li>
<li><strong>Semantic grouping:</strong> Tools like Keyword Insights, Ahrefs clustering</li>
<li><strong>Manual:</strong> Spreadsheet + judgment for niche sites</li>
</ol>

<h4>Example Cluster</h4>
<p>Primary: "wordpress image seo" — Includes: "wordpress alt text," "compress images wordpress," "lazy load wordpress seo" — One comprehensive guide with H2 sections.</p>
""" + diagram("""
KEYWORD CLUSTER: IMAGE SEO
────────────────────────────────────────
        [wordpress image seo]  ← Primary (pillar section)
              │
    ┌─────────┼─────────┐
    ▼         ▼         ▼
 alt text   compress   lazy load
 (H2)       (H2)       (H2)

Single URL unless SERPs differ significantly
────────────────────────────────────────
""") + """
<h4>AI Search Example</h4>
<p>ChatGPT: "Group these 30 keywords into clusters for a dental clinic website" — validate AI clusters against live SERPs; AI sometimes over-splits or under-splits.</p>
""" + tip("<p>Cluster before writing—retrofit clustering wastes content budget.</p>") + mistake("<ul><li>One keyword = one thin page ( doorway risk)</li><li>Ignoring SERP validation of clusters</li><li>Clusters too broad (unfocused content)</li></ul>"))
        + lesson(6, "SERP Analysis", """
<p>SERP analysis examines who ranks, what format Google prefers, and which features appear. It validates every keyword target before content investment.</p>

<h4>SERP Analysis Checklist</h4>
<ol>
<li>Search keyword in incognito; screenshot top 10</li>
<li>Note content types: guide, listicle, product, video</li>
<li>Identify SERP features: snippet, PAA, AI Overview, local pack</li>
<li>Estimate content length and depth of top 3</li>
<li>Check Domain Rating spread—can a smaller site break in?</li>
<li>Document required schema and media types</li>
</ol>
""" + diagram("""
SERP FEATURE MAP (EXAMPLE QUERY)
══════════════════════════════════════════════════════════════
┌─────────────────────────────────────┐
│ AI Overview (synthesized answer)    │
├─────────────────────────────────────┤
│ Featured Snippet (paragraph)        │
├─────────────────────────────────────┤
│ Organic #1-3 (2,500+ word guides)   │
├─────────────────────────────────────┤
│ People Also Ask (4 questions)       │
├─────────────────────────────────────┤
│ Video carousel                      │
├─────────────────────────────────────┤
│ Organic #4-10                       │
└─────────────────────────────────────┘
══════════════════════════════════════════════════════════════
""") + case_study("SERP Format Pivot", """
<p>Team planned a short FAQ for "core web vitals checklist." SERP showed only interactive tools and 4,000-word guides. Pivoted to downloadable checklist + embedded tool. Ranked #6 in 10 weeks.</p>
""") + """
<h4>WordPress Example</h4>
<p>If SERP shows video carousel, embed YouTube with schema. If PAA dominates, structure H2s as exact questions with 40–60 word answers beneath.</p>
""" + mistake("<ul><li>Skipping SERP analysis for 'obvious' keywords</li><li>Assuming 2020 SERP format still applies</li><li>Ignoring AI Overview pushing organic down</li></ul>"))
        + lesson(7, "Building a Keyword Strategy", """
<p>A keyword strategy prioritizes clusters by business impact, difficulty, and resource fit. Document it so content teams execute consistently.</p>

<h4>Prioritization Matrix</h4>
<table>
<tr><th>Priority</th><th>Criteria</th><th>Action</th></tr>
<tr><td>P1</td><td>High relevance, winnable, bottom-funnel</td><td>Publish this month</td></tr>
<tr><td>P2</td><td>High relevance, harder, TOFU</td><td>Pillar content Q2</td></tr>
<tr><td>P3</td><td>Medium relevance, easy long-tail</td><td>Batch programmatic or AI-assisted</td></tr>
<tr><td>Deprioritize</td><td>High KD, low conversion</td><td>Monitor only</td></tr>
</table>
""" + diagram("""
90-DAY KEYWORD STRATEGY TIMELINE
────────────────────────────────────────
Week 1-2:  Research + clustering + SERP analysis
Week 3-4:  Content map + briefs for P1 (5 URLs)
Week 5-8:  Publish P1 + internal linking
Week 9-10: GSC review + refresh underperformers
Week 11-12: Expand P2 clusters
────────────────────────────────────────
""") + tip("<p>Align keyword strategy with sales calendar—retail clients need seasonal clusters 8 weeks early.</p>") + mistake("<ul><li>No prioritization—random publishing</li><li>Strategy without KPIs (traffic, leads, revenue)</li><li>Never revisiting strategy quarterly</li></ul>"))
        + lesson(8, "Measuring Keyword Performance", """
<p>Publishing without measurement wastes budget. Track rankings, clicks, impressions, and conversions per URL and cluster.</p>

<h4>Metrics Dashboard</h4>
<ul>
<li><strong>GSC:</strong> Impressions, CTR, average position by query and page</li>
<li><strong>GA4:</strong> Organic sessions, conversions, landing pages</li>
<li><strong>Rank tracker:</strong> Daily position for priority keywords</li>
<li><strong>Revenue attribution:</strong> WooCommerce or CRM integration</li>
</ul>

<h4>Implementation Steps</h4>
<ol>
<li>Baseline all P1 keywords before publish</li>
<li>Tag posts in WordPress with cluster name (custom taxonomy)</li>
<li>Review GSC Performance report monthly by page</li>
<li>Refresh content when position drops 5+ places for 30 days</li>
<li>Report wins and losses with intent/cluster context</li>
</ol>
""" + case_study("CTR Optimization Loop", """
<p>Page ranked #3 for "woocommerce seo" but CTR was 1.2%. Rewrote title tag with year and benefit; CTR rose to 4.8%, adding 340 clicks/month without position change.</p>
""") + """
<h4>AI Search Example</h4>
<p>Track whether branded queries in GSC rise after publishing entity-rich content—early signal for AI citation potential.</p>
""" + diagram("""
MEASUREMENT FEEDBACK LOOP
────────────────────────────────────────
Publish → Index → Rank → Click → Convert
   ↑                              │
   └──────── Refresh / Expand ────┘
────────────────────────────────────────
""") + mistake("<ul><li>Tracking vanity rankings only</li><li>Ignoring impression growth as success signal</li><li>No cluster-level reporting</li></ul>"))
    )

    workshop = """
<div class="workshop">
<strong>Workshop: Build a Keyword Map for a Real Business</strong>
<h4>Duration:</h4> 2 hours
<h4>Materials:</h4> Laptop, Ahrefs/Semrush trial or GSC access, spreadsheet template, client or fictional business brief
<h4>Instructions:</h4>
<ol>
<li>Select a real local business or student's employer (with permission)</li>
<li>Document 3 products/services and 5 customer personas</li>
<li>Generate 100+ keyword ideas from seeds, Autocomplete, and PAA</li>
<li>Label intent and funnel stage for each keyword</li>
<li>Cluster into 8–12 groups using SERP similarity checks</li>
<li>Assign one primary keyword per planned URL (minimum 15 URLs)</li>
<li>Prioritize top 5 as P1 with rationale (relevance, difficulty, revenue)</li>
<li>Present map in 5-minute pitch: "What we will publish first and why"</li>
</ol>
<h4>Deliverable:</h4> Keyword map spreadsheet (URL, primary KW, cluster, intent, funnel, priority, SERP notes) + one-page strategy summary
</div>
"""

    notes = """
<ul>
<li>Provide spreadsheet template with data validation for intent/funnel columns</li>
<li>Students often over-cluster—demand SERP proof for splits</li>
<li>For students without tool access, GSC + manual SERP is sufficient</li>
<li>Real business context increases engagement vs fictional examples</li>
<li>Time-box SERP analysis to 3 minutes per cluster lead keyword</li>
</ul>
"""

    exercises = """<ol>
<li>Classify 10 provided queries by intent with SERP justification.</li>
<li>Build a mini content map with 8 URLs for a fictional coffee shop.</li>
<li>Perform SERP analysis for one commercial keyword and recommend content format.</li>
<li>Identify cannibalization risk in a sample 20-URL site export.</li>
</ol>"""

    homework = """<p>Expand your workshop keyword map to 25 URLs. Write 300-word strategy memo explaining P1 choices, funnel balance, and one cluster you deliberately deprioritized—with reasoning.</p>"""

    quiz = """<ol>
<li>Name the four classic search intent types.</li>
<li>What is keyword cannibalization?</li>
<li>What SERP feature shows expandable questions?</li>
<li>How do you validate a keyword cluster?</li>
<li>What metric in GSC shows visibility without clicks?</li>
<li>What funnel stage matches "best CRM for startups"?</li>
<li>Why might zero-volume keywords still be valuable?</li>
<li>What is a content map?</li>
<li>Name two keyword research tools.</li>
<li>What should you do when two pages target the same primary keyword?</li>
</ol>
<p><strong>Answer Key:</strong> 1) Informational, navigational, commercial, transactional 2) Multiple URLs competing for same keyword, splitting signals 3) People Also Ask 4) SERP similarity/overlap in top results 5) Impressions 6) Consideration/MOFU 7) High intent fit, niche B2B, emerging topics 8) Document mapping URLs to target keywords 9) Ahrefs, Semrush, GSC (any two) 10) Merge, redirect, or differentiate intent</p>"""

    outcomes = """<ul>
<li>Classify search intent accurately using SERP evidence</li>
<li>Conduct keyword research aligned to business goals</li>
<li>Map user journeys and funnel stages to content</li>
<li>Build keyword clusters and content maps</li>
<li>Perform SERP analysis to choose content formats</li>
<li>Deliver a prioritized keyword strategy for a real business</li>
</ul>"""

    return module_html(
        3, "SEO Fundamentals",
        [
            "Classify search intent with SERP validation",
            "Conduct keyword research using multiple sources",
            "Map user journeys across the marketing funnel",
            "Build content maps and keyword clusters",
            "Analyze SERPs to determine content strategy",
            "Create a measurable keyword strategy",
        ],
        [
            "Understanding Search Intent",
            "Keyword Research Foundations",
            "User Journeys and the Marketing Funnel",
            "Content Mapping to Keywords",
            "Keyword Clustering",
            "SERP Analysis",
            "Building a Keyword Strategy",
            "Measuring Keyword Performance",
        ],
        lessons, workshop, notes, exercises, homework, quiz, outcomes,
    )


def _module_4():
    lessons = (
        lesson(1, "Title Tags: Crafting Click-Worthy Headlines", """
<p>The title tag is the strongest on-page relevance signal and primary SERP headline. It should include the primary keyword near the front, stay under 60 characters when possible, and compel clicks without clickbait.</p>

<h4>Title Tag Formula</h4>
<ul>
<li><strong>Primary keyword</strong> + benefit or differentiator + brand (optional)</li>
<li>Example: <code>WordPress SEO Guide: 2026 Best Practices | Brand</code></li>
<li>Avoid duplicate titles across site—each URL unique</li>
</ul>
""" + diagram("""
TITLE TAG ANATOMY
══════════════════════════════════════════════════════════════
[Primary Keyword] : [Benefit/Hook] | [Brand]
     ↑                    ↑              ↑
  Relevance           CTR driver    Trust (optional)

SERP display: ~600px desktop, ~78 char mobile (varies)
══════════════════════════════════════════════════════════════
""") + case_study("Title Tag CTR Test", """
<p>Ecommerce category page title changed from "Running Shoes" to "Running Shoes for Men &amp; Women | Free Returns." CTR increased from 2.1% to 5.4% at position 5. Revenue from organic rose 28% for that category in 60 days.</p>
""") + """
<h4>WordPress Example</h4>
<p>Rank Math → Edit Post → Snippet Editor. Use variables <code>%title%</code>, <code>%sep%</code>, <code>%sitename%</code> in global templates but override for priority pages.</p>

<h4>Implementation Steps</h4>
<ol>
<li>Audit top 20 pages in GSC for low CTR at positions 1–10</li>
<li>Rewrite titles with keyword front-loaded + unique hook</li>
<li>A/B test via before/after GSC comparison (14-day windows)</li>
<li>Ensure one title tag per URL in source HTML</li>
</ol>
""" + tip("<p>Export GSC queries where position &lt; 8 and CTR &lt; 2%—fastest title optimization list.</p>") + mistake("<ul><li>Keyword stuffing titles</li><li>Identical titles on paginated archives</li><li>Missing title tag (WordPress defaults to site name only)</li></ul>"))
        + lesson(2, "Meta Descriptions That Drive Clicks", """
<p>Meta descriptions are not a direct ranking factor but influence CTR, which correlates with performance. Google may rewrite them—write descriptions that match page content precisely.</p>

<h4>Best Practices</h4>
<ul>
<li>150–160 characters; include primary keyword naturally</li>
<li>Active voice, clear value proposition, optional CTA</li>
<li>Unique per page; summarize what user will learn or get</li>
<li>Match search intent (informational vs commercial tone)</li>
</ul>
""" + diagram("""
META DESCRIPTION TEMPLATE
────────────────────────────────────────
Learn [topic] with [specific benefit].
[Proof point or number]. [CTA: Read guide / Compare / Get started]

Example:
Learn WordPress SEO with our 2026 step-by-step guide.
Covers plugins, speed, and schema. Start optimizing today.
────────────────────────────────────────
""") + """
<h4>WordPress Example</h4>
<p>Rank Math snippet preview shows desktop/mobile truncation. For WooCommerce products, include price range or shipping hook if relevant to query intent.</p>

<h4>AI Search Example</h4>
<p>AI Overviews often pull from meta-like summaries in first paragraph—align meta description with opening paragraph for consistency across SERP and AI.</p>
""" + case_study("Rewrite Recovery", """
<p>Blog meta descriptions were auto-generated duplicates. Custom descriptions on 45 posts increased average CTR from 1.8% to 3.2% over 30 days.</p>
""") + mistake("<ul><li>Quotation marks that truncate oddly</li><li>Descriptions unrelated to content (Google rewrites)</li><li>Using same description site-wide</li></ul>"))
        + lesson(3, "Heading Hierarchy H1–H6", """
<p>Headings structure content for users and crawlers. One H1 per page containing primary keyword; H2s for main sections; H3s for subsections. Never skip levels for styling—use CSS instead.</p>

<h4>Proper Structure Example</h4>
<pre class="diagram">H1: Complete WordPress SEO Guide (2026)
  H2: Why WordPress SEO Matters
  H2: On-Page Optimization
    H3: Title Tags and Meta
    H3: Internal Linking
  H2: Technical Setup
    H3: Sitemaps and robots.txt</pre>

<h4>WordPress Example</h4>
<p>Block editor: one H1 block in post title (theme renders as H1). Do not add second H1 in content body—use H2 for first section. Classic editor users often bold text instead of headings—fix in content audit.</p>
""" + case_study("Heading Fix Impact", """
<p>800-word posts used bold paragraphs instead of H2s. Restructuring with question-based H2s aligned to PAA captured 3 featured snippets within 6 weeks.</p>
""") + """
<h4>Implementation Steps</h4>
<ol>
<li>Crawl site with Screaming Frog; export H1/H2 report</li>
<li>Flag missing H1, multiple H1s, skipped levels</li>
<li>Map H2s to keyword cluster subtopics from Module 3</li>
<li>Update templates so category pages have unique H1</li>
</ol>
""" + tip("<p>Teach accessibility angle: screen readers navigate by headings—good SEO equals good a11y.</p>") + mistake("<ul><li>Multiple H1 tags for design</li><li>H1 hidden in widget areas on all pages</li><li>Keyword-stuffed headings that read unnaturally</li></ul>"))
        + lesson(4, "Internal Linking Strategy", """
<p>Internal links distribute PageRank, establish hierarchy, and help crawlers discover content. Every important page should be reachable within 3 clicks from homepage.</p>

<h4>Internal Linking Rules</h4>
<ul>
<li>Link from high-authority pages to priority targets</li>
<li>Use descriptive anchor text (not "click here")</li>
<li>Link contextually within body copy, not only nav/footer</li>
<li>Audit orphan pages quarterly</li>
<li>Build hub pages linking to cluster spokes</li>
</ul>
""" + diagram("""
INTERNAL LINK FLOW: TOPIC HUB
══════════════════════════════════════════════════════════════
              [Homepage]
                   │
                   ▼
         [Pillar: WordPress SEO]
          /      |       \\
         ▼       ▼        ▼
    [Plugins] [Speed]  [Schema]
         │       │        │
         └───────┴────────┘
              cross-links
══════════════════════════════════════════════════════════════
""") + """
<h4>WordPress Example</h4>
<p>Rank Math link suggestions while editing. For manual control, maintain "linking spreadsheet" mapping source posts to targets. Use Related Posts plugin sparingly—ensure links are editorially chosen.</p>
""" + case_study("Orphan Page Recovery", """
<p>47 product guides had zero internal links. Added contextual links from category pages and blog posts. Indexed count rose from 31 to 44; organic sessions +67% in 90 days.</p>
""") + mistake("<ul><li>Over-optimized exact-match anchor everywhere</li><li>Footer spam with 100 keyword links</li><li>Ignoring pagination and breadcrumb links</li></ul>") + tip("<p>Visualize link graph in GSC Links report—students understand authority flow instantly.</p>"))
        + lesson(5, "Image SEO and Alt Text", """
<p>Images affect page speed, accessibility, image search, and AI multimodal understanding. Optimize file size, dimensions, filenames, alt text, and lazy loading.</p>

<h4>Image Optimization Checklist</h4>
<ol>
<li>Resize before upload (max width 1920px for heroes, 800px inline)</li>
<li>Compress with ShortPixel or Imagify</li>
<li>Use WebP/AVIF via plugin or CDN</li>
<li>Descriptive filenames: <code>wordpress-seo-checklist.webp</code></li>
<li>Alt text: describe image + context, not keyword spam</li>
<li>Lazy load below-fold; never lazy load LCP image</li>
</ol>
""" + diagram("""
IMAGE SEO LAYERS
────────────────────────────────────────
Technical: format, size, CDN, srcset
On-page:   filename, alt, title, caption
Context:   surrounding text, schema ImageObject
Search:    Google Images, AI vision indexing
────────────────────────────────────────
""") + """
<h4>WordPress Example</h4>
<p>Media Library alt text field. Rank Math flags missing alt on post save. For WooCommerce, alt on product gallery images should describe variant (color, angle).</p>

<h4>AI Search Example</h4>
<p>Alt text and nearby captions help AI describe your content accurately when generating multimodal answers about products or tutorials.</p>
""" + case_study("Image Search Traffic", """
<p>Recipe site added descriptive alt and ImageObject schema. Google Images traffic rose 89%; 12% of image visitors converted to email subscribers.</p>
""") + mistake("<ul><li>Alt text 'image' or keyword lists</li><li>Uploading 4MB PNG screenshots</li><li>Lazy loading hero/LCP image</li></ul>"))
        + lesson(6, "Content Optimization and Readability", """
<p>On-page SEO extends to content depth, readability, freshness, and semantic coverage. Match or exceed top-ranking content quality for target queries.</p>

<h4>Content Optimization Framework</h4>
<ul>
<li><strong>Depth:</strong> Cover subtopics in cluster (Module 3)</li>
<li><strong>Readability:</strong> Grade 8–10 reading level for general audiences</li>
<li><strong>Structure:</strong> Short paragraphs, bullets, tables, visuals</li>
<li><strong>Freshness:</strong> Update stats and year in title annually</li>
<li><strong>E-E-A-T signals:</strong> Author bio, citations, first-hand experience</li>
</ul>
""" + diagram("""
CONTENT QUALITY SCORECARD
────────────────────────────────────────
[ ] Primary keyword in first 100 words
[ ] All cluster subtopics as H2 sections
[ ] 3+ internal links out, 2+ internal links in
[ ] Original images or diagrams
[ ] FAQ section matching PAA
[ ] Author with credentials
[ ] Updated date visible
────────────────────────────────────────
""") + """
<h4>WordPress Example</h4>
<p>Rank Math content analysis scores are training wheels—not gospel. Aim for green on focus keyword while maintaining natural prose. Use Table of Contents block for long guides.</p>
""" + case_study("Content Refresh", """
<p>2,000-word post from 2022 dropped from #4 to #11. Updated stats, added 800 words on AI search, refreshed schema. Recovered #3 within 4 weeks.</p>
""") + tip("<p>Compare word count and H2 count to top 3 SERP results—students need concrete benchmarks.</p>") + mistake("<ul><li>Thin content with filler</li><li>AI-generated content without expert review</li><li>Ignoring user questions in PAA</li></ul>"))
        + lesson(7, "On-Page SEO for WordPress Pages vs Posts", """
<p>WordPress pages and posts serve different roles. Posts suit dated, topical content; pages suit evergreen service and landing content. SEO tactics differ slightly.</p>

<h4>Posts</h4>
<ul>
<li>Category/tag taxonomy, author archives, date in schema</li>
<li>Ideal for blogs, news, tutorials</li>
<li>Consider Article schema with dateModified</li>
</ul>

<h4>Pages</h4>
<ul>
<li>Hierarchical parent/child (e.g., /services/seo-audit/)</li>
<li>No category clutter; focus on conversion</li>
<li>WebPage or Service schema</li>
</ul>
""" + diagram("""
WHEN TO USE POST VS PAGE
────────────────────────────────────────
POST:  blog, news, guides, comparisons
PAGE:  about, contact, services, landing
CUSTOM: products (WooCommerce), portfolios
────────────────────────────────────────
""") + """
<h4>Implementation Steps</h4>
<ol>
<li>Audit content types—move misplaced content</li>
<li>Set noindex on low-value archives (author, date) if thin</li>
<li>Ensure service pages not buried as posts with wrong URL</li>
<li>Configure Rank Math defaults per post type</li>
</ol>
""" + mistake("<ul><li>Important landing pages published as posts with /2026/ in URL</li><li>Duplicate service info across multiple pages</li></ul>"))
        + lesson(8, "On-Page Audit Workflow", """
<p>Combine lessons into a repeatable on-page audit workflow for any URL or site section.</p>

<h4>Audit Steps (Per URL)</h4>
<ol>
<li>Confirm target keyword and intent from content map</li>
<li>Check title, meta, H1, URL slug alignment</li>
<li>Evaluate heading structure and keyword coverage</li>
<li>Count internal links in/out</li>
<li>Audit images: alt, size, LCP impact</li>
<li>Score readability and depth vs SERP top 3</li>
<li>Document fixes in task tracker with priority</li>
</ol>
""" + diagram("""
ON-PAGE AUDIT REPORT TEMPLATE
══════════════════════════════════════════════════════════════
URL: _______________  Primary KW: _______________
Title: [pass/fail]  Meta: [pass/fail]  H1: [pass/fail]
Headings: [pass/fail]  Internal links: [count]
Images: [pass/fail]  Content depth: [word count vs SERP]
Priority fixes: 1. ___ 2. ___ 3. ___
══════════════════════════════════════════════════════════════
""") + case_study("Agency Audit Win", """
<p>Monthly on-page audits on 10 priority URLs for SaaS client compounded to 156% organic lead growth over 12 months—mostly from CTR and content depth fixes, not new links.</p>
""") + """
<h4>AI Search Example</h4>
<p>After on-page optimization, test if Perplexity cites your page for target query—on-page clarity directly affects AI extractability.</p>
""" + tip("<p>Workshop uses one real article—students see immediate before/after in snippet preview.</p>") + mistake("<ul><li>Auditing without priority order</li><li>Fixing meta only while ignoring content depth</li><li>No re-crawl verification after changes</li></ul>"))
    )

    workshop = """
<div class="workshop">
<strong>Workshop: Optimize an Article Step-by-Step</strong>
<h4>Duration:</h4> 2.5 hours
<h4>Materials:</h4> WordPress site access, Rank Math/Yoast, GSC data for one underperforming post, SERP screenshot for target keyword
<h4>Instructions:</h4>
<ol>
<li>Select one published post ranking position 8–20 with impressions in GSC</li>
<li>Record baseline: position, CTR, impressions, word count</li>
<li>Run SERP analysis on primary keyword; note top 3 content patterns</li>
<li>Rewrite title tag and meta description with CTR focus</li>
<li>Restructure headings: one H1, H2s for each cluster subtopic</li>
<li>Add 400+ words covering missing subtopics from SERP gap analysis</li>
<li>Add 3 contextual internal links in/out; optimize 5 images with alt text</li>
<li>Update modified date; request indexing in Search Console</li>
<li>Document all changes in audit template; set 14-day review reminder</li>
</ol>
<h4>Deliverable:</h4> Completed on-page audit report + before/after snippet screenshots + change log
</div>
"""

    notes = """
<ul>
<li>Provide sample underperforming post if students lack GSC access</li>
<li>Emphasize content additions over meta-only tweaks for lasting gains</li>
<li>Demo Rank Math snippet editor live; common confusion with title vs SEO title</li>
<li>Warn against changing URL slug during workshop without redirect plan</li>
<li>Celebrate small CTR wins—builds confidence before Module 5 technical depth</li>
</ul>
"""

    exercises = """<ol>
<li>Write three title tag variants for a given keyword and defend your choice.</li>
<li>Fix heading hierarchy in a provided broken HTML sample.</li>
<li>Create internal linking plan for a 5-page mini cluster.</li>
<li>Write alt text for 5 images following accessibility guidelines.</li>
</ol>"""

    homework = """<p>Perform full on-page audit on 3 additional URLs from your site. Implement fixes and write 500-word reflection comparing results after 7 days of GSC data.</p>"""

    quiz = """<ol>
<li>What is the recommended H1 count per page?</li>
<li>Do meta descriptions directly affect rankings?</li>
<li>What makes good internal link anchor text?</li>
<li>Why should LCP images not be lazy-loaded?</li>
<li>What character range is typical for meta descriptions?</li>
<li>How does heading hierarchy help SEO?</li>
<li>Name three image optimization tactics.</li>
<li>When should you use a Page instead of a Post?</li>
<li>What GSC metric indicates title/meta improvement opportunity?</li>
<li>What is the first step in an on-page audit?</li>
</ol>
<p><strong>Answer Key:</strong> 1) One 2) No, but affect CTR 3) Descriptive, natural, relevant to target page 4) Delays largest paint, hurts Core Web Vitals 5) ~150–160 characters 6) Structures content, signals topics, aids accessibility 7) Compress, WebP, alt text, descriptive filenames (any three) 8) Evergreen service/landing content 9) Low CTR at good positions 10) Confirm target keyword and intent</p>"""

    outcomes = """<ul>
<li>Write optimized title tags and meta descriptions</li>
<li>Structure content with proper H1–H6 hierarchy</li>
<li>Design internal linking strategies for topic clusters</li>
<li>Optimize images for search, speed, and accessibility</li>
<li>Execute a complete on-page audit workflow</li>
<li>Optimize a live WordPress article with measurable checklist</li>
</ul>"""

    return module_html(
        4, "On-Page SEO",
        [
            "Craft title tags and meta descriptions for CTR",
            "Structure headings H1–H6 correctly",
            "Build internal linking strategies",
            "Optimize images and alt text",
            "Optimize content depth and readability",
            "Execute on-page audits on WordPress content",
        ],
        [
            "Title Tags: Crafting Click-Worthy Headlines",
            "Meta Descriptions That Drive Clicks",
            "Heading Hierarchy H1–H6",
            "Internal Linking Strategy",
            "Image SEO and Alt Text",
            "Content Optimization and Readability",
            "On-Page SEO for WordPress Pages vs Posts",
            "On-Page Audit Workflow",
        ],
        lessons, workshop, notes, exercises, homework, quiz, outcomes,
    )


def _module_5():
    lessons = (
        lesson(1, "robots.txt and Crawl Control", """
<p>robots.txt tells crawlers which paths they may request. It does not guarantee exclusion from index (use noindex for that). Misconfigured robots.txt is a top cause of accidental deindexing.</p>

<h4>WordPress robots.txt Best Practice</h4>
<pre class="diagram">User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /wp-includes/
Disallow: /?s=
Disallow: /search/
Sitemap: https://example.com/sitemap_index.xml</pre>

<h4>Implementation Steps</h4>
<ol>
<li>Verify robots.txt at root (Rank Math or Yoast can manage)</li>
<li>Never Disallow critical CSS/JS needed for rendering</li>
<li>Do not block /wp-content/uploads/</li>
<li>Test with GSC robots.txt Tester</li>
<li>After changes, monitor Coverage report for 2 weeks</li>
</ol>
""" + diagram("""
ROBOTS.TXT vs NOINDEX
────────────────────────────────────────
robots.txt Disallow → may not crawl (can't see noindex)
noindex meta       → can crawl, won't index
Use noindex for thin archives; robots for admin paths
────────────────────────────────────────
""") + case_study("Accidental Block", """
<p>Developer Disallow'd entire /blog/ during staging migration; rule copied to production. Blog traffic zero in 10 days. Fix + resubmit sitemap; recovery took 21 days.</p>
""") + tip("<p>Show GSC Blocked by robots.txt report—visceral lesson.</p>") + mistake("<ul><li>Blocking CSS/JS</li><li>Using robots.txt for confidential data (use auth)</li><li>Duplicate conflicting robots rules</li></ul>"))
        + lesson(2, "XML Sitemaps", """
<p>XML sitemaps list URLs for crawlers—especially important for new sites, large sites, and pages with weak internal linking.</p>

<h4>Sitemap Types</h4>
<ul>
<li><strong>Index sitemap</strong> — Points to sub-sitemaps (posts, pages, products)</li>
<li><strong>Image sitemap</strong> — Optional for image-heavy sites</li>
<li><strong>News sitemap</strong> — For Google News publishers only</li>
</ul>

<h4>WordPress Example</h4>
<p>Rank Math generates <code>/sitemap_index.xml</code>. Exclude tags, author archives, and low-value params. Submit in GSC Sitemaps report. Regenerates on publish—no manual updates needed.</p>
""" + diagram("""
SITEMAP SUBMISSION FLOW
══════════════════════════════════════════════════════════════
WordPress → SEO Plugin → sitemap_index.xml
              │
              ▼
    Google Search Console → Submit URL
              │
              ▼
    Coverage report → Indexed / Discovered / Errors
══════════════════════════════════════════════════════════════
""") + case_study("Sitemap Gap", """
<p>12,000-product WooCommerce store had products excluded from sitemap due to hidden status bug in custom code. Fixing sitemap inclusion added 4,200 indexed products in 6 weeks.</p>
""") + mistake("<ul><li>Submitting broken or empty sitemap</li><li>Including noindex URLs in sitemap</li><li>Ignoring lastmod dates on stale content</li></ul>"))
        + lesson(3, "Canonical Tags and Duplicate Content", """
<p>Canonical tags tell Google which URL is the preferred version when duplicates exist (www/non-www, HTTP/HTTPS, parameters, print versions).</p>

<h4>Common Duplicate Scenarios in WordPress</h4>
<ul>
<li>Tag and category showing same posts</li>
<li>Pagination without self-referencing canonical</li>
<li>WWW vs non-WWW both accessible</li>
<li>UTM parameters creating duplicate URLs</li>
<li>Trailing slash inconsistencies</li>
</ul>

<h4>Implementation Steps</h4>
<ol>
<li>Set preferred domain in GSC (www or non-www)</li>
<li>Force HTTPS via plugin or server redirect</li>
<li>Rank Math canonical on paginated archives</li>
<li>Self-referencing canonical on every indexable page</li>
<li>Audit with Screaming Frog canonical report</li>
</ol>
""" + diagram("""
CANONICAL DECISION
────────────────────────────────────────
Duplicate URLs detected?
  → Pick master URL
  → rel=canonical on duplicates → master
  → 301 if permanently replaced
  → Consolidate content if needed
────────────────────────────────────────
""") + tip("<p>Parameter handling in GSC is legacy—prefer canonicals and redirects in modern setups.</p>") + mistake("<ul><li>Canonical pointing to 404</li><li>Cross-domain canonical without ownership</li><li>Canonical chain (A→B→C)</li></ul>"))
        + lesson(4, "Structured Data and Schema Markup", """
<p>Schema markup helps search engines understand entities, content types, and relationships. Rich results can improve CTR; incorrect schema triggers manual actions.</p>

<h4>Essential Schema Types for WordPress</h4>
<table>
<tr><th>Type</th><th>Use Case</th></tr>
<tr><td>Organization / LocalBusiness</td><td>Homepage, contact</td></tr>
<tr><td>Article / BlogPosting</td><td>Blog posts</td></tr>
<tr><td>Product</td><td>WooCommerce</td></tr>
<tr><td>FAQPage</td><td>FAQ sections</td></tr>
<tr><td>BreadcrumbList</td><td>Site navigation</td></tr>
</table>

<h4>WordPress Example</h4>
<p>Rank Math Schema tab per post. Validate with Google Rich Results Test. Do not mark up invisible content or fake reviews.</p>
""" + diagram("""
SCHEMA STACK FOR BLOG POST
────────────────────────────────────────
BlogPosting
  ├── author (Person)
  ├── publisher (Organization)
  ├── image (ImageObject)
  └── breadcrumb (BreadcrumbList)
Optional: FAQPage if visible FAQ section exists
────────────────────────────────────────
""") + case_study("FAQ Schema Win", """
<p>SaaS pricing page added visible FAQ with FAQPage schema. Expanded PAA presence; organic clicks +41% for commercial keywords.</p>
""") + """
<h4>AI Search Example</h4>
<p>Structured data reinforces entity relationships that AI systems extract for Knowledge Graph-style answers.</p>
""" + mistake("<ul><li>FAQ schema on hidden content</li><li>Review schema without real reviews</li><li>Wrong @type for page content</li></ul>"))
        + lesson(5, "Core Web Vitals", """
<p>Core Web Vitals (CWV) measure real-user experience: LCP (loading), INP (interactivity), CLS (visual stability). They affect rankings and conversions.</p>

<h4>Thresholds</h4>
<ul>
<li><strong>LCP:</strong> ≤ 2.5s good</li>
<li><strong>INP:</strong> ≤ 200ms good</li>
<li><strong>CLS:</strong> ≤ 0.1 good</li>
</ul>

<h4>WordPress Fixes</h4>
<ol>
<li>LiteSpeed Cache or WP Rocket for page cache</li>
<li>Optimize LCP image (preload, no lazy load)</li>
<li>Defer non-critical JS; minimize plugins</li>
<li>Set explicit width/height on images (CLS)</li>
<li>Use CDN for static assets</li>
</ol>
""" + diagram("""
CORE WEB VITALS DIAGNOSTIC
══════════════════════════════════════════════════════════════
LCP slow?  → hero image, server TTFB, render-blocking CSS
INP high?  → heavy JS, third-party scripts, no defer
CLS bad?   → ads, fonts, images without dimensions
══════════════════════════════════════════════════════════════
""") + case_study("CWV Recovery", """
<p>News site CLS 0.42 from ad injection. Reserved ad slots with min-height; CLS 0.06; combined with LCP preload, organic traffic +12% in 90 days.</p>
""") + tip("<p>Use CrUX data in PageSpeed Insights—field data beats lab scores for SEO decisions.</p>") + mistake("<ul><li>Optimizing lab score only</li><li>Lazy loading above-fold hero</li><li>Ignoring mobile field data</li></ul>"))
        + lesson(6, "Performance Optimization", """
<p>Performance extends beyond CWV to TTFB, caching layers, database optimization, and asset delivery.</p>

<h4>Performance Stack</h4>
<ul>
<li>Object cache (Redis) for high-traffic sites</li>
<li>Database cleanup (revisions, transients, autoloaded options)</li>
<li>Critical CSS; remove unused CSS where possible</li>
<li>Font display: swap; subset fonts</li>
<li>HTTP/2 multiplexing via modern host</li>
</ul>
""" + diagram("""
CACHE LAYERS
────────────────────────────────────────
Browser cache → CDN edge → Page cache → Object cache → DB
Each layer reduces origin hits and TTFB
────────────────────────────────────────
""") + """
<h4>Implementation Steps</h4>
<ol>
<li>Baseline TTFB and CWV in GSC Experience report</li>
<li>Enable server/page cache; verify cache hit headers</li>
<li>Audit plugins with Query Monitor</li>
<li>Limit post revisions; schedule WP-Optimize monthly</li>
<li>Re-test after each major plugin add</li>
</ol>
""" + mistake("<ul><li>10 caching plugins conflicting</li><li>Minify breaking JS</li><li>Never clearing cache after deploy</li></ul>"))
        + lesson(7, "Mobile SEO", """
<p>Google uses mobile-first indexing. Your mobile version is what Google primarily crawls and ranks.</p>

<h4>Mobile SEO Checklist</h4>
<ul>
<li>Responsive design; avoid separate m. subdomain unless properly linked</li>
<li>Tap targets 48px minimum; readable font 16px+</li>
<li>No intrusive interstitials blocking content</li>
<li>Same content on mobile and desktop (parity)</li>
<li>Test with Mobile-Friendly Test and real devices</li>
</ul>
""" + diagram("""
MOBILE-FIRST INDEXING
══════════════════════════════════════════════════════════════
Googlebot Smartphone → crawls mobile HTML
              │
              ▼
Content parity required with desktop
Hidden tab content OK if visible in HTML
Separate mobile URL needs rel=alternate
══════════════════════════════════════════════════════════════
""") + case_study("Mobile Parity Fail", """
<p>Desktop had 2,000 words; mobile theme stripped FAQs for clean UX. Rankings dropped 35%. Restored full content on mobile; recovered in 8 weeks.</p>
""") + tip("<p>Chrome DevTools device mode + URL Inspection mobile view—demo in class.</p>") + mistake("<ul><li>Hiding content behind tabs Google can't see</li><li>Blocking resources on mobile only</li><li>Separate URLs without hreflang/alternate</li></ul>"))
        + lesson(8, "Technical SEO Audit Workflow", """
<p>Synthesize Module 5 into a site-wide technical audit repeatable quarterly.</p>

<h4>Audit Categories</h4>
<ol>
<li>Crawlability: robots, sitemap, status codes</li>
<li>Indexation: coverage, canonicals, noindex</li>
<li>Schema: validation, rich result eligibility</li>
<li>Performance: CWV, TTFB, caching</li>
<li>Mobile: parity, usability</li>
<li>Security: HTTPS, mixed content, hacks</li>
</ol>
""" + diagram("""
TECHNICAL AUDIT PRIORITY MATRIX
────────────────────────────────────────
P0: Site blocked, mass 404s, hack, no HTTPS
P1: CWV fail, sitemap errors, canonical breaks
P2: Schema warnings, minor redirects
P3: Optimization opportunities
────────────────────────────────────────
""") + """
<h4>Tools</h4>
<p>Screaming Frog, Sitebulb, GSC, PageSpeed Insights, Rich Results Test, Security Headers scan.</p>
""" + case_study("Quarterly Audit ROI", """
<p>Agency quarterly technical audits averaged 23 fixable issues per client. Systematic P0/P1 resolution correlated with 34% fewer indexation tickets year-over-year.</p>
""") + mistake("<ul><li>Running audits without prioritized fix list</li><li>Fixing P3 while P0 sitemap broken</li><li>No ticket assignment or deadlines</li></ul>"))
    )

    workshop = """
<div class="workshop">
<strong>Workshop: Conduct a Technical SEO Audit</strong>
<h4>Duration:</h4> 3 hours
<h4>Materials:</h4> Screaming Frog (free 500 URLs) or Sitebulb trial, GSC access, PageSpeed Insights, spreadsheet
<h4>Instructions:</h4>
<ol>
<li>Crawl student WordPress site (or provided demo site) up to 500 URLs</li>
<li>Export: response codes, titles, canonicals, robots meta</li>
<li>Review GSC Coverage and Experience reports; screenshot issues</li>
<li>Test robots.txt and sitemap in GSC tools</li>
<li>Run Rich Results Test on homepage + one post + one product/page</li>
<li>PageSpeed Insights mobile: record LCP, INP, CLS field data if available</li>
<li>Compile P0–P3 issue list with recommended fixes</li>
<li>Fix at least one P1 issue live (e.g., sitemap, canonical, cache)</li>
<li>Present top 5 findings in 3-minute audit summary</li>
</ol>
<h4>Deliverable:</h4> Technical audit report (issues, priority, fix, owner) + proof of one implemented fix
</div>
"""

    notes = """
<ul>
<li>Pre-crawl a demo site with intentional errors for practice</li>
<li>Students overwhelm on Screaming Frog—provide export column guide</li>
<li>Emphasize GSC as source of truth over crawl-only tools</li>
<li>Schedule break before CWV section—dense material</li>
<li>Connect to Module 2 hosting choices when discussing TTFB</li>
</ul>
"""

    exercises = """<ol>
<li>Write robots.txt rules for a WooCommerce site excluding cart/checkout.</li>
<li>Identify canonical issues in a sample crawl export.</li>
<li>Choose schema types for 5 different WordPress page types.</li>
<li>Diagnose CWV failures from a provided PageSpeed report screenshot.</li>
</ol>"""

    homework = """<p>Complete full technical audit on your workshop site. Fix all P0/P1 issues and submit updated GSC screenshots after 7 days.</p>"""

    quiz = """<ol>
<li>Does robots.txt guarantee a URL won't be indexed?</li>
<li>Where do you submit XML sitemaps?</li>
<li>What does a canonical tag do?</li>
<li>Name three Core Web Vitals metrics.</li>
<li>What schema type suits a visible FAQ section?</li>
<li>What is mobile-first indexing?</li>
<li>Why shouldn't you block CSS in robots.txt?</li>
<li>What causes CLS issues?</li>
<li>What tool validates schema for rich results?</li>
<li>What is P0 in a technical audit?</li>
</ol>
<p><strong>Answer Key:</strong> 1) No—use noindex 2) Google Search Console 3) Indicates preferred URL among duplicates 4) LCP, INP, CLS 5) FAQPage 6) Google primarily uses mobile version for indexing 7) Google needs CSS to render page 8) Layout shift from unsized images, ads, fonts 9) Rich Results Test 10) Critical blockers (site down, hacked, mass errors)</p>"""

    outcomes = """<ul>
<li>Configure robots.txt and XML sitemaps correctly</li>
<li>Resolve duplicate content with canonicals and redirects</li>
<li>Implement valid structured data in WordPress</li>
<li>Diagnose and improve Core Web Vitals</li>
<li>Optimize mobile SEO and performance</li>
<li>Deliver a prioritized technical SEO audit</li>
</ul>"""

    return module_html(
        5, "Technical SEO",
        [
            "Configure robots.txt and crawl directives",
            "Manage XML sitemaps in WordPress",
            "Resolve duplicate content with canonicals",
            "Implement structured data and schema",
            "Optimize Core Web Vitals and performance",
            "Execute mobile SEO and technical audits",
        ],
        [
            "robots.txt and Crawl Control",
            "XML Sitemaps",
            "Canonical Tags and Duplicate Content",
            "Structured Data and Schema Markup",
            "Core Web Vitals",
            "Performance Optimization",
            "Mobile SEO",
            "Technical SEO Audit Workflow",
        ],
        lessons, workshop, notes, exercises, homework, quiz, outcomes,
    )


def _module_6():
    lessons = (
        lesson(1, "Topic Clusters and Content Architecture", """
<p>Topic clusters organize content around a central theme with a pillar page linking to detailed cluster pages. This architecture signals topical depth to search engines and improves internal linking efficiency.</p>

<h4>Cluster Components</h4>
<ul>
<li><strong>Pillar page</strong> — Broad overview (2,500–5,000 words) targeting head term</li>
<li><strong>Cluster pages</strong> — Specific subtopics (1,200–2,500 words each)</li>
<li><strong>Internal links</strong> — Bidirectional links between pillar and clusters</li>
<li><strong>URL structure</strong> — Logical hierarchy under one category or hub path</li>
</ul>
""" + diagram("""
TOPIC CLUSTER MODEL
══════════════════════════════════════════════════════════════
              [PILLAR: WordPress SEO]
                     │
     ┌───────┬───────┼───────┬───────┐
     ▼       ▼       ▼       ▼       ▼
  Plugins  Speed  Schema  Links  Content
  (cluster)(cluster)(cluster)(cluster)(cluster)
     │       │       │       │       │
     └───────┴───────┴───────┴───────┘
              all link back to pillar
══════════════════════════════════════════════════════════════
""") + case_study("Cluster Launch", """
<p>Marketing agency built 1 pillar + 12 clusters for "email marketing." Pillar ranked #8 in 14 weeks; clusters captured 47 long-tail keywords in top 10. Combined cluster traffic exceeded pillar 3:1.</p>
""") + """
<h4>WordPress Example</h4>
<p>Create pillar as Page under /guides/wordpress-seo/; clusters as Posts or child Pages. Use Rank Math pillar content template with TOC and jump links to cluster summaries.</p>

<h4>Implementation Steps</h4>
<ol>
<li>Choose pillar keyword from Module 3 content map</li>
<li>List 8–15 cluster subtopics from keyword clusters</li>
<li>Publish pillar first with placeholder links to planned clusters</li>
<li>Publish 2 clusters per week; update pillar links each time</li>
<li>Add "Related in this guide" block on each cluster</li>
</ol>
""" + tip("<p>Draw clusters on whiteboard before writing—prevents orphan spokes without pillar links.</p>") + mistake("<ul><li>Clusters without links back to pillar</li><li>Pillar too thin (under 1,500 words)</li><li>Clusters targeting different intent than pillar theme</li></ul>"))
        + lesson(2, "Pillar Pages: Design and Execution", """
<p>Pillar pages are comprehensive hub resources—not keyword-stuffed landing pages. They answer the head query while routing users to deeper cluster content.</p>

<h4>Pillar Page Structure</h4>
<ol>
<li>H1 with primary head term</li>
<li>Executive summary (150 words) for snippets and AI extraction</li>
<li>Table of contents with anchor links</li>
<li>H2 sections summarizing each cluster topic (300–500 words each)</li>
<li>Links to full cluster articles ("Read the full guide →")</li>
<li>FAQ section from PAA research</li>
<li>Author credentials and last updated date</li>
</ol>
""" + diagram("""
PILLAR PAGE WIREFRAME
────────────────────────────────────────
[H1 Head Term Guide]
[Summary paragraph - snippet bait]
[TOC]
[H2 Subtopic 1] → link to cluster
[H2 Subtopic 2] → link to cluster
...
[FAQ - 5 questions]
[Author box + CTA]
────────────────────────────────────────
""") + """
<h4>AI Search Example</h4>
<p>Pillar pages with clear H2 definitions often get cited in Perplexity for broad queries; cluster pages win specific long-tail citations.</p>
""" + case_study("Pillar Refresh", """
<p>Existing thin category page expanded to 4,200-word pillar with 10 cluster links. Average position for head term improved from 22 to 6 in 11 weeks.</p>
""") + mistake("<ul><li>Trying to rank pillar for every long-tail in clusters</li><li>No unique value on pillar (only links)</li><li>Outdated pillar not updated when clusters publish</li></ul>"))
        + lesson(3, "Content Hubs and Site Architecture", """
<p>Content hubs extend clusters into site-wide architecture—multiple pillars under a hub (e.g., /marketing/ hub containing SEO, email, social pillars).</p>

<h4>Hub vs Cluster vs Pillar</h4>
<table>
<tr><th>Level</th><th>Example</th><th>Role</th></tr>
<tr><td>Hub</td><td>/digital-marketing/</td><td>Category landing, links to pillars</td></tr>
<tr><td>Pillar</td><td>/digital-marketing/seo/</td><td>Comprehensive topic overview</td></tr>
<tr><td>Cluster</td><td>/digital-marketing/seo/technical/</td><td>Deep dive subtopic</td></tr>
</table>

<h4>WordPress Example</h4>
<p>Use parent/child Pages for hub → pillar hierarchy. Or custom post type "Guides" with taxonomy "Topic Hub." Breadcrumbs must reflect hierarchy for users and schema.</p>
""" + diagram("""
SITE HUB ARCHITECTURE
══════════════════════════════════════════════════════════════
[Home]
   └── [Hub: Digital Marketing]
          ├── [Pillar: SEO] ── clusters...
          ├── [Pillar: PPC] ── clusters...
          └── [Pillar: Content] ── clusters...
══════════════════════════════════════════════════════════════
""") + tip("<p>Limit hub depth to 3 clicks from homepage—crawl budget and UX both suffer beyond that.</p>") + mistake("<ul><li>Hub pages with only links, no unique intro content</li><li>Flat blog ignoring hub structure</li><li>Inconsistent URL patterns across hubs</li></ul>"))
        + lesson(4, "E-E-A-T: Experience, Expertise, Authoritativeness, Trust", """
<p>Google's quality rater guidelines emphasize E-E-A-T—especially for YMYL (Your Money Your Life) topics: health, finance, legal, safety.</p>

<h4>E-E-A-T Signals on WordPress</h4>
<ul>
<li><strong>Experience:</strong> First-hand photos, case results, "we tested" language</li>
<li><strong>Expertise:</strong> Author bios with credentials, citations to primary sources</li>
<li><strong>Authoritativeness:</strong> Backlinks, brand mentions, industry awards</li>
<li><strong>Trust:</strong> HTTPS, clear contact, privacy policy, accurate facts</li>
</ul>
""" + diagram("""
E-E-A-T ON-PAGE CHECKLIST
────────────────────────────────────────
[ ] Named author with bio page
[ ] datePublished + dateModified schema
[ ] Sources linked for statistics
[ ] About page with company history
[ ] Contact page with physical address if local
[ ] Editorial policy for AI-assisted content
────────────────────────────────────────
""") + case_study("YMYL Recovery", """
<p>Health blog without author bios lost 70% traffic after core update. Added MD-reviewed badges, author pages, medical citations. Recovered 55% over 6 months.</p>
""") + """
<h4>Implementation Steps</h4>
<ol>
<li>Create author custom post type or user profile pages</li>
<li>Add Person schema linked from Article author field</li>
<li>Display reviewer for regulated content</li>
<li>Publish About and Editorial Standards pages</li>
<li>Audit AI-generated content for factual review workflow</li>
</ol>
""" + mistake("<ul><li>Fake author personas</li><li>Anonymous blog for YMYL topics</li><li>No correction policy for outdated medical/legal info</li></ul>"))
        + lesson(5, "Topical Authority: Building Depth Over Breadth", """
<p>Topical authority means becoming the go-to source for a subject area—not ranking one lucky page. Google rewards sites that comprehensively cover a topic with consistent quality.</p>

<h4>Authority Building Tactics</h4>
<ul>
<li>Complete cluster coverage (no major gaps vs competitors)</li>
<li>Regular content updates and new cluster additions</li>
<li>Internal linking density within topic silo</li>
<li>External citations and links from niche publications</li>
<li>Brand searches growing for "yourbrand + topic"</li>
</ul>
""" + diagram("""
TOPICAL AUTHORITY MATURITY
────────────────────────────────────────
Stage 1: 1-3 pages on topic (weak)
Stage 2: Pillar + 5 clusters (emerging)
Stage 3: 20+ interconnected pages (competitive)
Stage 4: Industry citations + brand queries (authority)
────────────────────────────────────────
""") + """
<h4>WordPress Example</h4>
<p>Track topical coverage in spreadsheet: topic | pages published | pages indexed | avg position | gap vs competitor SERP count.</p>

<h4>AI Search Example</h4>
<p>Brands with dense, consistent topic coverage get cited more often in AI answers for category queries—Perplexity favors authoritative domains with multiple corroborating pages.</p>
""" + case_study("Niche Domination", """
<p>B2B cybersecurity blog published 34 interconnected cluster pages over 18 months. Became #1 organic referrer for "zero trust architecture" family—competitors with 3 posts couldn't compete despite higher DR.</p>
""") + tip("<p>Measure branded search volume in GSC as proxy for topical authority growth.</p>") + mistake("<ul><li>Random topics outside core niche</li><li>Abandoning cluster mid-build</li><li>Thin affiliate pages diluting authority</li></ul>"))
        + lesson(6, "Content Refresh and Consolidation", """
<p>Advanced strategy includes maintaining authority through refreshes and consolidating cannibalized or outdated content.</p>

<h4>Refresh Triggers</h4>
<ul>
<li>Position drop 5+ for 30 days</li>
<li>Competitor SERP format change (new sections required)</li>
<li>Statistics or product info outdated</li>
<li>New subtopic emerged (AI search, regulatory change)</li>
</ul>

<h4>Consolidation Process</h4>
<ol>
<li>Identify overlapping URLs via GSC and content audit</li>
<li>Choose strongest URL as survivor</li>
<li>Merge unique content from weaker pages</li>
<li>301 redirect losers to survivor</li>
<li>Update internal links sitewide</li>
</ol>
""" + diagram("""
REFRESH vs CONSOLIDATE DECISION
────────────────────────────────────────
Same intent, overlapping? → Consolidate + 301
Same URL, outdated?       → Refresh in place
Wrong format for SERP?    → Restructure + expand
Low quality beyond fix?   → Noindex or delete
────────────────────────────────────────
""") + case_study("Consolidation Win", """
<p>Five thin posts on "local SEO tips" merged into one 3,800-word guide. Four 301s. Traffic to survivor doubled; total cluster traffic up 80%.</p>
""") + mistake("<ul><li>Deleting without redirects</li><li>Refresh cosmetic only (date bump)</li><li>Consolidating pages with different intent</li></ul>"))
        + lesson(7, "Content Governance and Editorial Calendar", """
<p>Scale clusters with governance: roles, standards, calendar, and quality gates prevent inconsistent authority signals.</p>

<h4>Governance Elements</h4>
<ul>
<li>Content brief template (keyword, intent, cluster, E-E-A-T requirements)</li>
<li>Editorial calendar synced to pillar/cluster roadmap</li>
<li>Review workflow: writer → editor → SEO → publish</li>
<li>Style guide: headings, linking rules, schema requirements</li>
<li>Quarterly content audit calendar</li>
</ul>
""" + diagram("""
EDITORIAL WORKFLOW
══════════════════════════════════════════════════════════════
Brief → Draft → SEO Review → Legal (YMYL) → Publish
  ↑                              │
  └──────── Quarterly audit ─────┘
══════════════════════════════════════════════════════════════
""") + """
<h4>WordPress Example</h4>
<p>Use Editorial Calendar plugin or Notion + WordPress REST API. Tag posts with custom field "cluster_id" for reporting.</p>
""" + tip("<p>Assign one student as 'cluster owner' in workshop—mirrors agency roles.</p>") + mistake("<ul><li>No brief before writing</li><li>Publishing off-calendar random topics</li><li>Skipping SEO review for speed</li></ul>"))
        + lesson(8, "Measuring Content Strategy Success", """
<p>Measure clusters holistically—not single keyword rankings.</p>

<h4>KPIs by Level</h4>
<table>
<tr><th>Level</th><th>Metrics</th></tr>
<tr><td>Pillar</td><td>Head term position, impressions, assisted conversions</td></tr>
<tr><td>Cluster</td><td>Long-tail rankings count, internal link clicks</td></tr>
<tr><td>Hub</td><td>Total organic sessions in silo, indexed page ratio</td></tr>
<tr><td>Authority</td><td>Brand queries, referring domains to silo, AI citations</td></tr>
</table>
""" + diagram("""
CONTENT STRATEGY DASHBOARD
────────────────────────────────────────
Cluster: WordPress SEO
  Pages: 14 | Indexed: 13 | Avg pos: 11.2
  Organic sessions (90d): 4,820
  Top gap: "wordpress hreflang" - not published
────────────────────────────────────────
""") + case_study("Dashboard Discipline", """
<p>Agency shared monthly cluster dashboard with clients. Content investment aligned to gap data; clients renewing retainers 92% vs 71% without dashboard.</p>
""") + """
<h4>Implementation Steps</h4>
<ol>
<li>Tag content by cluster in WordPress</li>
<li>Build Looker Studio or Sheets dashboard from GSC export</li>
<li>Review monthly: gaps, refresh candidates, consolidation candidates</li>
<li>Report wins as cluster-level, not vanity single keywords</li>
</ol>
""" + mistake("<ul><li>Judging strategy by one pillar rank only</li><li>No gap analysis vs competitors</li><li>Ignoring zero-click growth in impressions</li></ul>"))
    )

    workshop = """
<div class="workshop">
<strong>Workshop: Build a Topical Authority Map</strong>
<h4>Duration:</h4> 2.5 hours
<h4>Materials:</h4> Keyword map from Module 3, Miro/FigJam or spreadsheet, competitor site for gap analysis
<h4>Instructions:</h4>
<ol>
<li>Choose one core topic aligned to business (e.g., "WordPress SEO" or client niche)</li>
<li>Define hub URL and 1 pillar URL with target head keyword</li>
<li>Plan 10 cluster pages with primary keywords from existing research</li>
<li>Draw internal linking diagram: pillar ↔ clusters ↔ hub</li>
<li>Audit top competitor: count their pages in same topic; note gaps</li>
<li>Assign E-E-A-T requirements per page (author, citations, schema)</li>
<li>Build 90-day editorial calendar: publish order and refresh dates</li>
<li>Write 200-word pillar executive summary (snippet/AI bait)</li>
<li>Present authority map in 5-minute pitch to class</li>
</ol>
<h4>Deliverable:</h4> Topical authority map (visual + spreadsheet) + pillar outline + 90-day calendar
</div>
"""

    notes = """
<ul>
<li>Connect to Module 3 keyword map—students should reuse prior work</li>
<li>Common mistake: 20 clusters planned, none published—cap at 10 for realism</li>
<li>Discuss YMYL if students choose health/finance topics</li>
<li>Show real hub example (Ahrefs blog, HubSpot topic clusters)</li>
<li>Module 8 entity SEO extends this architecture—foreshadow relationships</li>
</ul>
"""

    exercises = """<ol>
<li>Sketch a topic cluster with 1 pillar and 6 spokes for a hobby blog.</li>
<li>Write E-E-A-T improvement plan for a sample anonymous health article.</li>
<li>Decide refresh vs consolidate for three overlapping URL scenarios.</li>
<li>Define 5 KPIs for a content hub dashboard.</li>
</ol>"""

    homework = """<p>Draft full pillar page outline (H1, H2s, FAQ, cluster links) for your authority map topic. 1,000-word narrative explaining competitive gap and why your cluster order prioritizes revenue.</p>"""

    quiz = """<ol>
<li>What is a pillar page?</li>
<li>How do cluster pages connect to pillars?</li>
<li>What does the second E in E-E-A-T stand for?</li>
<li>What is topical authority?</li>
<li>When should you consolidate two URLs?</li>
<li>What is a content hub?</li>
<li>Name two E-E-A-T trust signals.</li>
<li>What triggers a content refresh?</li>
<li>Why bidirectional internal links in clusters?</li>
<li>What metric shows emerging topical authority beyond rankings?</li>
</ol>
<p><strong>Answer Key:</strong> 1) Comprehensive hub page for broad topic 2) Internal links both ways 3) Experience 4) Being recognized comprehensive source for a subject 5) Same intent, overlapping/cannibalizing content 6) Site section linking multiple pillars 7) HTTPS, contact info, accurate content (any two) 8) Rank drop, outdated info, SERP format change (any) 9) Distributes authority and aids discovery 10) Brand queries, impression growth, AI citations</p>"""

    outcomes = """<ul>
<li>Design topic clusters with pillars and spokes</li>
<li>Build pillar pages and content hub architecture</li>
<li>Implement E-E-A-T signals in WordPress</li>
<li>Develop topical authority strategically</li>
<li>Govern content with editorial workflows</li>
<li>Deliver a topical authority map with calendar</li>
</ul>"""

    return module_html(
        6, "Advanced Content Strategy",
        [
            "Design topic clusters and pillar pages",
            "Architect content hubs for site structure",
            "Apply E-E-A-T principles to WordPress content",
            "Build topical authority over time",
            "Refresh and consolidate content strategically",
            "Measure content strategy at cluster level",
        ],
        [
            "Topic Clusters and Content Architecture",
            "Pillar Pages: Design and Execution",
            "Content Hubs and Site Architecture",
            "E-E-A-T: Experience, Expertise, Authoritativeness, Trust",
            "Topical Authority: Building Depth Over Breadth",
            "Content Refresh and Consolidation",
            "Content Governance and Editorial Calendar",
            "Measuring Content Strategy Success",
        ],
        lessons, workshop, notes, exercises, homework, quiz, outcomes,
    )


def _module_7():
    lessons = (
        lesson(1, "Local SEO Fundamentals", """
<p>Local SEO optimizes visibility for geographically relevant searches—"near me," city + service queries, and map pack results. Critical for brick-and-mortar and service-area businesses.</p>

<h4>Local Ranking Factors</h4>
<ul>
<li>Google Business Profile (GBP) optimization</li>
<li>Relevance, distance, prominence (Google's local algorithm)</li>
<li>NAP consistency (Name, Address, Phone)</li>
<li>Reviews quantity, velocity, and sentiment</li>
<li>Local citations and backlinks</li>
<li>Localized on-page content and schema</li>
</ul>
""" + diagram("""
LOCAL SEO ECOSYSTEM
══════════════════════════════════════════════════════════════
        [Google Business Profile]
              │    │    │
    ┌─────────┘    │    └─────────┐
    ▼              ▼              ▼
 Reviews      Citations    Website
    │              │              │
    └──────────────┴──────────────┘
              Local Pack Rankings
══════════════════════════════════════════════════════════════
""") + case_study("Map Pack Entry", """
<p>Plumber optimized GBP + 40 citations + location pages. Map pack appearance for "emergency plumber [city]" within 5 weeks; call volume +180%.</p>
""") + """
<h4>WordPress Example</h4>
<p>LocalBusiness schema on homepage; location pages as Pages with unique content per city; embed Google Map on contact page.</p>
""" + tip("<p>Search target keyword in incognito with city VPN or location spoofing—SERP varies by geography.</p>") + mistake("<ul><li>Using PO box as address on GBP</li><li>Identical location page copy with city swap only</li><li>Ignoring service-area vs storefront distinction</li></ul>"))
        + lesson(2, "Google Business Profile Optimization", """
<p>GBP is the centerpiece of local SEO. Complete every field; post weekly; respond to all reviews; use accurate categories.</p>

<h4>GBP Optimization Checklist</h4>
<ol>
<li>Primary category most specific to core service</li>
<li>Secondary categories (up to 9) relevant and honest</li>
<li>Business description with keywords natural, 750 chars</li>
<li>Services list with descriptions</li>
<li>Photos: exterior, interior, team, products—geo-tagged when authentic</li>
<li>Posts: offers, events, updates weekly</li>
<li>Q&amp;A seeded with real customer questions</li>
<li>Appointment/booking link if applicable</li>
</ol>
""" + diagram("""
GBP COMPLETENESS SCORE (SELF-AUDIT)
────────────────────────────────────────
[ ] Primary + 3 secondary categories
[ ] 10+ photos uploaded this quarter
[ ] Weekly Google Posts
[ ] 100% review response rate
[ ] Products/services filled
[ ] Hours including holidays
────────────────────────────────────────
""") + """
<h4>Implementation Steps</h4>
<ol>
<li>Claim and verify GBP ( postcard, phone, or video)</li>
<li>Audit against checklist; screenshot before state</li>
<li>Align NAP exactly with website footer and schema</li>
<li>Enable messaging only if monitored daily</li>
<li>Track GBP insights: calls, direction requests, website clicks</li>
</ol>
""" + case_study("Category Fix", """
<p>Restaurant listed as "Restaurant" only. Added "Italian Restaurant" primary + "Pizza Delivery" secondary. Impressions +340% for "italian food near me" in 8 weeks.</p>
""") + mistake("<ul><li>Keyword-stuffed business name (spam policy)</li><li>Fake reviews or review gating</li><li>Virtual office address for SAB without hiding address properly</li></ul>"))
        + lesson(3, "Citations and NAP Consistency", """
<p>Citations are online mentions of business NAP on directories, social profiles, and industry sites. Consistency strengthens entity trust.</p>

<h4>Core Citations</h4>
<ul>
<li>Google Business Profile, Bing Places, Apple Business Connect</li>
<li>Facebook, LinkedIn, Yelp, BBB</li>
<li>Industry-specific: Avvo (legal), Healthgrades (medical), Houzz (home)</li>
<li>Data aggregators: Data Axle, Foursquare, Neustar Localeze</li>
</ul>
""" + diagram("""
NAP CONSISTENCY RULE
────────────────────────────────────────
Name:    Exact legal/trade name everywhere
Address: Same format (St vs Street, suite #)
Phone:   One primary local number; track with call tracking carefully

Mismatch → split entity signals → lower local rank
────────────────────────────────────────
""") + """
<h4>WordPress Example</h4>
<p>Footer NAP matches GBP character-for-character. LocalBusiness schema uses same values. Use <code>sameAs</code> in schema for social/directory URLs.</p>

<h4>Implementation Steps</h4>
<ol>
<li>Export existing citations with BrightLocal or manual search</li>
<li>Document master NAP in style guide</li>
<li>Fix top 20 citations first (highest authority)</li>
<li>Build new citations on industry directories monthly</li>
<li>Monitor for rogue duplicates or old addresses</li>
</ol>
""" + case_study("NAP Cleanup", """
<p>Law firm had 3 address variants across 60 citations. Normalized over 90 days; local pack stability improved; stopped fluctuating rank 3–12 daily.</p>
""") + tip("<p>Call tracking numbers OK on website if NAP citations use primary local number—document in client guide.</p>") + mistake("<ul><li>Automated citation spam on low-quality directories</li><li>Different business names on Yelp vs GBP</li><li>Ignoring duplicate GBP listings</li></ul>"))
        + lesson(4, "Reviews: Acquisition and Management", """
<p>Reviews influence prominence and conversion. Google prohibits incentives for reviews but encourages ethical acquisition.</p>

<h4>Review Strategy</h4>
<ul>
<li>Ask at point of satisfaction (email follow-up, SMS, receipt QR)</li>
<li>Respond to all reviews within 48 hours</li>
<li>Address negatives professionally; take offline when needed</li>
<li>Never buy reviews or use review gating ("only if 5 stars")</li>
<li>Track review velocity vs competitors</li>
</ul>
""" + diagram("""
REVIEW RESPONSE FRAMEWORK
────────────────────────────────────────
Positive: Thank + specific detail + invite return
Negative: Apologize + acknowledge + offline resolution offer
Fake:     Flag via GBP; professional public response
────────────────────────────────────────
""") + """
<h4>WordPress Example</h4>
<p>Embed Google reviews widget on homepage via plugin or Elfsight. Add Review schema only for aggregated on-site testimonials you control—not for pulling GBP stars into fake markup.</p>

<h4>AI Search Example</h4>
<p>AI local recommendations often cite businesses with strong recent review sentiment and consistent entity data across sources.</p>
""" + case_study("Review Velocity", """
<p>Dental practice implemented post-appointment email with direct GBP review link. Reviews/month rose from 2 to 11; map pack rank stabilized top 3.</p>
""") + mistake("<ul><li>Review gating violations</li><li>Keyword stuffing in review responses</li><li>Ignoring negative reviews</li></ul>"))
        + lesson(5, "Local Landing Pages and Content", """
<p>Multi-location businesses need unique location pages—not doorway pages with swapped city names.</p>

<h4>Location Page Requirements</h4>
<ul>
<li>Unique H1: Service + City</li>
<li>NAP, hours, embedded map, driving directions</li>
<li>Staff photos, local testimonials, case studies</li>
<li>Localized FAQ (parking, service area, local regulations)</li>
<li>LocalBusiness schema with geo coordinates</li>
</ul>
""" + diagram("""
LOCATION PAGE STRUCTURE
══════════════════════════════════════════════════════════════
H1: [Service] in [City, State]
[NAP block + map]
[Unique intro - 200+ words about local area service]
[Services at this location]
[Local testimonials]
[FAQ specific to location]
[CTA: call / book]
══════════════════════════════════════════════════════════════
""") + """
<h4>WordPress Example</h4>
<p>Parent Page "Locations" with child pages per city. Or custom post type "Location" with template single-location.php. Avoid creating 500 thin pages—consolidate to real service areas.</p>
""" + case_study("Doorway Penalty Avoided", """
<p>Franchise had 200 auto-generated location pages. Rewrote top 30 with unique content; noindexed rest. Traffic consolidated to quality pages; no manual penalty.</p>
""") + mistake("<ul><li>500 doorway pages with template swap</li><li>Same meta title except city</li><li>No physical presence claiming local pages</li></ul>"))
        + lesson(6, "Local Link Building and PR", """
<p>Local prominence requires local links: chambers, sponsors, news, community events, partnerships.</p>

<h4>Local Link Tactics</h4>
<ol>
<li>Chamber of Commerce membership</li>
<li>Sponsor local events, sports teams, charities</li>
<li>Local news pitches (new hire, community initiative)</li>
<li>Partner with complementary businesses (cross-link)</li>
<li>University and government resource pages</li>
</ol>
""" + diagram("""
LOCAL LINK SOURCES
────────────────────────────────────────
Chamber → .org authority + NAP
Local news → editorial link + brand
Sponsorship → logo link + community signal
HARO/local angles → journalist citations
────────────────────────────────────────
""") + tip("<p>Students love success stories—feature local bakery that got link from city blog.</p>") + mistake("<ul><li>Buying local directory spam links</li><li>Irrelevant national links ignoring local</li><li>Exact-match anchor overuse in press releases</li></ul>"))
        + lesson(7, "Maps Optimization and Geo-Targeting", """
<p>Map pack ranking combines GBP signals with website localization and user behavior (clicks, calls, directions).</p>

<h4>Maps Optimization Actions</h4>
<ul>
<li>Verify pin location accuracy on GBP</li>
<li>Service area configuration for SAB (service-area businesses)</li>
<li>Geo-modifiers in title tags where natural (not spam)</li>
<li>Mobile click-to-call prominent above fold</li>
<li>Track direction requests in GBP insights</li>
</ul>
""" + diagram("""
LOCAL PACK RANKING FACTORS (SIMPLIFIED)
────────────────────────────────────────
Relevance  → categories, content, reviews text
Distance   → user location vs business
Prominence → reviews, links, authority, behavior
────────────────────────────────────────
""") + """
<h4>WordPress Example</h4>
<p>Service-area business: hide address on GBP if legitimate SAB; show service radius. Website lists cities served with unique content pages only for primary markets.</p>
""" + case_study("SAB Configuration", """
<p>HVAC company showed home address on GBP—received spam visits. Switched to service-area business with defined radius; relevant leads up 40%, irrelevant visits down.</p>
""") + mistake("<ul><li>Fake locations or virtual offices</li><li>Geo-keyword stuffing in business name</li><li>Wrong map pin location</li></ul>"))
        + lesson(8, "Local SEO Audit and Reporting", """
<p>Combine local signals into repeatable audit and client reporting workflow.</p>

<h4>Local Audit Checklist</h4>
<ol>
<li>GBP completeness and policy compliance</li>
<li>NAP consistency (top 30 citations)</li>
<li>Review count, rating, response rate vs competitors</li>
<li>Location page quality and indexation</li>
<li>LocalBusiness schema validation</li>
<li>Local pack rank tracking for 10 core queries</li>
<li>GBP insights trend (90-day)</li>
</ol>
""" + diagram("""
LOCAL SEO REPORT TEMPLATE
══════════════════════════════════════════════════════════════
Map pack rank: [keyword] [#] (prev [#])
GBP views: +X% | Calls: +Y% | Direction requests: +Z%
Reviews: X total, Y new, Z avg rating
Citation accuracy: X% fixed
Priority actions: 1. 2. 3.
══════════════════════════════════════════════════════════════
""") + """
<h4>Tools</h4>
<p>BrightLocal, Whitespark, Local Falcon (grid rank tracking), GSC filtered by city landing pages, GBP insights.</p>
""" + case_study("Client Retention", """
<p>Monthly local SEO reports with map grid screenshots reduced client churn 40% for agency—visual proof of map pack movement.</p>
""") + mistake("<ul><li>Reporting only rankings, not calls/directions</li><li>Single-point rank check vs grid</li><li>Ignoring competitor GBP changes</li></ul>"))
    )

    workshop = """
<div class="workshop">
<strong>Workshop: Optimize a Local Business</strong>
<h4>Duration:</h4> 3 hours
<h4>Materials:</h4> Real local business (student employer or provided case), GBP access or public audit, BrightLocal trial optional, spreadsheet
<h4>Instructions:</h4>
<ol>
<li>Select local business; document current GBP state with screenshots</li>
<li>Complete GBP audit checklist; score /100</li>
<li>Rewrite business description and services list</li>
<li>Identify NAP inconsistencies across 10 citations; create fix list</li>
<li>Analyze top 3 competitors: reviews, categories, photos, posts</li>
<li>Draft one location/service page outline with unique local content</li>
<li>Create review acquisition email template (policy-compliant)</li>
<li>Plan 5 local link opportunities in community</li>
<li>Run Local Falcon or manual map check for 5 keywords</li>
<li>Present 90-day local SEO action plan</li>
</ol>
<h4>Deliverable:</h4> Local SEO audit report + optimized GBP copy + 90-day action plan + location page outline
</div>
"""

    notes = """
<ul>
<li>Use fictional business if no GBP access—but real is better</li>
<li>Review Google GBP guidelines handout—policy violations are common student errors</li>
<li>Discuss service-area vs storefront early</li>
<li>Sensitive industries (medical, legal) have extra E-E-A-T requirements</li>
<li>Demo grid rank tool—visual impact keeps engagement high</li>
</ul>
"""

    exercises = """<ol>
<li>Score a sample GBP profile against the completeness checklist.</li>
<li>Fix NAP inconsistencies in a provided citation table.</li>
<li>Write compliant review response to a 2-star negative review.</li>
<li>Outline location page for a second city without doorway content.</li>
</ol>"""

    homework = """<p>Implement at least 3 GBP improvements on workshop business (or simulate with before/after copy). Write 600-word report on competitor gap analysis and review strategy.</p>"""

    quiz = """<ol>
<li>What does NAP stand for?</li>
<li>Name three local ranking factor categories.</li>
<li>What is review gating?</li>
<li>Why must NAP match across citations?</li>
<li>What schema type suits a local business homepage?</li>
<li>What is a service-area business (SAB)?</li>
<li>Name two ethical review acquisition tactics.</li>
<li>What makes a location page a doorway page?</li>
<li>Where do you track calls and direction requests?</li>
<li>What tool shows map pack rank by geographic grid?</li>
</ol>
<p><strong>Answer Key:</strong> 1) Name, Address, Phone 2) Relevance, distance, prominence 3) Asking only happy customers to review publicly 4) Consistent entity signals for Google trust 5) LocalBusiness 6) Business serving customers at location without public storefront 7) Post-service email, QR on receipt (any compliant tactic) 8) Thin duplicate content with only city swapped 9) GBP insights 10) Local Falcon (or similar grid tracker)</p>"""

    outcomes = """<ul>
<li>Explain local SEO ranking factors</li>
<li>Optimize Google Business Profile completely</li>
<li>Build and audit local citations with NAP consistency</li>
<li>Manage reviews ethically and effectively</li>
<li>Create quality local landing pages</li>
<li>Deliver local SEO audit and 90-day plan</li>
</ul>"""

    return module_html(
        7, "Local SEO",
        [
            "Understand local search ranking factors",
            "Optimize Google Business Profile",
            "Manage citations and NAP consistency",
            "Build review acquisition and response systems",
            "Create localized landing pages in WordPress",
            "Execute local SEO audits and reporting",
        ],
        [
            "Local SEO Fundamentals",
            "Google Business Profile Optimization",
            "Citations and NAP Consistency",
            "Reviews: Acquisition and Management",
            "Local Landing Pages and Content",
            "Local Link Building and PR",
            "Maps Optimization and Geo-Targeting",
            "Local SEO Audit and Reporting",
        ],
        lessons, workshop, notes, exercises, homework, quiz, outcomes,
    )


def _module_8():
    lessons = (
        lesson(1, "Entities in Modern Search", """
<p>An entity is a uniquely identifiable thing—a person, place, organization, product, or concept—that search engines represent in knowledge systems. SEO is shifting from keywords to entities and relationships.</p>

<h4>Entity vs Keyword</h4>
<table>
<tr><th>Keyword</th><th>Entity</th></tr>
<tr><td>String users type</td><td>Real-world thing with attributes</td></tr>
<tr><td>"apple nutrition"</td><td>Apple (fruit) vs Apple Inc. (company)</td></tr>
<tr><td>Exact match focus</td><td>Disambiguation via context</td></tr>
</table>
""" + diagram("""
ENTITY RESOLUTION
══════════════════════════════════════════════════════════════
Query: "jaguar speed"
         │
    Context analysis
         │
    ┌────┴────┐
    ▼         ▼
[Animal]   [Car brand]
 different   different
  SERP        SERP
══════════════════════════════════════════════════════════════
""") + case_study("Entity Disambiguation", """
<p>Tech blog post titled "Python tips" ranked poorly—Google interpreted as snake. Renamed to "Python Programming Tips," added SoftwareSourceCode schema and author dev credentials. Rankings recovered for programming intent.</p>
""") + """
<h4>WordPress Example</h4>
<p>Use Organization and Person schema; link authors to LinkedIn via sameAs; mention full entity names on first reference in content.</p>
""" + tip("<p>Link Module 1 Knowledge Graph lesson—students connect history to this module.</p>") + mistake("<ul><li>Ambiguous titles without context</li><li>Ignoring entity disambiguation in international markets</li><li>Treating brand as keyword only, not entity</li></ul>"))
        + lesson(2, "Knowledge Graphs and Knowledge Panels", """
<p>Google's Knowledge Graph stores entities and relationships. Knowledge Panels display entity summaries on branded searches.</p>

<h4>How to Influence Knowledge Panels</h4>
<ul>
<li>Claim Google Business Profile (local businesses)</li>
<li>Wikipedia/Wikidata entry if notable (notable = Wikipedia guidelines)</li>
<li>Consistent entity data across web (sameAs links)</li>
<li>Official social profiles linked from website</li>
<li>Google Search Console entity tools where available</li>
</ul>
""" + diagram("""
KNOWLEDGE PANEL DATA SOURCES
────────────────────────────────────────
Wikipedia/Wikidata → high trust
Official website   → schema + about page
Google Business    → local entities
Social profiles    → corroboration
News publications  → prominence
────────────────────────────────────────
""") + """
<h4>Implementation Steps</h4>
<ol>
<li>Audit branded SERP: panel present? accurate?</li>
<li>Ensure About page defines entity clearly</li>
<li>Add Organization schema with logo, sameAs array</li>
<li>Submit corrections via feedback link on panel if errors</li>
<li>Build prominence through PR and authoritative mentions</li>
</ol>
""" + case_study("Panel Correction", """
<p>SaaS company Knowledge Panel showed wrong founding date from scraper site. Updated Wikidata, About page, and Crunchbase; submitted panel feedback; corrected in 6 weeks.</p>
""") + mistake("<ul><li>Creating fake Wikipedia pages (gets deleted)</li><li>Inconsistent founding dates across web</li><li>Expecting panel for non-notable brand immediately</li></ul>"))
        + lesson(3, "Semantic Search and Natural Language", """
<p>Semantic search understands meaning and relationships—not just keyword matching. BERT, MUM, and LLMs power this understanding across Google and AI search.</p>

<h4>Optimizing for Semantic Search</h4>
<ul>
<li>Cover related concepts and synonyms naturally</li>
<li>Answer questions explicitly (who, what, when, where, why, how)</li>
<li>Use structured headings matching query patterns</li>
<li>Link related entities internally</li>
<li>Avoid keyword density obsession</li>
</ul>
""" + diagram("""
SEMANTIC COVERAGE MAP
────────────────────────────────────────
Primary entity: [Rank Math SEO Plugin]
Related: WordPress SEO, schema markup, sitemap,
         Google Search Console, focus keyword
Relationships: builtBy → Rank Math team
               competesWith → Yoast SEO
────────────────────────────────────────
""") + """
<h4>AI Search Example</h4>
<p>Query ChatGPT: "How does Rank Math compare to Yoast?" Systems extract entities Rank Math, Yoast SEO, attributes (features, pricing), and relationship (competitor). Content with clear comparison tables gets cited.</p>

<h4>WordPress Example</h4>
<p>Write semantically rich FAQ sections; use Rank Math's related keywords as coverage checklist, not stuffing list.</p>
""" + case_study("Semantic Expansion", """
<p>Article on "canonical tags" expanded with sections on duplicates, hreflang, and parameter handling—semantically related subtopics. Impressions doubled; ranked for 40 related queries beyond primary.</p>
""") + tip("<p>Use Google's NLP API or simply PAA + related searches for semantic gap list.</p>") + mistake("<ul><li>Synonym stuffing invisible to users</li><li>Single-keyword page ignoring related concepts</li><li>Over-relying on plugin keyword density scores</li></ul>"))
        + lesson(4, "Structured Relationships with Schema", """
<p>Schema markup expresses entity relationships explicitly: author worksFor Organization, Product brand is Brand, LocalBusiness parentOrganization.</p>

<h4>Key Relationship Properties</h4>
<ul>
<li><code>sameAs</code> — Links entity to official profiles</li>
<li><code>author</code> / <code>publisher</code> — Content attribution</li>
<li><code>about</code> / <code>mentions</code> — Topic entities in content</li>
<li><code>hasPart</code> / <code>isPartOf</code> — Hub/cluster structure</li>
<li><code>founder</code>, <code>employee</code>, <code>brand</code> — Org relationships</li>
</ul>
""" + diagram("""
ORGANIZATION ENTITY GRAPH (SCHEMA)
══════════════════════════════════════════════════════════════
Organization: Acme SEO Agency
  ├── sameAs → [LinkedIn, Twitter, Crunchbase]
  ├── founder → Person: Jane Doe
  ├── employee → Person: John Smith
  ├── location → Place: Austin, TX
  └── makesOffer → Service: SEO Audit
══════════════════════════════════════════════════════════════
""") + """
<h4>WordPress Example</h4>
<p>Rank Math Organization schema with sameAs. For articles, connect Person author to Organization via worksFor in custom schema JSON-LD if needed.</p>

<h4>Implementation Steps</h4>
<ol>
<li>Map entity relationships for your company on whiteboard</li>
<li>Implement Organization schema sitewide</li>
<li>Add Person schema for key authors</li>
<li>Validate with Rich Results Test and Schema Markup Validator</li>
<li>Document JSON-LD in technical SEO runbook</li>
</ol>
""" + mistake("<ul><li>Marking up entities not visible on page</li><li>Broken sameAs links to 404 profiles</li><li>Conflicting @id across pages</li></ul>"))
        + lesson(5, "Entity SEO for Brands and Products", """
<p>Brands and products are entities requiring consistent naming, identifiers, and cross-platform presence.</p>

<h4>Brand Entity Checklist</h4>
<ul>
<li>Consistent brand name spelling and capitalization</li>
<li>Logo in schema Organization.logo ImageObject</li>
<li>Product schema on WooCommerce with SKU, brand, offers</li>
<li>Brand + product mentions in authoritative third-party sites</li>
<li>Google Merchant Center for product entities</li>
</ul>
""" + diagram("""
PRODUCT ENTITY (WOOCOMMERCE)
────────────────────────────────────────
@type: Product
name: Organic Dog Food 5lb
brand: @type Brand, name: PawNatural
sku: PN-DF-5
offers: price, availability, url
aggregateRating: (if genuine reviews)
────────────────────────────────────────
""") + case_study("Product Rich Results", """
<p>WooCommerce store added valid Product schema with real reviews and in-stock offers. Rich results impressions +220%; CTR on product SERPs +1.8%.</p>
""") + """
<h4>AI Search Example</h4>
<p>AI shopping assistants resolve Product entities by brand + attributes. Incomplete product data (missing brand, vague titles) loses citations to retailers with structured catalogs.</p>
""" + tip("<p>Align WooCommerce product titles with how users and AI describe products—not internal SKUs.</p>") + mistake("<ul><li>Product title keyword spam</li><li>Fake aggregateRating schema</li><li>Inconsistent brand name (Acme vs ACME vs Acme Inc.)</li></ul>"))
        + lesson(6, "Topical Entities and Content Hubs", """
<p>Connect Module 6 hubs to entity thinking: your pillar topic is an entity; cluster pages mention related entities and build topical graphs.</p>

<h4>Entity-Based Content Planning</h4>
<ol>
<li>Identify core entity (topic or product category)</li>
<li>List related entities from Knowledge Graph, PAA, Wikipedia categories</li>
<li>Assign one primary entity focus per URL</li>
<li>Cross-link entities via internal links and schema mentions</li>
<li>Build entity glossary pages for complex niches</li>
</ol>
""" + diagram("""
TOPICAL ENTITY HUB
══════════════════════════════════════════════════════════════
[Entity: Technical SEO]
    ├── Crawling (entity)
    ├── Indexing (entity)
    ├── Core Web Vitals (entity)
    └── Schema Markup (entity)
Each page defines entity + links to related entities
══════════════════════════════════════════════════════════════
""") + """
<h4>WordPress Example</h4>
<p>Create glossary custom post type; link terms from articles; use DefinedTerm schema where appropriate.</p>
""" + case_study("Glossary Strategy", """
<p>MarTech site published 80 glossary entities with DefinedTerm schema. Collective traffic 45% of blog; AI tools cite glossary for definitional queries.</p>
""") + mistake("<ul><li>Thin glossary pages with one sentence</li><li>Duplicate entity pages targeting same @id concept</li><li>No internal links from content to glossary</li></ul>"))
        + lesson(7, "Entity Audit Methodology", """
<p>Entity audits assess how search engines and AI systems understand your brand, people, products, and topics.</p>

<h4>Entity Audit Steps</h4>
<ol>
<li>Branded SERP audit: panel, sitelinks, accuracy</li>
<li>Schema audit: Organization, Person, Product validation</li>
<li>sameAs audit: all profiles live and consistent</li>
<li>Mention audit: brand name consistency in top 50 web results</li>
<li>AI citation audit: 10 queries in ChatGPT, Perplexity, Gemini</li>
<li>Competitor entity comparison: who owns panel? who gets cited?</li>
</ol>
""" + diagram("""
ENTITY AUDIT SCORECARD
────────────────────────────────────────
Organization schema valid     [ /10 ]
Person/author schema          [ /10 ]
sameAs completeness           [ /10 ]
NAP/brand consistency         [ /10 ]
Knowledge Panel accuracy      [ /10 ]
AI citation rate (10 queries) [ /10 ]
────────────────────────────────────────
""") + """
<h4>Tools</h4>
<p>Google Search (branded), Rich Results Test, Schema Validator, Wikidata search, Perplexity, GSC branded query report.</p>
""" + case_study("Entity Gap", """
<p>B2B brand had schema but zero AI citations. Added detailed About, founder interviews, and industry report PDFs. Cited in 4/10 AI queries within 4 months vs 0/10 before.</p>
""") + tip("<p>Entity audit makes excellent capstone bridge to Module 14 SEO agents monitoring brand mentions.</p>") + mistake("<ul><li>Audit once never again</li><li>Ignoring AI citation layer</li><li>Fixing schema only without off-site prominence</li></ul>"))
        + lesson(8, "Future-Proof Entity SEO Strategy", """
<p>Entity SEO integrates with GEO (Module 10): authoritative, well-structured entities get cited in AI answers; fragmented signals get ignored.</p>

<h4>Strategic Pillars</h4>
<ul>
<li><strong>Clarity:</strong> Unambiguous entity definitions on-site</li>
<li><strong>Consistency:</strong> NAP, brand, product data everywhere</li>
<li><strong>Connections:</strong> Schema sameAs, internal links, external mentions</li>
<li><strong>Corroboration:</strong> Third-party authoritative sources confirm facts</li>
<li><strong>Maintenance:</strong> Quarterly entity audits and updates</li>
</ul>
""" + diagram("""
ENTITY SEO → GEO PIPELINE
══════════════════════════════════════════════════════════════
Entity clarity (schema + content)
        → Knowledge systems trust
        → Traditional rankings + panels
        → AI citation in answers
        → Brand search growth flywheel
══════════════════════════════════════════════════════════════
""") + """
<h4>WordPress Example</h4>
<p>Build entity hub page /about/ with Organization schema, team Person entities, sameAs links, timeline, and downloadable fact sheet PDF for AI crawlers.</p>

<h4>Implementation Roadmap</h4>
<ol>
<li>Month 1: Organization + author schema + sameAs</li>
<li>Month 2: Product/Service schema complete</li>
<li>Month 3: Glossary/topical entity pages</li>
<li>Month 4: PR for corroborating mentions</li>
<li>Ongoing: AI citation tracking monthly</li>
</ol>
""" + case_study("Full Entity Program", """
<p>Regional bank implemented entity program across 12 branches. Knowledge Panels for branches, consistent Wikidata for parent org, FAQ schema on services. Branded search +28%; AI referrals measurable from analytics UTM experiments.</p>
""") + mistake("<ul><li>Treating entity SEO as one-time schema install</li><li>Neglecting human-readable About content</li><li>Fake corroboration via PBN mentions</li></ul>") + tip("<p>End module with workshop presentations—peer review catches entity gaps.</p>"))
    )

    workshop = """
<div class="workshop">
<strong>Workshop: Build an Entity Map for a Company</strong>
<h4>Duration:</h4> 2.5 hours
<h4>Materials:</h4> Company choice (student employer or case study), spreadsheet, Miro/FigJam, schema reference docs
<h4>Instructions:</h4>
<ol>
<li>Select company; identify primary entities: Organization, People (founders/key staff), Products/Services, Locations</li>
<li>Draw entity relationship diagram with labeled edges (founder, offers, locatedIn, sameAs)</li>
<li>Audit branded SERP and Knowledge Panel (if any); document inaccuracies</li>
<li>List all sameAs profiles; verify live URLs and NAP/brand match</li>
<li>Draft Organization + Person JSON-LD outline (properties, not full code required)</li>
<li>Run 5 branded and 5 category queries in Perplexity; log citation yes/no</li>
<li>Identify 3 entity gaps vs top competitor</li>
<li>Propose 5 content/schema actions to strengthen entity clarity</li>
<li>Present entity map and 90-day roadmap in 5 minutes</li>
</ol>
<h4>Deliverable:</h4> Visual entity map + audit scorecard + schema outline + AI citation report + 90-day roadmap
</div>
"""

    notes = """
<ul>
<li>Entity SEO is abstract—use concrete brand students know (Apple, local restaurant)</li>
<li>Clarify Wikipedia notability rules to prevent spam attempts</li>
<li>Demo schema.org Organization page and Rank Math implementation</li>
<li>Connect to Module 6 topical authority and Module 7 local entities</li>
<li>Preview Module 10 GEO—entity clarity enables AI citations</li>
</ul>
"""

    exercises = """<ol>
<li>Classify 10 terms as keyword vs entity with disambiguation notes.</li>
<li>Draw entity graph for a coffee shop with 2 locations and 3 products.</li>
<li>Audit Organization schema on a provided homepage HTML sample.</li>
<li>Run AI citation test for one brand; document results in table.</li>
</ol>"""

    homework = """<p>Complete entity audit for your workshop company. Implement Organization schema improvements on WordPress site if available. Write 750-word report on entity gaps and competitor comparison.</p>"""

    quiz = """<ol>
<li>What is an entity in search?</li>
<li>How does an entity differ from a keyword?</li>
<li>What is the Knowledge Graph?</li>
<li>What does schema sameAs property do?</li>
<li>Name two ways to improve semantic search coverage.</li>
<li>What schema type links authors to organizations?</li>
<li>Why are consistent brand names important for entities?</li>
<li>What is an entity audit?</li>
<li>How does entity SEO relate to AI search citations?</li>
<li>Name three entity types for a typical company.</li>
</ol>
<p><strong>Answer Key:</strong> 1) Uniquely identifiable thing (person, place, org, product, concept) 2) Entity is real-world thing; keyword is search string 3) Database of entities and relationships Google uses 4) Links entity to official profiles confirming identity 5) Related concepts, FAQ structure, natural synonyms (any two) 6) worksFor on Person or author/publisher on Article 7) Consistent signals prevent entity fragmentation 8) Systematic review of how search/AI understand your entities 9) Clear entities get cited as authoritative sources in AI answers 10) Organization, Person, Product/Service (any three valid)</p>"""

    outcomes = """<ul>
<li>Explain entities vs keywords and semantic search</li>
<li>Understand Knowledge Graphs and Knowledge Panels</li>
<li>Implement schema expressing entity relationships</li>
<li>Optimize brand and product entities in WordPress</li>
<li>Connect topical content to entity graphs</li>
<li>Deliver entity map and audit for a real company</li>
</ul>"""

    return module_html(
        8, "Entity SEO",
        [
            "Define entities and their role in modern search",
            "Understand Knowledge Graphs and Knowledge Panels",
            "Optimize for semantic search and NLP",
            "Express entity relationships with structured data",
            "Build brand and product entity presence",
            "Execute entity audits and strategic roadmaps",
        ],
        [
            "Entities in Modern Search",
            "Knowledge Graphs and Knowledge Panels",
            "Semantic Search and Natural Language",
            "Structured Relationships with Schema",
            "Entity SEO for Brands and Products",
            "Topical Entities and Content Hubs",
            "Entity Audit Methodology",
            "Future-Proof Entity SEO Strategy",
        ],
        lessons, workshop, notes, exercises, homework, quiz, outcomes,
    )


def get_modules_2_8():
    """Return HTML strings for course modules 2 through 8."""
    return [
        _module_2(),
        _module_3(),
        _module_4(),
        _module_5(),
        _module_6(),
        _module_7(),
        _module_8(),
    ]


if __name__ == "__main__":
    modules = get_modules_2_8()
    for i, mod in enumerate(modules, start=2):
        print(f"Module {i}: {len(mod):,} chars")
    print(f"Total: {sum(len(m) for m in modules):,} chars")
