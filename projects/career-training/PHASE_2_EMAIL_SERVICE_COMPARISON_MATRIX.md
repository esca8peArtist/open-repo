---
title: "Phase 2 Email Service Comparison Matrix"
project: career-training
phase: "2"
created: 2026-06-28
status: decision-ready
---

# Phase 2 Email Service Comparison Matrix

**Purpose**: Platform-agnostic comparison to support email list infrastructure decision. Covers Mailchimp, Kit (formerly ConvertKit), and Substack across five dimensions relevant to the career-training static site deployment. Scoring: 1 (poor) to 5 (excellent).

---

## 1. Pricing Comparison (June 2026 Actuals)

### Kit (formerly ConvertKit)

| Plan | Subscribers | Monthly Price | Key Limits |
|------|-------------|---------------|------------|
| Newsletter (Free) | Up to 10,000 | $0 | 1 automation only; "Powered by Kit" badge on all sends |
| Creator | 1,000 | $39/mo | Unlimited automations, sequences, A/B subject testing |
| Creator | 3,000 | $59/mo | Same features |
| Creator | 5,000 | $89/mo | Same features |
| Creator Pro | 1,000 | ~$59/mo | Adds subscriber scoring, FB custom audiences, referral system |

Annual discount: 16% off paid plans.

Kit's free plan is the most generous free tier currently available — 10,000 subscribers, unlimited emails, unlimited forms and landing pages, one automation. The Creator plan underwent a 160% price increase in late 2025 ($15 → $39/mo for 1,000 subscribers). Kit bills on active subscribers only, not total contacts including unsubscribes.

### Mailchimp

| Plan | Contacts | Monthly Price | Key Limits |
|------|----------|---------------|------------|
| Free | 250 | $0 | No automations (removed Feb 2026), 500 sends/mo, 250/day send cap |
| Essentials | 500 | $13/mo | 5,000 sends/mo, 10x contact limit, all templates, scheduling |
| Essentials | 1,500 | $26.50/mo | Same features |
| Essentials | 5,000 | $75/mo | Same features |
| Standard | 500 | $20/mo | Adds advanced automations, 12x send limit, dynamic content |

Mailchimp's free plan has been progressively degraded: 2,000 contacts (2022) → 500 contacts (2023) → 250 contacts with all automations removed (Feb 2026). Mailchimp counts all contacts including unsubscribed addresses against your plan limit, which inflates effective cost.

### Substack

| Plan | Subscribers | Monthly Price | Key Limits |
|------|-------------|---------------|------------|
| Free (free newsletter) | Unlimited | $0 | 10% revenue cut on paid subscriptions |
| Paid newsletter | Unlimited | 10% of revenue + Stripe fees | ~13% total take rate |

Substack has no tiered pricing for free newsletters. The cost model is pure revenue share on paid subscriptions. For a free-access curriculum (career-training's current model), Substack costs nothing but limits email tooling significantly.

### Pricing Score

| Platform | Score | Rationale |
|----------|-------|-----------|
| Kit | 5 | 10,000 subscriber free tier is exceptional for launch phase |
| Mailchimp | 2 | 250 subscriber free tier effectively unusable; paid tiers competitive but free plan stripped |
| Substack | 3 | Free only if you never charge; 10% take rate is punishing at scale |

---

## 2. Static Site Integration

### Kit

Kit provides embeddable HTML forms with custom fields, tags on subscribe, and redirect-on-subscribe configuration. The embed code is a standard `<form>` block with a `<script>` tag that works on any static HTML page including Jekyll-generated GitHub Pages. No server required — the form posts directly to Kit's endpoint. Landing pages are hosted by Kit if you want zero-embed options.

Integration path for GitHub Pages/Jekyll:
1. Create form in Kit dashboard
2. Copy embed code (inline form or modal)
3. Paste into Jekyll `_layouts/default.html` or specific module pages
4. Tags applied at subscribe time based on which form the subscriber used (allows automatic path segmentation at signup)

Kit also integrates with ConvertFlow, Jotform, Typeform, and 100+ other tools via native integrations, useful for adding quiz-based path selection at signup.

### Mailchimp

Mailchimp provides a similar embeddable HTML form. The form posts to `https://[yourlist].list-manage.com/subscribe/post`. Works on any static site. Mailchimp also offers a hosted signup page, pop-up forms via JavaScript snippet, and a dedicated WordPress plugin (not relevant here).

One advantage: Mailchimp's API is mature and well-documented. If you later want to programmatically add subscribers (e.g., from a quiz or path selector), Mailchimp's REST API (`POST /3.0/lists/{list_id}/members`) is simpler to use from a serverless function (Netlify Functions, Cloudflare Workers) than Kit's.

### Substack

Substack does not provide embeddable forms for external sites. Subscribers must visit your Substack page directly. This breaks the "email capture on module pages" flow entirely. Not viable as a primary list tool for a static site.

### Integration Score

| Platform | Score | Rationale |
|----------|-------|-----------|
| Kit | 5 | Clean embed, works on static sites, tag-on-subscribe enables path segmentation at capture |
| Mailchimp | 4 | Equivalent embed, mature API, slightly more complex dashboard but broadly compatible |
| Substack | 1 | No embeddable form; subscribers must navigate to Substack; unusable for static site capture |

---

## 3. Automation Capabilities

### Kit

Kit's automation model is visual and tag-triggered. The key workflow for career-training:

- Subscriber signs up via "Residential GC Path" form → tagged `residential-gc` → enters welcome sequence
- Subscriber clicks "Industrial Path" link in email → tagged `industrial-gc` → routing automation moves them to industrial sequence
- Subscriber opens fewer than 3 emails in 30 days → tagged `low-engagement` → enters re-engagement drip
- Subscriber tagged `instructor` → enters instructor-specific monthly sequence

Kit supports: conditional branching in automations, wait-until triggers (e.g., "wait until subscriber clicks module link"), time delays, tag-based routing, sequence A/B testing on Creator Pro.

Free plan: 1 automation only. This is a meaningful limitation — a welcome sequence plus a path-routing automation already requires 2. You need Creator plan for multi-path automation.

### Mailchimp

Mailchimp's Standard plan adds "Customer Journeys" — visual automation builder with conditional branching. Trigger types: sign-up, tag added, date, purchase, custom API event.

For career-training: sign-up trigger → welcome email → if opens email, branch to path-selection drip; if no open in 7 days, send re-engagement. Available on Standard ($20/mo for 500 contacts).

Mailchimp automation is comparable to Kit's but historically has been less intuitive for non-commerce workflows. E-commerce triggers (abandoned cart, purchase confirmation) are irrelevant here but dominate the Mailchimp UX, adding noise.

Essentials plan (cheapest paid tier) has basic automation but not Customer Journeys. Standard ($20/mo) is effectively the minimum viable plan for multi-step automation.

### Substack

Substack has no meaningful automation. Welcome email is sent automatically but there are no sequences, branching, or tag-based routing. Not suitable for a multi-path nurture model.

### Automation Score

| Platform | Score | Rationale |
|----------|-------|-----------|
| Kit | 5 | Purpose-built for creator-style multi-sequence automation; tag-triggered branching matches the 3-path model exactly |
| Mailchimp | 3 | Capable on Standard plan but UX skews toward e-commerce; adequate for linear sequences |
| Substack | 1 | No automation; unsuitable |

---

## 4. API Availability

### Kit

Kit's v3 API (developers.kit.com) provides:
- `GET /v3/tags` — list all tags
- `POST /v3/tags` — create tag
- `POST /v3/tags/{tag_id}/subscribe` — tag a subscriber
- `DELETE /v3/subscribers/{id}/tags/{tag_id}` — remove tag
- `POST /v3/sequences/{id}/subscribe` — add subscriber to sequence
- `GET /v3/subscribers` — list with filtering
- `POST /v3/forms/{id}/subscribe` — add subscriber to form

API key authentication. Rate limit: 120 requests/minute on Creator plan. Free plan has API access.

Use case for career-training: If you add a "which path are you on?" quiz, a serverless function can call the Kit API to tag subscribers based on their quiz answer, automatically routing them into the right sequence without manual list management.

### Mailchimp

Mailchimp's Marketing API (REST, v3) is among the most mature email APIs:
- `POST /3.0/lists/{list_id}/members` — add/update subscriber
- `PATCH /3.0/lists/{list_id}/members/{subscriber_hash}` — update tags/status
- `POST /3.0/lists/{list_id}/members/{subscriber_hash}/tags` — add/remove tags
- Full webhook support for subscribe, unsubscribe, open, click events

Mailchimp's API is better documented with more third-party SDK support (Python, Node, PHP). Higher rate limits on paid plans.

### Substack

Substack has no public API. No programmatic subscriber management, tagging, or segmentation.

### API Score

| Platform | Score | Rationale |
|----------|-------|-----------|
| Kit | 4 | Clean REST API, adequate rate limits, well-documented for creator use cases |
| Mailchimp | 5 | Most mature API, best third-party SDK ecosystem, webhook support |
| Substack | 1 | No API |

---

## 5. Segmentation and Tagging

### Kit

Kit's segmentation model is subscriber-centric, not list-centric. All subscribers are in one pool; tags and segments organize them.

**Tags** (permanent labels unless removed):
- Applied at signup via form
- Applied by automation when subscriber takes action
- Applied manually or via API
- Example tags for career-training: `industrial-gc`, `residential-gc`, `specialty-sub`, `instructor`, `career-changer`, `inactive-30d`, `high-engagement`

**Segments** (dynamic, filter-based):
- "Subscribers tagged `residential-gc` AND opened an email in last 14 days"
- "Subscribers tagged `instructor` AND NOT tagged `inactive-30d`"
- "Subscribers who clicked any link in last 7 days"

Tags persist across sequences — a subscriber tagged `residential-gc` retains that tag even when they move from the welcome sequence to the monthly digest. This allows permanent path tracking without re-tagging logic.

Creator Pro adds subscriber scoring (behavioral engagement score 0–100), which enables automatic downgrade to re-engagement sequences when score drops below threshold.

### Mailchimp

Mailchimp uses a list (audience) model with tags, groups, and segments.

**Groups** (subscriber-selected interest categories): Good for path selection at signup ("Which path are you following?" with checkboxes).

**Tags** (similar to Kit): Manually applied or via automation.

**Segments**: Filter conditions on any subscriber data field, tag, group membership, engagement behavior.

Mailchimp's segmentation is functionally equivalent to Kit's but requires navigating multiple overlapping systems (groups vs. tags vs. segments), which creates confusion for new users.

### Substack

Substack has no subscriber tagging or segmentation. All subscribers receive all posts. Not viable for a multi-path curriculum.

### Segmentation Score

| Platform | Score | Rationale |
|----------|-------|-----------|
| Kit | 5 | Tag model is elegant and matches multi-path education use case exactly; segments are dynamic and powerful |
| Mailchimp | 4 | Equivalent functionality but multiple overlapping systems (groups/tags/segments) create complexity |
| Substack | 1 | No segmentation |

---

## Summary Scorecard

| Dimension | Weight | Kit | Mailchimp | Substack |
|-----------|--------|-----|-----------|---------|
| Pricing | 25% | 5 | 2 | 3 |
| Static Site Integration | 20% | 5 | 4 | 1 |
| Automation | 25% | 5 | 3 | 1 |
| API Availability | 15% | 4 | 5 | 1 |
| Segmentation/Tagging | 15% | 5 | 4 | 1 |
| **Weighted Score** | | **4.85** | **3.45** | **1.50** |

---

## Recommendation

**Use Kit (formerly ConvertKit). Start on the free plan.**

**Rationale:**

1. The free plan's 10,000 subscriber ceiling covers the entire expected Phase 2 growth period. Most new education sites take 6–18 months to reach 1,000 subscribers; you are unlikely to hit Kit's free tier limit before the project generates revenue or reaches a scale that justifies $39/month.

2. Tag-on-subscribe maps directly to the career-training three-path model. Each form (Industrial, Residential, Specialty Sub) can apply a different tag at the moment of signup, automatically routing subscribers to the correct sequence without any manual intervention.

3. The one-automation limit on the free plan is a real constraint, but it is manageable in Phase 2: build a single branching welcome automation that covers path routing via conditional logic (if tagged `residential-gc` → send residential welcome email; if tagged `industrial-gc` → send industrial welcome email). This satisfies the core use case within the free tier's limit.

4. Upgrade trigger: move to Creator ($39/mo) when you need (a) a second or third standalone automation sequence, (b) A/B testing, or (c) your subscriber count approaches 10,000.

**If you expect to build a paid product quickly (within 6 months) or need Mailchimp's mature API from day one:** Mailchimp Standard at $20/month for 500 contacts is the alternative. Its API is better documented for programmatic subscriber management and its Customer Journeys automation is capable.

**Avoid Substack** for this use case. Its newsletter-discovery network is valuable for pure content publishers but the lack of embeddable forms, automation, and API makes it unsuitable for a curriculum site where path-based segmentation is the core email strategy.

---

## Template Design Notes

Both Kit and Mailchimp provide sufficient template tooling for the career-training email types:

- **Welcome emails**: Plain text performs better than designed templates for B2B/professional audiences. Construction professionals are not impressed by visual newsletters; they respond to clarity and respect for their time.
- **Module digest emails**: Simple single-column layout. Module title as H2, two-sentence excerpt, "Read module" button. No images needed.
- **Case study emails**: Question + multiple choice options + "See answer" link. Fits in 300 words.
- **Regulatory update emails**: Subject line does the work ("Module 12 updated: 2026 CSLB fee changes"). Body: 3 bullet points on what changed, link to module.

For all of the above, Kit's minimal template editor is a feature, not a limitation.

---

## Sources

- [Kit vs Mailchimp Ultimate Comparison 2026 — Moosend](https://moosend.com/blog/convertkit-vs-mailchimp/)
- [Kit Pricing: How Much Will It Cost in 2026 — EmailToolTester](https://www.emailtooltester.com/en/reviews/convertkit/pricing/)
- [Mailchimp Pricing 2026: Every Plan, Hidden Cost — Retainful](https://www.retainful.com/blog/mailchimp-pricing)
- [Kit Developer API Documentation](https://developers.kit.com/api-reference/v3/tags)
- [Tags and Segments in Kit — Kit Help Center](https://help.kit.com/en/articles/4257108-tags-and-segments-in-kit-and-when-to-use-which)
- [ConvertKit Free Plan 2026: What's Included — Mailsoftly](https://mailsoftly.com/blog/kit-free-plan/)
- [Kit vs Substack: Which Newsletter Platform — EmailToolTester](https://www.emailtooltester.com/en/blog/kit-vs-substack/)
- [ConvertKit vs Mailchimp 2026: Which is Better — Froxell](https://www.froxell.com/blog/convertkit-vs-mailchimp-email-platform-comparison)
