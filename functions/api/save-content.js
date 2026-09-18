// Cloudflare Pages Function — handles POST /api/save-content
// Lets the password-protected admin page (/admin.html) save edits to
// content.json by committing the change directly to GitHub. That push
// triggers Cloudflare Pages' existing auto-deploy (which reruns
// adobe-source/generate_site.py as the build step), so the live site
// updates automatically — no terminal or git commands needed.
//
// Required environment variables (set in Cloudflare Pages > Settings > Environment variables):
//   ADMIN_PASSWORD — the password required to save changes from /admin.html
//   GITHUB_TOKEN   — a GitHub personal access token with "repo" scope (or, for a
//                    fine-grained token, "Contents: Read and write" on this repo)
//
// Optional environment variables:
//   GITHUB_REPO    — "owner/repo" (defaults to alexjacobsen07-debug/portfolio)
//   GITHUB_BRANCH  — branch to commit to (defaults to main)

const DEFAULT_REPO = 'alexjacobsen07-debug/portfolio';
const DEFAULT_BRANCH = 'main';
const FILE_PATH = 'content.json';

export async function onRequestPost({ request, env }) {
  if (!env.ADMIN_PASSWORD || !env.GITHUB_TOKEN) {
    return json({ error: 'Admin editing is not configured yet. Set ADMIN_PASSWORD and GITHUB_TOKEN in Cloudflare Pages settings.' }, 500);
  }

  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: 'Invalid request body.' }, 400);
  }

  const { password, content } = body || {};

  if (typeof password !== 'string' || password !== env.ADMIN_PASSWORD) {
    return json({ error: 'Incorrect password.' }, 401);
  }

  if (!content || typeof content !== 'object') {
    return json({ error: 'Missing content.' }, 400);
  }

  const repo = env.GITHUB_REPO || DEFAULT_REPO;
  const branch = env.GITHUB_BRANCH || DEFAULT_BRANCH;
  const apiUrl = `https://api.github.com/repos/${repo}/contents/${FILE_PATH}`;
  const headers = {
    Authorization: `Bearer ${env.GITHUB_TOKEN}`,
    'User-Agent': 'alex-portfolio-admin',
    Accept: 'application/vnd.github+json',
  };

  // GitHub's update API requires the current file's SHA.
  let sha;
  try {
    const getRes = await fetch(`${apiUrl}?ref=${branch}`, { headers });
    if (!getRes.ok) {
      const err = await getRes.text();
      return json({ error: `Could not read current content.json from GitHub: ${err}` }, 502);
    }
    const current = await getRes.json();
    sha = current.sha;
  } catch (err) {
    return json({ error: `Could not reach GitHub: ${err.message}` }, 502);
  }

  const newContentBase64 = btoa(unescape(encodeURIComponent(JSON.stringify(content, null, 2) + '\n')));

  try {
    const putRes = await fetch(apiUrl, {
      method: 'PUT',
      headers: { ...headers, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        message: 'Update site content via admin page',
        content: newContentBase64,
        sha,
        branch,
      }),
    });

    if (!putRes.ok) {
      const err = await putRes.text();
      return json({ error: `GitHub rejected the update: ${err}` }, 502);
    }
  } catch (err) {
    return json({ error: `Could not reach GitHub: ${err.message}` }, 502);
  }

  return json({ ok: true, message: 'Saved. Cloudflare Pages will rebuild and deploy in about a minute.' });
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
