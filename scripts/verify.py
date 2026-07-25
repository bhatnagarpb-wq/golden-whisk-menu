#!/usr/bin/env python3
"""
Post-build sanity gate. Fails (non-zero exit) if the built dist/index.html
doesn't look right, so a broken build never reaches the deploy step.

Checks:
  - vendored JS matches the checksums recorded in build/vendor/SOURCES.md,
    catching an accidental or malicious edit to those files before they're
    inlined into the published page
  - required meta tags are present (viewport, charset)
  - every <script> block is syntactically valid JS (via `node --check`)
  - no leftover __..._JS__ template placeholders
  - expected content structure: 5 categories, 50 <tr> (45 data rows + 5
    header rows), 7 gallery photocards each with an embedded WebP photo
"""
import hashlib
import re
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DIST_HTML = REPO_ROOT / "dist" / "index.html"
VENDOR_DIR = REPO_ROOT / "build" / "vendor"
SOURCES_MD = VENDOR_DIR / "SOURCES.md"

EXPECTED_CATEGORIES = 5
EXPECTED_TR = 50
EXPECTED_PHOTOCARDS = 7


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


def check_html_structure():
    if not DIST_HTML.exists():
        fail(f"{DIST_HTML} does not exist — did the build step run?")
    html = DIST_HTML.read_text()

    if "__GSAP_JS__" in html or "__ANIMATION_JS__" in html or "__SCROLLTRIGGER_JS__" in html or "__SCROLLTOPLUGIN_JS__" in html:
        fail("a template placeholder was never substituted — build is broken")

    if '<meta name="viewport"' not in html:
        fail("missing <meta name=\"viewport\"> — page would render tiny on phones")
    if '<meta charset="utf-8"' not in html:
        fail("missing <meta charset=\"utf-8\">")

    cat_count = html.count('class="category"')
    if cat_count != EXPECTED_CATEGORIES:
        fail(f"expected {EXPECTED_CATEGORIES} categories, found {cat_count}")
    ok(f"{cat_count} categories present")

    tr_count = len(re.findall(r"<tr>", html))
    if tr_count != EXPECTED_TR:
        fail(f"expected {EXPECTED_TR} <tr> elements, found {tr_count}")
    ok(f"{tr_count} table rows present")

    photocard_count = html.count('class="photocard"')
    if photocard_count != EXPECTED_PHOTOCARDS:
        fail(f"expected {EXPECTED_PHOTOCARDS} gallery photocards, found {photocard_count}")
    ok(f"{photocard_count} gallery photocards present")

    img_count = len(re.findall(r'<img src="data:image/webp;base64,', html))
    if img_count != EXPECTED_PHOTOCARDS:
        fail(f"expected {EXPECTED_PHOTOCARDS} embedded gallery photos, found {img_count}")
    ok(f"{img_count} gallery photos embedded as WebP data URIs")


def check_inline_scripts_parse():
    html = DIST_HTML.read_text()
    scripts = re.findall(r"<script>(.*?)</script>", html, re.S)
    if not scripts:
        fail("no inline <script> blocks found")
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
                fail(f"script block {i} failed node --check:\n{result.stderr}")
    ok(f"{len(scripts)} inline script blocks are syntactically valid")


def check_cname():
    src = REPO_ROOT / "build" / "CNAME"
    dist_cname = REPO_ROOT / "dist" / "CNAME"
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
    check_html_structure()
    check_inline_scripts_parse()
    check_cname()
    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
