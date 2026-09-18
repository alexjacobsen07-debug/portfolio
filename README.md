# alex-portfolio

Static site, deployed on Cloudflare Pages. Plain HTML/CSS, plus Cloudflare Pages
Functions for the contact form and the admin editor.

The homepage and all project pages are generated from `content.json` by
`adobe-source/generate_site.py`. Cloudflare Pages runs that script automatically on every
build (see **Build command** in Deploying, below) — either edit `content.json` yourself
and push, or use the `/admin.html` page (see below), which saves straight to GitHub and
triggers the same rebuild.

## Contact form setup

The form at `/contact.html` posts to `/api/contact` (`functions/api/contact.js`), which
sends the message via [Resend](https://resend.com) to `alexjacobsen07@gmail.com`.

To make it live:

1. Create a free Resend account at https://resend.com (100 emails/day, no credit card).
2. Create an API key (Resend dashboard → API Keys).
3. In the Cloudflare Pages project settings → **Environment variables**, add:
   - `RESEND_API_KEY` = the key from step 2
   - (optional) `CONTACT_TO_EMAIL` = destination inbox, defaults to `alexjacobsen07@gmail.com`
   - (optional) `CONTACT_FROM` = a verified sender once you've added your own domain in Resend
     (until then it sends from Resend's shared `onboarding@resend.dev`, which works fine but
     shows that address as the sender)
4. Redeploy — Pages Functions pick up env vars on the next deploy.

Locally, `wrangler pages dev` will read a `.dev.vars` file for these env vars if you want
to test the form without hitting Cloudflare — see wrangler docs.

## Admin editor setup (`/admin.html`)

A password-protected page for editing site text (hero, stats, services, about, and each
project's title/subtitle/category/description) without touching code. It saves by
committing the updated `content.json` straight to this GitHub repo via the GitHub API,
which triggers Cloudflare Pages to rebuild and redeploy automatically — no terminal
needed. Video links and cover photos aren't editable there yet; those still need a code
change.

To turn it on:

1. Create a GitHub personal access token the admin page can use to commit changes:
   - GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
   - Generate a new token with the **repo** scope, no expiration (or a long one)
   - Copy it — GitHub only shows it once
2. In the Cloudflare Pages project settings → **Environment variables**, add:
   - `GITHUB_TOKEN` = the token from step 1
   - `ADMIN_PASSWORD` = whatever password you want to type into `/admin.html` to unlock it
3. Redeploy (or just wait for the next push) so the Function picks up the new env vars.

Then visit `https://<your-site>/admin.html`, enter the password, make changes, and click
Save. Give it about a minute to rebuild before checking the live site.

**Keep both of those values secret** — `GITHUB_TOKEN` can push to this repo, and
`ADMIN_PASSWORD` is the only thing gating who can use it. Don't share them or commit them
into any file.

## Deploying

In Cloudflare Pages project settings → **Builds & deployments**:
- Build command: `python3 adobe-source/generate_site.py`
- Build output directory: `/` (repo root)

This reruns the generator (reading `content.json`) on every push, so `index.html` and all
project pages stay in sync with whatever was last edited — whether that was a manual
edit to `content.json` or a save from `/admin.html`.

Connect the repo (or `wrangler pages deploy .`) and Cloudflare handles the rest, including
serving everything in `functions/api/` as serverless endpoints automatically.

## Status

- [x] Contact page + working form backend (needs `RESEND_API_KEY` set, see above)
- [x] Work gallery (15 projects)
- [x] Admin editor for site text (needs `GITHUB_TOKEN` + `ADMIN_PASSWORD` set, see above)
- [ ] Admin editing for video links and cover photos
- [ ] 4 videos still need source files: Level the Playing Field (1), Champs Sports (2)
