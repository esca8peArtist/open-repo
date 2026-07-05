---
title: "Phase 1 Fallback Activation Procedures — Netlify / Vercel / Gist"
project: career-training
phase: "1"
created: 2026-07-04
status: execution-ready
item: "53 (Session 4588)"
cross-reference: "fallback-distribution-protocol.md (full Netlify/Vercel/Gist setup + URL transition protocol + distribution channel sequence)"
trigger: "GitHub Pages unrecoverable after 2 hours of troubleshooting"
---

# Phase 1 Fallback Activation Procedures

**When to use this document**: You have pushed to GitHub, the build has failed or the site is not live, and after working through `GITHUB_PAGES_TROUBLESHOOTING_DECISION_TREE.md` you still do not have a live site. At the 2-hour mark, stop debugging GitHub Pages and activate a fallback.

**Core principle**: A hosting failure is not a launch failure. The curriculum (38 modules, case studies, signup page) is production-ready. The question is only where it is hosted. This document gives you three fallback paths with explicit go/no-go criteria, timing, and setup checklists.

**This is not a last resort — it is a normal contingency.** Netlify in particular is arguably a better hosting platform than GitHub Pages for this use case: it builds faster, supports custom redirects, and the free tier is more flexible.

---

## Decision Gate: When to Activate

| Time since first push attempt | Situation | Decision |
|-------------------------------|-----------|----------|
| < 30 minutes | Build in progress or DNS propagating | Wait |
| 30-60 minutes | Build failing, known error, fix in progress | Continue debugging |
| 60-90 minutes | Build failing, error unclear, troubleshooting stalled | Activate Netlify now |
| > 2 hours | Any continued failure | Activate Netlify; debug GitHub Pages in parallel |
| Any time | You need the site live within the next 2 hours | Activate Netlify immediately |

The 2-hour rule is not arbitrary — it is the point at which the cost of continuing to debug (your time, the delay to launch) exceeds the cost of setting up Netlify (20-30 minutes) and accepting a different URL for now.

---

## Fallback Priority Order

| Priority | Platform | Activation time | Confidence | Best for |
|----------|----------|-----------------|------------|---------|
| 1 (primary) | GitHub Pages | Already in progress | High | Permanent home, SEO, custom domain |
| 2 (first fallback) | Netlify | 20-30 minutes | Very high | Full Jekyll, identical build, CDN |
| 3 (second fallback) | Vercel | 15-25 minutes | High | Fast deploy, zero config |
| 4 (emergency) | GitHub Gist | 5-10 minutes | Medium | Content distribution, no build pipeline |

Activate in order. Do not skip Netlify for Vercel — Netlify runs the identical Jekyll build and produces an indistinguishable site. Vercel requires more build configuration for Jekyll.

---

## Fallback A — Netlify (30 minutes, recommended)

### Pre-activation checklist

Before starting, confirm:
- [ ] Your repository is on GitHub (this is the source Netlify will pull from)
- [ ] You have a browser window open — the entire setup is in the Netlify web UI
- [ ] 30 minutes of uninterrupted time

### Setup steps

**Step A.1 — Create Netlify account (5 minutes)**

Go to [netlify.com](https://netlify.com). Click "Sign up". Select "Continue with GitHub". Authorize Netlify with your GitHub account. This gives Netlify read access to your repositories.

If you already have a Netlify account: log in and skip to Step A.2.

**Step A.2 — Create a new site (5 minutes)**

1. Netlify dashboard > "Add new site" > "Import an existing project"
2. Select "Deploy with GitHub"
3. Authorize the repository access dialog if prompted
4. Find and select your repository from the list

**Step A.3 — Configure build settings (2 minutes)**

On the build configuration page, set:

| Setting | Value |
|---------|-------|
| Base directory | `projects/career-training/docs` |
| Build command | `jekyll build` |
| Publish directory | `projects/career-training/docs/_site` |

Click "Deploy site".

**Step A.4 — Set environment variable (1 minute)**

After the site is created (before or after first build):

1. Netlify dashboard > Site > Site configuration > Environment variables
2. Add variable: `JEKYLL_ENV` = `production`
3. This enables the GA4 analytics guard in `head_custom.html`

If you skip this step, GA4 tracking will not fire on the Netlify site (because the `jekyll.environment == "production"` guard will not be true). Add it before the first build completes if possible.

**Step A.5 — Wait for first build (2-5 minutes)**

Netlify automatically starts a build after you click "Deploy site". Watch the build log in the Netlify dashboard. A successful build shows "Published" with a green indicator.

**Step A.6 — Verify the Netlify URL (5 minutes)**

Netlify assigns a random subdomain like `https://confident-einstein-8f4c2a.netlify.app`. Click it when the build completes. Run the homepage check from `PHASE_1_POST_LAUNCH_VERIFICATION_CHECKLIST.md` Check 1 — confirm the Just the Docs layout loads with sidebar and navigation.

**Step A.7 — Set a clean subdomain (2 minutes, optional but recommended)**

Netlify dashboard > Site configuration > General > Site details > Change site name.

Set it to: `construction-career-training`

Your URL becomes `https://construction-career-training.netlify.app`. This is a clean URL suitable for sharing in LinkedIn posts and outreach emails.

**Step A.8 — Point custom domain to Netlify (if you have one)**

If you own `constructiontrainingpath.com` and want it to point to Netlify instead of GitHub Pages:

1. Netlify dashboard > Domain management > Add custom domain
2. Add `constructiontrainingpath.com`
3. Netlify shows the DNS records to create at your domain registrar
4. At your domain registrar (Namecheap, GoDaddy, Cloudflare, etc.): update the A record and CNAME to the values Netlify shows
5. DNS propagation: 24-48 hours

During DNS propagation: distribute with the Netlify URL (`construction-career-training.netlify.app`). Once DNS propagates, both URLs work.

### Netlify activation time

```
T+0:00   Decision to activate Netlify
T+0:05   Netlify account created (if new) or logged in
T+0:10   Repository imported, build settings configured, deploy started
T+0:12   Environment variable JEKYLL_ENV=production set
T+0:15   First build completes
T+0:17   Netlify URL verified — site is live
T+0:19   Custom subdomain set (construction-career-training.netlify.app)
T+0:25   Launch email drafted (3 sentences + Netlify URL)
T+0:30   Distribution activated
```

### netlify.toml (pre-stage in repository)

Create this file at the repository root to remove the need for manual build configuration in Step A.3:

File path: `/home/awank/dev/SuperClaude_Framework/netlify.toml`

```toml
[build]
  base    = "projects/career-training/docs"
  command = "jekyll build"
  publish = "projects/career-training/docs/_site"

[build.environment]
  JEKYLL_ENV = "production"
  RUBY_VERSION = "3.1"
```

If this file is committed to the repo root before you create the Netlify site, Netlify reads it automatically and Step A.3 requires no manual configuration.

### Verification after Netlify is live

Run `PHASE_1_POST_LAUNCH_VERIFICATION_CHECKLIST.md` Checks 1-7 using the Netlify URL as your `[SITE_URL]`. The experience is identical to GitHub Pages because Netlify runs the same Jekyll build.

---

## Fallback B — Vercel (25 minutes, secondary)

Use Vercel only if Netlify fails or is unavailable. Netlify's Jekyll support is better-documented and more reliably zero-config.

### Pre-activation checklist

- [ ] Netlify was attempted and failed (or you have a specific reason to skip it)
- [ ] 25 minutes available
- [ ] Ruby build may require manual configuration (Vercel does not have a Jekyll preset)

### Setup steps

**Step B.1 — Create Vercel account (3 minutes)**

Go to [vercel.com](https://vercel.com). Sign up with GitHub. Authorize Vercel.

**Step B.2 — Import repository (3 minutes)**

1. Dashboard > "Add New..." > "Project"
2. Import your GitHub repository
3. On the configuration page, set:

| Setting | Value |
|---------|-------|
| Framework Preset | Other |
| Root Directory | `projects/career-training/docs` |
| Build Command | `gem install bundler && bundle install && bundle exec jekyll build` |
| Output Directory | `_site` |
| Install Command | (leave blank) |

**Step B.3 — Set environment variables**

In the project deployment settings, add:
- `JEKYLL_ENV` = `production`

**Step B.4 — Deploy and verify**

Click "Deploy". First build takes 3-8 minutes (Vercel installs Ruby gems at build time, which is slower than Netlify's cached environment).

If the build fails with gem errors, try this alternative build command:
```
gem install github-pages && bundle exec jekyll build
```

Vercel URL format: `https://[your-repo-name].vercel.app`

### Vercel activation time

```
T+0:00   Decision to activate Vercel
T+0:05   Vercel account created
T+0:10   Project imported, build configured, deploy started
T+0:18   Build completes (Vercel first builds are typically faster than Netlify)
T+0:20   Vercel URL verified
T+0:25   Distribution activated
```

---

## Fallback C — GitHub Gist (10 minutes, emergency)

### When to use

Use only when:
- GitHub Pages AND Netlify AND Vercel are all unavailable simultaneously (extremely rare), OR
- You need content accessible within 10 minutes and cannot wait for any build pipeline

This path does not produce a website with navigation. It produces shareable URLs to individual Markdown files rendered by GitHub. The user experience is minimal but the content is intact.

### Setup steps

**For one critical module (5 minutes):**

1. Go to [gist.github.com](https://gist.github.com)
2. Create a new Gist
3. Filename: `construction-career-training-module-01.md`
4. Paste the full content of `projects/career-training/docs/modules/01-foundations-contracts-estimating.md`
5. Click "Create public gist"
6. Share the URL

**For module index (10 minutes):**

1. Repository > Discussions > New discussion
2. Title: "Construction Career Training — 38 Modules Available"
3. Body: list all module files with raw GitHub URLs:
   ```
   https://github.com/[username]/[repo]/blob/master/projects/career-training/docs/modules/01-foundations-contracts-estimating.md
   ```
4. Pin the discussion
5. Share the Discussion URL in distribution channels

### Gist activation time

```
T+0:00   Decision to activate Gist
T+0:02   GitHub Gist opened
T+0:07   Module 01 pasted and published
T+0:10   Discussion created with links to all module files
T+0:12   Direct email to 5-10 individual contacts
T+0:15   LinkedIn post published with GitHub Discussion URL
```

---

## URL Transition Protocol

If you launch on a fallback URL and later recover GitHub Pages (or move to a permanent custom domain), follow this sequence to avoid breaking links shared in early distribution.

**Rule: Do not delete the fallback deployment.** Keep it running with a redirect.

**Step 1 — Add redirect on fallback platform**

On Netlify: create `_redirects` file in `projects/career-training/docs/`:
```
/*  https://constructiontrainingpath.com/:splat  301
```

On Vercel: create `vercel.json` in repo root:
```json
{
  "redirects": [
    {
      "source": "/(.*)",
      "destination": "https://constructiontrainingpath.com/$1",
      "permanent": true
    }
  ]
}
```

**Step 2 — Send one follow-up message**

Email your list: "Quick note: the curriculum has moved to its permanent home at [new URL]. Update your bookmarks. If you have the old link saved, it will redirect automatically."

**Step 3 — Update social posts**

Add a comment to the original LinkedIn post with the new URL. Do not delete the original post — it still drives traffic.

**Step 4 — Keep redirect active for 30 days**

After 30 days, traffic to the old URL should have naturally transitioned. You may then disable the fallback deployment.

**Step 5 — Update internal links**

If you used the Netlify/Vercel URL in any email sequences (Kit welcome emails), update the links in Kit to point to the permanent URL.

---

## Comparison: GitHub Pages vs Netlify vs Vercel

| Criterion | GitHub Pages | Netlify Free | Vercel Hobby |
|-----------|-------------|-------------|-------------|
| First deployment time | 5-10 min (+ DNS) | 20-30 min | 15-25 min |
| Jekyll support | Native | Native | Manual config |
| Custom domain | Free | Free | Free |
| HTTPS | Auto | Auto | Auto |
| CDN | GitHub's CDN | Netlify Edge (faster) | Vercel Edge (fastest) |
| Build minutes/month | Unlimited | 300 min | 6,000 min |
| Bandwidth/month | Soft 100GB | 100GB | 100GB |
| Environment variables | Not needed (GitHub sets JEKYLL_ENV) | Manual (required for GA4) | Manual (required for GA4) |
| Form handling | Via Kit embed | Via Kit embed | Via Kit embed |
| Analytics integration | Via GA4 snippet | Via GA4 snippet | Via GA4 snippet |
| SEO / indexability | Full | Full | Full |

**Bottom line**: All three platforms produce an identical site experience. The only practical difference is setup complexity and build time. Netlify is the correct first fallback.

---

## Full Implementation Detail

This document covers decision gates, timing, and setup checklists. For the complete Netlify, Vercel, and Gist implementation procedures including sub-steps, `netlify.toml` configuration, DNS configuration, distribution channel activation sequence, and URL transition procedures, see `fallback-distribution-protocol.md`.
