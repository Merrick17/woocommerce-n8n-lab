#!/usr/bin/env python3
"""Module 1 HTML content: The Evolution of Search."""
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


def get_module_1():
    lessons = (
        lesson(1, "A Brief History of Search Engines", """
<p>Before Google dominated the web, search was a chaotic landscape of directories, portals, and early crawlers. Understanding this history helps you see why modern SEO, AEO, and GEO exist—and why they keep changing.</p>
<h4>The Early Web (1990–1998)</h4>
<p>In 1994, Yahoo! began as a human-edited directory. Webmasters submitted sites manually. AltaVista (1995) and Excite pioneered full-text search. Google's breakthrough in 1998 was PageRank: treating links as votes of trust.</p>
""" + diagram("""
TIMELINE OF SEARCH
──────────────────────────────────────────────────────────────
1990  Archie (FTP search)
1994  Yahoo Directory (human-curated)
1995  AltaVista (full-text crawl)
1998  Google (PageRank algorithm)
2000  Google AdWords launches
2004  Local search + Google Suggest
2007  Universal Search (images, news, video)
2011  Panda update (content quality)
2012  Knowledge Graph launch
2015  RankBrain (machine learning)
2019  BERT (natural language understanding)
2023  Search Generative Experience (SGE)
2024  AI Overviews rollout
2025  AI-native search (ChatGPT, Perplexity, Gemini)
──────────────────────────────────────────────────────────────
""") + case_study("Dmoz to Google", """
<p>The Open Directory Project (Dmoz) was once the gold standard for categorization. When Google automated discovery via crawling, the SEO industry was born overnight. Sites that understood linking and relevance gained traffic; those that didn't vanished from results.</p>
<p><strong>Lesson:</strong> Every major search shift creates winners and losers. Today's shift—from ten blue links to AI-generated answers—is equally transformative.</p>
""") + tip("<p>When teaching history, connect each era to a modern tactic. PageRank → link building. Knowledge Graph → entity SEO. SGE → GEO.</p>") + mistake("<ul><li>Teaching SEO as static rules frozen in 2010</li><li>Ignoring that AI search is a new channel, not a replacement for all search</li></ul>"))
        + lesson(2, "How Google Works Today", """
<p>Google is a three-stage system: <strong>Crawl → Index → Rank</strong>. Every SEO decision maps to one of these stages.</p>
<h4>Crawling</h4>
<p>Googlebot discovers URLs via links, sitemaps, and submitted URLs. It fetches HTML, follows redirects, and respects robots.txt. Crawl budget limits how often Google visits your site—critical for large sites.</p>
<h4>Indexing</h4>
<p>Google parses content, extracts entities, stores a searchable copy, and decides whether a page is canonical. Noindex pages are crawled but not shown in results.</p>
<h4>Ranking</h4>
<p>For each query, Google retrieves candidate pages and scores them using hundreds of signals: relevance, quality, freshness, E-E-A-T, page experience, and now AI Overview eligibility.</p>
""" + diagram("""
HOW GOOGLE PROCESSES A QUERY
══════════════════════════════════════════════════════════════
  User types: "best wordpress seo plugin 2026"
         │
         ▼
  ┌──────────────┐
  │ Query        │  → Intent: Commercial Investigation
  │ Understanding│  → Entities: WordPress, SEO, Plugin
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │ Index        │  → Retrieve 1000+ candidate pages
  │ Retrieval    │
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐
  │ Ranking      │  → Score by relevance, authority, UX
  │ Algorithm    │
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐     ┌─────────────────┐
  │ SERP Layout  │────▶│ AI Overview     │ (if triggered)
  │              │     │ Organic Results │
  └──────────────┘     │ People Also Ask │
                       │ Local Pack      │
                       └─────────────────┘
══════════════════════════════════════════════════════════════
""") + """
<h4>WordPress Example</h4>
<p>A WooCommerce store publishing 500 product pages without a sitemap may have 40% of products uncrawled after 90 days. Adding Rank Math sitemap + internal links from category pages typically increases indexed pages within 2–4 weeks.</p>
<h4>AI Search Example</h4>
<p>When users ask ChatGPT "how does Google indexing work," it synthesizes from high-authority sources (Google Search Central, Moz, Search Engine Journal). Sites with clear, structured explanations of technical concepts become training and retrieval sources.</p>
""" + mistake("<ul><li>Assuming publishing = indexing</li><li>Blocking CSS/JS in robots.txt (prevents rendering)</li></ul>"))
        + lesson(3, "Crawling Deep Dive", """
<p>Crawling is the foundation. If Googlebot cannot reach a page, nothing else matters.</p>
<h4>Implementation Steps</h4>
<ol>
<li>Verify robots.txt at <code>yoursite.com/robots.txt</code></li>
<li>Submit XML sitemap in Google Search Console</li>
<li>Check Coverage report for "Discovered – currently not indexed"</li>
<li>Fix orphan pages with internal links</li>
<li>Monitor server response times (slow servers reduce crawl rate)</li>
</ol>
<h4>WordPress Configuration</h4>
<pre class="diagram"># Recommended robots.txt additions for WordPress
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Sitemap: https://yoursite.com/sitemap_index.xml</pre>
<h4>Best Practices</h4>
<ul>
<li>Keep important pages within 3 clicks of homepage</li>
<li>Use consistent internal linking from high-authority pages</li>
<li>Fix 404 chains and redirect loops promptly</li>
<li>Monitor crawl stats in Google Search Console weekly</li>
</ul>
""" + tip("<p>Use Screaming Frog or Sitebulb on WordPress sites monthly. Export crawl data to track indexation trends.</p>"))
        + lesson(4, "Indexing Explained", """
<p>Indexing is Google's decision to store and potentially rank a page. Common reasons pages fail to index:</p>
<ul>
<li>Duplicate or thin content</li>
<li>noindex meta tag or HTTP header</li>
<li>Canonical pointing elsewhere</li>
<li>Low quality or spam signals</li>
<li>Crawl budget exhaustion on large sites</li>
</ul>
<h4>Real-World Example</h4>
<p>A digital agency client had 847 blog posts but only 312 indexed. Root cause: tag pages created duplicate URLs, and pagination lacked canonical tags. After consolidating tags and adding rel=canonical, indexed pages rose to 801 within 6 weeks.</p>
""" + diagram("""
INDEX STATUS DECISION TREE
──────────────────────────
Page crawled?
  NO  → Fix links, sitemap, robots.txt
  YES → Has noindex?
          YES → Remove if you want indexing
          NO  → Duplicate content?
                  YES → Set canonical or merge
                  NO  → Quality sufficient?
                          YES → Likely indexed ✓
                          NO  → Improve content
""") + case_study("WooCommerce Indexation", """
<p>An online retailer with 2,400 SKU variations saw only 900 indexed. Faceted navigation created millions of parameter URLs. Solution: canonical tags on filtered views, noindex on sort parameters, and a streamlined XML product sitemap. Indexed products reached 2,100 within 8 weeks.</p>
"""))
        + lesson(5, "Ranking Signals Overview", """
<p>Ranking combines relevance and authority. Key signal categories:</p>
<table>
<tr><th>Category</th><th>Examples</th><th>WordPress Action</th></tr>
<tr><td>On-page</td><td>Title, headings, content depth</td><td>Optimize with Rank Math/Yoast</td></tr>
<tr><td>Technical</td><td>Speed, mobile, HTTPS</td><td>LiteSpeed Cache, CDN</td></tr>
<tr><td>Off-page</td><td>Backlinks, brand mentions</td><td>Digital PR, guest posts</td></tr>
<tr><td>Behavioral</td><td>CTR, dwell time</td><td>Compelling titles, UX</td></tr>
<tr><td>Entity</td><td>Knowledge Graph connections</td><td>Schema, consistent NAP</td></tr>
</table>
""" + case_study("Featured Snippet Win", """
<p>A recipe blog optimized a chicken tikka masala post with a 40-word definition paragraph, numbered steps, and FAQ schema. Within 3 weeks it captured the featured snippet for "how to make chicken tikka masala," increasing organic traffic 340% for that URL.</p>
""") + tip("<p>Prioritize ranking signals by business stage: new sites need technical + on-page; established sites need authority + entities.</p>"))
        + lesson(6, "Knowledge Graphs and Entities", """
<p>Google's Knowledge Graph stores facts about entities—people, places, organizations, concepts—and their relationships. When you search "Apple," Google knows you might mean the company or the fruit based on context.</p>
<h4>Why Entities Matter for SEO</h4>
<p>Modern search doesn't just match keywords—it resolves entities. Your brand is an entity. Your products are entities. Connecting them with structured data and consistent mentions across the web strengthens your visibility in both traditional and AI search.</p>
""" + diagram("""
ENTITY RELATIONSHIP EXAMPLE: Local Bakery
────────────────────────────────────────────
[Artisan Bake Co.] ──type──▶ LocalBusiness
        │
        ├── locatedIn ──▶ [Austin, Texas]
        ├── serves ──▶ [Sourdough Bread, Croissants]
        ├── founder ──▶ [Maria Santos]
        └── sameAs ──▶ [Google Business, Yelp, Facebook]
""") + """
<h4>Implementation Steps</h4>
<ol>
<li>Define your primary entities (brand, products, people, locations)</li>
<li>Add Organization schema on homepage</li>
<li>Use sameAs links to official profiles</li>
<li>Maintain consistent naming across all platforms</li>
<li>Build content that establishes entity relationships</li>
</ol>
""")
        + lesson(7, "The Rise of AI Search Engines", """
<p>AI search engines—ChatGPT, Perplexity, Gemini, Claude—retrieve and synthesize information differently from Google. They favor:</p>
<ul>
<li>Clear, authoritative source text</li>
<li>Well-structured factual content</li>
<li>Cited, verifiable claims</li>
<li>Entities with strong web presence</li>
<li>Recent, maintained content</li>
</ul>
<h4>AI Search Example</h4>
<p>Query Perplexity: "What is the best WordPress SEO plugin?" Notice which domains are cited. Typically: official plugin pages, major review sites (WPBeginner, Search Engine Journal), and comparison articles with structured pros/cons. Thin affiliate pages rarely appear.</p>
<h4>Retrieval vs Ranking</h4>
<p>Traditional SEO optimizes for ranking position. GEO optimizes for being <em>retrieved and cited</em> by AI systems. A page ranked #8 on Google may be the primary citation in ChatGPT if its content is clearer and more quotable.</p>
""" + tip("<p>Track your brand citations in AI tools monthly. Create a spreadsheet: Query | Tool | Cited? | Citing URL | Competitor Cited Instead</p>") + mistake("<ul><li>Optimizing only for Google while ignoring AI citation channels</li><li>Blocking AI crawlers without understanding impact (GPTBot, ClaudeBot policies vary)</li></ul>"))
        + lesson(8, "The Future of Search", """
<p>Search is fragmenting into:</p>
<ol>
<li><strong>Traditional SERPs</strong> — still dominant for transactional queries</li>
<li><strong>AI Overviews</strong> — Google's synthesized answers</li>
<li><strong>Conversational AI</strong> — ChatGPT, Claude, Gemini as research tools</li>
<li><strong>Answer engines</strong> — Perplexity, You.com with citations</li>
<li><strong>Vertical search</strong> — TikTok, YouTube, Amazon for specific intents</li>
</ol>
<h4>Strategic Implication</h4>
<p>Build an <strong>SEO Operating System</strong>: one WordPress hub, entity-optimized content, technical excellence, automation via n8n, and AI agents for monitoring and production. This course teaches you to build exactly that.</p>
<h4>Off-Page SEO Preview</h4>
<p>While this module focuses on how search works, remember that authority still matters. Links, brand mentions, and digital PR feed both Google's algorithms and AI training/retrieval corpora.</p>
""" + diagram("""
THE MODERN SEARCH ECOSYSTEM (2026)
═══════════════════════════════════════════════════
                    ┌─────────────┐
                    │   USER      │
                    └──────┬──────┘
           ┌───────────────┼───────────────┐
           ▼               ▼               ▼
    ┌────────────┐  ┌────────────┐  ┌────────────┐
    │ Google     │  │ AI Chat    │  │ Vertical   │
    │ (SERP+AIO) │  │ (GEO)      │  │ (YT/TikTok)│
    └─────┬──────┘  └─────┬──────┘  └─────┬──────┘
          │               │               │
          └───────────────┼───────────────┘
                          ▼
                 ┌─────────────────┐
                 │ YOUR WORDPRESS  │
                 │ SEO OPERATING   │
                 │ SYSTEM          │
                 └─────────────────┘
═══════════════════════════════════════════════════
""") + mistake("<ul><li>Betting everything on one channel</li><li>Neglecting fundamentals while chasing AI trends</li><li>Using AI to mass-produce low-quality pages</li></ul>"))
    )

    workshop = """
<div class="workshop">
<strong>Workshop: Analyze How Google, ChatGPT, Gemini, and Perplexity Answer the Same Query</strong>
<h4>Duration:</h4> 90 minutes
<h4>Materials:</h4> Laptop, spreadsheet, incognito browser sessions
<h4>Instructions:</h4>
<ol>
<li>Choose 5 queries across intent types:
  <ul>
  <li>Informational: "what is technical SEO"</li>
  <li>Commercial: "best wordpress hosting for seo"</li>
  <li>Local: "plumber near downtown seattle"</li>
  <li>Transactional: "buy organic dog food online"</li>
  <li>Comparison: "yoast vs rank math"</li>
  </ul>
</li>
<li>Run each query on Google (note AI Overview presence), ChatGPT (browse mode), Gemini, and Perplexity</li>
<li>Record for each: answer format, sources cited, brand mentions, content types preferred</li>
<li>Identify patterns: who gets cited, who doesn't, why</li>
<li>Present findings in 5-minute group discussion</li>
</ol>
<h4>Deliverable:</h4> Comparison spreadsheet + 1-page analysis of citation patterns
</div>"""

    notes = """<ul>
<li>Emphasize that AI tools hallucinate—teach students to verify claims</li>
<li>Use VPN-free, logged-out sessions for consistency</li>
<li>Discuss how GEO differs from traditional SEO in citation vs ranking</li>
<li>Common student insight: Wikipedia and major publishers dominate entity queries</li>
<li>Allocate 30 min research, 30 min analysis, 30 min presentation</li>
</ul>"""

    exercises = """<ol>
<li>Draw the Crawl-Index-Rank pipeline from memory and label where robots.txt, sitemap, and canonical tags act.</li>
<li>Find one page on any website that is likely not indexed and explain why.</li>
<li>List three differences between Google SERPs and Perplexity results for the same query.</li>
<li>Identify three entities related to your chosen capstone business.</li>
</ol>"""

    homework = """<p>Write a 500-word essay: <em>How has search changed in the last 5 years, and what should a WordPress site owner do today?</em> Include at least two ASCII diagrams and reference one case study from class.</p>"""

    quiz = """<ol>
<li>What three stages does Google use to process web pages?</li>
<li>What was Google's key innovation in 1998?</li>
<li>What is crawl budget and why does it matter?</li>
<li>Name three reasons a page might not be indexed.</li>
<li>What is the Knowledge Graph?</li>
<li>How does an entity differ from a keyword?</li>
<li>Name two AI search engines and one difference from Google.</li>
<li>What is an AI Overview?</li>
<li>What file tells crawlers which URLs to avoid?</li>
<li>Why should you not block CSS in robots.txt?</li>
</ol>
<p><strong>Answer Key:</strong> 1) Crawl, Index, Rank 2) PageRank 3) Limited resources Google allocates to crawling your site 4) noindex, duplicates, thin content (any three) 5) Database of entities and relationships 6) Entity is a real-world thing with attributes; keyword is a search string 7) ChatGPT, Perplexity (examples); AI synthesizes vs lists links 8) Google's AI-generated answer box 9) robots.txt 10) Google needs CSS to render pages properly</p>"""

    outcomes = """<ul>
<li>Explain search engine history and its impact on modern SEO</li>
<li>Describe Crawl-Index-Rank with WordPress examples</li>
<li>Identify indexing blockers and fixes</li>
<li>Understand entities and Knowledge Graphs</li>
<li>Compare traditional and AI search behavior</li>
<li>Complete a multi-engine query analysis workshop</li>
</ul>"""

    objectives = [
        "Understand search engine history and evolution",
        "Explain how Google crawls, indexes, and ranks",
        "Describe Knowledge Graphs and entities",
        "Compare traditional vs AI search engines",
        "Analyze the future of search and its SEO implications",
    ]
    lesson_titles = [
        "A Brief History of Search Engines",
        "How Google Works Today",
        "Crawling Deep Dive",
        "Indexing Explained",
        "Ranking Signals Overview",
        "Knowledge Graphs and Entities",
        "The Rise of AI Search Engines",
        "The Future of Search",
    ]

    obj_li = "".join(f"<li>{esc(o)}</li>" for o in objectives)
    list_li = "".join(f"<li>{esc(l)}</li>" for l in lesson_titles)

    return f'''
<section class="module" id="module1">
<h1>Module 1: The Evolution of Search</h1>
<div class="objectives"><strong>Learning Objectives</strong><ul>{obj_li}</ul></div>
<h2>Lesson List</h2>
<ol>{list_li}</ol>
<h2>Detailed Lesson Content</h2>
{lessons}
{workshop}
<div class="notes"><strong>Instructor Notes</strong>{notes}</div>
<div class="exercise"><strong>Student Exercises</strong>{exercises}</div>
<div class="homework"><strong>Homework</strong>{homework}</div>
<div class="quiz"><strong>Quiz Questions</strong>{quiz}</div>
<div class="outcomes"><strong>Expected Outcomes</strong>{outcomes}</div>
</section>
'''
