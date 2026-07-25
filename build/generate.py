# -*- coding: utf-8 -*-
import html
from pathlib import Path

# All paths are relative to this script's own location, not the current
# working directory, so `python3 build/generate.py` works the same whether
# it's run from the repo root (CI) or from inside build/ (local dev).
BUILD_DIR = Path(__file__).resolve().parent
REPO_ROOT = BUILD_DIR.parent
FONTS_DIR = BUILD_DIR / "assets" / "fonts"
PHOTOS_DIR = BUILD_DIR / "assets" / "photos"
VENDOR_DIR = BUILD_DIR / "vendor"
DIST_DIR = REPO_ROOT / "dist"

def load(key):
    return (FONTS_DIR / f"{key}.b64").read_text().strip()

def load_photo(key):
    """Base64 WebP for a gallery photo, sourced from build/assets/photos/*.b64
    (originals kept in build/assets/photos/originals/ for reference — see
    build/assets/photos/README.md for how these were optimized)."""
    return (PHOTOS_DIR / f"{key}.b64").read_text().strip()

FONTS = {k: load(k) for k in ["fraunces", "inter400", "inter600", "karla400", "karla600", "spacemono400", "spacemono700", "caveat", "dmseriftext"]}

def money(n):
    return "₹{:,}".format(n)

FRUIT = [
    ("Pineapple", 1200, 800),
    ("Mixed Fruits", 1200, 800),
    ("Fresh Fruits", 1300, 850),
    ("Strawberry Cake", 1200, 600),
    ("Strawberry", 600, 350),
    ("Fresh Strawberry (Seasonal)", 1300, 700),
    ("Fresh Mango (Seasonal)", 1300, 850),
    ("Blueberry", 800, 500),
    ("Orange & Cranberry", 800, 500),
    ("Plum", 1300, 750),
]

CHOCOLATE = [
    ("Chocolate", 1300, 850),
    ("Chocolate Strawberry", 1300, 850),
    ("Chocolate Truffle", 1500, 1000),
    ("Chocolate Truffle — Overloaded", 1600, 1100),
    ("Chocolate White Mud", 1400, 900),
    ("Chocolate Walnut", 700, 400),
    ("Chocolate with Choco Garnish", 800, 500),
    ("Hazelnut", 1400, 900),
    ("Nutella", 1400, 900),
    ("Kit Kat", 1500, 1000),
    ("Lotus Biscoff", 1500, 1000),
    ("Rum", 1400, 850),
]

SIGNATURE = [
    ("Black Forest", 1300, 850),
    ("Red Velvet", 1400, 900),
    ("Red Velvet Cheese Cream Cake", 600, None),
    ("Rasmalai", 1400, 900),
    ("Parsi Mawa", 1000, 600),
    ("Paan Flavour", 1200, 800),
    ("Rose & Pistachio", 750, 450),
    ("Dundee", 750, 450),
    ("Cappuccino", 1300, 850),
    ("Oreo", 1300, 850),
    ("Butterscotch", 1200, 800),
    ("Marble Cake", 500, 300),
]

WHOLESOME = [
    ("Ragi", 450, None),
    ("Chocolate Whole Wheat", 500, None),
    ("Coffee Whole Wheat", 500, None),
    ("Chocolate with Choco Garnish (Whole Wheat)", 650, None),
    ("Natural Sugar-free", 500, None),
    ("Kaju Mawa Whole Wheat", 600, None),
    ("Honey Almond", 700, 400),
    ("Banana Jaggery", 700, 400),
    ("Mixed Dry Fruit", 700, 400),
]

PIECE = [
    ("Brownie", 80),
    ("Honey-nut Crunch Cupcakes", 80),
]

# ---- custom-cake gallery: real photos of recent custom orders, shown
# below the masthead intro. Descriptions cover only what's visible in the
# photo (decoration, technique) — no invented flavour/ingredient claims,
# since these are real delivered cakes, not menu items. No weight is
# shown for the same reason: these are one-off orders, not a standing
# catalogue entry with a knowable minimum. ----

GALLERY = [
    dict(
        photo="cake",
        title="A Golden 50th Anniversary",
        desc="A two-tier gold and white cake marking fifty years together, finished with pearl accents and a hand-lettered gold message.",
        occasion="Anniversary",
    ),
    dict(
        photo="cake_on_table",
        title="Best Husband, Best Dad",
        desc="A tongue-in-cheek tic-tac-toe cake for a husband and dad, finished with hand-cut silhouettes and piped hearts.",
        occasion="Birthday",
    ),
    dict(
        photo="happy_birthday",
        title="A Birthday to Remember",
        desc="A hand-sculpted fondant topper brings the birthday message to life, finished with piped blue rosettes and a hand-lettered plaque.",
        occasion="Birthday",
    ),
    dict(
        photo="jai_guru_ji",
        title="Roses for Guru Ji",
        desc="Delicate piped pink roses and gold leaf detailing, finished with a hand-lettered message band.",
        occasion="Birthday",
    ),
    dict(
        photo="photo_01",
        title="A BLACKPINK Birthday",
        desc="A BLACKPINK-themed cake with a printed edible topper, piped hearts on skewers, and hand-lettered fondant lettering.",
        occasion="Birthday",
    ),
    dict(
        photo="welcome",
        title="A Warm Welcome",
        desc="A hand-piped rosette wreath in blush and sky blue, finished with a mirrored gold Welcome topper.",
        occasion="Celebration",
    ),
    dict(
        photo="welcome_arjun",
        title="Welcome, Baby Arjun",
        desc="Piped blue stars and tiny fondant footprints welcome the newest arrival, finished with a gold mirrored topper.",
        occasion="Welcome Baby",
    ),
    dict(
        photo="mermaid_birthday",
        title="A Mermaid's Birthday Wish",
        desc="A two-tier pink birthday cake with hand-sculpted mermaid tails, gold starfish, and a hand-lettered topper.",
        occasion="Birthday",
    ),
    dict(
        photo="glutenfree_boxed",
        title="A Gluten-Free Chocolate Cake",
        desc="A gluten-free chocolate cake finished with piped chocolate rosettes and a glittered gold topper.",
        occasion="Birthday",
    ),
    dict(
        photo="lotus_biscoff_drip",
        title="A Lotus Biscoff Drip Cake",
        desc="A caramel drip cake finished with crushed Biscoff crumble and a whole Lotus biscuit, hand-lettered on the base.",
        occasion="Birthday",
    ),
    dict(
        photo="glutenfree_drip",
        title="A Tall Gluten-Free Chocolate Drip",
        desc="A gluten-free chocolate cake finished with a dark ganache drip, piped rosettes, and a gold-lettered topper.",
        occasion="Birthday",
    ),
    dict(
        photo="fairy_princess",
        title="A Fairy-Tale Birthday for Mehar",
        desc="A pink butterfly-wing cake with a fairy, unicorn, and castle topper, finished with a hand-lettered name plaque.",
        occasion="Birthday",
    ),
    dict(
        photo="harry_potter",
        title="A Harry Potter Birthday",
        desc="A Harry Potter-themed cake with a hand-sculpted golden snitch, sorting hat, wand, and house scarf, finished with gold lettering.",
        occasion="Birthday",
    ),
    dict(
        photo="myra_stitch",
        title="A Lilo &amp; Stitch Birthday for Myra",
        desc="A pastel ombre cake with Stitch and Angel toppers, piped rosettes, and a hand-lettered name and age.",
        occasion="Birthday",
    ),
    dict(
        photo="anniversary_couple",
        title="A 40th Anniversary Cake",
        desc="A two-tier white cake with pink buttercream ruffle roses, a gold &ldquo;Mrs&rdquo; topper, hand-sculpted figures of the couple, and gold-lettered &ldquo;Happy 40th Anniversary.&rdquo;",
        occasion="Anniversary",
    ),
    dict(
        photo="puneet_drycake",
        title="A Two-Tier Dry Cake for Puneet",
        desc="A two-tier fruit dry cake topped with almonds, glacé cherries, and candied peel, finished with fresh blue and cream roses, a gilded ball, and a gold glitter topper.",
        occasion="Birthday",
    ),
    dict(
        photo="shivanshi_butterfly",
        title="A Butterfly Birthday for Shivanshi",
        desc="A two-tier dark chocolate cake with bronze-gold buttercream rosettes, purple-and-gold butterfly toppers, and edible pearls, finished with a piped name plaque.",
        occasion="Birthday",
    ),
    dict(
        photo="cupcake_bouquet",
        title="A Cupcake Bouquet",
        desc="Seven cupcakes wrapped like a bouquet, with alternating sky-blue and white swirled buttercream and sprigs of baby&rsquo;s breath.",
        occasion="Gift",
    ),
]

def photocard(item):
    photo_b64 = load_photo(item["photo"])
    alt = html.escape(item["title"] + " — " + item["desc"])
    return f"""
        <article class="photocard">
          <div class="photocard-img"><img src="data:image/webp;base64,{photo_b64}" alt="{alt}" loading="lazy" width="640" height="640"></div>
          <h3>{item['title']}</h3>
          <p class="photocard-desc">{item['desc']}</p>
          <div class="photocard-divider"></div>
          <div class="photocard-foot"><span>Occasion</span><strong>{item['occasion']}</strong></div>
        </article>"""

GALLERY_HTML = "\n".join(photocard(item) for item in GALLERY)

def cell(price):
    return money(price) if price is not None else '<span class="dash">—</span>'

def rows_3col(items):
    out = []
    for name, kg, g650 in items:
        out.append(
            f'<tr><td class="name">{html.escape(name)}</td>'
            f'<td class="price">{cell(kg)}</td>'
            f'<td class="price">{cell(g650)}</td></tr>'
        )
    return "\n".join(out)

def rows_2col(items):
    out = []
    for name, price in items:
        out.append(
            f'<tr><td class="name">{html.escape(name)}</td>'
            f'<td class="price">{money(price)} <span class="unit">/ piece</span></td></tr>'
        )
    return "\n".join(out)

def category(cat_id, title, note, items, count_label):
    return f"""
      <section class="category" id="{cat_id}">
        <div class="card">
          <span class="pin" aria-hidden="true"></span>
          <div class="card-head">
            <h2>{title}</h2>
            <span class="count">{count_label}</span>
          </div>
          {note}
          <div class="table-wrap">
            <table>
              <thead>
                <tr><th class="col-name">Flavour</th><th>1&nbsp;kg</th><th>650&nbsp;g</th></tr>
              </thead>
              <tbody>
{rows_3col(items)}
              </tbody>
            </table>
          </div>
        </div>
      </section>"""

def category_piece(cat_id, title, items, count_label):
    return f"""
      <section class="category" id="{cat_id}">
        <div class="card card-narrow">
          <span class="pin" aria-hidden="true"></span>
          <div class="card-head">
            <h2>{title}</h2>
            <span class="count">{count_label}</span>
          </div>
          <div class="table-wrap">
            <table class="table-2col">
              <thead>
                <tr><th class="col-name">Flavour</th><th>Price</th></tr>
              </thead>
              <tbody>
{rows_2col(items)}
              </tbody>
            </table>
          </div>
        </div>
      </section>"""

def sort_by_name(items):
    return sorted(items, key=lambda row: row[0].lower())

FRUIT = sort_by_name(FRUIT)
CHOCOLATE = sort_by_name(CHOCOLATE)
SIGNATURE = sort_by_name(SIGNATURE)
WHOLESOME = sort_by_name(WHOLESOME)
PIECE = sort_by_name(PIECE)

sections = []
sections.append(category("fruit", "Fruit Cakes", "", FRUIT, "10 flavours"))
sections.append(category("chocolate", "Chocolate Cakes", "", CHOCOLATE, "12 flavours"))
sections.append(category("signature", "Signature Flavours", "", SIGNATURE, "12 flavours"))
sections.append(category(
    "wholesome", "Wholesome &amp; Sugar-Free",
    '<p class="card-note">Whole-wheat, sugar-free, and lighter bakes — most come in 1&nbsp;kg only.</p>',
    WHOLESOME, "9 flavours"
))
sections.append(category_piece("piece", "By the Piece", PIECE, "2 items"))

CATEGORIES_HTML = "\n".join(sections)

TEMPLATE = """<!doctype html>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{page_title}</title>
<meta name="description" content="{meta_description}" />
<style>

@font-face {{
  font-family: 'GW Fraunces';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url(data:font/woff2;base64,{fraunces}) format('woff2');
}}
@font-face {{
  font-family: 'GW DM Serif Text';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(data:font/woff2;base64,{dmseriftext}) format('woff2');
}}
@font-face {{
  font-family: 'GW Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(data:font/woff2;base64,{inter400}) format('woff2');
}}
@font-face {{
  font-family: 'GW Inter';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url(data:font/woff2;base64,{inter600}) format('woff2');
}}
@font-face {{
  /* Space Mono, matching the main WordPress theme's utility font exactly
     (not DM Mono, which the header/masthead used before this page adopted
     the main site's theme — the header itself is untouched, see .wordmark
     and the base .eyebrow/.intro rules below, which still resolve through
     --font-body/DM Serif Text as before). */
  font-family: 'GW Mono';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(data:font/woff2;base64,{spacemono400}) format('woff2');
}}
@font-face {{
  font-family: 'GW Mono';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url(data:font/woff2;base64,{spacemono700}) format('woff2');
}}
@font-face {{
  font-family: 'GW Karla';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(data:font/woff2;base64,{karla400}) format('woff2');
}}
@font-face {{
  font-family: 'GW Karla';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url(data:font/woff2;base64,{karla600}) format('woff2');
}}
@font-face {{
  font-family: 'GW Caveat';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url(data:font/woff2;base64,{caveat}) format('woff2');
}}

:root{{
  --board:        #241610;
  --board-deep:   #180F0A;
  --paper:        #FFFDF8;
  --paper-alt:    #F4E3BE;
  --ink:          #2B1B14;
  --ink-70:       rgba(43,27,20,.72);
  --ink-45:       rgba(43,27,20,.45);
  --cream:        #FBF3E7;
  --cream-60:     rgba(251,243,231,.6);
  --cream-40:     rgba(251,243,231,.4);
  --gold:         #C89B3C;
  --gold-dark:    #9C7527;
  --gold-soft:    rgba(200,155,60,.4);
  --jam:          #B23A48;
  --jam-deep:     #8E2A36;
  --line:         rgba(43,27,20,.14);

  --font-display: 'GW Fraunces', Georgia, serif;
  /* --font-body (Inter) is kept only for the header/masthead, which stays
     exactly as it was. Everything else on the page uses --font-karla,
     matching the main WordPress theme's actual body font. */
  --font-body:    'GW Inter', -apple-system, sans-serif;
  --font-karla:   'GW Karla', -apple-system, sans-serif;
  --font-mono:    'GW Mono', 'Courier New', monospace;
  --font-script:  'GW Caveat', cursive;

  --content-w: 720px;
  --nav-h: 60px;
  color-scheme: light;
}}

*, *::before, *::after {{ box-sizing: border-box; }}

@media (prefers-reduced-motion: reduce) {{
  *, *::before, *::after {{
    animation-duration: .001ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .001ms !important;
  }}
}}

/* Anchor-nav scrolling is driven by GSAP's ScrollToPlugin (see scripts at
   the end of the document), not CSS scroll-behavior: smooth — that CSS
   property fights with ScrollTrigger's own scroll listener (both try to
   own the scroll position at once), which is what caused the jumpy,
   half-animated scroll instead of a clean one. */
html {{ scroll-behavior: auto; }}

html {{
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
  overflow-x: hidden;
}}

/* Belt-and-braces against the full-bleed sections (.masthead, .hero,
   .jump, .gallery) ever pushing the page a few pixels wider than the
   viewport on very narrow phones — those all use the standard
   `calc(50% - 50vw)` breakout trick, which can overshoot by a
   scrollbar's width on browsers that reserve space for one. */
body {{
  margin: 0;
  background: var(--cream);
  color: var(--ink);
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}}

img, svg {{ display: block; max-width: 100%; }}
a {{ color: inherit; }}
table {{ border-collapse: collapse; width: 100%; }}

a:focus-visible, button:focus-visible {{
  outline: 2px solid var(--gold);
  outline-offset: 3px;
  border-radius: 3px;
}}

.board {{ max-width: var(--content-w); margin: 0 auto; padding: 0 22px 90px; }}

/* ============ site nav ============ */
/* Brought over from the main WordPress theme's header.php nav (same
   sticky-blur, logo mark, underline-on-hover links, is-scrolled shadow
   state) — adapted to this site's two real pages (Home/Menu) instead of
   the full site's six section anchors, and to a WhatsApp CTA instead of
   a #contact form that doesn't exist here. */
.nav {{
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(251,243,231,.85);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid transparent;
  transition: border-color .3s ease, box-shadow .3s ease;
}}
.nav.is-scrolled {{ border-color: var(--line); box-shadow: 0 6px 20px -14px rgba(43,27,20,.3); }}
.nav-inner {{
  max-width: 1180px;
  margin: 0 auto;
  padding: 15px 22px;
  display: flex;
  align-items: center;
  gap: 24px;
}}
.nav-logo {{
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: var(--font-display);
  font-size: 1.05rem;
  color: var(--ink);
  text-decoration: none;
  margin-right: auto;
  white-space: nowrap;
}}
.whisk-mark {{ width: 26px; height: 26px; color: var(--jam); flex-shrink: 0; }}
.nav-links {{ display: flex; gap: 26px; }}
.nav-links a {{
  font-family: var(--font-karla);
  font-size: .88rem;
  font-weight: 600;
  color: var(--ink-70);
  text-decoration: none;
  position: relative;
  padding: 4px 0;
  transition: color .2s ease;
}}
.nav-links a::after {{
  content: '';
  position: absolute; left: 0; right: 100%; bottom: -3px; height: 2.5px;
  border-radius: 2px;
  background: var(--jam);
  transition: right .3s ease;
}}
.nav-links a:hover {{ color: var(--ink); }}
.nav-links a:hover::after {{ right: 0; }}
.nav-links a.is-current {{ color: var(--ink); }}
.nav-links a.is-current::after {{ right: 0; background: var(--gold); }}
.nav-cta {{
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: .5em;
  padding: .6em 1.3em;
  border-radius: 100px;
  background: var(--jam);
  color: var(--paper);
  font-family: var(--font-karla);
  font-weight: 700;
  font-size: .82rem;
  text-decoration: none;
  white-space: nowrap;
  box-shadow: 0 10px 22px -10px rgba(178,58,72,.5);
  transition: background .2s ease, transform .2s ease;
}}
.nav-cta:hover {{ background: var(--jam-deep); transform: translateY(-1px); }}
.nav-toggle {{
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  padding: 6px;
  cursor: pointer;
}}
.nav-toggle span {{ width: 22px; height: 2px; background: var(--ink); border-radius: 2px; }}
.nav-mobile {{
  display: none;
  flex-direction: column;
  gap: 2px;
  padding: 8px 22px 20px;
  border-top: 1px solid var(--line);
}}
.nav-mobile a {{
  font-family: var(--font-karla);
  font-weight: 600;
  padding: 12px 0;
  border-bottom: 1px solid rgba(43,27,20,.09);
  text-decoration: none;
  color: var(--ink-70);
}}
.nav-mobile .nav-cta {{ margin-top: 14px; }}

@media (max-width: 640px) {{
  .nav-links, .nav-cta {{ display: none; }}
  .nav-toggle {{ display: flex; }}
  .nav-mobile.is-open {{ display: flex; }}
}}

/* ============ hero (brought over from the main WordPress homepage) ============ */
/* Home page only — the Menu page keeps its own simpler masthead below.
   Copy, stats, and the scattered-ingredient illustrations are verbatim
   from the WordPress theme's front-page.php; only the two action links
   were repointed at pages/contacts that actually exist on this site. */
.hero {{
  position: relative;
  margin: 0 calc(50% - 50vw) 0;
  padding: 96px 22px 110px;
  min-height: min(80vh, 760px);
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  overflow: hidden;
}}
.hero-flour {{ position: absolute; inset: 0; pointer-events: none; z-index: 0; }}
.hero-inner {{ position: relative; z-index: 2; max-width: 780px; margin: 0 auto; }}
.hero-eyebrow {{ opacity: 0; }}
.hero-script {{
  font-family: var(--font-script);
  font-size: clamp(1.4rem, 2.6vw, 1.9rem);
  font-weight: 600;
  color: var(--jam);
  transform: rotate(-2deg);
  display: inline-block;
  margin: 0 0 .35em;
}}
.hero-title {{
  font-family: var(--font-display);
  font-weight: 600;
  font-size: clamp(2.3rem, 5.4vw, 4rem);
  line-height: 1.08;
  color: var(--ink);
  letter-spacing: -.01em;
  margin: 0 0 .45em;
}}
.hero-title .line {{ display: block; overflow: hidden; }}
.hero-title em {{ font-style: italic; color: var(--jam); }}
.hero-sub {{
  font-family: var(--font-karla);
  max-width: 52ch;
  margin: 0 auto 1em;
  font-size: 1.04rem;
  color: var(--ink-70);
  opacity: 0;
}}
.hero-actions {{ display: flex; gap: 16px; flex-wrap: wrap; justify-content: center; margin: 24px 0 44px; opacity: 0; }}
.hero-actions .btn {{ margin-top: 0; }}
.hero-actions .btn-ghost {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 26px;
  border-radius: 100px;
  background: transparent;
  color: var(--ink);
  border: 1.5px solid var(--ink-45);
  font-family: var(--font-karla);
  font-weight: 700;
  font-size: .88rem;
  text-decoration: none;
  transition: border-color .2s ease, transform .2s ease;
}}
.hero-actions .btn-ghost:hover {{ border-color: var(--ink); transform: translateY(-1px); }}
.hero-stats {{ display: flex; gap: 40px; justify-content: center; opacity: 0; }}
.hero-stats strong {{ display: block; font-family: var(--font-display); font-size: 1.5rem; color: var(--jam); }}
.hero-stats span {{ font-family: var(--font-karla); font-size: .8rem; color: var(--ink-70); }}

.hero-scatter {{ position: absolute; inset: 0; z-index: 1; pointer-events: none; }}
.scatter-item {{ position: absolute; filter: drop-shadow(0 12px 14px rgba(43,27,20,.14)); }}
.scatter-item svg {{ width: 100%; height: auto; }}
.sc-wheat {{    top: 9%;    left: 4%;   width: 52px; transform: rotate(-20deg); }}
.sc-sprig {{    top: 7%;    right: 5.5%;width: 50px; transform: rotate(26deg); }}
.sc-butter {{   top: 33%;   left: 2.5%; width: 62px; transform: rotate(9deg); }}
.sc-anise {{    top: 13%;   right: 17%; width: 38px; transform: rotate(14deg); }}
.sc-citrus {{   top: 41%;   right: 2.5%;width: 72px; transform: rotate(12deg); }}
.sc-berries {{  top: 68%;   right: 11%; width: 48px; transform: rotate(-10deg); }}
.sc-cookie {{   top: 58%;   left: 8%;   width: 54px; transform: rotate(16deg); }}
.sc-egg {{      bottom: 15%;left: 4.5%; width: 42px; transform: rotate(-12deg); }}
.sc-cinnamon {{ bottom: 13%;right: 6%;  width: 74px; transform: rotate(-6deg); }}
.sc-whisk {{    bottom: 9%; left: 21%;  width: 32px; transform: rotate(20deg); }}
.sc-stamp {{    top: 12%;   left: 15%;  width: 100px; }}

.stamp {{ animation: gw-spin 26s linear infinite; }}
.stamp text {{
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: 10.5px;
  letter-spacing: .2em;
  fill: var(--gold-dark);
  text-transform: uppercase;
}}
.stamp .stamp-star {{ fill: var(--jam); }}
@keyframes gw-spin {{ to {{ transform: rotate(360deg); }} }}

.hero-tear {{ position: absolute; left: 0; right: 0; bottom: -1px; z-index: 3; line-height: 0; }}
.hero-tear svg {{ width: 100%; height: 48px; display: block; }}

@media (max-width: 900px) {{
  .hero {{ padding: 64px 22px 96px; min-height: 0; }}
  .sc-butter, .sc-cookie, .sc-berries, .sc-whisk, .sc-anise, .sc-stamp {{ display: none; }}
  .sc-wheat {{ width: 40px; }}
  .sc-sprig {{ width: 38px; }}
  .sc-citrus {{ width: 54px; top: 30%; }}
  .sc-cinnamon {{ width: 58px; }}
  .sc-egg {{ width: 34px; }}
  .hero-stats {{ gap: 24px; }}
}}

/* ============ buttons ============ */
.btn {{
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-top: 22px;
  padding: 12px 26px;
  border-radius: 100px;
  background: var(--gold);
  color: var(--board);
  font-family: var(--font-body);
  font-weight: 600;
  font-size: .88rem;
  text-decoration: none;
  box-shadow: 0 10px 22px -10px rgba(200,155,60,.5);
  transition: background .2s ease, transform .2s ease;
}}
.btn:hover {{ background: #E0B356; transform: translateY(-1px); }}

/* ============ masthead ============ */
/* The rest of the page is now a light paper theme (matching the main
   WordPress site), but the masthead itself is unchanged — it keeps the
   exact dark backdrop the whole page used to have, now given its own
   full-bleed background instead of inheriting it from <body>. */
.masthead {{
  text-align: center;
  margin: 0 calc(50% - 50vw) 0;
  padding: 72px 22px 34px;
  background:
    radial-gradient(ellipse 90% 60% at 50% -10%, rgba(200,155,60,.10), transparent 60%),
    var(--board);
}}
.mark {{
  width: 46px; height: 46px;
  margin: 0 auto 22px;
  color: var(--gold);
}}
.eyebrow {{
  font-family: var(--font-body);
  font-weight: 600;
  font-size: .72rem;
  letter-spacing: .18em;
  text-transform: uppercase;
  color: var(--gold);
  margin: 0 0 18px;
}}
.wordmark {{
  font-family: 'GW DM Serif Text', Georgia, serif;
  font-weight: 400;
  font-size: clamp(2.4rem, 8vw, 3.6rem);
  line-height: 1.05;
  margin: 0 0 14px;
  letter-spacing: -.01em;
  text-wrap: balance;
  background: linear-gradient(180deg, #F3DFA0 0%, var(--gold) 65%, #9C7527 100%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}}
.note {{
  font-family: var(--font-script);
  font-size: 1.5rem;
  color: var(--cream);
  max-width: 34ch;
  transform: rotate(-1.4deg);
  margin: 0 auto 26px;
}}
.intro {{
  max-width: 46ch;
  margin: 0 auto;
  color: var(--cream-60);
  font-size: .96rem;
}}

/* Entrance and parallax are applied by GSAP at runtime (see scripts at the
   end of the document) so the masthead still reads fine with JS disabled —
   nothing here is hidden by default CSS. */

/* ============ category jump nav ============ */
.jump {{
  position: sticky;
  top: var(--nav-h);
  z-index: 40;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px;
  margin: 0 calc(50% - 50vw) 30px;
  padding: 14px 22px;
  background: rgba(251,243,231,.85);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--line);
}}
.jump a {{
  font-family: var(--font-karla);
  font-weight: 700;
  font-size: .68rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  text-decoration: none;
  color: var(--ink-70);
  border: 1px solid var(--line);
  border-radius: 100px;
  padding: 7px 14px;
  transition: border-color .2s ease, color .2s ease, background .2s ease;
}}
.jump a:hover,
.jump a.is-active {{
  color: var(--board);
  background: var(--gold);
  border-color: var(--gold);
}}

/* ============ custom-cake gallery ============ */
/* Breaks out to a wider column than the 720px reading width, same trick
   as .jump — four photocards side by side need more room than a single
   paragraph does. */
.gallery {{
  margin: 0 calc(50% - 50vw) 56px;
  padding: 0 22px;
}}
.gallery-inner {{
  max-width: 1120px;
  margin: 0 auto;
}}
.gallery-intro {{
  max-width: 560px;
  margin: 0 auto 36px;
  text-align: center;
}}
/* The masthead's .eyebrow stays Inter (header, unchanged) — this section
   isn't the header, so its eyebrow matches the main theme's actual
   pattern instead, where eyebrows use the mono face, not the body one. */
.gallery-intro .eyebrow {{
  font-family: var(--font-mono);
  font-weight: 400;
  letter-spacing: .14em;
}}
.gallery-heading {{
  font-family: var(--font-display);
  font-weight: 600;
  font-size: clamp(1.6rem, 3vw, 2.1rem);
  color: var(--ink);
  text-wrap: balance;
  margin: 0 0 .5em;
}}
.gallery-sub {{
  font-family: var(--font-karla);
  font-size: .95rem;
  color: var(--ink-70);
  margin: 0;
}}

.photocard-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}}
.photocard {{
  background: var(--paper);
  border-radius: 20px;
  padding: 12px 12px 20px;
  box-shadow: 0 18px 32px -18px rgba(0,0,0,.55);
}}
.photocard-img {{
  border-radius: 14px;
  overflow: hidden;
  aspect-ratio: 1 / 0.94;
  margin-bottom: 16px;
  background: var(--paper-alt);
}}
.photocard-img img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
.photocard h3 {{
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 1.14rem;
  line-height: 1.22;
  color: var(--ink);
  margin: 0 6px 10px;
  text-wrap: balance;
}}
.photocard-desc {{
  font-family: var(--font-karla);
  font-size: .84rem;
  line-height: 1.55;
  color: var(--ink-70);
  margin: 0 6px 16px;
}}
.photocard-divider {{
  height: 1px;
  background: var(--line);
  margin: 0 6px 12px;
}}
.photocard-foot {{
  font-family: var(--font-karla);
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin: 0 6px;
  font-size: .78rem;
}}
.photocard-foot span {{ color: var(--ink-45); }}
.photocard-foot strong {{
  font-weight: 600;
  color: var(--jam-deep);
}}

@media (max-width: 900px) {{
  .photocard-grid {{ grid-template-columns: repeat(2, 1fr); }}
}}
@media (max-width: 560px) {{
  .gallery {{ padding: 0 18px; margin-bottom: 44px; }}
  .photocard-grid {{ grid-template-columns: 1fr; gap: 18px; }}
}}

/* ============ category cards ============ */
.category {{
  margin-bottom: 30px;
  /* Starting hidden state is applied by GSAP at runtime, not here, so the
     board still reads fine with JS disabled. */
}}

.card {{
  position: relative;
  background: var(--paper);
  background-image: repeating-linear-gradient(var(--paper) 0 26px, rgba(43,27,20,.05) 27px);
  border-radius: 3px;
  padding: 30px 26px 12px;
  box-shadow: 0 18px 34px -18px rgba(0,0,0,.55), 0 2px 0 rgba(0,0,0,.08);
}}
.card::before {{
  content: '';
  position: absolute; left: 0; top: 0; bottom: 0; width: 30px;
  background: repeating-linear-gradient(rgba(43,27,20,.05) 0 1px, transparent 1px 8px);
  border-right: 1px solid var(--line);
}}
.pin {{
  position: absolute; top: -9px; left: 34px;
  width: 15px; height: 15px; border-radius: 50%;
  background: radial-gradient(circle at 35% 30%, #E7566A, var(--jam-deep));
  box-shadow: 0 3px 5px rgba(0,0,0,.4);
}}
.card-head {{
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 12px;
  padding-left: 12px;
  margin-bottom: 6px;
}}
.card-head h2 {{
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 1.35rem;
  color: var(--ink);
  margin: 0;
}}
.count {{
  font-family: var(--font-mono);
  font-size: .68rem;
  letter-spacing: .06em;
  text-transform: uppercase;
  color: var(--ink-45);
  white-space: nowrap;
}}
.card-note {{
  font-family: var(--font-karla);
  padding-left: 12px;
  font-size: .82rem;
  color: var(--ink-45);
  margin: 0 0 10px;
}}

.table-wrap {{ padding-left: 12px; overflow-x: auto; }}

table {{ font-size: .92rem; }}
thead th {{
  text-align: right;
  font-family: var(--font-mono);
  font-weight: 400;
  font-size: .64rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  color: var(--ink-45);
  padding: 8px 4px 8px 10px;
  border-bottom: 1px solid var(--line);
  white-space: nowrap;
}}
thead th.col-name {{ text-align: left; padding-left: 0; }}
tbody td {{
  padding: 10px 4px 10px 10px;
  border-bottom: 1px dashed var(--line);
  white-space: nowrap;
}}
tbody tr:last-child td {{ border-bottom: none; }}
td.name {{
  font-family: var(--font-karla);
  font-weight: 600;
  color: var(--ink);
  padding-left: 0;
  white-space: normal;
}}
td.price {{
  font-family: var(--font-mono);
  font-weight: 700;
  color: var(--jam-deep);
  text-align: right;
  font-variant-numeric: tabular-nums;
}}
.table-2col td.price {{ color: var(--jam-deep); }}
.unit {{
  font-family: var(--font-karla);
  font-weight: 400;
  font-size: .72rem;
  color: var(--ink-45);
}}
.dash {{ color: var(--ink-45); }}

/* ============ footer ============ */
/* A dark card echoing the masthead, so the sign-off still reads as a
   bold closing note rather than fading into the light paper page. */
.board-footer {{
  text-align: center;
  margin-top: 14px;
  padding: 40px 24px 34px;
  border-radius: 20px;
  background: var(--board);
}}
.board-footer p {{
  font-family: var(--font-karla);
  font-size: .82rem;
  color: var(--cream-40);
  max-width: 48ch;
  margin: 0 auto .9em;
}}
/* .board-footer .signoff, not just .signoff: ".board-footer p" above is
   more specific than a bare class selector, so it was winning the
   cascade and silently overriding this back to Karla — the footer
   sign-off was rendering in the wrong font despite this rule existing. */
.board-footer .signoff {{
  font-family: var(--font-script);
  font-size: 1.4rem;
  color: var(--gold);
  transform: rotate(-1deg);
}}
.contact {{
  font-family: var(--font-karla);
  font-size: .8rem;
  letter-spacing: .01em;
  color: var(--cream-60) !important;
}}
.contact a {{
  color: var(--gold) !important;
  font-weight: 600;
  text-decoration: underline;
  text-decoration-color: var(--gold-soft);
  text-underline-offset: 3px;
  transition: text-decoration-color .2s ease;
}}
.contact a:hover,
.contact a:focus-visible {{
  text-decoration-color: var(--gold);
}}
.top-link {{
  display: inline-block;
  margin-top: 22px;
  font-family: var(--font-mono);
  font-weight: 700;
  font-size: .68rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  text-decoration: none;
  color: var(--gold);
  border-bottom: 1px solid var(--gold-soft);
  padding-bottom: 2px;
}}

/* ============ floating back-to-top button ============ */
.back-to-top {{
  position: fixed;
  right: 22px;
  bottom: 22px;
  z-index: 50;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--gold);
  color: var(--board);
  box-shadow: 0 10px 22px -8px rgba(0,0,0,.55);
  cursor: pointer;
  opacity: 0;
  transform: translateY(12px) scale(.9);
  pointer-events: none;
  transition: opacity .3s ease, transform .3s ease, background .2s ease;
}}
.back-to-top.is-visible {{
  opacity: 1;
  transform: translateY(0) scale(1);
  pointer-events: auto;
}}
.back-to-top:hover {{
  background: #E0B356;
}}
.back-to-top svg {{
  width: 20px;
  height: 20px;
}}

@media (max-width: 480px) {{
  .back-to-top {{ right: 14px; bottom: 14px; width: 44px; height: 44px; }}
  .back-to-top svg {{ width: 18px; height: 18px; }}
}}

/* Handheld sizing: legibility first — small utility text (badges, table
   headers, footer/contact lines) gets LARGER here, never smaller, since
   the whole point of this pass is readability on a phone screen. Layout
   spacing tightens instead, to give the same text more room. */
@media (max-width: 640px) {{
  .board {{ padding: 0 18px 70px; }}
  .masthead {{ padding: 56px 0 28px; }}
  .intro {{ font-size: 1rem; }}
  .eyebrow {{ font-size: .78rem; }}
  .jump {{ gap: 6px; padding: 12px 18px; }}
  .jump a {{ font-size: .74rem; padding: 7px 12px; }}
  .card-head h2 {{ font-size: 1.5rem; }}
  .count {{ font-size: .74rem; }}
  table {{ font-size: 1rem; }}
  thead th {{ font-size: .7rem; }}
  .unit {{ font-size: .8rem; }}
  .board-footer p {{ font-size: .9rem; }}
  .contact {{ font-size: .88rem; }}
  .top-link {{ font-size: .74rem; }}
}}

@media (max-width: 480px) {{
  .board {{ padding: 0 14px 60px; }}
  .masthead {{ padding: 48px 0 24px; }}
  .jump {{ padding: 10px 14px; }}
  .card {{ padding: 24px 14px 10px; }}
  .card-head {{ padding-left: 8px; flex-direction: column; align-items: flex-start; gap: 4px; }}
  .table-wrap {{ padding-left: 8px; }}
  thead th {{ padding: 8px 3px 8px 6px; }}
  tbody td {{ padding: 11px 3px 11px 6px; }}
}}
</style>

{body}

<script>__GSAP_JS__</script>
<script>__SCROLLTRIGGER_JS__</script>
<script>__SCROLLTOPLUGIN_JS__</script>
<script>__ANIMATION_JS__</script>
"""

# ---- shared page chrome: top nav, masthead, footer, back-to-top ----
# Two separate HTML documents (index.html, menu.html) share this chrome
# but each is fully self-contained (fonts/CSS/JS all inlined again in
# both) — there's no client-side router here, so nothing CAN be shared
# at the browser level anyway. The cost is that navigating between the
# two pages re-downloads the ~450KB of embedded fonts/JS rather than
# reusing a cached external file; accepted for now since this is a
# two-page site with light traffic, not a place to add a build step for
# extracting shared assets. Worth revisiting if a third page joins.

WHISK_MARK_SVG = """<svg class="whisk-mark" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <g stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
        <line x1="20" y1="5" x2="20" y2="14"/>
        <line x1="20" y1="26" x2="20" y2="35"/>
        <line x1="5" y1="20" x2="14" y2="20"/>
        <line x1="26" y1="20" x2="35" y2="20"/>
        <line x1="9.4" y1="9.4" x2="15.8" y2="15.8"/>
        <line x1="24.2" y1="24.2" x2="30.6" y2="30.6"/>
        <line x1="30.6" y1="9.4" x2="24.2" y2="15.8"/>
        <line x1="15.8" y1="24.2" x2="9.4" y2="30.6"/>
      </g>
      <circle cx="20" cy="20" r="3.4" fill="currentColor"/>
    </svg>"""

# Brought over from the main WordPress theme's header.php nav — same
# sticky-blur bar, logo mark, and mobile toggle, but linking to this
# site's actual two pages plus a WhatsApp CTA (the theme's nav links to
# six sections of one long homepage that don't exist on this stand-in).
def wp_nav(active):
    def link(href, label, key):
        cls = ' class="is-current"' if key == active else ""
        return f'<a href="{href}"{cls}>{label}</a>'
    return f"""
  <header class="nav" id="nav">
    <div class="nav-inner">
      <a href="index.html" class="nav-logo" aria-label="The Golden Whisk home">
        {WHISK_MARK_SVG}
        <span>The Golden&nbsp;Whisk</span>
      </a>
      <nav class="nav-links" aria-label="Primary">
        {link("index.html", "Home", "home")}
      </nav>
      <a href="https://wa.me/919872347816" class="nav-cta">Order on WhatsApp</a>
      <button class="nav-toggle" id="navToggle" aria-label="Open menu" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
    <div class="nav-mobile" id="navMobile">
      {link("index.html", "Home", "home")}
      <a href="https://wa.me/919872347816" class="nav-cta">Order on WhatsApp</a>
    </div>
  </header>"""

def masthead_html(intro, cta=""):
    return f"""
  <header class="masthead" id="top">
    <svg class="mark" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <g stroke="currentColor" stroke-width="2.2" stroke-linecap="round">
        <line x1="20" y1="5" x2="20" y2="14"/>
        <line x1="20" y1="26" x2="20" y2="35"/>
        <line x1="5" y1="20" x2="14" y2="20"/>
        <line x1="26" y1="20" x2="35" y2="20"/>
        <line x1="9.4" y1="9.4" x2="15.8" y2="15.8"/>
        <line x1="24.2" y1="24.2" x2="30.6" y2="30.6"/>
        <line x1="30.6" y1="9.4" x2="24.2" y2="15.8"/>
        <line x1="15.8" y1="24.2" x2="9.4" y2="30.6"/>
      </g>
      <circle cx="20" cy="20" r="3.4" fill="currentColor"/>
    </svg>
    <p class="eyebrow">Chandigarh Tricity</p>
    <h1 class="wordmark">The Golden Whisk</h1>
    <p class="note">the full site is still baking — here's today's board</p>
    <p class="intro">{intro}</p>
    {cta}
  </header>"""

# The main WordPress homepage's hero, brought over as-is — copy, stats,
# and the scattered hand-drawn ingredient illustrations are verbatim from
# front-page.php. Only the two action links were repointed: "See the
# Menu" goes to menu.html instead of a WP menu-page permalink, and
# "Order for This Weekend" goes to WhatsApp instead of a #contact section
# this stand-in site doesn't have.
HOME_HERO_HTML = """
  <section class="hero" id="top">
    <div class="hero-flour" id="flourLayer" aria-hidden="true"></div>

    <div class="hero-scatter" id="heroScatter" aria-hidden="true">

      <span class="scatter-item sc-wheat">
        <svg viewBox="0 0 44 120" xmlns="http://www.w3.org/2000/svg">
          <path d="M22 118 C22 84 22 52 22 14" stroke="#9C7527" stroke-width="2.5" fill="none"/>
          <g fill="#E8C874" stroke="#C89B3C" stroke-width="1">
            <ellipse cx="22" cy="12" rx="5.5" ry="10"/>
            <ellipse cx="15" cy="26" rx="5.5" ry="10" transform="rotate(-26 15 26)"/>
            <ellipse cx="29" cy="26" rx="5.5" ry="10" transform="rotate(26 29 26)"/>
            <ellipse cx="14" cy="44" rx="5.5" ry="10" transform="rotate(-26 14 44)"/>
            <ellipse cx="30" cy="44" rx="5.5" ry="10" transform="rotate(26 30 44)"/>
            <ellipse cx="14" cy="62" rx="5.5" ry="10" transform="rotate(-26 14 62)"/>
            <ellipse cx="30" cy="62" rx="5.5" ry="10" transform="rotate(26 30 62)"/>
          </g>
        </svg>
      </span>

      <span class="scatter-item sc-sprig">
        <svg viewBox="0 0 60 110" xmlns="http://www.w3.org/2000/svg">
          <path d="M30 106 C 26 70 30 40 34 8" stroke="#9C7527" stroke-width="2.2" fill="none"/>
          <g fill="#C89B3C">
            <ellipse cx="34" cy="12" rx="9" ry="4.6" transform="rotate(60 34 12)"/>
            <ellipse cx="18" cy="28" rx="10" ry="5" transform="rotate(-32 18 28)"/>
            <ellipse cx="44" cy="38" rx="10" ry="5" transform="rotate(28 44 38)"/>
            <ellipse cx="16" cy="52" rx="10" ry="5" transform="rotate(-30 16 52)"/>
            <ellipse cx="44" cy="64" rx="10" ry="5" transform="rotate(26 44 64)"/>
            <ellipse cx="18" cy="78" rx="10" ry="5" transform="rotate(-28 18 78)"/>
          </g>
        </svg>
      </span>

      <span class="scatter-item sc-butter">
        <svg viewBox="0 0 70 50" xmlns="http://www.w3.org/2000/svg">
          <path d="M8 20 L34 10 L62 16 L62 30 L36 42 L8 34 Z" fill="#F4E3BE" stroke="#D9B96A" stroke-width="1.5"/>
          <path d="M8 20 L36 28 L62 16" fill="none" stroke="#D9B96A" stroke-width="1.5"/>
          <path d="M36 28 L36 42" stroke="#D9B96A" stroke-width="1.5"/>
        </svg>
      </span>

      <span class="scatter-item sc-anise">
        <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
          <g fill="#7A4B2A">
            <path d="M30 30 L24 12 A8 8 0 0 1 36 12 Z"/>
            <path d="M30 30 L24 12 A8 8 0 0 1 36 12 Z" transform="rotate(45 30 30)"/>
            <path d="M30 30 L24 12 A8 8 0 0 1 36 12 Z" transform="rotate(90 30 30)"/>
            <path d="M30 30 L24 12 A8 8 0 0 1 36 12 Z" transform="rotate(135 30 30)"/>
            <path d="M30 30 L24 12 A8 8 0 0 1 36 12 Z" transform="rotate(180 30 30)"/>
            <path d="M30 30 L24 12 A8 8 0 0 1 36 12 Z" transform="rotate(225 30 30)"/>
            <path d="M30 30 L24 12 A8 8 0 0 1 36 12 Z" transform="rotate(270 30 30)"/>
            <path d="M30 30 L24 12 A8 8 0 0 1 36 12 Z" transform="rotate(315 30 30)"/>
          </g>
          <circle cx="30" cy="30" r="6" fill="#5C3720"/>
        </svg>
      </span>

      <span class="scatter-item sc-citrus">
        <svg viewBox="0 0 70 70" xmlns="http://www.w3.org/2000/svg">
          <circle cx="35" cy="35" r="32" fill="#B23A48"/>
          <circle cx="35" cy="35" r="26" fill="#D98590"/>
          <g stroke="#FBF3E7" stroke-width="3" stroke-linecap="round">
            <line x1="35" y1="12" x2="35" y2="58"/>
            <line x1="12" y1="35" x2="58" y2="35"/>
            <line x1="19" y1="19" x2="51" y2="51"/>
            <line x1="51" y1="19" x2="19" y2="51"/>
          </g>
          <circle cx="35" cy="35" r="4" fill="#FBF3E7"/>
        </svg>
      </span>

      <span class="scatter-item sc-berries">
        <svg viewBox="0 0 54 44" xmlns="http://www.w3.org/2000/svg">
          <ellipse cx="16" cy="12" rx="9" ry="4.5" fill="#C89B3C" transform="rotate(-24 16 12)"/>
          <circle cx="16" cy="28" r="9" fill="#B23A48"/>
          <circle cx="33" cy="32" r="8" fill="#D06070"/>
          <circle cx="40" cy="16" r="7" fill="#8E2A36"/>
        </svg>
      </span>

      <span class="scatter-item sc-cookie">
        <svg viewBox="0 0 60 60" xmlns="http://www.w3.org/2000/svg">
          <circle cx="30" cy="30" r="27" fill="#CE9C62" stroke="#B98449" stroke-width="2"/>
          <g fill="#5C3B26">
            <circle cx="21" cy="22" r="3.4"/>
            <circle cx="38" cy="18" r="3"/>
            <circle cx="42" cy="34" r="3.4"/>
            <circle cx="27" cy="40" r="3"/>
            <circle cx="15" cy="34" r="2.6"/>
            <circle cx="33" cy="29" r="2.8"/>
          </g>
        </svg>
      </span>

      <span class="scatter-item sc-egg">
        <svg viewBox="0 0 46 58" xmlns="http://www.w3.org/2000/svg">
          <path d="M23 3 C34 3 43 20 43 35 A20 20 0 0 1 3 35 C3 20 12 3 23 3 Z" fill="#FBF7EC" stroke="#DFD5BE" stroke-width="1.5"/>
          <path d="M14 14 C11 20 10 24 10 30" stroke="#EFE7D3" stroke-width="3" fill="none" stroke-linecap="round"/>
        </svg>
      </span>

      <span class="scatter-item sc-cinnamon">
        <svg viewBox="0 0 80 60" xmlns="http://www.w3.org/2000/svg">
          <rect x="6" y="24" width="68" height="11" rx="5.5" fill="#8B5E3C" transform="rotate(-14 40 30)"/>
          <rect x="6" y="24" width="68" height="11" rx="5.5" fill="#7A4E2E" transform="rotate(12 40 30)"/>
        </svg>
      </span>

      <span class="scatter-item sc-whisk">
        <svg viewBox="0 0 40 90" fill="none" xmlns="http://www.w3.org/2000/svg">
          <rect x="16" y="4" width="8" height="26" rx="4" stroke="#2B1B14" stroke-width="2.2"/>
          <path d="M20 30 C6 42 6 62 20 74 C34 62 34 42 20 30 Z" stroke="#2B1B14" stroke-width="2"/>
          <path d="M20 30 C14 44 14 60 20 74" stroke="#2B1B14" stroke-width="1.6"/>
          <path d="M20 30 C26 44 26 60 20 74" stroke="#2B1B14" stroke-width="1.6"/>
        </svg>
      </span>

      <span class="scatter-item sc-stamp">
        <svg class="stamp" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <path id="stampCircle" d="M64,64 m-50,0 a50,50 0 1,1 100,0 a50,50 0 1,1 -100,0"/>
          </defs>
          <text><textPath href="#stampCircle">Baked to order · Small batch · Mohali ·</textPath></text>
          <path class="stamp-star" d="M64 44 L68 60 L84 64 L68 68 L64 84 L60 68 L44 64 L60 60 Z"/>
        </svg>
      </span>

    </div>

    <div class="hero-inner">
      <p class="hero-eyebrow hero-script" data-reveal>baked only when you order</p>
      <h1 class="hero-title">
        <span class="line" data-line>Baked with butter,</span>
        <span class="line" data-line>patience, and a <em>little</em> chaos.</span>
      </h1>
      <p class="hero-sub" data-reveal>
        The Golden Whisk is a one-woman, one-oven bakery serving the Chandigarh Tricity,
        taking orders for customised celebration cakes, dry cakes, cookies, and breads.
        Nothing sits ready on a shelf — every single bake starts only after your order
        comes in.
      </p>
      <div class="hero-actions" data-reveal>
        <a href="https://wa.me/919872347816" class="btn">Order for This Weekend</a>
      </div>
      <div class="hero-stats" data-reveal>
        <div><strong>2019</strong><span>Baking since</span></div>
        <div><strong>4.9★</strong><span>from 300+ orders</span></div>
        <div><strong>100%</strong><span>made to order</span></div>
      </div>
    </div>

    <div class="hero-tear" aria-hidden="true">
      <svg viewBox="0 0 1200 70" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M0 70 L0 45 L35 52 L70 38 L105 50 L140 34 L180 48 L215 40 L255 55 L290 37 L330 49 L365 35 L405 51 L440 42 L480 54 L515 36 L555 50 L590 40 L630 53 L665 38 L705 49 L740 35 L780 52 L815 43 L855 55 L890 37 L930 50 L965 41 L1005 54 L1040 36 L1080 48 L1115 40 L1155 52 L1200 44 L1200 70 Z" fill="#FBF3E7"/>
      </svg>
    </div>
  </section>"""

def footer_html(extra=""):
    return f"""
  <footer class="board-footer">
    {extra}
    <p class="signoff">made with love in a home kitchen</p>
    <p class="contact">To order: WhatsApp <a href="https://wa.me/919872347816">98723 47816</a></p>
    <a class="top-link" href="#top">Back to top</a>
  </footer>"""

BACK_TO_TOP_HTML = """
<button class="back-to-top" id="backToTop" type="button" aria-label="Back to top">
  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path d="M12 19V6M12 6L6 12M12 6L18 12" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</button>"""

MENU_INTRO = ("Every cake below is mixed and iced only after you order it — nothing sits "
              "ready on a shelf. Two sizes on most flavours: a 1&nbsp;kg cake serves about "
              "12–15, a 650&nbsp;g serves about 8–10. Message us on WhatsApp with your "
              "flavour, size, and the date you need it.")

MENU_FOOTER_NOTE = ("<p>Prices in ₹. A 1&nbsp;kg cake serves about 12–15 guests, a "
                     "650&nbsp;g serves about 8–10 — sizes are approximate cake weight, "
                     "not a guaranteed ingredient count.</p>")

HOME_MAIN = f"""
  <section class="gallery">
    <div class="gallery-inner">
      <div class="gallery-intro">
        <p class="eyebrow">Custom Cakes</p>
        <h2 class="gallery-heading">A Few Recent Favourites</h2>
        <p class="gallery-sub">Every custom cake starts with a conversation, not a catalogue — this is a small sample of what's come out of the oven lately.</p>
      </div>
      <div class="photocard-grid">
{GALLERY_HTML}
      </div>
    </div>
  </section>"""

MENU_MAIN = f"""
  <nav class="jump" aria-label="Jump to a category">
    <a href="#fruit">Fruit</a>
    <a href="#chocolate">Chocolate</a>
    <a href="#signature">Signature</a>
    <a href="#wholesome">Wholesome</a>
    <a href="#piece">By the Piece</a>
  </nav>

{CATEGORIES_HTML}"""

def render_body(nav_active, intro, cta, main_html, footer_extra):
    return (
        wp_nav(nav_active)
        + '\n<div class="board">\n'
        + masthead_html(intro, cta)
        + "\n"
        + main_html
        + "\n"
        + footer_html(footer_extra)
        + "\n\n</div>\n"
        + BACK_TO_TOP_HTML
    )

# Home gets the WordPress homepage's hero instead of the masthead — the
# Menu page keeps the simpler masthead below the same shared nav.
HOME_BODY = (
    wp_nav("home")
    + HOME_HERO_HTML
    + '\n<div class="board">\n'
    + HOME_MAIN
    + "\n"
    + footer_html("")
    + "\n\n</div>\n"
    + BACK_TO_TOP_HTML
)
MENU_BODY = render_body("menu", MENU_INTRO, "", MENU_MAIN, MENU_FOOTER_NOTE)

HOME_TITLE = "The Golden Whisk — Cake Board"
HOME_DESCRIPTION = ("The Golden Whisk — a home bakery in the Chandigarh Tricity baking "
                     "custom cakes, dry cakes, cookies, and breads, always made to order.")
MENU_TITLE = "Full Menu — The Golden Whisk"
MENU_DESCRIPTION = ("The full menu for The Golden Whisk — custom cakes, dry cakes, "
                     "cookies, and breads, priced by weight. Made to order, nothing sits "
                     "ready on a shelf.")

home_html = TEMPLATE.format(page_title=HOME_TITLE, meta_description=HOME_DESCRIPTION, body=HOME_BODY, **FONTS)
menu_html = TEMPLATE.format(page_title=MENU_TITLE, meta_description=MENU_DESCRIPTION, body=MENU_BODY, **FONTS)

# Inlined verbatim (not through .format()) so the thousands of literal { }
# in the minified library source never collide with str.format() syntax.
gsap_js = (VENDOR_DIR / "gsap.min.js").read_text()
scrolltrigger_js = (VENDOR_DIR / "ScrollTrigger.min.js").read_text()
scrolltoplugin_js = (VENDOR_DIR / "ScrollToPlugin.min.js").read_text()

animation_js = r"""
(function(){
  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);

  // Only the Menu page has a .masthead now — Home replaced it with the
  // WordPress hero (animated separately below). Scoped under .masthead
  // itself so these selectors can't accidentally match an unrelated
  // element of the same class elsewhere on the page (e.g. the gallery's
  // own .eyebrow).
  var mastheadRoot = document.querySelector('.masthead');
  var mastheadEls = mastheadRoot ? {
    mark: mastheadRoot.querySelector('.mark'),
    eyebrow: mastheadRoot.querySelector('.eyebrow'),
    wordmark: mastheadRoot.querySelector('.wordmark'),
    note: mastheadRoot.querySelector('.note'),
    intro: mastheadRoot.querySelector('.intro')
  } : null;
  var cards = gsap.utils.toArray('.category');
  var photocards = gsap.utils.toArray('.photocard');

  if (prefersReduced) {
    if (mastheadEls) {
      gsap.set([mastheadEls.mark, mastheadEls.eyebrow, mastheadEls.wordmark, mastheadEls.intro], { opacity: 1, y: 0 });
      gsap.set(mastheadEls.note, { opacity: 1, y: 0, rotate: -1.4 });
    }
    gsap.set(cards, { opacity: 1, y: 0 });
    gsap.set(photocards, { opacity: 1, y: 0 });
  } else {
    if (mastheadEls) {
    // ---- masthead entrance, orchestrated as one sequence ----
    gsap.timeline({ defaults: { ease: 'power3.out' } })
      .from(mastheadEls.mark, { opacity: 0, y: 14, duration: .7, ease: 'back.out(1.6)' }, .1)
      .from(mastheadEls.eyebrow, { opacity: 0, y: 14, duration: .6 }, .35)
      .from(mastheadEls.wordmark, { opacity: 0, y: 18, duration: .8, ease: 'power4.out' }, .5)
      .fromTo(mastheadEls.note,
        { opacity: 0, rotate: -6, y: 10 },
        { opacity: 1, rotate: -1.4, y: 0, duration: .7, ease: 'back.out(1.7)' }, .95)
      .from(mastheadEls.intro, { opacity: 0, y: 14, duration: .7 }, 1.15);

    // ---- masthead parallax: drifts up and fades as it scrolls out of view ----
    gsap.to('.masthead', {
      y: -60,
      opacity: 0.25,
      ease: 'none',
      scrollTrigger: {
        trigger: '.masthead',
        start: 'top top',
        end: 'bottom top',
        scrub: true
      }
    });
    }

    // ---- category cards: rise and fade in as each is scrolled to ----
    cards.forEach(function (card) {
      gsap.fromTo(card,
        { opacity: 0, y: 36 },
        {
          opacity: 1, y: 0, duration: .8, ease: 'power3.out',
          scrollTrigger: { trigger: card, start: 'top 88%', once: true }
        }
      );
    });

    // ---- gallery photocards: same treatment, staggered within the grid ----
    if (photocards.length) {
      gsap.fromTo(photocards,
        { opacity: 0, y: 30 },
        {
          opacity: 1, y: 0, duration: .7, ease: 'power3.out', stagger: .1,
          scrollTrigger: { trigger: '.photocard-grid', start: 'top 88%', once: true }
        }
      );
    }
  }

  // ---- jump nav: click to smooth-scroll to a section ----
  // Driven by GSAP's ScrollToPlugin rather than CSS scroll-behavior:smooth,
  // which fights with ScrollTrigger's own scroll listener and is what
  // caused the scroll to glitch/jump instead of animating cleanly.
  document.querySelectorAll('.jump a').forEach(function (a) {
    a.addEventListener('click', function (e) {
      var target = document.querySelector(a.getAttribute('href'));
      if (!target) { return; }
      e.preventDefault();
      if (prefersReduced) {
        target.scrollIntoView({ behavior: 'auto', block: 'start' });
        return;
      }
      gsap.to(window, {
        duration: 0.9,
        ease: 'power2.inOut',
        scrollTo: { y: target, offsetY: 0 }
      });
    });
  });

  // ---- jump nav: highlight the category currently in view ----
  // A state toggle, not motion, so this runs regardless of reduced-motion.
  var navLinks = {};
  document.querySelectorAll('.jump a').forEach(function (a) {
    navLinks[a.getAttribute('href').slice(1)] = a;
  });
  function setActiveNav(id) {
    Object.keys(navLinks).forEach(function (key) {
      navLinks[key].classList.toggle('is-active', key === id);
    });
  }
  cards.forEach(function (card) {
    ScrollTrigger.create({
      trigger: card,
      start: 'top 55%',
      end: 'bottom 55%',
      onToggle: function (self) { if (self.isActive) { setActiveNav(card.id); } }
    });
  });

  // ---- floating back-to-top button ----
  var backToTop = document.getElementById('backToTop');
  if (backToTop) {
    ScrollTrigger.create({
      start: 400,
      end: 'max',
      onUpdate: function (self) {
        backToTop.classList.toggle('is-visible', self.scroll() > 400);
      }
    });
    backToTop.addEventListener('click', function () {
      if (prefersReduced) {
        window.scrollTo({ top: 0, behavior: 'auto' });
        return;
      }
      gsap.to(window, { duration: 0.9, ease: 'power2.inOut', scrollTo: { y: 0 } });
    });
  }

  // ---- top nav: shadow once the page scrolls, mobile menu toggle ----
  // Brought over from the WordPress theme's main.js.
  var navBar = document.getElementById('nav');
  var navToggle = document.getElementById('navToggle');
  var navMobile = document.getElementById('navMobile');
  if (navBar) {
    ScrollTrigger.create({
      start: 'top -10',
      end: 99999,
      toggleClass: { targets: navBar, className: 'is-scrolled' }
    });
  }
  if (navToggle && navMobile) {
    navToggle.addEventListener('click', function () {
      var isOpen = navMobile.classList.toggle('is-open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
    navMobile.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        navMobile.classList.remove('is-open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // ---- hero (Home page only): ambient flour specks, load sequence,
  // scattered ingredients popping in and drifting. Brought over from the
  // WordPress theme's main.js. ----
  var flourLayer = document.getElementById('flourLayer');
  if (flourLayer && !prefersReduced) {
    var dustCount = window.innerWidth < 700 ? 8 : 16;
    var speckColors = ['rgba(200,155,60,0.35)', 'rgba(178,58,72,0.16)', 'rgba(244,227,190,0.7)'];
    for (var i = 0; i < dustCount; i++) {
      var dot = document.createElement('span');
      var size = gsap.utils.random(3, 7);
      Object.assign(dot.style, {
        position: 'absolute',
        width: size + 'px',
        height: size + 'px',
        borderRadius: '50%',
        background: speckColors[i % speckColors.length],
        left: gsap.utils.random(0, 100) + '%',
        top: gsap.utils.random(0, 100) + '%',
        pointerEvents: 'none'
      });
      flourLayer.appendChild(dot);
      gsap.to(dot, {
        y: gsap.utils.random(-40, 40),
        x: gsap.utils.random(-30, 30),
        opacity: gsap.utils.random(0.2, 0.6),
        duration: gsap.utils.random(4, 8),
        repeat: -1,
        yoyo: true,
        ease: 'sine.inOut',
        delay: gsap.utils.random(0, 3)
      });
    }
  }

  if (document.querySelector('.hero')) {
    if (prefersReduced) {
      gsap.set(['.hero-eyebrow', '.hero-sub', '.hero-actions', '.hero-stats', '[data-line]'], { opacity: 1, y: 0, yPercent: 0 });
    } else {
      var heroTl = gsap.timeline({ defaults: { ease: 'power3.out' } });
      heroTl
        .from('.hero-eyebrow', { opacity: 0, y: 14, duration: .5 })
        .to('.hero-eyebrow', { opacity: 1, y: 0, duration: .5 }, '<')
        .from('[data-line]', { yPercent: 110, opacity: 0, duration: .9, stagger: .12 }, '-=.2')
        .to('.hero-sub', { opacity: 1, duration: .7 }, '-=.5')
        .to('.hero-actions', { opacity: 1, duration: .7 }, '-=.5')
        .to('.hero-stats', { opacity: 1, duration: .7 }, '-=.5');
    }

    var scatter = document.getElementById('heroScatter');
    if (scatter && !prefersReduced) {
      var scatterItems = scatter.querySelectorAll('.scatter-item');
      gsap.from(scatterItems, {
        opacity: 0,
        scale: .5,
        duration: .8,
        ease: 'back.out(1.7)',
        stagger: { each: .07, from: 'random' },
        delay: .3
      });
      scatterItems.forEach(function (item) {
        gsap.to(item, {
          y: gsap.utils.random(-16, 16),
          rotation: '+=' + gsap.utils.random(-6, 6),
          duration: gsap.utils.random(3.5, 6),
          repeat: -1,
          yoyo: true,
          ease: 'sine.inOut',
          delay: gsap.utils.random(0, 2)
        });
      });
    }
  }
})();
"""

def inline_scripts(html_out):
    html_out = html_out.replace("__GSAP_JS__", gsap_js, 1)
    html_out = html_out.replace("__SCROLLTRIGGER_JS__", scrolltrigger_js, 1)
    html_out = html_out.replace("__SCROLLTOPLUGIN_JS__", scrolltoplugin_js, 1)
    html_out = html_out.replace("__ANIMATION_JS__", animation_js, 1)
    return html_out

home_html = inline_scripts(home_html)
menu_html = inline_scripts(menu_html)

DIST_DIR.mkdir(parents=True, exist_ok=True)

for name, content in [("index.html", home_html), ("menu.html", menu_html)]:
    out_path = DIST_DIR / name
    out_path.write_text(content)
    print("wrote", len(content), "bytes to", out_path)

# GitHub Pages reads this file to know which custom domain to serve the
# site on and to provision the HTTPS certificate for. Sourced from
# build/CNAME rather than hardcoded here so the domain is easy to find
# and change in one place. Applies to the whole dist/ site, not per page.
cname_src = BUILD_DIR / "CNAME"
if cname_src.exists():
    (DIST_DIR / "CNAME").write_text(cname_src.read_text().strip())
