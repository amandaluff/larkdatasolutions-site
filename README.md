# larkdatasolutions.com

Website for Lark Data Solutions, live at https://www.larkdatasolutions.com.

- `docs/` is the published site (GitHub Pages serves this folder). The HTML pages are generated; edit the stylesheet (`docs/assets/css/style.css`) and images in `docs/assets/` directly.
- `src/build.py` generates the pages in `docs/`, and `src/policies_body.html` holds the Terms, Privacy and Disclaimers text. Run `python3 src/build.py docs` after editing either.
- Preview: `python3 -m http.server 8420 --directory docs`, then open http://localhost:8420
- `CLAUDE.md`: rules for copy and editing. `Setup.md`: hosting, DNS, email, form, analytics, and open tasks. `Brand.md`: colors, type, and logo history.
- `brand/`: logo concept files (not published).
