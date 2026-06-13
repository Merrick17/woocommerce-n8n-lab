#!/usr/bin/env python3
"""Slide framework for WordPress Management PPT-style course."""
import html as html_lib

def esc(s):
    return html_lib.escape(str(s))

CSS = """
:root {
  --wp-blue: #0073aa;
  --wp-dark: #23282d;
  --wp-accent: #00a0d2;
  --wp-orange: #d54e21;
  --slide-w: 1280px;
  --slide-h: 720px;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: 'Segoe UI', Calibri, Arial, sans-serif;
  background: #2c3338;
  color: #1d2327;
  padding: 24px;
}
.deck { max-width: var(--slide-w); margin: 0 auto; }

/* ── SLIDE SHELL ── */
.slide {
  width: var(--slide-w);
  height: var(--slide-h);
  background: #fff;
  margin: 0 auto 32px;
  box-shadow: 0 8px 32px rgba(0,0,0,.35);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  position: relative;
  page-break-after: always;
  break-after: page;
}
.slide-header {
  background: linear-gradient(135deg, var(--wp-dark) 0%, var(--wp-blue) 100%);
  color: #fff;
  padding: 18px 40px 14px;
  min-height: 72px;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
}
.slide-header h2 {
  font-size: 28px;
  font-weight: 600;
  line-height: 1.2;
  border: none;
  margin: 0;
}
.slide-header .module-tag {
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 1.5px;
  opacity: .85;
  white-space: nowrap;
}
.slide-body {
  flex: 1;
  padding: 32px 48px 24px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}
.slide-footer {
  background: #f0f0f1;
  border-top: 3px solid var(--wp-accent);
  padding: 8px 40px;
  font-size: 11px;
  color: #646970;
  display: flex;
  justify-content: space-between;
}
.slide-footer .brand { color: var(--wp-blue); font-weight: 600; }

/* ── SLIDE TYPES ── */
.slide-cover {
  background: linear-gradient(160deg, #1d2327 0%, #0073aa 55%, #00a0d2 100%);
  color: #fff;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.slide-cover .slide-body { justify-content: center; align-items: center; text-align: center; padding: 60px; }
.slide-cover h1 { font-size: 44px; font-weight: 700; line-height: 1.15; margin-bottom: 16px; border: none; }
.slide-cover .subtitle { font-size: 22px; opacity: .92; margin-bottom: 32px; }
.slide-cover .meta { font-size: 14px; opacity: .75; line-height: 1.8; }
.slide-cover .wp-icon { font-size: 64px; margin-bottom: 24px; }

.slide-section {
  background: linear-gradient(160deg, var(--wp-dark) 0%, #135e96 100%);
  color: #fff;
}
.slide-section .slide-body { justify-content: center; align-items: center; text-align: center; }
.slide-section h1 { font-size: 48px; font-weight: 700; border: none; margin-bottom: 12px; }
.slide-section .mod-num { font-size: 18px; text-transform: uppercase; letter-spacing: 3px; opacity: .7; margin-bottom: 8px; }
.slide-section .mod-desc { font-size: 20px; opacity: .85; max-width: 700px; }

.slide-title-only .slide-body { justify-content: center; }
.slide-title-only h2 { font-size: 36px; color: var(--wp-blue); border-left: 6px solid var(--wp-orange); padding-left: 20px; }

/* Content elements */
.slide-body ul, .slide-body ol { margin: 8px 0 8px 28px; }
.slide-body li { font-size: 22px; line-height: 1.45; margin: 10px 0; color: #1d2327; }
.slide-body li strong { color: var(--wp-blue); }
.slide-body p { font-size: 20px; line-height: 1.5; margin: 8px 0; }
.slide-body .lead { font-size: 24px; color: #50575e; margin-bottom: 16px; }

.two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; flex: 1; }
.col h3 { font-size: 18px; color: var(--wp-blue); margin-bottom: 12px; text-transform: uppercase; letter-spacing: .5px; }
.col ul { margin-left: 20px; }
.col li { font-size: 18px; margin: 8px 0; }

.diagram {
  font-family: Consolas, 'Courier New', monospace;
  font-size: 13px;
  background: #f6f7f7;
  border: 1px solid #c3c4c7;
  border-left: 4px solid var(--wp-accent);
  padding: 16px 20px;
  line-height: 1.4;
  white-space: pre;
  overflow: hidden;
  margin-top: 12px;
}
.callout {
  background: #e5f5fa;
  border-left: 5px solid var(--wp-accent);
  padding: 14px 18px;
  margin-top: 16px;
  font-size: 17px;
}
.callout-warn { background: #fcf0f1; border-left-color: var(--wp-orange); }
.callout-tip { background: #edfaef; border-left-color: #00a32a; }
.callout strong { display: block; margin-bottom: 4px; color: var(--wp-dark); }

.steps { counter-reset: step; list-style: none; margin-left: 0 !important; }
.steps li { counter-increment: step; padding-left: 48px; position: relative; }
.steps li::before {
  content: counter(step);
  position: absolute; left: 0; top: 2px;
  width: 32px; height: 32px;
  background: var(--wp-blue); color: #fff;
  border-radius: 50%; text-align: center;
  line-height: 32px; font-size: 16px; font-weight: 700;
}

table.data { width: 100%; border-collapse: collapse; font-size: 16px; margin-top: 8px; }
table.data th { background: var(--wp-dark); color: #fff; padding: 10px 14px; text-align: left; }
table.data td { border: 1px solid #c3c4c7; padding: 10px 14px; }
table.data tr:nth-child(even) { background: #f6f7f7; }

.speaker-notes {
  display: none;
}
.icon-row { display: flex; gap: 24px; flex-wrap: wrap; margin-top: 16px; }
.icon-card {
  flex: 1; min-width: 180px;
  background: #f6f7f7; border-top: 4px solid var(--wp-blue);
  padding: 16px; text-align: center;
}
.icon-card .emoji { font-size: 36px; margin-bottom: 8px; }
.icon-card h4 { font-size: 16px; color: var(--wp-blue); margin-bottom: 6px; }
.icon-card p { font-size: 14px; color: #50575e; }

/* TOC slide */
.toc-grid { columns: 2; column-gap: 40px; }
.toc-grid li { font-size: 17px; break-inside: avoid; margin: 6px 0; }

/* Checklist */
.checklist { list-style: none; margin-left: 0 !important; }
.checklist li { font-size: 18px; padding-left: 28px; position: relative; }
.checklist li::before { content: "☐"; position: absolute; left: 0; color: var(--wp-blue); font-weight: bold; }

@media print {
  body { background: #fff; padding: 0; }
  .deck { max-width: none; }
  .slide {
    width: 100%; height: 100vh;
    margin: 0; box-shadow: none;
    page-break-after: always;
  }
  @page { size: landscape; margin: 0; }
}
@media screen {
  .slide:hover { outline: 2px solid var(--wp-accent); outline-offset: 4px; }
}
"""

def slide_cover(title, subtitle, meta_lines):
    meta = "<br>".join(esc(m) for m in meta_lines)
    return f'''<section class="slide slide-cover">
<div class="slide-body">
<div class="wp-icon">⚙️</div>
<h1>{esc(title)}</h1>
<p class="subtitle">{esc(subtitle)}</p>
<p class="meta">{meta}</p>
</div>
</section>'''

def slide_toc(items):
    lis = "".join(f"<li>{esc(i)}</li>" for i in items)
    return slide_content(0, "Course Overview — Modules at a Glance", f'<ol class="toc-grid">{lis}</ol>', "Introduction", 2)

def slide_section(mod_num, title, description):
    return f'''<section class="slide slide-section" id="module{mod_num}">
<div class="slide-body">
<p class="mod-num">Module {mod_num}</p>
<h1>{esc(title)}</h1>
<p class="mod-desc">{esc(description)}</p>
</div>
<div class="slide-footer"><span class="brand">SEO · AEO · GEO on WordPress</span><span>Module {mod_num} · Section</span></div>
</section>'''

def slide_content(module, title, body_html, mod_title, slide_num, extra_class=""):
    cls = f"slide {extra_class}".strip()
    return f'''<section class="{cls}">
<div class="slide-header"><h2>{esc(title)}</h2><span class="module-tag">{esc(mod_title)}</span></div>
<div class="slide-body">{body_html}</div>
<div class="slide-footer"><span class="brand">SEO · AEO · GEO on WordPress</span><span>Module {module} · Slide {slide_num}</span></div>
</section>'''

def slide_two_col(module, title, left_title, left_items, right_title, right_items, mod_title, slide_num):
    left = "".join(f"<li>{esc(i)}</li>" for i in left_items)
    right = "".join(f"<li>{esc(i)}</li>" for i in right_items)
    body = f'''<div class="two-col">
<div class="col"><h3>{esc(left_title)}</h3><ul>{left}</ul></div>
<div class="col"><h3>{esc(right_title)}</h3><ul>{right}</ul></div>
</div>'''
    return slide_content(module, title, body, mod_title, slide_num)

def slide_bullets(module, title, bullets, mod_title, slide_num, lead="", callout=None):
    bl = "".join(f"<li>{b}</li>" for b in bullets)  # bullets may contain <strong>
    body = f'{f"<p class=lead>{lead}</p>" if lead else ""}<ul>{bl}</ul>'
    if callout:
        body += callout
    return slide_content(module, title, body, mod_title, slide_num)

def slide_diagram(module, title, diagram_text, bullets, mod_title, slide_num):
    bl = "".join(f"<li>{esc(b)}</li>" for b in bullets)
    body = f'<pre class="diagram">{esc(diagram_text)}</pre><ul>{bl}</ul>'
    return slide_content(module, title, body, mod_title, slide_num)

def slide_workshop(module, title, steps, deliverable, mod_title, slide_num):
    steps_html = "".join(f"<li>{esc(s)}</li>" for s in steps)
    body = f'''<p class="lead">Hands-on lab — instructor-led</p>
<ol class="steps">{steps_html}</ol>
<div class="callout callout-tip"><strong>Deliverable</strong>{esc(deliverable)}</div>'''
    return slide_content(module, title, body, mod_title, slide_num, "slide-workshop")

def slide_summary(module, objectives, mod_title, slide_num):
    bl = "".join(f"<li>{esc(o)}</li>" for o in objectives)
    body = f'<p class="lead">Key takeaways from this module</p><ul>{bl}</ul>'
    return slide_content(module, "Module Summary", body, mod_title, slide_num)

def callout(cls, title, text):
    return f'<div class="callout {cls}"><strong>{esc(title)}</strong>{esc(text)}</div>'

def icon_cards(cards):
    items = "".join(
        f'<div class="icon-card"><div class="emoji">{c[0]}</div><h4>{esc(c[1])}</h4><p>{esc(c[2])}</p></div>'
        for c in cards
    )
    return f'<div class="icon-row">{items}</div>'

def wrap_deck(slides_html, title):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<style>{CSS}</style>
</head>
<body>
<div class="deck">
{slides_html}
</div>
</body>
</html>'''
