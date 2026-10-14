# Setup

How larkdatasolutions.com is hosted and connected, as of October 13, 2026.

## Hosting

- **Repo:** [amandaluff/larkdatasolutions-site](https://github.com/amandaluff/larkdatasolutions-site) (public, so GitHub Pages works on the free plan).
- **GitHub Pages:** serves the `docs/` folder from the `main` branch. The custom domain is set in `docs/CNAME` (`www.larkdatasolutions.com`). HTTPS is enforced. The certificate covers `larkdatasolutions.com` and `www.larkdatasolutions.com` and renews automatically.
- **Redirects:** `larkdatasolutions.com`, `http://` addresses, and `amandaluff.github.io/larkdatasolutions-site` all redirect to `https://www.larkdatasolutions.com/`. Old page addresses (`/home/`, `/our-services/`, `/about-us/`, `/contact-us/`) are small pages that redirect to the matching section of the home page.
- **Links are relative** (the build rewrites `/path` to `path` or `../path`), so the site also works when served from a subfolder.

## DNS (Dynadot, using Dynadot DNS)

| Type | Host | Value | Purpose |
|---|---|---|---|
| A | @ | 185.199.108.153 | GitHub Pages |
| A | @ | 185.199.109.153 | GitHub Pages |
| A | @ | 185.199.110.153 | GitHub Pages |
| A | @ | 185.199.111.153 | GitHub Pages |
| CNAME | www | amandaluff.github.io | GitHub Pages |
| MX | @ | 1 smtp.google.com | **Email. Do not delete.** |
| TXT | @ | google-site-verification=KsHk55… | Google domain verification |
| TXT | @ | google-site-verification=_yQre8… | Google domain verification |
| CNAME | 6murwocd… | gv-rm4zl2kaqy53bi.dv.googlehosted.com | Google verification |

- TTL is 5 minutes. Never use Dynadot's "Clear Settings" button.
- There is no SPF record. Optional: add TXT `v=spf1 include:_spf.google.com ~all` if anyone sends mail as contact@larkdatasolutions.com, to keep it out of spam.

## Email

- `contact@larkdatasolutions.com` is an alias in the **Lark Services Google Workspace**, so it lands in that inbox. Delivery depends on the MX record above.
- Delivery can lag several minutes. A delayed test is not a failure.

## Contact form (Formspree)

- Endpoint: `https://formspree.io/f/mbgdzqze` (`FORM` in `src/build.py`).
- The recipient (contact@larkdatasolutions.com) is set in the Formspree dashboard, not in the site code.
- Fields: name, email (both required), organization, role, phone, area of interest, project details (required). Email subject: "New inquiry from larkdatasolutions.com". The hidden `_gotcha` field is a spam trap.
- Submits in the page with `fetch`. Shows a thank-you message on success, or asks the visitor to email directly on failure.
- The privacy policy (section 3.1) names Formspree as the processor.

## Analytics (Google Analytics 4)

- Measurement ID `G-YW9BVNQKPN` (`GA_ID` in `src/build.py`), on every page.
- A `generate_lead` event fires only after Formspree confirms a submission. Clicks on "Contact Us" are not counted.
- The privacy policy (sections 3.1 and 3.5) describes Google Analytics and its cookies, with opt-out links.

## Search

- Sitemap: `https://www.larkdatasolutions.com/sitemap.xml` (home page and Terms page). `robots.txt` allows everything and points to the sitemap.
- The domain is already verified for Google through the TXT records above.

## Open items

- [ ] Formspree: confirm form `mbgdzqze` delivers to contact@larkdatasolutions.com, and if allowed domains are restricted, add `www.larkdatasolutions.com`. Send a test from the live page.
- [ ] Google Analytics: mark `generate_lead` as a key event (after the first real submission appears), and define internal traffic to exclude the partners' own visits.
- [ ] Google Search Console: submit `sitemap.xml`.
- [ ] Bing Webmaster Tools: import the site from Search Console and submit the sitemap.
- [ ] Unpublish the old Google Sites page (`sites.google.com/view/larkdatasolutions`). It still shows the old copy and "Lark Data Solutions LLC".
- [ ] Set up a Google Business Profile for local search.
- [ ] fspfinder.com footer still says "a service of Lark Data Solutions LLC" (Duncan's site, separate repo).
- [ ] Optional: make sitemap `lastmod` dates update automatically (currently fixed at 2026-10-13).
- [ ] Optional: host the Plus Jakarta Sans font locally instead of loading it from Google Fonts (faster first load).
- [ ] New logo (see `Brand.md`). When it changes, update the logo alt text in `src/build.py` and the `logo` in the structured data.
