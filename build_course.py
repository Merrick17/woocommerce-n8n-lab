#!/usr/bin/env python3
"""Build SEO/AEO/GEO WordPress course (non-coder, plugin-focused)."""
from pathlib import Path
from wp_seo_course_part3 import build_all_slides

OUT = Path(__file__).parent / "modern-seo-aeo-geo-mastery-course.html"
ALT = Path(__file__).parent / "wordpress-management-course.html"

def main():
    html = build_all_slides()
    OUT.write_text(html, encoding="utf-8")
    ALT.write_text(html, encoding="utf-8")
    slides = html.count('<section class="slide')
    print(f"Generated: {OUT}")
    print(f"Also saved: {ALT}")
    print(f"Size: {len(html):,} chars · ~{slides} slides")
    print("Focus: SEO/AEO/GEO on WordPress with plugins — no coding")

if __name__ == "__main__":
    main()
