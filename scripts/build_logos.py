"""Generate every Paruto logo, icon and social image from one source of truth.

The P/D symbol is drawn as geometry (traced from the Paruto Media master
artwork) and all lettering is converted to outlines from Montserrat, so the
output SVGs render identically everywhere and need no installed fonts.

    python3 -m venv .venv && .venv/bin/pip install fonttools resvg-py
    .venv/bin/python scripts/build_logos.py
"""

import zipfile
from pathlib import Path

import resvg_py
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "logos"
ICONS = ROOT / "assets" / "icons"
FONT = ROOT / "scripts" / "fonts" / "Montserrat-VF.ttf"

# Symbol geometry: 365 x 347 units. One continuous band that runs from the
# P's stem, round the bowl, down the diagonal, and round the outer D.
SYMBOL_W, SYMBOL_H = 365, 347
SYMBOL = (
    "M75 259V77.5H190.5A96 96 0 0 1 190.5 269.5H168.5L91 347H0V0H190.5"
    "A173.5 173.5 0 0 1 190.5 347H147L184 310H190.5A136.5 136.5 0 0 0 190.5 37"
    "H37V310H79L153.5 235.5H190.5A62 62 0 0 0 190.5 111.5H111V223Z"
)

GOLD_STOPS = [(0, "#B8841E"), (0.42, "#F5D68A"), (0.7, "#D9A847"), (1, "#C9952A")]
COLOURS = {"gold": None, "black": "#0A0A0A", "white": "#FFFFFF"}
INK = "#0A0A0A"

SUBSIDIARIES = {
    "media": ("MEDIA", "WE AMPLIFY IMPACT"),
    "music": ("MUSIC", None),
    "capital": ("CAPITAL", None),
}
MASTER_TAGLINE = "THINK POSSIBILITIES"

_font = instancer.instantiateVariableFont(TTFont(FONT), {"wght": 500})
_glyphs = _font.getGlyphSet()
_cmap = _font.getBestCmap()
CAP = 700  # Montserrat cap height in font units


def text_path(text, cap, x, baseline, tracking=0.0, width=None, align="left"):
    """Outline `text` with caps `cap` units tall. Returns (path d, ink width).

    Pass `width` to solve the tracking so the ink spans exactly that width.
    `x` is the left ink edge (align="left") or the centre (align="center").
    """
    s = cap / CAP
    names = [_cmap[ord(c)] for c in text]

    def layout(track):
        pen_x, placed = 0.0, []
        for n in names:
            placed.append((n, pen_x))
            pen_x += _glyphs[n].width * s + track
        bp = BoundsPen(_glyphs)
        for n, gx in placed:
            _glyphs[n].draw(TransformPen(bp, (s, 0, 0, -s, gx, 0)))
        x0, _, x1, _ = bp.bounds
        return placed, x0, x1 - x0

    placed, x0, ink = layout(tracking)
    if width is not None and len(names) > 1:
        tracking += (width - ink) / (len(names) - 1)
        placed, x0, ink = layout(tracking)
    left = x - ink / 2 if align == "center" else x
    pen = SVGPathPen(_glyphs, ntos=lambda v: f"{v:.2f}".rstrip("0").rstrip("."))
    for n, gx in placed:
        _glyphs[n].draw(TransformPen(pen, (s, 0, 0, -s, left - x0 + gx, baseline)))
    return pen.getCommands(), ink, tracking


def ruled(text, cap, cy, x0, x1, tracking=None, width=None, gap=40, rule=3):
    """Centred text between two hairline rules spanning x0..x1."""
    mid = (x0 + x1) / 2
    d, ink, _ = text_path(text, cap, mid, cy + cap / 2, tracking or 0, width, "center")
    a, b = mid - ink / 2 - gap, mid + ink / 2 + gap
    return [d, f"M{x0} {cy - rule / 2}H{a}v{rule}H{x0}Z", f"M{b} {cy - rule / 2}H{x1}v{rule}H{b}Z"]


def symbol_at(x, y, scale=1.0):
    return f'<path transform="translate({x:g} {y:g}) scale({scale:g})" d="{SYMBOL}"/>'


def svg(w, h, body, colour, pad=0, bg=None, title="Paruto"):
    vb = f"{-pad:g} {-pad:g} {w + 2 * pad:g} {h + 2 * pad:g}"
    if colour == "gold":
        stops = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in GOLD_STOPS)
        defs = (f'<defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="0" '
                f'x2="{w:g}" y2="{h:g}">{stops}</linearGradient></defs>')
        fill = "url(#g)"
    else:
        defs, fill = "", COLOURS[colour]
    back = f'<rect x="{-pad:g}" y="{-pad:g}" width="{w + 2 * pad:g}" height="{h + 2 * pad:g}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{title}">'
            f"<title>{title}</title>{defs}{back}<g fill=\"{fill}\">{body}</g></svg>\n")


# --- Lockups -------------------------------------------------------------
TEXT_X0, TEXT_X1 = 586, 1635          # wordmark column, matched to the Media artwork
DIVIDER = '<rect x="444" y="0" width="3" height="347"/>'
PARUTO_CAP = 127
LOCKUP_W, LOCKUP_H = TEXT_X1, SYMBOL_H


def wordmark(top):
    d, _, _ = text_path("PARUTO", PARUTO_CAP, TEXT_X0, top + PARUTO_CAP, width=TEXT_X1 - TEXT_X0)
    return f'<path d="{d}"/>'


def master_lockup():
    rows = ruled(MASTER_TAGLINE, 34, 269, TEXT_X0, TEXT_X1, width=760)
    return symbol_at(0, 0) + DIVIDER + wordmark(60) + "".join(f'<path d="{d}"/>' for d in rows)


# Descriptor tracking is fixed by MEDIA's width in the original artwork so
# every subsidiary name is set identically.
_, _, DESCRIPTOR_TRACK = text_path("MEDIA", 52, 0, 0, width=526)


def subsidiary_lockup(name, tagline):
    dy = 0 if tagline else 6
    rows = ruled(name, 52, 254 + dy, TEXT_X0, TEXT_X1, tracking=DESCRIPTOR_TRACK)
    body = symbol_at(0, 0) + DIVIDER + wordmark(55 + dy) + "".join(f'<path d="{d}"/>' for d in rows)
    if tagline:
        d, _, _ = text_path(tagline, 33, (TEXT_X0 + TEXT_X1) / 2, 353, width=750, align="center")
        body += f'<path d="{d}"/>'
    return body


STACK_W = TEXT_X1 - TEXT_X0
STACK_H = 680


def stacked_lockup():
    sx = (STACK_W - SYMBOL_W) / 2
    d, _, _ = text_path("PARUTO", PARUTO_CAP, 0, 347 + 110 + PARUTO_CAP, width=STACK_W)
    rows = ruled(MASTER_TAGLINE, 34, 663, 0, STACK_W, width=760)
    return symbol_at(sx, 0) + f'<path d="{d}"/>' + "".join(f'<path d="{d}"/>' for d in rows)


def write(path, content, png_width=None):
    path.write_text(content)
    if png_width:
        png = resvg_py.svg_to_bytes(svg_string=content, width=png_width)
        path.with_suffix(".png").write_bytes(bytes(png))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    ICONS.mkdir(parents=True, exist_ok=True)
    pad_l, pad_s = 40, 24
    for colour in COLOURS:
        write(OUT / f"paruto-symbol-{colour}.svg",
              svg(SYMBOL_W, SYMBOL_H, symbol_at(0, 0), colour, pad_s, title="Paruto symbol"), 1024)
        write(OUT / f"paruto-logo-{colour}.svg",
              svg(LOCKUP_W, LOCKUP_H, master_lockup(), colour, pad_l, title="Paruto — Think Possibilities"), 2400)
        write(OUT / f"paruto-logo-stacked-{colour}.svg",
              svg(STACK_W, STACK_H, stacked_lockup(), colour, pad_l, title="Paruto — Think Possibilities"), 1600)
        for key, (name, tagline) in SUBSIDIARIES.items():
            h = 353 + 4 if tagline else LOCKUP_H
            write(OUT / f"paruto-{key}-logo-{colour}.svg",
                  svg(LOCKUP_W, h, subsidiary_lockup(name, tagline), colour, pad_l,
                      title=f"Paruto {name.title()}"), 2400)

    # Icons: gold symbol on brand black. The browser favicon keeps a rounded
    # tile; app icons are full-bleed squares (the OS applies its own mask).
    def tile(size, inset, radius=0):
        scale = size * (1 - 2 * inset) / SYMBOL_W
        x = (size - SYMBOL_W * scale) / 2
        y = (size - SYMBOL_H * scale) / 2
        body = symbol_at(x, y, scale)
        doc = svg(size, size, body, "gold", 0, INK, "Paruto")
        if radius:
            doc = doc.replace(f'fill="{INK}"/>', f'fill="{INK}" rx="{radius}"/>', 1)
        return doc

    write(ICONS / "favicon.svg", tile(64, 0.14, 12))
    for size, name in [(32, "favicon-32"), (180, "apple-touch-icon"), (192, "icon-192"), (512, "icon-512")]:
        doc = tile(512, 0.14 if size <= 32 else 0.2, 96 if size <= 32 else 0)
        (ICONS / f"{name}.png").write_bytes(bytes(resvg_py.svg_to_bytes(svg_string=doc, width=size)))

    # Open Graph card, 1200 x 630.
    s = 0.62
    w, h = LOCKUP_W * s, LOCKUP_H * s
    og_body = f'<g transform="translate({(1200 - w) / 2:g} {(630 - h) / 2:g}) scale({s})">{master_lockup()}</g>'
    stops = "".join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in GOLD_STOPS)
    og = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630">'
        f'<defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="{LOCKUP_W}" y2="{LOCKUP_H}">{stops}</linearGradient>'
        '<radialGradient id="glow" cx="50%" cy="115%" r="75%"><stop offset="0" stop-color="#C9952A" stop-opacity=".28"/>'
        '<stop offset="1" stop-color="#C9952A" stop-opacity="0"/></radialGradient></defs>'
        f'<rect width="1200" height="630" fill="{INK}"/><rect width="1200" height="630" fill="url(#glow)"/>'
        '<rect x="40" y="40" width="1120" height="550" fill="none" stroke="#C9952A" stroke-opacity=".35"/>'
        f'<g fill="url(#g)">{og_body}</g></svg>'
    )
    (ICONS / "og-image.png").write_bytes(bytes(resvg_py.svg_to_bytes(svg_string=og, width=1200)))

    # The downloadable asset pack linked from the Downloads section.
    with zipfile.ZipFile(ROOT / "paruto-brand-assets.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted([*OUT.iterdir(), *ICONS.iterdir()]):
            z.write(f, f"paruto-brand-assets/{f.parent.name}/{f.name}")
    print("Wrote", len(list(OUT.iterdir())), "logo files,", len(list(ICONS.iterdir())), "icons and the asset zip")


if __name__ == "__main__":
    main()
