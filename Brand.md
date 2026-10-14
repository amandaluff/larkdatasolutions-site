# Brand

## Name and tagline

- **Lark Data Solutions** (owned by Lark Services LLC; see `CLAUDE.md` for naming rules).
- Tagline: **"Helping Your Data Take Flight."** It plays on the Lark name and stays.

## Colors and type

Defined as tokens at the top of `docs/assets/css/style.css`.

| Token | Hex | Use |
|---|---|---|
| `--ink` | #0f1b2d | Text, dark backgrounds, buttons |
| `--teal` | #08776d | Links, labels, roles (darkened from #0a8c80 in Oct 2026 to pass WCAG AA contrast on the light gray sections) |
| `--teal-bright` | #19c6b4 | Accents, checkmarks, dots |
| `--orange` | #f26b1d | Accent dot |
| `--lime` | #a6d10c | Accent dot |
| `--gold` | #ffc21a | Accent dot (Products) |

The accent colors come from the dot graphic on the original site (`docs/assets/img/data-dots.webp`, used as the home page hero art).

Font: **Plus Jakarta Sans**, weights 400 to 800. Self-hosted as one variable file, Latin characters only: `docs/assets/fonts/plus-jakarta-sans-latin.woff2` (from Google Fonts, SIL Open Font License).

## Current logo (placeholder)

Three dots (orange, gold, teal) rising on a navy rounded square: `docs/assets/img/mark.svg`, `docs/favicon.svg`, `docs/favicon.ico`, `docs/apple-touch-icon.png`. The social share card is `docs/assets/img/og-image.png` (1200x630, navy, everything centered: the logo mark on its rounded square, "Lark Data Solutions," the tagline, "Statistics, research design, and machine learning consulting.", and the web address with Milwaukee. Chosen after rejecting versions with the dot plot and with a large mark on the right, which left awkward empty space). When the logo changes, redraw this card to match. Regenerate it with `src/og/make_og.py` (instructions at the top of that file). The header pairs the mark with the text "Lark / DATA SOLUTIONS". This stays until a new logo is chosen.

## New logo: what Amanda wants

- The idea behind the **original Google Sites logo** (an outlined bird in flight with a line chart in its body, plus speed lines and dots) is liked. It was too busy and hard to read at small sizes.
- **Subtle, not on the nose.** A literal bird next to or on a chart was rejected as too obvious.
- Must have a **version using the multicolored dots** (the palette above).
- Must read at favicon size (16 to 32 px).

## Concepts tried (October 2026)

Files are in `brand/concepts/` (open `index.html` for the last board, round 4). All were drawn by hand in SVG code. That is the limitation: hand-placed shapes did not produce convincing bird or wing forms.

1. **Round 1** (axis-and-ascent, feather bar chart, scatter-plot lark, single-stroke song line): rejected. The birds did not read as birds.
2. **Round 2** (solid lark with knocked-out chart, chart with lark taking off, outlined bird with chart): rejected as too on the nose.
3. **Round 3, subtler** (wing of dots, bird-shaped gap in a dot grid, rising flight path of dots, letter L of dots): **the wing of dots was liked best.**
4. **Round 4, wing variations** (feather layers, open wingtip, halftone crescent, wingbeat arcs): rejected. None looked like a wing.

## Next approach

- Start from a real wing silhouette (a leading edge that bends at the wrist and a scalloped trailing edge) and fill it with dots, instead of arranging dots and hoping a wing appears.
- Or explore with an image generator (Canva is connected), reference images Amanda likes, or a designer, then convert the chosen mark to clean SVG plus favicon sizes.
