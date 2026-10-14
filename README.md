# larkdatasolutions.com

Website for Lark Data Solutions, a DBA of Lark Services LLC.

- `docs/` is the published site (GitHub Pages serves this folder).
- `src/build.py` generates the HTML pages in `docs/`. Run `python3 src/build.py docs` after editing it.
- Preview: `python3 -m http.server 8420 --directory docs`, then open http://localhost:8420
