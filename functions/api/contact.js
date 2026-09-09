// Cloudflare Pages Function — handles POST /api/contact
// Sends the submitted message via Resend (https://resend.com) to the site owner's inbox.
//
// Required environment variable (set in Cloudflare Pages > Settings > Environment variables):
//   RESEND_API_KEY   — API key from your Resend account
//
// Optional environment variables:
//   CONTACT_TO_EMAIL — destination inbox (defaults to alexjacobsen07@gmail.com)
//   CONTACT_FROM     — verified "from" address (defaults to Resend's shared onboarding@resend.dev,
//                       which works without verifying a domain but is best replaced once a
//                       domain is set up in Resend)

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export async function onRequestPost({ request, env }) {
  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: 'Invalid request body.' }, 400);
  }

  const { name, email, message, company } = body || {};

  // Honeypot: bots fill hidden fields, real users never see this one.
  if (company) {
    return json({ ok: true });
  }

  if (!name || !email || !message) {
    return json({ error: 'Name, email, and message are required.' }, 400);
  }
  if (typeof email !== 'string' || !EMAIL_RE.test(email)) {
    return json({ error: 'Please enter a valid email address.' }, 400);
  }
  if (String(message).length > 5000) {
    return json({ error: 'Message is too long.' }, 400);
  }

  if (!env.RESEND_API_KEY) {
    return json({ error: 'Contact form is not configured yet.' }, 500);
  }

  const toEmail = env.CONTACT_TO_EMAIL || 'alexjacobsen07@gmail.com';
  const fromEmail = env.CONTACT_FROM || 'Portfolio Contact Form <onboarding@resend.dev>';

  const resendRes = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from: fromEmail,
      to: [toEmail],
      reply_to: email,
      subject: `New contact form message from ${name}`,
      text: `Name: ${name}\nEmail: ${email}\n\n${message}`,
    }),
  });

  if (!resendRes.ok) {
    const detail = await resendRes.text().catch(() => '');
    console.error('Resend error:', resendRes.status, detail);
    return json({ error: 'Could not send your message right now. Please try again later.' }, 502);
  }

  return json({ ok: true });
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}
