#!/usr/bin/env python3
"""
Post-build sanity gate. Fails (non-zero exit) if the built dist/ pages
don't look right, so a broken build never reaches the deploy step.

Checks (per page, plus site-wide):
  - vendored JS matches the checksums recorded in build/vendor/SOURCES.md,
    catching an accidental or malicious edit to those files before they're
    inlined into the published page
  - required meta tags are present (viewport, charset)
  - every <script> block is syntactically valid JS (via `node --check`)
  - no leftover __..._JS__ or {page_title}-style template placeholders
  - both pages link to each other via .site-nav, with the correct one
    marked is-active
  - index.html: 18 gallery photocards each with an embedded WebP photo,
    and NO category/menu content (that moved to its own page)
  - menu.html: 5 categories, 50 <tr> (45 data rows + 5 header rows), and
    NO gallery content (that's the home page's job)
"""
import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIST_DIR = REPO_ROOT / "dist"
VENDOR_DIR = REPO_ROOT / "build" / "vendor"
SOURCES_MD = VENDOR_DIR / "SOURCES.md"

EXPECTED_CATEGORIES = 5
EXPECTED_TR = 50
EXPECTED_PHOTOCARDS = 18


def fail(message):
    print(f"FAIL: {message}", file=sys.stderr)
    sys.exit(1)


def ok(message):
    print(f"OK: {message}")


def check_vendor_checksums():
    sources_text = SOURCES_MD.read_text()
    # Pull each "`filename.js`" ... "`hexhash`" pair out of the markdown table.
    rows = re.findall(r"`([\w.]+\.js)`.*?`([0-9a-f]{64})`", sources_text)
    if not rows:
        fail("could not find any checksum rows in build/vendor/SOURCES.md")
    for filename, expected_hash in rows:
        path = VENDOR_DIR / filename
        if not path.exists():
            fail(f"vendored file listed in SOURCES.md is missing: {filename}")
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            fail(
                f"{filename} does not match the checksum recorded in SOURCES.md "
                f"(expected {expected_hash}, got {actual_hash}) — if this change "
                f"is intentional, review the diff and re-run "
                f"`shasum -a 256 *.js > SHA256SUMS.txt` to update the record"
            )
    ok(f"vendored JS matches recorded checksums ({len(rows)} files)")


def check_common(name, html):
    if "__GSAP_JS__" in html or "__ANIMATION_JS__" in html or "__SCROLLTRIGGER_JS__" in html or "__SCROLLTOPLUGIN_JS__" in html:
        fail(f"{name}: a template placeholder was never substituted — build is broken")
    if "{page_title}" in html or "{body}" in html or "{meta_description}" in html:
        fail(f"{name}: a .format() placeholder was never substituted — build is broken")

    if '<meta name="viewport"' not in html:
        fail(f"{name}: missing <meta name=\"viewport\"> — page would render tiny on phones")
    if '<meta charset="utf-8"' not in html:
        fail(f"{name}: missing <meta charset=\"utf-8\">")


def check_nav(name, html, active_href):
    if 'class="nav" id="nav"' not in html:
        fail(f"{name}: missing the top nav")
    if not re.search(r'<a href="index\.html"[^>]*>Home</a>', html):
        fail(f"{name}: nav is missing a Home link")
    if not re.search(r'<a href="menu\.html"[^>]*>Menu</a>', html):
        fail(f"{name}: nav is missing a Menu link")
    active_pattern = rf'<a href="{re.escape(active_href)}" class="is-current">'
    if not re.search(active_pattern, html):
        fail(f"{name}: nav does not mark {active_href} as is-current")
    ok(f"{name}: nav present and pointing at {active_href} as active")


def check_home(html):
    photocard_count = html.count('class="photocard"')
    if photocard_count != EXPECTED_PHOTOCARDS:
        fail(f"index.html: expected {EXPECTED_PHOTOCARDS} gallery photocards, found {photocard_count}")
    ok(f"index.html: {photocard_count} gallery photocards present")

    img_count = len(re.findall(r'<img src="data:image/webp;base64,', html))
    if img_count != EXPECTED_PHOTOCARDS:
        fail(f"index.html: expected {EXPECTED_PHOTOCARDS} embedded gallery photos, found {img_count}")
    ok(f"index.html: {img_count} gallery photos embedded as WebP data URIs")

    if 'class="category"' in html:
        fail("index.html: found menu category content — that should only be on menu.html now")
    if 'class="jump"' in html:
        fail("index.html: found the category jump nav — that should only be on menu.html now")
    ok("index.html: no menu/category content leaked in from menu.html")

    if 'href="menu.html"' not in html:
        fail("index.html: missing a link to menu.html (the \"View Full Menu\" CTA)")
    ok("index.html: links to the full menu")


def check_menu(html):
    cat_count = html.count('class="category"')
    if cat_count != EXPECTED_CATEGORIES:
        fail(f"menu.html: expected {EXPECTED_CATEGORIES} categories, found {cat_count}")
    ok(f"menu.html: {cat_count} categories present")

    tr_count = len(re.findall(r"<tr>", html))
    if tr_count != EXPECTED_TR:
        fail(f"menu.html: expected {EXPECTED_TR} <tr> elements, found {tr_count}")
    ok(f"menu.html: {tr_count} table rows present")

    if 'class="photocard"' in html or 'class="gallery"' in html:
        fail("menu.html: found gallery content — that should only be on index.html now")
    ok("menu.html: no gallery content leaked in from index.html")


def check_inline_scripts_parse(name, html):
    scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
    if not scripts:
        fail(f"{name}: no inline <script> blocks found")
    with tempfile.TemporaryDirectory() as tmp:
        for i, script in enumerate(scripts):
            script_path = Path(tmp) / f"script_{i}.js"
            script_path.write_text(script)
            result = subprocess.run(
                ["node", "--check", str(script_path)],
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                fail(f"{name}: script block {i} failed node --check:\n{result.stderr}")
    ok(f"{name}: {len(scripts)} inline script blocks are syntactically valid")


def check_cname():
    src = REPO_ROOT / "build" / "CNAME"
    dist_cname = DIST_DIR / "CNAME"
    if not src.exists():
        # No custom domain configured — nothing to check.
        return
    if not dist_cname.exists():
        fail("build/CNAME exists but was not copied into dist/ — check generate.py")
    expected = src.read_text().strip()
    actual = dist_cname.read_text().strip()
    if actual != expected:
        fail(f"dist/CNAME ({actual!r}) does not match build/CNAME ({expected!r})")
    ok(f"dist/CNAME matches build/CNAME ({expected})")


def main():
    check_vendor_checksums()

    home_path = DIST_DIR / "index.html"
    menu_path = DIST_DIR / "menu.html"
    if not home_path.exists():
        fail(f"{home_path} does not exist — did the build step run?")
    if not menu_path.exists():
        fail(f"{menu_path} does not exist — did the build step run?")

    home_html = home_path.read_text()
    menu_html = menu_path.read_text()

    check_common("index.html", home_html)
    check_common("menu.html", menu_html)
    check_nav("index.html", home_html, "index.html")
    check_nav("menu.html", menu_html, "menu.html")
    check_home(home_html)
    check_menu(menu_html)
    check_inline_scripts_parse("index.html", home_html)
    check_inline_scripts_parse("menu.html", menu_html)
    check_cname()

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
