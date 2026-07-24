# -*- coding: utf-8 -*-
import html
from pathlib import Path

# All paths are relative to this script's own location, not the current
# working directory, so `python3 build/generate.py` works the same whether
# it's run from the repo root (CI) or from inside build/ (local dev).
BUILD_DIR = Path(__file__).resolve().parent
REPO_ROOT = BUILD_DIR.parent
FONTS_DIR = BUILD_DIR / "assets" / "fonts"
VENDOR_DIR = BUILD_DIR / "vendor"
DIST_DIR = REPO_ROOT / "dist"

def load(key):
    return (FONTS_DIR / f"{key}.b64").read_text().strip()

FONTS = {k: load(k) for k in ["fraunces", "inter400", "inter600", "dmmono400", "dmmono500", "caveat", "dmseriftext"]}

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
<title>The Golden Whisk — Cake Board</title>
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
  font-family: 'GW Mono';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(data:font/woff2;base64,{dmmono400}) format('woff2');
}}
@font-face {{
  /* DM Mono tops out at 500 (Medium) — there is no 700/bold cut, so this
     stands in for "bold" mono text rather than triggering the browser's
     synthetic/faux bold on a face that was never drawn that way. */
  font-family: 'GW Mono';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(data:font/woff2;base64,{dmmono500}) format('woff2');
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
  --paper:        #FBF3E7;
  --paper-alt:    #F4E3BE;
  --ink:          #2B1B14;
  --ink-70:       rgba(43,27,20,.72);
  --ink-45:       rgba(43,27,20,.45);
  --cream:        #FBF3E7;
  --cream-60:     rgba(251,243,231,.6);
  --cream-40:     rgba(251,243,231,.4);
  --gold:         #C89B3C;
  --gold-soft:    rgba(200,155,60,.4);
  --jam:          #B23A48;
  --jam-deep:     #8E2A36;
  --line:         rgba(43,27,20,.14);

  --font-display: 'GW Fraunces', Georgia, serif;
  --font-body:    'GW Inter', -apple-system, sans-serif;
  --font-mono:    'GW Mono', 'Courier New', monospace;
  --font-script:  'GW Caveat', cursive;

  --content-w: 720px;
  color-scheme: dark;
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
}}

body {{
  margin: 0;
  background:
    radial-gradient(ellipse 90% 60% at 50% -10%, rgba(200,155,60,.10), transparent 60%),
    var(--board);
  color: var(--cream);
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
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

/* ============ masthead ============ */
.masthead {{
  text-align: center;
  padding: 72px 0 34px;
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
  transform: rotate(-1.4deg);
  margin: 0 0 26px;
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
  top: 0;
  z-index: 40;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px;
  margin: 0 calc(50% - 50vw) 30px;
  padding: 14px 22px;
  background: rgba(24,15,10,.78);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(251,243,231,.08);
}}
.jump a {{
  font-family: var(--font-body);
  font-weight: 600;
  font-size: .68rem;
  letter-spacing: .08em;
  text-transform: uppercase;
  text-decoration: none;
  color: var(--cream-60);
  border: 1px solid rgba(251,243,231,.22);
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
  font-family: var(--font-body);
  font-weight: 600;
  color: var(--ink);
  padding-left: 0;
  white-space: normal;
}}
td.price {{
  font-family: var(--font-mono);
  font-weight: 500;
  color: var(--jam-deep);
  text-align: right;
  font-variant-numeric: tabular-nums;
}}
.table-2col td.price {{ color: var(--jam-deep); }}
.unit {{
  font-family: var(--font-mono);
  font-weight: 400;
  font-size: .72rem;
  color: var(--ink-45);
}}
.dash {{ color: var(--ink-45); }}

/* ============ footer ============ */
.board-footer {{
  text-align: center;
  padding-top: 36px;
  border-top: 1px solid rgba(251,243,231,.14);
}}
.board-footer p {{
  font-size: .82rem;
  color: var(--cream-40);
  max-width: 48ch;
  margin: 0 auto .9em;
}}
.signoff {{
  font-family: var(--font-script);
  font-size: 1.4rem;
  color: var(--gold);
  transform: rotate(-1deg);
}}
.contact {{
  font-family: var(--font-body);
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

<div class="board">

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
    <p class="intro">Every cake below is mixed and iced only after you order it — nothing sits ready on a shelf. Two sizes on most flavours: a 1&nbsp;kg cake serves about 12–15, a 650&nbsp;g serves about 8–10. Message us with your flavour, size, and the date you need it.</p>
  </header>

  <nav class="jump" aria-label="Jump to a category">
    <a href="#fruit">Fruit</a>
    <a href="#chocolate">Chocolate</a>
    <a href="#signature">Signature</a>
    <a href="#wholesome">Wholesome</a>
    <a href="#piece">By the Piece</a>
  </nav>

{categories}

  <footer class="board-footer">
    <p>Prices in ₹. A 1&nbsp;kg cake serves about 12–15 guests, a 650&nbsp;g serves about 8–10 — sizes are approximate cake weight, not a guaranteed ingredient count.</p>
    <p class="signoff">made with love in a home kitchen</p>
    <p class="contact">To order: WhatsApp <a href="https://wa.me/919872347816">98723 47816</a></p>
    <a class="top-link" href="#top">Back to top</a>
  </footer>

</div>

<button class="back-to-top" id="backToTop" type="button" aria-label="Back to top">
  <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
    <path d="M12 19V6M12 6L6 12M12 6L18 12" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</button>

<script>__GSAP_JS__</script>
<script>__SCROLLTRIGGER_JS__</script>
<script>__SCROLLTOPLUGIN_JS__</script>
<script>__ANIMATION_JS__</script>
"""

html_out = TEMPLATE.format(categories=CATEGORIES_HTML, **FONTS)

# Inlined verbatim (not through .format()) so the thousands of literal { }
# in the minified library source never collide with str.format() syntax.
gsap_js = (VENDOR_DIR / "gsap.min.js").read_text()
scrolltrigger_js = (VENDOR_DIR / "ScrollTrigger.min.js").read_text()
scrolltoplugin_js = (VENDOR_DIR / "ScrollToPlugin.min.js").read_text()

animation_js = r"""
(function(){
  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);

  var mastheadEls = {
    mark: document.querySelector('.mark'),
    eyebrow: document.querySelector('.eyebrow'),
    wordmark: document.querySelector('.wordmark'),
    note: document.querySelector('.note'),
    intro: document.querySelector('.intro')
  };
  var cards = gsap.utils.toArray('.category');

  if (prefersReduced) {
    gsap.set([mastheadEls.mark, mastheadEls.eyebrow, mastheadEls.wordmark, mastheadEls.intro], { opacity: 1, y: 0 });
    gsap.set(mastheadEls.note, { opacity: 1, y: 0, rotate: -1.4 });
    gsap.set(cards, { opacity: 1, y: 0 });
  } else {
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
})();
"""

html_out = html_out.replace("__GSAP_JS__", gsap_js, 1)
html_out = html_out.replace("__SCROLLTRIGGER_JS__", scrolltrigger_js, 1)
html_out = html_out.replace("__SCROLLTOPLUGIN_JS__", scrolltoplugin_js, 1)
html_out = html_out.replace("__ANIMATION_JS__", animation_js, 1)

DIST_DIR.mkdir(parents=True, exist_ok=True)
out_path = DIST_DIR / "index.html"
out_path.write_text(html_out)

print("wrote", len(html_out), "bytes to", out_path)
