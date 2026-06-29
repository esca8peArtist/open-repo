---
title: "GitHub Pages Rollback Procedures — 3 Fallback Options"
project: career-training
phase: "1"
created: 2026-06-29
status: execution-ready
trigger: "Activate if GitHub Pages deployment fails after 2 hours of troubleshooting"
---

# GitHub Pages Rollback Procedures

**When to activate**: GitHub Pages deployment fails AND you have worked through the full `GITHUB_ACTIONS_TROUBLESHOOTING_FLOWCHART.md` (all 6 checks) without resolution. Or: you need the site live within 2-4 hours and cannot afford to wait for GitHub support.

**This is not a failure**. GitHub Pages is a convenient default for Jekyll sites — not the only option. Netlify and Vercel both support Jekyll natively and in many ways provide a faster, more reliable deployment pipeline. The content (all 38 modules, case studies, signup page) does not change. Only where it is hosted changes.

**Three options**:

| Option | Platform | Time | Confidence | Complexity |
|--------|----------|------|------------|------------|
| A | Netlify | 30 min | Very high | Low |
| B | Vercel | 25 min | High | Medium |
| C | GitHub Gist (temporary) | 10 min | Medium | Low |

**Recommendation**: Option A (Netlify) if you have 30 minutes. Option C if you need something up in 10 minutes and can migrate properly later.

---

## Option A — Netlify Deployment (30 minutes, recommended)

**Why Netlify over GitHub Pages**:
- Netlify runs Jekyll builds on its own infrastructure — completely independent of GitHub Pages' build environment
- Netlify supports all standard Jekyll plugins including `jekyll-remote-theme`
- Build logs are clearer and easier to read
- Deploy previews for every push (see exactly what each commit looks like before it goes live)
- Custom domain setup is identical to GitHub Pages

**Confidence level**: Very high. Netlify's Jekyll support is mature. The same `_config.yml` and `_layouts/` that worked locally will work on Netlify.

---

### Step A.1 — Create a Netlify account (5 minutes)

1. Go to [netlify.com](https://netlify.com)
2. Click "Sign up"
3. Choose "Sign up with GitHub" — this authorizes Netlify to access your repositories
4. Complete OAuth flow in GitHub (authorize Netlify)
5. You are now in the Netlify dashboard

---

### Step A.2 — Connect your repository (5 minutes)

1. In Netlify dashboard, click **"Add new site"** > **"Import an existing project"**
2. Click **"Deploy with GitHub"**
3. If prompted to install Netlify GitHub App: install it for your account (or just the career-training repository)
4. A list of your repositories appears — select your career-training repository
5. You are now on the "Configure your site" page

---

### Step A.3 — Configure the build settings (5 minutes)

Netlify auto-detects Jekyll in most cases. Verify these settings:

- **Branch to deploy**: `main` (or `master` — whatever your primary branch is)
- **Base directory**: `projects/career-training/docs` (the path from repo root to the Jekyll site — this is critical)
  - If your repo root IS the Jekyll site (i.e., `_config.yml` is at the repo root), leave this blank
  - For this project structure: `projects/career-training/docs`
- **Build command**: `jekyll build` (Netlify may auto-fill this; if not, type it)
- **Publish directory**: `projects/career-training/docs/_site` (where Jekyll writes built files)

If Netlify auto-detected different values, override them with the above.

**Do not click Deploy yet** — complete Step A.4 first.

---

### Step A.4 — Set environment variables (2 minutes)

Click **"Show advanced"** to expand environment variable settings. Add:

| Key | Value |
|-----|-------|
| `JEKYLL_ENV` | `production` |

This activates the `jekyll.environment == "production"` guard in `head_custom.html`, so GA4 fires correctly on the live Netlify site.

---

### Step A.5 — Deploy (10 minutes including build wait)

1. Click **"Deploy site"**
2. Netlify starts the build immediately
3. Click **"Deploying your site"** to watch the live build log
4. The build log shows Jekyll output — look for `done in X.XXX seconds` at the end
5. If the build succeeds: Netlify assigns a temporary URL like `https://random-name-12345.netlify.app`
6. Visit the temporary URL to confirm the site looks correct

**If the Netlify build fails**: The error message in Netlify's log is the same Jekyll error you would see anywhere. Apply the same fixes from `GITHUB_PAGES_REMEDIATION_RUNBOOK.md`.

---

### Step A.6 — Connect custom domain (5 minutes)

If you have a custom domain (`constructiontrainingpath.com`):

1. In Netlify dashboard for your site, click **"Domain settings"** > **"Add a domain"**
2. Enter your domain: `constructiontrainingpath.com`
3. Netlify shows you the DNS records to set
4. Log in to your domain registrar (GoDaddy, Namecheap, Google Domains, etc.)
5. In your DNS settings, add or update:
   - If using Netlify nameservers: change your NS records to Netlify's nameservers (Netlify provides these)
   - If keeping your existing DNS provider: add a CNAME record pointing `www` to your Netlify site URL, and an ALIAS/ANAME record for the apex domain
6. DNS propagation takes 5-60 minutes

If you previously had GitHub Pages DNS configured (a CNAME pointing to `yourusername.github.io`), delete or update that record.

---

### Step A.7 — Verify SSL certificate (automatic)

Netlify automatically provisions a free SSL certificate via Let's Encrypt within 5-10 minutes of DNS propagating. You will see a green "Netlify DNS" badge and `https://` in the site URL when complete.

**Total time**: 25-35 minutes including build and DNS propagation.

---

## Option B — Vercel Deployment (25 minutes)

**Why Vercel over GitHub Pages**:
- Vercel supports Jekyll via static site output
- Fast global CDN, good performance scores
- Generous free tier
- CI/CD pipeline is faster than GitHub Pages

**Vs. Netlify**: Vercel's native Jekyll support is slightly more involved than Netlify's because Vercel is primarily optimised for Node-based frameworks. It works, but Netlify is better for pure Jekyll. Use Vercel if you have an existing Vercel account or preference.

---

### Step B.1 — Create a Vercel account (3 minutes)

1. Go to [vercel.com](https://vercel.com)
2. Click "Sign Up" > "Continue with GitHub"
3. Authorize Vercel to access your GitHub account
4. Select "Hobby" plan (free)

---

### Step B.2 — Import your project (5 minutes)

1. In Vercel dashboard, click **"Add New..."** > **"Project"**
2. Click **"Import"** next to your career-training repository
3. If you do not see your repository: click "Adjust GitHub App Permissions" and grant Vercel access to the repository

---

### Step B.3 — Configure build settings for Jekyll (10 minutes)

Vercel does not auto-detect Jekyll the same way Netlify does. You need to configure manually.

- **Framework Preset**: Select **"Other"** (not Jekyll specifically — Jekyll is not a first-class preset)
- **Root Directory**: `projects/career-training/docs`
- **Build Command**: `gem install bundler jekyll jekyll-remote-theme jekyll-feed jekyll-sitemap jekyll-seo-tag && jekyll build`
- **Output Directory**: `_site`

This build command installs gems directly without a Gemfile, which is the most reliable approach for Vercel's environment.

**Alternative with Gemfile**: If you have a `docs/Gemfile`:
- Build Command: `bundle install && bundle exec jekyll build`
- Output Directory: `_site`

---

### Step B.4 — Set environment variable

Under "Environment Variables" in the project settings:
- Key: `JEKYLL_ENV`
- Value: `production`

---

### Step B.5 — Deploy and verify (5 minutes)

1. Click **"Deploy"**
2. Watch the build log in Vercel dashboard
3. On success: Vercel assigns a URL like `https://career-training-abc123.vercel.app`
4. Visit the URL and confirm the site renders correctly

---

### Step B.6 — Add custom domain

In Vercel project dashboard:
1. Click **"Settings"** > **"Domains"**
2. Add your domain name
3. Vercel shows DNS configuration instructions
4. Follow the same DNS update process as Option A, Step A.6

**Note**: Vercel assigns SSL automatically, same as Netlify.

---

## Option C — Temporary Gist Publishing (10 minutes, stopgap only)

**Use case**: You need the content accessible within 10 minutes. The URL will not be pretty. This is not a permanent solution — it is a "content is up, fix hosting later" approach for urgent launches or demos.

**Limitation**: GitHub Gist does not render Jekyll. You are publishing raw Markdown files. They will display as Markdown (readable but unstyled) via GitHub's default Gist renderer. Navigation, search, and the full site layout will not work.

**Confidence**: Medium — content is accessible, not the polished site.

---

### Step C.1 — Build the site locally

```bash
cd projects/career-training/docs
bundle exec jekyll build
```

This generates the `_site/` directory with fully rendered HTML files.

If bundle is not installed:
```bash
gem install bundler jekyll jekyll-remote-theme
bundle exec jekyll build
```

---

### Step C.2 — Create a GitHub Gist with the built HTML

Option C.2a — Single file (index only):

1. Go to [gist.github.com](https://gist.github.com)
2. Filename: `index.html`
3. Content: paste contents of `projects/career-training/docs/_site/index.html`
4. Set to Public
5. Click "Create public gist"
6. Share the raw URL: `https://gist.githubusercontent.com/USERNAME/GISTID/raw/index.html`

This only exposes the homepage. Individual module pages require separate gists.

Option C.2b — GitHub Release with `_site.zip`:

```bash
cd projects/career-training/docs
bundle exec jekyll build
zip -r _site.zip _site/
gh release create v1.0-pages-emergency \
  --title "Career Training Site — Emergency Release" \
  --notes "Temporary release while GitHub Pages build is resolved." \
  _site.zip
```

Users download `_site.zip` and open `index.html` in a browser locally. Not ideal for public access but preserves the full styled experience.

---

### Step C.3 — Communicate the temporary URL

If using Option C for a time-sensitive launch: communicate to your initial audience (e.g., email list, social) that the site is temporarily at `[gist URL]` and will move to `constructiontrainingpath.com` within 24-48 hours.

**Do not do this**: Do not publish the Gist URL widely. It is not the permanent home.

---

### Step C.4 — Migrate to Netlify when ready

Follow Option A to set up Netlify properly. Once Netlify is live on your custom domain, stop sharing the Gist URL.

---

## Recommendation Summary

**You have 30 minutes and want the real site**: Choose Option A (Netlify).

**You have 20 minutes and already use Vercel**: Choose Option B.

**You need something up in 10 minutes for a specific meeting or deadline**: Choose Option C temporarily, then Option A within 24 hours.

**You want to keep trying GitHub Pages**: Continue with `GITHUB_ACTIONS_TROUBLESHOOTING_FLOWCHART.md` and open a GitHub support ticket in parallel. Wait for the support response while Netlify/Vercel hosts the live content.

---

## Reverting from Netlify/Vercel back to GitHub Pages (optional, later)

If GitHub Pages eventually starts working and you want to consolidate:

1. Confirm GitHub Pages is deploying correctly (green build, site live)
2. Update DNS: point your domain from Netlify/Vercel back to GitHub Pages
   - For GitHub Pages: CNAME pointing to `yourusername.github.io` (for `www`), A records for apex pointing to GitHub Pages IPs (see [GitHub docs](https://docs.github.com/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site))
3. Wait for DNS propagation (5-60 minutes)
4. Verify the site loads from the GitHub Pages URL
5. Archive the Netlify/Vercel project (do not delete — keep as fallback)

Keeping the Netlify/Vercel project archived costs nothing on the free tier and gives you a one-click fallback if GitHub Pages degrades again.
