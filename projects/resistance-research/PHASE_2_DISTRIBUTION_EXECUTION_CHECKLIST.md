---
title: "Phase 2 Distribution Execution Checklist — Domains 56 & 39 Unified Runbook"
created: "2026-05-26"
version: "2.0 (Unified from Session 1645 checklists)"
scope: "Production-ready execution guide for Domain 56 (May 28 send) and Domain 39 (May 28–June 3 send). Synthesizes DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md and DOMAIN_39_JUNE1_PRE_PRODUCTION_CHECKLIST.md into one unified runbook."
deadline: "Domain 56: May 28 send complete. Domain 39: May 28–June 3 distribution complete."
estimated_total_time: "8–10 hours across May 26–June 3"
---

# Phase 2 Distribution Execution Checklist
## Domains 56 & 39 Unified Production Runbook

**How to use this document**: This is a copy-paste-ready checklist synthesizing Session 1645's two detailed checklists. For full context, reference the originals: `DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md` and `DOMAIN_39_JUNE1_PRE_PRODUCTION_CHECKLIST.md`.

---

## Part A: Domain 56 — Civil Service Politicization (May 28 Send)

### Overview: Domain 56 Execution at a Glance

- **What**: Send 4 emails to civil service reform organizations
- **When**: May 28, 2026 (single day execution)
- **Why**: H.R. 492 (Saving the Civil Service Act) pre-recess markup window opens June 1. Organizations with Domain 56 before June 1 can frame their advocacy around democratic-design argument, not just react to it.
- **Recipients**: 4 organizations, 4 different templates
- **Total time**: ~2 hours (30 min per send, staggered across day)

---

### Domain 56 Pre-Flight Verification (May 26–27)

**Complete these checks before May 28 send day:**

**Step 1: Template Verification** (20 min)

- [ ] Gist is live: https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f
  - **Action**: Open in fresh browser tab. If returns 404 → STOP, do not send until you have working URL.
  - **Verify**: Page loads, shows markdown content, no authentication required

- [ ] All 4 email templates exist in source file
  - **Location**: `projects/resistance-research/execution/domain-56-email-template.md`
  - **Verify**: File contains Template 1 (Volcker), Template 4 (Democracy Forward), Template 3 (Government Executive), and CREW contact form text
  - **Action**: If file missing → create it or locate alternate source

- [ ] No major court rulings or policy changes since May 20
  - **Check**: Search "Schedule Policy Career" or "PEER v Trump" on CourtListener
  - **Action**: If major ruling (e.g., injunction on Schedule P/C rule), add postscript to templates noting ruling date and relevant finding

**Step 2: Contact List Verification** (15 min)

| # | Organization | Contact Email | Template | Status |
|---|---|---|---|---|
| 1 | Volcker Alliance | volcker@volckeralliance.org | Template 1 | [ ] Verified |
| 2 | Democracy Forward | info@democracyforward.org | Template 4 | [ ] Verified |
| 3 | CREW | https://www.citizensforethics.org/contact/ | Template 4 (form) | [ ] Verified |
| 4 | Government Executive | editors@govexec.com | Op-ed pitch (this doc) | [ ] Verified |

- **Action**: Open each contact method in browser. Confirm email addresses are current and contact forms are functional.
- **If changed**: Update checklist immediately

**Step 3: One-Time Setup** (5 min)

Fill these two fields now. You will use them consistently across all 4 sends:

- **[YOUR_NAME]**: ________________________________________________
- **[YOUR_CONTACT_INFO]**: ________________________________________________ (personal email, not institutional)

---

### Domain 56 Send Instructions (Execute May 28)

#### Send 1 of 4 — Volcker Alliance

**When**: Morning of May 28 (first send of the day)  
**To**: volcker@volckeralliance.org  
**Method**: Direct email  
**Template**: Template 1 (Civil Service Reform Organizations)  
**Estimated time**: 25 minutes

**Email preparation**:

1. Open `projects/resistance-research/execution/domain-56-email-template.md`
2. Find section: "Template 1: Civil Service Reform Organizations"
3. Copy full text (subject line through sign-off)

**Subject line** (replace default with this):
```
Domain 56 Research: Civil Service Institutional Design — H.R. 492 Pre-Recess Window
```

**Body customizations required**:

1. Replace `[YOUR_NAME]` with your real name (appears near email close)
2. Replace `[YOUR_CONTACT_INFO]` with your email address
3. Add this paragraph at the start of second paragraph, after "I wanted to share a research document:":

```
Your work through the Volcker Alliance on civil service institutional design — and your joint initiative with Partnership for Public Service — represents the most credible bipartisan framework for this issue. Domain 56 provides the historical and constitutional underpinning for your policy recommendations: the Pendleton Act as democratic-infrastructure precedent, and the German Berufsbeamtentum model as a comparative case study for institutional durability.
```

4. Verify Gist URL is intact: `https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f`

**Pre-send checklist**:
- [ ] Subject line updated to specific version above
- [ ] `[YOUR_NAME]` replaced with your name
- [ ] `[YOUR_CONTACT_INFO]` replaced with your email
- [ ] Volcker Alliance customization paragraph inserted in correct location
- [ ] Gist URL is present and matches verified URL above
- [ ] Email sent from your personal email account (not orchestrator or automated address)
- [ ] Sent to: volcker@volckeralliance.org

**After sending**:
- [ ] Record send time in Domain 56 Send Log (Section at end of this checklist)
- [ ] Check inbox for auto-replies or bounces within 30 minutes

---

#### Send 2 of 4 — Democracy Forward

**When**: Late morning or early afternoon, May 28 (2–3 hours after Send 1)  
**To**: info@democracyforward.org  
**Method**: Direct email  
**Template**: Template 4 (Federal Watchdog Organizations)  
**Estimated time**: 25 minutes

**Email preparation**:

1. Open `projects/resistance-research/execution/domain-56-email-template.md`
2. Find section: "Template 4: Federal Watchdog Organizations and Democracy Advocacy"
3. Copy full text

**Subject line**:
```
Litigation Support: Domain 56 APA and Constitutional Analysis — PEER v. Trump Brief Materials
```

**Body customizations required**:

1. Replace `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]`
2. Locate paragraph starting "For Democracy Forward:" — this is already written for them
3. Verify it reads: "Section 3 maps directly to your PEER v. Trump litigation. The APA arbitrary-and-capricious argument (115+ organizational comments not adequately addressed; insufficient engagement with the departure from the Biden 2024 final rule) and the Loper Light statutory authority argument are the document's primary legal analysis..."
4. **Remove** the "**For GAP**:" and "**For Protect Democracy / CREW**:" paragraphs
5. Keep only the Democracy Forward-specific paragraph
6. Verify Gist URL is intact

**Pre-send checklist**:
- [ ] Subject line is litigation-specific version above
- [ ] `[YOUR_NAME]` replaced
- [ ] `[YOUR_CONTACT_INFO]` replaced
- [ ] Only Democracy Forward paragraph is included (other org paragraphs removed)
- [ ] Gist URL intact
- [ ] Sent to: info@democracyforward.org

**After sending**:
- [ ] Record in Send Log

---

#### Send 3 of 4 — CREW (Citizens for Responsibility and Ethics in Washington)

**When**: Afternoon, May 28  
**To**: https://www.citizensforethics.org/contact/ (website contact form)  
**Method**: Contact form submission (not direct email)  
**Template**: Template 4 (Federal Watchdog Organizations), CREW variant  
**Estimated time**: 30 minutes (form navigation adds time)

**Form submission steps**:

1. Open https://www.citizensforethics.org/contact/ in a browser
2. Look for "General Inquiry" or "Research Submission" form type option
3. Open `projects/resistance-research/execution/domain-56-email-template.md`, find Template 4, copy full text

**Form fields to fill**:

- **Name**: your name
- **Email**: your personal email
- **Organization** (if asked): leave blank, or your institutional affiliation if you have one
- **Subject**: `Research Submission: Domain 56 — Civil Service Democratic-Design Analysis`
- **Message**: Paste Template 4 text, then apply these edits:
  1. Replace `[YOUR_NAME]` with your name
  2. Replace `[YOUR_CONTACT_INFO]` with your email
  3. **Keep only** the "For Protect Democracy / CREW:" paragraph. It reads: "The Hungary and Poland case studies document the end-state of the architecture being constructed. V-Dem's 'electoral autocracy' classification for Hungary is the outcome of the same five mechanisms — elite replacement, enforcement capture, independent agency hollowing, whistleblower elimination — now in progress in the United States..."
  4. **Remove** "For GAP:" and "For Democracy Forward:" paragraphs
  5. Verify Gist URL is intact

4. Submit the form
5. Wait for confirmation message (take screenshot or note confirmation text)

**Pre-send checklist**:
- [ ] Form URL opened: citizensforethics.org/contact
- [ ] Subject line filled correctly
- [ ] `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` replaced
- [ ] Only CREW-specific paragraph included
- [ ] Gist URL intact
- [ ] Form submitted
- [ ] Confirmation message received and noted

**Fallback**: If contact form is broken/unavailable, search CREW website for staff email (media, press contacts), use same message text with same subject line, send as direct email.

**After submitting**:
- [ ] Record in Send Log: form submitted, confirmation received Y/N, any error messages

---

#### Send 4 of 4 — Government Executive

**When**: Late afternoon or evening, May 28 (last send)  
**To**: editors@govexec.com  
**Method**: Direct email  
**Format**: Op-ed pitch (different from other three sends)  
**Template**: Op-ed pitch text (in Session 1645 checklist, Section: "Send 4 of 4")  
**Estimated time**: 30 minutes

**Important**: Government Executive is a trade publication. This is an editorial pitch for a guest op-ed or analysis piece, not a research submission. Tone should be journalistic/editorial, not advocacy-heavy.

**Email to send** (copy this entire block and fill the two fields):

**Subject**:
```
Op-Ed Pitch: The Democratic-Design Argument for Civil Service Reform — New Angle on Schedule P/C
```

**Body**:
```
Dear Government Executive editorial team,

I'm pitching a guest op-ed or analysis piece on civil service reform that I believe will resonate with your federal employee and government community readership.

Headline: "The Democratic-Design Argument for Civil Service Reform: Why the Pendleton Act Matters Beyond Schedule P/C"

Lead fact: Over 385,000 federal employees have departed since January 2025. The civil service reform debate has focused on employment impacts. This piece reframes the issue as a structural threat to electoral accountability — a genuinely new angle for your coverage space.

Angle: The Pendleton Civil Service Reform Act (1883) was not primarily a labor protection statute. It was a democratic infrastructure statute — the legislative response to the spoils system's fundamental corruption of democratic governance. When Schedule Policy/Career reclassifies 50,000 career positions and removes MSPB appeal rights, it is not merely an employment policy change. It is the replication of the spoils system's functional structure with 21st-century mechanisms.

Key points:
- Historical: Pendleton Act (1883) as democratic infrastructure, not employment protection
- The "30 to 6" data: DOJ Voting Section collapsed from 30 to 6 attorneys; 95% drop in voting rights enforcement actions — this is your publication's audience
- Constitutional: Humphrey's Executor doctrine and MSPB independence
- Comparative: Hungary and Poland case studies document what this architecture produces once complete
- Legislative: H.R. 492 / Saving the Civil Service Act is in committee; the June 1-30 pre-recess window is the current advocacy moment

Full research (6,800 words, 47 citations) available for reference and citation sourcing:
https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f

Author credentials: [YOUR_NAME], research on democratic governance and civil service institutional design
Word count for op-ed: 1,000-1,500 words, flexible
Timing: Available immediately

Open to discussion about angle, length, or publication timeline.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**Customization**: Replace `[YOUR_NAME]` (appears twice) and `[YOUR_CONTACT_INFO]` (appears once). Everything else is ready to send.

**Pre-send checklist**:
- [ ] Subject line is the op-ed pitch version
- [ ] Both instances of `[YOUR_NAME]` replaced
- [ ] Both instances of `[YOUR_CONTACT_INFO]` replaced
- [ ] Gist URL intact and verified
- [ ] Tone review: reads like editorial pitch, not advocacy email
- [ ] Sent to: editors@govexec.com

**After sending**:
- [ ] Record in Send Log

---

### Domain 56 Response Tracking (May 28–31)

**Check your email at these intervals**:

| Check | When | What to Look For |
|---|---|---|
| **T+4h** | May 28 evening | Any auto-replies or bounces; log immediately |
| **T+24h** | May 29 morning | First substantive replies; score per rubric below |
| **T+48h** | May 30 | Second reply check |
| **T+72h** | May 31 | 72-hour window close; assess response rate |

**Response scoring rubric**:
- **Score 5**: Organization offers to distribute, cite in their publications, or brief their team
- **Score 3**: Substantive reply engaging with the analysis (not a form acknowledgment)
- **Score 1**: Generic thank-you or auto-acknowledgment
- **Score 0**: No reply, bounce, or unsubscribe

**Target**: 2 of 4 substantive replies (Score 3+) within 72 hours is a successful send wave.

---

### Domain 56 Contingency: No Response After 72 Hours

If zero substantive replies by May 31:

1. **Check for bounces first**: If any emails bounced, use alternative contact methods. Search organization websites for named staff contacts (policy directors, communications directors) and resend to a named person.

2. **Follow-up template** (send June 3–4 to non-respondents):

**Subject**: Following up — Domain 56 civil service analysis [H.R. 492 markup window now open]

```
Following up on my May 28 message — the H.R. 492 / Saving the Civil Service Act pre-recess markup window is now open (June 1-30). If the democratic-design framing in Domain 56 is useful for your work during this window, I'm happy to discuss or provide an adapted version.

[Gist URL]

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

3. **Do NOT follow up with Government Executive** — publication pitches get one send only. Multiple follow-ups burn the contact. Give them 10 business days before any follow-up.

4. **For Volcker Alliance or Democracy Forward if no response by June 1**: Add them to legislative window follow-up. When H.R. 492 markup is announced (check Congress.gov), resend with markup date as new hook.

---

### Domain 56 Send Log

| # | Organization | Contact Method | Sent Date | Sent Time | Gist Link Used | Bounce/Error | Response by May 31 | Score | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Volcker Alliance | Direct email: volcker@volckeralliance.org | May 28 | | | | | | |
| 2 | Democracy Forward | Direct email: info@democracyforward.org | May 28 | | | | | | |
| 3 | CREW | Contact form: citizensforethics.org/contact | May 28 | | | | | | |
| 4 | Government Executive | Direct email: editors@govexec.com | May 28 | | | | | | |

---

## Part B: Domain 39 — Healthcare Access & Democratic Infrastructure (May 28–June 3 Distribution)

### Overview: Domain 39 Execution at a Glance

- **What**: 5-tier distribution to healthcare + voting rights organizations
- **When**: May 28 (internal prep complete), May 30–June 3 (Tier 1–3 sends)
- **Why**: HHS interim final rule on OBBBA Medicaid work requirements drops June 1. Organizations that have Domain 39 *before* the rule can frame publication as a democracy event, not just a health policy reaction.
- **Recipients**: 5 organizations across 3 tiers (Georgetown CCF, NHeLP, Brennan Center, IRG, Black Mamas Matter)
- **Total time**: 4–5 hours across May 26–June 3

---

### Domain 39 Pre-Production Checklist (Complete by May 29)

#### Step 1: Source Document Verification (May 26–27)

**Time**: 20 minutes

Verify the Domain 39 research document is production-complete before creating the Gist.

**File to check**: `projects/resistance-research/domain-39-healthcare-access-democratic-infrastructure.md`

**Verification checklist**:

- [ ] Open file; confirm header shows `status: production-complete`
- [ ] Confirm citation count is ~47 (count sources: peer-reviewed, government, institutional healthcare, institutional democracy, disability rights, maternal health)
- [ ] Confirm Lead Finding section references June 1 HHS rule as active deadline
- [ ] Quick-check rural hospital closure statistic: 417 vulnerable facilities as of January 2026 (if you've seen updated figure, note it but don't delay send)
- [ ] Verify one key citation for live access: https://ccf.georgetown.edu/2025/04/17/medicaid-work-reporting-requirements-under-consideration-by-congress-put-people-with-disabilities-cancer-and-those-impacted-by-the-opioid-crisis-at-risk/ (if 404, note it; citation still exists but Georgetown CCF site may have issues)

**Outcome**: If all checks pass, proceed to Step 2. If status shows anything other than production-complete, read `DOMAIN_39_DISTRIBUTION_STRATEGY.md` for known gaps before proceeding.

#### Step 2: Create Domain 39 GitHub Gist (May 27–29)

**Time**: 30–40 minutes

The document needs to be publicly accessible via a Gist URL before any emails are sent.

**Steps**:

1. Go to https://gist.github.com
2. Log in with your GitHub account (same account as Domain 56 Gist: esca8peArtist)
3. Create a new Gist:
   - **Filename**: `domain-39-healthcare-access-democratic-infrastructure.md`
   - **Description**: `Domain 39: Healthcare Access as Democratic Infrastructure — How Medical Exclusion Functions as Civic Exclusion`
   - **Content**: Paste full text from `projects/resistance-research/domain-39-healthcare-access-democratic-infrastructure.md`
   - **Visibility**: Public (essential — recipients must open without GitHub account)

4. Click "Create public Gist"
5. Copy the Gist URL (format: `https://gist.github.com/esca8peArtist/[hash]`)
6. Test the URL in an incognito browser window:
   - [ ] Page loads without requiring login
   - [ ] Title and markdown render correctly
   - [ ] No 404 or authentication errors

**After creating Gist, record URL here**:

Domain 39 Gist URL: ___________________________________________________

**Then**: Replace all instances of `[Gist URL — insert before send]` in all email templates below (Steps 4 & 5) with this actual URL. Use find-and-replace in your text editor.

---

#### Step 3: Key Contacts Verification (May 27–28)

**Time**: 30 minutes

Verify that the 5 highest-priority contact emails and form URLs are still current before the send window.

| # | Organization | Contact Method | URL to Verify | Status |
|---|---|---|---|---|
| 1 | Georgetown Center for Children and Families (CCF) | childhealth@georgetown.edu (NOT ccf@georgetown.edu) | https://ccf.georgetown.edu/about-us/contact-us/ | [ ] Verified |
| 2 | National Health Law Program (NHeLP) | info@healthlaw.org OR contact form | https://healthlaw.org/contact/ | [ ] Verified |
| 3 | Brennan Center for Justice | Contact form | https://www.brennancenter.org/contact | [ ] Verified |
| 4 | Institute for Responsive Government (IRG) | Contact form | https://responsivegov.org/contact/ | [ ] Verified |
| 5 | Black Mamas Matter Alliance | Contact form | https://blackmamasmatter.org/contact/ | [ ] Verified |

**Verification process** (5 min per contact):
- Load the contact URL
- Confirm page is active (not 404 or parked domain)
- For email addresses: confirm organization website exists
- Note any changes to contact process (some orgs use Submittable or other platforms now)

---

### Domain 39 Email Templates & Tier 1 Wave (Send May 30)

#### Email 1: Georgetown Center for Children and Families

**To**: childhealth@georgetown.edu (CORRECTED — ccf@georgetown.edu is wrong; CC: Catherine.Hope@Georgetown.edu for press)  
**Timing**: May 30 (two days before June 1 rule)  
**Time**: 15 minutes

**Subject**:
```
Democratic participation dimension of OBBBA work requirements — for your June 1 analysis
```

**Body**:
```
Dear Georgetown CCF team,

As the HHS interim final rule on OBBBA work requirements drops on June 1, I want to share an analysis that adds the democratic participation dimension to your work on exemption inadequacy and enrollment infrastructure.

Your April 2025 documentation of the disability exemption gap — particularly the documentation catch-22 (prove disability to a physician you cannot access because you lost coverage) — is incorporated directly in this document as one of three disability disenfranchisement pathways. But the democratic participation argument extends your analysis: Medicaid enrollment offices are statutory voter registration sites under 52 U.S.C. § 20506. The OBBBA's 6-month redetermination cycles and administrative compression don't just degrade coverage stability — they degrade the voter registration infrastructure for low-income populations who depend on Medicaid offices as their primary registration point.

The specific finding: states with Medicaid Automatic Voter Registration achieve 85-90% registration rates. States with traditional NVRA paper-form compliance achieve 1.6%. That 50-fold gap widens when enrollment office capacity is compressed. Organizations framing their June 1 advocacy around HHS's discretionary implementation choices should have this argument in hand.

Three additional findings that may be directly relevant to your current work:

First: A peer-reviewed study of 10.5 million rural voters (Cox, Epp, and Shepherd, American Political Science Review, August 2025) found 3.8 percentage-point voter turnout reduction in communities affected by hospital closures. The 417 rural hospitals currently classified as vulnerable to closure are concentrated in states that declined Medicaid expansion — the political choice not to extend coverage predicts the turnout penalty the OBBBA cuts will generate.

Second: CBO projects 1.3 million additional uninsured Americans in 2026, rising to 6.8 million by 2028. Each percentage point absorbed into the medical debt burden is a documented reduction in civic engagement capacity for those households — the same scarcity mechanism documented in financial stress and educational achievement research.

Third: The Trump administration's proposed elimination of the Protection and Advocacy for Voting Accessibility program (PAVA, $10 million annually, $130 million distributed since 2003) removes the primary legal infrastructure that makes voting accessible for disabled Medicaid beneficiaries — the same population most affected by work requirement exemption inadequacy.

Full analysis (approximately 7,200 words, 47 citations):
[INSERT DOMAIN 39 GIST URL FROM STEP 2]

I'm happy to discuss the analysis or provide a shorter brief adapted to your publication format.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**Customization required**:
- [ ] Replace `[INSERT DOMAIN 39 GIST URL FROM STEP 2]` with actual Gist URL from Step 2
- [ ] Replace `[YOUR_NAME]` with your name
- [ ] Replace `[YOUR_CONTACT_INFO]` with your email

**After sending**:
- [ ] Record in Domain 39 Send Log (end of this section)

---

#### Email 2: National Health Law Program

**To**: info@healthlaw.org (or contact form)  
**Timing**: May 30 (same day as Georgetown CCF)  
**Time**: 15 minutes

**Subject**:
```
Democratic participation argument for your work requirement litigation — pre-June 1
```

**Body**:
```
Dear NHeLP team,

Your December 2024 analysis "Unfit to Work? How Medicaid Work Requirements Hurt People with Disabilities" is central to this broader framework, which makes the democratic participation argument that may not be fully developed in your current litigation strategy: healthcare implementation choices are electoral infrastructure decisions.

The specific contribution for your litigation work: Domain 39 documents five causal pathways through which Medicaid coverage loss reduces civic participation — rural hospital closures (3.8 percentage-point turnout penalty per American Political Science Review 2025, 10.5 million rural voters), NVRA voter registration infrastructure degradation at Medicaid offices, medical debt as civic engagement capacity depletion, maternal mortality as permanent civic capacity loss, and disability disenfranchisement through guardianship, PAVA defunding, and work requirements.

This strengthens APA challenges in two specific ways:

First, it expands the documented harms beyond the healthcare domain, making the public interest framing stronger and broader than a welfare benefits argument. District courts are more likely to grant preliminary injunctions when the documented harm encompasses democratic participation, not just health coverage.

Second, it gives courts a democratic infrastructure argument: the HHS work requirement rule is not merely a healthcare policy decision. It degrades the statutory voter registration infrastructure at Medicaid offices (NVRA Section 7), eliminates the PAVA program that makes voting accessible for disabled beneficiaries, and generates documented voter turnout reduction through rural hospital closure. Courts can weigh those harms differently than they weigh coverage loss alone.

The pre-litigation window is June through December 2026, before work requirements take effect January 1, 2027. Organizations that document the democratic participation harms now build the record that courts will need for standing arguments and constitutional claims.

Full analysis (approximately 7,200 words, 47 citations):
[INSERT DOMAIN 39 GIST URL FROM STEP 2]

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**Customization**:
- [ ] Replace `[INSERT DOMAIN 39 GIST URL FROM STEP 2]` with actual Gist URL
- [ ] Replace `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]`

**After sending**:
- [ ] Record in Send Log

---

### Domain 39 Tier 2 Wave (Send June 1)

#### Email 3: Brennan Center for Justice

**To**: Contact form at https://www.brennancenter.org/contact  
**Timing**: June 1 (day HHS rule drops; frame with rule as news hook)  
**Time**: 20 minutes

**Subject**:
```
NVRA enforcement angle on OBBBA Medicaid cuts — for your 2026 election protection framework
```

**Body**:
```
Dear Brennan Center team,

The OBBBA's administrative architecture creates a concrete NVRA Section 7 enforcement opportunity I want to make sure is in your 2026 election protection framework, particularly as the HHS interim final rule on work requirements publishes today.

Medicaid enrollment offices are mandatory voter registration sites under NVRA Section 7 (52 U.S.C. § 20506). The OBBBA's 6-month redetermination cycle — doubled from the prior 12-month standard — and administrative budget compression reduce the capacity of these offices to offer voter registration at precisely the moment enrollment volume increases from coverage churn. Each 6-month redetermination is a new NVRA-mandated voter registration opportunity. In the 42 states without Medicaid Automatic Voter Registration, traditional paper-form compliance already produces only 1.6% uptake, compared to 85-90% in AVR states. Administrative compression will reduce even that minimal compliance.

NVRA Section 7 compliance is privately enforceable. Domain 39 documents the systematic degradation of voter registration infrastructure at Medicaid offices as a consequence of OBBBA implementation — providing the factual record for litigation that treats healthcare infrastructure loss as a voting rights violation, not merely a health policy failure.

A second finding for your election protection briefings: a peer-reviewed study of 10.5 million rural voters (Cox, Epp, and Shepherd, American Political Science Review, August 2025) found 3.8 percentage-point voter turnout reduction in communities affected by hospital closures. The 417 rural hospitals currently classified as vulnerable to closure — concentrated in states that declined Medicaid expansion — carry a documented turnout penalty that your 2026 midterm analysis should incorporate. Rural hospital infrastructure loss is a voter suppression mechanism that your current election protection framework may not yet cover.

Full analysis (approximately 7,200 words, 47 citations):
[INSERT DOMAIN 39 GIST URL FROM STEP 2]

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**Customization**:
- [ ] Replace Gist URL, name, contact info

**After submitting form**:
- [ ] Record in Send Log

---

#### Email 4: Institute for Responsive Government

**To**: Contact form at https://responsivegov.org/contact/  
**Timing**: June 1  
**Time**: 20 minutes

**Subject**:
```
OBBBA impact on Medicaid AVR infrastructure — extends your NVRA-Medicaid research
```

**Body**:
```
Dear Institute for Responsive Government team,

Your research on Medicaid Automatic Voter Registration — particularly the 85% registration rate in Oregon projections versus the 1.6% national NVRA compliance rate — is the empirical foundation for one of the five causal pathways in this analysis, which I wanted to make sure was in your hands before the HHS work requirement rule publishes today.

The framework extends your NVRA-Medicaid research into a five-pathway democratic infrastructure argument that I think strengthens the policy case for your ongoing Medicaid AVR advocacy:

Pathway 2 (the NVRA nexus): The OBBBA's 6-month redetermination cycle doubles the enrollment office administrative burden without any corresponding increase in NVRA compliance capacity. The 50-fold gap between AVR and traditional NVRA compliance that your research documents will widen as enrollment offices are administratively compressed. This is not merely a voter registration efficiency problem — it is a statutory compliance problem with a private right of action under Section 7.

The additional pathways (rural hospital closure voter turnout penalty, medical debt civic capacity depletion, maternal mortality civic voice loss, disability disenfranchisement) provide the coalition argument: Medicaid AVR advocacy should be coordinated with voting rights organizations, disability rights litigators, and reproductive justice coalitions who are fighting for the same communities through different frameworks.

If you are interested in coordinating distribution or incorporating this analysis into your state policy network communications, I would welcome the conversation.

Full analysis (approximately 7,200 words, 47 citations):
[INSERT DOMAIN 39 GIST URL FROM STEP 2]

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**Customization**:
- [ ] Replace Gist URL, name, contact info

---

### Domain 39 Tier 3 Wave (Send June 2–3)

#### Email 5: Black Mamas Matter Alliance

**To**: Contact form at https://blackmamasmatter.org/contact/  
**Timing**: June 2–3 (Tier 3; send after Tier 1 responses assessed)  
**Time**: 20 minutes

**Subject**:
```
Democratic voice argument for your maternal mortality work — coalition bridge to voting rights funders
```

**Body**:
```
Dear Black Mamas Matter Alliance team,

I want to put in front of you an argument that I believe expands your coalition considerably: the communities with the highest maternal mortality rates are communities whose civic voice is most systematically constrained by preventable death.

The historical evidence runs both directions. After women gained the right to vote in 1920, maternal and infant mortality declined significantly. When the Voting Rights Act expanded Black political power in 1965, infant mortality in VRA-covered counties fell by 17.5% in five years (Rushovich et al., American Journal of Public Health, 2024) — through documented mechanisms: increased government funding to high-Black-population counties, reduced racial wage gaps, lower arrest rates. Political power, operationalized through voting rights, improved the health outcomes that determine survival.

That relationship runs in both directions. Black women who die in childbirth cannot vote, run for office, or raise children who will become voters. Preventable maternal mortality depletes the civic voice of communities where political power is already most constrained. The 3.5x Black-white maternal mortality ratio (50.3 vs. 14.5 deaths per 100,000 live births, CDC 2023) is not only a health justice crisis — it is a voter suppression mechanism operating through the body rather than through ballot access rules.

This argument expands your coalition. Voting rights funders who currently do not see maternal health as their issue should — because the same communities whose maternal health outcomes are worst are the communities whose civic voice is most systematically diminished. Domain 39 makes that case with the empirical record that allows the framing to be specific and defensible.

The Momnibus coalition (H.R. 7973, 119th Congress) and voting rights organizations are fighting for the same communities. Domain 39 is the analytical bridge document that makes joint advocacy and joint distribution coherent.

Full analysis (approximately 7,200 words, 47 citations):
[INSERT DOMAIN 39 GIST URL FROM STEP 2]

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

**Customization**:
- [ ] Replace Gist URL, name, contact info

---

### Domain 39 Response Tracking (June 1–4)

**Check email at these intervals**:

| Check | When | What to Look For |
|---|---|---|
| **T+24h** | June 1 (after Tier 1 sends May 30) | First replies from Georgetown CCF, NHeLP |
| **T+48h** | June 2 | Replies to Brennan Center, IRG sends (June 1) |
| **T+72h** | June 4 | Final assessment of Tier 1–2 response rate |

**Response scoring**:
- **Score 5**: Organization offers to distribute, co-author, or partner
- **Score 3**: Substantive engagement with specific argument
- **Score 1**: Generic acknowledgment
- **Score 0**: No reply

**Target**: 2 of 4 Tier 1 organizations reply substantively (Score 3+).

---

### Domain 39 Send Log

| # | Organization | Contact | Sent Date | Sent Time | Gist URL Used | Bounce/Error | Response | Score | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Georgetown CCF | childhealth@georgetown.edu | May 30 | | | | | | |
| 2 | NHeLP | info@healthlaw.org | May 30 | | | | | | |
| 3 | Brennan Center | contact form | June 1 | | | | | | |
| 4 | IRG | contact form | June 1 | | | | | | |
| 5 | Black Mamas Matter | contact form | June 2–3 | | | | | | |

---

## Part C: Integration Logging

### Domain 56 & 39 Combined Execution Log (for DISTRIBUTION_EXECUTION_LOG.md)

After completing all Domain 56 (May 28) and Domain 39 (May 30–June 3) sends, add this entry to `projects/resistance-research/DISTRIBUTION_EXECUTION_LOG.md`:

```
## Domain 56 + Domain 39 Combined Wave — May 28–June 3, 2026

**Domains**: 56 (Civil Service) + 39 (Healthcare Access)  
**Scope**: 4 Domain 56 sends (May 28) + 5 Domain 39 sends (May 30–June 3)  
**Total contacts**: 9 organizations  
**Execution window**: May 28–June 3  

### Domain 56 Tier 2 — May 28 Results

| Organization | Sent | Response | Score | Notes |
|---|---|---|---|---|
| Volcker Alliance | May 28 [time] | | | |
| Democracy Forward | May 28 [time] | | | |
| CREW | May 28 [time] | | | |
| Government Executive | May 28 [time] | | | |

**Domain 56 Outcome**: [STRONG / MODERATE / WEAK] based on response scoring
**Domain 56 Next Action**: [Per synthesis outcome decision tree]

### Domain 39 Tiers 1–3 — May 30–June 3 Results

| Organization | Sent | Response | Score | Notes |
|---|---|---|---|---|
| Georgetown CCF | May 30 [time] | | | |
| NHeLP | May 30 [time] | | | |
| Brennan Center | June 1 [time] | | | |
| IRG | June 1 [time] | | | |
| Black Mamas Matter | June 2–3 [time] | | | |

**Domain 39 Outcome**: [STRONG / MODERATE / WEAK] based on response scoring
**Domain 39 Next Action**: [Per synthesis outcome decision tree]

**Combined Phase 2 Activation**: [Domain 56 + 39 + 58 sequencing per synthesis outcome]
```

---

## Key Dates & Deadlines (Quick Reference)

- **May 28 (this day)**: Domain 39 distribution COMPLETE (internal pre-production only; not public sends)
- **May 28**: Domain 56 all 4 sends COMPLETE
- **May 30**: Domain 39 Tier 1 sends (Georgetown CCF, NHeLP)
- **June 1**: Domain 56 + 39 Tier 2 sends (Brennan Center, IRG; Domain 56 follow-up if applicable)
- **June 3**: Domain 39 Tier 3 send (Black Mamas Matter)
- **May 28–31**: Domain 56 response tracking window
- **June 1–4**: Domain 39 response tracking window
- **June 5**: Combined response assessment; determine Phase 2 next steps per synthesis outcome

---

## Contingency Paths

**If Domain 56 Gist is not live**: Verify URL at https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f. If 404, do not send until you have a working URL. Create new Gist using domain-56-civil-service-politicization.md source document.

**If Domain 39 Gist is not live**: Create it May 27–29 per Step 2. Do not send without a live Gist URL.

**If any email bounces**: Within 24 hours, search organization website for alternative contact (named staff, different email) and resend using same message.

**If contact form is broken**: Search organization website for email or media contact; use direct email instead.

**If response rate is very low** (0 of 4 Domain 56, or 0 of 4 Tier 1 Domain 39) by May 31 / June 4: Review delivery (did emails land in spam?), check for bounces, and determine if re-send or follow-up is warranted per SYNTHESIS_OUTCOME_DECISION_TREE.md contingency sections.

---

*Execution checklist created: May 26, 2026. Synthesis of Session 1645 deliverables (DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md and DOMAIN_39_JUNE1_PRE_PRODUCTION_CHECKLIST.md). All email templates and procedures are production-ready. Ready for May 28 execution.*
