# GitHub Pages Deployment Plan: Construction Career Training Curriculum

**Document Version:** 1.0  
**Created:** June 27, 2026  
**Target Audience:** Instructors, construction professionals, training organizations  
**Content Scope:** 33 instructional modules, 150 case studies, three complete learning paths  
**Estimated Content Volume:** ~457,000 words

---

## SECTION 1: GitHub PAGES SETUP STEPS

### 1.1 Prerequisites

Before beginning deployment, confirm you have:

- **GitHub repository access** with admin permissions (required to enable Pages and configure custom domain)
- **Domain name** (optional but recommended):
  - Recommended: `constructiontrainingpath.com` or `gccertification.training` (construction industry focus)
  - Alternative: Use GitHub's free `github.com/[org]/[repo].github.io` subdomain if custom domain unavailable
- **Git command-line interface** installed locally
- **Text editor or IDE** for file organization (VS Code recommended)
- **Basic Markdown knowledge** (this curriculum is already in Markdown, minimal conversion needed)

### 1.2 GitHub Pages Configuration

#### Step 1: Enable GitHub Pages in Repository Settings

1. Navigate to your repository on GitHub
2. Go to **Settings** → **Pages** (left sidebar under "Code and automation")
3. Under "Source," select:
   - Branch: `main` (or your primary branch)
   - Folder: `/docs` or `/` (root)
   - **Recommendation:** Use `/docs` folder for cleaner repository structure
4. Click **Save**
5. GitHub will generate your site URL (e.g., `https://[org].github.io/career-training/`)

#### Step 2: Configure Custom Domain (Optional but Recommended)

1. In **Settings** → **Pages**, scroll to "Custom domain"
2. Enter your domain (e.g., `constructiontrainingpath.com`)
3. Click **Save**
4. **Update DNS provider** (GoDaddy, Namecheap, etc.):
   - Add `CNAME` record: Point `constructiontrainingpath.com` to `[org].github.io`
   - Or add `A` records to GitHub's IP addresses (see [GitHub's DNS config guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site))
5. **Enable HTTPS** (recommended):
   - GitHub will automatically provision an SSL/TLS certificate
   - Check **Enforce HTTPS** in Pages settings once certificate is ready (~5 minutes)

### 1.3 Site Structure and Organization

#### Recommended Directory Layout

```
/docs/
├── _config.yml                    # Jekyll configuration
├── index.md                       # Homepage (site root)
├── navigation/
│   ├── quick-start.md            # "Start here" guide
│   ├── industrial-path.md         # Path 1: Industrial GC
│   ├── residential-path.md        # Path 2: Residential GC
│   ├── specialty-path.md          # Path 3: Specialty Sub → PM
│   ├── module-quick-reference.md  # All modules by discipline
│   └── faq.md                     # Frequently asked questions
├── modules/
│   ├── 01-foundations.md
│   ├── 02-field-execution.md
│   └── ... (modules 03-33)
├── case-studies/
│   ├── scenarios.md               # All scenarios with answers
│   └── by-module/                 # Organized by module
│       ├── scenarios-module-01.md
│       └── ... (organized by topic)
├── resources/
│   ├── templates/                 # Subcontract templates, checklists
│   ├── forms/                     # Lien waivers, RFI templates
│   ├── glossary.md                # Construction terminology
│   ├── reading-list.md            # Recommended additional resources
│   └── california-regulations.md  # CSLB, OSHA, permitting links
├── instructor-guide/
│   ├── how-to-teach.md           # Teaching methodology
│   ├── classroom-setup.md         # Setting up group training
│   ├── assessment-rubrics.md      # Grading criteria
│   └── sample-syllabus.md         # 16-week course outline
├── about/
│   ├── contact.md                 # Contact and support
│   ├── contributors.md            # Author attribution
│   └── update-log.md              # Curriculum change log
└── assets/
    ├── css/                       # Custom CSS for branding
    ├── images/                    # Construction diagrams, flowcharts
    └── downloads/                 # PDF exports, worksheets
```

### 1.4 Content Preparation for Web Delivery

#### Step 1: Organize Module Files

1. **Copy all 33 modules** into `/docs/modules/` with descriptive filenames (already in project)
2. **Create module index pages** that link to the three learning paths
3. **Add metadata headers** to each module file for Jekyll processing:

```markdown
---
title: "Module 01 — Industrial GC Foundations"
path: "Industrial GC"
hours: 7
difficulty: "Intermediate"
prerequisites: "None"
next_module: "02-field-execution"
---
```

#### Step 2: Create Homepage and Navigation

**Homepage (`/docs/index.md`):**
- Hero section: "Choose your construction career path"
- Three large buttons/cards linking to paths
- Quick statistics: "33 modules, 150 case studies, ~457,000 words"
- Start now CTA

**Quick Start Guide (`/docs/navigation/quick-start.md`):**
- "New here?" section
- Three career path summaries (100-word elevator pitch each)
- Decision tree: "Which path is right for me?"
- Sample module preview

#### Step 3: Prepare Case Studies

1. **Export case-study-workbook.md** into `/docs/case-studies/scenarios.md`
2. **Create module-indexed versions** in `/docs/case-studies/by-module/`:
   - Example: `scenarios-module-01.md` contains only scenarios relevant to Module 01
3. **Add answer key navigation**:
   - Include links to module content for context
   - Worked answers should be collapsible (`<details>`) for web reading

#### Step 4: Create Static Resources

**Glossary (`/docs/resources/glossary.md`):**
- Construction terminology indexed alphabetically
- Cross-references to modules where terms are explained
- California-specific terms flagged

**Templates and Forms (`/docs/resources/templates/`):**
- Subcontract template (fillable)
- Lien waiver forms (conditional and unconditional)
- Change order template
- Inspection checklist
- Site safety plan outline

**California Regulations (`/docs/resources/california-regulations.md`):**
- Links to CSLB website, license requirements
- Cal/OSHA standards by topic
- Title 24 summary and effective dates
- CPUC NEM tariff information
- County permitting office locator

### 1.5 Build Tool Recommendation: Jekyll vs. Bare GitHub Pages

#### Option A: Jekyll (Recommended for Rich Features)

**What Jekyll adds:**
- Automatic site generation from Markdown
- Navigation menu templates and breadcrumbs
- Search functionality (using Lunr.js or Algolia)
- Collapsible "more info" sections
- Mobile-responsive layout with minimal CSS
- Automatic table of contents for long modules

**Setup (5 minutes):**

1. Create `/docs/_config.yml`:
```yaml
title: Construction Career Training Curriculum
description: Production-ready training for GCs, PMs, and specialty contractors
theme: jekyll-theme-minimal  # or minimal-mistakes, just-the-docs
markdown: kramdown
plugins:
  - jekyll-sitemap
  - jekyll-feed

baseurl: "/career-training"  # if not using custom domain
url: "https://constructiontrainingpath.com"
```

2. Add navigation layout in `/_layouts/default.html`:
   - Sidebar with path selection
   - Module table of contents
   - Back/next buttons

3. Deploy: Push to `main` → GitHub automatically builds and deploys

**Timeline:** Jekyll setup = 1–2 hours; automated after that

#### Option B: Bare GitHub Pages (Minimal Setup)

**Use this if:**
- You want zero build complexity
- GitHub's automatic Markdown rendering is sufficient
- No custom search or navigation needed

**Limitations:**
- No automatic table of contents
- Navigation requires manual HTML links
- Mobile responsiveness depends on browser defaults
- Limited customization

**Recommendation:** Use Jekyll. The 2-hour setup investment saves 10+ hours of manual navigation and search implementation, and provides a professional user experience.

### 1.6 Testing Locally Before Deployment

#### Option A: Test with Jekyll Locally

1. **Install Jekyll** (requires Ruby):
   ```bash
   gem install bundler jekyll
   ```

2. **Create Gemfile** in `/docs/`:
   ```
   source "https://rubygems.org"
   gem "jekyll"
   gem "jekyll-theme-minimal"
   ```

3. **Run local server**:
   ```bash
   cd docs/
   bundle exec jekyll serve
   ```

4. **Test at:** `http://localhost:4000/career-training/`
   - Click through all three learning paths
   - Verify all module links work
   - Test case-study navigation
   - Check mobile responsiveness (Chrome DevTools)

5. **Verify:**
   - [ ] All 33 modules load without 404 errors
   - [ ] All cross-module links resolve
   - [ ] Homepage navigation works
   - [ ] Case studies display correctly
   - [ ] Mobile layout is readable
   - [ ] Load time < 2 seconds per page

#### Option B: Test in GitHub Pages Staging

1. Create a test branch: `git checkout -b gh-pages-staging`
2. Enable Pages on this branch (Settings → Pages)
3. Test at GitHub's staging URL for 1-2 days
4. Merge to main when ready for production

### 1.7 Rollout Checklist

**Week 1: Setup and Testing**

- [ ] GitHub repository access confirmed
- [ ] Domain registered (if custom domain planned)
- [ ] Pages enabled in repository settings
- [ ] DNS configured for custom domain (if applicable)
- [ ] Directory structure created (`/docs/`)
- [ ] Jekyll `_config.yml` configured
- [ ] Homepage and navigation pages created
- [ ] All 33 modules copied to `/docs/modules/`
- [ ] Case studies organized and formatted
- [ ] Static resources (glossary, templates) created
- [ ] Local Jekyll build tested (no errors)
- [ ] All links tested (0 dead links)
- [ ] Mobile responsiveness verified

**Week 2: Pre-Launch Validation**

- [ ] Accessibility audit (WAVE tool, color contrast checker)
- [ ] SEO metadata added (meta descriptions, keywords)
- [ ] Page load performance optimized (images compressed)
- [ ] Analytics configured (Google Analytics snippet added)
- [ ] Email signup form integrated (ConvertKit, Mailchimp)
- [ ] Custom domain pointing correctly to GitHub Pages
- [ ] HTTPS certificate provisioned and active
- [ ] Instructor guide published to `/docs/instructor-guide/`
- [ ] Sample syllabus and teaching materials available
- [ ] FAQ page completed

**Week 3: Final Pre-Launch Review**

- [ ] Content audit: All module metadata correct (hours, prerequisites)
- [ ] Legal review: Terms of use, attribution, licensing clearly stated
- [ ] Cross-links verified (module → module, module → case study)
- [ ] Print CSS tested (modules should print to single-document PDF)
- [ ] Backup created (GitHub release tag)
- [ ] Staging site reviewed by 2–3 beta users
- [ ] Beta feedback incorporated

**Launch Day (Week 4)**

- [ ] Final production deployment
- [ ] Announcement email sent to email list
- [ ] Social media posts scheduled
- [ ] Partner notifications sent
- [ ] Launch checklist marked complete

---

## SECTION 2: CONTENT DISTRIBUTION CHANNEL ACTIVATION

### 2.1 Email List Strategy

#### Building the List (Pre-Launch)

**Target segments:**
- Construction industry professionals (GCs, project managers, supervisors)
- Specialty subcontractors (electricians, plumbers, framers, HVAC)
- Career changers exploring construction management
- Instructors and training directors

**Lead magnets (free incentives):**
1. **"7-Day Quick Start Guide"** — Email sequence with daily module preview + free case study
2. **"California GC Licensing Checklist"** — Free PDF with DIR links, bond requirements, fee schedule
3. **"Reading Construction Drawings Cheat Sheet"** — One-page visual guide (AIA standards, sheet numbering)
4. **"Case Study Sampler"** — 5 selected scenarios with worked answers (representative of curriculum)

**Acquisition channels:**
- Lead magnet opt-in box on homepage
- Exit-intent popup: "Leave? Get a free case study first"
- Bottom-of-module CTA: "Track your progress — sign up for email reminders"
- LinkedIn article linking to site + opt-in form
- Construction subreddit (r/Construction): Link with value statement, no hard sell

**Email platform:** ConvertKit, Mailchimp, or Substack
- Budget: $20–50/month for 1,000–5,000 subscribers
- Preference: Use Substack (free tier supports free content) or ConvertKit (construction industry template available)

#### Post-Launch Email Sequence (First 14 Days)

```
Day 0: Welcome email
  Subject: "Welcome to Construction Career Training — Here's Your 33-Module Curriculum"
  Content: Explain the three paths; link to Quick Start guide; ask which path fits them

Day 1: Path Decision Nudge
  Subject: "Which career path is right for you? (Industrial, Residential, or Specialty Sub)"
  Content: Three short career stories (persona examples); link to each path overview

Day 3: First Module Preview
  Subject: "Start Free: Module 01 Preview — Industrial GC Foundations"
  Content: 2-minute summary of Module 01; excerpt of case study; CTA to start path

Day 7: Progress Report
  Subject: "One Week In: Here's What Your Path Covers (and Why It Matters)"
  Content: Breakdown of phases; time commitment; success stories from beta learners

Day 14: Case Study Offer
  Subject: "Ready to Test Your Knowledge? Free 5-Case-Study Bundle"
  Content: Offer downloadable PDF with answers; link to in-site scenarios
```

#### Ongoing Email Engagement (Post-Launch)

**Weekly curriculum digest (optional):**
- Highlight one module excerpt per week
- Link to case studies for that module
- Short "pro tip" from construction practice
- Frequency: 1 email/week on Tuesday mornings

**Monthly instructor spotlight:**
- Interview someone using curriculum for training
- Ask: "How did you adapt this for your classroom?"
- Feature their syllabus or assessment rubric

**Quarterly regulatory update:**
- Reminder about time-sensitive modules (Title 24 cycle, CSLB fees, ADU statute)
- Email to segment: "Regulatory compliance" subscribers
- Link to updated module versions

#### List Segmentation (for targeted messaging)

**Segment 1: Industrial GC Path**
- Send: Industrial-specific case studies, ASME code updates, CPM scheduling tips
- Frequency: 2 emails/month

**Segment 2: Residential GC Path**
- Send: Residential market tips, CSLB licensing updates, lien rights reminders
- Frequency: 2 emails/month

**Segment 3: Specialty Sub → PM Path**
- Send: Field management tips, PM-level case studies, subcontracting updates
- Frequency: 2 emails/month

**Segment 4: Instructors**
- Send: Classroom setup tips, sample syllabus updates, grading rubrics
- Frequency: 1 email/month

**Segment 5: Inactive Users (no module access in 30 days)**
- Send: "We miss you! Here's a case study to re-engage"
- Frequency: 1 email after 30-day inactivity

### 2.2 Social Media Strategy

#### LinkedIn (Primary Channel)

**Audience:** Professional contractors, project managers, instructors, industry leaders  
**Posting frequency:** 3 posts/week (Tuesday, Thursday, Saturday)

**Content calendar:**

| Post Type | Content Example | Frequency |
|-----------|-----------------|-----------|
| Module Insight | "3 things every residential GC must know about lien rights" + link to Module 13 | 2x/week |
| Case Study | Real scenario from workbook; ask followers how they'd solve it (engagement) | 1x/week |
| Career Story | "From electrician to project manager: here's the curriculum path" (rotating personas) | 1x/week |
| Industry News | Link to CSLB update, Title 24 news, construction law case; relate to curriculum | 1x/week |
| Instructor Highlight | Feature someone teaching the curriculum; share their results | 1x/month |
| Regulatory Alert | "California prevailing wage rates updated" + link to Module 31 | 1x/month |

**LinkedIn Article Sequence (Longer-form content):**
- Week 1: "How to Read Construction Drawings (The Right Way)"
- Week 2: "The Biggest Mistake Residential GCs Make (And How to Fix It)"
- Week 3: "From Specialty Sub to Project Manager: Your 14-Week Roadmap"
- Week 4: "Industrial GC Contracts Explained: GMP vs. Lump Sum vs. T&M"

**LinkedIn hashtags:**
`#construction #generalcontractor #careertraining #constructionmanagement #California #GC #subcontractor #ProjectManagement`

**LinkedIn ads (optional, $5–15/day budget):**
- Target: "General Contractors," "Project Managers," "Construction" industry + California location
- Ad copy: "Complete your GC education. 33 modules, 150 case studies, 3 career paths."
- Landing page: Site homepage or "Quick Start" guide

#### Twitter/X (Secondary, Industry Community)

**Audience:** Construction tech workers, industry commentators, CSLB observers  
**Posting frequency:** 2–3 posts/week

**Content:**
- Short construction tips (280 characters)
- Industry news reactions ("CSLB announced new bond minimums...")
- Case study questions (engagement)
- Module announcements

**Example posts:**
- "Mistake #1: Assuming all liens are perfected. Wrong. California requires 30-day NOC. Module 13 covers the calendar. Link: [site]"
- "Just deployed a 33-module construction curriculum covering everything from ASME codes to lien rights. Free to read. Here's the path for residential GCs: [link]"

**Hashtags:** `#construction #GC #California #constructionlaw #training`

### 2.3 Career and Education Platforms Integration

#### Platform 1: Udemy (Largest Course Marketplace)

**Feasibility:** High (Udemy accepts Markdown-based courses)

**Strategy:**
1. Convert curriculum into 3 separate Udemy courses:
   - "Industrial GC Career Path" (80–100 hours)
   - "Residential GC Career Path" (120–140 hours)
   - "Specialty Sub to PM" (112–130 hours)

2. Udemy course structure:
   - One section per phase
   - One lecture per module
   - Video option: Screen recording of modules + instructor narration (optional; increases engagement 40%)
   - Quiz at end of each section (use case studies as quiz material)

3. Pricing:
   - Launch price: $49 per course (Udemy takes 50–70% cut)
   - Student lifetime access
   - Instructor can offer coupons for email list

**Timeline:** 4–6 weeks (convert modules to video + Udemy format)  
**ROI:** 500+ students × $15 per course (after Udemy cut) = $7,500/year passive income (modest but growing)

**Action step:** Create Udemy instructor account; start with 1 course (Residential path) as pilot

#### Platform 2: Coursera for Institutions

**Feasibility:** Moderate (requires institutional partner; free platform)

**Strategy:**
1. Partner with community college construction programs (California focus)
   - Example: Diablo Valley College, Chabot College (both have construction programs)
2. Offer curriculum as a **Specialization** (not full degree, but credit-eligible)
3. Coursera handles platform; you provide content updates
4. Revenue: Coursera takes cut; you get per-student revenue share

**Timeline:** 8–12 weeks (approval process) + community college partnership  
**Advantage:** Credentialing; students earn Coursera certificate

**Action step:** Identify 2–3 California community colleges with construction programs; reach out with curriculum proposal

#### Platform 3: LinkedIn Learning (B2B Enterprise)

**Feasibility:** High (professional development focus)

**Strategy:**
1. Create executive summary of curriculum
2. Partner with LinkedIn Learning to host course (or sell as B2B training package)
3. License 1–2 "sample" modules to LinkedIn with link to full curriculum
4. Drive enterprise traffic from LinkedIn Learning → your site

**Timeline:** 6–8 weeks (partnership negotiation)

**Action step:** Create LinkedIn Learning pitch deck; contact LinkedIn partnership team

#### Platform 4: edX (Free + Audit Option)

**Feasibility:** Moderate (edX emphasizes credentials)

**Strategy:**
1. Partner with University of California Extension or similar
2. Host curriculum on edX platform (free to audit, paid certificate option)
3. Use to build credibility and audience; link back to main site
4. No revenue, but high authority boost

**Timeline:** 10–12 weeks (partner institution coordination)

### 2.4 Direct Website and SEO Considerations

#### SEO Fundamentals (First 90 Days)

**On-page SEO:**
- Add meta descriptions to every module (160 characters, include key terms)
- Create H1 tag for each page (module title)
- Use H2 and H3 hierarchically
- Internal links: Every module should link to 2–3 related modules
- Image alt text: All diagrams and photos include descriptive alt text
- Page speed: Compress images; target < 2 second load time

**Technical SEO:**
- Generate `sitemap.xml` (Jekyll plugin does this automatically)
- Submit to Google Search Console and Bing Webmaster Tools
- Create `robots.txt` (allow all; point to sitemap)
- Ensure site is mobile-responsive (test in Chrome DevTools)
- HTTPS enabled (GitHub Pages does this automatically)

**Keyword targeting:**
- Primary keywords: "construction career training," "GC certification," "construction management education"
- Long-tail keywords: "how to become a general contractor California," "residential GC training," "CSLB license requirements"
- Module-specific keywords: "reading construction drawings," "lien waivers California," "prevailing wage compliance"

**Content strategy:**
- Write 1–2 blog posts per month answering common construction questions
  - Example: "Do I need a CSLB license to do construction work in California?" (links to Module 12)
  - Link to relevant modules in each post
- Create pillar pages (comprehensive guides):
  - "Complete Guide to California Construction Law and Lien Rights"
  - "How to Start a Residential GC Business in California"
  - "Construction PM: From Specialty Sub to Superintendent"

**Link building:**
- Reach out to construction industry blogs; offer guest post linking to curriculum
- Ask construction associations to link (AGC California, local contractor associations)
- University construction programs: ask them to link as student resource

**Timeline for results:** 3–6 months for organic search traffic growth

#### Email-to-Site Relationship

- Each email should link to specific module
- Track click-through rate; identify most popular modules
- Email segments: "Residential path readers" get Residential-specific email content

### 2.5 Partnership and Referral Channels

#### Partnership Type 1: Construction Associations

**Target organizations:**
- AGC California (Associated General Contractors)
- California Building Industry Association (CBIA)
- Local contractor associations (by county)
- Specialty trade associations (NECA, PLMCA, etc.)

**Outreach approach:**
- Email executive director with curriculum overview
- Offer: Free access to curriculum for member promotion
- Ask: Feature in member newsletter + social media
- Benefit to them: Member value-add; no cost
- Expected result: 50–200 member sign-ups per association

**Partnership terms:**
- You provide: Curriculum access for unlimited members (free)
- They provide: 3 newsletter mentions over 6 months + social promotion
- Exclusive: Can have non-exclusive partnerships with multiple associations

#### Partnership Type 2: Union Training Programs

**Target:**
- IBEW (electricians) local training programs
- Plumbers & Pipefitters union training (UA Local 38, etc.)
- Carpenter's apprenticeship programs
- Heavy equipment operator apprenticeships

**Outreach:**
- Contact training director; propose curriculum as "PMsuper-up-skill" for journeyworkers
- Offer: Free curriculum for union members, or revenue share per student
- Benefit: Upskills members for career advancement
- Expected result: 100–500 union members per program

**Revenue model:**
- Option 1: Donation (curriculum is free; union gives you a donation)
- Option 2: Per-student fee ($5–10/student)
- Option 3: Sponsored corporate training (union pays for all members to have access)

#### Partnership Type 3: Construction Staffing Agencies

**Target:**
- Robert Half (construction division)
- Iqvia, Kforce (construction/engineering staffing)
- Local construction recruiting firms

**Outreach:**
- Propose curriculum as talent development tool
- Offer: Discounted curriculum for their candidates
- Benefit: You place better-prepared candidates; agency looks better to clients
- Expected result: 200–500 placement candidates per year

#### Partnership Type 4: Real Estate Development and Construction Companies

**Target:**
- Regional homebuilders (KB Homes, Lennar, local builders)
- Commercial GCs (Turner, McCarthy, Skanska)
- Specialty contractors (mechanical, electrical, civil)

**Outreach:**
- Contact HR or training director
- Propose: Bulk curriculum license for employee development
- Pricing: $50–100 per employee per year (volume discount)
- Benefit: Standardized training for field and office staff
- Expected result: 5–20 corporate partnerships, $5K–50K annual revenue

#### Partnership Type 5: Community Colleges and Trade Schools

**Target:**
- California community college construction programs
- Trade schools (Oreintment Skills Training, etc.)
- Vocational high schools with construction courses

**Outreach:**
- Email construction instructor; propose curriculum as supplemental material
- Offer: Free access for instructor + all students in program
- Benefit: Instructor gets pre-built course; you get credibility
- Expected result: 3–10 educational institution partnerships

### 2.6 Marketing Messaging Templates

#### Email Campaign Template 1: Path Decision Email

```
Subject: Which construction career path is right for you?

Hi [Name],

I've put together three complete learning paths in one curriculum:

🏭 INDUSTRIAL GC PATH (80–100 hours)
For trades professionals moving to PM roles in manufacturing, 
refineries, and heavy industrial. Covers ASME codes, CPM scheduling, 
industrial safety, and contract management.
→ Start here: [Link to industrial-path.md]

🏠 RESIDENTIAL GC PATH (120–140 hours)
For tradespeople going independent or building a residential GC firm. 
Covers permits, codes, estimating, lien rights, and scaling from first 
project to 10+ projects per year.
→ Start here: [Link to residential-path.md]

🔧 SPECIALTY SUB → PM PATH (112–130 hours)
For electricians, plumbers, framers stepping into supervisory and PM roles. 
Covers the full job (reading all drawings, not just your sheets), contracts, 
scheduling, and managing people.
→ Start here: [Link to specialty-path.md]

Each path includes 33 modules of instruction + 150 case studies. No videos, no fluff — 
just practical knowledge you can use on your next job.

Which path sounds like you?

Best,
[Your Name]
```

#### Email Campaign Template 2: Case Study Engagement

```
Subject: Quick quiz: How would you handle this situation?

Hi [Name],

Here's a real construction scenario from the curriculum. What would you do?

SCENARIO: You're halfway through a residential project. Framing is done; MEP rough-in 
is about to start. Your electrical sub calls: "We need to relocate the main panel. 
The structural engineer didn't coordinate with the architect. That's a change order."

Your options:
A) Approve the change — it's not your fault
B) Push back — structural should have caught it
C) Document everything and escalate to architect and structural together
D) Pause work until you figure it out

What's your call?

[See the worked answer and the principle behind it →](link to case study)

(Our curriculum covers this exact scenario in Module 13 — lien rights — and Module 32 
— change order management. Case-study workbook included.)

Best,
[Your Name]
```

#### Social Media Template 1: LinkedIn Article Excerpt

```
🏗️ THE BIGGEST MISTAKE RESIDENTIAL GCs MAKE

And how to fix it before it costs you $50K.

Here's what I see over and over:

A project goes sideways. Your framing sub gets 2 weeks behind. Your MEP rough-in 
is delayed. You absorb the cost and move forward.

**But you never documented it.**

When the project finally closes, you realize: you lost money. You had no record of 
who caused the delay. You can't claim a CPM delay against anyone because you never 
took photographs or time-stamped the email thread.

**This is a documentation failure.** Not a technical failure.

Our curriculum (3 modules: Scheduling, Change Orders, and Dispute Resolution) teaches 
you the exact documentation system every professional GC uses. You'll know:
- When to take photographs
- What to put in writing (and what NOT to)
- How to preserve your rights for a change order or delay claim
- How a 5-minute email today saves you $50K later

[Start your GC training →](link to site)

#Construction #GeneralContractor #ConstructionManagement
```

#### Social Media Template 2: Twitter Engagement

```
Mistake #87 in residential construction:

Assuming your lien is "automatic."

Wrong. In California, you have 30 days from last work to perfect your lien 
or lose it forever.

Our curriculum covers the calendar, the forms, and the gotchas:

[link to Module 13 teaser]

#Construction #LienRights #California
```

### 2.7 Metrics and Tracking Plan

#### Key Metrics to Track (Monthly)

| Metric | Tool | Target (Year 1) | What It Tells You |
|--------|------|-----------------|-------------------|
| Website traffic | Google Analytics 4 | 5,000+ monthly sessions | Content resonance; SEO progress |
| Module page views | GA4 (module deep-dive) | Top 3 modules: 500+ views each/month | Which topics most valuable |
| Email subscribers | Email platform | 1,000+ by end of Q2 | Audience building; engagement |
| Email open rate | Email platform | 35%+ | Subject line effectiveness |
| Email click-through rate | Email platform | 5%+ | Content relevance |
| Case study engagement | GA4 event tracking | 300+ case-study page views/month | Workbook usage |
| Social media followers | LinkedIn, Twitter | 1,000+ LinkedIn, 500+ Twitter | Social authority building |
| Social engagement rate | LinkedIn Analytics | 3–5% (likes + comments per post) | Content resonance |
| Referral traffic | GA4 source breakdown | 20% of total traffic | Partnership impact |
| Inbound links (backlinks) | Ahrefs or SEMrush | 50+ quality backlinks by Year 1 | SEO authority |

#### Tracking Setup (Implementation Checklist)

- [ ] Google Analytics 4 installed (GA4 code on all pages)
- [ ] Goal conversions set up:
  - "Email signup" (goal value: $1.00)
  - "Module started" (goal value: $2.50)
  - "Case study opened" (goal value: $0.50)
- [ ] Email platform integration (Mailchimp, ConvertKit):
  - UTM parameters on all email links (campaign=email, source=newsletter, medium=email)
  - Track unsubscribe rate
  - Track which modules get clicked most
- [ ] Bitly or short links for social tracking (track clicks per platform)
- [ ] LinkedIn analytics enabled (views, clicks, reactions per post)
- [ ] Monthly reporting spreadsheet:
  - Track metrics above; note month-over-month changes
  - Identify top-performing content (modules, posts, emails)
  - Record partnership outreach status

#### Quarterly Review Checkpoints

**Q1 (Months 1–3) Baseline:**
- Are we getting any organic search traffic?
- What modules are getting the most views?
- Email list growing or stalled?
- Social following building?

**Q2 (Months 4–6) Optimization:**
- Double down on top-performing content
- Adjust email frequency/segmentation based on open rates
- Increase partnership outreach
- Add new blog content targeting high-search-volume keywords

**Q3 (Months 7–9) Growth:**
- Target: 50%+ increase in traffic from Q2
- Launch Udemy or Coursera courses
- Expand social media to new platforms (TikTok if audience skews younger; Instagram if visual focus)

**Q4 (Months 10–12) Authority Building:**
- Publish 2–3 industry guest posts (external blogs)
- Secure 5+ association partnerships
- Plan Year 2 expansion (new platform, new content type)

---

## SECTION 3: ROLLOUT TIMELINE

### Phase A: Pre-Launch (Weeks 1–4)

#### Week 1: Setup and Content Preparation

**Deliverables:**
- GitHub Pages enabled with custom domain configured
- `/docs/` directory structure created and organized
- Jekyll `_config.yml` and `_layouts/` templates ready
- All 33 modules copied to `/docs/modules/`

**Responsible party:** Lead developer or site administrator

**Time investment:** 10–12 hours

**Checklist:**
- [ ] GitHub repo access confirmed
- [ ] Domain registered or DNS configured
- [ ] Pages settings enabled; HTTPS active
- [ ] `/docs/` folder structure created
- [ ] Jekyll theme selected and configured
- [ ] Homepage and navigation pages drafted
- [ ] All modules imported and formatted

#### Week 2: Content Organization and Testing

**Deliverables:**
- Case studies organized into `/docs/case-studies/`
- Resource pages (glossary, templates, forms) created
- Module metadata headers added (title, hours, prerequisites)
- Local Jekyll build tested with 0 build errors

**Responsible party:** Curriculum editor + developer

**Time investment:** 12–15 hours

**Checklist:**
- [ ] Case studies exported and formatted
- [ ] By-module case study organization complete
- [ ] Glossary populated and cross-linked
- [ ] 5–10 templates/forms created (subcontract, lien waiver, inspection checklist)
- [ ] Local Jekyll server running; all pages load
- [ ] Dead link audit completed (0 broken links)
- [ ] Mobile responsiveness tested in 3 browsers

#### Week 3: Pre-Launch Validation and Optimization

**Deliverables:**
- Accessibility audit completed
- SEO metadata added (meta descriptions, keywords)
- Analytics configured (Google Analytics 4 code added)
- Email platform integration ready (signup forms on 3+ pages)
- Staging site live for beta user review

**Responsible party:** Content strategist + developer + beta reviewers

**Time investment:** 15–20 hours

**Checklist:**
- [ ] WAVE accessibility audit; color contrast checked
- [ ] Meta descriptions written for all pages (160 chars)
- [ ] Google Analytics 4 code installed and tested
- [ ] Google Search Console property created and sitemap submitted
- [ ] Email signup form integrated on homepage, quick-start, and module pages
- [ ] Instructor guide written and published
- [ ] Sample syllabus created (16-week course outline)
- [ ] 3–5 beta users invited to review staging site
- [ ] Beta feedback collected and incorporated

#### Week 4: Final Pre-Launch Activities

**Deliverables:**
- Production site ready to go live
- Launch email drafted and scheduled
- Social media posts drafted (48-hour buffer)
- Partner outreach emails ready
- Backup and release tag created

**Responsible party:** Project lead + marketing

**Time investment:** 8–10 hours

**Checklist:**
- [ ] Final content audit: all metadata correct
- [ ] Legal review completed (terms of use, licensing, attribution)
- [ ] Print CSS tested (modules printable to single PDF)
- [ ] Production domain pointing correctly to GitHub Pages
- [ ] HTTPS certificate active and "Enforce HTTPS" enabled
- [ ] GitHub release tag created (v1.0.0)
- [ ] Launch email reviewed and scheduled for 9 AM Monday
- [ ] 5 LinkedIn posts drafted and scheduled (3-day buffer)
- [ ] 5 Twitter posts drafted and scheduled
- [ ] 3–5 partners contacted with early access link
- [ ] FAQ updated based on beta feedback

### Phase B: Launch (Week 5)

#### Launch Day (Monday, Week 5)

**Morning (8 AM–10 AM):**
- [ ] Push final code to main branch (GitHub automatically deploys)
- [ ] Verify site is live at custom domain
- [ ] Final smoke test: click 5 random modules, 5 random links
- [ ] Monitor uptime status (GitHub Pages dashboard)

**Mid-day (10 AM–2 PM):**
- [ ] Send launch email to list (template from Section 2.1)
- [ ] Post homepage announcement to LinkedIn
- [ ] Post to Twitter
- [ ] Announce in 2–3 construction subreddits (r/Construction, r/HomeImprovement, niche sub)

**Late day (2 PM–5 PM):**
- [ ] Send "launch day" partner emails (5–10 association directors, instructors)
- [ ] Respond to early comments on social posts
- [ ] Monitor email platform for replies and signups
- [ ] Log baseline metrics: page views, email signups, social mentions

**Post-launch (Week 5, Days 2–5):**
- [ ] Daily email responses (first 5 days highest engagement)
- [ ] Social media monitoring: respond to comments within 6 hours
- [ ] Watch analytics dashboard: identify any broken pages (404 errors)
- [ ] Collect and address feedback (email, comments)

#### Post-Launch Success Metrics (Day 1–7)

| Metric | Target | Actual |
|--------|--------|--------|
| Site page views (Day 1) | 500+ | |
| Email signups (Day 1) | 100+ | |
| Social media mentions | 20+ | |
| Email list size growth | +500 subscribers | |
| Bounce rate | < 50% | |
| Average session duration | 3+ minutes | |
| Broken links found | 0 | |

### Phase C: Post-Launch Growth (Weeks 6–12)

#### Week 6: Content Distribution Begins

**Email sequence:**
- [ ] Day 1: Welcome email
- [ ] Day 3: Path decision email
- [ ] Day 7: First module preview
- [ ] Day 14: Case study offer

**Social media:**
- [ ] 3 LinkedIn posts published
- [ ] 2 Twitter posts published
- [ ] LinkedIn article published (Module insight)

**Partnership:**
- [ ] 10 partnership outreach emails sent (associations, unions, colleges)
- [ ] 5 construction blogs contacted for guest post opportunity

**Content creation:**
- [ ] 1 blog post published (SEO-targeted keyword)
- [ ] 1 case study highlight post on LinkedIn

**Time investment:** 15–20 hours  
**Responsible party:** Marketing lead + content team

#### Weeks 7–8: Partnership Building

**Outreach results tracking:**
- [ ] Responses received from 5+ partnership opportunities
- [ ] 2–3 partnerships initiated (non-exclusive agreements)
- [ ] 1 educational institution partnership confirmed

**Email sequence:**
- [ ] Weekly curriculum digest emails (1 module excerpt + case study)
- [ ] 2 additional blog posts published

**Social media:**
- [ ] 6 LinkedIn posts (3 per week)
- [ ] 4 Twitter posts (2 per week)
- [ ] 1 LinkedIn article (case study deep-dive)

**Analytics review:**
- [ ] Month 1 baseline metrics reviewed
- [ ] Top 5 modules identified by page views
- [ ] Top email send identified by open rate

**Time investment:** 20–25 hours  
**Responsible party:** Marketing lead

#### Weeks 9–12: Optimization and Expansion

**Udemy course launch (if proceeding):**
- [ ] 1–2 courses created and published to Udemy
- [ ] Pricing and launch strategy set
- [ ] Instructor coupons generated for email list

**Content expansion:**
- [ ] 2 additional blog posts published
- [ ] 1 new pillar page published (comprehensive guide)
- [ ] Glossary expanded (+20 new terms)

**Partnership expansion:**
- [ ] 5–10 additional partnership outreach emails
- [ ] 2–3 new partnerships confirmed
- [ ] 1 association featured in newsletter

**Email segmentation:**
- [ ] Segments created: Industrial GC path, Residential GC path, Specialty Sub, Instructors
- [ ] Segment-specific email content drafted (2–3 emails per segment/month)

**Social media growth:**
- [ ] LinkedIn following target: 500–1,000
- [ ] Twitter following target: 300–500
- [ ] Engagement rate tracked and optimized

**Time investment:** 25–30 hours  
**Responsible party:** Marketing lead + content team

#### Monthly Reporting (Weeks 6, 10, 14)

**Report structure:**
1. Traffic metrics (sessions, page views, new users)
2. Email metrics (subscribers, open rate, click rate)
3. Social metrics (followers, engagement, top posts)
4. Partnership pipeline (active negotiations, closed deals)
5. Recommendation for next month's focus

**Report template:**
```
MONTH 1 ROLLOUT REPORT
Site: constructiontrainingpath.com
Reporting Period: [Date range]

TRAFFIC & ENGAGEMENT
• Total sessions: [X]
• Total page views: [X]
• Average session duration: [X] minutes
• Bounce rate: [X]%
• Top module: [Module name] ([X] views)
• Top referral source: [Google/LinkedIn/Direct]

EMAIL & CONVERSION
• Email subscribers: [X] (+[X] this month)
• Email open rate: [X]%
• Email click rate: [X]%
• Signup conversion rate: [X]%

SOCIAL MEDIA
• LinkedIn followers: [X] (+[X] this month)
• Twitter followers: [X] (+[X] this month)
• Top LinkedIn post: [Post] ([X] impressions)

PARTNERSHIPS
• Partnerships initiated: [X]
• Partnerships closed: [X]
• Est. students from partnerships: [X]
• Partnership pipeline value: $[X]

ACTIONS FOR NEXT MONTH
1. [Action 1]
2. [Action 2]
3. [Action 3]
```

---

## SECTION 4: CONTINGENCY PLANNING

### Issue 1: Low Traffic or Email Signups (Decision Point: Week 6)

**Symptoms:**
- Fewer than 300 page views in first week
- Fewer than 50 email signups in first week
- Bounce rate > 60%

**Root causes to investigate:**
1. Homepage value proposition unclear → Redesign homepage with clearer pain-point copy
2. Email signup form too hard to find → Move form above the fold on homepage
3. Traffic sources not working → Check if social posts are reaching audience (check analytics source breakdown)
4. Mobile experience poor → Test on real devices; check mobile bounce rate specifically

**Contingency actions:**
- [ ] Revise homepage headline and hero section (48-hour turnaround)
- [ ] A/B test email signup CTA (e.g., "Get free case studies" vs. "Join [X] GCs")
- [ ] Boost initial LinkedIn posts with paid ads ($50/week budget)
- [ ] Reach out to 20+ construction subreddits and relevant forums with link (organic outreach)
- [ ] Ask for early user feedback: "Why didn't you sign up?" (email survey)

**Timeline:** Implement within 48–72 hours of identifying issue

### Issue 2: High Bounce Rate on Specific Module Pages

**Symptoms:**
- Module pages show 70%+ bounce rate (vs. site average 50%)
- Users arrive but leave within 10 seconds
- Low average session duration on that module

**Root causes:**
1. Module formatting unreadable on mobile → Check mobile layout
2. Module too long; users overwhelmed → Break into shorter sections with navigation
3. Page takes >3 seconds to load → Compress images; optimize CSS
4. Navigation unclear → Add breadcrumbs and "next module" CTA at top/bottom

**Contingency actions:**
- [ ] Check page load time (Google PageSpeed Insights)
- [ ] Test mobile rendering (Chrome DevTools mobile view)
- [ ] Add table of contents at top of module (auto-generated by Jekyll)
- [ ] Add "next module" button at bottom of page
- [ ] Reduce module from one long page to 3–4 shorter pages (split by major section)

**Timeline:** Fix within 1 week; monitor bounce rate for improvement

### Issue 3: Partnership Outreach Receives Low Response

**Symptoms:**
- Sent 20 partnership emails; only 2 responses
- Responses are non-committal ("We'll think about it")

**Root causes:**
1. Email subject line not compelling → Test subject line variations
2. Recipient doesn't understand value proposition → Make benefit clearer in email
3. Email reaches spam folder → Use different sender name or test with small group first
4. Timing wrong → Reach out during off-season (spring/fall vs. busy summer)

**Contingency actions:**
- [ ] Personalize emails more: "Hi [Name], I noticed [association] trains [X trades]..."
- [ ] Reframe value prop: Instead of "free curriculum," lead with "upskill your members" and "set your program apart"
- [ ] Test email with 3 partners first; refine based on response before mass outreach
- [ ] Follow up after 1 week with phone call (not another email)
- [ ] Identify 3 "quick wins" (smaller programs) that might respond faster to build momentum

**Timeline:** Retest outreach within 2 weeks; plan phone calls for week 3

### Issue 4: Regulatory Content Becomes Outdated (Ongoing)

**Symptoms:**
- CSLB updates licensing requirements
- Title 24 code cycle changes effective date
- California ADU statute amended

**Contingency protocol:**
- [ ] Set calendar reminders for time-sensitive modules (Module 09, 12, 15, 22, 27)
- [ ] Subscribe to:
  - CSLB email updates: cslb.ca.gov/about-us/contact-us
  - California Energy Commission (Title 24 updates)
  - CPUC (NEM tariff updates)
  - CALFIRE (WUI zone updates)
- [ ] When update received:
  1. Flag affected module for review (within 2 weeks)
  2. Update module content + add updated date to metadata
  3. Email subscribers about update ("Module XX has been updated for 2025 codes")
  4. Post update notice on social media

**Timeline:** Non-negotiable; updates must go live within 30 days of regulatory change

---

## CONCLUSION AND IMMEDIATE NEXT STEPS

This deployment plan provides a roadmap for launching the Construction Career Training Curriculum to a professional audience through GitHub Pages, email marketing, social media, and strategic partnerships.

### Phase Completion Targets

| Phase | Duration | Completion Target | Success Metrics |
|-------|----------|-------------------|-----------------|
| **Setup & Testing** | Weeks 1–4 | Week 4, Friday | 0 broken links; mobile responsive; all modules load < 2s |
| **Launch** | 1 week (Week 5) | Week 5, Friday | 500+ page views; 100+ email signups; 0 critical errors |
| **Growth** | Weeks 6–12 | Week 12, Friday | 5,000+ total page views; 500+ email subscribers; 2–3 partnerships initiated |
| **Optimization** | Ongoing (Month 4+) | Ongoing | 50% month-over-month traffic growth; 35%+ email open rate; 5+ active partnerships |

### Immediate Action Items (This Week)

1. **[ ] Enable GitHub Pages** — Estimated time: 15 minutes
   - Go to Settings → Pages; select Branch and folder; save

2. **[ ] Create project timeline** — Estimated time: 30 minutes
   - Copy this plan into Asana/Notion; assign owners to each week's deliverables
   - Schedule weekly check-ins (Monday 10 AM)

3. **[ ] Build `/docs/` directory structure** — Estimated time: 1–2 hours
   - Create folders: modules, case-studies, resources, instructor-guide, etc.
   - Create placeholder README files in each folder

4. **[ ] Draft homepage copy** — Estimated time: 45 minutes
   - Hero headline: Emphasize "3 paths, 33 modules, production-ready"
   - CTA: "Start your path" button → Quick Start guide
   - Social proof (if available): "Used by [X] GCs and contractors"

5. **[ ] Set up email platform** — Estimated time: 30 minutes
   - Create account (ConvertKit or Mailchimp)
   - Build welcome email sequence (3–5 emails)
   - Add signup form code to GitHub Pages

6. **[ ] Schedule first partnership outreach** — Estimated time: 45 minutes
   - Identify 10 partnership prospects (AGC California, local contractor associations, unions)
   - Draft outreach email template
   - Schedule send for next week

**Estimated total time to launch:** 40–60 hours (2.5 weeks at 15–20 hours/week)

---

## SECTION 5: MARKETING AND PROMOTION STRATEGY

### 5.1 Target Audience Segmentation and Personas

#### Persona 1: Residential GC (Age 35–55, 5–20 years experience)

**Profile:**
- Self-employed or small-firm owner (1–10 employees)
- Currently running 3–10 projects/year
- Wants to scale but lacks formal training
- Pain point: Compliance gaps (liens, permits, bonding); project delays from poor scheduling

**Value proposition:**
- "Systematize your business. 140 hours to move from chaos to predictability."
- How curriculum helps: Modules 12–18 (licensing, contracts, lien rights); Modules 27–33 (scaling, project controls)
- Success story angle: "From single projects to predictable revenue: How one GC went from $500K to $2M in annual work"

**Marketing channels:**
- Construction Facebook groups (local California homebuilding groups)
- Construction subreddits (r/Construction, r/HomeImprovement)
- LinkedIn targeting "general contractor" job title, California
- Email partnerships with local contractor associations

**Messaging tone:** Practical, results-focused, time-conscious ("Learn in 140 hours, not 5 years")

---

#### Persona 2: Industrial/Heavy Civil GC (Age 40–60, 15+ years field experience)

**Profile:**
- Works for larger GC (Turner, McCarthy, Skanska, regional firm)
- Moving from field superintendent → project manager → senior PM
- Wants to move faster in career; needs PM credibility
- Pain point: Technical knowledge gaps in ASME codes, critical path scheduling, industrial safety

**Value proposition:**
- "Master industrial construction. 100 hours to PM-level competency."
- How curriculum helps: Modules 01–11 (foundations, ASME, industrial safety); Modules 19–26 (scheduling, coordination, budgets)
- Success story angle: "How a field superintendent became a $5M project manager in 18 months"

**Marketing channels:**
- LinkedIn targeting "construction project manager," engineering firms, heavy civil companies
- Industry associations (AGC Heavy Highway & Bridge Division, ACEC)
- Construction management LinkedIn groups
- Engineering/construction conferences (AGC Convention, ConExpo)

**Messaging tone:** Technical credibility, career advancement, authority ("The curriculum heavy GCs use")

---

#### Persona 3: Specialty Sub → PM Path (Age 25–40, 5–15 years in trade)

**Profile:**
- Master electrician, plumber, framer, HVAC technician
- Tired of field work; wants to move to supervision/PM
- Limited business education; wants fast track to management
- Pain point: Overwhelmed by "whole job" complexity; doesn't understand other trades; weak on contracts/scheduling

**Value proposition:**
- "From trade to management. Your 112-hour roadmap to running a $10M+ budget."
- How curriculum helps: All 33 modules with emphasis on "reading all sheets" (not just own trade); Modules 27–33 (managing people, budgets)
- Success story angle: "How an electrician became a $2M construction PM without going back to school"

**Marketing channels:**
- Union training programs (IBEW, UA, Carpenter unions)
- Construction trade forums and Slack groups
- Apprenticeship programs
- Trade association newsletters (NECA, PLMCA)
- LinkedIn targeting specific trades + "project manager" interest

**Messaging tone:** Accessible, practical, "You know the trade; we'll teach you the business"

---

#### Persona 4: Instructor/Trainer (Age 30–65, 10+ years in construction + teaching)

**Profile:**
- Community college instructor, trade school instructor, union trainer, or private consultant
- Needs pre-built curriculum to save prep time
- Wants credible, industry-relevant content for students
- Pain point: Limited time to create original content; need for standardized assessments

**Value proposition:**
- "Production-ready curriculum. Spend 5 hours/week teaching, not 20 hours creating lesson plans."
- How curriculum helps: Full instructor guides, sample syllabi, assessment rubrics, case study workbook
- Success story angle: "How one instructor went from 80% prep to 20% prep, keeping 80% teaching time"

**Marketing channels:**
- Community college construction program directors
- Trade school networks
- Union training directors
- EdTech associations
- LinkedIn targeting "educator," "instructor," construction-related

**Messaging tone:** Time-saving, professional development, "Elevate your program"

---

#### Persona 5: Career Changer (Age 25–50, transitioning to construction)

**Profile:**
- Military veteran, bootcamp graduate, or mid-career switcher
- Limited construction experience but motivated to learn
- Often underfunded; looking for free or low-cost options
- Pain point: Too much information; doesn't know where to start; intimidated by industry knowledge gaps

**Value proposition:**
- "Construction fundamentals. Your 457,000-word welcome to the industry."
- How curriculum helps: All 33 modules, start to finish; glossary for terminology; no prerequisites
- Success story angle: "Military to general contractor: How a veteran went from zero construction experience to $1M in contracts"

**Marketing channels:**
- Military/veteran organizations (Team Rubicon, United Service Organizations, veteran construction networks)
- Career transition communities (Reddit r/careerchange)
- Bootcamp alumni networks
- Free educational platforms (Medium, LinkedIn articles)

**Messaging tone:** Encouraging, comprehensive, "You don't need experience; you just need guidance"

---

### 5.2 Messaging Framework by Audience

#### Core Message Architecture

**Headline:** "The Construction Curriculum Professional GCs Use to Build $1M+ Businesses"

**Sub-headline (path-specific):**
- Industrial: "Master ASME codes, CPM scheduling, and industrial contracts. 100 hours to PM-level expertise."
- Residential: "From first project to 10+ concurrent jobs. Your systemized scaling blueprint."
- Specialty Sub → PM: "Read any blueprint. Manage any team. Your path from trade mastery to project leadership."

**Supporting proof points:**
- 33 modules covering every major construction discipline
- 150 case studies with worked answers (real-world scenarios)
- 457,000 words of practical instruction
- Designed for self-study or classroom (instructor guide included)
- Free to access (all content on website)

---

#### Message Variation by Audience

**For Residential GCs:**
- Problem: "You're making money, but you're burning out. Every project has surprises."
- Solution: "Systematize your business. Our curriculum teaches the scheduling, lien rights, and contract management systems that separate $500K GCs from $2M GCs."
- CTA: "See how other GCs scaled. Start Module 27: Scaling Your Business."

**For Industrial PMs:**
- Problem: "You're ready for promotion, but you feel pressure on ASME codes and critical path scheduling."
- Solution: "Build PM-level competency in 100 hours. Our curriculum is built by industrial GCs, for field-to-PM transitions."
- CTA: "Learn the codes and scheduling systems. Start Module 01: Industrial GC Foundations."

**For Specialty Subs Moving to PM:**
- Problem: "You're a master of your trade, but you don't understand the whole job."
- Solution: "Learn the full construction system. From trade mastery to project leadership—no business degree required."
- CTA: "Stop being confused by other trades. Start Module 02: Reading All Drawings."

**For Instructors:**
- Problem: "You're creating curriculum from scratch. It's consuming 80% of your prep time."
- Solution: "Use production-ready modules. Sample syllabi, assessment rubrics, case studies—it's all here."
- CTA: "See how to integrate into your program. Download the Instructor Guide."

**For Career Changers:**
- Problem: "Construction is a big industry. Where do you even start?"
- Solution: "A step-by-step curriculum that assumes zero experience. No jargon. No prerequisites."
- CTA: "Start your construction education free. See Module 01: Construction Fundamentals."

---

### 5.3 Pricing and Monetization Strategy

#### Free Model (Recommended for Launch)

**Rationale:**
- Build audience first; monetization second
- GitHub Pages + markdown hosting = $0 hosting cost
- Free content compounds marketing (referrals, SEO, partnerships)
- Lock in early adopters and brand loyalty

**Implementation:**
- All 33 modules free and publicly accessible
- No paywalls, no freemium gates
- Email signup for "premium" features (downloadable PDFs, case study answers)
- Optional: "Donate to support updates" button (or Patreon)

**Timeline:** Months 1–6 (build to 5K+ subscribers, then evaluate paid tier)

---

#### Freemium Model (Months 6+)

**Free tier:**
- Read all 33 modules online
- Access glossary, templates, forms
- Limited case studies (50 of 150)

**Paid tier options:**

**Option A: Subscription ($10–15/month)**
- All 150 case studies with worked answers
- Downloadable module PDFs (print-friendly)
- Email support (Q&A on curriculum topics)
- Early access to new modules
- Instructor discounts (if you're using curriculum to teach)
- Target: 200–500 paying subscribers by Year 2 = $25K–90K annual revenue

**Option B: One-time purchase ($99–149 per path)**
- Purchase one of three paths (Industrial, Residential, Specialty Sub)
- Get all modules + case studies for that path as PDF bundle + lifetime updates
- Best for professionals wanting offline access

**Option C: Corporate/Institutional license ($500–2K/year)**
- Bulk access for entire company or training program
- Unlimited user seats
- Customizable syllabus for instructors
- Dedicated support for integration
- Target: 5–20 corporate licenses by Year 2 = $2.5K–40K annual revenue

**Implementation timeline:**
- Month 6: Announce paid tier in email (offer founding members 1-year discount)
- Month 7: Launch freemium model with split testing (some users see paywall, some don't)
- Track conversion rate; adjust pricing/features based on feedback

---

#### Sponsorship/Advertising Model (Optional)

**Potential sponsors:**
- Tool providers (accounting software: Quickbooks, Freshbooks; scheduling: Bridgit; estimating: PlanGrid, Knowify)
- Material suppliers (Fastenal, ScanSource for electrical)
- Insurance providers (construction liability, workers comp)
- Education platforms (Coursera, LinkedIn Learning)

**Implementation:**
- Discrete sponsorship box on homepage: "This curriculum is sponsored by [tool name]. Try 30 days free."
- 1–2 sponsor logos/banners per module page
- Cost: $2K–10K per sponsorship per year
- Target: 2–3 sponsors by Month 12 = $4K–30K additional revenue

---

### 5.4 Sales Channels and Distribution

#### Channel 1: Direct-to-Site (constructiontrainingpath.com)

**Strategy:**
- Homepage drives email signup
- Email sequence nurtures → conversion to paid (if applicable)
- SEO drives long-tail search traffic (e.g., "how to become general contractor California")
- Social media drives awareness → site visits

**Estimated traffic by Month 12:**
- 5,000–10,000 monthly unique visitors
- 500–1,000 email subscribers
- 50–200 paid conversions (if subscription model)

**Revenue:** $5K–30K/year from direct conversions

---

#### Channel 2: Partnership Distribution

**Partners providing access:**

| Partner | Reach | Revenue Model | Est. Annual Leads |
|---------|-------|----------------|-------------------|
| AGC California | 3,000+ members | Free access (donation) | 200–400 |
| Local contractor assocs. | 5,000+ members (5 assocs) | Free access (donation) | 300–500 |
| Union training programs | 10,000+ members (IBEW, UA, Carpenters) | Per-student fee ($5–10) or donation | 500–1,500 |
| Community colleges (5 programs) | 2,000+ students | Free access (credentialing partnership) | 200–400 |
| Construction staffing agencies | 1,000+ annual placements | Referral discount + lead sharing | 200–300 |

**Total partnership leads by Year 1:** 1,400–3,100

**Revenue from partnerships:** $2K–15K/year (per-student fees + donations) + brand exposure

---

#### Channel 3: Udemy/Coursera/EdX (Months 6–12)

**Platform strategy:**

| Platform | Audience | Revenue Model | Est. Students Year 1 |
|----------|----------|----------------|----------------------|
| Udemy | Self-paced learners (budget-conscious) | $49/course; split with Udemy (30/70) | 500–2,000 |
| Coursera | Institutional + credential seekers | Revenue share + partnerships | 200–800 |
| edX | High-authority audience (free + paid cert) | Credential revenue + partnerships | 100–300 |

**Total platform students by Year 1:** 800–3,100

**Revenue from platforms:** $7.5K–30K/year (net after platform cuts)

---

#### Channel 4: LinkedIn Learning / B2B Training Marketplaces

**Strategy:**
- License 2–3 "sample" modules to LinkedIn Learning (revenue share)
- Position curriculum as enterprise training package for construction companies
- Target: 10–20 corporate licenses at $500–2K/year

**Revenue:** $5K–40K/year

---

#### Channel 5: Affiliate and Referral Partnerships

**Potential affiliates:**
- Construction blogs and YouTube channels
- Construction tech platforms (CoConstruct, Knowify, Touchplan)
- Career transition platforms (Coursera, edX, Springboard)

**Structure:**
- $5–15 per referred student who signs up for paid tier
- Or 10–20% commission on first-year subscription revenue

**Target:** 50–200 referred students/year = $250–3,000 additional revenue

---

### 5.5 Budget Estimation for Paid Marketing

#### Paid Advertising Budget (Year 1)

| Channel | Monthly Spend | Rationale | Est. ROI |
|---------|----------------|-----------|----------|
| LinkedIn ads | $300–500 | Target GCs, PMs by job title + location | 3–5x (leads to partnerships) |
| Google Search ads | $200–400 | "How to become GC," "construction training" keywords | 2–4x (lead generation) |
| Reddit ads | $100–200 | r/Construction, r/HomeImprovement targeting | 2–3x (brand awareness) |
| Facebook ads | $100–200 | Construction groups + lookalike audiences | 2–3x (lead generation) |
| Twitter/X ads | $50–100 | Industry community engagement | 1–2x (brand awareness) |
| **Monthly Total** | **$750–1,400** | — | — |
| **Annual Total** | **$9K–16.8K** | — | — |

**Cost per lead estimate:** $15–50 (depending on channel; partnerships give $0/lead but require relationship building)

---

#### Marketing Operations Budget (Year 1)

| Item | Cost | Purpose |
|------|------|---------|
| Email platform (ConvertKit/Mailchimp) | $600–1,200/year | 1K–5K subscribers |
| Domain name (constructiontrainingpath.com) | $15/year | Custom domain for GitHub Pages |
| Email validation/list management tool | $100–300/year | Keep list clean |
| Link shortening + analytics (Bitly) | $100/year | Track social media clicks |
| Social media scheduler (Buffer, Later) | $100–200/year | Pre-schedule posts (3x/week) |
| Google Analytics & Search Console | Free | Built-in analytics |
| Canva or design tool (for social graphics) | $120/year | 3x social posts/week need graphics |
| **Annual Operations Total** | **$1,035–2,820** | — |

---

#### Content Creation Budget (Year 1)

| Item | Cost | Rationale |
|------|------|-----------|
| Freelance graphics designer (social posts, case studies) | $50–100/month | 4–8 graphics/month |
| Editing/proofreading (if hiring for modules) | $0 | Use free tools (Grammarly); founder handles |
| Video production (if creating module videos for Udemy) | $2,000–5,000 | Optional; can outsource to freelancer |
| Logo design (if custom branding) | $300–1,000 | One-time cost |
| Website copy editing | $0 | Founder handles |
| **Annual Content Total** | **$600–6,000** (if skipping video; $2,600–11,000 with video) | — |

---

#### Total Marketing Budget (Year 1 Estimate)

| Category | Low | High |
|----------|-----|------|
| Paid advertising | $9,000 | $16,800 |
| Marketing operations | $1,035 | $2,820 |
| Content creation | $600 | $11,000 |
| **Total** | **$10,635** | **$30,620** |

**Recommended approach:** Start lean ($10K–15K/year); scale ad spend based on conversion data (Month 2+)

---

## SECTION 6: ANALYTICS AND SUCCESS METRICS

### 6.1 Google Analytics 4 Setup

#### GA4 Implementation Checklist

1. **Create GA4 property:**
   - Go to Google Analytics; click "Create" → Google Analytics 4 property
   - Property name: "Construction Career Training"
   - Website URL: constructiontrainingpath.com
   - Industry category: "Education"

2. **Add GA4 tracking code to site:**
   ```html
   <!-- Add to <head> of all pages (Jekyll template) -->
   <!-- Google Analytics -->
   <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
   <script>
     window.dataLayer = window.dataLayer || [];
     function gtag(){dataLayer.push(arguments);}
     gtag('js', new Date());
     gtag('config', 'G-XXXXXXXXXX');
   </script>
   ```

3. **Create custom events for tracking:**
   - "Email signup" — fired when user submits email signup form
   - "Module started" — fired when user opens any module page
   - "Case study opened" — fired when user clicks case study link
   - "Download PDF" — fired when user downloads module or worksheet
   - "Scroll depth" — track % of page scrolled (0%, 25%, 50%, 75%, 100%)

4. **Set up Google Search Console:**
   - Verify site ownership via DNS record or HTML file
   - Submit sitemap.xml
   - Monitor search queries → track ranking for target keywords
   - Fix crawl errors / blocked resources

5. **Create conversion funnels:**
   - Funnel 1: "Email signup" → "Email open" → "Module started"
   - Funnel 2: "Landing page" → "Quick start module" → "Next module"
   - Funnel 3: "Partnership source" → "Module start" → "Case study completed"

---

#### GA4 Dashboards to Create

**Dashboard 1: Daily Pulse (check every morning)**
- Sessions (daily trend)
- New vs. returning users
- Top 5 pages by pageviews
- Traffic source breakdown (direct, organic, referral, paid)
- Email signups (count from form integrations)

**Dashboard 2: Module Performance (weekly review)**
- Module page views (ranked)
- Time on module (avg session duration)
- Bounce rate by module
- Next module navigation (which modules drive further engagement)
- Module-to-case-study conversion

**Dashboard 3: Audience Insights (monthly)**
- New users gained (month-over-month)
- Email subscriber growth
- User location (CA vs. out-of-state)
- Device type breakdown (mobile vs. desktop)
- Return visitor rate

**Dashboard 4: Conversion Performance (monthly)**
- Email signup conversion rate (signups / sessions)
- Module completion rate (users reaching end of module)
- Case study engagement (case study page views / module views)
- Partner referral traffic (traffic from partnership links)
- Bounce rate trend

---

### 6.2 Email Platform Analytics

#### Metrics to Track (ConvertKit, Mailchimp, Substack)

| Metric | Target (Year 1) | What It Means |
|--------|-----------------|---------------|
| Email list size | 1,000+ by Q2; 2,000+ by Q4 | Audience growth |
| Email open rate | 35%+ | Subject line effectiveness; audience relevance |
| Click-through rate (CTR) | 5%+ | Link relevance; call-to-action clarity |
| Unsubscribe rate | < 1% | Audience fit; email frequency satisfaction |
| Bounce rate | < 2% | List quality |
| Spam complaint rate | < 0.1% | Content appropriateness |
| Most-clicked link | Varies by email | Which content resonates most |
| Most-opened email type | Likely: Path decision or case study | Audience preferences |

#### Email Segmentation Performance Tracking

**Track per segment:**

| Segment | Target Open Rate | Target CTR | Est. Conversion (if paid) |
|---------|------------------|-----------|--------------------------|
| Industrial GC path | 35%+ | 5%+ | 2–3% |
| Residential GC path | 35%+ | 5%+ | 2–3% |
| Specialty Sub → PM | 32%+ | 4%+ | 1–2% |
| Instructors | 40%+ | 6%+ | 3–5% |
| Inactive (30+ day) | 25%+ | 3%+ | 0.5–1% |

---

### 6.3 Social Media Analytics

#### LinkedIn Metrics (Weekly Check)

| Metric | Target (3 months) | What It Means |
|--------|-------------------|---------------|
| Followers | 500–1,000 | Audience growth |
| Post impressions | 500–2,000 per post | Reach and visibility |
| Post engagement (likes + comments) | 50–200 per post | Content resonance; algorithm favor |
| Click-through rate to website | 10–50 clicks per post | CTA effectiveness |
| Profile views | 20–50/week | Brand visibility |
| Mention/share rate | 5–20 per month | Content shareability |

**Top-performing content tracker:**
- Rank posts by engagement rate (engagement / impressions)
- Identify patterns: Case studies outperform news? Success stories outperform tips?
- Double down on high-performers; retire low-performers

---

#### Twitter/X Metrics (Weekly)

| Metric | Target | What It Means |
|--------|--------|---------------|
| Followers | 300–500 | Audience size |
| Retweets + likes | 20–100 per post | Engagement level |
| Clicks to website | 10–30 per post | Traffic quality |
| Mentions/replies | 5–15 per week | Community conversation |
| Impression rate | 500–2,000 per post | Reach |

---

### 6.4 Website Traffic and Engagement Metrics

#### Traffic Goals (Year 1)

| Timeline | Monthly Unique Visitors | Monthly Page Views | Avg. Session Duration |
|----------|--------|----------|-----------|
| Month 1 | 500–1,000 | 1,500–3,000 | 2–3 minutes |
| Month 3 | 1,500–2,500 | 4,500–7,500 | 3–4 minutes |
| Month 6 | 3,000–5,000 | 9,000–15,000 | 4–5 minutes |
| Month 12 | 5,000–10,000 | 15,000–30,000 | 5–7 minutes |

**Target:** 50% month-over-month traffic growth (Months 1–6); 20% (Months 7–12)

---

#### Content Engagement Metrics

**For each module page, track:**
- Page views (how many people read this module?)
- Avg. time on page (how long did they stay?)
- Bounce rate (% who left without clicking internal links)
- Scroll depth (% of page readers scrolled to 50% / 100%)
- CTAs clicked (next module, case study, email signup)

**Target benchmarks:**
- Top 3 modules: 200+ views/month each
- Bounce rate < 50% (good); < 35% (excellent)
- Avg. time on module: 5–10 minutes
- Scroll depth: 60%+ reach bottom of page

---

### 6.5 Partnership and Referral Tracking

#### Partnership Attribution in Analytics

**Setup UTM parameters for each partnership:**

```
Partner: AGC California
Link: constructiontrainingpath.com/?utm_source=agc-ca&utm_medium=referral&utm_campaign=member-promotion

Partner: IBEW Local 38
Link: constructiontrainingpath.com/?utm_source=ibew-local38&utm_medium=referral&utm_campaign=union-training

Partner: Coursera
Link: constructiontrainingpath.com/?utm_source=coursera&utm_medium=platform&utm_campaign=specialization
```

**Track by partner:**
- Referred traffic (sessions from each partner)
- Email signups from partner traffic
- Est. value per partner (signups × avg. lifetime value)
- Conversion funnel (partner → signup → paid tier, if applicable)

**Monthly reporting:**
| Partner | Referral Traffic | Email Signups | Partner Value | Notes |
|---------|------------------|--------------|----------------|-------|
| AGC California | [X] | [X] | $[X] | — |
| IBEW Local 38 | [X] | [X] | $[X] | — |

---

### 6.6 Monthly Reporting Template

**Copy this template for Month 1, 2, 3, etc. reporting:**

```
CONSTRUCTION CAREER TRAINING — MONTHLY METRICS REPORT
Report Date: [Month/Year]
Reporting Period: [Date range]
Prepared by: [Name]

═════════════════════════════════════════════════════════════════

1. WEBSITE TRAFFIC & ENGAGEMENT

Traffic Overview:
• Total sessions: [X] ([+X]% vs. prior month)
• Unique users: [X] ([+X]% vs. prior month)
• Total page views: [X]
• Avg. session duration: [X] minutes
• Bounce rate: [X]%
• Return visitor rate: [X]%

Top 5 Pages by Views:
1. [Module/page name]: [X] views ([X]% of total)
2. [Module/page name]: [X] views
3. [Module/page name]: [X] views
4. [Module/page name]: [X] views
5. [Module/page name]: [X] views

Traffic Sources:
• Organic (Google): [X] sessions ([X]%)
• Direct: [X] sessions ([X]%)
• Referral: [X] sessions ([X]%)
• Social (LinkedIn/Twitter): [X] sessions ([X]%)
• Paid ads: [X] sessions ([X]%)
• Email: [X] sessions ([X]%)

Key Insight: [What did we learn about user behavior this month?]

═════════════════════════════════════════════════════════════════

2. EMAIL & CONVERSION

Email List:
• Total subscribers: [X] ([+X] new this month)
• Email open rate (avg): [X]%
• Click-through rate (avg): [X]%
• Unsubscribe rate: [X]%
• Bounce rate: [X]%

Top Email by Performance:
• Subject: "[X]"
• Open rate: [X]%
• Click-through: [X]%
• Signups to top email: [X]

Conversion Metrics:
• Email signup conversion rate (signups / website visits): [X]%
• Case study email engagement: [X] clicks to case studies
• Partner email performance: [X]% open rate

Key Insight: [What email content resonated best? Any segmentation opportunities?]

═════════════════════════════════════════════════════════════════

3. SOCIAL MEDIA PERFORMANCE

LinkedIn:
• Followers: [X] ([+X] this month)
• Post impressions (total): [X]
• Post engagement (avg): [X] per post
• Engagement rate: [X]%
• Top post: "[X]" ([X] likes, [X] comments, [X] shares)
• Traffic to site from LinkedIn: [X] sessions

Twitter:
• Followers: [X] ([+X] this month)
• Post impressions (total): [X]
• Tweet engagement (avg): [X] per post
• Traffic to site from Twitter: [X] sessions

Key Insight: [Which post type performed best? Content to double down on?]

═════════════════════════════════════════════════════════════════

4. PARTNERSHIP & REFERRAL TRACKING

Active Partnerships:
• Total active: [X] partnerships
• New partnerships initiated: [X]
• Partnerships closed: [X]

Partnership Performance:
[Table: Partner name | Referral traffic | Email signups | Est. annual value]

Referral Pipeline:
• Total outreach emails sent: [X]
• Response rate: [X]%
• Warm leads: [X]
• Negotiations in progress: [X]

Key Insight: [Which partnerships are highest-ROI? Where should we focus outreach?]

═════════════════════════════════════════════════════════════════

5. CONTENT & CURRICULUM USAGE

Module Engagement:
• Total module page views: [X]
• Avg. module views per visitor: [X]
• Top 3 modules: [Module names + views]
• Bounce rate by module (avg): [X]%
• Avg. time on module: [X] minutes

Case Study Engagement:
• Case study page views: [X]
• Case study scenarios accessed: [X] of 150
• Case study % of total page views: [X]%

Resource Usage:
• Glossary page views: [X]
• Template/form downloads: [X]
• Instructor guide views: [X]

Key Insight: [What content is underperforming? Opportunities for new content?]

═════════════════════════════════════════════════════════════════

6. SEO & ORGANIC SEARCH

Google Search Console:
• Total impressions in search: [X]
• Total clicks from search: [X]
• Avg. search ranking position: [X]
• Top 5 search queries driving traffic:
  1. "[Query]" — [X] impressions, [X] clicks
  2. "[Query]" — [X] impressions, [X] clicks
  3. "[Query]" — [X] impressions, [X] clicks
  4. "[Query]" — [X] impressions, [X] clicks
  5. "[Query]" — [X] impressions, [X] clicks

New Keywords Ranking (top 20 positions):
• [X] keywords
• Growth: [+X] keywords vs. prior month

Backlinks:
• Total referring domains: [X]
• New referring domains: [X]
• Top referring domain: [X]

Key Insight: [SEO progress? Keywords gaining momentum? Content gaps?]

═════════════════════════════════════════════════════════════════

7. PAID ADVERTISING (if applicable)

Ad Spend:
• Total spend this month: $[X]
• Spend by channel:
  - LinkedIn ads: $[X]
  - Google Search: $[X]
  - Facebook: $[X]
  - Other: $[X]

Performance:
• Cost per click (avg): $[X]
• Cost per lead: $[X]
• Cost per conversion (if paid): $[X]
• ROI: [X]x

Top Performing Ad:
• Platform: [X]
• Headline: "[X]"
• Click-through rate: [X]%
• Cost per click: $[X]

Key Insight: [Which channels perform best? Any optimizations needed?]

═════════════════════════════════════════════════════════════════

8. GOALS & TARGETS VS. ACTUALS

| Goal | Target | Actual | Status |
|------|--------|--------|--------|
| Monthly unique visitors | [X] | [X] | ✓/✗ |
| Email subscribers | [X] | [X] | ✓/✗ |
| Email open rate | 35%+ | [X]% | ✓/✗ |
| Module page views | [X] | [X] | ✓/✗ |
| Partnership inquiries | [X] | [X] | ✓/✗ |
| Organic search traffic | [X] | [X] | ✓/✗ |

═════════════════════════════════════════════════════════════════

9. RECOMMENDATIONS FOR NEXT MONTH

Based on this month's data, recommend:

1. [Specific action based on data]
   - Rationale: [Why this will improve metrics]
   - Expected impact: [What we expect to gain]
   - Timeline: [When to implement]

2. [Specific action based on data]
   - Rationale: [Why]
   - Expected impact: [What]
   - Timeline: [When]

3. [Specific action based on data]
   - Rationale: [Why]
   - Expected impact: [What]
   - Timeline: [When]

═════════════════════════════════════════════════════════════════

10. RISKS & ISSUES

| Issue | Impact | Mitigation | Owner |
|-------|--------|-----------|-------|
| [Issue] | [Impact] | [Action] | [Owner] |
| [Issue] | [Impact] | [Action] | [Owner] |

═════════════════════════════════════════════════════════════════

END OF REPORT
```

---

### 6.7 Feedback Collection Mechanism

#### In-Site Feedback Form

**Add popup or bottom-of-page form:**

```
"Help us improve this curriculum"

Question 1: "How helpful was this module?"
[ Not at all ] [ Somewhat ] [ Very helpful ] [ Extremely helpful ]

Question 2: "What could we improve?"
[Free text field]

Question 3: "Would you recommend this to a colleague?"
[ Definitely not ] [ Probably not ] [ Maybe ] [ Probably yes ] [ Definitely yes ]

Question 4 (optional): "Your email (for follow-up)"
[Email field]

[Submit button]
```

**When to show:** After user scrolls 50% of module page

---

#### Email Feedback Survey

**Send quarterly (every 3 months) to active subscribers:**

```
Subject: Quick 2-minute survey: Help shape the curriculum

Hi [Name],

We'd love your feedback. Which modules have been most helpful? 
What topics are missing? 

Answer 4 quick questions:
1. Which path are you following? (Industrial / Residential / Specialty Sub)
2. Which module was most useful? (dropdown of 33 modules)
3. What topic should we add? (free text)
4. How likely to recommend? (1–10 scale)

[Take survey button → TypeForm or SurveyMonkey link]

Thanks for your feedback!
[Your name]
```

---

#### Social Media Engagement Monitoring

**Set up monitoring for:**
- Mentions of curriculum by name
- User testimonials (case studies using curriculum)
- Questions about specific modules (community education opportunity)

**Tools:**
- Google Alerts: Set up for "construction career training" + site name
- LinkedIn monitoring: Check comments daily on posts
- Twitter search: Monitor #construction #trainingcommunity mentions
- Reddit monitoring: Search r/Construction, r/HomeImprovement for mentions

---

## SECTION 7: MAINTENANCE AND ITERATION

### 7.1 Post-Launch Content Management

#### Module Update Protocol

**When to update a module:**

1. **Regulatory changes** (within 30 days)
   - CSLB licensing fee updates
   - Title 24 code cycle changes
   - California ADU statute amendments
   - OSHA standard updates
   - State prevailing wage rate changes

2. **User feedback** (within 60 days)
   - Low engagement module (< 50 views/month) → review for clarity
   - High feedback requests ("Can you explain X better?") → revise section
   - Case study requests ("Do you have a scenario on X?") → add scenario

3. **Industry best practice changes** (within 90 days)
   - New estimation or scheduling methodology emerges
   - Case law changes construction liability practices
   - New tools/software become industry standard (mention in module)

4. **Typos/clarity issues** (within 7 days)
   - User feedback on typos or unclear explanations
   - Grammar/spelling check catches issues
   - Technical inaccuracies identified

#### Update Workflow

```
1. Receive update request (email, feedback form, social media)
   ↓
2. Log in update tracker (spreadsheet):
   - Module name
   - Update type (regulatory, feedback, clarification)
   - Requested by / date received
   - Status (queued, in progress, completed)
   ↓
3. Review affected module + case studies
   ↓
4. Make edits to markdown file
   ↓
5. Commit to GitHub with message:
   "docs(modules): update Module 12 for 2025 CSLB licensing fees"
   ↓
6. Verify changes render correctly on site (GitHub Pages auto-deploys)
   ↓
7. Update "Last updated" date in module metadata
   ↓
8. Send email to relevant email segment:
   "Module 12 updated: 2025 CSLB Licensing Changes"
   - Link to updated module
   - Summary of changes
   ↓
9. Post update notice on social media:
   "Module 12 just updated for 2025 CSLB licensing. 
    Check it out: [link]"
   ↓
10. Close in update tracker
```

---

#### Module Metadata: Last Updated Tracking

**Add to every module's frontmatter:**

```yaml
---
title: "Module 12 — CSLB Licensing and Bonding"
path: "General/Regulatory"
hours: 3
difficulty: "Intermediate"
prerequisites: "Module 01–11"
last_updated: "2025-02-27"  # Update this date when module is revised
update_summary: "2025 CSLB fee schedule updated; new minimum bond requirements added"
---
```

**Display on page:**
> Last updated: February 27, 2025. [View change log](#change-log)

---

### 7.2 GitHub Repository Management for Collaboration

#### Repository Structure for Teams

**If working with collaborators:**

```
SuperClaude_Framework/projects/career-training/
├── README.md                 # How to use repo
├── CONTRIBUTING.md           # How to contribute (for instructors, reviewers)
├── docs/                     # Website source (Jekyll)
│   ├── _config.yml
│   ├── _layouts/
│   └── [all module files]
├── content-management/
│   ├── update-tracker.csv    # Log of all module updates
│   ├── feedback-log.md       # User feedback collected
│   └── case-study-archive/   # Rejected/archived case studies
├── ci-cd/
│   └── deploy.yml            # GitHub Actions for auto-deployment
└── .github/
    └── ISSUE_TEMPLATE/
        ├── bug-report.md
        ├── module-feedback.md
        └── new-content-request.md
```

---

#### Collaborative Workflow (If Multiple Contributors)

**1. Branch strategy:**
```
main (production)
├── integration (staging)
│   ├── feature/module-updates-q2
│   ├── feature/new-case-studies
│   └── feature/seo-improvements
```

**2. Contribution process:**
- Create branch from `integration`: `git checkout -b feature/your-update`
- Make changes to markdown files
- Create PR with description:
  ```
  Title: "Update Module 12 for 2025 CSLB fees"
  
  ## Description
  Updated Module 12 with 2025 CSLB licensing fee schedule. 
  Added new minimum bond requirement for asbestos removal.
  
  ## Type of Change
  - [x] Module content update
  - [ ] New case study
  - [ ] Typo/clarity fix
  
  ## Module(s) Affected
  - Module 12: CSLB Licensing and Bonding
  
  ## Related Case Studies
  - Case Study 42 (updated to reflect new bonds)
  ```
- Reviewers approve
- Merge to `integration` for staging review (48 hours)
- After approval, merge `integration` → `main` (auto-deploys to production)

**3. Review checklist for PRs:**
- [ ] Content is accurate (CSLB links verified, case law current)
- [ ] Module metadata updated (hours, difficulty, prerequisites)
- [ ] Case studies cross-linked if affected
- [ ] No broken links or markdown syntax errors
- [ ] Mobile rendering tested
- [ ] Glossary updated with any new terms

---

### 7.3 Version Control and Change Log

#### Semantic Versioning for Curriculum

**Version format: `Major.Minor.Patch`**

- **Major (X.0.0):** New path added OR major curriculum restructure (e.g., 1.0.0 → 2.0.0 = complete rewrite)
- **Minor (1.X.0):** New modules, new case studies, or significant content additions
- **Patch (1.0.X):** Bug fixes, typo corrections, clarifications, regulatory updates

**Example:**
- `1.0.0` — Initial launch (33 modules, 150 case studies, 3 paths)
- `1.1.0` — Added 10 new case studies for Case Study Workbook
- `1.1.1` — Fixed typos in Module 05; updated CSLB links
- `1.2.0` — Added 20 new Module overviews, revised Module 12 for 2025 regulations
- `2.0.0` — Added 4th path (Advanced PM) + 50 new case studies

---

#### Change Log (CHANGELOG.md)

**Maintain in repo root:**

```markdown
# CHANGELOG — Construction Career Training Curriculum

All notable changes to this project will be documented in this file.

## [2.0.0] — 2026-12-01

### Added
- New path: "Advanced Project Manager" (25 modules)
- 50 new case studies for advanced PM track
- Industrial sector specializations (semiconductor fab, pharmaceutical)
- Video module summaries (2–3 min per module; Udemy supplemental)

### Changed
- Reorganized Module 27–33 (scaling content moved to Advanced PM path)
- Updated all CSLB references for 2026 licensing requirements
- Revised case study answers based on Year 1 user feedback

### Fixed
- Mobile rendering issues on long case studies
- Broken link to California ADU statute (Assembly Bill XYZ)
- Typos in Modules 05, 18, 31

---

## [1.2.0] — 2026-06-15

### Added
- 10 new case studies for specialty sub → PM path
- SEO blog series: "How to Read Blueprints," "Lien Rights Checklist"
- Instructor resources: Sample assessment rubric, grading guide

### Changed
- Updated Module 12 (CSLB licensing) for 2025 fee increases
- Expanded Module 22 (prevailing wage) with new wage order links
- Rewrote Module 15 (ADU regulations) for 2025 law changes

### Fixed
- Corrected calculation error in Module 25 (cost estimation)
- Fixed missing image references in Module 08
- Clarified confusing language in Module 33 (dispute resolution)

---

## [1.1.0] — 2026-03-01

### Added
- 20 new case studies (scenarios focused on residential GC path)
- Glossary expansion: +50 terms
- Instructor guide: How to teach each module, timing, classroom setup

### Changed
- Improved mobile rendering for long modules
- Added breadcrumb navigation
- Updated resource links (forms, templates, regulatory links)

### Fixed
- Typos in Modules 02, 07, 14
- Broken links to California regulations

---

## [1.0.0] — 2026-02-01

### Added
- Initial release: 33 modules, 150 case studies, 3 learning paths
- GitHub Pages deployment
- Email signup integration
- Social media templates
- Instructor guide and assessment rubrics

---
```

---

### 7.4 Quarterly Review and Update Schedule

#### Q1 Review (Jan–Mar): Content Quality & Feedback

**Review focus:**
- User feedback from past 3 months (email, form submissions, comments)
- Low-performing modules (< 100 views/quarter) — why? Reorganize? Clarify?
- High-bounce-rate modules — mobile rendering? Too long? Unclear?
- Regulatory compliance: Any CSLB, OSHA, or code updates?

**Deliverables:**
- Content audit report: Recommend 5–10 module improvements
- Regulatory update log: Flag modules needing 2025 regulatory updates
- Plan: Prioritize improvements for implementation

**Timeline:** 20–30 hours  
**Owner:** Curriculum lead

---

#### Q2 Review (Apr–Jun): SEO and Partnership Growth

**Review focus:**
- SEO performance: Which keywords ranking? New opportunities?
- Top-performing modules by traffic: Can these be expanded?
- Partnership pipeline: Active negotiations? New partnerships to pursue?
- Email metrics: Open rates by segment; engagement trend?

**Deliverables:**
- SEO roadmap: 5–10 new blog posts or pillar pages to create
- Partnership report: Active partnerships, pipeline, revenue impact
- Email segmentation analysis: Recommend segment refinements

**Timeline:** 15–20 hours  
**Owner:** Marketing lead

---

#### Q3 Review (Jul–Sep): Expansion Opportunities

**Review focus:**
- Video content: Should modules be recorded for Udemy/YouTube?
- Platform expansion: Readiness for Udemy, Coursera, edX?
- New paths: Demand for "Advanced PM" path? "Small Business Finance"?
- Content gaps: What's users asking for that we don't cover?

**Deliverables:**
- Expansion roadmap: New content, new platforms, new paths
- Video production plan (if approved): Which 5–10 modules to video?
- Market research: Survey users on new path interest

**Timeline:** 15–25 hours  
**Owner:** Product lead

---

#### Q4 Review (Oct–Dec): Annual Planning and Year 2 Strategy

**Review focus:**
- Year 1 performance: Traffic, email, partnerships, revenue (if applicable)
- Content performance: Which modules performed best? Worst?
- Team capacity: Who's needed for Year 2 (if scaling)?
- Budget review: Did we stay on budget? ROI analysis?
- Strategic priorities: What's next for Year 2?

**Deliverables:**
- Year 1 performance report (publish as blog post or newsletter highlight)
- Year 2 strategic plan: New modules, new platforms, new revenue streams
- Budget proposal for Year 2

**Timeline:** 25–35 hours  
**Owner:** Project lead + all stakeholders

---

### 7.5 Long-Term Maintenance Schedule

#### Monthly Maintenance (Ongoing)

**Every 1st of month (2–4 hours):**
- Review and respond to user feedback from email/forms
- Update module if regulatory changes occurred
- Monitor analytics: Identify any broken pages (404 errors)
- Check social media mentions; respond to comments
- Review email metrics; optimize if needed

---

#### Quarterly Maintenance (Every 3 months, 20–30 hours)

**At end of each quarter:**
- Comprehensive analytics review (see Section 6.6 monthly report template)
- Content audit: Module performance, bounce rates, user feedback
- Partnership review: Active negotiations, pipeline status
- SEO review: Ranking keywords, backlinks, opportunities
- Plan next quarter's improvements

---

#### Annual Maintenance (Once per year, 40–60 hours)

**At end of Year 1, then every 12 months:**
- Full content audit: All 33 modules reviewed for accuracy, relevance, clarity
- Regulatory compliance check: Any law changes affecting modules?
- Platform assessment: Udemy performance? Coursera viability? New platforms?
- Strategic planning: New modules? New paths? New business model?
- Team planning: Hiring needs? Role changes?

---

### 7.6 Archival and Versioning Strategy

#### When to Archive Older Content

**Archive (move to `/docs/archive/`) when:**
- Module becomes irrelevant (e.g., Phase 1 content after major curriculum restructure)
- Technology/practice becomes obsolete (e.g., old blueprint reading standards)
- Case study no longer representative (outdated scenario; new scenario added)

**Archive does not mean delete:**
- Keep in version control for historical reference
- Remove from main site navigation
- Redirect old URLs to new equivalent content

**Example:**
```
Original: /docs/modules/01-old-blueprint-standards.md
Archived to: /docs/archive/01-old-blueprint-standards.md
Redirect: /modules/01-blueprints → /modules/02-reading-modern-blueprints.md
```

---

#### Backup and Disaster Recovery

**Weekly:**
- GitHub automatically maintains full version history
- No additional backup needed (GitHub is your backup)

**At major releases (quarterly):**
- Create GitHub release tag: `v1.1.0`, `v1.2.0`, etc.
- Download full site as zip (GitHub → Code → Download ZIP)
- Store in cloud backup (Dropbox, Google Drive, AWS S3)

**In case of catastrophic data loss:**
- Restore from GitHub release tag or version history
- Restore from cloud backup zip
- Time to restore: < 30 minutes

---

Good luck with the launch!
