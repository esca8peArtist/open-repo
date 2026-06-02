# Track A vs Track B Decision Matrix and Activation Playbook

## What Track A and Track B Actually Are

**Track A** = Etsy store launch. The 21 Phase 1 digital products (seed guides, zone cards, field manuals) go live for paid sale. Revenue from Day 1, but gated on two user-action blockers: tag corrections on three listings and Etsy account/Payments verification.

**Track B** = Free zone card distribution via social media + email list building. Eight zone-specific quickstart card PDFs are distributed for free through Reddit, Instagram, TikTok, Pinterest, and influencer outreach. Subscribers enter a 5-email Kit automation sequence. By Day 10, Email 5 drives them to the Etsy shop with a 15% coupon (SEEDWARDEN15). Track B builds the audience; Track A monetizes it.

---

## Decision Matrix — One Page

| Dimension | Track A Only | Track B Only | Both (Concurrent) |
|---|---|---|---|
| **What launches** | Etsy shop with 21 paid products | Free zone card distribution + email list | Both, with Track B audience feeding Track A revenue |
| **Revenue model** | Direct Etsy sales, $X per product, Day 1 | Zero revenue at launch; Email 5 (Day 10) drives Etsy conversion | Track B builds list; Track A captures revenue |
| **Infrastructure ready** | NO — 2 user blockers remain | YES — all 8 zone PDFs, 5 emails, 18 social posts, 15 influencer contacts verified June 1 | Track B ready now; Track A follows when blockers clear |
| **User time to activate** | 30 min (tag corrections) + 1-5 business days (Etsy verification) | 3.5–4.5 hours total across 5 gates | Same Track B hours + Track A resolves in parallel |
| **Risk** | Etsy verification delay is out of user control | Social handle availability (mitigated: fallbacks documented); Kit DNS propagation timing | Track B risk only; Track A adds Etsy dependency |
| **Launch date** | Unknown (Etsy verification pending) | Today or tomorrow (June 2) | Track B: today; Track A: whenever verification clears |
| **Audience building** | None — Etsy buyers do not become email subscribers automatically | Direct email list in Kit, segmented by zone | Strongest outcome: list grows during Track B window, Email 5 converts to Etsy buyers |
| **Phase 3 gating** | Not a Phase 3 input | Day 3/7/14 checkpoints gate June 22 Phase 3 decision | Same Track B checkpoints gate Phase 3 |
| **Reversibility** | Can pause uploads any time; no public commitment until listings go live | Can halt launch at GO/HOLD gate (07:53 UTC) before anything is public | Independent — each track can stop or continue separately |

**Recommendation**: Launch Track B now. Resolve Track A blockers in parallel whenever convenient. There is no cost to launching Track B today other than 3.5–4.5 hours of user time. Waiting for Track A to clear first has no upside and delays the audience-building window that Phase 3 depends on.

---

## Track B Activation Playbook

Track B activation is the process of completing 5 user action gates, then executing a 7-step autonomous pre-launch sequence, then running launch day. The infrastructure (8 zone PDFs, 5 email bodies, 18 social post drafts, 15 influencer contacts, hour-by-hour launch runbook) is already production-ready.

**Confidence level: 92% launch-ready** once gates are cleared.

---

## Phase 1: Complete the 5 Gates (3.5–4.5 hours total)

Execute in this order — Gate 4 first.

**Gate 4: Upload zone PDFs to Google Drive (20 minutes)**

1. Create a Google Drive folder named "Seedwarden Zone Cards"
2. Upload all 8 PDFs from `/projects/seedwarden/assets/zone-cards/` (Zones 3–10)
3. Set folder sharing: "Anyone with the link can view"
4. For each file, generate a direct download link: `https://drive.google.com/uc?export=download&id=[FILE_ID]`
5. Test all 8 links in incognito browser — each should trigger download
6. Log all 8 links in WORKLOG.md under "Kit Zone Card File URLs"

**Gate 1: Create Social Media Accounts (45–60 minutes)**

- Instagram: handle `seedwarden` (fallbacks: `seedwarden.co`, `seedwarden.seeds`) — Bio: "Field guides for growers, foragers + food preservers. Zone-specific free card below"
- TikTok: mobile app required. Bio: "Field guides for growers + foragers / Free zone card in bio"
- Pinterest Business: "Seedwarden — heirloom seeds, wild edibles, food preservation + zone-specific growing guides"

All three: upload `projects/seedwarden/logos/seedwarden_logo_1.png` as profile photo.

**Gate 3: Create Kit Account and Build Landing Page + Email Automation (2–3 hours)**

1. Create Kit account at kit.com (wanka95@gmail.com). Sender name: Seedwarden.
2. Create 15 tags: `zone-3` through `zone-10` plus `seed-saver`, `forager`, `food-preserver`, `homesteader`, `medicinal-herbs`, `vip-buyer`, `phase-1-buyer`
3. Build landing page: Headline "Get Your Zone Quick-Start Card — Free" with form for First name, Email, Growing zone (Zones 3–10)
4. Build 5-email automation using copy from `execution/TRACK_B_EMAIL_COPY_FINAL.md`: Day 0, Day 2, Day 5, Day 7, Day 10
5. Test email delivery to wanka95@gmail.com — verify zone card download link resolves
6. Change automation status from Draft to Published
7. Update social media bios with Kit landing page URL

**Gate 2: Canva Brand Kit (20–30 minutes, non-blocking)**

This gate does not block launch. It blocks new visual content production only.

1. Log in at canva.com
2. Brand Hub > Create Brand Kit "Seedwarden"
3. Add 10 colors (brand greens, earth tones, zone bands)
4. Add 3 fonts: Playfair Display, Lato, Cormorant Garamond
5. Upload logo

**Gate 5: Confirm SEEDWARDEN15 Coupon (5 minutes, 10-day buffer)**

Etsy Shop Manager > Coupons > Confirm SEEDWARDEN15 is Active, 15% off. This only blocks Email 5 (Day 10).

---

## Phase 2: Autonomous Pre-Launch Steps

Once user reports all 5 gates complete and provides Kit landing page URL, orchestrator executes these 7 steps:

1. Replace all `[LANDING_PAGE_URL]` instances in social calendar with Kit URL
2. Replace `[LANDING_PAGE_URL]` in influencer DM templates
3. Verify Kit automation status is Published (not Draft)
4. Run pre-launch test: submit form as Zone 5, confirm Email 1 arrives within 60s with working PDF link
5. Verify all three social media bios load Kit landing page without errors
6. Confirm SEEDWARDEN15 coupon Active in Etsy
7. Schedule posts (or set phone reminders): Instagram 18:00 UTC, TikTok 16:00 UTC, Pinterest 20:00 UTC

**Pre-launch go/no-go**: Kit Published + all 8 PDFs accessible + all 3 social bios correct. All three must be YES before launch day.

---

## Phase 3: Launch Day (Approximate 3.5–4.0 hours total)

| UTC Time | Action | Notes |
|---|---|---|
| 07:30 | Log in to all 7 platforms, verify setup | Kit, Instagram, TikTok, Pinterest, Etsy, Reddit, Buffer/Later |
| 07:48 | Send final test email; scan for placeholder text | Should see clean zone card delivery |
| 07:53 | GO/HOLD decision | All 3 criteria must be YES |
| 08:00 | Post Reddit r/herbalism launch post (manual) | Cannot pre-schedule Reddit |
| 08:05 | Send outreach emails to 3 Tier 1 contacts | Sabrena Gwin, Susan Leopold, John Gallagher |
| 08:15 | Send DMs to 15 remaining contacts | Via platform DM routes |
| 08:30 | Post Instagram launch post | Manual or scheduled |
| 08:45 | Upload TikTok launch video natively | NOT cross-posted from Instagram |
| 09:00 | Post Pinterest launch pin | Manual or scheduled |
| 09:30–14:30 | Hourly pulse checks (5 min each) | Reply to Reddit comments |
| 16:00 | Mid-day check; optional TikTok boost post | |
| 18:00 | Log Day 0 metrics, queue Day 2 content | |
| 20:00 | Final check, close launch day | |

Total operator time: 3.5–4.0 hours in 5-minute bursts.

---

## Phase 4: Post-Launch Monitoring (Orchestrator Role)

**Day 3 Checkpoint (June 5 if launching June 2)**

| Metric | Minimum (Marginal) | Target | Strong Signal |
|---|---|---|---|
| Combined reach | 500 | 1,000–2,000 | 2,000+ |
| Reddit upvotes | 10 | 30–80 | 80+ |
| Reddit comments | 5 | 50 | 100+ |
| Instagram/TikTok engagement | 50 likes + 10 comments | 100+ likes | 200+ |
| Kit open rate | 15% | 20–30% | 30%+ |
| Kit new subscribers | 5 | 25–50 | 50+ |
| Influencer responses | 1 | 3–5 | 5+ commit to sharing |

Decision: Go / Marginal (proceed with adjustments) / Fail (investigate before continuing)

**Day 7 Checkpoint (June 9)**

Identify Tier 2 partnership candidates from influencer responses. Target: 3+ identified. Metrics: cumulative reach 2,000–5,000, email click-through 5–10%.

**Day 14 Checkpoint (June 16)**

Final Phase 3 launch decision: GO for June 22 / GO with adjustments for June 29 / DEFER. Target: cumulative reach 5,000–15,000, email list 50–150 subscribers.

---

## Timeline Summary

| Date | Milestone |
|---|---|
| June 2 (today) | Gates 4 → 1 → 3 → 2 → 5 completed (3.5–4.5 hrs user time) |
| June 2 evening | Autonomous pre-launch steps executed |
| June 2, 07:30 UTC | Launch day pre-launch verification begins |
| June 2, 08:00 UTC | Reddit post goes live — Track B is launched |
| June 5 | Day 3 checkpoint |
| June 9 | Day 7 checkpoint |
| June 16 | Day 14 checkpoint — Phase 3 GO/DEFER decision |
| June 22 | Phase 3 medicinal herbs bundle production begins (if GO) |

Track A (Etsy tag corrections + account verification) runs in parallel and does not affect any of these dates.
