#!/usr/bin/env python3
"""Course modules 9–15: AEO, GEO, AI Content, Programmatic SEO, n8n, Agents, Capstone."""

import html as html_lib


def esc(s):
    return html_lib.escape(str(s))


def diagram(text):
    return f'<pre class="diagram">{esc(text)}</pre>'


def box(cls, title, content):
    return f'<div class="{cls}"><strong>{esc(title)}</strong>{content}</div>'


def lesson(num, title, body):
    return f'<h3>Lesson {num}: {esc(title)}</h3>\n{body}\n'


def case_study(title, content):
    return f'<div class="case-study"><strong>Case Study: {esc(title)}</strong>{content}</div>'


def mistake(content):
    return f'<div class="mistake"><strong>Mistakes to Avoid:</strong>{content}</div>'


def tip(content):
    return f'<div class="tip"><strong>Expert Tip:</strong>{content}</div>'


def module_header(mid, title, objectives, lesson_titles, lessons_content, workshop_html, exercises, homework, quiz, outcomes):
    return f'''
<section class="module" id="module{mid}">
<h1>Module {mid}: {esc(title)}</h1>
<div class="objectives"><strong>Learning Objectives</strong><ul>{"".join(f"<li>{esc(o)}</li>" for o in objectives)}</ul></div>
<h2>Lesson List</h2>
<ol>{"".join(f"<li>{esc(l)}</li>" for l in lesson_titles)}</ol>
<h2>Detailed Lesson Content</h2>
{lessons_content}
{workshop_html}
<div class="exercise"><strong>Student Exercises</strong>{exercises}</div>
<div class="homework"><strong>Homework</strong>{homework}</div>
<div class="quiz"><strong>Quiz Questions</strong>{quiz}</div>
<div class="outcomes"><strong>Expected Outcomes</strong>{outcomes}</div>
</section>
'''


def _module_9():
    titles = [
        "Introduction to Answer Engine Optimization (AEO)",
        "Featured Snippets: Types, Triggers, and Capture",
        "Voice Search Optimization",
        "FAQ Optimization and Structured Data",
        "Conversational Search and Query Patterns",
        "Google AI Overviews: Eligibility and Optimization",
        "Answer-First Content Architecture",
        "Measuring and Iterating AEO Performance",
    ]
    lessons = (
        lesson(1, titles[0], """
<p>Answer Engine Optimization (AEO) is the practice of structuring content so search engines—and increasingly AI systems—can extract direct answers for users. Where traditional SEO optimizes for clicks on blue links, AEO optimizes for <strong>position zero</strong>, voice responses, People Also Ask expansions, and AI Overview citations.</p>
<p>AEO sits between classic SEO and GEO. You still need crawlable, authoritative pages, but you also need atomic answer blocks: concise definitions, scannable lists, comparison tables, and FAQ pairs that machines can quote without ambiguity.</p>
""" + diagram("""
AEO TARGET SURFACES
══════════════════════════════════════════════════════════
  Featured Snippet (paragraph / list / table)
  People Also Ask (PAA) accordion
  Voice Search (Google Assistant, Siri, Alexa)
  Knowledge Panel facts
  Google AI Overviews
  Rich Results (FAQ, HowTo, QAPage)
══════════════════════════════════════════════════════════
""") + case_study("Health Publisher PAA Domination", """
<p>A medical publisher restructured 120 condition pages with a 50-word answer paragraph immediately after each H1, followed by H2 questions mirroring PAA phrasing. FAQ schema was added only where answers matched visible text. PAA appearances rose 4.2× in 90 days; featured snippet capture rate went from 3% to 19% on target queries.</p>
""") + tip("<p>Teach students to search their target query in incognito, expand every PAA box, and paste questions into a content brief before writing.</p>"))
        + lesson(2, titles[1], """
<p>Featured snippets are extracted answers displayed above organic results. Google selects them when a page clearly satisfies intent with a self-contained block.</p>
<h4>Snippet Types</h4>
<ul>
<li><strong>Paragraph</strong> — 40–60 words defining or explaining (ideal for "what is" queries)</li>
<li><strong>List</strong> — ordered steps or unordered items (ideal for "how to" and "best" queries)</li>
<li><strong>Table</strong> — comparisons, specs, pricing (ideal for "vs" and "cost" queries)</li>
<li><strong>Video</strong> — timestamped YouTube clips (ideal for visual tasks)</li>
</ul>
<h4>Capture Workflow</h4>
<ol>
<li>Identify snippet currently ranking (or PAA question with no strong snippet)</li>
<li>Match format: list beats paragraph for step queries</li>
<li>Place answer block directly under question-matching H2</li>
<li>Use clean HTML: <code>&lt;ol&gt;</code>, <code>&lt;table&gt;</code>, no hidden text</li>
<li>Strengthen page authority with internal links and E-E-A-T signals</li>
</ol>
""" + diagram("""
SNIPPET FORMAT SELECTION
────────────────────────────────────────
Query intent          Best format
────────────────────────────────────────
"what is X"           Paragraph (≤60 words)
"how to X"            Numbered list
"best X for Y"        Bulleted list + intro
"X vs Y"              Table + summary paragraph
"X cost"              Table or paragraph with numbers
────────────────────────────────────────
""") + mistake("<ul><li>Writing 300-word intros before the answer</li><li>Using schema markup that doesn't match visible content</li><li>Keyword-stuffing the snippet block</li></ul>"))
        + lesson(3, titles[2], """
<p>Voice search queries are longer, conversational, and heavily local. Devices read a single answer—usually the featured snippet or knowledge panel—so winning snippet equals winning voice.</p>
<h4>Voice Query Characteristics</h4>
<ul>
<li>Question form: who, what, where, when, why, how</li>
<li>Natural language: "What's the best WordPress SEO plugin for beginners?"</li>
<li>Local modifiers: "near me," city names, "open now"</li>
<li>Mobile and smart-speaker context</li>
</ul>
<h4>WordPress Optimization Checklist</h4>
<ol>
<li>Build FAQ sections with spoken-friendly phrasing</li>
<li>Target long-tail question keywords in H2s</li>
<li>Ensure page speed &lt; 2.5s LCP on mobile</li>
<li>Claim and optimize Google Business Profile for local voice</li>
<li>Use Speakable schema sparingly on truly speakable summaries</li>
</ol>
""" + tip("<p>Read answers aloud in class. If it sounds robotic or exceeds 30 seconds, rewrite for conversational clarity.</p>"))
        + lesson(4, titles[3], """
<p>FAQ sections serve dual purposes: user experience and machine extraction. When paired with valid FAQPage schema, they can earn rich results—but only if content is visible and accurate.</p>
<h4>FAQ Content Rules</h4>
<ul>
<li>Each question must be a genuine user question (from GSC, Also Asked, sales calls)</li>
<li>Answers should be 2–5 sentences; link to deeper content when needed</li>
<li>Avoid duplicate FAQs across pages (canonical confusion)</li>
<li>Update FAQs when products, laws, or pricing change</li>
</ul>
<h4>Schema Implementation on WordPress</h4>
<p>Rank Math and Yoast generate FAQ blocks. Manual JSON-LD is acceptable when plugins cannot represent complex pages. Always validate in Google Rich Results Test.</p>
<pre class="diagram">FAQPage schema checklist:
□ Questions match visible H3/H4 text exactly
□ Answers appear in page HTML (not JS-only)
□ No FAQ spam on irrelevant pages
□ Combined with Article or Product schema where appropriate</pre>
""" + case_study("SaaS Pricing FAQ Rich Results", """
<p>A B2B SaaS site added 8 pricing FAQs to its plans page with matching FAQPage schema. Rich results appeared within 11 days for branded pricing queries; support tickets about billing dropped 22% because answers were surfaced in search.</p>
"""))
        + lesson(5, titles[4], """
<p>Conversational search reflects how people talk to assistants and AI chat interfaces. Users submit follow-ups, refine intent, and expect contextual answers. Your content must support <strong>topic depth</strong> and <strong>entity clarity</strong> so each page can serve multiple related questions.</p>
<h4>Content Cluster Pattern for Conversational Intent</h4>
""" + diagram("""
PILLAR + SPOKE CONVERSATIONAL MODEL
─────────────────────────────────────
Pillar: "WordPress SEO Guide" (broad)
  ├── Spoke: "How to set up Rank Math"
  ├── Spoke: "WordPress sitemap not indexing"
  ├── Spoke: "Canonical tags in WooCommerce"
  └── Spoke: "SEO for multilingual WordPress"
Each spoke answers one conversational thread; pillar links all.
─────────────────────────────────────
""") + """
<p>Use "People Also Ask" and Search Console queries to map follow-up questions. Each follow-up becomes an H2 or a child page in the cluster.</p>
""" + mistake("<ul><li>One giant FAQ page instead of clustered answers</li><li>Ignoring zero-click searches that still build brand authority</li></ul>"))
        + lesson(6, titles[5], """
<p>Google AI Overviews (formerly SGE) synthesize answers from multiple sources. Pages earn visibility when they provide citable, factual, well-structured excerpts—not when they game keywords.</p>
<h4>AI Overview Optimization Principles</h4>
<ol>
<li><strong>Lead with facts</strong> — verifiable statements with dates and sources</li>
<li><strong>Structure for extraction</strong> — headings that mirror questions; tables for comparisons</li>
<li><strong>Demonstrate E-E-A-T</strong> — author bios, citations, updated timestamps</li>
<li><strong>Avoid fluff</strong> — AI systems prefer dense information gain</li>
<li><strong>Technical access</strong> — allow Googlebot; no paywalls on key facts</li>
</ol>
<p>AI Overviews often pull from pages already ranking top 10. Strong traditional SEO remains the foundation; AEO layers extractable answer blocks on top.</p>
""" + tip("<p>Track AI Overview triggers in Semrush or manual SERP checks weekly for your top 20 keywords. Note which competitors get cited.</p>"))
        + lesson(7, titles[6], """
<p>Answer-first architecture inverts the classic blog template. Instead of story → context → answer, you publish <strong>answer → support → depth</strong>.</p>
<h4>Template Structure</h4>
<pre class="diagram">H1: [Exact question or topic]
P:  Direct answer (40–60 words) — snippet-ready
H2: Key details / steps / comparison
H2: Supporting evidence, examples, data
H2: Related questions (FAQ)
H2: Conclusion + next steps</pre>
<h4>When to Use Answer-First</h4>
<ul>
<li>Informational and educational content</li>
<li>Support documentation and knowledge bases</li>
<li>Product comparison and buyer guides</li>
<li>Any page targeting PAA or snippet positions</li>
</ul>
<p>Long-form narrative still works for thought leadership—but place a summary box at the top with the direct answer.</p>
""" + case_study("Recipe Site Snippet Recovery", """
<p>A recipe site moved the 45-word recipe summary above a 800-word personal story. Snippet loss recovered in 2 weeks; total time-on-page increased because users who wanted the story still scrolled.</p>
"""))
        + lesson(8, titles[7], """
<p>AEO measurement combines SERP feature tracking, GSC performance, and qualitative citation checks.</p>
<h4>Metrics Dashboard</h4>
<table>
<tr><th>Metric</th><th>Tool</th><th>Frequency</th></tr>
<tr><td>Featured snippet count</td><td>Semrush, Ahrefs</td><td>Weekly</td></tr>
<tr><td>PAA appearances</td><td>Also Asked, GSC</td><td>Monthly</td></tr>
<tr><td>Rich result impressions</td><td>GSC Enhancements</td><td>Weekly</td></tr>
<tr><td>AI Overview citations</td><td>Manual + Otterly.AI</td><td>Biweekly</td></tr>
<tr><td>Voice query share</td><td>GSC query length analysis</td><td>Monthly</td></tr>
</table>
<h4>Iteration Loop</h4>
<ol>
<li>Identify target query and current SERP feature holder</li>
<li>Compare format and information gain</li>
<li>Rewrite answer block; A/B test title and H2 phrasing</li>
<li>Republish with updated date; request indexing in GSC</li>
<li>Review results in 14–21 days</li>
</ol>
""" + tip("<p>Build a shared AEO scorecard in Google Sheets: URL, target query, snippet type, status, last optimized date.</p>"))
    )
    workshop = """
<div class="workshop">
<strong>Workshop: Transform an Article to Answer-First Format</strong>
<h4>Duration:</h4> 120 minutes
<h4>Materials:</h4> One existing 1,000+ word blog post (student's or provided), Google Doc, Rich Results Test access
<h4>Instructions:</h4>
<ol>
<li>Select an informational article currently ranking positions 4–15 for a question-based query</li>
<li>Search the query; screenshot current snippet, PAA, and AI Overview (if present)</li>
<li>Write a 50-word direct answer paragraph; place immediately under H1</li>
<li>Restructure H2s as questions pulled from PAA and Also Asked</li>
<li>Add one list or table matching dominant snippet format</li>
<li>Create 5 FAQ pairs; implement FAQPage schema on WordPress staging</li>
<li>Validate schema; peer review for accuracy and E-E-A-T</li>
<li>Present before/after outline in 3-minute lightning talks</li>
</ol>
<h4>Deliverable:</h4> Revised article outline + implemented staging URL + snippet target spreadsheet row
</div>
<div class="notes"><strong>Instructor Notes</strong>
<ul>
<li>Provide a "before" article with intentionally buried answers for dramatic contrast</li>
<li>Emphasize that moving content is not duplicate content if URL stays the same</li>
<li>Common mistake: schema questions that don't match visible headings—catch in review</li>
<li>Extension: students rewrite the same page for voice (read-aloud test)</li>
<li>Discuss zero-click SERPs: brand visibility still has value even without clicks</li>
</ul></div>
"""
    exercises = """<ol>
<li>Find three featured snippet types in your niche and screenshot each format.</li>
<li>Rewrite one paragraph into a 45-word snippet-ready answer.</li>
<li>Build a 10-question FAQ from GSC queries for one URL.</li>
<li>Map PAA questions for "how to [your topic]" and assign each to an H2 or new page.</li>
</ol>"""
    homework = """<p>Complete a full AEO audit on one WordPress URL: document current SERP features, rewrite in answer-first format, add FAQ schema, and write a 400-word reflection on expected impact with metrics you'll track for 30 days.</p>"""
    quiz = """<ol>
<li>What is AEO and how does it differ from traditional SEO?</li>
<li>Name four featured snippet formats.</li>
<li>What is the ideal length for a paragraph snippet?</li>
<li>Why does voice search heavily depend on featured snippets?</li>
<li>What are three FAQ schema requirements?</li>
<li>What is answer-first content architecture?</li>
<li>Name three signals that help AI Overview eligibility.</li>
<li>What tool validates FAQ rich results?</li>
<li>How do conversational queries differ from head terms?</li>
<li>What is a reasonable snippet capture iteration cycle?</li>
</ol>
<p><strong>Answer Key:</strong> 1) Optimizing for direct answers in SERP features, not just rankings 2) Paragraph, list, table, video 3) ~40–60 words 4) Assistants read one extracted answer, usually the snippet 5) Visible matching Q&A, accurate content, no spam (any three) 6) Direct answer before supporting content 7) E-E-A-T, structure, factual density (any three) 8) Google Rich Results Test 9) Longer, question-form, natural language 10) 14–21 days</p>"""
    outcomes = """<ul>
<li>Define AEO and its relationship to SEO and GEO</li>
<li>Capture and optimize for featured snippets by format type</li>
<li>Optimize content for voice and conversational search</li>
<li>Implement FAQ content and valid schema on WordPress</li>
<li>Apply answer-first architecture to existing articles</li>
<li>Measure AEO performance and run iteration cycles</li>
<li>Complete an answer-first transformation workshop</li>
</ul>"""
    return module_header(
        9, "Answer Engine Optimization (AEO)",
        [
            "Define AEO and its target SERP surfaces",
            "Capture featured snippets using format-matched blocks",
            "Optimize for voice search and conversational queries",
            "Implement FAQ optimization and structured data",
            "Optimize content for Google AI Overviews",
            "Apply answer-first content architecture",
            "Measure and iterate AEO campaigns",
        ],
        titles, lessons, workshop, exercises, homework, quiz, outcomes,
    )


def _module_10():
    titles = [
        "Introduction to Generative Engine Optimization (GEO)",
        "How ChatGPT Retrieves and Cites Sources",
        "Perplexity and Citation-First Search",
        "Gemini, Google AI Mode, and Cross-Platform Visibility",
        "Claude and Authoritative Source Patterns",
        "Citation Optimization Strategies",
        "AI Retrieval Patterns and RAG Fundamentals",
        "GEO Measurement, Monitoring, and Competitive Analysis",
    ]
    lessons = (
        lesson(1, titles[0], """
<p>Generative Engine Optimization (GEO) is the discipline of earning citations and mentions in AI-generated answers from ChatGPT, Perplexity, Gemini, Claude, and similar systems. Unlike ranking in a list of ten links, GEO targets <strong>inclusion inside the synthesized response</strong>—often with a footnote or source link.</p>
<p>GEO complements SEO and AEO: crawlable, authoritative pages feed retrieval systems. GEO adds brand entity strength, citation-worthy prose, original data, and distribution across platforms AI models trust.</p>
""" + diagram("""
SEO vs AEO vs GEO
═══════════════════════════════════════════════════════
SEO   → Rank in organic results (click to site)
AEO   → Win snippet / PAA / voice answer boxes
GEO   → Get cited in AI-generated composite answers
═══════════════════════════════════════════════════════
""") + case_study("B2B Tool Citation Gap", """
<p>A project management SaaS ranked #3 on Google for "best project management software" but was never cited by ChatGPT or Perplexity. Competitors with Wikipedia mentions, G2 profiles, and original benchmark studies dominated AI answers. After publishing an annual industry report and earning 12 editorial links, citations appeared within 8 weeks across three AI engines.</p>
"""))
        + lesson(2, titles[1], """
<p>ChatGPT with browsing and search plugins retrieves live or indexed web content, then synthesizes an answer. Citation behavior varies by query type, model version, and user settings.</p>
<h4>What ChatGPT Tends to Cite</h4>
<ul>
<li>Primary sources: official documentation, government sites, academic papers</li>
<li>Established publishers: major news, industry leaders, Wikipedia</li>
<li>Structured comparisons with clear pros/cons</li>
<li>Recent content for time-sensitive topics</li>
<li>Pages with clear authorship and topical focus</li>
</ul>
<h4>What It Often Ignores</h4>
<ul>
<li>Thin affiliate pages with duplicate summaries</li>
<li>Content behind aggressive paywalls or interstitials</li>
<li>Sites with weak entity signals or new domains without authority</li>
</ul>
""" + tip("<p>Run the same prompt monthly in ChatGPT browse mode; log cited domains in a GEO tracker spreadsheet.</p>") + mistake("<ul><li>Assuming training data alone drives citations—live retrieval matters for current queries</li><li>Optimizing for ChatGPT while ignoring Perplexity's different citation graph</li></ul>"))
        + lesson(3, titles[2], """
<p>Perplexity is built as an answer engine with explicit citations—every claim can link to sources. It favors recency, clarity, and domains with strong topical authority.</p>
<h4>Perplexity Optimization Tactics</h4>
<ol>
<li>Publish original research, statistics, and downloadable data</li>
<li>Use descriptive H2/H3 headings that match research queries</li>
<li>Maintain author pages and organizational About content</li>
<li>Ensure fast, bot-accessible pages (no blocking AI crawlers unnecessarily)</li>
<li>Build brand searches so Perplexity associates your entity with the topic</li>
</ol>
""" + diagram("""
PERPLEXITY CITATION FLOW (SIMPLIFIED)
──────────────────────────────────────────
User query → Retrieve top sources → Rank passages
           → Synthesize answer → Attach footnotes
Your goal: be in retrieved set with quotable passages
──────────────────────────────────────────
""") + case_study("Niche Blog Perplexity Win", """
<p>A cybersecurity blog published detailed CVE explainers within 24 hours of disclosure. Perplexity began citing them for technical queries ahead of slower mainstream outlets, driving 15k monthly referral visits from perplexity.ai.</p>
"""))
        + lesson(4, titles[3], """
<p>Google Gemini integrates with Google's index and Knowledge Graph. AI Mode in Search blends traditional results with generative summaries. Optimization aligns with Google quality guidelines plus entity clarity.</p>
<h4>Gemini / Google AI Visibility Factors</h4>
<ul>
<li>Strong organic rankings for related queries</li>
<li>Structured data reinforcing entities and facts</li>
<li>Google Business Profile and YouTube presence where relevant</li>
<li>Consistent NAP and sameAs schema across the web</li>
<li>Helpful Content System compliance</li>
</ul>
<p>Winning in Google still matters enormously for Gemini visibility—GEO on Google is not separate from SEO excellence.</p>
""" + tip("<p>Compare Gemini answers with AI Overviews for the same query; note overlap in cited domains.</p>"))
        + lesson(5, titles[4], """
<p>Claude and similar models used in research workflows often rely on uploaded documents or connected search. Brands appear when sources are authoritative, well-written, and fact-dense.</p>
<h4>Claude-Friendly Content Patterns</h4>
<ul>
<li>Executive summaries at document start</li>
<li>Explicit section labels and numbered findings</li>
<li>Methodology sections for research credibility</li>
<li neutral, declarative tone with cited sources</li>
<li>Markdown-friendly structure when content is syndicated</li>
</ul>
""" + mistake("<ul><li>Marketing fluff without extractable facts</li><li>PDFs that are image scans without OCR text</li></ul>"))
        + lesson(6, titles[5], """
<p>Citation optimization is deliberate engineering of quotable, trustworthy passages and distribution so AI systems encounter your brand.</p>
<h4>The Citation Stack</h4>
<ol>
<li><strong>On-site:</strong> definitive guides, glossaries, original data, expert bylines</li>
<li><strong>Off-site:</strong> Wikipedia-worthy facts, press coverage, industry directories</li>
<li><strong>Social proof:</strong> reviews on G2, Trustpilot, Google</li>
<li><strong>Technical:</strong> llms.txt (optional), clear robots policy, fast HTML</li>
<li><strong>PR:</strong> digital PR, expert quotes in trade publications</li>
</ol>
<pre class="diagram">Quotable passage formula:
Claim + evidence + scope + date
"We analyzed 10,000 WooCommerce stores (n=10,000, Q1 2026)
 and found median LCP improved 34% after CDN adoption."</pre>
""" + case_study("Original Data GEO Lift", """
<p>An email marketing firm published open benchmark data with CC licensing. Six AI tools cited the dataset within a quarter; organic backlinks increased 140% from researchers linking the source.</p>
"""))
        + lesson(7, titles[6], """
<p>Retrieval-Augmented Generation (RAG) powers most AI search: retrieve documents, then generate answers grounded in those documents. Understanding RAG explains why chunk-level clarity matters.</p>
""" + diagram("""
RAG PIPELINE (CONCEPTUAL)
════════════════════════════════════════════
1. EMBED query and document chunks
2. RETRIEVE top-k similar passages
3. RANK by relevance + authority heuristics
4. GENERATE answer citing retrieved passages
════════════════════════════════════════════
Implication: each H2 section should stand alone as a retrievable "chunk"
""") + """
<h4>Chunk-Level GEO Writing</h4>
<ul>
<li>One main idea per section under descriptive heading</li>
<li>First sentence of section answers the heading question</li>
<li>Avoid context that requires previous section to understand</li>
<li>Include entity names in full on first mention</li>
</ul>
""" + tip("<p>Test retrievability: ask an AI 'According to [your URL], what is X?' and see if it finds the right section.</p>"))
        + lesson(8, titles[7], """
<p>GEO measurement is immature compared to SEO—but systematic tracking is essential.</p>
<h4>GEO Tracking Program</h4>
<table>
<tr><th>Activity</th><th>Frequency</th></tr>
<tr><td>Prompt set testing (20–50 core queries)</td><td>Weekly</td></tr>
<tr><td>Citation share vs competitors</td><td>Monthly</td></tr>
<tr><td>Referral traffic from AI domains</td><td>Weekly in GA4</td></tr>
<tr><td>Brand mention monitoring</td><td>Ongoing</td></tr>
<tr><td>New authoritative placements</td><td>Per campaign</td></tr>
</table>
<h4>Sample Prompt Bank Categories</h4>
<ul>
<li>Best [product category] for [use case]</li>
<li>What is [concept you own]?</li>
<li>[Your brand] vs [competitor]</li>
<li>How to [problem you solve]</li>
</ul>
""" + mistake("<ul><li>Only tracking ChatGPT and ignoring Perplexity/Gemini</li><li>Celebrating citations for irrelevant prompts with no business value</li></ul>"))
    )
    workshop = """
<div class="workshop">
<strong>Workshop: Analyze Why AI Cites Some Sites and Not Others</strong>
<h4>Duration:</h4> 90 minutes
<h4>Materials:</h4> Laptops, shared spreadsheet template, access to ChatGPT, Perplexity, Gemini
<h4>Instructions:</h4>
<ol>
<li>Team selects one commercial query (e.g., "best wordpress seo plugin") and one informational query</li>
<li>Run both queries on ChatGPT (browse), Perplexity, and Gemini; export cited URLs</li>
<li>For each unique cited domain, score 1–5 on: authority, structure, originality, recency, entity strength</li>
<li>Run the same queries for your site or a client site—is it cited? If not, identify gap vs top cited page</li>
<li>List three concrete content or PR actions to close the citation gap</li>
<li>Groups present a 5-minute "citation autopsy" of one winning page</li>
</ol>
<h4>Deliverable:</h4> Citation analysis spreadsheet + one-page action plan
</div>
<div class="notes"><strong>Instructor Notes</strong>
<ul>
<li>Pre-seed queries relevant to your cohort's industries</li>
<li>Discuss GPTBot, ClaudeBot, and robots.txt—ethical crawling policies</li>
<li>Highlight that Wikipedia and Reddit appear often—students should not spam but understand entity graphs</li>
<li>AI outputs change—run workshop twice in course if possible to show volatility</li>
<li>Connect findings to Module 11 content production and Module 14 agents</li>
</ul></div>
"""
    exercises = """<ol>
<li>Build a 10-prompt GEO test bank for your niche.</li>
<li>Write one quotable, data-backed paragraph designed for AI citation.</li>
<li>Audit robots.txt for AI crawler rules and document decisions.</li>
<li>Compare cited sources for three queries across two AI engines.</li>
</ol>"""
    homework = """<p>Execute a 30-day GEO sprint: publish one original data section, earn one editorial mention, re-test prompt bank weekly, and submit a report with citation share before/after and referral traffic from AI sources.</p>"""
    quiz = """<ol>
<li>Define GEO in one sentence.</li>
<li>How does GEO differ from AEO?</li>
<li>Name three content types AI engines prefer to cite.</li>
<li>What is RAG?</li>
<li>Why do chunk-level headings matter for GEO?</li>
<li>Name two factors Perplexity weighs heavily.</li>
<li>What is a quotable passage formula element?</li>
<li>Why is Google SEO still relevant for Gemini?</li>
<li>What referral source appears in GA4 for Perplexity?</li>
<li>Name one GEO measurement activity and frequency.</li>
</ol>
<p><strong>Answer Key:</strong> 1) Optimizing to be cited in AI-generated answers 2) AEO targets SERP features; GEO targets AI synthesis citations 3) Original research, official docs, authoritative guides (any three) 4) Retrieval-Augmented Generation 5) AI retrieves passage-level chunks 6) Recency, clarity, authority (any two) 7) Claim + evidence + scope/date 8) Gemini leverages Google's index and quality systems 9) perplexity.ai (referral) 10) Weekly prompt testing (example)</p>"""
    outcomes = """<ul>
<li>Define GEO and distinguish it from SEO and AEO</li>
<li>Explain how major AI engines retrieve and cite sources</li>
<li>Apply citation optimization and quotable passage writing</li>
<li>Understand RAG and chunk-level content design</li>
<li>Run GEO measurement and competitive citation analysis</li>
<li>Complete AI citation autopsy workshop</li>
</ul>"""
    return module_header(
        10, "Generative Engine Optimization (GEO)",
        [
            "Define GEO and the AI citation landscape",
            "Optimize for ChatGPT, Perplexity, Gemini, and Claude",
            "Apply citation optimization and RAG-aware writing",
            "Build GEO measurement and prompt testing programs",
            "Develop competitive citation strategies",
        ],
        titles, lessons, workshop, exercises, homework, quiz, outcomes,
    )


def _module_11():
    titles = [
        "AI-Assisted Research Workflows for SEO",
        "Prompt Engineering for SEO Content",
        "Building SEO Content Briefs",
        "AI-Assisted Writing: Draft to Publish Pipeline",
        "Human Review, Fact-Checking, and Quality Gates",
        "Brand Voice and Style Guides with AI",
        "Scaling Content Production Safely",
        "AI Content Ethics, Policy, and Google Guidelines",
    ]
    lessons = (
        lesson(1, titles[0], """
<p>Modern SEO content starts with research—not keywords alone, but intent mapping, SERP analysis, entity gaps, and competitor information gain. AI accelerates synthesis but cannot replace strategic judgment.</p>
<h4>Research Workflow</h4>
<ol>
<li>Seed keywords from GSC, sales, and customer questions</li>
<li>SERP scrape: snippets, PAA, AI Overview sources, content length, format</li>
<li>Entity extraction: people, products, concepts competitors cover</li>
<li>Gap analysis: what top pages miss that users still need</li>
<li>Brief approval before any AI drafting</li>
</ol>
""" + diagram("""
AI RESEARCH STACK
────────────────────────────────────────
Inputs: GSC, Ahrefs, Also Asked, AI prompt tests
AI role: Summarize SERP, cluster intents, draft outline
Human role: Validate gaps, assign angle, approve brief
Output: Approved brief → production pipeline
────────────────────────────────────────
""") + tip("<p>Never skip SERP review—AI hallucinates competitor features and outdated rankings.</p>"))
        + lesson(2, titles[1], """
<p>Prompt engineering for SEO means specifying role, context, constraints, output format, and evaluation criteria—so AI produces usable drafts, not generic filler.</p>
<h4>Effective SEO Prompt Template</h4>
<pre class="diagram">Role: Senior SEO content strategist for [niche]
Context: Target query "[query]", intent [informational/commercial]
Constraints: 1,800 words, answer-first H1 block, 5 FAQs
Format: Markdown with H2 questions, table for comparison
Must include: [entities], [internal links], [CTA]
Avoid: passive voice, unverified stats, keyword stuffing</pre>
<h4>Advanced Techniques</h4>
<ul>
<li>Chain-of-thought: ask for outline before full draft</li>
<li>Few-shot: paste one exemplar paragraph from your site</li>
<li>Critic pass: second prompt to flag thin sections and missing E-E-A-T</li>
</ul>
""" + mistake("<ul><li>Single mega-prompt with no outline step</li><li>No word-level brand banned phrases list</li></ul>"))
        + lesson(3, titles[2], """
<p>A content brief is the contract between strategy and production. It prevents AI from wandering off-brand or off-intent.</p>
<h4>Brief Components</h4>
<table>
<tr><th>Section</th><th>Content</th></tr>
<tr><td>Objective</td><td>Query, intent, funnel stage, success metric</td></tr>
<tr><td>SERP analysis</td><td>Top URLs, formats, avg word count, snippet type</td></tr>
<tr><td>Outline</td><td>H1–H3 with question phrasing</td></tr>
<tr><td>Entities</td><td>Required mentions and internal link targets</td></tr>
<tr><td>E-E-A-T</td><td>Author, sources, original data requirements</td></tr>
<tr><td>GEO/AEO</td><td>Snippet block, FAQ list, quotable stats</td></tr>
</table>
""" + case_study("Agency Brief Discipline", """
<p>An agency reduced revision rounds from 4.1 to 1.6 per article by mandating brief sign-off before AI generation. Production time dropped 30% while quality scores rose.</p>
"""))
        + lesson(4, titles[3], """
<p>The draft-to-publish pipeline integrates AI at defined stages with human gates.</p>
""" + diagram("""
AI CONTENT PIPELINE
═══════════════════════════════════════════════
Brief approved
    → AI outline (human edit)
    → AI section drafts (human merge)
    → Human rewrite intro/conclusion
    → Fact-check + link check
    → SEO plugin optimization (Rank Math)
    → Editor QA → Publish → GSC inspect
═══════════════════════════════════════════════
""") + """
<h4>WordPress Integration</h4>
<p>Use block editor with reusable patterns. Plugins like Rank Math analyze focus keyword after human polish—not before. Schedule posts via editorial calendar; avoid bulk publish without review.</p>
""" + tip("<p>Track % AI-assisted vs human-written per URL in a content registry for quality audits.</p>"))
        + lesson(5, titles[4], """
<p>Human review is non-negotiable for YMYL, legal claims, pricing, and medical content. Even non-YMYL content needs fact-checking and voice alignment.</p>
<h4>Quality Gate Checklist</h4>
<ul>
<li>Every statistic has a primary source link</li>
<li>No fabricated quotes, cases, or product features</li>
<li>Internal links resolve; external links are authoritative</li>
<li>Reading level matches audience</li>
<li>Unique information gain vs top 3 SERP results</li>
<li>Disclosure if AI substantially assisted (per client policy)</li>
</ul>
""" + mistake("<ul><li>Publish AI drafts with wrong year in title</li><li>Accept AI citations to non-existent studies</li></ul>"))
        + lesson(6, titles[5], """
<p>Brand voice documents train humans and AI consistently. Include tone adjectives, sample paragraphs, vocabulary allow/deny lists, and formatting rules.</p>
<h4>Style Guide Elements for AI</h4>
<ol>
<li>Voice: conversational vs clinical examples</li>
<li>Person: first plural "we" vs third person</li>
<li>Formatting: Oxford comma, heading capitalization</li>
<li>Product naming: exact trademark usage</li>
<li>CTA patterns: approved button copy</li>
</ol>
<p>Attach style guide excerpt to every content prompt as context window allows.</p>
""" + case_study("Voice Drift Fix", """
<p>A fintech blog fed 3 gold-standard posts into every prompt as few-shot examples. Brand voice survey scores improved from 6.2 to 8.7/10 within one quarter.</p>
"""))
        + lesson(7, titles[6], """
<p>Scaling requires templates, brief libraries, and role specialization—not unmanned AI spam.</p>
<h4>Safe Scaling Model</h4>
<ul>
<li>Template pages for repeatable formats (comparisons, glossaries)</li>
<li>Editorial tiers: Tier 1 full custom, Tier 2 AI-assisted, Tier 3 programmatic</li>
<li>Weekly quality sampling: 10% deep audit</li>
<li>Indexation monitoring for spike detection</li>
</ul>
""" + diagram("""
CONTENT VELOCITY vs RISK
────────────────────────────────────
Low velocity + high review  → Safest
High velocity + low review  → Penalty risk
Target: High velocity + tiered review gates
────────────────────────────────────
"""))
        + lesson(8, titles[7], """
<p>Google's guidance rewards helpful, people-first content regardless of production method. Mass auto-generated pages without value violate spam policies.</p>
<h4>Ethical AI Content Principles</h4>
<ul>
<li>Disclose AI assistance where required by law or client</li>
<li>Never use AI to fake reviews, testimonials, or credentials</li>
<li>Respect copyright—don't paste proprietary text into public models</li>
<li>Maintain author accountability for published claims</li>
</ul>
<p>Align with Google's scaled content abuse and helpful content system documentation. When in doubt, add human expertise—not more AI passes.</p>
""" + tip("<p>Assign a 'content risk' rating (low/medium/high) to every brief; high risk requires subject-matter expert sign-off.</p>"))
    )
    workshop = """
<div class="workshop">
<strong>Workshop: Generate and Improve an Article with AI</strong>
<h4>Duration:</h4> 150 minutes
<h4>Materials:</h4> Approved brief template, ChatGPT/Claude access, WordPress staging, Rank Math
<h4>Instructions:</h4>
<ol>
<li>In pairs, complete a content brief for "how to optimize WooCommerce product schema"</li>
<li>Run three prompt passes: outline → section drafts → critic review</li>
<li>Human-edit intro, conclusion, and one body section entirely by hand</li>
<li>Fact-check all stats; add two internal links and one original tip from experience</li>
<li>Run quality gate checklist; score peer draft 1–10 with written feedback</li>
<li>Publish to staging; optimize title/meta in Rank Math</li>
<li>Lightning demo: show one AI failure caught in review</li>
</ol>
<h4>Deliverable:</h4> Staging URL + brief + prompt log + peer review scoresheet
</div>
<div class="notes"><strong>Instructor Notes</strong>
<ul>
<li>Provide a intentionally weak AI draft for a "fix it" exercise if time allows</li>
<li>Stress that prompts are intellectual property—students should save libraries</li>
<li>Discuss enterprise tools (Jasper, Writer, custom GPTs) vs raw ChatGPT</li>
<li>Connect pipeline to Module 13 n8n automation and Module 14 content agent</li>
</ul></div>
"""
    exercises = """<ol>
<li>Write a full SEO content brief for one target keyword.</li>
<li>Create a reusable prompt template with role, constraints, and format.</li>
<li>Run critic-pass prompt on any AI draft and fix three flagged issues.</li>
<li>Draft a one-page brand voice guide with 5 do/don't rules.</li>
</ol>"""
    homework = """<p>Produce one 1,500-word AI-assisted article end-to-end: brief, prompts, human edits, fact-check log, and reflection on where AI saved time vs where humans were essential.</p>"""
    quiz = """<ol>
<li>What five inputs belong in an SEO research workflow?</li>
<li>Name four parts of an SEO content brief.</li>
<li>What is a critic-pass prompt?</li>
<li>Why must humans fact-check AI drafts?</li>
<li>What is information gain?</li>
<li>Name two safe scaling practices.</li>
<li>What Google policy addresses low-value scaled content?</li>
<li>How do few-shot examples help brand voice?</li>
<li>Where should answer-first blocks appear?</li>
<li>What should a content registry track?</li>
</ol>
<p><strong>Answer Key:</strong> 1) Keywords, SERP, entities, gaps, approval (any five from lesson) 2) Objective, SERP analysis, outline, entities, E-E-A-T (any four) 3) Second prompt reviewing draft for gaps/errors 4) AI hallucinates facts and outdated info 5) Unique value vs competing pages 6) Tiered review, quality sampling (any two) 7) Scaled content abuse / helpful content system 8) They anchor tone and structure 9) Immediately under H1 10) AI-assistance level, author, metrics (reasonable answers)</p>"""
    outcomes = """<ul>
<li>Design AI-assisted SEO research workflows</li>
<li>Engineer prompts for outlines, drafts, and critique passes</li>
<li>Build comprehensive SEO content briefs</li>
<li>Operate draft-to-publish pipelines with human quality gates</li>
<li>Maintain brand voice and scale content safely</li>
<li>Apply Google AI content ethics and policies</li>
<li>Complete generate-and-improve article workshop</li>
</ul>"""
    return module_header(
        11, "AI Content Production",
        [
            "Build AI-assisted SEO research workflows",
            "Apply prompt engineering for SEO content",
            "Create production-ready content briefs",
            "Run AI-assisted writing pipelines with human review",
            "Maintain brand voice and scale safely",
            "Follow AI content ethics and Google guidelines",
        ],
        titles, lessons, workshop, exercises, homework, quiz, outcomes,
    )


def _module_12():
    titles = [
        "Introduction to Programmatic SEO",
        "Template Design for Scalable Pages",
        "Data-Driven Page Generation",
        "URL Architecture and Indexation at Scale",
        "Internal Linking and Hub Structure for pSEO",
        "Quality Gates and Thin Content Prevention",
        "WordPress Programmatic SEO Implementation",
        "Programmatic SEO Case Studies and ROI",
    ]
    lessons = (
        lesson(1, titles[0], """
<p>Programmatic SEO (pSEO) creates many pages from templates plus structured data—location pages, integrations, comparisons, glossary terms, tool pages. Done well, it captures long-tail demand at scale. Done poorly, it triggers thin content penalties.</p>
<h4>When pSEO Works</h4>
<ul>
<li>Each URL serves unique intent with unique data</li>
<li>Template adds value beyond mail-merge city names</li>
<li>Strong internal linking and sitemap discipline</li>
<li>Clear business model (lead gen, affiliate, SaaS integrations)</li>
</ul>
<h4>When It Fails</h4>
<ul>
<li>10,000 near-duplicate pages differing by one variable</li>
<li>No indexation strategy or crawl budget plan</li>
<li>Auto-generated text with no factual differentiation</li>
</ul>
""" + diagram("""
pSEO SUCCESS FORMULA
════════════════════════════════════════
Unique data × Useful template × Technical SEO
────────────────────────────────────────
≠ Mail merge spam
════════════════════════════════════════
""") + case_study("Zapier Integration Pages", """
<p>Zapier's integration directory generates thousands of "[App A] + [App B]" pages with unique setup steps and use cases—canonical pSEO at scale with genuine utility.</p>
"""))
        + lesson(2, titles[1], """
<p>Templates define repeating structure: hero, data module, FAQ, related links, CTA. Variables inject city, SKU, stat, or pairing.</p>
<h4>Template Components</h4>
<ol>
<li><strong>Title pattern:</strong> [Service] in [City] | [Brand]</li>
<li><strong>Meta description:</strong> dynamic with caps on length</li>
<li><strong>H1:</strong> matches primary intent</li>
<li><strong>Data block:</strong> tables, maps, stats from database</li>
<li><strong>Unique prose:</strong> min 150 words human or high-quality conditional copy</li>
<li><strong>FAQ:</strong> 3–5 localized or contextual questions</li>
</ol>
""" + tip("<p>Design templates in Figma or HTML first; validate one gold page before generating 500.</p>"))
        + lesson(3, titles[2], """
<p>Data sources include CSV, Airtable, PostgreSQL, WooCommerce exports, public APIs. n8n or custom scripts merge data into WordPress via REST API or WP-CLI.</p>
<h4>Data Pipeline</h4>
""" + diagram("""
DATA → PAGE PIPELINE
────────────────────────────────────────
Source (CSV/API/DB)
  → Validate & dedupe
  → Map fields to template variables
  → Generate slug & meta
  → Create/update WP post via REST
  → Trigger indexation check
────────────────────────────────────────
""") + """
<p>Version data sets; rollback when source errors create 404s or wrong prices.</p>
""" + mistake("<ul><li>Generating pages before data QA</li><li>No unique slug strategy causing collisions</li></ul>"))
        + lesson(4, titles[3], """
<p>URL patterns should be logical, shallow, and stable: <code>/integrations/slack-salesforce/</code> not <code>/p?id=88421</code>.</p>
<h4>Indexation Strategy</h4>
<ul>
<li>Phase rollout: 50 → 500 → 5,000 pages with GSC monitoring</li>
<li>Exclude low-value combinations with noindex until enriched</li>
<li>Sitemap index split by page type</li>
<li>Monitor "Crawled – not indexed" rate</li>
</ul>
""" + case_study("Phased Rollout Saves Crawl Budget", """
<p>A real estate startup published 12,000 city pages at once; 9,000 stayed unindexed. Re-launching in batches of 500 with unique local stats improved index rate to 78% over 4 months.</p>
"""))
        + lesson(5, titles[4], """
<p>Programmatic pages need programmatic internal links: related items, breadcrumbs, hub pages linking to all children.</p>
<h4>Linking Patterns</h4>
<ul>
<li>Hub: "All [Category] Integrations" lists child pages</li>
<li>Related: 6 nearest neighbors by category or geography</li>
<li>Breadcrumb: Home → Directory → Item</li>
<li>Footer sitemap modules for orphan prevention</li>
</ul>
""" + diagram("""
HUB-AND-SPOKE pSEO
        [HUB PAGE]
       /    |    \\
   Page  Page  Page ...
   each links back to hub + 3 related peers
"""))
        + lesson(6, titles[5], """
<p>Quality gates block publication below thresholds.</p>
<h4>Minimum Requirements Example</h4>
<table>
<tr><th>Gate</th><th>Rule</th></tr>
<tr><td>Word count</td><td>≥ 300 unique words per URL</td></tr>
<tr><td>Data fields</td><td>≥ 5 populated unique fields</td></tr>
<tr><td>Duplicate</td><td>Simhash distance above threshold</td></tr>
<tr><td>Images</td><td>≥ 1 relevant non-stock image</td></tr>
<tr><td>Manual spot check</td><td>5% random sample weekly</td></tr>
</table>
""" + tip("<p>Automate gate failures to Slack via n8n—Module 13 connects here.</p>"))
        + lesson(7, titles[6], """
<p>WordPress options: custom post types, ACF fields, WP All Import, headless front-end, or WooCommerce product loops.</p>
<h4>Implementation Checklist</h4>
<ol>
<li>Register CPT <code>location</code> or <code>integration</code></li>
<li>ACF field group mapped to template</li>
<li>Single PHP template or block theme template part</li>
<li>Rank Math dynamic title variables</li>
<li>REST endpoint or import for bulk create</li>
<li>Cache strategy (LiteSpeed) for high page count</li>
</ol>
<pre class="diagram">// Example slug pattern
/integrations/{app_a}-{app_b}/
/locations/{state}/{city}/</pre>
""" + mistake("<ul><li>Using posts instead of CPT—clutters blog archive</li><li>No canonical on filtered parameter URLs</li></ul>"))
        + lesson(8, titles[7], """
<p>ROI = organic traffic value + leads − production and hosting cost. Track by page cohort in GA4 segments.</p>
<h4>Benchmark Metrics</h4>
<ul>
<li>Indexed ratio (indexed / published)</li>
<li>Median clicks per page at 90 days</li>
<li>Long-tail keyword coverage</li>
<li>Conversion rate by template type</li>
</ul>
<p>Successful pSEO portfolios often show 80/20: most traffic from 20% of pages—optimize winners, prune losers with 301 or noindex.</p>
""" + case_study("Glossary pSEO", """
<p>A DevTools company published 2,400 API glossary terms with code examples. 180 pages drove 62% of organic signups from pSEO within one year.</p>
"""))
    )
    workshop = """
<div class="workshop">
<strong>Workshop: Mini Programmatic SEO Project</strong>
<h4>Duration:</h4> 180 minutes
<h4>Materials:</h4> CSV of 30 records (provided: US cities + population + median income), WordPress staging, ACF, optional WP All Import
<h4>Instructions:</h4>
<ol>
<li>Define template: "[Service] in [City], [State]" for a fictional marketing agency</li>
<li>Design URL pattern and CPT in WordPress</li>
<li>Map CSV columns to ACF fields; write conditional intro paragraph rules</li>
<li>Generate 30 pages via import or REST script</li>
<li>Build hub page linking all locations; add related-city module</li>
<li>Apply quality gate checklist; flag any failing pages</li>
<li>Submit sitemap; inspect 3 URLs in GSC</li>
<li>Present indexation risk assessment and phase-2 plan for 500 pages</li>
</ol>
<h4>Deliverable:</h4> Live staging hub + 30 child pages + quality gate spreadsheet
</div>
<div class="notes"><strong>Instructor Notes</strong>
<ul>
<li>Provide CSV with intentional bad rows for data validation teaching</li>
<li>Discuss legal/ethical issues with location pages without real presence</li>
<li>Compare WP All Import vs custom n8n workflow</li>
<li>Emphasize pruning strategy—not every generated page deserves index</li>
</ul></div>
"""
    exercises = """<ol>
<li>Sketch a pSEO template with 6 variable fields and one unique data module.</li>
<li>Design URL architecture for 1,000 comparison pages.</li>
<li>Write five quality gate rules for your template.</li>
<li>Identify one real site using pSEO well and one doing it poorly.</li>
</ol>"""
    homework = """<p>Plan a 100-page pSEO project for your niche: data source, template wireframe, indexation phases, quality gates, and projected ROI assumptions with KPIs at 90 days.</p>"""
    quiz = """<ol>
<li>What is programmatic SEO?</li>
<li>When does pSEO fail?</li>
<li>Name three template components.</li>
<li>Why phase rollouts?</li>
<li>What is a hub page in pSEO?</li>
<li>Name two quality gate examples.</li>
<li>Why use custom post types on WordPress?</li>
<li>What indexation metric should you monitor in GSC?</li>
<li>What is the 80/20 rule in pSEO portfolios?</li>
<li>How does n8n relate to pSEO?</li>
</ol>
<p><strong>Answer Key:</strong> 1) Many pages from templates + structured data 2) Thin duplicates, no unique value 3) Title pattern, data block, FAQ (any three) 4) Protect crawl budget and monitor quality 5) Directory linking to all child pages 6) Min word count, duplicate simhash (examples) 7) Separates scalable content from blog 8) Crawled – currently not indexed 9) Most traffic from minority of pages 10) Automates data → page pipelines</p>"""
    outcomes = """<ul>
<li>Evaluate pSEO opportunities and risks</li>
<li>Design scalable templates and data pipelines</li>
<li>Implement URL architecture and hub linking</li>
<li>Apply quality gates and phased indexation</li>
<li>Build WordPress pSEO implementations</li>
<li>Measure pSEO ROI and prune underperformers</li>
<li>Complete mini programmatic SEO project workshop</li>
</ul>"""
    return module_header(
        12, "Programmatic SEO",
        [
            "Understand programmatic SEO use cases and risks",
            "Design templates and data-driven page generation",
            "Plan URL architecture and indexation at scale",
            "Implement quality gates and WordPress pSEO",
            "Measure ROI and manage pSEO portfolios",
        ],
        titles, lessons, workshop, exercises, homework, quiz, outcomes,
    )


def _module_13():
    titles = [
        "n8n Fundamentals for SEO Teams",
        "SEO Monitoring and Alert Workflows",
        "Keyword Research Automation",
        "Content Publishing Automation",
        "Technical SEO Alert Workflows",
        "Search Console and Analytics Integrations",
        "Reporting Automation with Slack and Email",
        "Designing Autonomous SEO Operations",
    ]
    lessons = (
        lesson(1, titles[0], """
<p>n8n is a workflow automation platform connecting 400+ apps via nodes, webhooks, and code. For SEO teams, it replaces manual checks with scheduled, repeatable pipelines—without heavy engineering.</p>
<h4>Core Concepts</h4>
<ul>
<li><strong>Workflow:</strong> directed graph of nodes</li>
<li><strong>Trigger:</strong> schedule, webhook, manual, app event</li>
<li><strong>Nodes:</strong> HTTP Request, Google Sheets, Slack, OpenAI, WordPress</li>
<li><strong>Credentials:</strong> secure API key storage</li>
<li><strong>Executions:</strong> logs for debugging failed runs</li>
</ul>
""" + diagram("""
n8n SEO AUTOMATION LAYERS
═══════════════════════════════════════════════
Monitor  → GSC, uptime, rank trackers
Produce  → briefs, drafts, meta updates
Publish  → WordPress REST, schedule posts
Report   → Slack digests, client PDFs
═══════════════════════════════════════════════
""") + tip("<p>Self-host n8n via Docker for data privacy; cloud n8n for faster cohort setup.</p>"))
        + lesson(2, titles[1], """
<p>Monitoring workflows detect regressions before humans open dashboards.</p>
<h4>Example Monitoring Workflow</h4>
<ol>
<li>Schedule trigger: daily 6 AM</li>
<li>HTTP Request: pull GSC API for clicks/impressions delta</li>
<li>IF node: drop &gt; 15% week-over-week on priority URLs</li>
<li>Slack node: alert #seo-alerts with URL list</li>
<li>Google Sheets: log incident row</li>
</ol>
""" + case_study("Traffic Cliff Detection", """
<p>An e-commerce brand's n8n workflow flagged a 22% click drop on category pages within 24 hours of a robots.txt mistake. Mean time to detect fell from 9 days to 1 day.</p>
""") + mistake("<ul><li>Alert fatigue—too many thresholds with no prioritization</li><li>No runbook link in Slack messages</li></ul>"))
        + lesson(3, titles[2], """
<p>Automate keyword expansion while keeping human approval for targets.</p>
<h4>Keyword Automation Pipeline</h4>
""" + diagram("""
KEYWORD WORKFLOW
────────────────────────────────────────
Seed list (Sheets)
  → Ahrefs/Semrush API (related keywords)
  → Filter: volume &gt; 50, KD &lt; 40
  → Dedupe against existing content map
  → AI cluster by intent (OpenAI node)
  → Output brief rows for editor review
────────────────────────────────────────
""") + """
<p>Never auto-publish from keyword output alone—always gate with strategist approval.</p>
""" + tip("<p>Store API responses in n8n static data or Sheets for audit trails.</p>"))
        + lesson(4, titles[3], """
<p>Publishing automation drafts posts, sets meta, assigns categories, and schedules—human approval optional via Slack buttons.</p>
<h4>WordPress REST Publishing Flow</h4>
<ol>
<li>Trigger: new row in "Approved Briefs" sheet</li>
<li>OpenAI: generate draft from brief JSON</li>
<li>HTTP Request: POST <code>/wp-json/wp/v2/posts</code> as draft</li>
<li>Rank Math meta via custom REST field or plugin hook</li>
<li>Slack: "Review draft" link to editor</li>
</ol>
<pre class="diagram">POST /wp-json/wp/v2/posts
Authorization: Application Password
Body: title, content, status=draft, categories</pre>
""" + mistake("<ul><li>Publishing without staging review on YMYL sites</li><li>Hardcoding production credentials in workflow JSON exports</li></ul>"))
        + lesson(5, titles[4], """
<p>Technical SEO alerts cover uptime, SSL expiry, sitemap changes, Core Web Vitals regressions, and broken redirects.</p>
<h4>Technical Alert Examples</h4>
<table>
<tr><th>Check</th><th>Tool Node</th><th>Threshold</th></tr>
<tr><td>Homepage status</td><td>HTTP Request</td><td>≠ 200</td></tr>
<tr><td>SSL expiry</td><td>HTTP / SSL API</td><td>&lt; 14 days</td></tr>
<tr><td>Sitemap count</td><td>Parse XML</td><td>Δ &gt; 10%</td></tr>
<tr><td>CWV</td><td>PageSpeed API</td><td>LCP regression &gt; 500ms</td></tr>
</table>
""" + case_study("Redirect Chain Detector", """
<p>Weekly Screaming Frog export to Google Drive triggers n8n parsing; chains &gt; 2 hops auto-ticket in Linear with affected URLs.</p>
"""))
        + lesson(6, titles[5], """
<p>Google Search Console and GA4 APIs feed unified dashboards when native UI is insufficient.</p>
<h4>Integration Pattern</h4>
<ol>
<li>OAuth credentials for Google APIs in n8n</li>
<li>Fetch query/page data weekly</li>
<li>Merge with GA4 landing page metrics on URL</li>
<li>Write to BigQuery or Sheets for Looker Studio</li>
</ol>
<p>Respect API quotas; batch requests and cache results.</p>
""" + tip("<p>Map GSC query + page dimensions to content owner for accountability reports.</p>"))
        + lesson(7, titles[6], """
<p>Automated reports reduce client reporting time from hours to minutes.</p>
<h4>Weekly SEO Digest Workflow</h4>
<ul>
<li>Pull KPIs: clicks, impressions, avg position, top movers</li>
<li>Format Markdown message for Slack</li>
<li>Attach PDF from HTML template (optional HTTP to PDF service)</li>
<li>Email node for external stakeholders</li>
</ul>
""" + diagram("""
REPORT NODE CHAIN
Schedule → GSC + GA4 → Code (format)
         → Slack + Email → Archive row in Sheets
"""))
        + lesson(8, titles[7], """
<p>Autonomous SEO operations combine monitoring, decision rules, and limited auto-remediation—with human oversight for high-risk actions.</p>
<h4>Autonomy Maturity Model</h4>
<ol>
<li><strong>Level 1:</strong> Alerts only</li>
<li><strong>Level 2:</strong> Auto-tickets with suggested fixes</li>
<li><strong>Level 3:</strong> Auto-fix low-risk items (meta typos, broken internal links)</li>
<li><strong>Level 4:</strong> Agent-driven research and draft generation (Module 14)</li>
</ol>
<p>Document every autonomous action in an audit log. Roll back workflows that cause errors.</p>
""" + mistake("<ul><li>Auto-deploying robots.txt changes without review</li><li>Chaining too many AI steps without validation nodes</li></ul>"))
    )
    workshop = """
<div class="workshop">
<strong>Workshop: Build an Autonomous SEO Workflow in n8n</strong>
<h4>Duration:</h4> 180 minutes
<h4>Materials:</h4> n8n instance (Docker or cloud), GSC API access, Slack webhook, Google Sheet template
<h4>Instructions:</h4>
<ol>
<li>Import starter workflow: daily GSC fetch for top 20 URLs</li>
<li>Add IF node: alert if clicks drop &gt; 10% WoW on any URL</li>
<li>Connect Slack notification with URL, metric delta, and runbook link</li>
<li>Log all checks to Google Sheets with timestamp</li>
<li>Extension: add HTTP node checking homepage returns 200</li>
<li>Extension: add OpenAI node summarizing weekly trend in plain English</li>
<li>Test failure modes: break robots.txt on staging and confirm alert fires</li>
<li>Document workflow diagram and escalation path for stakeholders</li>
</ol>
<h4>Deliverable:</h4> Exported n8n JSON + screenshot of successful execution + runbook PDF
</div>
<div class="notes"><strong>Instructor Notes</strong>
<ul>
<li>Provide sanitized workflow JSON to reduce setup friction</li>
<li>Students without GSC API can use mock HTTP JSON</li>
<li>Discuss GDPR and credential rotation for client work</li>
<li>This workshop feeds directly into Module 14 agent orchestration</li>
<li>Common failure: OAuth scope—pre-verify Google credentials before class</li>
</ul></div>
"""
    exercises = """<ol>
<li>Diagram three SEO tasks you would automate first and expected time saved.</li>
<li>Build a simple HTTP Request node that fetches your sitemap and counts URLs.</li>
<li>Write Slack alert message template with severity levels.</li>
<li>Define autonomy Level 1 vs Level 3 actions for one client scenario.</li>
</ol>"""
    homework = """<p>Deploy one production-ready n8n workflow (monitoring OR reporting) for a real or lab WordPress site. Submit JSON export, 2-week execution log, and post-mortem if any run failed.</p>"""
    quiz = """<ol>
<li>What is n8n and why do SEO teams use it?</li>
<li>Name four n8n node types useful for SEO.</li>
<li>What should a traffic drop alert workflow include?</li>
<li>Why gate keyword automation with human approval?</li>
<li>How do you publish to WordPress via n8n?</li>
<li>Name two technical SEO checks to automate.</li>
<li>What APIs feed unified SEO dashboards?</li>
<li>What is autonomy Level 1 vs Level 3?</li>
<li>Why export workflow audit logs?</li>
<li>What is alert fatigue and how do you prevent it?</li>
</ol>
<p><strong>Answer Key:</strong> 1) Workflow automation connecting apps/APIs 2) HTTP, Schedule, Slack, Google Sheets (examples) 3) Threshold, URL list, notification, logging 4) Prevent low-quality target selection 5) WordPress REST API with auth 6) Uptime, SSL, CWV, redirects (any two) 7) GSC and GA4 8) Alerts only vs auto-fix low-risk 9) Accountability and debugging 10) Too many low-value alerts; prioritize thresholds</p>"""
    outcomes = """<ul>
<li>Understand n8n fundamentals for SEO automation</li>
<li>Build monitoring, keyword, and publishing workflows</li>
<li>Integrate GSC, GA4, Slack, and WordPress</li>
<li>Design reporting automation and autonomy maturity levels</li>
<li>Complete autonomous SEO workflow workshop</li>
</ul>"""
    return module_header(
        13, "n8n SEO Automation",
        [
            "Apply n8n fundamentals to SEO workflows",
            "Automate monitoring, keywords, and publishing",
            "Integrate Search Console, Analytics, and WordPress",
            "Build reporting and autonomous SEO operations",
        ],
        titles, lessons, workshop, exercises, homework, quiz, outcomes,
    )


def _module_14():
    titles = [
        "SEO Agent Architecture Overview",
        "Tool Calling and Function Design for SEO Agents",
        "Competitor Analysis Agent",
        "Content Production Agent",
        "Technical Audit Agent",
        "GEO Monitoring Agent",
        "Multi-Agent Orchestration Patterns",
        "Deploying Production SEO Agents",
    ]
    lessons = (
        lesson(1, titles[0], """
<p>SEO agents are LLM-powered systems that plan tasks, call tools, and iterate toward goals—audits, briefs, reports— with human oversight. Architecture separates planner, tools, memory, and guardrails.</p>
""" + diagram("""
SEO AGENT STACK
═══════════════════════════════════════════════
User goal → Planner (LLM)
         → Tool calls (GSC, crawl, SERP, WP)
         → Memory (vector DB / Sheets)
         → Guardrails (budget, allowlist)
         → Output (report, tickets, drafts)
═══════════════════════════════════════════════
""") + """
<h4>Agent vs Workflow</h4>
<ul>
<li><strong>n8n workflow:</strong> deterministic steps you define</li>
<li><strong>Agent:</strong> LLM decides next tool based on observations</li>
<li>Best practice: hybrid—agent for analysis, workflow for deployment</li>
</ul>
""" + case_study("Agency Audit Agent", """
<p>An agency built a GPT-4 agent with Screaming Frog export + GSC tools. Audit time per site dropped from 6 hours to 90 minutes with human final review.</p>
"""))
        + lesson(2, titles[1], """
<p>Tool calling lets agents invoke functions with structured parameters—search analytics, fetch URL, create ticket—not free-form hallucinated actions.</p>
<h4>Essential SEO Agent Tools</h4>
<table>
<tr><th>Tool</th><th>Input</th><th>Output</th></tr>
<tr><td>get_gsc_data</td><td>url, date_range</td><td>clicks, impressions, queries</td></tr>
<tr><td>fetch_serp</td><td>query</td><td>titles, snippets, features</td></tr>
<tr><td>crawl_url</td><td>url</td><td>status, title, h1, canonical</td></tr>
<tr><td>create_brief</td><td>keyword</td><td>markdown brief</td></tr>
<tr><td>wp_create_draft</td><td>title, content</td><td>post_id, edit_url</td></tr>
</table>
<p>Define JSON schemas strictly; validate responses before passing back to LLM.</p>
""" + tip("<p>Start with 3–5 tools; tool sprawl confuses models and increases cost.</p>") + mistake("<ul><li>Giving agents write access to production without approval gates</li><li>Tools that return unparsed HTML walls</li></ul>"))
        + lesson(3, titles[2], """
<p>Competitor agents automate SERP teardown: who ranks, content format, entities, backlink gap summaries.</p>
<h4>Agent Loop Example</h4>
<ol>
<li>User: "Analyze top 5 for 'woocommerce seo plugin'"</li>
<li>Agent calls fetch_serp → extracts URLs</li>
<li>Agent calls crawl_url on each → headings, word count, schema</li>
<li>Agent calls ahrefs_backlinks (if available) → DR comparison</li>
<li>Agent synthesizes gap report with recommended angle</li>
</ol>
""" + diagram("""
COMPETITOR AGENT OUTPUT SECTIONS
────────────────────────────────────
1. SERP feature map
2. Content format comparison table
3. Entity coverage matrix
4. Information gain opportunities
5. Recommended outline
────────────────────────────────────
"""))
        + lesson(4, titles[3], """
<p>Content agents chain research → brief → draft → critique, invoking Module 11 prompts as tool-backed steps.</p>
<h4>Guardrails</h4>
<ul>
<li>Max tokens and cost per run</li>
<li>Required brief approval tool before wp_create_draft</li>
<li>Fact-check tool: verify URLs in citations return 200</li>
<li>Banned phrase filter post-generation</li>
</ul>
""" + case_study("Editor-in-the-Loop Agent", """
<p>Content agent stops at draft; Slack approval button triggers publish workflow. Zero unauthorized publishes in 6 months.</p>
"""))
        + lesson(5, titles[4], """
<p>Technical audit agents interpret crawl data and prioritize fixes by impact and effort.</p>
<h4>Audit Agent Checklist Categories</h4>
<ul>
<li>Indexation: noindex, canonicals, orphans</li>
<li>Performance: CWV, image weight</li>
<li>Structure: headings, internal links</li>
<li>Schema: errors, missing types</li>
<li>Security: HTTPS, mixed content</li>
</ul>
<p>Output ranked ticket list with evidence snippets—not vague advice.</p>
""" + tip("<p>Feed agents pre-processed CSV from Screaming Frog, not raw 500MB exports.</p>"))
        + lesson(6, titles[5], """
<p>GEO agents run prompt banks across ChatGPT, Perplexity APIs (where available), log citations, and recommend citation gap actions from Module 10.</p>
<h4>GEO Agent Workflow</h4>
<ol>
<li>Load prompt bank from Sheets</li>
<li>Execute queries via browser automation or API</li>
<li>Parse cited domains and passages</li>
<li>Compare to client domain presence</li>
<li>Generate weekly GEO scorecard</li>
</ol>
""" + mistake("<ul><li>Conflating training-data mentions with live retrieval citations</li></ul>"))
        + lesson(7, titles[6], """
<p>Multi-agent systems assign specialized agents—researcher, writer, auditor, publisher—coordinated by orchestrator.</p>
""" + diagram("""
ORCHESTRATOR PATTERN
                    [Orchestrator]
                    /    |     \\
            Research  Content  Technical
              Agent    Agent     Agent
                 \\      |      /
                  Shared memory
""") + """
<p>Patterns: sequential handoff, parallel gather + merge, critic-reviewer dual agent.</p>
""" + case_study("Orchestrated Launch", """
<p>Product launch used researcher agent for SERP map, content agent for 5 drafts, technical agent for schema validation—orchestrator merged into single launch checklist.</p>
"""))
        + lesson(8, titles[7], """
<p>Production deployment requires observability, versioning, rate limits, and rollback.</p>
<h4>Production Checklist</h4>
<ol>
<li>Environment variables for all API keys</li>
<li>Logging: prompt, tool calls, outputs, latency, cost</li>
<li>Human approval for destructive/write tools</li>
<li>Version agent system prompts in Git</li>
<li>Load test tool endpoints before agent scale</li>
<li>Document failure modes and fallbacks</li>
</ol>
<p>Deploy on n8n AI nodes, LangChain, OpenAI Assistants API, or Cursor agents—architecture principles remain the same.</p>
""" + tip("<p>Run weekly eval sets: fixed tasks where expected tool sequence is known.</p>"))
    )
    workshop = """
<div class="workshop">
<strong>Workshop: Build a Complete SEO AI Agent</strong>
<h4>Duration:</h4> 240 minutes
<h4>Materials:</h4> OpenAI or Claude API, n8n with AI Agent node OR Python LangChain starter, GSC export CSV, Slack
<h4>Instructions:</h4>
<ol>
<li>Define agent goal: "Produce technical SEO audit summary for one URL"</li>
<li>Implement three tools: crawl_url (HTTP), parse_gsc_row (Code), format_report (template)</li>
<li>Write system prompt with role, tool usage rules, output format</li>
<li>Run agent on lab WordPress URL; verify tool call sequence in logs</li>
<li>Add guardrail: refuse to publish changes; output Markdown report only</li>
<li>Peer review: swap reports and validate three findings manually</li>
<li>Optional: connect Slack to deliver report on command</li>
<li>Present architecture diagram and cost per run estimate</li>
</ol>
<h4>Deliverable:</h4> Agent config/code + sample audit report + architecture one-pager
</div>
<div class="notes"><strong>Instructor Notes</strong>
<ul>
<li>Provide mock GSC CSV so API access is not a blocker</li>
<li>Cap API spend per student ($2–5) with rate limits</li>
<li>Discuss prompt injection when agents fetch untrusted URLs</li>
<li>Compare build vs buy: Semrush AI, Ahrefs AI vs custom agents</li>
<li>Link to Module 15 capstone where agents are integration requirement</li>
</ul></div>
"""
    exercises = """<ol>
<li>Sketch SEO agent architecture with 4 tools and one guardrail.</li>
<li>Write JSON schema for a get_gsc_data tool.</li>
<li>Define eval task: expected tools for "find top declining queries."</li>
<li>Compare when to use agent vs fixed n8n workflow.</li>
</ol>"""
    homework = """<p>Extend lab agent with a fourth tool (SERP or competitor crawl) and run 5 eval tasks. Submit logs showing correct tool selection on at least 4/5 runs.</p>"""
    quiz = """<ol>
<li>What are the four parts of SEO agent architecture?</li>
<li>How does an agent differ from an n8n workflow?</li>
<li>Name three essential SEO agent tools.</li>
<li>Why validate tool outputs before returning to LLM?</li>
<li>What should a competitor agent report include?</li>
<li>Name two content agent guardrails.</li>
<li>What does a technical audit agent output?</li>
<li>What is an orchestrator pattern?</li>
<li>Name three production deployment requirements.</li>
<li>What is a weekly agent eval set?</li>
</ol>
<p><strong>Answer Key:</strong> 1) Planner, tools, memory, guardrails 2) LLM chooses dynamic steps vs fixed graph 3) get_gsc_data, fetch_serp, crawl_url (examples) 4) Prevent hallucinated data propagation 5) SERP map, format table, gaps, outline (any three) 6) Cost cap, approval gate (examples) 7) Prioritized tickets with evidence 8) Coordinator delegating to specialist agents 9) Secrets mgmt, logging, approval, versioning (any three) 10) Fixed tasks testing tool usage consistency</p>"""
    outcomes = """<ul>
<li>Design SEO agent architecture with tools and guardrails</li>
<li>Build competitor, content, technical, and GEO agents</li>
<li>Apply multi-agent orchestration patterns</li>
<li>Deploy production-ready agents with observability</li>
<li>Complete full SEO AI agent workshop</li>
</ul>"""
    return module_header(
        14, "Building SEO Agents",
        [
            "Design SEO agent architecture and tool calling",
            "Build competitor, content, technical, and GEO agents",
            "Orchestrate multi-agent SEO systems",
            "Deploy production agents with guardrails and evals",
        ],
        titles, lessons, workshop, exercises, homework, quiz, outcomes,
    )


def _module_15():
    titles = [
        "Capstone Overview and Project Requirements",
        "WordPress Site Setup for SEO Excellence",
        "Technical SEO Foundation and Launch Checklist",
        "Content Cluster and AEO Strategy",
        "GEO Strategy and Citation Plan",
        "n8n Automation Implementation",
        "SEO Agent Deployment and Integration",
        "Final Presentation, Documentation, and Certification",
    ]
    lessons = (
        lesson(1, titles[0], """
<p>The capstone integrates Modules 1–14 into a live WordPress property with documented SEO strategy, content cluster, GEO/AEO execution, n8n automation, and a functioning SEO agent. This is your portfolio piece.</p>
<h4>Capstone Deliverables</h4>
<ol>
<li><strong>Live WordPress site</strong> — staging or production URL</li>
<li><strong>SEO strategy document</strong> — audience, keywords, competitors, KPIs</li>
<li><strong>Technical audit report</strong> — resolved critical issues checklist</li>
<li><strong>Content cluster</strong> — 1 pillar + minimum 5 supporting articles (AEO-optimized)</li>
<li><strong>GEO plan</strong> — prompt bank, citation targets, one original data or research asset</li>
<li><strong>n8n workflow</strong> — exported JSON for monitoring OR publishing automation</li>
<li><strong>SEO agent</strong> — configured agent with ≥3 tools and sample output report</li>
<li><strong>Final presentation</strong> — 15-minute demo + Q&A</li>
</ol>
""" + diagram("""
CAPSTONE TIMELINE (4 WEEKS)
═══════════════════════════════════════════════
Week 1: Site + technical foundation
Week 2: Content cluster + AEO
Week 3: GEO + automation + agent
Week 4: Polish, measure, present
═══════════════════════════════════════════════
""") + tip("<p>Students without a client should use a fictional business in a niche they know well.</p>"))
        + lesson(2, titles[1], """
<p>WordPress setup must follow Module 2–5 standards: performance, security, SEO plugin, schema-ready theme.</p>
<h4>Minimum Site Requirements</h4>
<ul>
<li>WordPress 6.x on HTTPS hosting (Docker lab or managed host)</li>
<li>SEO plugin: Rank Math or Yoast with sitemap enabled</li>
<li>Caching: LiteSpeed or equivalent</li>
<li>Theme: block theme or lightweight classic theme</li>
<li>Google Search Console and GA4 connected</li>
<li>Organization + WebSite schema on homepage</li>
</ul>
""" + case_study("Capstone Site Baseline", """
<p>Students using the course Docker stack deploy WooCommerce or blog variant, verify <code>local-docker.php</code> mu-plugin settings, and confirm sitemap at <code>/sitemap_index.xml</code> before content work begins.</p>
""") + mistake("<ul><li>Starting content before technical checklist complete</li><li>Using default 'Hello World' post as indexed content</li></ul>"))
        + lesson(3, titles[2], """
<p>Technical foundation covers crawlability, indexation, Core Web Vitals baseline, mobile usability, and structured data validation.</p>
<h4>Launch Checklist</h4>
<table>
<tr><th>Area</th><th>Pass Criteria</th></tr>
<tr><td>robots.txt</td><td>Allows key paths; sitemap declared</td></tr>
<tr><td>Sitemap</td><td>Submitted in GSC; no 404 URLs</td></tr>
<tr><td>CWV</td><td>LCP &lt; 2.5s mobile lab test</td></tr>
<tr><td>HTTPS</td><td>No mixed content on homepage</td></tr>
<tr><td>Schema</td><td>Rich Results Test passes for key templates</td></tr>
<tr><td>Redirects</td><td>Single hop from HTTP and www variants</td></tr>
</table>
<p>Document before/after for at least three fixed issues in the technical report.</p>
""" + tip("<p>Run Screaming Frog on capstone site—even 20 URLs teaches professional habit.</p>"))
        + lesson(4, titles[3], """
<p>Content cluster demonstrates Module 6 and 9 skills: pillar page, spokes, internal linking, answer-first formatting, FAQ schema.</p>
<h4>Cluster Requirements</h4>
<ul>
<li>One pillar (2,000+ words) targeting primary head or topic term</li>
<li>Five spokes (800+ words each) targeting long-tail and PAA questions</li>
<li>Bidirectional internal links between pillar and spokes</li>
<li>Each spoke includes snippet-ready answer paragraph and 3+ FAQs</li>
<li>Author bio and updated date visible (E-E-A-T)</li>
</ul>
""" + diagram("""
CONTENT CLUSTER MAP (EXAMPLE)
        [Pillar: Complete WooCommerce SEO Guide]
           /      |      \\      \\      \\
      Spoke1  Spoke2  Spoke3  Spoke4  Spoke5
      schema  speed   images  categories  local
"""))
        + lesson(5, titles[4], """
<p>GEO strategy proves Module 10 execution: prompt bank testing, citation gap analysis, and one asset designed for AI citation.</p>
<h4>GEO Deliverable Components</h4>
<ol>
<li>20-query prompt bank with baseline citation screenshot</li>
<li>Competitor citation analysis (who gets cited and why)</li>
<li>One original element: mini-study, benchmark table, or definitive glossary section</li>
<li>Chunk-optimized passages on pillar page (Module 10 Lesson 7)</li>
<li>30-day re-test plan with success metrics</li>
</ol>
""" + case_study("Capstone GEO Win", """
<p>A student published original "WordPress plugin performance benchmark" data on their pillar page. Perplexity cited the page within 45 days for a commercial query; referrals tracked in GA4.</p>
"""))
        + lesson(6, titles[5], """
<p>Automation demonstrates Module 13: at least one production workflow with logging and documentation.</p>
<h4>Acceptable Automation Projects</h4>
<ul>
<li>Daily GSC anomaly alert to Slack/email</li>
<li>Weekly SEO KPI digest</li>
<li>Approved brief → WordPress draft pipeline</li>
<li>Broken link monitor on capstone URLs</li>
<li>pSEO data import trigger (if Module 12 used)</li>
</ul>
<p>Submit exported n8n JSON, credential redaction notes, and runbook for maintenance.</p>
""" + mistake("<ul><li>Workflow that only works on instructor's machine</li><li>No error handling branch in workflow</li></ul>"))
        + lesson(7, titles[6], """
<p>SEO agent demonstrates Module 14: planner + tools + guardrails producing actionable output.</p>
<h4>Minimum Agent Requirements</h4>
<ul>
<li>Clear system prompt defining role and limits</li>
<li>≥3 functional tools (crawl, GSC data, SERP, or brief generator)</li>
<li>Sample run output: audit, competitor summary, or content brief</li>
<li>Human approval gate for any write/publish action</li>
<li>Cost and latency estimate documented</li>
</ul>
<p>Agent may run in n8n, Python, or OpenAI Assistants—architecture clarity matters more than stack.</p>
""" + tip("<p>Include one 'failure case' in documentation showing agent mistake caught by human review.</p>"))
        + lesson(8, titles[7], """
<p>Final presentation tells the story: business context, strategy, execution, metrics, and lessons learned.</p>
<h4>Presentation Outline (15 minutes)</h4>
<ol>
<li>Site and business context (2 min)</li>
<li>SEO strategy and keyword map (2 min)</li>
<li>Technical highlights and fixes (2 min)</li>
<li>Content cluster + AEO examples (3 min)</li>
<li>GEO results or baseline (2 min)</li>
<li>Live demo: n8n workflow + agent (3 min)</li>
<li>Metrics, next 90 days, Q&A (1 min)</li>
</ol>
<h4>Grading Rubric (100 points)</h4>
<table>
<tr><th>Component</th><th>Points</th></tr>
<tr><td>Technical foundation</td><td>15</td></tr>
<tr><td>Content cluster + AEO</td><td>25</td></tr>
<tr><td>GEO strategy</td><td>15</td></tr>
<tr><td>Automation workflow</td><td>15</td></tr>
<tr><td>SEO agent</td><td>15</td></tr>
<tr><td>Presentation + documentation</td><td>15</td></tr>
</table>
<p>Certification requires ≥70 points and live site URL accessible to reviewers.</p>
""" + case_study("Portfolio Value", """
<p>Capstone sites frequently become freelance case studies. Students should add strategy doc and agent demo to LinkedIn portfolio posts.</p>
"""))
    )
    workshop = """
<div class="workshop">
<strong>Workshop: Capstone Sprint Planning and Milestone Setup</strong>
<h4>Duration:</h4> 120 minutes (Week 1 kickoff)
<h4>Materials:</h4> Capstone checklist template, project board (Trello/Notion/GitHub Projects), Docker or hosting access
<h4>Instructions:</h4>
<ol>
<li>Define business niche, target audience, and primary conversion goal</li>
<li>Complete Week 1 milestone: WordPress live, GSC/GA4 connected, technical checklist 50%+</li>
<li>Draft keyword map: 1 pillar + 5 spoke targets with SERP notes</li>
<li>Assign GEO prompt bank seeds and automation choice</li>
<li>Sketch agent architecture on whiteboard</li>
<li>Set up weekly standup schedule and peer accountability pairs</li>
<li>Instructor approves scope—prevent over-scoped capstones</li>
</ol>
<h4>Deliverable:</h4> Capstone project charter (1–2 pages) with timeline and success metrics
</div>
<div class="notes"><strong>Instructor Notes</strong>
<ul>
<li>Reject capstones that skip automation or agent—integration is the point</li>
<li>Provide rubric PDF at kickoff; no surprises at presentation</li>
<li>Schedule midpoint review in Week 2 to catch technical debt</li>
<li>Allow team capstones (max 3) with clear individual accountability</li>
<li>Certification exam (course-level) can pull questions from Modules 9–15 quizzes</li>
<li>Extension policy: +1 week for documented blockers only</li>
</ul></div>
"""
    exercises = """<ol>
<li>Draft capstone project charter with all eight deliverables listed.</li>
<li>Complete technical checklist on your site; screenshot GSC sitemap status.</li>
<li>Outline pillar + 5 spoke titles with target queries.</li>
<li>Write GEO prompt bank (10 queries) and run baseline citation test.</li>
</ol>"""
    homework = """<p>Execute full capstone over four weeks. Submit portfolio folder: strategy PDF, technical report, content URLs, n8n JSON, agent sample output, presentation slides, and 500-word retrospective on what you would scale next.</p>"""
    quiz = """<ol>
<li>Name all eight capstone deliverables.</li>
<li>What is the minimum content cluster size?</li>
<li>What technical items must pass before launch?</li>
<li>What GEO asset types satisfy the citation requirement?</li>
<li>What n8n submission is required?</li>
<li>How many tools must the SEO agent include?</li>
<li>What is the presentation time limit?</li>
<li>What is the minimum passing score?</li>
<li>What should the four-week timeline cover?</li>
<li>Why include a human approval gate on agents?</li>
</ol>
<p><strong>Answer Key:</strong> 1) Live WP site, strategy doc, technical report, content cluster, GEO plan, n8n workflow, SEO agent, presentation 2) 1 pillar + 5 spokes 3) robots, sitemap, CWV, HTTPS, schema, redirects (core items) 4) Original data, benchmark, definitive glossary section (examples) 5) Exported JSON + runbook 6) Three 7) 15 minutes 8) 70/100 9) Site/tech, content/AEO, GEO/automation/agent, present 10) Prevent unauthorized automated changes</p>"""
    outcomes = """<ul>
<li>Launch a WordPress site meeting technical SEO standards</li>
<li>Execute a documented SEO and content cluster strategy</li>
<li>Implement AEO and GEO plans with measurable baselines</li>
<li>Deploy n8n automation and a functional SEO agent</li>
<li>Present integrated capstone and earn certification eligibility</li>
<li>Build a portfolio-ready SEO operating system</li>
</ul>"""
    return module_header(
        15, "Capstone Project",
        [
            "Integrate SEO, AEO, GEO, automation, and agents on WordPress",
            "Deliver technical foundation and content cluster",
            "Implement n8n workflows and SEO agent",
            "Present capstone and meet certification requirements",
        ],
        titles, lessons, workshop, exercises, homework, quiz, outcomes,
    )


def get_modules_9_15():
    """Return HTML strings for course modules 9 through 15."""
    return [
        _module_9(),
        _module_10(),
        _module_11(),
        _module_12(),
        _module_13(),
        _module_14(),
        _module_15(),
    ]


if __name__ == "__main__":
    modules = get_modules_9_15()
    for i, html in enumerate(modules, start=9):
        print(f"Module {i}: {len(html):,} characters")
    print(f"Total: {sum(len(m) for m in modules):,} characters across {len(modules)} modules")
