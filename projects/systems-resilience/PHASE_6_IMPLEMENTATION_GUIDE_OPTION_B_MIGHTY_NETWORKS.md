---
title: "Phase 6 Platform Implementation Guide — Option B: Mighty Networks (Scale Path)"
project: systems-resilience
phase: 6
option: B
score: "5.5/10"
status: READY — pending June 3 decision
created: 2026-06-02
decision_deadline: 2026-06-03
operational_target: 2026-06-05 00:00 UTC
cost_annual: "$950/yr (annual billing) or $948/yr (monthly billing)"
cross_references:
  - PHASE_6_PLATFORM_ANALYSIS_v2.md
  - PHASE_6_DECISION_SUPPORT_CHECKLIST.md
---

# Option B: Mighty Networks — Scale Path Implementation Guide

**Score**: 22/40 (5.5/10) | **Annual cost**: $950 | **Setup time**: 3–4 hours | **Technical requirement**: None

---

## 1. Pre-Implementation Checklist

Option B requires no server, no DNS configuration, and no technical prerequisites. The checklist is brief.

**Account and Payment**
- [ ] Email address for the community administrator account (this becomes the owner account permanently; use a role address like `community@yourdomain.org` rather than a personal email if possible).
- [ ] Credit card or PayPal for billing. The 14-day trial requires a payment method on file but does not charge until the trial ends.
- [ ] Decision on billing period: $79/month (monthly, cancel anytime, $948/year) vs. $99/month billed annually ($950/year — Mighty Networks quotes this as their "annual plan" at a slight discount vs. the $79 listed price; verify at checkout as pricing changes).

**Brand Assets**
- [ ] Community name decided (cannot be changed after the domain slug is assigned — choose carefully).
- [ ] Community logo or icon (PNG, 500x500 px minimum, transparent background preferred). A simple text-based image is sufficient for launch.
- [ ] Cover/banner image (1500x500 px recommended). Optional for launch but improves first impressions.
- [ ] Short community description (1–2 sentences for the welcome screen).

**Content Ready to Upload**
- [ ] Phase 5 Wave 1 and Wave 2 documents in PDF or DOCX format (Mighty Networks accepts both for file uploads in posts).
- [ ] List of the first 8–12 community builders with email addresses (for the initial invite wave).

**No DNS, no SSH, no server required.**

---

## 2. Step-by-Step Setup

### Step 1 — Account Creation and Trial Activation (15 minutes)

Navigate to `https://www.mightynetworks.com/pricing` and click "Start free trial" on the Launch plan. The trial activates all Launch features for 14 days without a charge.

During the signup flow:
- Set the network name (this becomes your URL slug: `yourcommunity.mn.co`)
- Choose "Community" as the network type
- Skip the optional onboarding questions if short on time — they can be revisited

### Step 2 — Brand Configuration (30 minutes)

From the Admin panel (gear icon → "Settings"):

- Upload your logo (square format, appears in the nav bar and app icon)
- Upload your cover image (appears on the community landing page)
- Set the community tagline and description (shown to prospective members before joining)
- Color theme: select a primary color matching your existing branding. For systems-resilience: dark green or slate blue reads as serious and grounded.
- Welcome email: Admin → Members → Welcome Email. Write a 3–5 sentence welcome message that appears when any new member joins. Include: what the community is for, what members are expected to contribute, and a link to the Knowledge Base space (once created in Step 3).

### Step 3 — Space Configuration (45 minutes)

Spaces are Mighty Networks' equivalent of channels or categories. Create the following:

**Knowledge Base** (type: "Course" or "Posts")
- Visibility: Members only
- Description: "Phase 5 and Phase 6 research documents, protocols, and resource guides"
- Posting permission: Hosts only (prevents clutter; admins post documents, members comment)
- Upload Phase 5 Wave 1 and Wave 2 documents as posts in this space. Title each document clearly and add a 1–2 sentence description. Upload the PDF or link to the GitHub Pages version.

**Discussion** (type: "Posts")
- Visibility: Members only
- Description: "General discussion, questions, and coordination"
- Posting permission: All members
- Enable: "Allow members to create topics"

**Events** (type: "Events" — available on Launch plan)
- Visibility: Members only
- Create the June 15 community foundation session immediately: set title, date/time, description, and enable RSVP. Mighty Networks will send automatic reminders at 24 hours and 1 hour before the event.

**Optional: Announcements** (type: "Posts", hosts-only posting)
- For platform updates and governance decisions. Members can comment but not post new topics.

### Step 4 — Member Onboarding Configuration (30 minutes)

Admin → Members → Member Onboarding:
- Set "Join" mode to "By invitation" (prevents spam signups)
- Enable "Welcome Checklist": create 3–4 checklist items that guide new members (e.g., "Introduce yourself in Discussion", "Read the Community Guidelines", "Browse the Knowledge Base")
- Write a pinned "Welcome and Guidelines" post in the Discussion space. This is the first thing new members see. Include: community purpose, norms of conduct, who to contact with questions.

Admin → Members → Invite Members:
- Enter the email addresses of all 8–12 initial community builders
- Send invitations with a personal message (Mighty Networks allows a custom invite message in the email)
- Invitees receive an email with a direct join link; clicking it creates their account and enrolls them in the community

### Step 5 — Mobile App (10 minutes, members do this themselves)

Mighty Networks' native iOS and Android apps are available in both app stores under the name "Mighty Networks." Instruct members to search for the community name after creating their account. Push notifications are enabled by default. This is the primary engagement advantage of Option B — members receive activity notifications on their phones without configuring anything.

---

## 3. Integration With Existing Systems

**GitHub Pages**
Mighty Networks has no embed or widget capability. The integration is manual: post links to GitHub Pages documents as posts in the Knowledge Base space. Members click through to read on GitHub Pages, then return to Mighty Networks to discuss.

For the opposite direction — linking back to the community from GitHub Pages — add a simple "Join the Community" button in the GitHub Pages site navigation linking to your `yourcommunity.mn.co` URL.

**Email**
Mighty Networks handles all transactional email internally (join notifications, event reminders, digest emails, @mention alerts). No external email configuration is needed. Digest settings are in Admin → Settings → Emails. Set digest frequency to weekly for a volunteer community that doesn't need daily pings.

**Loomio Governance Supplement**
Create a pinned post in the Discussion space titled "Governance Decisions" with a direct link to the Loomio group. Add the Loomio URL to the community's resource links section (Admin → Settings → Links). No technical integration exists between Mighty Networks and Loomio; the link-out pattern is sufficient.

**No API on Launch Plan**
The Mighty Networks API is locked to the Scale plan ($179/month). On the Launch plan ($79/month), there is no programmatic access to community data, no webhooks, and no Zapier integration. All automation requires a manual upgrade to Scale. If any automation is needed in Phase 6 (e.g., posting new GitHub Pages content automatically to the Knowledge Base), either upgrade to Scale ($179/month) or do not choose Option B.

---

## 4. Timeline and Effort Estimate

| Date | Action | Time Required | Prerequisite |
|---|---|---|---|
| June 3 (decision day) | Account creation; trial activated | 15 min | Decision made |
| June 3 | Brand configuration (logo, colors, welcome email) | 30 min | Brand assets ready |
| June 3 | Three spaces created (Knowledge Base, Discussion, Events) | 45 min | Account active |
| June 3 | Phase 5 documents uploaded to Knowledge Base | 60 min | Documents in hand |
| June 3 | June 15 foundation event created with RSVP | 30 min | Events space created |
| June 4 | Welcome post and guidelines written and pinned | 30 min | Discussion space created |
| June 5 (target) | Initial 8–12 invitations sent | 20 min | Invite list ready |
| June 5 | Members join, onboarding checklist appears | Ongoing | Invitations sent |
| June 17 | Trial ends; $79/month billing begins | — | — |

**Critical path**: There is no critical path in the technical sense. The only constraint is having brand assets (logo, cover image) and the invite list ready on June 3. Everything can be done in a single afternoon.

**Total active effort**: approximately 3.5–4 hours, all on June 3.

---

## 5. Post-Launch Validation

**Access and Onboarding**
- [ ] Log in as admin; confirm all three spaces are visible
- [ ] Send a test invitation to yourself (second email address); confirm invite email arrives and "Join" flow creates an account
- [ ] On mobile: install Mighty Networks app, join with the test account, confirm push notification arrives when a post is made

**Content**
- [ ] Open Knowledge Base space; confirm Phase 5 documents are listed with titles and descriptions
- [ ] Open Events space; confirm June 15 event is visible with date, time, and RSVP button

**Email**
- [ ] Test account receives welcome email after joining
- [ ] Verify welcome checklist appears after the test account first logs in

**Success criteria**: A new member can receive an invite, create an account, access Knowledge Base documents, RSVP to the June 15 event, and receive push notifications on mobile — all within 30 minutes of accepting an invite.

**Hard limitation to verify**: Disconnect from WiFi and cellular; confirm no content is accessible. This is the expected behavior (no offline support) but community members should be warned in the welcome materials that the platform requires internet connectivity.

---

## 6. Rollback and Migration Path

Option B has no data portability tools on the Launch plan. The API (required for bulk data export) is a Scale-tier feature.

**Content export options**
- Knowledge Base documents: you still have the original files. No migration needed — re-upload to any other platform.
- Discussion posts: manual copy-paste. Mighty Networks does not export discussion threads. For a community that has been active for less than two weeks (June 3–17 trial period), the volume is small enough to save manually if needed.
- Member list: Admin → Members → Export as CSV (email addresses only). Available on all plans.

**Cost to walk away during trial**: $0 (no charge if cancelled before June 17 trial end).

**Cost to walk away after first payment**: $79 for one month. Annual prepayment ($950) is non-refundable after 30 days per Mighty Networks Terms of Service — do not commit to annual billing unless the trial has confirmed the platform meets needs.

**Migration to Option A or C**: Export member email list (CSV), re-invite via new platform's invite system. Re-post documents (already on local disk). Estimated 2–3 hours to rebuild the same community structure on Discourse or Nextcloud + Matrix. Discussion history is not migrated.

**Minimum viable rollback time**: 30 minutes to export member list and cancel account; 2–3 hours to rebuild on an alternative platform.
