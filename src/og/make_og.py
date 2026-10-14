"""Draws the social share card (docs/assets/img/og-image.png).
Run from the repo root: python3 src/og/make_og.py docs/assets/fonts/plus-jakarta-sans-latin.woff2 docs/assets/img/og-image.png
Layout: the logo mark (docs/assets/img/mark.svg) on its rounded square, centered above the name, tagline, subtitle, and web address.
When the logo changes, update mark() to draw the new one."""
import json, os, sys, tempfile
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

FONT_WOFF2, OUT = sys.argv[1], sys.argv[2]
# Pillow cannot read WOFF2, so convert the site font to a temporary TTF.
TTF = os.path.join(tempfile.gettempdir(), "pjs.ttf")
f = TTFont(FONT_WOFF2); f.flavor = None; f.save(TTF)

def font(size, weight):
    ft = ImageFont.truetype(TTF, size)
    ft.set_variation_by_axes([weight])
    return ft

W, H, S = 1200, 630, 2          # draw at 2x, then downsample for smooth edges
NAVY, WHITE, TEAL = (15, 27, 45), (255, 255, 255), (25, 198, 180)
img = Image.new("RGB", (W * S, H * S), NAVY)
d = ImageDraw.Draw(img)

def text(xy, s, size, weight, fill, spacing=0):
    x, y = xy[0] * S, xy[1] * S
    ft = font(size * S, weight)
    if not spacing:
        d.text((x, y), s, font=ft, fill=fill); return
    for ch in s:
        d.text((x, y), ch, font=ft, fill=fill)
        x += ft.getlength(ch) + spacing * S

MUTED, SOFT = (138, 150, 168), (201, 210, 222)
LINE = (95, 108, 128)
def ctext(y, s, size, weight, fill):
    w = font(size, weight).getlength(s); text(((W - w) / 2, y), s, size, weight, fill)
def mark(cx0, cy0, k, square=False):
    pt = lambda x, y: ((cx0 + (x - 16) * k) * S, (cy0 + (y - 16) * k) * S)
    if square:
        d.rounded_rectangle((pt(0, 0)[0], pt(0, 0)[1], pt(32, 32)[0], pt(32, 32)[1]), radius=8 * k * S, fill=(31, 48, 73))
    d.line([pt(8, 22), pt(24, 10)], fill=LINE, width=round(2 * k * S))
    for x, y in ((8, 22), (24, 10)):
        X, Y = pt(x, y); e = k * S; d.ellipse((X - e, Y - e, X + e, Y + e), fill=LINE)
    for x, y, c in ((8, 22, (242, 107, 29)), (16, 16, (255, 194, 26)), (24, 10, (25, 198, 180))):
        X, Y = pt(x, y); r = 3.2 * k * S; d.ellipse((X - r, Y - r, X + r, Y + r), fill=c)
def tag(x, y, HS, center=False):
    f = font(HS, 800)
    if center:
        ctext(y, "Helping Your Data", HS, 800, WHITE)
        w = f.getlength("Take Flight") + f.getlength(".") - 6; x = (W - w) / 2
    else:
        text((x, y), "Helping Your Data", HS, 800, WHITE)
    text((x, y + HS * 1.18), "Take Flight", HS, 800, TEAL)
    text((x + f.getlength("Take Flight") - 6, y + HS * 1.18), ".", HS, 800, TEAL)
mark(W / 2, 112, 2.6, square=True)
ctext(176, "Lark Data Solutions", 48, 800, WHITE)
tag(0, 268, 60, center=True)
ctext(446, "Statistics, research design, and machine learning consulting.", 27, 500, SOFT)
ctext(530, "larkdatasolutions.com  ·  Milwaukee, Wisconsin", 21, 500, MUTED)

img.resize((W, H), Image.LANCZOS).save(OUT, optimize=True)
print("ok")
