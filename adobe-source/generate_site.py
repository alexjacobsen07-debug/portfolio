#!/usr/bin/env python3
"""One-off generator for the project gallery + detail pages.
Run once from the project root: python3 adobe-source/generate_site.py
Safe to re-run — it just overwrites the generated HTML files.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NAV = """  <header class="site-header">
    <a class="logo" href="/">Alex Jacobsen</a>
    <nav>
      <a href="/">Work</a>
      <a href="/contact.html">Contact</a>
    </nav>
  </header>"""

FOOTER = """  <footer class="site-footer">
    &copy; <span class="year"></span> Alex Jacobsen
  </footer>
  <script>document.querySelectorAll('.year').forEach(el => el.textContent = new Date().getFullYear());</script>"""

def youtube_embed(video_id):
    return f'''  <div class="video-embed">
    <iframe src="https://www.youtube.com/embed/{video_id}" title="YouTube video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
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
        "subtitle": "Producer",
        "body": "Part of a custom video partnership with PUMA for their release of the MB.1 shoe. We used Hudl highlights from LaMelo's high school days to help tie this campaign to a high school basketball audience in the Hudl app.",
        "media": [
            watch_link("https://www.hudl.com/video/61bd0912041da90e445a8b71"),
        ],
    },
    {
        "slug": "gatorade-fueled",
        "title": "Gatorade Fueled",
        "subtitle": "Producer/Shooter/Editor",
        "body": "Can a team's surroundings influence their style of play? Can community fuel their drive to win? Introducing Fueled — exploring how a team's competitive edge is driven by those on and off the field.",
        "media": [
            youtube_embed("DjIDVZXSjtE"),
        ],
    },
    {
        "slug": "hudl-contenders",
        "title": "Hudl Contenders",
        "subtitle": "Producer/Director/Shooter/Editor",
        "body": "Hudl Contenders is an Hudl original content series. My team created, produced, shot and edited each piece. During its three seasons, Contenders has been sponsored by Facebook, Snapchat and Gatorade and has won two Heartland Emmy awards for best sports programming.\n\nEach week, Contenders follows two top-ranked high school football players as they prepare to face off under the lights. The docu-series produced by Hudl provides a behind-the-scenes look at the competition and admiration among the top recruits in the nation.",
        "media": [
            watch_link("https://www.hudl.com/video/5d7be2d768991805e8b3d7a1", "Watch Episode 1 on Hudl"),
            watch_link("https://www.hudl.com/video/5bcf7096f56a8b0e1c93e439", "Watch Episode 2 on Hudl"),
            watch_link("https://www.hudl.com/video/59e9139c02b1c80a5034323e", "Watch Episode 3 on Hudl"),
        ],
    },
    {
        "slug": "gatorade-highlight-themes",
        "title": "Gatorade Highlight Themes",
        "subtitle": "Producer/editor",
        "body": "",
        "media": [
            watch_link("https://www.hudl.com/video/6189859c02b2150b58835c04"),
        ],
    },
    {
        "slug": "sierra-canyon",
        "title": "Sierra Canyon",
        "subtitle": "Producer/director/shooter/editor",
        "body": "Sierra Canyon is the most dominant program in the nation. We meet three of their star players Scotty Pippen Jr., Cassius Stanley and KJ Martin.",
        "media": [
            watch_link("https://www.hudl.com/video/5c64097a386dd90670ee4d28"),
        ],
    },
    {
        "slug": "nfl-draft-chase-winovich",
        "title": "NFL Draft - Chase Winovich",
        "subtitle": "Producer/shooter/editor",
        "body": "Chase Winovich has been chasing his dream of playing in the NFL since he was 7 years old. Because of his work ethic, that dream is now within reach.",
        "media": [
            watch_link("https://www.hudl.com/video/5cc0d3e76e8bf90e30d6a7d5"),
        ],
    },
    {
        "slug": "scotty-pippen-jr-hudl-kicks",
        "title": "Scotty Pippen Jr - Hudl Kicks",
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
        "subtitle": "",
        "body": "To further my education, I attended a non-fiction cinematography course taught by renowned videographer Zach Zamboni. Zach has won 3 Primetime Emmy Awards, and earned 5 nominations for Non-Fiction Cinematography. His series, Parts Unknown, has won the Peabody Award.",
        "media": [
            video_placeholder(),
        ],
    },
    {
        "slug": "hudl-top-5",
        "title": "Hudl Top 5",
        "subtitle": "Producer/editor",
        "body": "The Gen Z athlete is looking for short, bite-sized content, so we've adjusted Top 5 to match their viewing habits. Each play is distributed independently, as snackable content, improving brand touch points and engagement on Hudl and Instagram.",
        "media": [
            watch_link("https://www.hudl.com/page/top-5-football/videos"),
        ],
    },
    {
        "slug": "champs-sports",
        "title": "Champs Sports",
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
        "subtitle": "Producer/director/editor",
        "body": "",
        "media": [
            watch_link("https://www.hudl.com/video/60f6de560dca580c14c12266"),
        ],
    },
    {
        "slug": "kamaka-hepa-profile",
        "title": "Kamaka Hepa Profile",
        "subtitle": "Producer/director/shooter/editor",
        "body": "Growing up in Barrow, Alaska, the most northern city in the United States, Kamaka Hepa knew what he had to do to get to the next level. What would you be willing to sacrifice?",
        "media": [
            watch_link("https://www.hudl.com/video/5a943f0202b1c82658a05f58"),
        ],
    },
]

def project_page(p):
    media_html = "\n".join(p["media"])
    body_html = f'  <p class="project-body">{p["body"]}</p>\n' if p["body"] else ""
    subtitle_html = f'    <p class="project-subtitle">{p["subtitle"]}</p>\n' if p["subtitle"] else ""
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{p["title"]} | Alex Jacobsen</title>
  <link rel="stylesheet" href="/styles.css" />
</head>
<body>
{NAV}

  <main>
    <img class="project-hero" src="/images/covers/{p["slug"]}.jpg" alt="{p["title"]} cover" />
    <h1 class="project-title">{p["title"]}</h1>
{subtitle_html}{body_html}
{media_html}

    <a class="back-link" href="/">&larr; Back to all work</a>
  </main>

{FOOTER}
</body>
</html>
"""

def gallery_card(p):
    return f'''      <a class="project-card" href="/{p["slug"]}.html">
        <img src="/images/covers/{p["slug"]}.jpg" alt="{p["title"]}" loading="lazy" />
        <div class="project-card-title">{p["title"]}</div>
      </a>'''

def gallery_page():
    cards = "\n".join(gallery_card(p) for p in PROJECTS)
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Alex Jacobsen</title>
  <link rel="stylesheet" href="/styles.css" />
</head>
<body>
{NAV}

  <main>
    <h1 class="gallery-title">Work</h1>
    <div class="project-grid">
{cards}
    </div>
  </main>

{FOOTER}
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
