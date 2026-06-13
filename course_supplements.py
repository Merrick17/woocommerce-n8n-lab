#!/usr/bin/env python3
"""Supplementary course materials: glossary, checklists, slides, workshops, rubrics, exam."""


def _glossary_html():
    terms = [
        ("AI Overview", "Google's AI-generated answer box at the top of select SERPs, synthesizing information from multiple sources with citations."),
        ("AI Search", "Search interfaces powered by large language models that generate conversational answers rather than only listing links."),
        ("Alt Text", "HTML alt attribute describing images for accessibility and image search relevance."),
        ("Anchor Text", "Clickable text in a hyperlink; a ranking signal when descriptive and relevant."),
        ("Answer Engine", "Platforms like Perplexity or You.com that provide direct answers with source citations."),
        ("Answer Engine Optimization (AEO)", "Optimizing content to be selected and cited as the authoritative answer by AI and featured-snippet systems."),
        ("Authority", "Perceived trustworthiness of a site or page based on expertise, links, brand signals, and citations."),
        ("Backlink", "An inbound hyperlink from another domain pointing to your page; core off-page SEO signal."),
        ("BERT", "Google's Bidirectional Encoder Representations from Transformers; improves query and content understanding."),
        ("Breadcrumb", "Navigational trail showing page hierarchy; supports UX and structured data."),
        ("Canonical Tag", "rel=canonical link element indicating the preferred URL when duplicate or similar pages exist."),
        ("Citation", "Reference to a source URL in AI-generated answers; GEO success metric."),
        ("Click-Through Rate (CTR)", "Percentage of impressions that result in clicks; influenced by titles and meta descriptions."),
        ("Content Cluster", "Hub-and-spoke content architecture linking pillar pages to related subtopic articles."),
        ("Content Decay", "Gradual traffic loss as content becomes outdated or competitors publish fresher material."),
        ("Core Web Vitals", "Google page experience metrics: LCP, INP, and CLS."),
        ("Crawl Budget", "Limited resources search engines allocate to crawling a site within a given period."),
        ("Crawlability", "Ability of search engine bots to discover and access URLs without obstruction."),
        ("Crawler", "Automated bot (e.g., Googlebot) that fetches web pages for indexing."),
        ("Cumulative Layout Shift (CLS)", "Core Web Vital measuring unexpected layout movement during page load."),
        ("Disavow File", "Google Search Console file listing backlinks you ask Google to ignore."),
        ("Domain Authority", "Third-party metric estimating ranking strength; not a Google official signal."),
        ("Duplicate Content", "Substantially similar content accessible at multiple URLs; may dilute rankings."),
        ("E-E-A-T", "Experience, Expertise, Authoritativeness, Trustworthiness; quality framework for YMYL topics."),
        ("Entity", "A distinct real-world person, place, thing, or concept recognized in knowledge systems."),
        ("Entity SEO", "Optimizing for entity recognition, disambiguation, and Knowledge Graph inclusion."),
        ("Featured Snippet", "Position-zero answer box extracted from a page and displayed above organic results."),
        ("Generative Engine Optimization (GEO)", "Optimizing content and brand presence to be cited by generative AI search tools."),
        ("Google Business Profile", "Local business listing on Google Search and Maps."),
        ("Google Search Console", "Free tool for monitoring indexing, performance, and technical issues."),
        ("Heading Tags", "H1–H6 HTML elements structuring content hierarchy for users and crawlers."),
        ("Hreflang", "Attribute signaling language and regional targeting for multilingual sites."),
        ("Index", "Search engine database of crawled pages eligible to appear in results."),
        ("Indexing", "Process of storing and organizing crawled pages for retrieval."),
        ("Information Gain", "Unique value a page adds beyond what already ranks for a query."),
        ("Interaction to Next Paint (INP)", "Core Web Vital measuring responsiveness to user interactions."),
        ("Internal Link", "Hyperlink between pages on the same domain distributing authority and context."),
        ("JSON-LD", "JavaScript Object Notation for Linked Data; preferred format for schema markup."),
        ("Keyword Cannibalization", "Multiple pages competing for the same query, splitting ranking potential."),
        ("Keyword Intent", "Underlying goal behind a search query: informational, navigational, commercial, transactional."),
        ("Knowledge Graph", "Google's database of entities and their relationships powering rich results."),
        ("Knowledge Panel", "Information box about an entity displayed in search results."),
        ("Large Language Model (LLM)", "AI model trained on vast text corpora to generate and understand language."),
        ("Largest Contentful Paint (LCP)", "Core Web Vital measuring main content load performance."),
        ("Link Building", "Acquiring quality backlinks through outreach, content, and partnerships."),
        ("Local Pack", "Map-based local business results for geo-modified queries."),
        ("Local SEO", "Optimizing for location-based searches and Google Business Profile."),
        ("Long-Tail Keyword", "Specific, lower-volume query phrase often with clearer intent."),
        ("Meta Description", "HTML summary influencing SERP snippet and click appeal; not a direct ranking factor."),
        ("Mobile-First Indexing", "Google primarily uses mobile version of pages for indexing and ranking."),
        ("NAP Consistency", "Matching Name, Address, Phone across directories and local citations."),
        ("Natural Language Processing (NLP)", "Technology enabling machines to interpret human language."),
        ("Noindex", "Directive preventing a page from appearing in search results."),
        ("Off-Page SEO", "External signals—primarily links and brand mentions—affecting rankings."),
        ("On-Page SEO", "Optimizing HTML, content, and internal structure of individual pages."),
        ("Organic Search", "Unpaid search engine traffic from standard result listings."),
        ("Page Experience", "Google ranking consideration including Core Web Vitals and UX signals."),
        ("PageRank", "Google's original link-analysis algorithm measuring page importance via links."),
        ("People Also Ask (PAA)", "Expandable question boxes on SERPs surfacing related queries."),
        ("Pillar Page", "Comprehensive hub page covering a broad topic linked to cluster content."),
        ("Programmatic SEO", "Template-driven page generation at scale for long-tail keyword coverage."),
        ("Prompt Engineering", "Crafting effective instructions for AI models to produce desired outputs."),
        ("Query Fanout", "AI systems decomposing a user query into sub-queries for retrieval."),
        ("RankBrain", "Google machine learning system helping interpret unfamiliar queries."),
        ("Redirect", "Server instruction sending users and bots from one URL to another (301/302)."),
        ("Retrieval-Augmented Generation (RAG)", "AI pattern combining search retrieval with generative answers."),
        ("Rich Result", "Enhanced SERP listing using structured data (stars, FAQs, recipes, etc.)."),
        ("Robots.txt", "File instructing crawlers which paths they may or may not request."),
        ("Schema Markup", "Structured vocabulary (Schema.org) helping search engines understand page content."),
        ("Search Console Coverage", "Report showing indexed, excluded, and error URLs."),
        ("Search Intent", "Purpose behind a query; alignment with intent is critical for rankings."),
        ("Semantic SEO", "Optimizing for topics and entity relationships, not isolated keywords."),
        ("SERP", "Search Engine Results Page displaying organic, paid, and rich features."),
        ("Sitemap", "XML file listing important URLs to aid discovery and crawling."),
        ("Slug", "URL path segment identifying a page, typically derived from the title."),
        ("Structured Data", "Machine-readable annotations enabling rich results and entity clarity."),
        ("Technical SEO", "Infrastructure optimizations: crawlability, speed, indexing, security, architecture."),
        ("Topical Authority", "Demonstrated depth and breadth of expertise across a subject area."),
        ("Transactional Intent", "Query indicating readiness to purchase or convert."),
        ("User-Generated Content (UGC)", "Reviews, comments, and forum posts contributing to site content."),
        ("Voice Search", "Spoken queries via assistants; favors concise, conversational answers."),
        ("WordPress", "Open-source CMS powering over 40% of websites; extensible via plugins and themes."),
        ("XML Sitemap", "Sitemap format submitted to search engines listing crawlable URLs."),
        ("YMYL", "Your Money Your Life—topics affecting health, finance, safety requiring high E-E-A-T."),
        ("Zero-Click Search", "User obtains answer on SERP without clicking through to a website."),
        ("404 Error", "HTTP status indicating a page was not found; harms UX and wastes crawl budget if widespread."),
        ("301 Redirect", "Permanent redirect passing most link equity to the destination URL."),
        ("302 Redirect", "Temporary redirect; link equity handling differs from 301."),
        ("A/B Testing", "Comparing two page variants to measure performance impact on SEO or conversions."),
        ("Above the Fold", "Content visible without scrolling; important for engagement signals."),
        ("Algorithm Update", "Search engine change to ranking systems affecting visibility."),
        ("Alt Attribute", "See Alt Text; critical for image SEO and WCAG compliance."),
        ("API", "Application Programming Interface enabling integrations like n8n workflows with SEO tools."),
        ("Autonomous Agent", "AI system executing multi-step tasks with tools and memory."),
        ("Bounce Rate", "Percentage of single-page sessions; contextual engagement indicator."),
        ("Brand SERP", "Search results page for a brand name query."),
        ("Cache", "Stored copy of resources speeding delivery; misconfiguration can hide updates from crawlers."),
        ("CDN", "Content Delivery Network distributing assets globally for faster load times."),
        ("Cloaking", "Showing different content to crawlers vs users; violates search guidelines."),
        ("Content Brief", "Document outlining target keyword, intent, structure, and entities for writers."),
        ("Content Management System (CMS)", "Software like WordPress for creating and managing web content."),
        ("Conversion Rate Optimization (CRO)", "Improving percentage of visitors completing desired actions."),
        ("Crawl Depth", "Number of clicks from homepage to reach a URL; shallow is preferable."),
        ("Dwell Time", "Approximate time user spends on page after clicking from SERP."),
        ("Evergreen Content", "Material remaining relevant over long periods with periodic updates."),
        ("Faceted Navigation", "Filter-based browsing creating many URL combinations; requires SEO controls."),
        ("Fetch and Render", "Google process of loading page resources like a browser for indexing."),
        ("Gutenberg", "WordPress block editor for building content with reusable blocks."),
        ("Hallucination", "AI generating plausible but false information; critical risk in AI content."),
        ("Headless WordPress", "WordPress as backend CMS with decoupled JavaScript frontend."),
        ("HTTP/2", "Protocol enabling multiplexed requests improving page load performance."),
        ("HTTPS", "Secure HTTP; ranking signal and trust requirement since 2014."),
        ("IndexNow", "Protocol notifying search engines immediately when content changes."),
        ("Information Architecture", "Organizational structure of site content and navigation."),
        ("JavaScript SEO", "Ensuring JS-rendered content is crawlable and indexable."),
        ("Link Equity", "Ranking value passed through hyperlinks, also called link juice."),
        ("Log File Analysis", "Reviewing server logs to understand crawler behavior."),
        ("Multilingual SEO", "Optimizing sites for multiple languages and regions."),
        ("n8n", "Open-source workflow automation tool used in this course for SEO pipelines."),
        ("Open Graph", "Meta tags controlling social media preview cards."),
        ("Orphan Page", "Page with no internal links pointing to it; hard for crawlers to discover."),
        ("Pagination", "Splitting content across multiple pages; use rel=next/prev or view-all strategies."),
        ("Passage Ranking", "Google ranking specific page sections independently for queries."),
        ("Pogo-Sticking", "User quickly returning to SERP after clicking a result; negative quality signal."),
        ("Rank Tracking", "Monitoring keyword positions over time across devices and locations."),
        ("Render-Blocking Resources", "CSS/JS delaying first paint; impacts Core Web Vitals."),
        ("Responsive Design", "Layout adapting to screen sizes; required for mobile-first indexing."),
        ("Search Generative Experience (SGE)", "Google's experimental AI-enhanced search interface precursor to AI Overviews."),
        ("Seed Keyword", "Starting term expanded into related keywords for research."),
        ("Semantic HTML", "Using HTML elements for their intended meaning (nav, article, header)."),
        ("Site Migration", "Moving site to new domain or platform; high-risk SEO operation."),
        ("Soft 404", "Page returning 200 status but displaying not-found content."),
        ("Topic Map", "Visual or structured representation of content relationships and gaps."),
        ("URL Parameter", "Query string values creating duplicate URL variants."),
        ("Web Vitals", "Google metrics for loading, interactivity, and visual stability."),
        ("WooCommerce", "WordPress e-commerce plugin requiring specialized SEO for products and categories."),
        ("Workflow Automation", "Connecting apps and triggers (e.g., n8n) to automate SEO tasks."),
    ]
    items = "".join(f"<dt>{t}</dt><dd>{d}</dd>" for t, d in terms)
    return f'<section id="glossary"><h1>Glossary of Terms</h1><p>Comprehensive reference of {len(terms)} SEO, AEO, GEO, WordPress, and AI terms used throughout this course.</p><dl>{items}</dl></section>'


def _checklist(title, items):
    lis = "".join(f"<li>{item}</li>" for item in items)
    return f"<h3>{title}</h3><ul class=\"checklist\">{lis}</ul>"


def _checklists_html():
    seo = [
        "Define primary and secondary target keywords for each page",
        "Align page content with identified search intent",
        "Write unique, compelling title tags under 60 characters",
        "Craft meta descriptions that encourage clicks (150–160 characters)",
        "Use one clear H1 per page matching primary intent",
        "Structure content with logical H2–H4 hierarchy",
        "Include primary keyword naturally in first 100 words",
        "Add internal links to related pillar and cluster pages",
        "Ensure every page has at least 2–3 contextual internal links pointing to it",
        "Optimize images with descriptive filenames and alt text",
        "Compress images without visible quality loss",
        "Create and submit XML sitemap via Search Console",
        "Verify site ownership in Google Search Console and Bing Webmaster Tools",
        "Monitor index coverage and fix excluded URLs",
        "Build topical authority through content clusters",
        "Conduct quarterly content audits for decay and cannibalization",
        "Update outdated statistics, screenshots, and examples annually",
        "Earn quality backlinks through digital PR and linkable assets",
        "Disavow toxic links only after manual review",
        "Track rankings for priority keywords weekly",
        "Analyze Search Console queries for new content opportunities",
        "Implement breadcrumb navigation with schema markup",
        "Add FAQ sections targeting People Also Ask queries",
        "Ensure NAP consistency for any local presence",
        "Set up Google Analytics 4 with conversion events",
        "Define KPIs: organic traffic, impressions, CTR, conversions",
        "Benchmark against top 3 competitors for target queries",
        "Document SEO changes in a change log for troubleshooting",
        "Review Core Web Vitals monthly in Search Console",
        "Create a 90-day content calendar aligned with keyword research",
    ]
    aeo = [
        "Identify top 20 questions your audience asks in search and AI tools",
        "Structure answers in 40–60 word concise paragraphs for snippet extraction",
        "Use question-based H2/H3 headings matching natural language queries",
        "Implement FAQPage schema on Q&A content",
        "Add HowTo schema for step-by-step tutorials",
        "Include definitive opening sentences that directly answer the query",
        "Use ordered lists for process-based answers",
        "Use unordered lists for feature comparisons",
        "Create comparison tables for versus queries",
        "Cite authoritative sources with outbound links to build trust",
        "Add author bios with credentials on expert content",
        "Publish original research, surveys, or data studies",
        "Optimize for voice search with conversational phrasing",
        "Test queries in Google, Bing, and Perplexity for snippet opportunities",
        "Monitor featured snippet wins and losses monthly",
        "Build content that answers follow-up questions (PAA chains)",
        "Ensure mobile readability with short paragraphs",
        "Include speakable schema for voice assistant eligibility",
        "Create dedicated answer pages for high-volume single questions",
        "Measure zero-click visibility via impression data in Search Console",
        "Format dates and update timestamps on time-sensitive answers",
        "Use table of contents for long-form answer guides",
        "Validate structured data with Google Rich Results Test",
        "Avoid ambiguous pronouns; use entity names explicitly",
        "Test answer extraction by reading H2 sections in isolation",
    ]
    geo = [
        "Audit brand citations across ChatGPT, Perplexity, Gemini, and Copilot",
        "Create entity-rich About pages with Organization schema",
        "Maintain consistent brand name, logo, and description across the web",
        "Publish on authoritative platforms (LinkedIn, Medium, industry publications)",
        "Ensure Wikipedia/Wikidata presence if eligible (notable entities)",
        "Build comprehensive topic pages AI systems can reference",
        "Include statistics with clear attribution and publication dates",
        "Structure content with extractable facts, definitions, and lists",
        "Earn mentions in news, podcasts, and industry roundups",
        "Monitor competitor citations in AI answers for gap analysis",
        "Use sameAs schema linking to official social profiles",
        "Create original quotable insights for journalists and AI training visibility",
        "Maintain updated press/media kit page",
        "Submit site to relevant industry directories and associations",
        "Track AI referral traffic in analytics (utm parameters where possible)",
        "Optimize for query fanout by covering subtopics comprehensively",
        "Ensure robots.txt allows AI crawlers you want to permit (GPTBot, etc.)",
        "Document brand facts in a single canonical source page",
        "Publish case studies with measurable outcomes",
        "Use clear headings that match how users phrase AI prompts",
        "Refresh cornerstone content quarterly for citation freshness",
        "Build relationships with sources AI engines already trust",
        "Create comparison content citing primary sources, not competitors only",
        "Measure share of voice in AI answers vs top 3 competitors",
        "Implement llms.txt if appropriate for AI discovery guidance",
    ]
    wordpress = [
        "Update WordPress core, themes, and plugins within 7 days of security releases",
        "Use a lightweight, SEO-friendly theme (GeneratePress, Kadence, etc.)",
        "Install an SEO plugin (Rank Math, Yoast, or SEOPress) and configure basics",
        "Set permalinks to Post name structure (/sample-post/)",
        "Disable author archives if single-author site",
        "Disable attachment pages (redirect to media file or parent)",
        "Configure canonical URLs in SEO plugin",
        "Enable XML sitemap in SEO plugin; exclude low-value post types",
        "Set noindex on tag archives if thin content",
        "Configure breadcrumbs in SEO plugin and theme",
        "Add Organization and WebSite schema site-wide",
        "Set up caching plugin (WP Rocket, LiteSpeed Cache, or W3 Total Cache)",
        "Enable lazy loading for images",
        "Use WebP or AVIF image formats",
        "Minimize active plugins; audit quarterly",
        "Use staging environment for major changes",
        "Implement daily automated backups",
        "Configure SSL certificate and force HTTPS",
        "Set custom 404 page with search and popular links",
        "Limit post revisions or use revision management plugin",
        "Use child theme for customizations",
        "Disable XML-RPC if not needed",
        "Configure wp-cron or server cron for reliability",
        "Set proper file permissions (755 dirs, 644 files)",
        "Use security plugin with login attempt limiting",
        "Enable two-factor authentication for admin accounts",
        "Remove default 'admin' username",
        "Customize login URL if supported by security plugin",
        "Audit user roles; follow principle of least privilege",
        "Test site health in Site Health dashboard monthly",
    ]
    technical = [
        "Verify HTTPS across all pages with valid certificate",
        "Fix all 404 errors or implement 301 redirects",
        "Eliminate redirect chains longer than one hop",
        "Resolve duplicate content with canonical tags or redirects",
        "Ensure robots.txt does not block important resources or pages",
        "Submit and validate XML sitemap",
        "Check index coverage for soft 404s",
        "Implement hreflang for multilingual sites",
        "Optimize Core Web Vitals: LCP under 2.5s, INP under 200ms, CLS under 0.1",
        "Eliminate render-blocking CSS and JavaScript above the fold",
        "Enable compression (Gzip or Brotli) on server",
        "Use CDN for static assets",
        "Implement proper cache headers",
        "Fix broken internal and external links",
        "Ensure mobile-responsive design passes Mobile-Friendly Test",
        "Validate structured data across all templates",
        "Audit JavaScript rendering with URL Inspection tool",
        "Implement pagination best practices for archives",
        "Control faceted navigation with noindex or canonical rules",
        "Monitor crawl stats in Search Console",
        "Analyze server log files for crawl efficiency quarterly",
        "Set preferred domain (www vs non-www) consistently",
        "Implement security headers (HSTS, CSP where feasible)",
        "Ensure page speed score above 90 on mobile PageSpeed Insights",
        "Fix orphan pages by adding internal links",
        "Limit crawl waste on infinite scroll and filter combinations",
        "Use 301 for permanent URL changes during migrations",
        "Maintain clean URL structure without unnecessary parameters",
        "Test site after plugin updates for broken schema or redirects",
        "Document technical SEO baseline before and after changes",
    ]
    ai_content = [
        "Define human editor responsible for every AI-assisted publish",
        "Create brand voice and style guide for AI prompts",
        "Never publish raw AI output without fact-checking",
        "Verify all statistics, dates, and claims against primary sources",
        "Add original examples, case studies, and screenshots",
        "Disclose AI assistance where required by platform or law",
        "Use AI for outlines and drafts, not final expert opinions on YMYL",
        "Run plagiarism and AI detection checks on sensitive content",
        "Ensure content passes E-E-A-T review for your niche",
        "Customize prompts with entity names, audience, and intent",
        "Chunk long AI outputs into human-edited sections",
        "Add author bylines with real credentials on expert topics",
        "Include unique data, surveys, or proprietary insights",
        "Avoid mass-generating thin location or product pages",
        "Review for hallucinated citations and fake references",
        "Optimize AI content for humans first, algorithms second",
        "Use AI to scale research summaries, not replace subject expertise",
        "Implement content scoring rubric before publication",
        "Track performance of AI vs human-written content separately",
        "Update AI-generated content when facts change",
        "Maintain prompt library with version control",
        "Test readability scores (Flesch-Kincaid) for audience level",
        "Ensure diversity of sentence structure; avoid AI patterns",
        "Add multimedia (video, infographics) AI cannot replicate easily",
        "Document AI workflow for client transparency and compliance",
    ]
    body = (
        _checklist("SEO Master Checklist", seo)
        + _checklist("AEO (Answer Engine Optimization) Checklist", aeo)
        + _checklist("GEO (Generative Engine Optimization) Checklist", geo)
        + _checklist("WordPress SEO Checklist", wordpress)
        + _checklist("Technical SEO Checklist", technical)
        + _checklist("AI Content Production Checklist", ai_content)
    )
    return f'<section id="checklists"><h1>Master Checklists</h1><p>Use these checklists during audits, launches, and client deliverables.</p>{body}</section>'


def _slides_html():
    modules = [
        (1, "The Evolution of Search", [
            "Welcome & Course Roadmap", "A Brief History of Search Engines",
            "The PageRank Revolution", "How Google Works: Crawl-Index-Rank",
            "Crawling Deep Dive & Crawl Budget", "Indexing Explained",
            "Ranking Signals Overview", "Knowledge Graphs & Entities",
            "The Rise of AI Search Engines", "Traditional vs AI Search Comparison",
            "The Future of Search Landscape", "Module 1 Key Takeaways & Q&A",
        ]),
        (2, "WordPress Foundations", [
            "WordPress Architecture Overview", "Choosing SEO-Friendly Themes",
            "Essential Plugins Ecosystem", "Permalinks & URL Structure",
            "User Roles & Security Basics", "Staging & Deployment Workflow",
            "Site Health & Performance Baseline", "Media Library Best Practices",
            "Child Themes & Customization", "WordPress SEO Plugin Setup",
            "Hands-On: Configure a Clean WordPress Install", "Module 2 Summary",
        ]),
        (3, "SEO Fundamentals", [
            "What Is SEO in 2026?", "Search Intent Framework",
            "Keyword Research Methodology", "Tools: GSC, Ahrefs, Semrush Overview",
            "Competitive Analysis Basics", "SERP Feature Landscape",
            "Content-SEO Alignment", "Link Equity Fundamentals",
            "Measuring SEO Success", "Common Beginner Mistakes",
            "Building Your SEO Strategy Document", "Module 3 Review",
        ]),
        (4, "On-Page SEO Mastery", [
            "Title Tags & Meta Descriptions", "Heading Hierarchy & Content Structure",
            "Keyword Placement Without Stuffing", "Internal Linking Strategies",
            "Image & Media Optimization", "URL Slugs & Breadcrumbs",
            "Content Freshness & Updates", "On-Page Audit Walkthrough",
            "Optimizing Blog Posts vs Landing Pages", "Schema for On-Page Enhancement",
            "Live On-Page Optimization Demo", "Module 4 Checklist Review",
        ]),
        (5, "Technical SEO", [
            "Technical SEO Audit Framework", "Crawlability & robots.txt",
            "XML Sitemaps & Index Management", "Canonicalization & Duplicates",
            "Site Speed & Core Web Vitals", "Mobile-First Indexing",
            "JavaScript SEO Essentials", "HTTPS & Security Headers",
            "Structured Data Implementation", "Log File Analysis Intro",
            "Technical Issue Prioritization Matrix", "Module 5 Lab Preview",
        ]),
        (6, "Advanced Content Strategy", [
            "Topical Authority & Content Clusters", "Pillar Page Architecture",
            "Content Gap Analysis", "Editorial Calendar Planning",
            "Content Decay & Refresh Cycles", "E-E-A-T for Content Teams",
            "Information Gain Strategy", "Multimedia Content Integration",
            "Content Promotion & Distribution", "Measuring Content ROI",
            "Case Study: Cluster That Ranked", "Module 6 Action Items",
        ]),
        (7, "Local SEO", [
            "Local Search Ecosystem", "Google Business Profile Optimization",
            "NAP Consistency & Citations", "Local Landing Page Templates",
            "Reviews & Reputation Management", "Local Schema Markup",
            "Multi-Location SEO Strategy", "Local Link Building",
            "Tracking Local Rankings", "Service Area Business Tactics",
            "Local SEO Audit Demo", "Module 7 Wrap-Up",
        ]),
        (8, "Entity SEO", [
            "Entities vs Keywords", "Knowledge Graph Mechanics",
            "Entity Research Tools", "SameAs & Organization Schema",
            "Building Entity Home Pages", "Wikidata & Wikipedia Strategy",
            "Brand SERP Optimization", "Entity-Based Internal Linking",
            "Disambiguation Best Practices", "Entity Audit Workshop Intro",
            "Measuring Entity Visibility", "Module 8 Summary",
        ]),
        (9, "Answer Engine Optimization (AEO)", [
            "What Is AEO?", "Featured Snippets Deep Dive",
            "People Also Ask Optimization", "Voice Search & Speakable Schema",
            "FAQ & HowTo Schema", "Answer Formatting Patterns",
            "Zero-Click Search Strategy", "AEO Measurement Framework",
            "Bing Copilot & AI Overview Differences", "AEO Content Templates",
            "Live Snippet Capture Exercise", "Module 9 Key Points",
        ]),
        (10, "Generative Engine Optimization (GEO)", [
            "GEO Defined & Why It Matters", "How AI Engines Select Sources",
            "Citation vs Ranking Metrics", "Brand Authority for AI Visibility",
            "Content Structures AI Prefers", "Monitoring AI Citations",
            "Competitor Citation Analysis", "GEO Content Refresh Strategy",
            "Robots.txt & AI Crawlers", "Building Quotable Assets",
            "GEO Reporting Dashboard", "Module 10 Discussion",
        ]),
        (11, "AI Content Production", [
            "AI Content Ethics & Guidelines", "Prompt Engineering for SEO",
            "Human-in-the-Loop Workflows", "Fact-Checking AI Output",
            "Brand Voice Customization", "AI Tools Landscape Overview",
            "Scaling Content Without Quality Loss", "YMYL & AI Risk Management",
            "AI Content Performance Tracking", "Editing AI Drafts Efficiently",
            "Building a Content QA Rubric", "Module 11 Best Practices",
        ]),
        (12, "Programmatic SEO", [
            "Programmatic SEO Use Cases", "Template Design Principles",
            "Data Sources & Quality Control", "WordPress Custom Post Types at Scale",
            "Avoiding Thin Content Penalties", "Internal Linking Automation",
            "Indexation Management for Large Sites", "Monitoring Programmatic Pages",
            "Case Study: Location Pages Done Right", "Case Study: Programmatic Failures",
            "Build vs Buy Decision Framework", "Module 12 Planning Exercise",
        ]),
        (13, "n8n SEO Automation", [
            "Introduction to n8n", "SEO Workflows Overview",
            "Connecting GSC & Analytics APIs", "Automated Rank Tracking",
            "Content Decay Alert Workflows", "Backlink Monitoring Automation",
            "Scheduled Site Health Checks", "Slack/Email Alert Configuration",
            "Error Handling in Workflows", "Building Your First SEO Workflow",
            "Workflow Documentation Standards", "Module 13 Demo",
        ]),
        (14, "Building SEO Agents", [
            "What Is an SEO Agent?", "Agent Architecture Components",
            "Tool Use & Function Calling", "RAG for SEO Knowledge Bases",
            "Monitoring Agent with Scheduled Tasks", "Content Brief Agent",
            "Technical Audit Agent Design", "Safety Guardrails & Human Approval",
            "Deploying Agents in Production", "Cost & Token Management",
            "Agent Evaluation Metrics", "Module 14 Capstone Preview",
        ]),
        (15, "Capstone Project", [
            "Capstone Requirements Overview", "Choosing Your Project Site",
            "Deliverable 1: Technical Audit Report", "Deliverable 2: Content Strategy",
            "Deliverable 3: AEO/GEO Plan", "Deliverable 4: Automation Workflow",
            "Deliverable 5: Agent or Tool Build", "Presentation Guidelines",
            "Peer Review Process", "Certification Exam Preparation",
            "Career Next Steps & Portfolio", "Course Completion Celebration",
        ]),
    ]
    parts = ['<section id="slides"><h1>Course Slides Outline</h1><p>Slide titles for instructor decks across all 15 modules.</p>']
    for mid, title, slides in modules:
        lis = "".join(f"<li>Slide {i+1}: {s}</li>" for i, s in enumerate(slides))
        parts.append(f'<h2 id="slides-module{mid}">Module {mid}: {title}</h2><ol>{lis}</ol>')
    parts.append("</section>")
    return "".join(parts)


def _workshops_html():
    workshops = [
        (1, "The Evolution of Search", "Analyze How Google, ChatGPT, Gemini, and Perplexity Answer the Same Query", "90 minutes", [
            "Choose 5 queries across intent types: informational, commercial, local, transactional, and comparison.",
            "Run each query on Google (note AI Overview), ChatGPT with browse, Gemini, and Perplexity.",
            "Record answer format, sources cited, brand mentions, and preferred content types.",
            "Identify citation patterns: who gets cited, who does not, and hypothesize why.",
            "Present findings in a 5-minute group discussion.",
        ], "Comparison spreadsheet plus 1-page citation pattern analysis."),
        (2, "WordPress Foundations", "Build a Production-Ready WordPress SEO Baseline", "120 minutes", [
            "Install WordPress locally or on staging with a lightweight theme.",
            "Configure permalinks, disable attachment pages, and install Rank Math or Yoast.",
            "Set up caching, SSL, and security hardening checklist items.",
            "Create sample posts and pages demonstrating proper heading structure.",
            "Export Site Health report and document baseline metrics.",
        ], "Configured staging site URL and baseline checklist PDF."),
        (3, "SEO Fundamentals", "Keyword Research & Intent Mapping Sprint", "90 minutes", [
            "Select a niche site or hypothetical business provided by instructor.",
            "Use GSC, AnswerThePublic, and one paid tool to gather 50+ keywords.",
            "Classify each keyword by intent and funnel stage.",
            "Map top 20 keywords to existing or proposed URL slugs.",
            "Present intent map to partner for peer review.",
        ], "Keyword spreadsheet with intent labels and URL mapping."),
        (4, "On-Page SEO Mastery", "Live On-Page Optimization Challenge", "75 minutes", [
            "Instructor provides an underoptimized WordPress page.",
            "Teams rewrite title, meta, H1, first paragraph, and internal links.",
            "Add FAQ section targeting PAA queries for the topic.",
            "Implement basic Article schema via SEO plugin.",
            "Compare before/after using on-page checklist scoring.",
        ], "Before/after document with checklist score improvement."),
        (5, "Technical SEO", "Technical Audit Scavenger Hunt", "120 minutes", [
            "Audit a provided problematic site (staging) using Screaming Frog or Sitebulb.",
            "Find and document at least 10 technical issues across crawl, index, speed, and schema.",
            "Prioritize issues using impact vs effort matrix.",
            "Write remediation steps for top 5 issues.",
            "Present one critical fix live to class.",
        ], "Technical audit report (5–10 pages) with prioritized action plan."),
        (6, "Advanced Content Strategy", "Design a Content Cluster from Scratch", "90 minutes", [
            "Choose a pillar topic relevant to your capstone or sample business.",
            "Define one pillar page and 8 cluster articles with working titles.",
            "Draw internal linking diagram showing hub-and-spoke relationships.",
            "Identify content gaps vs top 3 ranking competitors.",
            "Create 30-day publishing schedule for cluster rollout.",
        ], "Cluster map diagram and editorial calendar."),
        (7, "Local SEO", "Google Business Profile Optimization Lab", "60 minutes", [
            "Claim or use demo GBP listing provided by instructor.",
            "Complete all profile fields, categories, services, and attributes.",
            "Write keyword-rich business description within guidelines.",
            "Upload geotagged photos and create first Google post.",
            "Audit NAP consistency across 3 directories.",
        ], "GBP screenshot set and NAP consistency report."),
        (8, "Entity SEO", "Entity Mapping & Schema Workshop", "90 minutes", [
            "Research your brand or sample brand in Google Knowledge Panel.",
            "Document related entities using Google NLP API or manual SERP analysis.",
            "Build Organization schema with sameAs links to official profiles.",
            "Create entity home page outline with disambiguation content.",
            "Validate markup with Rich Results Test.",
        ], "Entity map document and validated JSON-LD snippet."),
        (9, "Answer Engine Optimization (AEO)", "Featured Snippet Capture Lab", "75 minutes", [
            "Identify 10 snippet opportunities from GSC query data.",
            "Rewrite answer blocks in 40–60 word format with matching H2 questions.",
            "Add FAQ schema to at least 3 pages.",
            "Test queries in Google and record snippet ownership before/after.",
            "Document which formats won: paragraph, list, or table.",
        ], "Snippet tracking sheet with optimization notes."),
        (10, "Generative Engine Optimization (GEO)", "AI Citation Audit & Gap Plan", "90 minutes", [
            "Run 15 brand and category queries across Perplexity, ChatGPT, and Gemini.",
            "Log every citation: URL, brand mentioned, competitor cited instead.",
            "Analyze content attributes of cited pages vs your content.",
            "Draft GEO improvement plan with 5 specific content actions.",
            "Set up monthly citation tracking spreadsheet.",
        ], "AI citation audit report and 90-day GEO plan."),
        (11, "AI Content Production", "Human-in-the-Loop Content Pipeline", "120 minutes", [
            "Receive content brief for 1,500-word article on assigned topic.",
            "Generate outline and draft using approved AI tool with custom prompt.",
            "Fact-check every claim; replace hallucinations with verified sources.",
            "Add original intro, examples, and expert commentary.",
            "Score final piece against AI content checklist before publish.",
        ], "Published or staged article with annotated edit log."),
        (12, "Programmatic SEO", "Template Design for Scalable Pages", "90 minutes", [
            "Choose programmatic use case: locations, integrations, or comparisons.",
            "Design URL pattern and template wireframe with unique value sections.",
            "Define minimum data fields required per page to avoid thin content.",
            "Mock up 3 sample pages with real data.",
            "Write indexation rules and quality gate checklist.",
        ], "Template spec document and 3 sample page HTML exports."),
        (13, "n8n SEO Automation", "Build an SEO Monitoring Workflow", "120 minutes", [
            "Set up n8n locally or cloud instance.",
            "Connect Google Search Console API or CSV export trigger.",
            "Build workflow: detect 20%+ traffic drop on any page → Slack alert.",
            "Add error handling and weekly summary email node.",
            "Document workflow with screenshot and node descriptions.",
        ], "Exported n8n workflow JSON and setup documentation."),
        (14, "Building SEO Agents", "Deploy a Content Brief Agent", "120 minutes", [
            "Define agent goal: generate SEO content brief from keyword input.",
            "Connect LLM with tools: SERP scraper or manual input, GSC export.",
            "Implement structured output: intent, outline, entities, word count.",
            "Add human approval step before brief delivery.",
            "Test with 3 keywords and refine prompts.",
        ], "Working agent demo and prompt documentation."),
        (15, "Capstone Project", "Capstone Milestone Review & Peer Critique", "180 minutes", [
            "Present 10-minute capstone progress: site, audit summary, strategy outline.",
            "Receive structured peer feedback using certification rubric criteria.",
            "Identify gaps before final submission.",
            "Create 2-week completion timeline with deliverable owners.",
            "Schedule instructor office hours for blockers.",
        ], "Revised capstone plan incorporating peer and instructor feedback."),
    ]
    parts = ['<section id="workshops"><h1>Workshop Instructions Master Document</h1><p>Consolidated instructions for all 15 module workshops.</p>']
    for mid, mod_title, wtitle, duration, steps, deliverable in workshops:
        steps_html = "".join(f"<li>{s}</li>" for s in steps)
        parts.append(f"""
<h2>Module {mid} Workshop: {wtitle}</h2>
<p><strong>Module:</strong> {mod_title} | <strong>Duration:</strong> {duration}</p>
<h4>Materials Required</h4>
<ul><li>Laptop with internet access</li><li>Course checklist printout or digital copy</li><li>Access to WordPress staging site (Modules 2+)</li><li>Spreadsheet software</li></ul>
<h4>Step-by-Step Instructions</h4>
<ol>{steps_html}</ol>
<h4>Deliverable</h4>
<p>{deliverable}</p>
<h4>Instructor Notes</h4>
<ul>
<li>Circulate during steps 2–3 to catch common errors early.</li>
<li>Pair struggling students with advanced peers for steps requiring tool setup.</li>
<li>Allow 10-minute buffer for Q&amp;A before deliverable submission.</li>
<li>Collect deliverables via LMS or shared folder for async review.</li>
</ul>
<hr>""")
    parts.append("</section>")
    return "".join(parts)


def _rubrics_html():
    return """
<section id="rubrics">
<h1>Assessment Rubrics</h1>

<h2>Module Quiz Rubric (Applies to All 15 Modules)</h2>
<table>
<tr><th>Criterion</th><th>Excellent (90–100%)</th><th>Proficient (75–89%)</th><th>Developing (60–74%)</th><th>Inadequate (&lt;60%)</th></tr>
<tr><td>Accuracy</td><td>9–10 of 10 correct with clear understanding</td><td>8 of 10 correct; minor misconceptions</td><td>6–7 of 10 correct</td><td>Below 6 correct; fundamental gaps</td></tr>
<tr><td>Application</td><td>Explains why answers are correct with examples</td><td>Most explanations adequate</td><td>Limited explanation quality</td><td>Cannot explain reasoning</td></tr>
<tr><td>Completion</td><td>Submitted on time with all questions attempted</td><td>Submitted on time; 1–2 blank</td><td>Late or incomplete</td><td>Not submitted</td></tr>
</table>
<p><strong>Pass threshold:</strong> 75% (8/10) per module quiz.</p>

<h2>Workshop Deliverable Rubric</h2>
<table>
<tr><th>Criterion</th><th>Points</th><th>Description</th></tr>
<tr><td>Completeness</td><td>25</td><td>All workshop steps addressed in deliverable</td></tr>
<tr><td>Technical Accuracy</td><td>25</td><td>SEO/AEO/GEO recommendations are correct and current</td></tr>
<tr><td>Analysis Depth</td><td>20</td><td>Insights go beyond surface observations</td></tr>
<tr><td>Documentation Quality</td><td>15</td><td>Clear formatting, labels, and reproducible steps</td></tr>
<tr><td>Presentation</td><td>15</td><td>Oral or written summary is organized and professional</td></tr>
</table>
<p><strong>Pass threshold:</strong> 70/100 on workshop deliverables.</p>

<h2>Participation Rubric</h2>
<table>
<tr><th>Level</th><th>Points</th><th>Behaviors</th></tr>
<tr><td>Exemplary</td><td>10</td><td>Active in discussions, helps peers, asks insightful questions every session</td></tr>
<tr><td>Active</td><td>8</td><td>Regular participation, completes in-class exercises</td></tr>
<tr><td>Moderate</td><td>6</td><td>Present but minimal engagement</td></tr>
<tr><td>Minimal</td><td>4</td><td>Rarely participates; often distracted</td></tr>
<tr><td>Absent</td><td>0</td><td>Did not attend session</td></tr>
</table>
<p>Participation scored per module session; cumulative average must be ≥7/10.</p>

<h2>Homework Assignment Rubric</h2>
<table>
<tr><th>Criterion</th><th>Weight</th><th>Exemplary</th><th>Needs Improvement</th></tr>
<tr><td>Content Quality</td><td>40%</td><td>Demonstrates mastery with original analysis</td><td>Generic or copied content without attribution</td></tr>
<tr><td>Requirements Met</td><td>30%</td><td>Word count, diagrams, citations all present</td><td>Missing required elements</td></tr>
<tr><td>Writing &amp; Clarity</td><td>20%</td><td>Professional, structured, error-free</td><td>Hard to follow; frequent errors</td></tr>
<tr><td>Timeliness</td><td>10%</td><td>On time</td><td>Late without approved extension</td></tr>
</table>

<h2>Grading Weight Summary</h2>
<ul>
<li>Module quizzes (15 × 10 questions): 25% of course grade</li>
<li>Workshop deliverables (15): 35% of course grade</li>
<li>Certification exam (100 questions): 25% of course grade</li>
<li>Capstone project: 10% of course grade</li>
<li>Participation: 5% of course grade</li>
</ul>
</section>
"""


def _exam_questions():
    """Return list of (module, question, options, correct_index 0-based)."""
    return [
        # Module 1 (7 questions)
        (1, "What three stages does Google use to process web pages?",
         ["Fetch, Store, Display", "Crawl, Index, Rank", "Scan, Parse, Serve", "Discover, Cache, Return"], 1),
        (1, "Google's PageRank algorithm primarily measures:",
         ["Page load speed", "Link-based authority", "Keyword density", "Social shares"], 1),
        (1, "Which file instructs crawlers which paths not to request?",
         ["sitemap.xml", "htaccess.conf", "robots.txt", "canonical.html"], 2),
        (1, "The Knowledge Graph stores:",
         ["Only keyword frequencies", "Entities and their relationships", "User passwords", "Ad auction data"], 1),
        (1, "An entity differs from a keyword because an entity:",
         ["Is always longer than 5 words", "Represents a real-world thing with attributes", "Only appears in paid search", "Cannot appear in schema"], 1),
        (1, "AI Overviews in Google search are best described as:",
         ["Paid advertisements", "AI-synthesized answers with citations", "User-generated forums", "Image carousels only"], 1),
        (1, "Blocking CSS in robots.txt is harmful because:",
         ["It improves crawl budget", "Google needs CSS to render pages properly", "It increases PageRank", "CSS files contain keywords"], 1),
        # Module 2 (7)
        (2, "The recommended WordPress permalink structure for SEO is:",
         ["Plain (?p=123)", "Day and name", "Post name", "Numeric"], 2),
        (2, "Attachment pages in WordPress should typically be:",
         ["Noindexed or redirected", "Promoted in navigation", "Used as landing pages", "Submitted separately in sitemap"], 0),
        (2, "A child theme is used to:",
         ["Disable plugins", "Preserve customizations during theme updates", "Speed up database queries", "Replace wp-admin"], 1),
        (2, "Which is NOT a recommended security practice for WordPress?",
         ["Two-factor authentication", "Using default 'admin' username", "Regular plugin updates", "Login attempt limiting"], 1),
        (2, "LiteSpeed Cache or WP Rocket primarily improve:",
         ["Keyword rankings directly", "Page load performance via caching", "Backlink acquisition", "Schema validation"], 1),
        (2, "Site Health in WordPress dashboard reports on:",
         ["Only SEO plugin settings", "Performance, security, and configuration", "Competitor rankings", "Social media followers"], 1),
        (2, "For a single-author blog, author archive pages should usually be:",
         ["Noindexed to prevent thin duplicates", "Promoted heavily", "Used as category pages", "Blocked in sitemap only"], 0),
        # Module 3 (7)
        (3, "Informational search intent indicates the user wants to:",
         ["Complete a purchase immediately", "Learn or answer a question", "Navigate to a specific brand site", "Compare two products only"], 1),
        (3, "Keyword cannibalization occurs when:",
         ["One page targets many keywords", "Multiple pages compete for the same query", "Keywords are too long-tail", "No keywords are used"], 1),
        (3, "Google Search Console is primarily used for:",
         ["Writing blog posts", "Monitoring indexing and search performance", "Sending email campaigns", "Managing social ads"], 1),
        (3, "A long-tail keyword typically has:",
         ["Higher volume and broad intent", "Lower volume and more specific intent", "No search volume", "Only navigational intent"], 1),
        (3, "Topical authority is built by:",
         ["Publishing one viral post", "Comprehensive coverage of a subject area", "Buying expired domains", "Hiding content from crawlers"], 1),
        (3, "CTR in SEO context measures:",
         ["Server response time", "Clicks divided by impressions", "Bounce rate", "Pages per session"], 1),
        (3, "Competitive SERP analysis should include:",
         ["Only your own site metrics", "Content format, length, and features of top results", "Random unrelated niches", "Only paid ad copy"], 1),
        # Module 4 (7)
        (4, "The ideal number of H1 tags per page is:",
         ["Zero", "One", "Three", "As many as needed"], 1),
        (4, "Title tags should generally stay under:",
         ["30 characters", "60 characters", "120 characters", "200 characters"], 1),
        (4, "Meta descriptions directly impact rankings because:",
         ["They are the strongest ranking factor", "They do not directly impact rankings but affect CTR", "Google copies them into H1 tags", "They replace schema markup"], 1),
        (4, "Internal links primarily help by:",
         ["Replacing backlinks entirely", "Distributing authority and providing context", "Blocking crawlers", "Creating duplicate content"], 1),
        (4, "Image alt text should:",
         ["Stuff keywords repeatedly", "Describe the image meaningfully", "Be left empty always", "Match the filename only"], 1),
        (4, "Breadcrumb schema helps search engines understand:",
         ["Page hierarchy and navigation path", "Server location", "User passwords", "Ad targeting"], 0),
        (4, "Keyword stuffing is:",
         ["Recommended for H2 tags", "Unnatural repetition that harms quality", "Required for featured snippets", "Same as semantic SEO"], 1),
        # Module 5 (7)
        (5, "A 301 redirect indicates:",
         ["Temporary move", "Permanent move", "Page not found", "Server error"], 1),
        (5, "Core Web Vitals include LCP, INP, and:",
         ["CTR", "CLS", "RPM", "DNS"], 1),
        (5, "rel=canonical is used to:",
         ["Block all crawlers", "Specify preferred URL among duplicates", "Increase crawl budget", "Hide content from users"], 1),
        (5, "A soft 404 occurs when:",
         ["Server returns 404 correctly", "Page returns 200 but shows not-found content", "Redirect chain exists", "HTTPS is missing"], 1),
        (5, "Mobile-first indexing means Google primarily uses:",
         ["Desktop version for ranking", "Mobile version for indexing and ranking", "AMP only", "PDF versions"], 1),
        (5, "hreflang tags are essential for:",
         ["Single-language sites", "Multilingual and multi-regional targeting", "Blocking AI crawlers", "Image optimization"], 1),
        (5, "Log file analysis reveals:",
         ["Social media engagement", "How search engine bots crawl your site", "Email open rates", "Ad quality scores"], 1),
        # Module 6 (7)
        (6, "A pillar page in content strategy is:",
         ["A short FAQ with one question", "Comprehensive hub covering a broad topic", "A 404 error page", "An admin dashboard"], 1),
        (6, "Content decay refers to:",
         ["Gradual traffic loss as content ages", "Server cache expiration", "Plugin deactivation", "Domain expiration"], 0),
        (6, "Information gain means:",
         ["Copying competitor content", "Adding unique value beyond existing results", "Increasing word count only", "Removing internal links"], 1),
        (6, "E-E-A-T stands for:",
         ["Engagement, Efficiency, Authority, Trust", "Experience, Expertise, Authoritativeness, Trustworthiness", "Entity, Engine, Algorithm, Tracking", "Edit, Export, Analyze, Test"], 1),
        (6, "Content clusters connect:",
         ["Unrelated topics randomly", "Pillar pages to related subtopic articles", "Only external domains", "Social profiles only"], 1),
        (6, "An editorial calendar helps teams:",
         ["Avoid all keyword research", "Plan publishing aligned with strategy and seasonality", "Disable analytics", "Remove old content automatically"], 1),
        (6, "YMYL topics require especially strong:",
         ["Humor and memes", "E-E-A-T signals", "Pop-up ads", "Auto-play video"], 1),
        # Module 7 (7)
        (7, "NAP in local SEO stands for:",
         ["Name, Address, Phone", "Network, API, Plugin", "Navigation, Analytics, Page", "New, Active, Published"], 0),
        (7, "Google Business Profile primarily affects:",
         ["Local pack and map results", "Only paid shopping ads", "Email deliverability", "DNS records"], 0),
        (7, "Local landing pages should include:",
         ["Generic national copy only", "City-specific content and local signals", "No contact information", "Hidden addresses"], 1),
        (7, "Review management best practice is to:",
         ["Ignore negative reviews", "Respond professionally to all reviews", "Delete all negative reviews", "Buy fake 5-star reviews"], 1),
        (7, "LocalBusiness schema helps with:",
         ["Rich local results and entity clarity", "Blocking competitors", "Increasing crawl budget artificially", "Removing GBP listing"], 0),
        (7, "Citation consistency means:",
         ["Matching business info across directories", "Copying competitor content", "Using different phone numbers per site", "Random NAP variations"], 0),
        (7, "Service area businesses without storefronts should:",
         ["Hide location entirely from web", "Define service areas in GBP and content", "Use fake addresses", "Block local schema"], 1),
        # Module 8 (7)
        (8, "Entity SEO focuses on:",
         ["Keyword density only", "Recognition and disambiguation of real-world things", "Paid ad copy", "Email subject lines"], 1),
        (8, "sameAs schema property links an entity to:",
         ["Competitor websites", "Official social and reference profiles", "Random URLs", "Noindex pages"], 1),
        (8, "Knowledge Panels appear when Google has high confidence in:",
         ["Entity identity and data", "Keyword stuffing", "Pop-up usage", "Flash content"], 0),
        (8, "Wikidata is useful for entity SEO because:",
         ["It stores structured entity identifiers used across the web", "It replaces Google Search Console", "It hosts WordPress sites", "It blocks AI crawlers"], 0),
        (8, "Brand SERP optimization aims to:",
         ["Control perception when users search your brand name", "Rank for competitor trademarks illegally", "Hide all reviews", "Remove social profiles"], 0),
        (8, "Entity disambiguation is needed when:",
         ["A name refers to multiple distinct things", "Pages load slowly", "Images are missing alt text", "SSL expires"], 0),
        (8, "Topical maps in entity strategy show:",
         ["Only paid keywords", "Relationships between topics and content gaps", "Server error logs", "Social follower counts"], 1),
        # Module 9 (7)
        (9, "AEO primarily optimizes for:",
         ["Direct answers and featured snippets", "Print advertising", "Offline billboards", "DNS configuration"], 0),
        (9, "Featured snippet optimal answer length is often:",
         ["500–800 words in one block", "40–60 words concise paragraph", "One word only", "Entire page copied"], 1),
        (9, "FAQPage schema is used for:",
         ["Product inventory", "Question-and-answer content", "Login forms", "404 pages"], 1),
        (9, "People Also Ask boxes surface:",
         ["Related questions users search", "Only paid ads", "Random unrelated queries", "Server status codes"], 0),
        (9, "Zero-click searches mean users:",
         ["Never use search engines", "Get answers without clicking results", "Always click first result", "Only use voice"], 1),
        (9, "Speakable schema targets:",
         ["Voice assistant read-aloud content", "Image compression", "Redirect chains", "Database backups"], 0),
        (9, "HowTo schema is appropriate for:",
         ["Step-by-step instructional content", "Privacy policies only", "Login pages", "Empty archives"], 0),
        # Module 10 (7)
        (10, "GEO focuses on visibility in:",
         ["Generative AI search and citation", "Traditional print media only", "Fax marketing", "Radio ads"], 0),
        (10, "In GEO, success is often measured by:",
         ["Citations in AI-generated answers", "Billboard impressions", "Post office mail volume", "FTP transfer speed"], 0),
        (10, "Query fanout in AI search refers to:",
         ["Decomposing queries into sub-queries for retrieval", "Blocking all crawlers", "Deleting sitemap", "Removing H1 tags"], 0),
        (10, "GPTBot robots.txt directive controls:",
         ["Whether OpenAI's crawler may access your site", "Google Ads billing", "WordPress updates", "Email SMTP"], 0),
        (10, "AI engines often prefer sources that:",
         ["Provide clear, citable facts with authority", "Use hidden text", "Cloak content", "Have no dates"], 0),
        (10, "Share of voice in GEO tracks:",
         ["Brand citation frequency vs competitors in AI answers", "Office square footage", "Plugin count only", "Theme color"], 0),
        (10, "RAG in AI search combines:",
         ["Retrieval of sources with generative answers", "Random ads with email", "Only image generation", "Database deletion with caching"], 0),
        # Module 11 (6)
        (11, "Human-in-the-loop AI content workflow requires:",
         ["Publishing raw AI output without review", "Human editing and fact-checking before publish", "No editorial oversight", "Automatic deletion of drafts"], 1),
        (11, "AI hallucination refers to:",
         ["Plausible but false generated information", "Improved page speed", "Valid schema markup", "Correct citations always"], 0),
        (11, "For YMYL topics, AI content should:",
         ["Replace all expert review", "Be reviewed by qualified humans with credentials", "Never cite sources", "Use anonymous authors"], 1),
        (11, "Prompt engineering for SEO should include:",
         ["Intent, audience, entities, and format requirements", "Random characters only", "No context", "Competitor passwords"], 0),
        (11, "Brand voice guides help AI by:",
         ["Ensuring consistent tone and terminology", "Blocking all crawlers", "Removing meta tags", "Disabling SSL"], 0),
        (11, "Mass-producing thin AI pages typically:",
         ["Build sustainable rankings", "Risks quality penalties and poor UX", "Guarantees featured snippets", "Replaces technical SEO"], 1),
        # Module 12 (6)
        (12, "Programmatic SEO generates pages by:",
         ["Templates plus structured data at scale", "Manual writing only", "Deleting sitemaps", "Blocking indexing"], 0),
        (12, "Primary risk of programmatic SEO is:",
         ["Too much unique content", "Thin, duplicate, or low-value pages at scale", "Excessive E-E-A-T", "Too few URLs"], 1),
        (12, "Quality gates for programmatic pages should require:",
         ["Minimum unique content per URL", "Identical copy on all pages", "No internal links", "Random noindex on homepage"], 0),
        (12, "Location page templates need unique value such as:",
         ["Local facts, testimonials, or service details", "Copied city names only", "Hidden competitor content", "Empty body text"], 0),
        (12, "Indexation management for large programmatic sites involves:",
         ["Monitoring coverage and pruning low performers", "Indexing every URL blindly", "Removing all canonicals", "Blocking sitemap"], 0),
        (12, "Custom post types in WordPress can support programmatic SEO by:",
         ["Structuring repeatable content types with fields", "Disabling permalinks", "Removing all plugins", "Blocking REST API always"], 0),
        # Module 13 (6)
        (13, "n8n is primarily used for:",
         ["Workflow automation connecting apps and APIs", "WordPress theme design only", "Physical server hardware", "Domain registration"], 0),
        (13, "Automated rank tracking workflow might trigger when:",
         ["Position drops beyond defined threshold", "Site theme color changes", "User logs into wp-admin", "SSL renews automatically"], 0),
        (13, "Content decay alerts help teams:",
         ["Identify pages losing traffic for refresh", "Delete all blog posts", "Disable Search Console", "Remove schema"], 0),
        (13, "Error handling in n8n workflows should:",
         ["Notify team and log failures", "Fail silently always", "Delete production database", "Block all email"], 0),
        (13, "GSC API integration in automation enables:",
         ["Scheduled performance data pulls", "Guaranteed page-one rankings", "Automatic link buying", "Removal of competitors"], 0),
        (13, "SEO automation documentation should include:",
         ["Trigger, nodes, credentials scope, and alert recipients", "Admin passwords in plain text", "No version history", "Random emoji only"], 0),
        # Module 14 (6)
        (14, "An SEO agent differs from a simple chatbot by:",
         ["Using tools, memory, and multi-step task execution", "Only returning static FAQs", "Cannot access data", "Replacing all human SEO"], 0),
        (14, "Function calling in agents allows:",
         ["LLM to invoke APIs and structured tools", "Unlimited free rankings", "Automatic hacking", "Removal of HTTPS"], 0),
        (14, "RAG for SEO agents provides:",
         ["Retrieved domain knowledge to ground responses", "Random hallucinations only", "No source attribution", "Blocked indexing"], 0),
        (14, "Human approval gates in agents are important for:",
         ["Preventing unchecked automated changes", "Speeding up all publishes without review", "Deleting backups", "Disabling analytics"], 0),
        (14, "Token cost management for agents includes:",
         ["Monitoring usage and optimizing prompts", "Ignoring all API bills", "Running infinite loops", "Maximizing context always"], 0),
        (14, "Agent evaluation metrics should track:",
         ["Accuracy, completion rate, and human override frequency", "Only social likes", "Office temperature", "Theme font size"], 0),
        # Module 15 (6)
        (15, "The capstone project demonstrates:",
         ["Integrated application of SEO, AEO, GEO, WordPress, and automation skills", "Only theoretical knowledge", "Unrelated hobby projects", "Plugin installation only"], 0),
        (15, "Capstone technical audit should prioritize issues by:",
         ["Impact on crawl, index, and user experience", "Alphabetical URL order", "Random selection", "Theme color contrast only"], 0),
        (15, "Certification requires passing the exam with minimum score of:",
         ["50%", "70%", "80%", "100%"], 2),
        (15, "Peer review in capstone helps students:",
         ["Identify gaps using structured rubric feedback", "Avoid all criticism", "Skip final deliverables", "Copy others' work"], 0),
        (15, "A complete SEO operating system includes:",
         ["WordPress hub, entities, technical excellence, automation, and agents", "Only paid ads", "Social media alone", "No measurement"], 0),
        (15, "Final presentation should cover:",
         ["Strategy, implementation, results, and lessons learned", "Personal unrelated stories only", "No data or metrics", "Competitor confidential data"], 0),
    ]


def _exam_html():
    questions = _exam_questions()
    assert len(questions) == 100, f"Expected 100 exam questions, got {len(questions)}"
    parts = ['<section id="exam"><h1>Certification Exam — 100 Questions</h1>',
             '<p>Multiple choice, 4 options each. Passing score: 80%. Organized by module.</p>']
    current_mod = 0
    qnum = 0
    answers = []
    for mod, qtext, options, correct in questions:
        if mod != current_mod:
            if current_mod:
                parts.append("</ol>")
            current_mod = mod
            parts.append(f"<h2>Module {mod} Questions</h2><ol>")
        qnum += 1
        labels = ["A", "B", "C", "D"]
        opts = "".join(f"<li>({labels[i]}) {o}</li>" for i, o in enumerate(options))
        parts.append(f"<li value=\"{qnum}\"><strong>Q{qnum}.</strong> {qtext}<ul>{opts}</ul></li>")
        answers.append((qnum, labels[correct]))
    parts.append("</ol>")
    key_items = "".join(f"<li>Q{n}: {a}</li>" for n, a in answers)
    parts.append(f"<h2>Answer Key</h2><ol>{key_items}</ol></section>")
    return "".join(parts)


def _cert_rubric_html():
    return """
<section id="cert-rubric">
<h1>Final Certification Project Rubric</h1>
<p>The capstone is worth 10% of the course grade. Students must score ≥70/100 to pass the project component. Combined with exam (≥80%) and module requirements, this qualifies for certification.</p>

<h2>Deliverable Overview</h2>
<table>
<tr><th>#</th><th>Deliverable</th><th>Weight</th></tr>
<tr><td>1</td><td>Technical SEO Audit Report</td><td>20%</td></tr>
<tr><td>2</td><td>Content Strategy &amp; Cluster Map</td><td>20%</td></tr>
<tr><td>3</td><td>AEO/GEO Optimization Plan</td><td>15%</td></tr>
<tr><td>4</td><td>n8n Automation Workflow (exported JSON + docs)</td><td>15%</td></tr>
<tr><td>5</td><td>SEO Agent or AI Tool Build</td><td>15%</td></tr>
<tr><td>6</td><td>Final Presentation &amp; Executive Summary</td><td>15%</td></tr>
</table>

<h2>Detailed Scoring Criteria</h2>

<h3>1. Technical SEO Audit Report (20 points)</h3>
<table>
<tr><th>Score</th><th>Crawl &amp; Index (5)</th><th>Performance (5)</th><th>Architecture (5)</th><th>Documentation (5)</th></tr>
<tr><td>5</td><td>All major issues identified with evidence</td><td>CWV measured with tools; fixes prioritized</td><td>URL structure, schema, mobile fully analyzed</td><td>Professional report with screenshots and URLs</td></tr>
<tr><td>3</td><td>Most issues found; minor gaps</td><td>Some metrics; generic recommendations</td><td>Partial architecture review</td><td>Readable but incomplete evidence</td></tr>
<tr><td>1</td><td>Superficial or incorrect findings</td><td>No measurements</td><td>Missing key areas</td><td>Disorganized or missing data</td></tr>
</table>

<h3>2. Content Strategy &amp; Cluster Map (20 points)</h3>
<table>
<tr><th>Score</th><th>Keyword/Intent Research (5)</th><th>Cluster Design (5)</th><th>Editorial Plan (5)</th><th>E-E-A-T Alignment (5)</th></tr>
<tr><td>5</td><td>Data-driven keyword set with intent labels</td><td>Clear pillar + 8+ clusters with internal links</td><td>Realistic 90-day calendar with owners</td><td>YMYL considerations addressed if applicable</td></tr>
<tr><td>3</td><td>Adequate keywords; some intent gaps</td><td>Cluster present but linking weak</td><td>Calendar lacks detail</td><td>Generic E-E-A-T mentions</td></tr>
<tr><td>1</td><td>No research evident</td><td Random topics without hub</td><td>No calendar</td><td>Ignores quality guidelines</td></tr>
</table>

<h3>3. AEO/GEO Optimization Plan (15 points)</h3>
<table>
<tr><th>Score</th><th>Snippet/AEO Tactics (5)</th><th>GEO Citation Strategy (5)</th><th>Measurement Plan (5)</th></tr>
<tr><td>5</td><td>Specific pages/formats for featured snippets and FAQ schema</td><td>AI citation audit completed with actionable gaps</td><td>KPIs, tools, and monthly review process defined</td></tr>
<tr><td>3</td><td>Generic AEO advice</td><td>Surface-level GEO ideas</td><td>Vague metrics</td></tr>
<tr><td>1</td><td>AEO/GEO confused or absent</td><td>No competitor/citation analysis</td><td>No measurement</td></tr>
</table>

<h3>4. n8n Automation Workflow (15 points)</h3>
<table>
<tr><th>Score</th><th>Functionality (5)</th><th>Reliability (5)</th><th>Documentation (5)</th></tr>
<tr><td>5</td><td>Workflow runs end-to-end; solves real SEO task</td><td>Error handling and alerts configured</td><td>Setup guide, credentials scope, and diagram included</td></tr>
<tr><td>3</td><td>Partially working workflow</td><td>Minimal error handling</td><td>Incomplete docs</td></tr>
<tr><td>1</td><td>Non-functional or unrelated to SEO</td><td>No testing evidence</td><td>Missing documentation</td></tr>
</table>

<h3>5. SEO Agent or AI Tool Build (15 points)</h3>
<table>
<tr><th>Score</th><th>Design (5)</th><th>Execution (5)</th><th>Safety &amp; Quality (5)</th></tr>
<tr><td>5</td><td>Clear agent purpose, tools, and human approval gates</td><td>Demo successful on 3+ test cases</td><td>Guardrails prevent harmful auto-publish; outputs verified</td></tr>
<tr><td>3</td><td>Basic chatbot without tools</td><td>Limited demo</td><td>Weak oversight</td></tr>
<tr><td>1</td><td>No working agent</td><td>Cannot demonstrate</td><td>Unsafe automation</td></tr>
</table>

<h3>6. Final Presentation &amp; Executive Summary (15 points)</h3>
<table>
<tr><th>Score</th><th>Clarity (5)</th><th>Results &amp; Data (5)</th><th>Professional Delivery (5)</th></tr>
<tr><td>5</td><td>Logical narrative from audit to implementation</td><td>Before/after metrics or projected impact quantified</td><td>Within time limit; engages Q&amp;A confidently</td></tr>
<tr><td>3</td><td>Some organization issues</td><td>Limited data</td><td>Reads slides; weak Q&amp;A</td></tr>
<tr><td>1</td><td>Incoherent or incomplete</td><td>No metrics</td><td>Over time or unprepared</td></tr>
</table>

<h2>Certification Requirements Checklist</h2>
<ul class="checklist">
<li>Complete all 15 module quizzes with ≥75% average</li>
<li>Submit all 15 workshop deliverables with ≥70% average</li>
<li>Pass certification exam with ≥80% (80/100 correct)</li>
<li>Score ≥70/100 on capstone project rubric</li>
<li>Maintain participation average ≥7/10</li>
<li>Present capstone within scheduled session or approved async video</li>
<li>Sign academic integrity statement for all AI-assisted work</li>
</ul>

<h2>Grade Boundaries</h2>
<table>
<tr><th>Capstone Score</th><th>Rating</th><th>Certification Eligibility</th></tr>
<tr><td>90–100</td><td>Distinction</td><td>Eligible — Honors certificate</td></tr>
<tr><td>80–89</td><td>Merit</td><td>Eligible — Standard certificate</td></tr>
<tr><td>70–79</td><td>Pass</td><td>Eligible — Standard certificate</td></tr>
<tr><td>60–69</td><td>Revision Required</td><td>Revise and resubmit within 14 days</td></tr>
<tr><td>Below 60</td><td>Fail</td><td>Must retake capstone next cohort</td></tr>
</table>
</section>
"""


def get_supplements():
    """Return HTML string containing all supplementary course sections."""
    sections = [
        _glossary_html(),
        _checklists_html(),
        _slides_html(),
        _workshops_html(),
        _rubrics_html(),
        _exam_html(),
        _cert_rubric_html(),
    ]
    html = "\n".join(sections)
    if len(html) < 25000:
        raise ValueError(f"Supplements HTML must be at least 25000 chars; got {len(html)}")
    return html


if __name__ == "__main__":
    out = get_supplements()
    print(f"Generated supplements: {len(out):,} characters")
    print(f"Glossary terms: 80+ | Exam questions: 100 | Sections: glossary, checklists, slides, workshops, rubrics, exam, cert-rubric")
