# Vendored third-party scripts

These are committed as static files (not fetched at build time) so the CI
build has no runtime network dependency on a third-party CDN and produces
a byte-identical result every run. `scripts/verify.py` checks each file
against the checksum recorded here before every build — if cdnjs or the
upstream project ever needs to be re-synced, regenerate this file with
`shasum -a 256 *.js > SHA256SUMS.txt` after manually reviewing the diff.

| File | Upstream | Version | SHA-256 |
|---|---|---|---|
| `gsap.min.js` | https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js | 3.12.5 | `28033e449a31ebcc396e5be8b13b63152bf03094288fb5867034321927bce087` |
| `ScrollTrigger.min.js` | https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js | 3.12.5 | `ad33c2df9ada8a663c2147357828f980d0b7ca731ef33eb3c6e4f327c3b2cda5` |
| `ScrollToPlugin.min.js` | https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollToPlugin.min.js | 3.12.5 | `e82f1a686ce2f7a62a7078bf101a386c58bd4e3b0b2e99f5774b7c1e54f8440f` |

## Fonts

`build/assets/fonts/*.b64` are base64-encoded WOFF2 subsets fetched once
from the Google Fonts CSS2 API (`fonts.googleapis.com/css2?family=...&text=...`),
trimmed to only the glyphs the page actually uses. They're committed for
the same reason as the scripts above — no network call during the CI
build. See `build/generate.py` for which family/weight/text each one
corresponds to.

| File | Family | Weight |
|---|---|---|
| `fraunces.b64` | Fraunces | 600 |
| `dmseriftext.b64` | DM Serif Text | 400 |
| `inter400.b64` | Inter | 400 |
| `inter600.b64` | Inter | 600 |
| `karla400.b64` | Karla | 400 |
| `karla600.b64` | Karla | 600 |
| `spacemono400.b64` | Space Mono | 400 |
| `spacemono700.b64` | Space Mono | 700 |
| `caveat.b64` | Caveat | 600 |
