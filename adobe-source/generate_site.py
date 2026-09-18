#!/usr/bin/env python3
"""One-off generator for the homepage + project detail pages.
Run once from the project root: python3 adobe-source/generate_site.py
Safe to re-run — it just overwrites the generated HTML files.
Design language borrowed from a RAUM Studio (Lovable) template Alex remixed:
Inter type, phi-scaled headline sizes, warm light-gray palette, fixed
reveal-on-scroll footer, watermark section heading, filterable work grid.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, "content.json")) as f:
    CONTENT = json.load(f)

TAGLINE = "Creative Studio Leader, Hudl"
SITE_URL = "https://alexjacobsen.pages.dev"
LINKEDIN_URL = "https://www.linkedin.com/in/alexjacobsen/"
SITE_DESCRIPTION = (
    "Alex Jacobsen leads Hudl's in-house creative studio, producing brand and partner "
    "video content for T-Mobile, Chase, Gatorade, PUMA, and the U.S. Army, and building "
    "AI-assisted production systems. 2x Heartland Emmy winner."
)


def head_meta(title, description, image_slug):
    image_url = f"{SITE_URL}/images/covers/{image_slug}.jpg"
    return f'''  <meta name="description" content="{description}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{description}" />
  <meta property="og:image" content="{image_url}" />
  <meta name="twitter:card" content="summary_large_image" />'''


def header(active):
    work_cls = ' class="active"' if active == "work" else ""
    contact_cls = ' class="active"' if active == "contact" else ""
    return f"""  <header class="site-header">
    <a class="logo" href="/">Alex Jacobsen</a>
    <div class="site-tagline">{TAGLINE}</div>
    <nav>
      <a href="/"{work_cls}>Work</a>
      <a href="/contact.html"{contact_cls}>Contact</a>
      <a href="{LINKEDIN_URL}" target="_blank" rel="noopener">LinkedIn</a>
    </nav>
  </header>"""


FOOTER_FIXED = f"""  <footer class="site-footer-fixed">
    <div class="inner">
      <div class="footer-left">
        <a href="/" class="footer-logo">Alex Jacobsen</a>
        <a href="{LINKEDIN_URL}" target="_blank" rel="noopener">LinkedIn</a>
      </div>
      <button class="back-to-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">Back to Top</button>
    </div>
    <div class="footer-copy">&copy; <span class="year"></span> Alex Jacobsen. All rights reserved.</div>
  </footer>
  <script>document.querySelectorAll('.year').forEach(el => el.textContent = new Date().getFullYear());</script>"""


def youtube_embed(video_id):
    return f'''  <div class="video-embed">
    <iframe src="https://www.youtube.com/embed/{video_id}" title="YouTube video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
  </div>'''

def vimeo_embed(video_id, h=None):
    src = f"https://player.vimeo.com/video/{video_id}" + (f"?h={h}" if h else "")
    return f'''  <div class="video-embed">
    <iframe src="{src}" title="Vimeo video" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" allowfullscreen loading="lazy"></iframe>
  </div>'''

def hudl_embed(video_id):
    return f'''  <div class="video-embed">
    <iframe src="https://www.hudl.com/embed/video/{video_id}" title="Hudl video" allowfullscreen loading="lazy"></iframe>
  </div>'''

def watch_link(url, label="Watch on Hudl"):
    return f'''  <a class="watch-link" href="{url}" target="_blank" rel="noopener">
    <span class="play-icon">&#9654;</span>
    <span>
      <span class="watch-label">{label}</span><br>
      <span class="watch-sub">Opens in a new tab</span>
    </span>
  </a>'''

def video_placeholder():
    return '''  <div class="video-placeholder">Video coming soon</div>'''

def render_media_item(item):
    """Render one media entry from content.json (edited via /admin.html) to HTML."""
    t = item.get("type")
    if t == "youtube":
        return youtube_embed(item["id"])
    if t == "vimeo":
        return vimeo_embed(item["id"], h=item.get("h") or None)
    if t == "hudl":
        return hudl_embed(item["id"])
    if t == "watch_link":
        return watch_link(item["url"], item.get("label") or "Watch on Hudl")
    return video_placeholder()

# All editable content (titles, categories, body copy, video links, hero/about/
# services/stats) comes from content.json, which the admin page (/admin.html)
# edits and commits back to the repo via the save-content Function.
PROJECTS = [
    {**p, "media": [render_media_item(m) for m in p.get("media", [])]}
    for p in CONTENT["projects"]
]

SERVICES = [(s["name"], s["desc"]) for s in CONTENT["services"]]
STATS = [(s["value"], s["label"]) for s in CONTENT["stats"]]
HERO_IMAGE = CONTENT["hero"].get("image", "sierra-canyon")
HERO_IMAGE_POSITION = CONTENT["hero"].get("imagePosition", "center 50%")
HERO_TAGLINE = CONTENT["hero"]["tagline"]
HERO_ROLE = CONTENT["hero"]["role"]
HERO_FOCUS = CONTENT["hero"]["focus"]
HERO_CLIENTS = CONTENT["hero"]["clients"]
ABOUT_BODY = CONTENT["about"]

def project_page(p):
    media_html = "\n".join(p["media"])
    body_html = f'  <p class="project-body">{p["body"]}</p>\n' if p["body"] else ""
    subtitle_html = f'    <p class="project-subtitle">{p["subtitle"]}</p>\n' if p["subtitle"] else ""
    description = p["body"] if p["body"] else f'{p["title"]} — video production work by Alex Jacobsen.'
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{p["title"]} | Alex Jacobsen</title>
{head_meta(f'{p["title"]} | Alex Jacobsen', description, p["slug"])}
  <link rel="stylesheet" href="/styles.css" />
</head>
<body>
  <div class="site-wrap">
{header("work")}

  <main>
    <img class="project-hero" src="/images/covers/{p["slug"]}.jpg" alt="{p["title"]} cover" />
    <h1 class="project-title">{p["title"]}</h1>
{subtitle_html}{body_html}
{media_html}

    <a class="back-link" href="/">&larr; Back to all work</a>
  </main>
  </div>

{FOOTER_FIXED}
</body>
</html>
"""

def gallery_card(p):
    return f'''      <a class="project-card" href="/{p["slug"]}.html" data-category="{p["category"]}">
        <img src="/images/covers/{p["slug"]}.jpg" alt="{p["title"]}" loading="lazy" />
        <div class="project-card-category">{p["category"]}</div>
        <div class="project-card-title">{p["title"]}</div>
      </a>'''

def filter_options():
    seen = []
    for p in PROJECTS:
        if p["category"] not in seen:
            seen.append(p["category"])
    opts = ['      <option value="all">All work</option>']
    for c in seen:
        opts.append(f'      <option value="{c}">{c}</option>')
    return "\n".join(opts)

def services_html():
    items = []
    for i, (name, desc) in enumerate(SERVICES, start=1):
        items.append(f'''      <div class="service-item">
        <span class="service-num">{i:02d}</span>
        <span class="service-name">{name}</span>
        <span class="service-desc">{desc}</span>
      </div>''')
    return "\n".join(items)

def stats_html():
    items = []
    for value, label in STATS:
        items.append(f'''      <div class="stat-tile">
        <div class="stat-tile-value">{value}</div>
        <div class="stat-tile-label">{label}</div>
      </div>''')
    return "\n".join(items)

def gallery_page():
    cards = "\n".join(gallery_card(p) for p in PROJECTS)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Alex Jacobsen — Creative Studio Leader, Hudl</title>
{head_meta("Alex Jacobsen — Creative Studio Leader, Hudl", SITE_DESCRIPTION, HERO_IMAGE)}
  <link rel="stylesheet" href="/styles.css" />
</head>
<body>
  <div class="site-wrap">
{header("work")}

  <main>
    <div class="container">
      <section class="hero-section" id="hero">
        <div class="hero-top">
          <h1 class="hero-name">Alex Jacobsen</h1>
          <p class="hero-tagline">{HERO_TAGLINE}</p>
        </div>
        <div class="hero-stats">
          <div>
            <div class="stat-label">Role</div>
            <div class="stat-value">{HERO_ROLE}</div>
          </div>
          <div>
            <div class="stat-label">Focus</div>
            <div class="stat-value">{HERO_FOCUS}</div>
          </div>
          <div>
            <div class="stat-label">Clients</div>
            <div class="stat-value">{HERO_CLIENTS}</div>
          </div>
        </div>
        <div class="hero-image">
          <img src="/images/covers/{HERO_IMAGE}.jpg" alt="Featured work" style="object-position: {HERO_IMAGE_POSITION};" />
        </div>
      </section>

      <section class="stats-section" id="impact">
        <div class="stats-grid">
{stats_html()}
        </div>
      </section>

      <section class="work-section" id="work">
        <div class="work-watermark" aria-hidden="true">WORK</div>
        <div class="work-heading-row">
          <h2 class="work-heading">Selected work spanning brand campaigns, documentary series, athlete profiles, and the AI-powered systems built to produce them — for Hudl, T-Mobile, Chase, Gatorade, PUMA, and more.</h2>
          <div class="work-filters">
            <select class="filter-select" id="work-filter" aria-label="Filter work by category">
{filter_options()}
            </select>
          </div>
        </div>
        <div class="project-grid" id="project-grid">
{cards}
        </div>
      </section>

      <section class="services-section" id="services">
        <h2 class="services-heading">Services</h2>
        <div class="service-list">
{services_html()}
        </div>
      </section>

      <section class="about-section" id="about">
        <h2 class="about-heading">About</h2>
        <p class="about-body">{ABOUT_BODY}</p>
      </section>

      <section class="cta-section" id="contact-cta">
        <h2 class="cta-heading">Let's work together</h2>
        <a class="cta-button" href="/contact.html">Get in touch</a>
      </section>
    </div>
  </main>
  </div>

{FOOTER_FIXED}
  <script>
    const filterSelect = document.getElementById('work-filter');
    const cards = document.querySelectorAll('#project-grid .project-card');
    filterSelect.addEventListener('change', () => {{
      const value = filterSelect.value;
      cards.forEach(card => {{
        const match = value === 'all' || card.dataset.category === value;
        card.classList.toggle('is-hidden', !match);
      }});
    }});
  </script>
</body>
</html>
"""

def main():
    for p in PROJECTS:
        path = os.path.join(ROOT, f'{p["slug"]}.html')
        with open(path, "w") as f:
            f.write(project_page(p))
        print("wrote", path)

    index_path = os.path.join(ROOT, "index.html")
    with open(index_path, "w") as f:
        f.write(gallery_page())
    print("wrote", index_path)

if __name__ == "__main__":
    main()
