# The Golden Whisk — Cake Board

A made-to-order cake site for The Golden Whisk, published as a stand-in
while the full site is being built. Two pages: Home (`index.html` — the
main WordPress site's actual hero, brought over verbatim, plus the
custom-cake gallery) and Menu (`menu.html` — flavours and prices), linked
by a shared top nav also brought over from the WordPress theme (adapted
to this site's two real pages instead of the six section anchors the
full homepage links to).

## How it's built

`build/generate.py` assembles **both** `dist/index.html` and
`dist/menu.html` from:

- the flavour/category/price data defined at the top of the script
  (renders into menu.html),
- gallery photos in `build/assets/photos/` (base64 WebP, cropped/
  compressed from the originals kept in `build/assets/photos/originals/`
  — see [`build/assets/photos/README.md`](build/assets/photos/README.md)
  for the exact pipeline; renders into index.html),
- font subsets in `build/assets/fonts/` (base64 WOFF2, one per typeface —
  see [`build/vendor/SOURCES.md`](build/vendor/SOURCES.md) for which
  family/weight each one is; the type system matches the main WordPress
  theme's — Fraunces for display headings, Karla for body copy, Space
  Mono for labels/prices/eyebrows, Caveat for the handwritten aside — with
  DM Serif Text and Inter kept only on the site-nav and masthead, unchanged
  from before). The colour scheme follows suit: a light paper page
  (`--cream`/`--paper`) rather than the original all-dark board, with the
  dark `--board` background kept only as its own accent band behind the
  masthead and the closing footer card — the site-nav and masthead are
  otherwise pixel-for-pixel what they were before this pass,
- vendored copies of GSAP, ScrollTrigger, and ScrollToPlugin in
  `build/vendor/` (also documented in `SOURCES.md`, with recorded SHA-256
  checksums).

Each page is inlined into one self-contained HTML file — no external
requests, no build-time network dependency, no CDN to go down or get
compromised. Fonts and libraries are committed as static files rather
than fetched on every build specifically so the output is reproducible
and doesn't depend on a third party being reachable or trustworthy at
build time. The tradeoff: since both pages inline their own copy of the
fonts/JS independently (there's no shared external file to cache), a
visitor navigating from Home to Menu re-downloads that ~450KB rather than
reusing it. Acceptable for now; worth revisiting with extracted shared
assets if a third page joins.

To build and stage locally:

```sh
python3 build/generate.py         # writes dist/index.html and dist/menu.html
python3 scripts/verify.py         # sanity-checks both pages
cd dist && python3 -m http.server 8420   # stage at http://localhost:8420/ and /menu.html
```

`scripts/verify.py` re-checks the vendored files' checksums, confirms the
required meta tags are present, validates every inline `<script>` block
with `node --check` on both pages, checks the top nav links both pages
together with the right one marked active, and asserts each page's
content stays on its own page (5 categories / 45 menu items only on
menu.html, the photo gallery only on index.html). It's the same gate CI
runs before deploying.

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

## Editing the gallery

The `GALLERY` list (same file) holds the Home page's photocards — each
entry is `photo` (the key into `build/assets/photos/*.b64`), `title`,
`desc` (describe only what's visibly decorated — these are real delivered
cakes, not menu items, so don't invent flavour/ingredient claims), and
`occasion`. To add a new one: drop the original photo in
`build/assets/photos/originals/`, run it through the pipeline in
`build/assets/photos/README.md`, then add an entry here.

## Editing shared copy

The masthead intro differs per page (`HOME_INTRO` / `MENU_INTRO`), as does
the footer's price disclaimer (`MENU_FOOTER_NOTE`, home page doesn't get
one) and the page `<title>`/meta description (`HOME_TITLE` /
`HOME_DESCRIPTION` / `MENU_TITLE` / `MENU_DESCRIPTION`) — all defined
together in `build/generate.py`, above where the two pages get rendered.
Everything else (masthead structure, footer signoff/contact, the CSS) is
shared via `masthead_html()` / `footer_html()` / the `TEMPLATE` string
further down the same file.

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
