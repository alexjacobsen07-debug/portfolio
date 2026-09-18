#!/usr/bin/env python3
"""One-off generator for the homepage + project detail pages.
Run once from the project root: python3 adobe-source/generate_site.py
Safe to re-run — it just overwrites the generated HTML files.
Design language borrowed from a RAUM Studio (Lovable) template Alex remixed:
Inter type, phi-scaled headline sizes, warm light-gray palette, fixed
reveal-on-scroll footer, watermark section heading, filterable work grid.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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

PROJECTS = [
    {
        "slug": "level-the-playing-field",
        "title": "Level the Playing Field",
        "category": "Brand Campaign",
        "subtitle": "Producer/Shooter/Motion Designer",
        "body": "Gatorade and Hudl are partnering to offer the Level the Playing Field grant. This three-year grant program will honor three deserving youth organizations in the U.S. with a suite of Hudl products customized to their individual needs.",
        "media": [
            watch_link("https://www.hudl.com/theplayingfield", "hudl.com/theplayingfield"),
            youtube_embed("IjLs3xIZCi4"),
            youtube_embed("749D2zTEX0I"),
            youtube_embed("8Q9lqMPhwI8"),
            youtube_embed("7kfcM2VFFuI"),
            video_placeholder(),
        ],
    },
    {
        "slug": "puma-lamelo-ball",
        "title": "PUMA - LaMelo Ball",
        "category": "Brand Campaign",
        "subtitle": "Producer",
        "body": "Part of a custom video partnership with PUMA for their release of the MB.1 shoe. We used Hudl highlights from LaMelo's high school days to help tie this campaign to a high school basketball audience in the Hudl app.",
        "media": [
            watch_link("https://www.hudl.com/video/61bd0912041da90e445a8b71"),
        ],
    },
    {
        "slug": "gatorade-fueled",
        "title": "Gatorade Fueled",
        "category": "Brand Campaign",
        "subtitle": "Producer/Shooter/Editor",
        "body": "Can a team's surroundings influence their style of play? Can community fuel their drive to win? Introducing Fueled — exploring how a team's competitive edge is driven by those on and off the field. One installment followed Houston's Heights High School football team, featuring an appearance and soundtrack by Houston native Tobe Nwigwe.",
        "media": [
            youtube_embed("DjIDVZXSjtE"),
            youtube_embed("zyPcwAzGaAY"),
        ],
    },
    {
        "slug": "hudl-contenders",
        "title": "Hudl Contenders",
        "category": "Documentary Series",
        "subtitle": "Producer/Director/Shooter/Editor",
        "body": "Hudl Contenders is an Hudl original content series. My team created, produced, shot and edited each piece. During its three seasons, Contenders has been sponsored by Facebook, Snapchat and Gatorade and has won two Heartland Emmy awards for best sports programming.\n\nEach week, Contenders follows two top-ranked high school football players as they prepare to face off under the lights. The docu-series produced by Hudl provides a behind-the-scenes look at the competition and admiration among the top recruits in the nation.",
        "media": [
            watch_link("https://www.hudl.com/video/5d7be2d768991805e8b3d7a1", "Watch Episode 1 on Hudl"),
            watch_link("https://www.hudl.com/video/5bcf7096f56a8b0e1c93e439", "Watch Episode 2 on Hudl"),
            watch_link("https://www.hudl.com/video/59e9139c02b1c80a5034323e", "Watch Episode 3 on Hudl"),
            watch_link("https://www.hudl.com/video/5da0b905344949068c91b1bb", "Watch: Kobe Hudson vs. Tank Bigsby on Hudl"),
        ],
    },
    {
        "slug": "gatorade-highlight-themes",
        "title": "Gatorade Highlight Themes",
        "category": "Brand Campaign",
        "subtitle": "Producer/editor",
        "body": "",
        "media": [
            watch_link("https://www.hudl.com/video/6189859c02b2150b58835c04"),
        ],
    },
    {
        "slug": "sierra-canyon",
        "title": "Sierra Canyon",
        "category": "Documentary Series",
        "subtitle": "Producer/director/shooter/editor",
        "body": "Sierra Canyon is the most dominant program in the nation. We meet three of their star players Scotty Pippen Jr., Cassius Stanley and KJ Martin.",
        "media": [
            watch_link("https://www.hudl.com/video/5c64097a386dd90670ee4d28"),
        ],
    },
    {
        "slug": "nfl-draft-chase-winovich",
        "title": "NFL Draft - Chase Winovich",
        "category": "Athlete Profile",
        "subtitle": "Producer/shooter/editor",
        "body": "Chase Winovich has been chasing his dream of playing in the NFL since he was 7 years old. Because of his work ethic, that dream is now within reach.",
        "media": [
            watch_link("https://www.hudl.com/video/5cc0d3e76e8bf90e30d6a7d5"),
        ],
    },
    {
        "slug": "scotty-pippen-jr-hudl-kicks",
        "title": "Scotty Pippen Jr - Hudl Kicks",
        "category": "Documentary Series",
        "subtitle": "Producer/director/shooter/editor",
        "body": "",
        "media": [
            watch_link("https://www.hudl.com/video/5c8fc1d8386dd91c74ded76d", "Watch Part 1 on Hudl"),
            watch_link("https://www.hudl.com/video/5c7d88e123481e1bd85d7038", "Watch Part 2 on Hudl"),
            watch_link("https://www.hudl.com/video/5c86a8406e8bf91828da8431", "Watch Part 3 on Hudl"),
        ],
    },
    {
        "slug": "maine-media-zach-zamboni",
        "title": "Maine Media - Zach Zamboni",
        "category": "Personal",
        "subtitle": "",
        "body": "To further my education, I attended a non-fiction cinematography course taught by renowned videographer Zach Zamboni. Zach has won 3 Primetime Emmy Awards, and earned 5 nominations for Non-Fiction Cinematography. His series, Parts Unknown, has won the Peabody Award.",
        "media": [
            video_placeholder(),
        ],
    },
    {
        "slug": "hudl-top-5",
        "title": "Hudl Top 5",
        "category": "Brand Campaign",
        "subtitle": "Producer/editor",
        "body": "The Gen Z athlete is looking for short, bite-sized content, so we've adjusted Top 5 to match their viewing habits. Each play is distributed independently, as snackable content, improving brand touch points and engagement on Hudl and Instagram.",
        "media": [
            watch_link("https://www.hudl.com/page/top-5-football/videos"),
        ],
    },
    {
        "slug": "champs-sports",
        "title": "Champs Sports",
        "category": "Brand Campaign",
        "subtitle": "Producer/editor",
        "body": "Champs x Reebok Crossover Campaign. Objective: Leverage Hudl to drive awareness of Reebok Basketball as well as Allen Iverson product drops. In this campaign, we sourced user-created Hudl highlights mixed with beauty product shots of Allen Iverson's new shoe, which I shot in our studio.",
        "media": [
            video_placeholder(),
            video_placeholder(),
        ],
    },
    {
        "slug": "grrridiron-girls",
        "title": "Grrridiron Girls",
        "category": "Documentary Series",
        "subtitle": "Producer/director/editor",
        "body": "",
        "media": [
            watch_link("https://www.hudl.com/video/60f6de560dca580c14c12266"),
        ],
    },
    {
        "slug": "kamaka-hepa-profile",
        "title": "Kamaka Hepa Profile",
        "category": "Athlete Profile",
        "subtitle": "Producer/director/shooter/editor",
        "body": "Growing up in Barrow, Alaska, the most northern city in the United States, Kamaka Hepa knew what he had to do to get to the next level. What would you be willing to sacrifice?",
        "media": [
            watch_link("https://www.hudl.com/video/5a943f0202b1c82658a05f58"),
        ],
    },
    {
        "slug": "ai-powered-reports",
        "title": "AI-Powered Reports",
        "category": "Systems & AI",
        "subtitle": "Creative Direction / Systems Design",
        "body": "A look at one of the AI-assisted systems built inside Hudl's in-house creative studio — turning raw data into branded, ready-to-publish reports automatically, part of a broader effort to scale content output without scaling headcount.",
        "media": [
            vimeo_embed("1219915768", h="d303b6de5d"),
        ],
    },
    {
        "slug": "walk-the-walk-lance-haas",
        "title": "Walk the Walk: Lance Haas",
        "category": "Athlete Profile",
        "subtitle": "Producer/Director/Editor",
        "body": "An installment of Hudl's Walk the Walk series, profiling Lance Haas at Mountain View High School.",
        "media": [
            youtube_embed("0h9lWdz_ii4"),
        ],
    },
]

SERVICES = [
    ("Creative Direction", "Leading concept-to-delivery for brand and partner campaigns."),
    ("Production Management", "Running the full pipeline: intake, scoping, scheduling, delivery."),
    ("AI-Assisted Workflows", "Building systems that scale output without scaling headcount."),
    ("Shooting & Editing", "Hands-on cinematography and post-production."),
    ("Motion Design", "Templated and custom graphics at scale."),
]

STATS = [
    ("11", "Years at Hudl"),
    ("80%", "Faster turnaround via AI-assisted editing"),
    ("2,000+", "Templated motion-graphics assets"),
    ("30+", "Branded packages delivered weekly"),
]

HERO_IMAGE = "sierra-canyon"

HERO_TAGLINE = "Leading Hudl's in-house creative studio — video production, creative operations, and AI-powered systems for brand and partner content."

ABOUT_BODY = (
    "Alex leads Hudl's in-house creative studio — the video team behind brand and partner "
    "content, from concept through delivery. Over 11 years at Hudl, he's grown from producer "
    "to studio leader, delivering campaigns for T-Mobile, Chase, Gatorade, PUMA, and the U.S. "
    "Army, and managing the studio's enterprise vendor stack (DAM, music licensing, transfer "
    "and review infrastructure). To scale output without scaling headcount, he's built "
    "AI-assisted editing workflows that cut turnaround time 80% across 30+ weekly branded "
    "packages, a library of 2,000+ templated motion-graphics assets, and an intake pipeline "
    "that automatically turns requests into scoped briefs. He's a 2x Heartland Emmy winner "
    "for sports programming."
)

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
            <div class="stat-value">Creative Studio Leader</div>
          </div>
          <div>
            <div class="stat-label">Focus</div>
            <div class="stat-value">Video Production &amp; AI Systems</div>
          </div>
          <div>
            <div class="stat-label">Clients</div>
            <div class="stat-value">T-Mobile, Chase, Gatorade, PUMA, U.S. Army</div>
          </div>
        </div>
        <div class="hero-image">
          <img src="/images/covers/{HERO_IMAGE}.jpg" alt="Featured work" />
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
