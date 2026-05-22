---
title: "Track B Critical Gates Execution Guide"
created: "2026-05-22"
updated: "2026-05-22"
timeline: "May 23-28 execution window; May 30 user decisions"
status: "PRODUCTION-READY — Step-by-step guide for all gates"
---

# Seedwarden Track B: Gates 1-3 Execution Guide

**Launch target**: May 30, 2026 (8 days)  
**Critical gates**: May 23-28 (7 days)  
**User decisions**: May 30 (scope, sourcing, final sign-off)

---

## Gate 1: Social Media Account Setup (45-60 min)

**Timeline**: May 23-24 (2 days available)  
**Complexity**: Low (account creation + basic configuration)  
**Pre-requisite**: None  
**Deliverable**: Instagram, TikTok, Pinterest accounts live + documented

### Step 1.1: Create Instagram Business Account (10-15 min)

**Action**:
1. Go to https://instagram.com
2. Sign up with your preferred email (create new account or use existing)
3. Follow setup: username, password, phone number or email verification
4. Once account created, switch to **Business Profile**:
   - Settings → Account Type → Switch to Professional Account → Choose Business
5. Fill in bio: `Native plants • wild edibles • habitat guides 🌱`
6. Save profile photo (use Wikimedia Commons CC-licensed plant image or placeholder)

**Documentation**:
- Username: `[fill after creation]`
- Business category: `Lifestyle`
- Website URL: `[leave blank for now — add after Gate 3]`
- Bio: "Native plants • wild edibles • habitat guides 🌱"
- Contact email: `[your email]`

### Step 1.2: Create TikTok Creator Account (10-15 min)

**Action**:
1. Go to https://tiktok.com
2. Sign up (email or existing account)
3. Follow setup: username, password, phone verification
4. Once created, switch to **Creator Account**:
   - Me → Settings → Account → Switch to Creator Account
5. Fill in bio: `Native plants | wild edibles | habitat guides`
6. Add profile picture (Wikimedia plant image or placeholder)

**Documentation**:
- Username: `[fill after creation]`
- Account type: `Creator`
- Bio: "Native plants | wild edibles | habitat guides"
- Contact: Link Instagram account (optional)

### Step 1.3: Create Pinterest Business Account (10-15 min)

**Action**:
1. Go to https://pinterest.com
2. Sign up with email
3. Follow setup: username, password, interests
4. Switch to **Business Account**:
   - Settings → Account → Switch to Business Account
5. Choose category: `Home Decor`, `Gardening`, or `Education`
6. Fill in about section: `Native plant guides, wild edibles identification, habitat photography`
7. Add profile image (Wikimedia plant image)

**Documentation**:
- Username: `[fill after creation]`
- Account type: `Business`
- Category: `Gardening` or `Home & Garden`
- About: "Native plant guides, wild edibles identification, habitat photography"
- Website: `[leave blank for now]`

### Step 1.4: Credential Storage (5 min)

**Action**:
1. Create `.env.seedwarden` file in `projects/seedwarden/` directory (DO NOT COMMIT)
2. Add credentials:
```
INSTAGRAM_USERNAME=[username]
INSTAGRAM_EMAIL=[email]
INSTAGRAM_PASSWORD=[password]
TIKTOK_USERNAME=[username]
TIKTOK_EMAIL=[email]
TIKTOK_PASSWORD=[password]
PINTEREST_USERNAME=[username]
PINTEREST_EMAIL=[email]
PINTEREST_PASSWORD=[password]
```
3. Restrict file: `chmod 600 .env.seedwarden`
4. Add to `.gitignore` if not already present

### Gate 1 Completion Checklist

- [ ] Instagram account created (business profile)
- [ ] TikTok account created (creator account)
- [ ] Pinterest account created (business account)
- [ ] All three accounts have profile pictures + bios
- [ ] Credentials saved in `.env.seedwarden` (not committed)
- [ ] Document completion: Create `track-b-gate-1-completion.md` with timestamps + account details
- [ ] Commit: `git add projects/seedwarden/track-b-gate-1-completion.md && git commit -m "feat(seedwarden): Gate 1 complete — Instagram/TikTok/Pinterest social media setup"`

**Estimated time**: 45-60 minutes  
**Success criteria**: All three accounts live and accessible  
**Next**: Gate 2 (Canva Brand Kit setup)

---

## Gate 2: Brand Kit + Content Templates (4-6 hours)

**Timeline**: May 25-26 (2 days available)  
**Complexity**: Medium (design system setup)  
**Pre-requisite**: Gate 1 complete  
**Deliverable**: Canva Brand Kit + 5 reusable content templates + zone card templates

### Gate 2 Overview

The goal is to create a reusable design system so all social media posts have consistent branding, fonts, colors, and layout. This is essential before launch day because you'll need to post frequently and consistently.

### Step 2.1: Set Up Canva Brand Kit (30 min)

**Action**:
1. Go to https://canva.com
2. Create account (if not already have one) or log in
3. Go to Brand Kit (https://canva.com/brandkit)
4. Create new Brand Kit named: "Seedwarden Native Plants"

**Brand Colors** (choose from these or add your own):
- Primary: `#2D5016` (dark green)
- Secondary: `#6B9D83` (medium sage green)
- Accent: `#E8C547` (gold/yellow)
- Neutral: `#F5F5F0` (off-white)
- Text: `#1A1A1A` (dark brown/black)

**Brand Fonts**:
- Heading font: `Poppins` (bold, modern)
- Body font: `Inter` or `Roboto` (readable, clean)
- Accent font: `Playfair Display` (elegant, serif for titles)

**Brand Logo**:
- If you have a logo, upload it (or use placeholder)
- Create simple text logo: "Seedwarden" in Poppins Bold

**Brand Elements**:
- Add leaf/plant icon (Canva has built-in icons)
- Add pattern (geometric or nature-inspired)
- Save these as reusable elements

**Time**: 25-30 minutes

### Step 2.2: Create Content Template Library (2 hours)

Create 5 template types in Canva that you'll reuse for all posts:

**Template 1: Plant Profile Post (Instagram/TikTok)**
- Dimensions: 1080 × 1350 (Instagram vertical) or 1080 × 1920 (TikTok)
- Layout: 
  - Top 40%: Large hero photo of plant (habit shot)
  - Bottom 60%: White/off-white background with:
    - Plant common name (Playfair Display, 48pt, dark green)
    - Scientific name (Inter, 18pt, italic, gray)
    - 3 key points (bullets, 16pt)
    - CTA: "Save this guide"
- Colors: Brand colors (dark green background with gold accents)
- Save as template: "Plant Profile - Vertical"

**Template 2: Educational Carousel (Instagram Carousel)**
- Create 3-5 slides for carousel posts
- Slide 1: Title + plant name
- Slides 2-4: "Did you know?" facts
- Slide 5: CTA + hashtags
- Dimensions: 1080 × 1350 each
- Save as: "Educational Carousel - Plant Facts"

**Template 3: Habitat Photo Showcase (Instagram/TikTok)**
- Large photo area (70% of slide)
- Small text area (30%): location + habitat type + date photographed
- Dimensions: 1080 × 1350 (Insta) / 1080 × 1920 (TikTok)
- Save as: "Habitat Showcase - Photo"

**Template 4: Identification Quick-Reference (Pinterest)**
- Dimensions: 1000 × 1500 (Pinterest vertical pin)
- Layout: Plant image + "How to identify [plant]" + 5 quick tips
- Fonts: Large bold heading, readable body
- Save as: "ID Guide - Pinterest Pin"

**Template 5: Seasonal Guide (All platforms)**
- Dimensions: 1080 × 1080 (Instagram square) / Vertical option
- Content: "What to find in [SEASON]"
- Grid of 4-6 plants with small photos + names
- Bottom: Hashtags + date
- Save as: "Seasonal Guide"

**Time**: 1-2 hours

### Step 2.3: Create Zone Card Templates (1-1.5 hours)

These are templates you'll use to showcase different plant zones (e.g., "Northeast Deciduous Forest," "Wetlands & Water Plants," etc.):

**Zone Card Design**:
- Dimensions: 1080 × 1080 (Insta square) / 1000 × 1500 (Pinterest)
- Layout:
  - Top 30%: Zone name (Playfair Display, 42pt bold)
  - Middle 50%: 3-4 representative plant photos (thumbnail grid)
  - Bottom 20%: Brief zone description (2-3 sentences) + "Learn More" button
  - Color: Different color per zone (use brand secondary + zone-specific accent)

**Create templates for these zones** (will personalize later):
1. Zone 1: "Northeast Deciduous Forest"
2. Zone 2: "Wetlands & Water Plants"
3. Zone 3: "Meadows & Grasslands"
4. Zone 4: "Desert & Arid Regions"
5. Zone 5: "Coastal Habitats"

**Time**: 1-1.5 hours

### Gate 2 Completion Checklist

- [ ] Canva Brand Kit created with colors, fonts, logo, elements
- [ ] 5 content templates created and saved in Brand Kit
- [ ] 5 zone card templates created (customizable structure)
- [ ] All templates use consistent branding (colors, fonts, spacing)
- [ ] Templates tested: Create one test post using each template
- [ ] Document completion: Create `track-b-gate-2-completion.md` with template list + links
- [ ] Commit: `git add projects/seedwarden/track-b-gate-2-completion.md && git commit -m "feat(seedwarden): Gate 2 complete — Canva Brand Kit + content templates"`

**Estimated time**: 4-6 hours  
**Success criteria**: All templates ready to use (save time on May 30 launch day)  
**Next**: Gate 3 (Email + landing page)

---

## Gate 3: Email Kit + Landing Page (3-4.5 hours)

**Timeline**: May 27-28 (2 days available)  
**Complexity**: Medium-High (integration across platforms)  
**Pre-requisite**: Gate 1 + Gate 2 complete  
**Deliverable**: Email template + landing page + integration tested

### Gate 3 Overview

Create email signup infrastructure and a simple landing page where people can subscribe to updates, learn about the project, and see featured plants.

### Step 3.1: Set Up Email (30-45 min)

**Option A: Substack (Recommended — easiest)**
1. Go to https://substack.com
2. Create account: username = "seedwarden" (or similar)
3. Fill in publication details:
   - Name: "Seedwarden: Native Plants & Wild Edibles"
   - Description: "Weekly guides to identifying native plants, wild edibles, and habitat photography from North America"
   - Topics: Nature, Education, Guides
4. Choose monetization: Free (for now)
5. Customize branding:
   - Upload header image (Canva design or habitat photo)
   - Set brand color to primary green
   - Add bio/about

**Option B: Mailchimp (More customization)**
1. Go to https://mailchimp.com
2. Create account
3. Create audience: "Seedwarden Subscribers"
4. Set up welcome email template using brand colors/fonts
5. Add email signup form to generate embed code

**Time**: 30-45 minutes

### Step 3.2: Create Landing Page (2-3 hours)

**Option A: Carrd (Simple, fast)**
1. Go to https://carrd.co
2. Create site: "seedwarden-plants" (or similar)
3. Design pages:
   - **Home**: 
     - Hero section: Large habitat photo + "Seedwarden: Guide to Native Plants & Wild Edibles"
     - Subheading: "Identify, learn about, and photograph the wild plants around you"
     - CTA button: "Subscribe for weekly guides"
   - **About**: 
     - Project mission (2-3 paragraphs)
     - What to expect from weekly guides
   - **Featured Plants** (2-3 plant examples):
     - Image + name + quick facts
   - **Contact**: Email signup form
4. Colors: Use brand colors (dark green, gold accents)
5. Domain: Start with Carrd subdomain (upgrade to custom domain later)

**Option B: Webflow (More powerful)**
- Similar process but more design flexibility
- Better for long-term growth
- Steeper learning curve (1.5-2x longer)

**Time**: 2-3 hours

### Step 3.3: Integration Test (30 min)

**Action**:
1. Create test Substack/Mailchimp account using personal email
2. Test landing page signup form → verify email delivers
3. Test email template: Send test message with plant feature content
4. Verify fonts/colors render correctly across devices
5. Document: What works, any issues, fixes needed

**Time**: 30 minutes

### Gate 3 Completion Checklist

- [ ] Email platform set up (Substack or Mailchimp)
- [ ] Landing page created with home + about + featured plants + signup
- [ ] Landing page colors/fonts match Canva Brand Kit
- [ ] Email welcome template created
- [ ] Signup form tested (test email delivered + readable)
- [ ] All links working (email → landing page, landing page → socials)
- [ ] Document completion: Create `track-b-gate-3-completion.md`
- [ ] Commit: `git add projects/seedwarden/track-b-gate-3-completion.md && git commit -m "feat(seedwarden): Gate 3 complete — email kit + landing page"`

**Estimated time**: 3-4.5 hours  
**Success criteria**: Email + landing page live and integrated  
**Next**: May 30 user decisions on scope, sourcing, launch timing

---

## Post-Gate Execution: May 30 Launch Prep

**May 30 user decisions needed**:
1. **Scope**: Which plant zones to launch with (all 5, or subset)
2. **Sourcing**: Confirm photo sourcing strategy (Wikimedia + iNaturalist + original)
3. **Content calendar**: Decide post frequency (daily? 3x/week?) and schedule
4. **Go/no-go**: Final approval to launch May 30 or defer

**May 30 Autonomous Execution** (once user decides):
1. Populate zone cards with actual plant data
2. Create first batch of 5-7 plant profile posts
3. Schedule launch posts across all channels
4. Monitor first 24 hours for engagement, fix issues

---

## Summary Timeline

| Date | Gate | Duration | Deliverable |
|------|------|----------|-------------|
| May 23 | 1 | 45-60 min | Instagram/TikTok/Pinterest accounts live |
| May 25-26 | 2 | 4-6 hrs | Canva Brand Kit + 5 templates |
| May 27-28 | 3 | 3-4.5 hrs | Email + landing page |
| May 29 | Buffer | — | Final testing, refinements |
| May 30 | Launch prep | — | User decisions; execute content population |
| May 31+ | Launch | — | Live 🚀 |

**Total autonomous time**: 8-10.5 hours across 7 days  
**User time before May 30**: ~10-11 hours  
**Completion target**: All gates done by May 28 11:59 UTC; ready for May 30 launch decisions

---

*Execution guide created: May 22, 2026 (13:40 UTC). Status: PRODUCTION-READY. All steps detailed, time-estimated, and checklist-ready. User can execute Gates 1-3 in parallel or sequentially based on availability.*
