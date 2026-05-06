---
title: "Phase 1 Launch Risk Mitigation and Response Playbook"
created: 2026-05-06
status: production-ready
applies_to: "All three distribution paths (A, A+37, B). Path-specific notes marked [PATH A], [PATH A+37], [PATH B] where relevant."
purpose: "Pre-scripted response protocols for foreseeable Phase 1 launch failures. Reference during execution — not before. Written for Anya executing solo."
companion_docs:
  - distribution-checklist-template.md
  - PHASE_1_EXECUTION_READINESS.md
  - DISTRIBUTION_GUIDE.md
  - DOMAIN_37_SEQUENCING_PLAN.md
  - failure-mode-decision-tree.md
---

# Phase 1 Launch Risk Mitigation and Response Playbook

**Written**: May 6, 2026
**For**: Anya — solo execution of Phase 1 distribution across Paths A, A+37, and B
**Use this document**: On launch day and in the 30 days following Batch 1 send. For pre-launch assessment, see `PHASE_1_EXECUTION_READINESS.md`.

The infrastructure is approved for launch. Gists are live. Batch 1 contacts are verified. All 35 domains are production-ready. The probability of catastrophic failure is low. The probability of minor friction — a bounced email, a non-response, a confused reply — is near-certain. This playbook scripts the response so that each friction point takes under 10 minutes to resolve and does not cause launch paralysis.

**Severity tiers used throughout this document**:
- CRITICAL: Stop. Do not send further emails until resolved. Estimated fix time > 2 hours.
- HIGH: Fix before sending the next email. Estimated fix time 15–60 minutes.
- MEDIUM: Monitor and fix in parallel with continued sending. Estimated fix time 1–4 hours.
- LOW: Log and defer to post-launch review. No execution impact.

---

## Section 1: Technical Failures

Technical failures during Phase 1 distribution break into three clusters: Gist creation and access, template field fill, and email delivery. Most are recoverable in under 30 minutes if caught early. The detection method for each is the most important part — you need to know something broke before assuming it worked.

### 1.1 Gist Creation and Access Failures

**Current state**: All 6 canonical Gists were created April 30 (Session 678) and verified live. The URLs are in `DISTRIBUTION_GIST_URLS.md`. [PATH A+37] requires one additional Gist — the Domain 37 standalone — created on Day 0, Block 2 of the 4-hour checklist.

**Failure: Gist URL not loading (existing Gists)**

Detection: Run the pre-checklist confirmation — visit https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261. If it does not load within 10 seconds, there is a problem.

Causes and responses:

- GitHub is down (check https://githubstatus.com). If GitHub has a verified outage: do not send emails yet. Wait for GitHub to restore. Recovery time: typically under 2 hours for a GitHub outage. While waiting: complete Blocks 1–4 (script config, contact verification, personalization). Emails can be drafted; do not send until Gist URLs resolve.

- GitHub account `esca8peArtist` is suspended or rate-limited. Severity: CRITICAL. If the account itself has been suspended, the public Gists are inaccessible and all distributed links are broken. Response: (1) Log in to GitHub and check account status. (2) If suspended, attempt account recovery via GitHub support (2–7 days response time). (3) Immediate fallback: create mirror Gists under a backup GitHub account. Record the new URLs in `DISTRIBUTION_GIST_URLS.md` and re-run `fill_templates.py` with the updated URLs before sending any emails.

- URL is correct but Gist was accidentally deleted. Response: Re-create the Gist from the local source file. The source files are in `/projects/resistance-research/`. Recovery time: 10–15 minutes per Gist. Log the new URL in `DISTRIBUTION_GIST_URLS.md`.

Severity: CRITICAL if Gists are inaccessible. Do not send emails with broken links.

**Failure: Domain 37 Gist creation error [PATH A+37 only]**

Detection: After Block 2 of the 4-hour checklist, visit the URL you just created. If it does not render with the advocacy windows table visible, something went wrong.

Causes and responses:

- Markdown rendering failure (table not displaying). Cause: A pipe character or whitespace error in the paste. Response: Edit the Gist in place — click the pencil icon at the top right of the Gist page. Re-paste the advocacy windows table section. The entire Gist does not need to be deleted and recreated. Recovery time: 5 minutes.

- "Gist too large" error. Gist has a size limit of approximately 10 MB per file. The full Domain 37 document is 543 lines. Cause: Unlikely to hit the limit on a single domain file; if it occurs, the document likely has embedded binary content or encoding artifacts from copy-paste. Response: Paste the content into a plain text editor, strip any non-UTF-8 characters, then re-paste into Gist. Recovery time: 10 minutes.

- Permission denied / not logged in. Response: Verify you are logged in as `esca8peArtist` before creating the Gist. The GitHub session may have expired. Log in again and repeat Block 2.

Severity: HIGH. Block 2 creates the Domain 37 URL that is referenced in all Phase 1b emails. The Domain 37 standalone Gist must exist before Phase 1b emails are drafted or sent.

**Failure: API rate limit during programmatic Gist operations**

Detection: `fill_templates.py` errors with a 429 response or "rate limit exceeded" message when attempting GitHub API operations.

Response: The fill script operates on local files only — it replaces text strings and writes to `scripts/filled_output/`. It does not call the GitHub API. If you are using the GitHub API separately (via `github-api-integration-guide.md` automation), rate limits apply: GitHub's unauthenticated API rate limit is 60 requests/hour; authenticated is 5,000/hour. Resolution: authenticate your GitHub API calls using a personal access token. Recovery time: 5 minutes to add the token; or wait 60 minutes if you have exceeded the unauthenticated limit.

Severity: LOW for manual workflow (no API calls involved). MEDIUM if API automation is in use.

---

### 1.2 Template Field Fill Errors

The `fill_templates.py` script applies field substitutions from `FIELD_VALUES` in the script to template files and writes output to `scripts/filled_output/`. Block 3 of the 4-hour checklist runs the script; Block 4 verifies the output.

**Failure: Unfilled placeholder strings remaining after script run**

Detection: Block 4 verification — search for `{{` in any file in `scripts/filled_output/`. If any `{{...}}` strings remain, the script ran with incomplete configuration.

Common unfilled fields and their fixes:

| Placeholder | Cause | Fix |
|-------------|-------|-----|
| `{{YOUR_NAME}}` | `FIELD_VALUES` dict not set | Edit `fill_templates.py`, set the value, re-run |
| `{{YOUR_CONTACT_INFO}}` | Same | Same |
| `{{DOMAIN_37_URL}}` | Path A+37 Gist not yet created | Complete Block 2 first |
| `{{PROPOSAL_URL}}` | `DISTRIBUTION_GIST_URLS.md` not read into script | Verify the URL constant in the script |
| `{{RECENT_JUST_SECURITY_ARTICLE}}` | Manual placeholder — script does not fill this | Fill by hand in email client draft (Block 6) |

The manual placeholders (`{{RECENT_JUST_SECURITY_ARTICLE}}`, `{{RECENT_WEISER_PUBLICATION}}`, etc.) are intentionally left for Block 6 hand-fill. They should remain in the `scripts/filled_output/` files and are filled per-contact in the email client drafts. Do not mistake these for script failures.

Severity: HIGH. Emails with unfilled `{{...}}` strings are not ready to send. Block 10 QA catches any remaining instances before send.

**Failure: Path-specific block resolution error**

Detection: The filled email templates for Path A should contain only the `[PATH A]` paragraph block; the `[PATH A+37]` and `[PATH B]` blocks should be absent. If all three blocks are present in the output, the script did not resolve the path-conditional logic.

Response: Verify `DISTRIBUTION_PATH` is set in `fill_templates.py` to the exact string `"A"`, `"A+37"`, or `"B"`. The string must match exactly — `"a"` (lowercase) will not resolve. Correct the value and re-run.

Severity: HIGH. Sending an email with all three path blocks visible looks like a template error to the recipient.

**Failure: Date math errors in the checklist**

The 4-hour checklist references relative dates (T+7, T+14, T+21, T+28, T+56). These are not calculated by any script — they are recorded manually in Blocks 7, 8, and 11.

Detection: Calendar reminders set to wrong dates.

Response: Before setting calendar reminders in Block 11, confirm the base date (T+0 = today, the day of decision). Write the T+0 date explicitly in the checklist header. All relative dates calculate from that fixed anchor.

For [PATH A+37] specifically: T+56 is the Week 8 Phase B decision point for the Domain 37 targeted send. From a May 6 launch, T+56 = July 1. Confirm this date and set the reminder explicitly.

Severity: LOW during launch. MEDIUM for planning: a missed T+56 reminder delays Phase 1b entirely.

---

### 1.3 Email Delivery Failures

**Failure: Bounce — hard bounce (address does not exist)**

Detection: An automated bounce notification arrives in your sending inbox within minutes to hours of sending. Subject line typically includes "Delivery Status Notification" or "Mail Delivery Failure."

Hard bounce protocol:

1. Do not resend to the bounced address. Hard bounces mean the address is invalid.
2. Identify the contact and open their entry in `BATCH_1_CONTACT_LOG.md`. Note the bounce.
3. Return to the contact's institutional website and verify the correct email. The five Batch 1 contacts have verified addresses, but institutional email patterns can change.
   - If a different address is listed: update the log, resend to the new address within 24 hours.
   - If no public email exists: attempt the institutional general contact address (e.g., info@protectdemocracy.org) with a note that you attempted to reach [Name] directly. Alternatively, contact via Twitter/X (@marceelias for Elias, @ProtectDemocracy for Bassin, etc.).
4. If two email attempts fail: flag as "email delivery failed — social fallback" in the log.

Severity: HIGH for Batch 1 contacts (the five most important). MEDIUM for Batch 2–5.
Recovery time: 15–30 minutes to verify and resend.

**Failure: Bounce — soft bounce (temporary delivery failure)**

Detection: Same as hard bounce, but the bounce message includes "temporarily unavailable," "try again later," or a 4xx error code rather than a 5xx error code.

Response: Wait 24 hours and resend the same email without modification. Soft bounces resolve on their own in most cases (mailbox full, server temporarily down). If the soft bounce repeats after 24 hours, treat it as a hard bounce and proceed with the hard bounce protocol.

Severity: MEDIUM. Do not resend immediately — wait the full 24 hours.

**Failure: SMTP error when sending**

Detection: Your email client shows an error when you attempt to send (e.g., "Could not connect to SMTP server," "Authentication failed").

Response: Check your email client's settings. This is typically a password expiration or two-factor authentication issue with the sending account, not a problem with the recipient. Resolve by re-authenticating in your email client. Recovery time: 5–10 minutes.

If using Gmail: Gmail has a daily send limit of 500 emails per day for personal accounts, 2,000 for Google Workspace. Phase 1 Batch 1 is 5 emails — this limit will not be reached. No SMTP quota concern for Phase 1.

Severity: HIGH. You cannot send until the SMTP connection is restored. Resolve before attempting to send.

**Failure: Email flagged as spam before arrival**

Detection: Indirect — no bounce, but also no open or response after 7 days. Or, a contact mentions in a later interaction that they did not receive your email.

Prevention during send:
- Send from a personal domain email address if possible (e.g., anya@yourdomain.com), not a free service (Gmail, Yahoo, Hotmail) — institutional contacts are more likely to have spam filters that catch free-service senders.
- Do not include more than 2 links in the email body. The Gist links count. A third link (e.g., to your Substack) can go in the sign-off footer rather than the body.
- Do not use subject lines with all-caps words, excessive punctuation, or trigger words ("FREE," "URGENT," "IMPORTANT").
- The personalized subject lines in `PHASE_1_EMAIL_TEMPLATES.md` are designed to avoid spam triggers.

Response if spam delivery suspected: If 7 days have passed with no engagement, send a brief follow-up from the same address: "I wanted to confirm this reached you — I sent a message on [date] about [topic]. Would you prefer I use a different channel?" This surfaces whether the original was received.

Severity: LOW (cannot confirm). Treat as non-response (see Section 2) after 7 days.

**Failure: Attachment size limit**

Phase 1 emails do not include attachments. All content is delivered via Gist links. This failure mode does not apply to the standard Phase 1 send. If you choose to add a PDF attachment (the 2-page executive summary PDF described in `DISTRIBUTION_GUIDE.md`): keep under 5 MB. Most institutional email servers reject attachments over 10 MB, and many filter at 5 MB. A 2-page PDF of the executive summary is well under 1 MB.

Severity: N/A for standard send. LOW if optional PDF is added.

**Failure: Sending domain blocklisted**

If your sending domain (not just the address) has been blocklisted by major anti-spam services, emails will be silently dropped. This affects everyone on the blocklisted domain.

Detection: Use a tool like MXToolbox (mxtoolbox.com/blacklists.aspx) to check if your sending domain is on any major blocklists. Run this check once before Day 0 send.

If blocklisted: The simplest fallback is to send from a Gmail or Protonmail address with a clear, personalized introduction explaining who you are. "My previous attempt from [domain] may have been caught — I am the researcher behind the Democratic Renewal Framework." This is an uncommon scenario but worth checking if your domain is less than 6 months old.

Severity: HIGH if confirmed. LOW as a pre-check (takes 2 minutes).

---

## Section 2: Contact Engagement Failures

Engagement failures are expected — the question is at what rate and what they signal. The protocols below distinguish between failure rates that are normal and rates that require diagnosis.

### 2.1 Email Bounces — Triage and Escalation

For Batch 1 (5 contacts), a single hard bounce is HIGH priority. Batch 1 contacts are the five most carefully selected and verified contacts in the entire outreach. A hard bounce on Wendy Weiser or Ryan Goodman means one of the institution's most important relationships starts broken. Use the hard bounce protocol in Section 1.3 immediately.

For Batch 2–5 (35–40 contacts total), a bounce rate above 8% (3 of 35 contacts) is HIGH priority and triggers contact list review. Above 15% (5+ of 35) is CRITICAL — the contact list has a data quality problem.

Batch bounce triage when rate exceeds 8%:

1. Identify all bounces. Classify: hard (address invalid) vs. soft (temporary).
2. For each hard bounce: visit institutional website, check LinkedIn for role changes. If the contact has left the institution, this is a stale entry (see Section 6).
3. Check if bounces cluster in any sector. All bounces from think tank contacts: check if there was a domain migration (organizations sometimes change their email domain). All bounces from law school contacts: check if the academic year calendar is relevant (some institutional inboxes are suspended during summer break).
4. If bounce clustering is confirmed: pause that sector's sends and correct the contact data before proceeding.

### 2.2 Non-Response Patterns

Define the non-response window explicitly before sending, so you are not guessing after the fact.

**Non-response windows by contact type**:

| Contact Type | First-response expectation | Follow-up trigger | Follow-up limit |
|-------------|---------------------------|-------------------|-----------------|
| Tier 1 institutions (Batch 1, 5 contacts) | 7–14 days | No response by Day 14 | 1 follow-up, then close |
| Tier 1 broader (Batches 2–3) | 14–21 days | No response by Day 21 | 1 follow-up, then close |
| Tier 2 state-level (Batches 4–5) | 21–30 days | No response by Day 30 | 1 follow-up, then close |
| Domain 37 election-protection [PATH A+37] | 7 days (time-sensitive) | No response by Day 7 | 1 follow-up within 3 days of trigger |

Follow-up email template (adapt for each contact):

> Subject: Following up — [original subject line topic]
>
> [Name], I wanted to follow up briefly on my email from [date]. I shared a research framework on [topic] — the summary is here: [Gist URL]. If the timing is off, or if a different colleague at [institution] would be a better contact for this, please let me know. No pressure either way.
>
> [Your name]

This follow-up is deliberate: it provides the easiest possible off-ramp (forward to a colleague, which often happens) and does not demand a response. The phrase "no pressure either way" explicitly invites a "not for us" response, which is better than silence because it closes the loop.

After one follow-up with no response: close the contact as "no response — close" in the tracking log. Do not send a third email. Three contacts to the same person within 30 days, with no response, damages the sender's credibility with that institution.

**Reading non-response patterns across batches**:

If 0 of 5 Batch 1 contacts respond within 14 days: this is an early warning signal. Before sending Batch 2, diagnose: are the emails being delivered? (Check for bounces, check spam.) Are the Gist links working? Is the personalization genuinely specific, or does it read as generic? Consider whether the subject line needs adjustment before Batch 2.

If fewer than 2 of 5 Batch 1 contacts respond within 21 days: review the email framing. Request an honest read from a trusted peer if possible.

If 2 or more of 5 Batch 1 contacts respond within 14 days: proceed to Batch 2 with confidence.

### 2.3 Opt-Outs and Unsubscribes

Institutional outreach emails are not mass mailing campaigns — they are individually composed and sent. There is no "unsubscribe" link because there is no list. If a contact replies asking not to be contacted further: honor it immediately, log it in the tracking spreadsheet, and do not follow up.

An opt-out response is useful data: it often includes a reason ("not our area of focus," "please contact our communications team instead"). Log the reason. If a pattern emerges — multiple contacts from one institution saying "not our area" — this reveals a contact-selection error, not a content problem.

An unexpected high opt-out rate (more than 3 contacts across all batches asking to stop) signals one of two things: the contacts are not well-matched to the content, or the outreach framing reads as aggressive or spammy. Diagnose by reviewing whether the declined contacts share any characteristics (same sector, same tier, same email framing). Adjust for subsequent batches.

### 2.4 Decline and Critique Responses

A decline response — "I looked at the framework, but it is not something I can engage with" — is not a failure. It is data. A critique response — "I reviewed the framework and have concerns about [specific issue]" — is potentially your most valuable early signal.

**Severity triage for decline/critique responses**:

| Response type | Assessment | Action |
|---------------|-----------|--------|
| Polite decline, no reason given | Normal | Log as "declined," no follow-up needed |
| Decline with redirect ("contact X at our org instead") | Positive — internal routing | Follow the redirect; thank the decliner |
| Critique of methodology or sourcing | Constructive — high value | Read carefully, assess whether critique reveals actual error; respond substantively (see below) |
| Critique of political framing ("this is too partisan") | Important signal | Assess whether the framing can be adjusted; do not argue |
| Hostile or dismissive response | Low priority | Log, do not engage beyond acknowledgment |

**Responding to constructive critique**:

If a contact raises a specific methodological concern (e.g., "the 3.5% movement participation threshold is contested in the literature"), respond within 24–48 hours with: (1) acknowledgment that you have read the concern carefully; (2) either a defense of the methodology with sources, or an acknowledgment that the critique reveals a real limitation; (3) an offer to share the underlying research. Do not be defensive. A contact who engages critically with the framework is reading it seriously. That engagement is the goal.

If the critique reveals an actual factual error: thank the contact, correct the error in the source Gist (edit the Gist directly), and note the correction in `WORKLOG.md`. This kind of correction, made publicly and transparently, strengthens rather than undermines the framework's credibility.

---

## Section 3: Institutional Feedback Surprises

Phase 1 is designed to solicit substantive institutional engagement. That means feedback will arrive that was not anticipated. The protocols below separate feedback that should trigger action from feedback that represents normal interpretation variation.

### 3.1 Negative Feedback on Framework Scope

**Scenario: A Tier 1 contact says the framework is too broad to be actionable.**

This feedback is common and often reflects the contact's own institutional focus, not a design flaw. The framework's breadth is a feature for some contacts and a barrier for others.

Response: "The 35-domain scope reflects the research's diagnostic ambition rather than its implementation roadmap. The five minimum-viable reforms in the executive summary are the near-term action set. Would a domain-specific deep dive be more useful for your work on [Domain X]?" This response redirects the conversation to the content most relevant to the contact and offers a narrower framing without conceding that the broad scope is wrong.

If this feedback arrives from more than three Tier 1 contacts independently: revisit the executive summary framing. The two-page executive summary should be doing more work to sequence the reader from "broad diagnosis" to "specific near-term actions." This does not require domain edits — it requires a clearer entry point in the summary document.

**Scenario: A contact challenges a specific domain's methodology — not a factual error, but a framing choice.**

Example: "The Domain 6 analysis of judicial independence overstates the historical norm of court compliance with executive authority."

Response protocol: (1) Thank the contact for engaging with the specific domain. (2) Identify whether this is a genuine interpretive disagreement or a factual claim. Interpretive disagreements are fine — frame them as "the evidence supports this reading, though I recognize the interpretive debate." Factual claims must be verified against the source material. (3) Do not revise domain content based on a single contact's framing objection. Revisions require a pattern of feedback (see 3.4 below) or an identified factual error.

**Scenario: A contact says a domain is missing a major development they expected to find.**

This is high-value feedback. A Tier 1 contact expecting to find X and not finding it identifies a gap that the framework should address.

Response: "Thank you — that is exactly the kind of gap I need to know about. Can you share the specific development or source you had in mind?" Then: log the gap in `WORKLOG.md` under "Feedback-driven domain updates." Assess whether the gap belongs in Phase 1 content (update the existing Gist) or Phase 2 expansion (new domain research). The distinction: if the missing content would substantially change a domain's conclusions, it is Phase 1. If it is additive but not corrective, it is Phase 2.

### 3.2 Requests for Domain Modifications or Rebalancing

**Scenario: A contact requests that a specific domain's policy recommendations be adjusted.**

Example: "The Domain 17 labor section recommends sectoral bargaining, but our organization's position is that enterprise bargaining with card-check neutrality is more politically viable."

This is the framework working as designed — institutional contacts have deep domain expertise and will refine recommendations. The question is what to do with the request.

Triage:
- If the request reflects a genuine evidence question (the contact has data that the framework does not): integrate the new evidence in a Phase 2 domain update. Notify the requesting contact when the update is live.
- If the request is a policy preference disagreement (the contact prefers a different approach, not a different evidence base): acknowledge the disagreement, note that the framework represents one evidence-based approach, and offer to discuss the comparative evidence. Do not modify domain content on the basis of a policy preference.
- If the request represents the dominant view in the domain's expert community (multiple experts across institutions suggest the same adjustment): treat as Phase 2 update.

**Scenario: A contact requests rebalancing across domains (e.g., "the judicial independence domain is overweight relative to the voting rights domain").**

Response: "The domain weighting reflects the research priority assessment at the time of the framework's construction. Would you be willing to share your thinking on the relative priority? That kind of expert input is exactly what Phase 2 iteration is for." This opens a feedback dialogue without committing to changes.

If the same rebalancing request comes from three or more independent contacts: flag in `WORKLOG.md` as a Phase 2 structural review item.

### 3.3 Unexpected Reinterpretation

**Scenario: A contact uses the framework to reach conclusions the framework does not support.**

Example: A contact cites the Domain 37 analysis to argue for election postponement, which the framework explicitly does not recommend.

Response: Clarify promptly and directly: "The framework's Domain 37 analysis documents federal interference mechanisms — it advocates for protecting existing election integrity infrastructure, not for altering the election calendar. Here is the specific section: [link to relevant section]." Do not let misreadings circulate without correction. A single clear correction sent privately to the misreading contact is the right response; do not create a public dispute.

**Scenario: A contact interprets the framework as partisan advocacy rather than structural analysis.**

This is a credibility-sensitive situation. The framework's claim to nonpartisan structural analysis is essential to its institutional reach across the ideological spectrum.

Response: "The framework is analytical — it documents what evidence from functioning democracies shows works, rather than advocating for a partisan position. I would be glad to discuss any specific framing you found read as advocacy rather than analysis." Offer to review the specific section they found problematic.

If the partisan-framing critique comes from a center-right contact (e.g., Cato Institute, R Street): take it seriously. These are the contacts best positioned to identify framing that reads as ideologically coded. If they identify specific language — not general topic disagreement, but specific framing — adjust that language in the Gist.

### 3.4 Triage: Phase 2 Domain Update vs. Implementation Variation

Not all feedback should drive content changes. The triage rule:

**Phase 2 domain update triggered by**:
- Factual error confirmed by primary source
- Missing major development that changes a domain's analysis
- Consistent feedback from 3+ independent expert contacts identifying the same gap
- A contact who is the leading expert in a domain identifying a significant omission

**Implementation variation — no content change needed**:
- A contact applies the framework to their state/jurisdiction and modifies recommendations for local conditions
- A contact uses one domain and ignores others (appropriate self-selection)
- A contact disagrees with a policy recommendation but not with the underlying evidence
- A contact frames the research's conclusions differently than the framework does in their own publication

Implementation variation is the intended outcome of Phase 1. Different institutions will use different pieces of the framework in different ways. This is not a failure — it is adoption. Document it in `DISTRIBUTION_EXECUTION_LOG.md` but do not treat it as requiring a content response.

---

## Section 4: Distribution Channel Failures

### 4.1 Substack Failures

**Failure: Cannot access Substack account**

Detection: Login fails at substack.com.

Response: Use the account recovery flow (email or phone). If 2FA is enabled and the device is unavailable, Substack's support response time is typically 24–48 hours. While waiting: Substack Post 1 is scheduled for T+7 (or T+3 from the 4-hour checklist). A 24-hour account recovery delay does not materially affect the T+7 timeline.

**Failure: Substack delivery to subscribers fails**

Detection: Unusual drop in subscriber open rates (below 15% when your baseline is higher), or subscriber complaints about not receiving the email.

Substack manages deliverability centrally — if Substack has a deliverability issue, it affects all publishers. Check https://status.substack.com. If no platform issue: check whether your publication's "From" address is being filtered by Gmail's "Promotions" tab. The open rate measurement is only as reliable as the email client's tracking pixel support; some contacts will have opened without registering a tracked open.

If Substack send appears to fail entirely: the nuclear option is to post the content as a publicly viewable Substack page (not a post), share the URL directly via social media and email, and retry the email send in a subsequent issue.

**Failure: Substack quota / rate limit**

Free Substack accounts have no subscriber limit but do have feature limitations. For Phase 1, the relevant limitation: free accounts can send emails to up to 50,000 subscribers. Phase 1 is not going to hit 50,000 subscribers in the first 30 days. This failure mode is not applicable.

### 4.2 Reddit Posting Blocks

**Failure: Post removed by moderators immediately after posting**

Detection: The post disappears within an hour. No notification, or notification that it was "removed by moderators."

Reddit removes posts for several reasons:
- Account age/karma requirements: some subreddits (r/neutralpolitics, r/ChangeMyView) require accounts with a minimum number of comment karma. The `distribution-reddit-templates.md` targets subreddits that are relevant without having high participation barriers. If your Reddit account is new (less than 30 days old), avoid subreddits with stated age/karma requirements.
- Self-promotion rules: most subreddits ban posts that read as self-promotion. The Reddit templates are framed as sharing research, not promoting a document. If removed for self-promotion: reframe the post as a question or discussion prompt ("Researchers have documented 24 active DOJ voter roll cases in competitive 2026 districts — what do election protection organizations need to prepare?") and link to the Gist in a comment rather than the post body.
- Link karma requirements: some subreddits require you to build karma through comments before posting links. If blocked from a target subreddit: participate in 3–5 substantive comment threads in that subreddit before attempting a post.

Recovery: Most subreddits allow resubmission after addressing the removal reason. Wait 24 hours and post with revised framing.

**Failure: Link blocked by Reddit (domain filtering)**

Detection: Post submits but the link is flagged as spam and the post is automatically removed.

GitHub Gist links (gist.github.com) are not blocklisted on Reddit. If this occurs, it suggests either the account is flagged as spam (new accounts with no history) or a specific subreddit has GitHub Gist filtered.

Response: Post the content directly as text (without a link), include the URL in the body as plain text (not a hyperlink), and note that the full document is available at the URL. Plain-text URLs are less likely to be filtered than hyperlinks.

Severity: LOW for most subreddits. MEDIUM if the target subreddit is a high-priority channel.

### 4.3 Institutional Email Rejection

**Failure: Email classified as bulk mail by recipient's server**

Detection: No open tracked, no bounce. Soft failure — the email arrived in a folder the contact does not check, or was classified as newsletter.

Prevention:
- Do not use email tracking pixels if your email client inserts them automatically (Mailtrack, Superhuman add tracking pixels). Tracking pixels are a spam signal. Disable tracking for Batch 1 sends and instead track engagement through direct response.
- The subject lines in `PHASE_1_EMAIL_TEMPLATES.md` are personalized and domain-specific, not newsletter-style. This reduces bulk classification risk.
- Send from your personal email account, not a marketing platform (Mailchimp, ConvertKit). Marketing platforms insert bulk headers that institutional spam filters flag.

Response if bulk classification suspected: Follow up with a brief direct message via the contact's institutional LinkedIn or Twitter/X. "I sent you an email on [date] about [topic] — wanted to make sure it reached you."

**Failure: Email rejected by recipient's server (hard delivery failure for non-address reasons)**

Rarely, some institutions (particularly government agencies, federal courts) have inbound email restrictions that block external senders who are not on approved lists.

Response: Use the institution's public contact form, or contact a person at the institution through a mutual connection who can route the message internally.

Severity: MEDIUM. Not common for the Tier 1–2 contacts (academic, policy, civil society organizations) in Phase 1. More likely if outreach expands to federal agencies in a later phase.

### 4.4 Social Media Platform Restrictions

**Failure: X/Twitter link blocked or post limited**

gist.github.com links are generally not blocked by X. If a post is limited in reach (X's "soft block" that reduces algorithmic distribution): this is undetectable and unlikely to matter significantly for Phase 1, where X/social media distribution is a secondary channel.

**Failure: Bluesky or Mastodon technical issues**

These are minor distribution channels. Technical issues on these platforms: wait and repost later. Recovery time: not a priority.

---

## Section 5: Coordination Failures

### 5.1 Duplicate Sends

Three contacts appear on both the Phase 1a (general framework) and Phase 1b (Domain 37 targeted) lists [PATH A+37 only]: Wendy Weiser (Brennan Center), Marc Elias (Democracy Docket), Ian Bassin (Protect Democracy). These three are intentionally receiving two emails, 1–3 days apart. This is by design, not an error.

The risk is sending an unintentional duplicate — sending the same email twice to the same person, or sending Batch 1 and Batch 2 to the same contact because they appear in both lists.

Prevention: The tracking spreadsheet (from `phase-1-contact-list-structure.md` schema) is the master deduplication record. Before each batch send, filter the batch list against the "email sent" column. Any contact with a send date already logged should be reviewed before sending again.

If an accidental duplicate send occurs: send a brief apology within 24 hours. "I inadvertently sent you a duplicate of my earlier email — apologies for the repetition. Please disregard the second copy." Keep it short. Do not explain at length. Most contacts will have noticed and will appreciate the quick acknowledgment.

Severity: LOW for individual duplicates. MEDIUM if systematic (a filter failure in the tracking spreadsheet that allows multiple batches to include the same contacts).

### 5.2 Response Routing Confusion

Phase 1 is a solo operation — all responses route to Anya. Response routing is not a complex problem. The risk is that a response sits in email and goes unanswered for too long.

The monitoring setup from Block 11 of the 4-hour checklist addresses this: a label/filter routes Phase 1 responses to a dedicated folder with flags. Check that folder at least once daily during the first 30 days.

For [PATH A+37] specifically: Phase 1b emails to election-protection organizations may generate faster and more operationally focused responses than Phase 1a. Domain 37 contacts may ask for specific follow-up documentation (case citations, data tables) on tight timelines. Treat Domain 37 organization responses as higher urgency than general framework responses: respond within 24 hours, not 48.

**If a contact responds to an incorrect email address** (e.g., replies to a Phase 1a email but their Phase 1b email is where the substantive conversation should be): acknowledge in your reply and clarify the dual-track intent. "I sent you a more targeted Domain 37 briefing at [date] as well — please see that email for the election-protection-specific content."

### 5.3 Version Control Gaps

The Gists are the canonical distributed versions. If you update a source file after the Gist is live, the Gist does not automatically update — you must manually edit the Gist.

Risk: A domain file is updated (e.g., Domain 1 to integrate the post-May 1 FISA confirmation) but the Gist is not updated. Contacts who received the Gist link before the update continue to see the old version.

Management protocol:
- Any correction to a production-ready domain that affects distributed content: edit the Gist within 24 hours of the source file edit.
- Log the Gist update in `WORKLOG.md` with the edit description and timestamp.
- Contacts who received the Gist before the update: a brief follow-up is appropriate for high-impact corrections (a factual error corrected is worth flagging); for minor updates, the updated Gist is self-evident from the Gist edit history.

For Phase 1b [PATH A+37]: the Domain 37 standalone Gist is the most time-sensitive version-controlled document. If Domain 37 analysis changes due to new developments before Phase 1b sends, update the Gist before sending. Election-protection organizations will use Domain 37 in active legal proceedings — they need the most current version.

### 5.4 Path Cross-Contamination [PATH A+37 only]

The three contacts who appear on both Phase 1a and Phase 1b lists (Weiser, Elias, Bassin) need to receive different emails that acknowledge the dual-track nature. The Phase 1b templates include the line: "Given your organization's specific work on [X active litigation], I wanted to follow up with Domain 37 separately."

**Failure: Phase 1b email reads as a correction of Phase 1a, not a targeted follow-up**

If the Phase 1b email's opening implies that the Phase 1a email was incomplete or an error, the contact may be confused about which version of the framework is authoritative.

Prevention: The Phase 1b email to these three contacts should explicitly frame itself as a second, separate document: "This is a targeted follow-up to my earlier email — Domain 37 on federal election interference mechanisms, which I am sending separately to election-protection organizations because of its specific relevance to your active litigation calendar."

**Failure: Phase 1a contacts receive Domain 37 framing before Phase 1a email lands**

If Phase 1b is accidentally sent to a contact before Phase 1a, the sequencing rationale collapses. The Phase 1a general framework email arrives after a targeted Domain 37 email, which reverses the intended credibility-building sequence.

Prevention: Phase 1b is not triggered until Phase 1a Batch 1 is confirmed sent. Block 9 of the 4-hour checklist is explicitly labeled "PATH A+37 ONLY — Phase 1b Email Preparation." These are prepared as drafts, not sent on Day 0. The send window for Phase 1b is Days 1–3 of the Phase A calendar.

---

## Section 6: Data Quality Issues

### 6.1 Stale Contact Entries

Contact verification was completed April 29, 2026 for the five Batch 1 contacts. The 4-hour checklist (Block 5) requires a rapid re-verification immediately before Day 0 send. For Batches 2–5, positions were not verified in April and require verification before each batch's send.

**Stale contact detection**:

| Signal | What it means |
|--------|--------------|
| Hard bounce on institutional email | Person has left the institution |
| Soft bounce on institutional email | Server-side issue (usually resolves); if persists 48 hours, check for institutional email migration |
| LinkedIn shows different title/employer | Person has moved — verify new institution, find appropriate new contact at old institution |
| Institutional website no longer lists the person | Departed. Check the "team" or "staff" page for the most recent version. |
| No recent publications or public activity in 6+ months | May be on leave or reduced capacity; lower-priority contact |

For each stale entry identified:
1. Log in the tracking spreadsheet: name, role at send time, current status discovered.
2. Find a replacement contact at the same institution if possible: the program director's deputy, the co-director, or the institutional contact email. Domain relevance score for the institution does not change — only the specific contact changes.
3. Resend if the institutional relationship is Tier 1 priority. If Tier 3 or lower, de-prioritize and continue to next contact in queue.

### 6.2 Missing Metadata

The contact list schema from `phase-1-contact-list-structure.md` requires `domain_relevance_score`, `primary_domain`, and `institutional_mandate_fit` for each contact. If a batch is assembled without these fields filled, personalization quality degrades.

Detection: Review each batch's contact entries before drafting personalization. If `domain_relevance_score` is blank, the contact has not been properly assessed.

Response: Do not send to contacts without a completed domain relevance assessment. A generic email to a think tank contact is worth less than no email — it signals that the sender did not do the homework. Complete the relevance assessment (10–15 minutes per institution) before including the contact in a batch.

If batch assembly is under time pressure and some contacts need relevance assessment: divide the batch. Send to fully assessed contacts in this batch; move un-assessed contacts to the next batch.

### 6.3 Formatting Corruption

**Risk: Gist content displays incorrectly for recipients**

The Gist documents use Markdown formatting. GitHub Gist renders Markdown correctly in the browser. The risk is that a contact views the raw Gist URL (which shows the Markdown source, not the rendered output) rather than the rendered page.

Prevention: Share the rendered Gist URL, not the raw URL. The rendered URL ends in the Gist hash (e.g., `/2dec7fd03b08ab5b41c55d402f44c261`). The raw URL contains `/raw/`. If you share a raw URL: the recipient sees the unformatted Markdown source, which is readable but not as clean.

**Risk: Email template character encoding corrupts on send**

Smart quotes (`""`), em dashes (`—`), and accented characters in proper names can render incorrectly if the email is sent in a non-UTF-8 encoding.

Prevention: When copying content from the `scripts/filled_output/` templates into your email client, paste as plain text first, then reformat. This strips problematic encoding artifacts. Review each email draft for visible encoding errors (question marks, boxes, or unexpected character sequences) before sending.

### 6.4 Detection and Cleanup Workflow

**Weekly data quality check (add to the monthly measurement review)**:

1. Review all contacts with "no response" status after 21 days. For each: confirm their current email via institutional website. Flag any where the institutional website now shows a different person.

2. Check the tracking spreadsheet for duplicate entries. The spreadsheet should have one row per contact, not per send. If a contact appears in both Phase 1a and Phase 1b tracking (for the three crossover contacts), they should have a clear "duplicate by design" note.

3. Verify Gist URLs in `DISTRIBUTION_GIST_URLS.md` remain live once per month. Spot-check at least two Gists.

---

## Section 7: Metrics Tracking and Early Success Signals

### 7.1 Day 0 Baseline — Set Before Sending

Before Block 11 (monitoring setup), record the following baselines. Without baselines, you cannot interpret whether any subsequent number is good or bad.

**Day 0 Baseline Capture (5 minutes, before sending Email 1)**:

| Metric | Day 0 Value | Source |
|--------|-------------|--------|
| Gist views — Democratic Renewal Proposal | ___ | Gist analytics (logged in as esca8peArtist) |
| Gist views — Executive Summary | ___ | Same |
| Gist views — Litigation Tracker | ___ | Same |
| Substack subscribers | ___ | Substack dashboard |
| Substack open rate (last issue, if applicable) | ___ | Substack dashboard |
| Contacts in tracking log | 0 | Tracking spreadsheet |
| Responses received | 0 | Email |

Record these in `DISTRIBUTION_EXECUTION_LOG.md` under "Day 0 Baseline."

### 7.2 Success Metrics by Cadence

**Minimum acceptable thresholds (not targets — floor)**:

| Metric | 7-day floor | 14-day floor | 30-day floor |
|--------|-------------|--------------|-------------|
| Batch 1 email delivery (non-bounce) | 4 of 5 | 5 of 5 | 5 of 5 |
| Batch 1 engagement (open or response) | 1 of 5 | 2 of 5 | 3 of 5 |
| Gist views (Proposal, all-time) | 20 | 50 | 150 |
| Institutional contacts replied | 1 | 3 | 8 |
| [PATH A+37] Phase 1b contacts opened or responded | — | 2 of 12 | 4 of 12 |

**Target metrics (what a successful Phase 1 looks like)**:

| Metric | 14-day target | 30-day target | 90-day target |
|--------|---------------|---------------|---------------|
| Institutional contacts replied | 5+ | 10+ | 20+ |
| Referrals generated (new contacts from existing contacts) | 1 | 5 | 15+ |
| Gist views (Proposal) | 100+ | 300+ | 1,000+ |
| Substack subscribers | 50+ | 200+ | 500+ |
| Framework citations in external publications | 0 | 0–2 | 3+ |
| [PATH A+37] Domain 37 contacts integrating into active litigation context | 0 | 1 | 3+ |

### 7.3 Early Warning Signs

The following signals, if observed within the first 14 days, require diagnosis before proceeding to Batch 2.

**Red flags that trigger pause-and-diagnose**:

- Bounce rate above 8% on any batch (3+ of 35 contacts). Pause next batch. Diagnose stale contact data.
- Zero opens or responses from Batch 1 after 14 days. Investigate delivery: are emails landing in spam? Are Gist links working? Reconsider personalization quality before Batch 2.
- Multiple contacts reply asking how you got their contact information. This signals that the sourcing of contact data is not as public as assumed. Review sourcing notes in the contact database.
- A Tier 1 contact publicly criticizes the framework on social media before responding privately. This is rare but high-impact. Respond promptly and publicly (not defensively) and reach out privately within 24 hours.
- GitHub Gist views plateau at under 20 after 7 days despite Batch 1 emails being sent. Possible cause: emails not being opened, or recipients not clicking the links. Consider whether the subject line or email body CTA is driving to the Gist effectively.

**[PATH A+37] Domain 37 specific early warnings**:

- Zero responses from Phase 1b Tier 1 contacts (7 election-protection organizations) after 14 days. This is a significant early warning given the time-sensitive nature of the May 30 and June 30 advocacy windows. Escalation: attempt social media contact or institutional contact form within 48 hours of the 14-day mark.
- A Phase 1b contact indicates the May 30 window has already been addressed by their organization. This is a positive signal (they are active) but means Domain 37 advocacy window 1 framing should shift to window 2 (June 30) in any follow-up.

### 7.4 Early Positive Signals

The following signals, if observed within the first 14 days, indicate Phase 1 is working as designed.

**Green flags**:

- A Batch 1 contact responds with a substantive question about a specific domain (they read the document deeply enough to generate a question). This is the best early signal.
- A contact offers to forward the framework to a colleague or forward it internally (internal routing). This generates second-order reach without additional effort.
- A Gist link is shared on social media by a contact or their institution. Track the share.
- A Substack post from a high-reach publisher cites or links to the framework. Even a brief mention is an early attribution event.
- [PATH A+37] An election-protection organization asks for additional data on one of the five advocacy windows. This is direct confirmation that the Domain 37 framing is being actively used, not filed away.

Secondary distribution — a contact forwarding the framework to a colleague unprompted — is the single most valuable early signal. It means the contact found the framework compelling enough to share it, and the second-order contact received it with an implicit endorsement. Track every secondary distribution event in `DISTRIBUTION_EXECUTION_LOG.md`.

### 7.5 Daily Checkpoint Template

Use this template to log Phase 1 status. The full entry takes under 15 minutes to complete. Copy into `DISTRIBUTION_EXECUTION_LOG.md` and fill each field.

---

**Phase 1 Daily Checkpoint — Day ___**

Date: _______________
Path: [ ] A  [ ] A+37  [ ] B
Checkpoint type: [ ] Day 0  [ ] Day 1  [ ] Day 2  [ ] Day 3  [ ] Day 7  [ ] Day 14  [ ] Day 30

**Send status**
- Emails sent today: ___ (names: _______________)
- Bounces received today: ___ (contacts: _______________)
- Bounce type: [ ] Hard  [ ] Soft  [ ] None
- Bounce action taken: _______________

**Response status**
- New responses received: ___ (contacts: _______________)
- Response types: [ ] Acknowledgment  [ ] Substantive  [ ] Referral offer  [ ] Decline  [ ] Critique
- Response requiring action within 24h: [ ] Yes  [ ] No
- Planned response: _______________

**Engagement tracking**
- Gist views (Proposal, all-time): ___
- Gist views (Executive Summary, all-time): ___
- Substack subscribers (if post is live): ___
- Secondary distributions observed (shares/forwards): ___

**[PATH A+37] Domain 37 status**
- Phase 1b emails sent today: ___
- Phase 1b responses received: ___
- Advocacy window status: May 30 [ ] Active  [ ] Passed / June 30 [ ] Active  [ ] Passed

**Early warning flags (check each)**
- [ ] Bounce rate remains under 8% (if above: PAUSE next batch)
- [ ] Gist links verified working
- [ ] No unaddressed responses older than 48 hours

**Next action**
- Next scheduled batch: Batch ___, send date: _______________
- Specific to-do before next batch: _______________

---

**Day 0 checkpoint**: Immediately after Block 11. Record send timestamps for all Batch 1 emails. Record baseline Gist view counts. Confirm no bounces in first 60 minutes.

**Day 1 checkpoint**: Check for bounces, check for any immediate responses (unlikely but possible from Ryan Goodman at Just Security, who monitors his inbox actively). Verify Substack post 1 is still scheduled correctly.

**Day 2 checkpoint**: First meaningful response window. Goodman and Weiser have 24–48 hour response cycles based on their public activity levels. Any Batch 1 response arriving on Day 2 is an early positive signal.

**Day 3 checkpoint**: [PATH A+37] Phase 1b emails should have been sent by today. Log Phase 1b send timestamps. All five Batch 1 contacts should have received their email by now. If zero bounces and zero responses: the 7-day mark is the next diagnosis point.

**Day 7 checkpoint**: Extended assessment. If fewer than 2 of 5 Batch 1 contacts have responded: assess whether to adjust subject line framing before Batch 2. If 2 or more have responded: Batch 2 proceeds with the same approach. Reddit posts go live today (r/PoliticalScience). Substack Post 1 is scheduled for today if set to T+7.

**Day 14 checkpoint**: Mid-point assessment. Review all Batch 1 and Batch 2 responses against the minimum acceptable thresholds in 7.2. Prepare Batch 3 contact list and personalization. [PATH A+37] First Phase 1b follow-up wave if any election-protection org has not responded.

**Day 30 checkpoint**: Month 1 review. Record all metrics against 30-day targets. Identify top-performing contacts (most substantive engagement, most referrals). Identify sectors lagging (lowest response rates). Draft month 2 approach adjustments. File a full status entry in `WORKLOG.md`.

---

*Phase 1 Launch Risk Playbook — Created May 6, 2026. Companion document: `failure-mode-decision-tree.md`. Reference before consulting: `PHASE_1_EXECUTION_READINESS.md`, `distribution-checklist-template.md`, `DOMAIN_37_SEQUENCING_PLAN.md`, `DISTRIBUTION_GIST_URLS.md`.*
