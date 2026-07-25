# The Golden Whisk — Cake Board

A single-page, made-to-order cake menu for The Golden Whisk, published as
a stand-in while the full site is being built.

## How it's built

`build/generate.py` assembles `dist/index.html` from:

- the flavour/category/price data defined at the top of the script,
- font subsets in `build/assets/fonts/` (base64 WOFF2, one per typeface —
  see [`build/vendor/SOURCES.md`](build/vendor/SOURCES.md) for which
  family/weight each one is),
- vendored copies of GSAP, ScrollTrigger, and ScrollToPlugin in
  `build/vendor/` (also documented in `SOURCES.md`, with recorded SHA-256
  checksums).

Everything is inlined into one self-contained HTML file — no external
requests, no build-time network dependency, no CDN to go down or get
compromised. Fonts and libraries are committed as static files rather
than fetched on every build specifically so the output is reproducible
and doesn't depend on a third party being reachable or trustworthy at
build time.

To build and stage locally:

```sh
python3 build/generate.py         # writes dist/index.html
python3 scripts/verify.py         # sanity-checks the output
cd dist && python3 -m http.server 8420   # stage it at http://localhost:8420/
```

`scripts/verify.py` re-checks the vendored files' checksums, confirms the
required meta tags are present, validates every inline `<script>` block
with `node --check`, and asserts the expected page structure (5
categories, 45 menu items). It's the same gate CI runs before deploying.

**Always open the local staging server and actually look at the change**
before pushing a branch — `verify.py` catches structural breakage, not
"does this look right." This applies to Claude Code sessions working in
this repo too: build, verify, and review the local `dist/` build before
pushing anything, even for small copy edits. Nothing goes straight from
an edit to a pushed branch without a local look first.

## Editing the menu

Flavours, categories, and prices live in the Python lists near the top of
`build/generate.py` (`FRUIT`, `CHOCOLATE`, `SIGNATURE`, `WHOLESOME`,
`PIECE`) — each entry is `(name, price_per_kg, price_per_650g)`. Items
within each category are sorted alphabetically at build time, so add
entries in any order.

Copy — the hero text, footer, contact line — lives in the `TEMPLATE`
string further down the same file.

## Publishing workflow

- **There is no separate staging environment on GitHub's side.** The
  local staging server above (`dist/` served on `localhost`) is the real
  review step — do that before opening a PR, not after.
- Changes land on `main` only through a reviewed pull request — direct
  pushes to `main` are blocked by branch protection.
- Every pull request runs [`.github/workflows/ci.yml`](.github/workflows/ci.yml):
  build + verify, so a broken build can't be approved and merged.
- **Merging to `main` does not deploy anything.**
  [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) only
  triggers on `workflow_dispatch` — deploying to the live domain is a
  separate, deliberate step:
  ```sh
  gh workflow run deploy.yml --repo bhatnagarpb-wq/golden-whisk-menu
  ```
  or use the "Run workflow" button under the repo's Actions tab. Run it
  once you've merged something you've actually reviewed on local
  staging — not automatically just because CI was green. The deploy job
  only has `pages: write` and `id-token: write` — nothing else — and
  only runs if the build/verify job succeeded.
- The live page is served straight from the `dist/` artifact GitHub Pages
  publishes; `dist/` itself is gitignored and never committed, so there's
  no stale build sitting in git history.
