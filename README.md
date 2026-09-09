# alex-portfolio

Static site, deployed on Cloudflare Pages. No build step — plain HTML/CSS, plus one
Cloudflare Pages Function for the contact form.

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

## Deploying

This repo has no build step, so in Cloudflare Pages:
- Build command: (leave blank)
- Build output directory: `/` (repo root)

Connect the repo (or `wrangler pages deploy .`) and Cloudflare handles the rest, including
serving `functions/api/contact.js` as a serverless endpoint automatically.

## Status

- [x] Contact page + working form backend
- [ ] Work gallery (13 projects, pending video links from Adobe Portfolio project pages)
- [ ] Custom uploader/admin tool for editing projects post-launch
