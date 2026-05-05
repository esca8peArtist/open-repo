---
title: "Phase 1 User Execution Checklist"
created: 2026-05-05
status: ready-for-execution
scope: "Step-by-step execution guide for Path A / Path A+37 / Path B immediately after path decision"
references:
  - PHASE_1_EXECUTION_READINESS.md
  - DOMAIN_37_SEQUENCING_PLAN.md
  - BATCH_1_CONTACT_VERIFICATION.md
  - execution/tier-1-contact-batches.md
  - execution/distribution-sequence.md
  - execution/path-a-materials.md
  - execution/path-a-domain37-materials.md
  - execution/path-b-materials.md
  - DISTRIBUTION_GUIDE.md
  - EMAIL_PERSONALIZATION_GUIDE.md
---

# Phase 1 User Execution Checklist

**Written**: May 5, 2026. For use immediately after path decision.

**Infrastructure status at time of writing**: APPROVED FOR PHASE 1 LAUNCH. All production domains verified, all Batch 1 contacts position-verified as of April 29, all distribution templates content-complete. The sole remaining trigger is path selection. Once you select a path, this checklist executes in order.

**Estimated time from path decision to Batch 1 emails sent**: 3-4.5 hours. You do not need to do all of this in one sitting — the natural break point is after Block 3 (Gist creation), when the documents are live and the URL-fill work can continue later.

**How to use this document**: Find your path section. Work through it numbered step by step. Do not skip the decision gates — they exist to catch real-world conditions (a bounced email, a subject line going to spam, a Gist that formatted wrong) before they compound. Mark each step complete as you finish it.

---

## PATH A: IMMEDIATE 35-DOMAIN DISTRIBUTION

**The Path A frame**: You are distributing the complete, production-ready 35-domain framework now. The pitch to all contacts is completeness — 35 domains, 160+ case studies, comparative evidence from 40+ countries. Domain 37 is part of the framework and reaches all contacts in the normal batch sequence; no separate election-protection track is needed.

**Path A is the right choice if**: You want maximum institutional impact in the 2026 midterm window and do not intend to add major domain updates before outreach begins.

---

### BLOCK 1: Gist Creation (30-45 minutes, do first — everything else depends on live URLs)

**What you are doing**: Publishing each canonical document as a public GitHub Gist so it has a permanent, shareable URL. This is the only technical step and the only real blocker. Until these URLs exist, no template can be finalized and no email can be sent.

**Before you start Block 1**, open a blank document or note to record URLs as you create them. You will need them in Block 2.

1. Go to https://gist.github.com. Sign in with your GitHub account.
2. Open `projects/resistance-research/democratic-renewal-proposal.md` locally. Copy all content.
3. In Gist: set filename to `democratic-renewal-proposal.md`. Paste content. Set visibility to **Public**. Click "Create public gist." Copy the URL and paste it into your URL log as: `PROPOSAL_URL = [paste]`.
4. Open `projects/resistance-research/democratic-renewal-executive-summary.md`. Copy all content.
5. In Gist: filename `democratic-renewal-executive-summary.md`. Paste. Public. Create. Record as `EXEC_SUMMARY_URL = [paste]`.
6. Open `projects/resistance-research/litigation-tracker-2026.md`. Copy all content.
7. In Gist: filename `litigation-tracker-2026.md`. Paste. Public. Create. Record as `LITIGATION_URL = [paste]`.
8. Open `projects/resistance-research/first-amendment-suppression.md`. Copy all content.
9. In Gist: filename `first-amendment-suppression.md`. Paste. Public. Create. Record as `FIRST_AMENDMENT_URL = [paste]`.
10. Open `projects/resistance-research/environmental-rollbacks-tracker.md`. Copy all content.
11. In Gist: filename `environmental-rollbacks-tracker.md`. Paste. Public. Create. Record as `ENVIRONMENTAL_URL = [paste]`.
12. Open `projects/resistance-research/police-brutality-consent-decree-tracker.md`. Copy all content.
13. In Gist: filename `police-brutality-consent-decree-tracker.md`. Paste. Public. Create. Record as `CONSENT_DECREE_URL = [paste]`.

**Decision gate after step 13**: Click each of the 6 recorded URLs in a new browser tab. Confirm the page loads, the Gist is public (not private), and the Markdown renders. If a Gist is private, edit it and change visibility to public. If a URL does not load, delete and re-create that Gist. Do not proceed to Block 2 until all 6 URLs open correctly.

---

### BLOCK 2: Template URL Fill-In (20-30 minutes — do after Block 1, can do in parallel with Block 3 if you have your URL log open)

**What you are doing**: Replacing every `[link]` placeholder in the three distribution template files with the actual Gist URLs you recorded in Block 1. The DISTRIBUTION_GUIDE.md "URL Placeholders" section (see table beginning "The 6 documents requiring public URLs") maps which document belongs in which template location.

14. Open `projects/resistance-research/distribution-institutional-outreach-templates.md`.
15. Use find-replace (Ctrl+H or Cmd+H): find `[link to proposal]` — replace with your `PROPOSAL_URL`. Find `[link to executive summary]` — replace with `EXEC_SUMMARY_URL`. Find `[link to litigation tracker]` — replace with `LITIGATION_URL`. Find `[link to first amendment tracker]` — replace with `FIRST_AMENDMENT_URL`. Find `[link to environmental tracker]` — replace with `ENVIRONMENTAL_URL`. Find `[link to consent decree tracker]` — replace with `CONSENT_DECREE_URL`. Any remaining `[link]` instance that you cannot identify — check the DISTRIBUTION_GUIDE.md table for which document it references.
16. Still in `distribution-institutional-outreach-templates.md`: find all `[Your name]` instances. Replace with your preferred name for professional outreach. There are 11 sign-off blocks; confirm all are updated.
17. Find all `[Contact information]` instances. Replace with your email address. Optionally include Signal handle or website if you use them professionally. Confirm all 11 sign-offs are updated.
18. Save `distribution-institutional-outreach-templates.md`.
19. Open `projects/resistance-research/distribution-substack-drafts.md`.
20. Find-replace all `[link]` instances with the appropriate Gist URLs using the same DISTRIBUTION_GUIDE.md table. The Substack drafts primarily use `PROPOSAL_URL` and `EXEC_SUMMARY_URL` in their call-to-action sections. Save the file.
21. Open `projects/resistance-research/distribution-reddit-templates.md`.
22. Find-replace all `[link]` instances. Reddit posts primarily reference `PROPOSAL_URL` and `EXEC_SUMMARY_URL`. Save the file.

**Decision gate after step 22**: Open each of the three template files and search for remaining `[link]` instances. There should be none. If any remain, identify which document they reference and fill them. Also search for `[Your name]` and `[Contact information]` in the outreach templates — there should be none remaining.

---

### BLOCK 3: Batch 1 Contact Email Verification (30-45 minutes — can run in parallel with Block 2)

**What you are doing**: Confirming the exact email address for each of the 5 Batch 1 contacts by visiting their current institutional page. Position verification was completed April 29 — this block is email-address confirmation only, not re-verification of their roles.

**Create your contact log now**: Copy the template from `execution/tier-1-contact-batches.md` (the `CONTACT LOG TEMPLATE` section at the bottom) into a spreadsheet or document. You will fill it as you verify each contact. Fields: Contact, Batch, Date sent, Email subject, Template used, Domains highlighted, Response received, Response date, Response summary, Forwarded/shared, Follow-up sent, Status.

23. For **Ryan Goodman**: visit https://justsecurity.org/author/ryan-goodman/ — look for email in the author bio or "Contact" section. Try `ryan@justsecurity.org` or `ryan.goodman@nyu.edu`. Record the confirmed email in your contact log.
24. For **Wendy Weiser**: visit https://www.brennancenter.org/people/wendy-weiser — confirm `wweiser@brennancenter.org` or the email listed on her staff page. Record confirmed email.
25. For **Erica Chenoweth**: visit https://www.hks.harvard.edu/faculty/erica-chenoweth — confirm `echenoweth@harvard.edu` or the email listed on her faculty page. Record confirmed email.
26. For **Ian Bassin**: visit https://protectdemocracy.org/team/ian-bassin/ — confirm `ian@protectdemocracy.org` or the email listed. Record confirmed email.
27. For **Marc Elias**: visit https://www.democracydocket.com/about/ — try `marc@democracydocket.com` or `melias@perkinscoie.com` (his Perkins Coie address). Check which is currently listed. Record confirmed email.

**Decision gate after step 27**: All 5 contact log rows should have a confirmed email. If any email address could not be confirmed from the institutional website, try: (1) the contact's X/LinkedIn profile for their email, (2) the institutional contact form as the send channel instead of direct email. Do not guess at email format — a bounced email wastes a first-contact opportunity. If you genuinely cannot confirm an email, send via the institution's contact form with the same template, and note "sent via contact form" in the log.

---

### BLOCK 4: Email Personalization — All 5 Batch 1 Contacts (60-90 minutes)

**What you are doing**: Writing the five personalized Batch 1 emails. Use `execution/outreach-email-templates.md` as your template base and `BATCH_1_CONTACT_VERIFICATION.md` for the specific personalization hooks for each contact. The `EMAIL_PERSONALIZATION_GUIDE.md` has structural frameworks by contact type. Do not send a generic email — every contact has a specific domain hook, a specific subject line, and a specific ask.

**For Path A, add this line to every email**: "The complete 35-domain framework is production-ready and available immediately at [PROPOSAL_URL]."

28. **Ryan Goodman email**. Open Template A-1 in `execution/outreach-email-templates.md`. Fill in: Name = "Ryan"; Subject line = "Framework + FISA 702 analysis: judicial independence and surveillance accountability domains" (or variant from `BATCH_1_CONTACT_VERIFICATION.md`). Domain opener: lead with **Domain 6** (judicial independence, 564 documented judicial threats in FY2025) and **Domain 25** (FISA "Fool's Gold" analysis, which Just Security published related coverage on). Personal hook: reference his recent Just Security editorial work on FISA and judicial capture. Specific ask: propose Domain 28/29 as standalone analytical pieces for Just Security, or co-citation in his ongoing DOJ accountability work. Documents to attach or link: Domains 28 and 29 excerpts (extract 5-7 pages from the domain files), plus `EXEC_SUMMARY_URL`. Insert `PROPOSAL_URL` as the full framework link. Fill `[Your name]` and `[Contact information]` in the sign-off. Save this draft — do not send yet.

29. **Wendy Weiser email**. Template A-1. Name = "Wendy"; Subject line = "Framework + April 2026 voting rights crisis: four-state SAVE Act wave + ballot initiatives." Domain opener: lead with **Domain 1** (voting rights — SAVE Act four-state enactment wave in April 2026, Arizona 621K ballot initiative signatures). Personal hook: Brennan Center publications are primary sources in Domain 1's sourcing — establish that direct connection. Specific ask: feedback on Domains 1 and 6, and (once relationship is established) an introduction to Senate Judiciary staff. Documents to link: Domain 1 and Domain 6 Gist links if you have created them; otherwise `PROPOSAL_URL` with a note to see Sections 1 and 6. Fill sign-off. Save draft.

30. **Erica Chenoweth email**. Template A-1. Name = "Erica"; Subject line = "Theory of change feedback: 35-domain framework grounded in Chenoweth nonviolent action research." Domain opener: lead with the framework's resistance meta-analysis and the fact that her 3.5% threshold research is foundational to it. Specific methodological question: whether the 3.5% threshold extrapolates from authoritarian-regime contexts to democratic-backsliding contexts. Personal hook: Harvard's $2.2B funding freeze (Domain 27) — her own institution is documented in the framework. Ask for feedback on the methodology, not endorsement. Documents to link: resistance meta-analysis section (extract from `democratic-renewal-proposal.md`), plus `EXEC_SUMMARY_URL`. Fill sign-off. Save draft.

31. **Ian Bassin email**. Template C (Legal/Institutional) from `execution/outreach-email-templates.md`. Name = "Ian"; Subject line = "Framework + prosecutorial weaponization: domain-29 SPLC analysis and domain-06 judicial threat documentation." Domain opener: lead with **Domain 6** (judicial independence) and **Domain 29** (prosecutorial weaponization, SPLC indictment, April 28 motions). Personal hook: Protect Democracy is co-plaintiff in active institutional cases documented in the framework's litigation tracker. Specific ask: feedback on litigation vehicles and implementation architecture. Documents to link: Domains 6, 29, and 34, and the activation architecture's Phase 1 actions for those domains. Use `PROPOSAL_URL` for the full framework. Fill sign-off. Save draft.

32. **Marc Elias email**. Template B (Media/Journalist) from `execution/outreach-email-templates.md`. Name = "Marc"; Subject line = "DOJ Voter Roll Litigation Documentation (23 Active Cases) + Systematic Election Interference Framework." Domain opener: lead with **Domain 1** redistricting analysis and the litigation tracker's election-related entries. Note Watson v. RNC (mail ballot deadline) and Louisiana v. Callais (VRA) — both expected June-July 2026 decisions that Democracy Docket is tracking. Specific offer: the DOJ voter roll litigation list (23 cases) as a documentation resource for Democracy Docket coverage. Documents to link: Domain 1 and the litigation tracker (`LITIGATION_URL`). Use `PROPOSAL_URL` for the full framework. Fill sign-off. Save draft.

**Decision gate after step 32**: Review all 5 drafts. Check for each: (1) no remaining `[brackets]` anywhere in the text, (2) correct recipient name in salutation, (3) correct domain hook for this specific person, (4) at least one live URL that works, (5) sign-off has your real name and contact. Read each email aloud — if a sentence sounds like a form letter, rewrite it. Form letters go unread.

---

### BLOCK 5: Tracking Infrastructure Setup (20-30 minutes — can run in parallel with Block 4)

**What you are doing**: Setting up the infrastructure to know whether your outreach is working. You cannot course-correct without data.

33. Create your tracking spreadsheet (see the contact log template you copied in step 22). If using Google Sheets: name the file "Phase 1 Contact Log — [your name]." Add tabs: "Tier 1 Contacts," "Tier 2 Contacts," "Social Media," "Response Log."
34. In the "Tier 1 Contacts" tab: pre-fill the 5 Batch 1 rows with the contact names, batch number (1), and template type, leaving the send-date and response columns blank for now.
35. Choose your email tracking method. Options in order of ease: (a) **Streak CRM** — free Gmail extension, tracks opens and link clicks per email, installs in 5 minutes; (b) **Mailtrack** — free Gmail extension, shows read receipts; (c) no tracking — rely on reply-based tracking only. Install whichever you choose before sending.
36. Create a folder in your email client labeled "Phase 1 Outreach — Responses." Set a rule to move any reply from the 5 Batch 1 domains (justsecurity.org, brennancenter.org, harvard.edu, protectdemocracy.org, democracydocket.com, perkinscoie.com) into this folder automatically. This prevents responses from getting lost in your inbox.
37. Set a calendar reminder for Day 5 (from today) and Day 8 (from today): "Check Batch 1 response status and launch Batch 2 prep."
38. Set a calendar reminder for Day 3 (from today): "Publish social media posts."

---

### BLOCK 6: Send Sequence — Batch 1 (15-20 minutes — do on launch morning)

**What you are doing**: Sending all 5 emails in a specific order within a 4-hour window. The order is strategic (see `execution/tier-1-contact-batches.md` for the rationale), not arbitrary.

**Optimal send time**: Tuesday or Wednesday morning, 9:00-11:00 AM Eastern time. If your decision day is neither, do not wait — send on the next available Tuesday or Wednesday that is within 3 days of your path decision. Do not hold the launch for the perfect day.

39. Open your Goodman email draft. Final check: subject line is correct, link to `PROPOSAL_URL` works, sign-off is complete. Send. Log in contact log: Date sent = today, time = now.
40. Wait 25-30 minutes. Open your Weiser email draft. Final check. Send. Log.
41. Wait 25-30 minutes. Open your Chenoweth email draft. Final check. Send. Log.
42. Wait 25-30 minutes. Open your Bassin email draft. Final check. Send. Log.
43. Wait 25-30 minutes. Open your Elias email draft. Final check. Send. Log.

**Decision gate after step 43**: Confirm all 5 entries in your contact log show a send date and time. That is your T-Day 0 record. Phase 1 is in flight.

---

### BLOCK 7: Social Media Queue — Schedule and Publish (60-90 minutes — T+Day 1 to T+Day 3)

**What you are doing**: Scheduling the three social media channels to go live in a staggered sequence after the institutional emails have had time to land.

44. **X/Bluesky thread — schedule for T+Day 2** (two days after your Batch 1 send). Open `distribution-substack-drafts.md` and find the X/Bluesky thread draft. Copy the text. Open your X or Bluesky drafts. The thread opening for Path A: "Of 25 countries with significant democratic backsliding since 1990, four have recovered. The variables: elite defection, parallel institutions, mass mobilization above 3.5%, and a blueprint. Here is the blueprint — 35 domains, primary sourced, free to use. [PROPOSAL_URL]". Add the remaining thread posts. Schedule for 9:00 AM Eastern on T+Day 2.
45. **Reddit posts — schedule for T+Day 3**. Open `distribution-reddit-templates.md`. There are 4 subreddit-customized posts. Read each one for Path A framing — the hook is "comprehensive diagnostic framework, 35 domains, CC 4.0." Do not cross-post identically. Confirm each post's subreddit framing is appropriate (r/PoliticalScience = academic framing; r/USPolitics = more accessible summary; r/LegalAdvice = litigation tracker lead; r/dataisbeautiful = fiscal analysis tables). Stage each as a Reddit draft or in a scheduler (e.g., Buffer free tier). Plan to publish at 10:00 AM Eastern on T+Day 3.
46. **Substack post — schedule for T+Day 3**. Open `distribution-substack-drafts.md`, Post 1 (executive summary post). The Path A title: "35 Structural Failures in American Democracy — A Comprehensive Diagnostic Framework." Review the draft and insert `EXEC_SUMMARY_URL` and `PROPOSAL_URL` in the call-to-action sections. If any Batch 1 contact has responded positively by T+Day 2, add a one-sentence note at the top: "Since circulating this among policy and academic contacts, I've received feedback from [name/institution if they've agreed to be named]." If no responses yet, publish without that note — do not fabricate. Schedule for noon Eastern on T+Day 3.
47. Confirm all three platforms have active accounts and you can log in before scheduling. If a social account has been dormant, post a brief introductory note first so the algorithm treats the account as active.

---

### BLOCK 8: Post-Send Monitoring and Batch 2 Preparation (Days 4-8)

**What you are doing**: Tracking Batch 1 responses and using what you learn to personalize Batch 2 before sending it on Day 8.

48. **Day 4**: Check your email tracking (open rates if using Streak/Mailtrack). Check the "Phase 1 Outreach — Responses" folder. Log any responses in your contact spreadsheet under "Response received = yes," "Response date = [date]," "Response summary = [one sentence]." If Ryan Goodman responds with interest in a Just Security piece: reply within 24 hours, offer Domain 28 or 29 as a standalone submission. If Erica Chenoweth responds: reference her engagement in every subsequent Batch 2 and 3 email. If Wendy Weiser or Brennan Center responds: follow up within 24 hours; the ask is feedback on Domains 1 and 6 and, once established, an introduction to Senate Judiciary staff.
49. **Day 5**: If no opens detected and no responses, check whether any of your 5 emails landed in spam by searching the recipient's domain in your sent folder and cross-referencing with your email tracking. If 0 of 5 have been opened by Day 5, your subject lines may be triggering spam filters — consider sending Batch 2 from a different email account or adjusting subject lines to remove any trigger phrases.
50. **Day 7**: Begin personalizing the 8 Batch 2 emails (Michael Waldman, Phil Brest, Dick Durbin staff, Sheldon Whitehouse staff, Jack Balkin, Quinta Jurecic, Zack Beauchamp, Janai Nelson — see `execution/tier-1-contact-batches.md` BATCH 2 section for detailed guidance on each). If any Batch 1 responses exist, begin each Batch 2 email with a reference: "Since distributing the framework, I have engaged with [institution] on the [domain] analysis..." Even one institutional response transforms cold outreach into warm outreach.
51. **Day 8**: Send all 8 Batch 2 emails. The send order for Batch 2: Day 8 — Michael Waldman (Brennan Center), Phil Brest (ACS), Dick Durbin staff; Day 9 — Sheldon Whitehouse staff, Jack Balkin (Yale), Quinta Jurecic; Day 10 — Zack Beauchamp (Vox), Janai Nelson (NAACP LDF). Log each in your contact spreadsheet.

---

### PATH A CONTINGENCY PLANNING

**If a Batch 1 email bounces**: Use the contact's institutional form (all 5 organizations have public contact forms). Re-send the same email via the form. Note "sent via contact form" in your contact log. The email still counts as a Batch 1 send.

**If open rate is 0 of 5 by Day 5**: One or more emails may be in spam. Try: (1) send one test email to yourself from the same account — if it lands in your own spam, your email domain may be flagged; (2) switch to a Gmail account for outreach if your current email is domain-hosted and misconfigured; (3) shorten the subject line — subject lines over 60 characters are more likely to trigger filters.

**If response rate after Batch 1 is 0 of 5 by Day 8**: Still send Batch 2. Academic and policy professionals respond on 1-3 week timelines. Do not treat non-response as rejection. Adjust Batch 2 subject lines based on which of the alternative subject line options from `BATCH_1_CONTACT_VERIFICATION.md` you did not use for Batch 1, and test those. Log the adjustment.

**If a Batch 1 contact responds negatively**: Log the response with their specific objection. Check `execution/objection-responses.md` for the documented responses to 12 common objections. If the objection is novel, note it — it is feedback about where the framework's framing is unclear. Do not argue in the reply; acknowledge the concern and, if appropriate, ask what would make the research more useful to them.

**If Ryan Goodman or Quinta Jurecic asks for a Just Security or Atlantic submission**: This is a high-priority response. Draft the submission within 48 hours, using the specific domain (28 or 29) that connects to their current editorial beat. See `execution/path-a-materials.md` "Path A Target Media Outlets" for the pitch framing.

---

## PATH A+37 HYBRID: RECOMMENDED PATH

**The Path A+37 frame**: You are distributing the complete 35-domain framework immediately, with Domain 37 (Federal Executive Interference in the 2026 Midterms) integrated into all general outreach — and you are also running a separate, second-wave targeted distribution of Domain 37 specifically to election-protection organizations beginning at Week 3. The two tracks are parallel, not sequential. General contacts get the full 35+1 framework now. Election-protection organizations get Domain 37 separately, after enough general-distribution credibility has been established to make that outreach warm.

**Path A+37 is the right choice if**: You want the urgency and operational specificity of Domain 37's five advocacy windows (May 30, June 30, August 7, September, October) to lead the outreach — and you want to reach election-protection organizations who can act on those windows before they close.

**Critical date check before starting**: Look at today's date. The May 30 advocacy window (DOJ consent decree finalization) is the first window in Domain 37 Section 6. If today's date is within 14 days of May 30, move Wendy Weiser (Brennan Center) and Marc Elias (Democracy Docket) to the front of your Batch 1 send order instead of Ryan Goodman — they are the election-protection contacts with the most direct stake in the May 30 window. If May 30 has already passed, the June 30 emergency EO routing window is your lead advocacy framing for all Domain 37 outreach.

---

### BLOCK 1A: Gist Creation — 7 Documents (35-45 minutes)

**Same as Path A Block 1, plus one additional Gist for Domain 37.**

1-13. Complete steps 1-13 from Path A Block 1 exactly as written. Record all 6 URLs.

14a. Open `projects/resistance-research/domains/domain-37-federal-executive-interference-2026-midterms.md`. Copy all content (8,857 words, 472 lines, 50 citations).
15a. In Gist: filename `domain-37-federal-executive-interference-2026-midterms.md`. Paste. Public. Create. Record as `DOMAIN_37_URL = [paste]`.

**Decision gate**: Click `DOMAIN_37_URL` in a new tab. Confirm it loads, is public, and renders correctly. You should see the five-mechanism structure and the five advocacy windows in Section 6. If the Gist truncated (very long documents occasionally truncate in Gist), consider splitting it into a Part 1 and Part 2 Gist, or hosting it on a Substack page instead.

---

### BLOCK 2A: Template URL Fill-In — Including Domain 37 (25-35 minutes)

16a. Complete steps 14-22 from Path A Block 2 exactly as written, filling the same 6 document URLs in the three template files.
17a. Additionally: in `distribution-institutional-outreach-templates.md`, find any references to Domain 37 (search for "Domain 37" — these are the election-protection-specific template sections). Insert `DOMAIN_37_URL` in those specific `[link]` placeholders.
18a. In `distribution-substack-drafts.md`: find the Domain 37 post draft (it may be labeled "Post 17" or "Domain 37 Substack Post" depending on the draft structure). Insert `DOMAIN_37_URL` in its call-to-action. Insert `EXEC_SUMMARY_URL` and `PROPOSAL_URL` in the framework reference sections.
19a. Save all three template files.

**Decision gate**: Search for remaining `[link]` instances in all three files. There should be none. Search for remaining `[Your name]` and `[Contact information]` — there should be none.

---

### BLOCK 3A: Domain 37 Integration Verification (15 minutes — do before email personalization)

**What you are doing**: Confirming that Domain 37 is correctly integrated into the general framework so that every Batch 1 contact receives a framework that includes it.

20a. Open `democratic-renewal-proposal.md`. Search for "Domain 37." Confirm it appears in the domain table of contents and is described there with the federal executive interference framing. If it does not appear, add a one-line entry for Domain 37 to the table: "Domain 37: Federal Executive Interference in the 2026 Midterms — CISA destruction, personnel network, DOJ voter roll litigation, HSGP conditionality, EAC capture. [DOMAIN_37_URL]." Do not modify the substantive content of existing domains.
21a. Open `ACTIVATION_ARCHITECTURE.md`. Confirm Domain 37 appears in the Phase 1 implementation table. If it does not, add one row: "Domain 37 | Federal Executive Interference | High | Time-sensitive (May 30, June 30, Aug 7, Sep, Oct 2026) | [DOMAIN_37_URL]."
22a. Check the current date against the five advocacy windows in Domain 37 Section 6. Identify which window is the most immediately actionable based on today's date. Write this down: "Current lead advocacy window: [window name and date]." You will use this in every Domain 37 email.

---

### BLOCK 4A: Email Personalization — All 5 Batch 1 Contacts, Path A+37 Framing (75-95 minutes)

**Same structure as Path A Block 4, with Domain 37 added to every email.**

23a. **Path A+37 addition to every Batch 1 email**: After your domain-specific opening, add one paragraph: "The 35-domain framework includes Domain 37 — Federal Executive Interference in the 2026 Midterms — which documents the federal election infrastructure dismantling and five specific advocacy windows before November. I'm distributing Domain 37 separately to election-protection organizations; this email contains the full framework including it. [DOMAIN_37_URL]." This paragraph appears in all five emails.

24a. **Ryan Goodman email**: Complete step 28 from Path A Block 4. Add the Domain 37 paragraph from step 23a. For Goodman specifically: in the Domain 37 paragraph, add "Domain 37's CISA documentation may be relevant to Just Security's national security coverage — the ProPublica CISA investigation cited in Domain 37 overlaps with your war powers beat."

25a. **Wendy Weiser email**: Complete step 29 from Path A Block 4. Add the Domain 37 paragraph. For Weiser specifically: "The May 30 advocacy window in Domain 37 — DOJ consent decree finalization — is directly relevant to Brennan Center's litigation work. If the current date is within 14 days of May 30, lead the Domain 37 paragraph with this: 'The most time-sensitive finding in Domain 37 is the May 30 DOJ consent decree finalization window — I'm distributing this to Brennan Center first because your team can act on it most directly.'"

26a. **Erica Chenoweth email**: Complete step 30 from Path A Block 4. Add the Domain 37 paragraph. For Chenoweth: "Domain 37's analysis of election infrastructure dismantling connects to your research on civil resistance environments — the mechanism by which federal agencies are captured before elections affects the institutional infrastructure that resistance movements depend on."

27a. **Ian Bassin email**: Complete step 31 from Path A Block 4. Add the Domain 37 paragraph. For Bassin: "The HSGP grant conditionality section of Domain 37 (Section 4) documents the legal mechanism Protect Democracy is best positioned to challenge — the specific statutory provisions used to leverage state and local election officials are there."

28a. **Marc Elias email**: Complete step 32 from Path A Block 4. Add the Domain 37 paragraph. For Elias: Lead the Domain 37 paragraph with the 23 active DOJ voter roll cases: "Domain 37 Section 3 documents 23 active DOJ cases challenging voter roll maintenance requirements in competitive 2026 districts — I offer this to Democracy Docket as a documentation resource for your litigation tracking."

**Decision gate after step 28a**: Review all 5 drafts. Every email should contain: (a) a domain-specific personal hook, (b) the Domain 37 integration paragraph with `DOMAIN_37_URL`, (c) `PROPOSAL_URL` as the full framework link, (d) your name and contact in the sign-off, (e) no remaining bracket placeholders.

---

### BLOCKS 5A and 6A: Tracking Setup and Send Sequence

29a. Complete steps 33-43 from Path A Blocks 5 and 6 exactly as written. The send order is the same, unless the May 30 window is within 14 days (in which case Weiser moves to second send and Elias moves to first — see the date check note at the top of this path).

30a. Additional log entry for Domain 37: After logging each Batch 1 send, add a separate entry: "Domain 37 Phase B outreach — queued for Week 3. Target first send: [date 21 days from today]." This is your reminder that the election-protection track begins at Week 3.

---

### BLOCK 7A: Social Media Queue — Path A+37 Additions (70-95 minutes)

31a. Complete steps 44-46 from Path A Block 7, with these additions:

32a. **Additional X/Bluesky thread — schedule for T+Day 5**: Post a Domain 37-specific thread. Opening: "CISA — the federal agency responsible for election security — has been given a $700M budget cut and had its career cybersecurity staff fired before the 2026 midterms. This is documented. The personnel network that replaced them is mapped. Here is the primary source documentation: [DOMAIN_37_URL]." Add 3-4 follow-up posts with specific findings (ProPublica personnel network, 23 DOJ voter roll cases, HSGP conditionality mechanism, five advocacy windows). Schedule for T+Day 5, 9:00 AM Eastern.

33a. **Additional Substack post — draft for T+Day 7**: Post title: "Domain 37: Federal Election Infrastructure Dismantling — Five Advocacy Windows Before November 2026." Content: Domain 37 core findings in Substack-accessible format (not the full 8,857-word document — a 1,000-1,500 word summary with links to the full Gist). This post goes live after election-protection organizations have received the full document (Days 1-7), then general audiences see the summary. Draft this post now; publish on T+Day 7.

---

### BLOCK 8A: Domain 37 Phase B Preparation — Week 2 (Days 8-14)

**What you are doing**: While Batch 2 general outreach is in flight, preparing the Domain 37 targeted election-protection track for launch at Week 3.

34a. **Day 8**: Open `DOMAIN_37_SEQUENCING_PLAN.md`. Read the Phase B contact list (Tier 1: Brennan Center Democracy Program, Democracy Docket, Protect Democracy, Lawyers' Committee VRP, ACLU Voting Rights, States United, Common Cause). Note that Brennan Center, Democracy Docket, and Protect Democracy are already in your Batch 1/2 general outreach. For those three: your Phase B Domain 37 outreach is a follow-up to the general outreach, not a separate cold contact. For Lawyers' Committee VRP, ACLU Voting Rights, States United, and Common Cause: these are new contacts in the Phase B track.

35a. **Day 10-11**: Personalize the 4 Domain 37-new Tier 1 contacts using Template D37-1 from `DOMAIN_37_SEQUENCING_PLAN.md`. For each: insert their organization name, their specific section of Domain 37 most relevant to their work (see the "Domain 37 Value" column in the DOMAIN_37_SEQUENCING_PLAN.md Tier 1 table), and the current lead advocacy window. Insert `DOMAIN_37_URL` and `PROPOSAL_URL`. Fill sign-off. Save drafts — do not send yet.

36a. **Day 14**: Assessment gate from `DOMAIN_37_SEQUENCING_PLAN.md`: Has Phase A established enough institutional credibility for Domain 37 Phase B to land as warm outreach rather than cold outreach? Criteria: (a) At least 2-3 institutional responses from general Batch 1-2 contacts; (b) the current advocacy window is still open (check today's date against the five windows). If both criteria are met: proceed to Phase B launch at Day 21. If institutional responses are below 2: defer Phase B by 7 days. Better to wait 7 days for credibility than to send Domain 37 to election-protection organizations as a cold pitch.

---

### BLOCK 9A: Domain 37 Phase B Launch — Week 3 (Days 21-24)

37a. **Day 21**: Send Domain 37 Phase B Tier 1 Wave 1 (3 contacts: Brennan Center follow-up if already contacted / Lawyers' Committee VRP / ACLU Voting Rights). Send order: Lawyers' Committee VRP first (voting@lawyerscommittee.org), ACLU Voting Rights second (voting@aclu.org), States United Democracy Center third (statesunited.org/contact). For Brennan Center (Wendy Weiser) and Protect Democracy (Ian Bassin): these are follow-ups to Batch 1 general outreach, so your Phase B email begins: "I'm following up on my earlier message with a more targeted briefing on Domain 37 specifically, given [their organization's] work on election protection..." Insert `DOMAIN_37_URL` and the current advocacy window framing.

38a. **Day 22**: Send Domain 37 Phase B Tier 1 Wave 2 (Common Cause — commoncause.org contact). Use Template D37-1 adapted for Common Cause: lead with Domain 37 CISA destruction and August 7 primary stress-testing window (Advocacy Window 3 — most relevant to Common Cause's election protection operations).

39a. **Day 24**: Log all Phase B sends in your contact spreadsheet under a separate "Domain 37 Phase B" tab. Fields: Organization, Contact, Send date, Advocacy window highlighted, Template version, Response, Notes.

---

### PATH A+37 CONTINGENCY PLANNING

**If May 30 window closes before Phase B launches**: Pivot to June 30 (emergency EO routing window) as the lead framing in all Domain 37 Phase B emails. Update every unsent Domain 37 draft to replace the May 30 reference with "June 30 — the emergency executive order routing window, which represents an administrative law challenge opportunity before July." The June 30 window is the second-most time-sensitive advocacy hook.

**If a Phase B election-protection contact already received a general framework email (via Batch 1-3)**: Do not send a duplicate first-contact. Instead: send a Domain 37 follow-up email that begins "Following up on the 35-domain framework I shared earlier — I'm distributing Domain 37 separately to election-protection organizations because the advocacy windows are time-sensitive. [DOMAIN_37_URL]." This is not a duplicate; it is a domain-specific supplement to the earlier general outreach.

**If the DOMAIN_37_URL Gist truncates or does not render well**: Host the document as a Substack page (not a post — a page, which is unlisted and accessible by URL). Use the Substack page URL as your `DOMAIN_37_URL`. Substack handles large Markdown documents more reliably than Gist for documents over 500 lines.

**If Domain 37 Phase B produces no responses by Day 30**: The election-protection community may not be engaging because the advocacy windows feel abstract or because the organization lacks bandwidth. Adjust: send a domain-specific excerpt (extract Section 6 "Five Advocacy Windows" as a standalone 2-page document) as a follow-up to non-respondents. A focused 2-page action document is harder to defer than an 8,000-word analytical brief.

---

## PATH B: CONTENT UPDATES BEFORE DISTRIBUTION

**The Path B frame**: Before distributing at full scale, you will complete targeted updates to specific domains, then execute Phase A distribution with an enhanced rolling-release model. Path B does not delay Batch 1 institutional outreach — it delays the public social media launch and frames the framework as ongoing research in progress.

**Path B is the right choice if**: You want to update specific domains before the framework is fully public, you intend to continue producing Phase 2 expansion domains, and you prefer positioning the research as ongoing scholarship rather than a completed product.

**What "Path B updates" covers**: Five domains were identified as candidates for pre-distribution updates (Domains 1, 21, 25, 33, and 19). You do not have to update all five — the domains are in priority order. Update Domain 25 first (FISA vote outcome is pending as of late April; the Senate outcome fills Domain 25 Section 7 automatically and requires no research). Then Domain 1 (SAVE Act Senate companion status). Then Domain 19 (Iran WPR post-May 1 outcome). Domains 21 and 33 are lower priority — update them if time allows, but do not hold distribution for them.

---

### BLOCK 1B: Priority Domain Updates (Time variable — 1-3 hours depending on domains selected)

1b. **Domain 25 update (FISA Senate outcome) — 30-45 minutes**: Open `projects/resistance-research/domains/domain-25-*.md` (the surveillance/FISA domain). Go to Section 7 (the checklist for post-Senate-vote filling). Find the items: "Senate vote count on S.4344," "date of presidential signature," "whether CBDC ban survived." Look up the current Senate FISA status (Senate cloture was set for no later than May 1 via Thune UC agreement; the vote outcome is now known). Fill the three Section 7 checklist items with the actual vote count, signature date (if signed), and CBDC provision outcome. Add a one-sentence update to the Section 7 opening: "Updated [date]: Senate passed S.4344 [vote count] on [date]; presidential signature [date if signed / pending if not]." Save the file.

2b. **Domain 1 update (SAVE Act Senate companion) — 20 minutes**: Open `projects/resistance-research/domains/domain-01-voting-rights-elections.md`. Find Section 2 (SAVE Act analysis). The Senate companion bill status as of April 29 was the 48-50 defeat with four GOP defectors. Check whether any subsequent Senate action has occurred. If the status is unchanged, add a one-sentence confirmation in Section 2.2: "As of [date], no further Senate action on the SAVE Act companion — the 48-50 defeat on April [date] remains the most recent status." If new Senate action has occurred, document it with the vote count and source URL.

3b. **Domain 19 update (Iran WPR post-May 1 outcome) — 30-45 minutes**: Open `projects/resistance-research/domains/domain-19f-*.md`. Find Section 15 (the three-scenario framework: peace / frozen conflict / resumed hostilities). The scenario framework was built in anticipation of the May 1 outcome. Identify which scenario materialized (look up current Iran-related news to determine whether the 60-day WPR clock produced a peace agreement, a frozen situation, or resumed hostilities). Fill Section 15 with: "Outcome (as of [date]): [scenario name]. [One paragraph documenting the actual development with source URL]." Note which sub-scenario within that scenario matches most closely.

4b. **Domain 33 update (state autocratization, ballot suppression wave) — 20 minutes, optional**: Open `projects/resistance-research/domains/domain-33-*.md`. The domain documented a 155-bill count as of April. Check whether the count has changed materially (any significant new state enactments or legislative defeats since April). If the count has changed by more than 5 bills in either direction, update the figure with a source. If unchanged or minor changes, add a one-sentence note: "As of [date], the bill count stands at [current count] — see [source] for current tracking."

5b. **Domain 21 update — 20 minutes, optional**: Open `projects/resistance-research/domains/domain-21-*.md`. Identify whether any new developments since the domain was last updated are significant enough to warrant an update. If the domain is current (no major developments in the relevant policy area since its last update date), no action needed. If a significant new development exists, add it in the appropriate section with a source URL.

**Decision gate after step 5b**: You do not need to update all five domains before proceeding. The minimum viable update set for Path B is: Domain 25 (fills automatically from public information, 30 minutes) + Domain 19 (fills scenario framework, 30-45 minutes). That is 60-75 minutes of domain updates. Once those two are complete, Path B proceeds to distribution with the same infrastructure as Path A. Domains 1, 33, and 21 updates are improvements, not requirements.

---

### BLOCK 2B: Gist Creation for Path B (Same as Path A Block 1)

6b. Complete steps 1-13 from Path A Block 1 exactly as written. The updated domain files are not published as separate Gists — they are part of the main proposal document. If you have made updates to domain files, confirm the changes are reflected in `democratic-renewal-proposal.md` before creating the Proposal Gist. (If the domain files are separate from the proposal, the proposal's domain list should reference them — check that the domain description in the proposal reflects any material changes you made in Block 1B above.)

7b. If you are running Path B with Domain 37 (Path B+37): also complete step 14a-15a from Path A+37 Block 1A to create the `DOMAIN_37_URL` Gist.

---

### BLOCK 3B: Path B Messaging — Frame the Research as Ongoing

**What you are doing**: Adjusting the messaging architecture in your distribution templates to reflect the "ongoing framework deepening" frame that distinguishes Path B from Path A.

8b. Open `execution/path-b-materials.md`. Read the "Path B Messaging Architecture" section completely. The three frames are: (1) "Ongoing Framework Deepening," (2) "Sustained Engagement for Long-Term Impact," (3) Subscriber-building. You will apply these frames in the next steps.

9b. In `distribution-institutional-outreach-templates.md`: find the call-to-action section of each of the 11 templates. Replace "The complete 35-domain framework is available at [link]" with "The 35-domain framework is available in full at [PROPOSAL_URL], with Phase 2 expansion domains being published on a rolling schedule over the coming months. If you prefer to follow the research as it develops, [Substack link] is the easiest way to stay current." (Use your actual Substack URL if your Substack is live; if not, remove the Substack line.)

10b. In `distribution-substack-drafts.md`: find Post 1 and replace the title with "A 35-Domain Framework for Democratic Renewal — Beginning the Serial Publication." Replace the post's first paragraph with the Path B version from `execution/path-b-materials.md` T-Day 0 section: "This newsletter begins a serialized publication of a two-year research project: a 35-domain framework for democratic structural reform..."

11b. Save both files.

---

### BLOCK 4B: Email Personalization and Contact Verification for Path B

12b. Complete steps 23-32 from Path A Block 4 exactly as written, with this single substitution in every email: the call-to-action sentence changes from "The complete framework is ready for immediate use" to "The framework is structured to incorporate institutional feedback — your input would inform the Phase 2 expansion priorities." This positions Path B as collaborative and ongoing rather than complete and final.

13b. Also add to every Batch 1 email: "I'm releasing additional domains on a rolling schedule — the first Phase 2 expansion domain will be released approximately [date 25-30 days from today]. If you prefer to receive each release as it publishes rather than the full framework at once, [Substack link] is the most efficient channel." (Fill in your estimated Phase 2 release date and Substack URL.)

14b. Contact verification for Path B: same as Path A steps 23-27. Position verification is complete (April 29). Email verification is the only action needed.

---

### BLOCK 5B: Tracking Setup and Rolling Release Calendar

15b. Complete Path A steps 33-38 (tracking spreadsheet, email tracking tool, response folder, calendar reminders).

16b. Add to your tracking spreadsheet a "Phase 2 Release Calendar" tab. In it, set the following tentative dates: Phase 2 Release 1 = T+Day 28; Phase 2 Release 2 = T+Day 42; Phase 2 Release 3 = T+Day 63. These are the rolling release milestones documented in `execution/path-b-materials.md`. You do not need to know which specific domain goes into each release slot now — these dates are placeholders that create the publishing rhythm. Identify which Phase 2 domain is closest to ready by reviewing `phase-2-expansion-candidates.md` or `phase-2-expansion-roadmap.md` (if those files exist) before Day 28.

17b. Set a calendar reminder for Day 25: "Confirm Phase 2 Release 1 domain is ready — if not ready, select backup domain or delay release to Day 35." Do not announce a release date you cannot meet. If a Phase 2 release will miss its scheduled date, send a brief note to Substack subscribers ("The next domain analysis is taking additional time — expected release [new date]"). Missing a scheduled release without notice damages the subscription relationship more than a brief delay.

---

### BLOCK 6B: Send Sequence and Social Media — Path B

18b. Complete Path A steps 39-47 exactly as written. The send timing, order, and platforms are identical. The only difference is in the Substack post content (Path B version from step 10b) and the call-to-action framing in each email (Path B version from step 12b-13b).

19b. After posting the T+Day 3 social media content: set your Path B social media cadence. Between Phase 2 releases, you will post: (a) one domain-specific thread on X/Bluesky every 5-7 days, drawing from existing domain content (format: "One finding from Domain [X]: [specific finding with number]. Primary documentation: [PROPOSAL_URL]"); (b) one brief Substack "research note" between full domain releases (300-500 words on a new development that connects to an existing domain). These between-release posts maintain momentum. Block 2 hours per week for this cadence in your calendar.

---

### BLOCK 7B: Post-Send Monitoring and Path B-Specific Response Handling

20b. Complete Path A steps 48-51 (Days 4-8 response monitoring and Batch 2 preparation). Path B-specific addition: for every Batch 1-2 contact who responds, note in your response log whether they expressed interest in the rolling release format or in receiving Phase 2 domains as they publish. Contacts who say "I'd like to see the next domain when it's ready" are Path B's most valuable signal — they are signaling sustained engagement, not just one-time engagement.

21b. For contacts who respond positively to the rolling-release framing: send a follow-up on Phase 2 Release Day (Day 28): "The first Phase 2 expansion domain is now available — [domain name]. [Gist URL]. This continues the framework's [relevant theme] analysis." This re-engagement email is brief (3-5 sentences), not a full re-pitch. It reminds them the research is active without overwhelming them.

---

### PATH B CONTINGENCY PLANNING

**If a Phase 2 domain is not ready at the scheduled release date**: Select the next most-ready domain from `phase-2-expansion-candidates.md`, or publish a longer Substack research note (1,000-1,500 words) on a significant new development instead. Maintain the release cadence even if the specific content shifts. The cadence is what keeps subscribers engaged.

**If the rolling-release format generates confusion** (contacts asking "is this a finished document or not?"): Address it directly in your next email. The answer: "The 35-domain base framework is complete and final — each domain is fully researched and sourced. The Phase 2 expansion domains are additional research being published as they are completed. Think of the base framework as the complete diagnostic; Phase 2 as deepening specific domains based on new developments and contact feedback."

**If Batch 1 response rate is below 20% by Day 8**: Path B's feedback loop framing may not be landing — the "please give feedback" ask can read as low-confidence to policy professionals. Adjust Batch 2 messaging to be more direct about what exists: "The 35-domain framework is complete and sourced. I'm reaching out to your institution specifically because [Domain X] directly overlaps with your current work. I welcome feedback, but the primary value is the research itself." Shift away from the feedback-invitation framing toward the substantive-content framing.

**If you decide to abandon Path B and shift to Path A during execution**: This is a legitimate course correction. If by Day 14 it is clear that the rolling-release model is not generating engagement and the framework's completeness would be a stronger credibility signal, you can switch. To switch: update the Substack post to remove the "serial publication" framing and replace with the Path A "complete diagnostic" framing. Send Batch 2 and 3 with the Path A call-to-action. The institutional outreach is identical regardless — only the framing shifts.

---

## UNIVERSAL CONTINGENCY: WHAT TO DO WHEN THINGS DEVIATE

These apply across all three paths.

**If a contact's email address cannot be confirmed**: Use the institutional contact form. Every organization in the Tier 1 contact list has a publicly accessible contact form. The email still counts as sent; the contact form route is fully legitimate for first-contact outreach.

**If an advocacy window closes before you reach election-protection contacts**: Update the window framing in all unsent Domain 37 emails to the next open window. The windows are: May 30 (DOJ consent decrees), June 30 (emergency EO routing), August 7 (primary data), September (pre-election litigation), October (operational readiness). If May 30 has closed, June 30 is the lead. If June 30 has closed, August 7 is the lead. The framework does not expire — it simply emphasizes whichever window is next.

**If the Gist URLs change or become inaccessible**: Re-create the Gist and update all unsent emails. For emails already sent: if a contact has clicked a dead link, a brief follow-up is appropriate: "I'm re-sending the framework link — the previous link had a hosting issue. Updated URL: [new URL]." One follow-up for a technical issue is entirely normal.

**If a contact introduces you to a colleague**: This is your highest-value outcome. Reply to the introduction within 24 hours. Send the same email you would have sent to the original contact, personalized for the colleague's specific role and institution. Log the colleague in your contact spreadsheet as a "warm referral" with higher expected response probability than a cold contact.

**If media pickup occurs before Week 2**: This is a positive outcome, not a disruption. Update your Batch 2 and 3 emails to reference the media coverage: "A brief note — [publication] mentioned the framework [where and when]. I wanted to follow up while it's top of mind." This transforms all subsequent outreach from cold to warm.

**If Tier 1 response rate is above 40% by Day 14**: This is a strong signal. Proceed immediately to Tier 2, do not wait until Day 25. The momentum window is open — act within it. Pull forward your Tier 2 contact list from `execution/distribution-sequence.md` T+Week 3 section and begin personalization immediately.

---

*Last updated: May 5, 2026. File path: `projects/resistance-research/phase-1-execution-checklist.md`. Sources: PHASE_1_EXECUTION_READINESS.md, DOMAIN_37_SEQUENCING_PLAN.md, BATCH_1_CONTACT_VERIFICATION.md, execution/tier-1-contact-batches.md, execution/distribution-sequence.md, execution/path-a-materials.md, execution/path-a-domain37-materials.md, execution/path-b-materials.md, DISTRIBUTION_GUIDE.md, EMAIL_PERSONALIZATION_GUIDE.md.*
