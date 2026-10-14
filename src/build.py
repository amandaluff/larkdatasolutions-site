import json, sys, os

OUT = sys.argv[1]
SITE = "https://www.larkdatasolutions.com"
EMAIL = "contact@larkdatasolutions.com"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLScG4-OfHltn9WoBjefh_RZRsHVTqhr_40jwCqcX0C2IqBriFQ/viewform"
YEAR = "2026"

NAV = [("/", "Home"), ("/our-services/", "Services"), ("/about-us/", "About")]

ORG = {
    "@type": "ProfessionalService",
    "@id": SITE + "/#organization",
    "name": "Lark Data Solutions",
    "legalName": "Lark Services LLC",
    "url": SITE + "/",
    "email": EMAIL,
    "logo": SITE + "/apple-touch-icon.png",
    "image": SITE + "/assets/img/og-image.png",
    "description": "Data strategy, machine learning and AI, statistical analysis, and research protocol consulting based in Milwaukee, Wisconsin.",
    "address": {"@type": "PostalAddress", "addressLocality": "Milwaukee", "addressRegion": "WI", "addressCountry": "US"},
    "areaServed": "Worldwide",
    "knowsAbout": ["Data strategy", "Analytics consulting", "Machine learning", "Artificial intelligence",
                   "Predictive modeling", "Natural language processing", "Statistical analysis",
                   "Real-world data analysis", "Evidence generation", "Research study design",
                   "Research protocol development", "Research compliance"],
    "founder": [{"@id": SITE + "/about-us/#duncan-clark"}, {"@id": SITE + "/about-us/#amanda-luff"}],
}
PEOPLE = [
    {"@type": "Person", "@id": SITE + "/about-us/#duncan-clark", "name": "Duncan Clark", "honorificSuffix": "PhD",
     "jobTitle": "Partner, Machine Learning & Intelligent Systems", "image": SITE + "/assets/img/duncan-clark.webp",
     "worksFor": {"@id": SITE + "/#organization"}, "sameAs": ["https://www.linkedin.com/in/duncan-clark-1b3548288/"]},
    {"@type": "Person", "@id": SITE + "/about-us/#amanda-luff", "name": "Amanda Luff", "honorificSuffix": "PhD",
     "jobTitle": "Partner, Research Methodology & Analytic Strategy", "image": SITE + "/assets/img/amanda-luff.webp",
     "worksFor": {"@id": SITE + "/#organization"}, "sameAs": ["https://www.linkedin.com/in/amanda-luff/"]},
]

SERVICES = [
    ("data-strategy", "Data Strategy & Analytics Consulting", "c-teal",
     "We help you chart a clear course to use your data for sustained impact.",
     "We help you understand your data's full potential and create a clear plan to achieve your goals. Whether you're just starting your data journey or looking to get more from your existing information, we guide you.",
     [("Data Roadmaps", "Mapping out how to use your data effectively to reach your business or organizational objectives."),
      ("Analytics Capability Assessment", "Evaluating your current data capabilities and identifying opportunities for improvement."),
      ("Data-Driven Decision Frameworks", "Designing clear ways to use data to make better, faster decisions."),
      ("AI & Technology Feasibility", "Exploring if and how advanced technologies like AI can solve your specific challenges.")]),
    ("machine-learning-ai", "Machine Learning & AI Solutions", "c-orange",
     "We build intelligent systems that predict, automate, and drive innovation.",
     "We build smart, custom systems that learn from your data to predict outcomes, automate tasks, and solve complex problems, giving you a competitive edge.",
     [("Custom AI & ML Model Development", "Designing and building specialized machine learning and artificial intelligence models for your unique needs."),
      ("Predictive Analytics", "Creating models that forecast future trends, behaviors, or risks."),
      ("Intelligent Automation", "Developing algorithms that streamline processes and enhance decision-making."),
      ("Model Deployment & Integration", "Ensuring your AI solutions are seamlessly implemented and work effectively within your existing systems.")]),
    ("analytics-evidence", "Advanced Analytics & Evidence Generation", "c-lime",
     "We uncover insights from your data to inform key decisions.",
     "We transform your raw data into clear, evidence-based findings using sophisticated statistical techniques. We help you uncover the true story within your data, understand what's working, and communicate those insights effectively.",
     [("Real-World Data Analysis", "Extracting deep insights from existing, complex datasets (like health records or administrative data) to inform decisions."),
      ("Advanced Statistical Modeling", "Applying rigorous statistical methods to explore relationships, evaluate interventions, and derive robust conclusions."),
      ("Data Preparation for Research", "Meticulously cleaning, organizing, and preparing your data specifically for accurate and reliable analytical outcomes."),
      ("Scientific Reporting & Dissemination", "Clearly translating complex findings into accessible reports, publications, and presentations for diverse audiences.")]),
    ("protocol-compliance", "Protocol Design & Compliance", "c-gold",
     "We ensure your data initiatives are robust, ethically sound, and fully compliant.",
     "We help you build the foundational strategy for sound research, ensuring your studies are well-planned, designed to yield reliable results, and fully compliant with ethical guidelines and regulations.",
     [("Project & Protocol Development", "Crafting comprehensive plans for projects, from initial concept to detailed data collection blueprints."),
      ("Regulatory and Compliance Consultation", "Guiding you through the ethical considerations and regulatory requirements for your projects and data initiatives, including preparing for external reviews."),
      ("Survey & Data Collection Tool Design", "Developing effective surveys, forms, and workflows to capture high-quality, relevant data efficiently."),
      ("Workflow Optimization", "Streamlining your processes and documentation for maximum efficiency and integrity.")]),
]

MENU_ICON = '<svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>'


def page(path, title, desc, body, schema=None, robots="index, follow"):
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
  <link rel="stylesheet" href="/assets/css/style.css">

  <script type="application/ld+json">
{json.dumps(graph, indent=2, ensure_ascii=False)}
  </script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>

  <header class="site-header">
    <div class="container">
      <a class="brand" href="/" aria-label="Lark Data Solutions home">
        <img class="brand-mark" src="/assets/img/mark.svg" alt="" width="30" height="30">
        <span>Lark<small>Data Solutions</small></span>
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">{MENU_ICON}</button>
      <nav class="nav" id="site-nav" aria-label="Main">
{nav}
        <a class="btn" href="/contact-us/"{" aria-current=\"page\"" if path == "/contact-us/" else ""}>Contact Us</a>
      </nav>
    </div>
  </header>

  <main id="main">
{body}
  </main>

  <footer class="site-footer">
    <div class="container">
      <div>
        <h2>Lark Data Solutions</h2>
        <p>Data strategy, machine learning, and research methodology consulting. Based in Milwaukee, Wisconsin, working with organizations everywhere.</p>
      </div>
      <div>
        <h2>Explore</h2>
        <ul>
          <li><a href="/our-services/">Our Services</a></li>
          <li><a href="/about-us/">About Us</a></li>
          <li><a href="/contact-us/">Contact Us</a></li>
        </ul>
      </div>
      <div>
        <h2>Get in touch</h2>
        <ul>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>Milwaukee, Wisconsin</li>
        </ul>
      </div>
      <div class="footer-legal">
        <span>&copy; {YEAR} Lark Services LLC. All rights reserved. Lark Data Solutions is a trade name of Lark Services LLC.</span>
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
    }})();
  </script>
</body>
</html>
'''


def cta(heading="Ready to put your data to work?", text="Tell us about your project. The first consultation is free."):
    return f'''    <section>
      <div class="container">
        <div class="cta">
          <div>
            <h2>{heading}</h2>
            <p>{text}</p>
          </div>
          <a class="btn" href="/contact-us/">Schedule a Free Consultation</a>
        </div>
      </div>
    </section>'''


def write(rel, html):
    p = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(html)


# ---------- Home ----------
cards = "\n".join(f'''          <a class="card" href="/our-services/#{sid}">
            <div class="dot {c}" aria-hidden="true"></div>
            <h3>{name}</h3>
            <p>{short}</p>
            <span class="more">Learn more &rarr;</span>
          </a>''' for sid, name, c, short, *_ in SERVICES)

home = f'''    <section class="hero">
      <div class="container">
        <div>
          <span class="eyebrow">Data Science &amp; Research Consulting</span>
          <h1>Helping Your Data <span>Take Flight.</span></h1>
          <p class="lead">Lark Data Solutions helps organizations turn complex data into clear strategies and intelligent solutions. We combine scientific rigor with leading technology to help you gain clarity from your data, overcome analytical hurdles, and build smart systems that make an impact.</p>
          <div class="btn-row">
            <a class="btn" href="/contact-us/">Schedule a Free Consultation</a>
            <a class="btn btn-ghost" href="/our-services/">Explore Our Services</a>
          </div>
        </div>
        <div class="hero-art">
          <img src="/assets/img/data-dots.webp" width="1000" height="501" alt="" fetchpriority="high">
        </div>
      </div>
    </section>

    <section class="section-soft" aria-labelledby="help-heading">
      <div class="container">
        <div class="section-head">
          <span class="eyebrow">What we do</span>
          <h2 id="help-heading">How We Can Help You</h2>
          <p class="lead">Explore how our core service areas empower your organization through data.</p>
        </div>
        <div class="grid grid-4">
{cards}
        </div>
      </div>
    </section>

    <section aria-labelledby="why-heading">
      <div class="container split">
        <div>
          <span class="eyebrow">Why Lark</span>
          <h2 id="why-heading">Why Choose Lark Data Solutions?</h2>
          <p class="lead">Our backgrounds, rooted in real-world data analysis and advanced mathematics, ensure your solutions are not just innovative, but also scientifically sound and ethically grounded.</p>
          <div class="team-preview">
            <a href="/about-us/#duncan-clark"><img src="/assets/img/duncan-clark-320.webp" width="64" height="64" alt="Duncan Clark, PhD" loading="lazy"><span>Duncan Clark, PhD<small>Machine Learning &amp; Intelligent Systems</small></span></a>
            <a href="/about-us/#amanda-luff"><img src="/assets/img/amanda-luff-320.webp" width="64" height="64" alt="Amanda Luff, PhD" loading="lazy"><span>Amanda Luff, PhD<small>Research Methodology &amp; Analytic Strategy</small></span></a>
          </div>
        </div>
        <ul class="checklist">
          <li><strong>Practical, implementable solutions.</strong> Based in Milwaukee, Wisconsin, we apply our expertise to deliver practical solutions and clear, strategic guidance that goes beyond a report.</li>
          <li><strong>End to end.</strong> We connect the essentials, from designing foundational research and generating robust evidence, to the sophisticated implementation of machine learning and AI systems.</li>
          <li><strong>Side by side.</strong> We collaborate with you, investing time to understand your challenges and working side-by-side to achieve your goals.</li>
        </ul>
      </div>
    </section>

{cta()}'''

write("index.html", page("/",
    "Lark Data Solutions | Data Strategy, Machine Learning & AI Consulting",
    "Lark Data Solutions helps organizations turn complex data into clear strategies and intelligent solutions: data strategy, machine learning and AI, statistical analysis, and research protocol design. Based in Milwaukee, WI.",
    home))

# ---------- Services ----------
blocks = "\n".join(f'''        <article class="service" id="{sid}" aria-labelledby="{sid}-h">
          <div class="service-intro">
            <div class="dot {c}" aria-hidden="true"></div>
            <h2 id="{sid}-h">{name}</h2>
            <p>{long}</p>
          </div>
          <ul>
{chr(10).join(f"            <li><strong>{t}</strong><span>{d}</span></li>" for t, d in items)}
          </ul>
        </article>''' for sid, name, c, short, long, items in SERVICES)

services_schema = [{
    "@type": "Service", "name": name, "description": long, "serviceType": name,
    "provider": {"@id": SITE + "/#organization"}, "areaServed": "Worldwide",
    "url": f"{SITE}/our-services/#{sid}",
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": name, "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": t, "description": d}} for t, d in items]},
} for sid, name, c, short, long, items in SERVICES]

services = f'''    <section class="page-hero">
      <div class="container">
        <span class="eyebrow">Our Services</span>
        <h1>What We Do</h1>
        <p class="lead">At Lark Data Solutions, we help organizations of all sizes leverage their data to make smarter decisions, understand complex trends, and build intelligent solutions. We translate intricate data into clear, actionable insights.</p>
      </div>
    </section>

    <section style="padding-top:24px">
      <div class="container">
{blocks}
      </div>
    </section>

{cta("Not sure where to start?", "We'll help you figure out which services fit your goals. The first consultation is free.")}'''

write("our-services/index.html", page("/our-services/",
    "Services: Data Strategy, ML & AI, Analytics, Protocol Design | Lark Data Solutions",
    "Data strategy and analytics consulting, custom machine learning and AI solutions, advanced statistical analysis and evidence generation, and research protocol design and compliance.",
    services, services_schema))

# ---------- About ----------
def person(pid, img, name, role, bio, tags, li):
    return f'''        <article class="person" id="{pid}">
          <img src="/assets/img/{img}.webp" width="640" height="640" alt="Portrait of {name}" loading="lazy">
          <div>
            <h2>{name}</h2>
            <p class="role">{role}</p>
            <p>{bio}</p>
            <h3>Expertise</h3>
            <ul class="tags">
{chr(10).join(f"              <li>{t}</li>" for t in tags)}
            </ul>
            <a href="{li}" rel="noopener" target="_blank">More about {name.split()[0]} on LinkedIn &rarr;</a>
          </div>
        </article>'''

about = f'''    <section class="page-hero">
      <div class="container">
        <span class="eyebrow">About Us</span>
        <h1>Real-world data analysis meets advanced data science.</h1>
        <p class="lead">Lark Data Solutions was founded on a simple idea: bringing together real-world data analysis and advanced data science. Our partners, with backgrounds in applied mathematics and statistics, offer a powerful combination of analytical insight and technical ability. Based in Milwaukee, Wisconsin, we help global organizations translate complex data into clear plans and effective solutions.</p>
      </div>
    </section>

    <section style="padding-top:24px" aria-labelledby="partners-heading">
      <div class="container">
        <h2 id="partners-heading" class="eyebrow" style="font-size:0.8rem">Meet Our Partners</h2>
{person("duncan-clark", "duncan-clark", "Duncan Clark, PhD", "Partner, Machine Learning &amp; Intelligent Systems",
        "Duncan is a data scientist and machine learning specialist. He excels at translating complex concepts into practical, impactful solutions.",
        ["Machine Learning &amp; Deep Learning", "Predictive Modeling &amp; AI Systems", "Python Development", "Natural Language Processing"],
        "https://www.linkedin.com/in/duncan-clark-1b3548288/")}
{person("amanda-luff", "amanda-luff", "Amanda Luff, PhD", "Partner, Research Methodology &amp; Analytic Strategy",
        "Amanda is a quantitative researcher and data strategist with over a decade of experience analyzing real-world data. She excels at designing and leading complex research, transforming data into clear, evidence-based findings grounded in rigorous methodology and ethical practices.",
        ["Research &amp; Study Design", "Real World Data Analysis &amp; Evidence Generation", "Advanced Statistical Methods", "Research Compliance", "Research Reporting &amp; Dissemination"],
        "https://www.linkedin.com/in/amanda-luff/")}
      </div>
    </section>

{cta("Let's work together.", "Tell us about your data challenge and we'll find the right approach.")}'''

write("about-us/index.html", page("/about-us/",
    "About Us: Duncan Clark, PhD & Amanda Luff, PhD | Lark Data Solutions",
    "Meet the partners of Lark Data Solutions: Duncan Clark, PhD (machine learning and intelligent systems) and Amanda Luff, PhD (research methodology and analytic strategy). Based in Milwaukee, WI.",
    about, PEOPLE))

# ---------- Contact ----------
contact = f'''    <section class="page-hero">
      <div class="container">
        <span class="eyebrow">Contact Us</span>
        <h1>Let's Connect!</h1>
        <p class="lead">We encourage prospective clients to use our contact form, as it helps us understand your needs efficiently. If you prefer, you can email us directly.</p>
      </div>
    </section>

    <section style="padding-top:16px">
      <div class="container contact-grid">
        <div class="card">
          <div class="dot c-teal" aria-hidden="true"></div>
          <h2>Contact form</h2>
          <p>Share a few details about your organization and project goals, and we'll follow up to schedule a free consultation.</p>
          <a class="btn" href="{FORM}" rel="noopener" target="_blank">Open the Contact Form</a>
        </div>
        <div class="card">
          <div class="dot c-orange" aria-hidden="true"></div>
          <h2>Email</h2>
          <p>Prefer email? Reach us directly and we'll get back to you.</p>
          <a class="btn btn-ghost" href="mailto:{EMAIL}">{EMAIL}</a>
        </div>
      </div>
    </section>'''

write("contact-us/index.html", page("/contact-us/",
    "Contact Us | Lark Data Solutions",
    "Get in touch with Lark Data Solutions to schedule a free consultation about data strategy, machine learning and AI, statistical analysis, or research protocol design.",
    contact, [{"@type": "ContactPage", "url": SITE + "/contact-us/", "about": {"@id": SITE + "/#organization"}}]))

# ---------- Policies ----------
legal = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "policies_body.html"), encoding="utf-8").read()
write("policies/index.html", page("/policies/",
    "Terms of Service, Privacy Policy & Disclaimers | Lark Data Solutions",
    "Terms of service, privacy policy, and disclaimers for larkdatasolutions.com, operated by Lark Services LLC, doing business as Lark Data Solutions.",
    legal))

# ---------- /home (old Google Sites URL) -> / ----------
write("home/index.html", f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Lark Data Solutions</title>
  <link rel="canonical" href="{SITE}/">
  <meta name="robots" content="noindex, follow">
  <meta http-equiv="refresh" content="0; url=/">
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
          <a class="btn btn-ghost" href="/our-services/">Our Services</a>
          <a class="btn btn-ghost" href="/contact-us/">Contact Us</a>
        </div>
      </div>
    </section>''', robots="noindex"))

# ---------- robots + sitemap ----------
open(os.path.join(OUT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
urls = [("/", "1.0"), ("/our-services/", "0.9"), ("/about-us/", "0.8"), ("/contact-us/", "0.7"), ("/policies/", "0.3")]
open(os.path.join(OUT, "sitemap.xml"), "w").write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url>\n    <loc>{SITE}{u}</loc>\n    <lastmod>2026-10-13</lastmod>\n    <priority>{p}</priority>\n  </url>\n" for u, p in urls) +
    "</urlset>\n")
open(os.path.join(OUT, ".nojekyll"), "w").write("")
print("built")
