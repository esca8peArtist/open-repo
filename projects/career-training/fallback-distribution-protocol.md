---
title: "Fallback Distribution Protocol — Construction Career Training Phase 1"
created: 2026-06-28
status: production-ready
applies_to: Alternative deployment if GitHub Pages fails or is delayed
---

# Fallback Distribution Protocol

This document exists for one reason: if GitHub Pages fails to deploy or the domain does not resolve, the curriculum gets distributed anyway. The content is production-ready. A hosting failure is not a launch failure — it is a routing problem with multiple solutions.

Phase 1 does not require a permanent URL. It requires that the content reaches the first wave of users. This protocol gives you three fully operational fallback paths and a rapid-response distribution method that works regardless of which hosting platform is serving the content.

---

## Fallback Priority Order

| Priority | Platform | Activation Time | Best For |
|----------|----------|-----------------|---------|
| 1 (primary) | GitHub Pages | Already configured | Permanent home; SEO; custom domain |
| 2 (first fallback) | Netlify | 20–30 minutes | Full Jekyll build, free HTTPS, instant CDN |
| 3 (second fallback) | Vercel | 15–25 minutes | Fast deploy from GitHub; zero config |
| 4 (emergency) | GitHub Gist / GitHub Discussions | 5–10 minutes | Content distribution without a site |

Activate in order. Once a fallback is live, do not skip to a higher-numbered option — the earlier fallbacks provide a better user experience and are closer to your intended final state.

---

## Platform Comparison

| Criterion | GitHub Pages | Netlify Free | Vercel Hobby | GitHub Gist |
|-----------|-------------|-------------|-------------|-------------|
| Deployment time (first deploy) | 5–10 min | 20–30 min | 15–25 min | 5 min |
| Jekyll support | Native | Native (full) | Via build config | None |
| Custom domain | Yes (free) | Yes (free) | Yes (free) | No |
| HTTPS | Auto (Let's Encrypt) | Auto | Auto | N/A |
| CDN | GitHub's CDN | Netlify Edge (faster) | Vercel Edge | None |
| Build minutes / month (free) | Unlimited | 300 min/month | 6,000 min/month | N/A |
| Bandwidth / month (free) | Soft 100GB limit | 100GB | 100GB | N/A |
| Discoverability | Google indexes it | Google indexes it | Google indexes it | Low |
| User experience | Good | Good | Good | Minimal |
| Cost | Free | Free | Free | Free |

**Verdict:** Netlify is the strongest fallback. It runs the same Jekyll build, supports the same `_config.yml`, and produces an identical site. The URL changes from `github.io` to `netlify.app`, but the content and structure are identical. If Netlify is online, the user experience is indistinguishable from GitHub Pages.

---

## Fallback 2: Netlify (Primary Fallback)

### Activation Procedure

**Estimated time: 20–30 minutes from decision to live site**

**Step 1: Create a Netlify account (if you do not have one)**

Go to `netlify.com` and sign up with your GitHub account. Use "Continue with GitHub" — this pre-authorizes Netlify to access your repositories without additional configuration.

**Step 2: Deploy from GitHub**

1. From the Netlify dashboard, click **"Add new site"** → **"Import an existing project"**
2. Select **"Deploy with GitHub"**
3. Authorize Netlify to access your repository
4. Select your repository from the list
5. Configure the build settings:
   - **Base directory:** `projects/career-training/docs`
   - **Build command:** `jekyll build`
   - **Publish directory:** `projects/career-training/docs/_site`
6. Click **"Deploy site"**

Netlify will start a build immediately. First build takes 2–5 minutes.

**Step 3: Verify the Netlify URL**

Netlify assigns a random subdomain like `https://confident-einstein-8f4c2a.netlify.app`. Click it when the build completes. Run through the testing checklist from `github-pages-deployment-guide.md` Part 4.

**Step 4: Set a custom subdomain (optional, 2 minutes)**

In Netlify dashboard → Site settings → General → Site details → Change site name. Set it to `construction-career-training` → your URL becomes `https://construction-career-training.netlify.app`. This is a cleaner URL to share in outreach emails.

**Step 5: Point your custom domain to Netlify (if GitHub Pages domain is blocked)**

If you have a registered domain that was previously pointed at GitHub Pages:
1. Netlify dashboard → Domain management → Add custom domain
2. Update your DNS provider: Change the A records to point to Netlify's load balancer IPs (shown in the Netlify dashboard)
3. DNS propagation: 24–48 hours (same as GitHub Pages)
4. HTTPS provisions automatically after DNS propagates

**Ongoing deployment:** Every push to your GitHub `master` branch automatically triggers a Netlify rebuild. No manual steps after initial setup.

**Netlify `netlify.toml` config (place in repository root for automatic configuration):**

```toml
[build]
  base    = "projects/career-training/docs"
  command = "jekyll build"
  publish = "projects/career-training/docs/_site"

[build.environment]
  JEKYLL_ENV = "production"
  RUBY_VERSION = "3.1"
```

Create this file at the root of your repository and commit it before the first Netlify deploy. Netlify will read it automatically and skip the manual build configuration in Step 2.

---

## Fallback 3: Vercel (Secondary Fallback)

### Activation Procedure

**Estimated time: 15–25 minutes**

Vercel is primarily a Next.js/React platform but handles static site generators including Jekyll with minimal configuration.

**Step 1: Create a Vercel account**

Go to `vercel.com` → sign up with GitHub.

**Step 2: Import repository**

1. Dashboard → **"Add New..."** → **"Project"**
2. Import your GitHub repository
3. Configure build settings:
   - **Framework Preset:** Select "Other"
   - **Root Directory:** `projects/career-training/docs`
   - **Build Command:** `gem install bundler && bundle install && bundle exec jekyll build`
   - **Output Directory:** `_site`
   - **Install Command:** (leave blank)
4. Click **"Deploy"**

**Step 3: Set environment variable for Jekyll**

In Vercel → Project settings → Environment Variables, add:
```
JEKYLL_ENV = production
```

**Note on Vercel and Jekyll:** Vercel's build environment includes Ruby but not the full GitHub Pages gem set. If the build fails with gem errors, switch the build command to:

```bash
gem install github-pages && bundle exec jekyll build
```

Alternatively, pre-build the site locally and deploy only the `_site` directory:

```bash
cd projects/career-training/docs
bundle exec jekyll build
# Then commit the _site directory and point Vercel's output to it
```

**Vercel URL format:** `https://your-repo-name.vercel.app`

Custom domain assignment works the same as Netlify: add domain in project settings, update DNS.

---

## Fallback 4: GitHub Gist / GitHub Discussions (Emergency)

### When to use this fallback

Use this option only when:
- GitHub Pages is down (GitHub infrastructure outage)
- Both Netlify and Vercel are down (extremely unlikely simultaneously)
- You need to get content to users within 5 minutes with no build pipeline

This option does not produce a website. It produces shareable URLs to raw Markdown content. The user experience is minimal (GitHub-rendered Markdown), but the content is intact and accessible.

### Activation Procedure

**For a single critical module (5 minutes):**

1. Go to `gist.github.com`
2. Create a new Gist
3. Filename: `construction-career-training-module-01.md`
4. Paste the content of the module
5. Click **"Create public gist"**
6. Share the URL directly in outreach emails

GitHub renders Gist Markdown with heading styles, code formatting, and tables. It is readable, just not themed.

**For multiple modules (10–15 minutes):**

1. Create a GitHub Discussion in your repository: Repository → Discussions → New discussion
2. Select "Announcements" category
3. Title: "Phase 1 Launch: Construction Career Training — 33 Modules Available"
4. Body: Include links to all 33 module files using the raw GitHub content URLs:
   ```
   https://github.com/yourusername/repo/blob/master/projects/career-training/01-foundations-contracts-estimating.md
   ```
5. Pin the Discussion to the repository
6. Share the Discussion URL in distribution outreach

---

## Rapid-Response Distribution Protocol

When a fallback is activated, distribution does not wait for the permanent URL to stabilize. Use the fallback URL immediately. If the URL changes later (e.g., Netlify URL replaced by final custom domain), send a brief follow-up message to your list.

### Distribution channel activation sequence

Activate these channels in order based on speed-to-audience:

**Within 30 minutes of fallback URL being live:**

1. **Direct email to your list (highest value)**
   - Subject: `Construction Career Training is live — 33 modules, 3 paths, free`
   - Body: State the URL, the three learning paths, and a direct link to the Quick Start page
   - If you do not yet have an email platform configured: use your personal email and BCC your contacts
   - Minimum viable email: 3 sentences + URL. Do not wait to write a long email.

2. **LinkedIn post**
   - Post the URL with 2–3 sentences describing the curriculum
   - Do not draft a long article for Phase 1 launch — a short post with the URL goes live in 2 minutes
   - Example: "Just launched: 33 modules of construction career training across three paths — Industrial GC, Residential GC, and Specialty Sub to PM. All free. Link in comments: [URL]"

3. **Reddit cross-post**
   - r/Construction: Post title "Free construction training curriculum — 33 modules, all career stages"
   - r/civilengineering (if applicable)
   - Keep it factual; no marketing language; Reddit communities downvote promotional posts
   - Lead with what it is, not why it is great

**Within 2 hours:**

4. **LinkedIn Pulse article (if you have time)**
   - Write a 400-word article: "Why I Built a Free Construction Curriculum" or "From Field to PM: The Training Path I Wish I Had"
   - Link to the site in the article body and closing CTA
   - LinkedIn Pulse articles receive additional distribution from LinkedIn's algorithm beyond your followers

5. **Direct outreach to 5–10 individual contacts**
   - Email or LinkedIn message to specific people who would find this valuable
   - Construction instructors, former colleagues, professional associations you know
   - Personalized 2-sentence message: "I know you teach [X] — wanted to share this before I announce it broadly. Here's the URL."

**Within 24 hours:**

6. **GitHub Discussions announcement in the repository**
   - Even if the site is live, create a pinned Discussion linking to it
   - This surfaces the curriculum to anyone who finds the GitHub repository

7. **Update LinkedIn profile**
   - Add the site URL to your LinkedIn profile "Featured" section
   - This makes it permanently visible on your profile without requiring active posting

8. **Google Search Console submission**
   - Submit the sitemap URL to Google so organic search indexing begins
   - URL: `https://yoursite.com/sitemap.xml`

---

## 30-Minute Activation Timelines

### Timeline A: Netlify Fallback

```
T+0:00  Decision made to use Netlify
T+0:05  Netlify account created with GitHub OAuth
T+0:10  Repository imported, build settings configured, deploy started
T+0:15  First build completes (or in progress)
T+0:20  Netlify URL verified — site is live
T+0:22  Custom subdomain set (construction-career-training.netlify.app)
T+0:25  Launch email drafted (3 sentences + URL)
T+0:30  Email sent, LinkedIn post published
```

### Timeline B: Vercel Fallback

```
T+0:00  Decision made to use Vercel
T+0:05  Vercel account created
T+0:10  Project imported, build configured
T+0:18  Build completes (Vercel builds are typically faster than Netlify for first deploy)
T+0:20  Vercel URL verified
T+0:25  Launch email drafted and sent
T+0:30  LinkedIn post published
```

### Timeline C: Gist Emergency (no build pipeline)

```
T+0:00  GitHub / Netlify / Vercel all unavailable
T+0:02  GitHub Gist opened
T+0:07  Module 01 pasted and published (first shareable module)
T+0:10  GitHub Discussion created with links to all module files in repo
T+0:12  Direct email sent to 5–10 individual contacts with GitHub Discussion URL
T+0:15  LinkedIn post: "Curriculum available on GitHub while site deploys — here's the link"
```

---

## URL Transition Protocol

If you launch on a fallback URL and the primary GitHub Pages URL later becomes available, follow this sequence to transition without losing users:

1. **Do not delete the fallback deployment.** Keep Netlify or Vercel running.

2. **Add a redirect on the fallback platform** pointing to the permanent URL:
   - Netlify: Add `_redirects` file in `/docs/`:
     ```
     /*  https://yourpermanentdomain.com/:splat  301
     ```
   - Vercel: Add `vercel.json` in the repo root:
     ```json
     {
       "redirects": [
         { "source": "/(.*)", "destination": "https://yourpermanentdomain.com/$1", "permanent": true }
       ]
     }
     ```

3. **Send one follow-up email** to your list: "Quick note: the curriculum has moved to its permanent home at [new URL]. Update your bookmarks."

4. **Update the LinkedIn post** with a comment containing the new URL.

5. After 30 days, disable the fallback deployment.

---

## Decision Rules for Rollback vs. Staying on Fallback

| Situation | Decision |
|-----------|----------|
| GitHub Pages build error, Netlify works | Use Netlify indefinitely; GitHub Pages is not required |
| GitHub Pages deploys but domain DNS is still propagating | Use `github.io` URL for distribution while waiting for custom domain |
| Both GitHub Pages and Netlify fail to build | Check if the error is in `/docs/_config.yml` — fix it, both will work |
| Site is live on fallback but GitHub Pages is now fixed | Redirect fallback to GitHub Pages; do not break existing links |
| Fallback URL shared in email, permanent URL now live | Add redirect; send one follow-up; keep fallback running for 30 days |
| Three consecutive build failures across all platforms | Content issue, not hosting issue — check YAML and Gemfile, then retry |
