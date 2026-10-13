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
  - both pages have the top nav with a Home link (Menu is deliberately
    unlinked for now — see check_nav)
  - index.html: 18 gallery photocards each pointing at a WebP file that
    exists in dist/assets/photos/, no photo inlined as a data URI, the
    page under its size budget, and NO category/menu content (that moved
    to its own page)
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
# index.html is ~260KB with fonts and scripts inlined. Well above that
# means something heavy (most likely a photo) got inlined into the page
# again, which every visitor then downloads before anything renders.
MAX_HOME_BYTES = 400_000
GA_MEASUREMENT_ID = "G-B0Y2THJ832"


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
    if "{page_title}" in html or "{body}" in html or "{meta_description}" in html or "{robots_meta}" in html:
        fail(f"{name}: a .format() placeholder was never substituted — build is broken")

    if '<meta name="viewport"' not in html:
        fail(f"{name}: missing <meta name=\"viewport\"> — page would render tiny on phones")
    if '<meta charset="utf-8"' not in html:
        fail(f"{name}: missing <meta charset=\"utf-8\">")

    if f"googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}" not in html or f"gtag('config', '{GA_MEASUREMENT_ID}')" not in html:
        fail(f"{name}: missing the Google Analytics tag ({GA_MEASUREMENT_ID}) — visits to this page wouldn't be counted")


def check_robots(home_html, menu_html):
    # menu.html is hidden from the nav for now, so it should stay out of
    # search results too; index.html must never pick up the same tag.
    noindex = '<meta name="robots" content="noindex"'
    if noindex not in menu_html:
        fail("menu.html: missing the noindex robots meta tag — the hidden Menu page could show up in search results")
    if noindex in home_html:
        fail("index.html: has a noindex robots meta tag — the home page would drop out of search results")
    ok("menu.html is noindex, index.html is indexable")


def check_nav(name, html, expect_home_link):
    # The Menu link is deliberately hidden from the nav for now (menu.html
    # still builds and is reachable by direct URL, just not linked from
    # anywhere on the site). The nav also never links to the page you're
    # already on, so index.html has no Home link — only menu.html does,
    # as a way back.
    if 'class="nav" id="nav"' not in html:
        fail(f"{name}: missing the top nav")
    has_home_link = bool(re.search(r'<a href="index\.html"[^>]*>Home</a>', html))
    if expect_home_link and not has_home_link:
        fail(f"{name}: nav is missing a Home link")
    if not expect_home_link and has_home_link:
        fail(f"{name}: nav has a self-referential Home link, expected none")
    ok(f"{name}: nav present" + (" with a Home link" if expect_home_link else ", no self-link to Home"))


def check_home(html):
    photocard_count = html.count('class="photocard"')
    if photocard_count != EXPECTED_PHOTOCARDS:
        fail(f"index.html: expected {EXPECTED_PHOTOCARDS} gallery photocards, found {photocard_count}")
    ok(f"index.html: {photocard_count} gallery photocards present")

    if "data:image/" in html:
        fail("index.html: a photo is inlined as a data URI — gallery photos should be separate files so they lazy-load")
    photo_srcs = re.findall(r'<img src="(assets/photos/[\w-]+\.webp)"[^>]*loading="lazy"', html)
    if len(photo_srcs) != EXPECTED_PHOTOCARDS:
        fail(f"index.html: expected {EXPECTED_PHOTOCARDS} lazy-loaded gallery photos, found {len(photo_srcs)}")
    for src in photo_srcs:
        photo_path = DIST_DIR / src
        if not photo_path.exists():
            fail(f"index.html: links to {src}, which is missing from dist/ — the photo would show as a broken image")
        header = photo_path.read_bytes()[:12]
        if header[:4] != b"RIFF" or header[8:12] != b"WEBP":
            fail(f"{src} is not a valid WebP file")
    ok(f"index.html: {len(photo_srcs)} gallery photos lazy-load from WebP files in dist/assets/photos/")

    home_bytes = len(html.encode())
    if home_bytes > MAX_HOME_BYTES:
        fail(f"index.html is {home_bytes:,} bytes, over the {MAX_HOME_BYTES:,} byte budget")
    ok(f"index.html: {home_bytes:,} bytes, within the {MAX_HOME_BYTES:,} byte budget")

    if 'class="category"' in html:
        fail("index.html: found menu category content — that should only be on menu.html now")
    if 'class="jump"' in html:
        fail("index.html: found the category jump nav — that should only be on menu.html now")
    ok("index.html: no menu/category content leaked in from menu.html")


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
    check_nav("index.html", home_html, expect_home_link=False)
    check_nav("menu.html", menu_html, expect_home_link=True)
    check_home(home_html)
    check_menu(menu_html)
    check_robots(home_html, menu_html)
    check_inline_scripts_parse("index.html", home_html)
    check_inline_scripts_parse("menu.html", menu_html)
    check_cname()

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
