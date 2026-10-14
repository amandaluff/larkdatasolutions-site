import json, sys, os, re

OUT = sys.argv[1]
SITE = "https://www.larkdatasolutions.com"
EMAIL = "contact@larkdatasolutions.com"
FORM = "https://formspree.io/f/mbgdzqze"
YEAR = "2026"

import hashlib
# Changes whenever style.css changes, so browsers fetch the new version after an update.
CSS_V = hashlib.md5(open(os.path.join(OUT, "assets", "css", "style.css"), "rb").read()).hexdigest()[:8]

NAV = [("/#top", "Home"), ("/#services", "Services"), ("/#partners", "Partners")]

ORG = {
    "@type": "ProfessionalService",
    "@id": SITE + "/#organization",
    "name": "Lark Data Solutions",
    "legalName": "Lark Services LLC",
    "url": SITE + "/",
    "email": EMAIL,
    "logo": SITE + "/apple-touch-icon.png",
    "image": SITE + "/assets/img/og-image.png",
    "description": "Statistics, research design, and machine learning consulting in Milwaukee, Wisconsin.",
    "address": {"@type": "PostalAddress", "addressLocality": "Milwaukee", "addressRegion": "WI", "addressCountry": "US"},
    "areaServed": "Worldwide",
    "knowsAbout": ["Statistical methods", "Research design", "Causal inference", "Program evaluation", "Real-world data",
                   "Clinical trials", "Research protocols", "Machine learning", "Deep learning",
                   "Speech recognition", "Predictive modeling"],
    "founder": [{"@id": SITE + "/#duncan-clark"}, {"@id": SITE + "/#amanda-luff"}],
}
PEOPLE = [
    {"@type": "Person", "@id": SITE + "/#duncan-clark", "name": "Duncan Clark", "honorificSuffix": "PhD",
     "jobTitle": "Partner, Applied Machine Learning & AI", "image": SITE + "/assets/img/duncan-clark.webp",
     "alumniOf": {"@type": "CollegeOrUniversity", "name": "The Ohio State University"}, "knowsAbout": ["Machine learning", "Speech recognition", "Algebraic topology"],
     "worksFor": {"@id": SITE + "/#organization"}},
    {"@type": "Person", "@id": SITE + "/#amanda-luff", "name": "Amanda Luff", "honorificSuffix": "PhD",
     "jobTitle": "Partner, Statistical Methods & Research Design", "image": SITE + "/assets/img/amanda-luff.webp",
     "alumniOf": {"@type": "CollegeOrUniversity", "name": "The Ohio State University"}, "knowsAbout": ["Statistical methods", "Research design", "Causal inference", "Epidemiology", "Clinical research"],
     "worksFor": {"@id": SITE + "/#organization"}},
]

LINES = [
    {"id": "statistics-research-design", "name": "Statistical Methods & Research Design", "color": "c-teal",
     "short": "Study design, causal inference, and analysis of real-world data.",
     "long": "We design studies and analyze data to answer specific questions, such as whether a program worked or which factors are associated with an outcome.",
     "items": ["Study Design & Analysis Plans", "Causal Inference & Program Evaluation", "Longitudinal & Real-World Data Analysis",
               "Advanced Statistical Methods", "Surveys & Data Collection", "Regulatory Compliance", "Research Reporting & Publication"],
     "extra": "",
     "lead": {"id": "amanda-luff", "name": "Amanda Luff, PhD, MPH", "title": "Partner, Statistical Methods &amp; Research Design",
              "bio": "Amanda is a quantitative researcher and data strategist with over a decade of experience analyzing real-world data. She excels at designing and leading complex research, transforming data into clear, evidence-based findings grounded in rigorous methodology and ethical practices."}},
    {"id": "machine-learning-ai", "name": "Applied Machine Learning & AI", "color": "c-orange",
     "short": "Predictive modeling, natural language processing, and speech recognition.",
     "long": "We build and train machine learning models on your data for prediction, classification, and language and speech tasks.",
     "items": ["Machine Learning & Deep Learning", "Predictive Modeling", "Natural Language Processing & Speech Recognition",
               "Model Fine-Tuning & Evaluation", "Training Data Development"],
     "extra": "",
     "lead": {"id": "duncan-clark", "name": "Duncan Clark, PhD", "title": "Partner, Applied Machine Learning &amp; AI",
              "bio": "Duncan is a data scientist and machine learning specialist with a background in advanced mathematics. He excels at developing custom machine learning models for prediction, classification, natural language processing, and speech recognition."}},
]


def amp(t):
    return t.replace("&", "&amp;")


MENU_ICON = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'


def check_meta(path, title, desc, robots):
    # Search results cut titles off after ~60 characters and descriptions after ~160.
    if robots.startswith("noindex"):
        return
    if len(title) > 60:
        print(f"WARNING {path}: title is {len(title)} characters (keep to 60 or fewer): {title}")
    if not 120 <= len(desc) <= 160:
        print(f"WARNING {path}: description is {len(desc)} characters (keep to 120-160): {desc}")


def page(path, title, desc, body, schema=None, robots="index, follow"):
    check_meta(path, title, desc, robots)
    url = SITE + path
    nav = "\n".join(
        f'        <a href="{h}"{" aria-current=\"page\"" if h == path else ""}>{n}</a>' for h, n in NAV)
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": "Lark Data Solutions",
         "publisher": {"@id": SITE + "/#organization"}},
        ORG] + (schema or [])}
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="{robots}">
  <link rel="canonical" href="{url}">
  <meta name="theme-color" content="#0f1b2d">

  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Lark Data Solutions">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE}/assets/img/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Lark Data Solutions: Helping Your Data Take Flight.">
  <meta property="og:locale" content="en_US">
  <meta name="twitter:card" content="summary_large_image">

  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">
  <link rel="stylesheet" href="/assets/css/style.css?v={CSS_V}">

  <script type="application/ld+json">
{json.dumps(graph, indent=2, ensure_ascii=False)}
  </script>
</head>
<body id="top">
  <a class="skip-link" href="#main">Skip to main content</a>

  <header class="site-header">
    <div class="container">
      <a class="brand" href="/" aria-label="Lark Data Solutions home">
        <img class="brand-mark" src="/assets/img/mark.svg" alt="Lark Data Solutions logo: three colored dots on a dark square" aria-hidden="true" width="30" height="30">
        <span>Lark<small>Data Solutions</small></span>
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{MENU_ICON}</button>
      <nav class="nav" id="site-nav" aria-label="Main">
{nav}
        <a class="btn" href="/#contact">Contact Us</a>
      </nav>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="container">
      <div>
        <p class="footer-head">Lark Data Solutions</p>
        <p>Statistics, research design, and machine learning consulting in Milwaukee, Wisconsin.</p>
      </div>
      <div>
        <p class="footer-head">Get in touch</p>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Milwaukee, Wisconsin</li>
        </ul>
      </div>
      <div class="footer-legal">
        <span>&copy; {YEAR} Lark Services LLC. All rights reserved.</span>
        <a href="/policies/">Terms, Privacy &amp; Disclaimers</a>
      </div>
    </div>
  </footer>

  <script>
    (function () {{
      var b = document.querySelector('.nav-toggle'), n = document.getElementById('site-nav');
      b.addEventListener('click', function () {{
        var open = n.classList.toggle('open');
        b.setAttribute('aria-expanded', open);
        b.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
      }});
      n.addEventListener('click', function (e) {{
        if (e.target.closest('a')) {{
          n.classList.remove('open');
          b.setAttribute('aria-expanded', false);
          b.setAttribute('aria-label', 'Open menu');
        }}
      }});
    }})();
  </script>
</body>
</html>
'''


def write(rel, html):
    # Root-relative links ("/about-us/") break when the site is served from a
    # subfolder (the github.io preview), so make them relative to this page.
    prefix = "../" * rel.count("/")
    html = re.sub(r'(href|src)="/(?!/)([^"]*)"',
                  lambda m: f'{m.group(1)}="{prefix + m.group(2) or "./"}"', html)
    # Bing flags images with missing or empty alt text, so every image needs one.
    # Decorative images get alt text plus aria-hidden="true" to keep screen readers quiet.
    for img in re.findall(r"<img\b[^>]*>", html):
        if not re.search(r'alt="[^"]+"', img):
            print(f"WARNING {rel}: image has no alt text: {img}")
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(html)


# ---------- Redirects for pages merged into the home page ----------
def redirect(rel, anchor):
    write(rel, f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Lark Data Solutions</title>
  <link rel="canonical" href="{SITE}/">
  <meta name="robots" content="noindex, follow">
  <meta http-equiv="refresh" content="0; url=../#{anchor}">
</head>
<body><p>This page has moved to <a href="/#{anchor}">the home page</a>.</p></body>
</html>
''')


redirect("our-services/index.html", "services")
redirect("about-us/index.html", "partners")
redirect("contact-us/index.html", "contact")

# ---------- Home (the whole site on one page) ----------
service_cards = "\n".join(f'''          <article class="line-card" id="{l['id']}" aria-labelledby="{l['id']}-h">
            <div class="dot {l['color']}" aria-hidden="true"></div>
            <h3 id="{l['id']}-h">{amp(l['name'])}</h3>
            <p>{l['long']}</p>
            <ul class="checklist">
{chr(10).join(f"              <li>{amp(t)}</li>" for t in l['items'])}
            </ul>
          </article>''' for l in LINES)

partner_cards = "\n".join(f'''          <article class="partner" id="{l['lead']['id']}">
            <img src="/assets/img/{l['lead']['id']}-320.webp" width="96" height="96" alt="Portrait of {l['lead']['name']}" loading="lazy">
            <h3>{l['lead']['name']}</h3>
            <p class="role">{l['lead']['title']}</p>
            <p>{l['lead']['bio']}</p>
          </article>''' for l in LINES)

products = '''        <article class="product-band" id="products" aria-labelledby="products-h">
          <div class="product-label">
            <div class="dot c-gold" aria-hidden="true"></div>
            <h3 id="products-h">Products</h3>
          </div>
          <div class="product-body">
            <h4>FSP Finder</h4>
            <p>A speech recognition tool radio stations use to make broadcast-ready edits of songs.</p>
          </div>
          <a class="btn btn-ghost" href="https://fspfinder.com" rel="noopener" target="_blank">Visit fspfinder.com</a>
        </article>'''

home_schema = PEOPLE + [{
    "@type": "Service", "name": l["name"], "description": l["long"], "serviceType": l["name"],
    "provider": {"@id": SITE + "/#organization"}, "areaServed": "Worldwide",
    "url": f"{SITE}/#{l['id']}",
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": l["name"], "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": t}} for t in l["items"]]},
} for l in LINES] + [{
    "@type": "SoftwareApplication", "name": "FSP Finder", "url": "https://fspfinder.com",
    "applicationCategory": "MultimediaApplication", "operatingSystem": "Web",
    "description": "A speech recognition tool radio stations use to make broadcast-ready edits of songs.",
    "publisher": {"@id": SITE + "/#organization"}}]

home = f'''    <section class="hero">
      <div class="container">
        <div>
          <h1 class="eyebrow">Data Science &amp; Research Consulting in Milwaukee</h1>
          <p class="tagline">Helping Your Data <span>Take Flight.</span></p>
          <p class="lead">Lark Data Solutions is a data science and research consulting firm in Milwaukee, Wisconsin. We help organizations design studies, analyze real-world data, and build machine learning models.</p>
          <div class="btn-row">
            <a class="btn" href="#contact">Contact Us</a>
            <a class="btn btn-ghost" href="#services">Our Services</a>
          </div>
        </div>
        <div class="hero-art">
          <img src="/assets/img/data-dots.webp" width="1000" height="501" alt="Decorative graphic of orange, yellow, green, teal, and gray dots arranged in rising columns, like a scatter plot" aria-hidden="true" fetchpriority="high">
        </div>
      </div>
    </section>

    <section class="section-soft anchor" id="services" aria-labelledby="services-heading">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Services</span>
          <h2 id="services-heading">What we do</h2>
          <p class="lead">Our work covers statistical methods and research design, and applied machine learning and AI. Projects often use both.</p>
        </div>
        <div class="line-grid">
{service_cards}
        </div>
{products}
      </div>
    </section>

    <section class="anchor" id="partners" aria-labelledby="partners-heading">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Partners</span>
          <h2 id="partners-heading">Who we are</h2>
        </div>
        <div class="grid grid-2">
{partner_cards}
        </div>
      </div>
    </section>

    <section class="section-soft anchor" id="contact" aria-labelledby="contact-heading">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">Contact</span>
          <h2 id="contact-heading">Get in touch</h2>
          <p class="lead">Tell us about your project and we'll reply to set up a free consultation. You can also email us directly.</p>
        </div>
        <div class="contact-grid">
        <div class="card">
          <h3>Send us a message</h3>
          <form class="contact-form" action="{FORM}" method="POST">
            <input type="hidden" name="_subject" value="New inquiry from larkdatasolutions.com">
            <div class="field-row">
              <label>Name <span class="req" aria-hidden="true">*</span>
                <input type="text" name="name" autocomplete="name" required>
              </label>
              <label>Email <span class="req" aria-hidden="true">*</span>
                <input type="email" name="email" autocomplete="email" required>
              </label>
            </div>
            <div class="field-row">
              <label>Organization
                <input type="text" name="organization" autocomplete="organization">
              </label>
              <label>Role or title
                <input type="text" name="role" autocomplete="organization-title">
              </label>
            </div>
            <div class="field-row">
              <label>Phone <span class="opt">(optional)</span>
                <input type="tel" name="phone" autocomplete="tel">
              </label>
              <label>Area of interest
                <select name="area">
                  <option value="">Select one</option>
                  <option>Statistical Methods &amp; Research Design</option>
                  <option>Applied Machine Learning &amp; AI</option>
                  <option>Both</option>
                  <option>Not sure yet</option>
                </select>
              </label>
            </div>
            <label>About your project <span class="req" aria-hidden="true">*</span>
              <textarea name="message" rows="6" required></textarea>
            </label>
            <input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
            <button class="btn" type="submit">Send message</button>
            <p class="form-status" role="status" aria-live="polite"></p>
          </form>
        </div>
        <div class="card">
          <h3>Email</h3>
          <p>Write to us directly.</p>
          <a class="btn btn-ghost" href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
        </div>
      </div>
    </section>

    <script>
      (function () {{
        var f = document.querySelector('.contact-form'), s = f.querySelector('.form-status'), b = f.querySelector('button');
        f.addEventListener('submit', function (e) {{
          e.preventDefault();
          b.disabled = true; s.className = 'form-status'; s.textContent = 'Sending...';
          fetch(f.action, {{ method: 'POST', body: new FormData(f), headers: {{ 'Accept': 'application/json' }} }})
            .then(function (r) {{
              if (!r.ok) throw new Error();
              f.reset(); s.className = 'form-status ok';
              s.textContent = 'Thanks. We received your message and will reply by email.';
            }})
            .catch(function () {{
              s.className = 'form-status err';
              s.textContent = 'Your message could not be sent. Please email us at {EMAIL}.';
            }})
            .finally(function () {{ b.disabled = false; }});
        }});
      }})();
    </script>'''

write("index.html", page("/",
    "Lark Data Solutions | Data Science Consulting, Milwaukee",
    "Data science and research consulting firm in Milwaukee, WI. We design studies, analyze real-world data, and build machine learning models.",
    home, home_schema))

# ---------- Policies ----------
legal = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "policies_body.html"), encoding="utf-8").read()
write("policies/index.html", page("/policies/",
    "Terms, Privacy & Disclaimers | Lark Data Solutions",
    "Terms of service, privacy policy, and disclaimers for larkdatasolutions.com, the website of Lark Data Solutions, operated by Lark Services LLC.",
    legal))

# ---------- /home (old Google Sites URL) -> / ----------
write("home/index.html", f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Lark Data Solutions</title>
  <link rel="canonical" href="{SITE}/">
  <meta name="robots" content="noindex, follow">
  <meta http-equiv="refresh" content="0; url=../">
</head>
<body><p>This page has moved to <a href="/">the home page</a>.</p></body>
</html>
''')

# ---------- 404 ----------
write("404.html", page("/404.html", "Page Not Found | Lark Data Solutions",
    "The page you were looking for could not be found.",
    '''    <section class="page-hero" style="padding-bottom:88px">
      <div class="container">
        <span class="eyebrow">404</span>
        <h1>We couldn't find that page.</h1>
        <p class="lead">It may have moved when we updated our site. Try one of these instead:</p>
        <div class="btn-row">
          <a class="btn" href="/">Home</a>
          <a class="btn btn-ghost" href="/#services">Services</a>
          <a class="btn btn-ghost" href="/#contact">Contact Us</a>
        </div>
      </div>
    </section>''', robots="noindex"))

# ---------- robots + sitemap ----------
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
urls = [("/", "1.0"), ("/policies/", "0.3")]
open(os.path.join(OUT, "sitemap.xml"), "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url>\n    <loc>{SITE}{u}</loc>\n    <lastmod>2026-10-13</lastmod>\n    <priority>{p}</priority>\n  </url>\n" for u, p in urls) +
    "</urlset>\n")
open(os.path.join(OUT, ".nojekyll"), "w").write("")
print("built")
