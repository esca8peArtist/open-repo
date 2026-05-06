---
title: "Phase 1 Failure Mode Decision Tree"
created: 2026-05-06
status: production-ready
applies_to: "All three distribution paths (A, A+37, B). Path-specific branches marked."
purpose: "Rapid triage during Phase 1 execution. Use this when something goes wrong and you need the immediate next step, not the full analysis. For full protocols, see phase-1-launch-risk-playbook.md."
companion_docs:
  - phase-1-launch-risk-playbook.md
  - PHASE_1_EXECUTION_READINESS.md
  - DISTRIBUTION_GIST_URLS.md
  - DISTRIBUTION_EXECUTION_LOG.md
---

# Phase 1 Failure Mode Decision Tree

**Written**: May 6, 2026
**Format**: Each failure type starts with a FIRST QUESTION. Answer it to get an immediate action or to branch further. Every path ends in one of four dispositions: STOP, PAUSE, CONTINUE, or LOG.

**Disposition definitions**:
- STOP: Halt all sends. Do not proceed until the condition is resolved. Playbook Section indicated.
- PAUSE: Finish any email currently being drafted. Do not start the next send until resolved.
- CONTINUE: No change to execution cadence. Handle the issue in parallel.
- LOG: Record in `DISTRIBUTION_EXECUTION_LOG.md` and carry on.

---

## INDEX — Go to the section matching your problem

1. [Gist link not loading or rendering incorrectly](#tree-1-gist-failures)
2. [Template fill script left {{placeholders}} in the output](#tree-2-template-fill-failures)
3. [Email bounced or failed to deliver](#tree-3-email-delivery-failures)
4. [Contact has not responded (non-response)](#tree-4-non-response)
5. [Contact responded negatively, opted out, or with critique](#tree-5-engagement-failures)
6. [Institutional feedback challenges the framework content](#tree-6-institutional-feedback)
7. [Substack, Reddit, or social channel is not working](#tree-7-channel-failures)
8. [Suspected duplicate send or contact overlap](#tree-8-coordination-failures)
9. [Contact data appears stale or incorrect](#tree-9-data-quality)
10. [Metrics look wrong or success signals are absent](#tree-10-metrics-and-signals)

---

## Tree 1: Gist Failures

**Symptom**: A Gist URL is not loading, not rendering correctly, or returning an error.

**FIRST QUESTION**: Is this an existing Gist (created April 30) or a new Gist you are creating right now [PATH A+37, Block 2]?

### Branch 1A: Existing Gist not loading

**Q1**: Does https://githubstatus.com show a current incident?

- YES → GitHub is down system-wide. **STOP**. Do not send emails with Gist links. Continue checklist Blocks 1–4 (drafting, contact verification, personalization). Do not send until GitHub confirms the incident resolved. Expected recovery: under 2 hours. Playbook Section 1.1.

- NO → Proceed to Q2.

**Q2**: Are you logged in to github.com as `esca8peArtist` and does the account show as active?

- NO (not logged in or session expired) → Log in. Retest the URL. If the Gist loads: **CONTINUE**. If it still does not load: proceed to Q3.

- YES (logged in, account appears active but Gist is not accessible) → Proceed to Q3.

**Q3**: Navigate directly to https://gist.github.com/esca8peArtist. Does the account page load and show existing Gists?

- NO — account page 404 or "suspended" message → The account has been suspended. **STOP**. See Playbook Section 1.1. Immediate action: (1) attempt GitHub account recovery; (2) simultaneously create mirror Gists under a backup account; (3) update `DISTRIBUTION_GIST_URLS.md` with new URLs; (4) re-run `fill_templates.py` before sending any email. Do not send until Gist URLs are confirmed live.

- YES — account page loads but the specific Gist is missing → The Gist was accidentally deleted. **PAUSE**. Recreate from the source file in `/projects/resistance-research/`. Log the new URL in `DISTRIBUTION_GIST_URLS.md`. Recovery: 10–15 minutes per Gist. Resume sending after confirming the new URL renders correctly.

- YES — Gist is listed on the account page but the URL you have in your email draft returns an error → URL in the draft is incorrect. **PAUSE**. Cross-reference against `DISTRIBUTION_GIST_URLS.md` and correct the URL in the draft. Do not send until corrected.

**DISPOSITION SUMMARY — Tree 1A**:
| Condition | Disposition | Fix time |
|-----------|-------------|----------|
| GitHub platform outage | STOP | 1–2 hrs (external) |
| Account suspended | STOP | 2–7 days (GitHub support) + mirror account 30 min |
| Gist deleted | PAUSE | 10–15 min |
| Wrong URL in draft | PAUSE | 2 min |

---

### Branch 1B: New Gist (Domain 37 standalone, PATH A+37 only)

**Q1**: Did you successfully create the Gist and receive a URL?

- NO — creation failed with an error message → What was the error?
  - "Permission denied" or redirect to login: You are not authenticated. Log in as `esca8peArtist` and retry.
  - "File too large": Strip non-UTF-8 characters from the source file using a plain text editor, re-paste, retry.
  - Any other error: Copy the exact error message. Check https://githubstatus.com. If platform issue: wait. If no platform issue: attempt creation in a different browser.

- YES — URL was created → Proceed to Q2.

**Q2**: Does the rendered Gist display the advocacy windows table correctly (not raw Markdown source)?

- NO — you see raw pipe characters and asterisks instead of a formatted table → The Gist is showing raw Markdown. This happens when the URL points to the raw view. Confirm you are using the base URL (`/gist.github.com/esca8peArtist/[hash]`), not the raw URL (which contains `/raw/`). If the URL is correct and GitHub Gist is not rendering the Markdown, click the pencil icon, make a trivial edit (add a space, remove it), and save. This forces a re-render.

- YES — table renders correctly → **CONTINUE**. Record the URL in `DISTRIBUTION_GIST_URLS.md` before proceeding to Block 3.

**DISPOSITION**: Domain 37 Gist creation issue is severity HIGH. Phase 1b emails cannot be drafted until this URL exists and renders correctly. If unresolvable after 30 minutes: **STOP Phase 1b preparation** and escalate via GitHub support. Phase 1a can proceed independently.

---

## Tree 2: Template Fill Failures

**Symptom**: After running `fill_templates.py`, output files still contain `{{placeholder}}` strings.

**FIRST QUESTION**: Search the output files for `{{`. How many distinct placeholder strings remain?

### Branch 2A: Placeholders remain that should have been filled automatically

These placeholders are filled by the script and should not appear in `scripts/filled_output/` after a successful run: `{{YOUR_NAME}}`, `{{YOUR_CONTACT_INFO}}`, `{{PROPOSAL_URL}}`, `{{EXECUTIVE_SUMMARY_URL}}`, `{{LITIGATION_TRACKER_URL}}`, `{{DOMAIN_37_URL}}` [PATH A+37 only].

**Q1**: Did the script run without errors in the terminal?

- NO — script exited with an error → Read the error message. Most common cause: a syntax error introduced when you edited `FIELD_VALUES`. Check that all values are strings in quotes, the dictionary has no trailing comma errors, and the file is saved. Fix and re-run.

- YES — script ran but the placeholder is still present → The `FIELD_VALUES` key for that placeholder does not match the placeholder string exactly. Open `fill_templates.py`, find the `FIELD_VALUES` dict, and verify the key is an exact character-for-character match. Re-run after correcting.

**Q2** [PATH A+37 only, for `{{DOMAIN_37_URL}}`]: Does the Domain 37 Gist URL exist in `DISTRIBUTION_GIST_URLS.md`?

- NO → You have not yet completed Block 2 (Domain 37 Gist creation). Block 2 must complete before Block 3. **PAUSE** Block 3. Complete Block 2 first. Then return to Block 3 and re-run.

- YES — URL exists → Copy it into `FIELD_VALUES` in `fill_templates.py` and re-run.

**DISPOSITION**: Unfilled automatic placeholders = **PAUSE**. Do not proceed to Block 5 (contact verification) until `fill_templates.py` produces clean output. Block 10 QA is the final check — but catching this in Block 4 saves rework.

---

### Branch 2B: Placeholders that are intentionally manual

These placeholders are NOT filled by the script and SHOULD remain in `scripts/filled_output/`: `{{RECENT_JUST_SECURITY_ARTICLE}}`, `{{RECENT_WEISER_PUBLICATION}}`, `{{RECENT_BASSIN_STATEMENT}}`, `{{INSTITUTION_SPECIFIC_DOMAIN_REFERENCE}}`, and similar per-contact personalization fields.

These are filled in Block 6 (email client draft personalization). Their presence in `scripts/filled_output/` is correct, not a failure.

**DISPOSITION**: If only manual placeholders remain after script run → **CONTINUE**. They will be filled in Block 6.

---

### Branch 2C: Wrong path block is visible in output

**Symptom**: The email template output contains paragraph blocks for multiple paths (e.g., the `[PATH B]` paragraph appears in what should be a Path A email).

**Q1**: What is `DISTRIBUTION_PATH` set to in `fill_templates.py`?

- Lowercase or incorrect string (e.g., `"a"` instead of `"A"`, `"A+37"` versus `"A + 37"`) → Correct to exact string `"A"`, `"A+37"`, or `"B"`. Re-run. The string comparison is case-sensitive and whitespace-sensitive.

- Correct string, but all three path blocks still appear → The conditional resolution logic in the script may have an indentation or logic error. Open the script and check that the path-conditional block is inside an `if/elif/else` structure, not three separate `if` statements. Fix and re-run.

**DISPOSITION**: Wrong path blocks visible in output = **PAUSE**. Sending an email with multiple path paragraphs visible reads as a template error to the recipient and damages credibility.

---

## Tree 3: Email Delivery Failures

**Symptom**: A bounce notification arrived, or you received an SMTP error when attempting to send.

**FIRST QUESTION**: Is this a bounce notification (arrived after sending) or an SMTP/send error (occurred while sending)?

### Branch 3A: Bounce notification received

**Q1**: Does the bounce notification contain a 5xx error code, or language like "address not found," "user does not exist," or "invalid recipient"?

- YES → Hard bounce. The address is permanently invalid. **PAUSE** sending to this contact. Protocol:
  1. Log the bounce in `DISTRIBUTION_EXECUTION_LOG.md` and `BATCH_1_CONTACT_LOG.md`.
  2. Visit the contact's institutional website. Check the "team" or "staff" page for a current email.
  3. If a new address is listed: update the log, resend within 24 hours.
  4. If no email is publicly listed: attempt the institutional general contact email (e.g., info@protectdemocracy.org) noting you are trying to reach [Name]. Alternatively, use Twitter/X direct message if the contact is active there.
  5. If two email attempts fail: log as "email delivery failed — social fallback" and use the social fallback.

  Batch-level escalation: If you receive 3 or more hard bounces in a single batch (above 8% bounce rate): **STOP** sending the remainder of that batch. Diagnose whether the batch has a data quality problem before continuing. See Tree 9.

- NO — contains 4xx error code, or language like "temporarily unavailable," "try again later," "mailbox full" → Soft bounce. Do not resend immediately. **CONTINUE** other sends. Wait 24 hours. If the same address soft-bounces again after 24 hours: treat as hard bounce and follow the Branch 3A hard-bounce protocol.

**Batch bounce rate escalation thresholds**:
| Bounce rate | Batch size | Threshold count | Action |
|-------------|------------|-----------------|--------|
| Above 8% | 5 (Batch 1) | 1 bounce | HIGH — re-verify all remaining Batch 1 addresses |
| Above 8% | 35 (Batch 2–5) | 3 bounces | PAUSE — data quality review before continuing |
| Above 15% | 35 | 5+ bounces | STOP — systematic data quality failure, see Tree 9 |

---

### Branch 3B: SMTP or send error

**Q1**: What does the error message say?

- "Authentication failed" or "password incorrect" → Your email client's credentials have expired (common after a password change or 2FA reset). Re-authenticate in your email client settings. Recovery: 5–10 minutes. **PAUSE** until resolved.

- "Could not connect to SMTP server" or "connection timed out" → SMTP server is temporarily unreachable. Check your internet connection. If connection is fine: check whether your email provider (Gmail, Protonmail) has a service incident at their status page. Wait and retry. Recovery: 5–30 minutes. **PAUSE** until resolved.

- "Daily send limit exceeded" → Gmail personal accounts: 500 emails/day. Gmail Workspace: 2,000/day. Phase 1 Batch 1 is 5 emails — this limit will not be reached in Phase 1. If this error appears, you are likely using a shared or restricted account. Switch to your primary sending account.

**DISPOSITION**: SMTP errors are all **PAUSE** — you cannot send until the connection is restored. None require STOP unless the account is permanently inaccessible.

---

### Branch 3C: Suspected spam filtering (no bounce, no response)

**Indicator**: No bounce received. No response after 7 days. Or a contact later mentions they did not receive your email.

This is not a confirmed failure — it is a hypothesis. Treat as non-response (Tree 4) unless confirmed by a contact.

**Pre-send prevention check** (run before Batch 1):
- [ ] Sending from a personal or institutional domain address (not Gmail/Yahoo for primary send)?
- [ ] Subject line has no all-caps words, no "FREE," "URGENT," "IMPORTANT"?
- [ ] Email body contains 2 or fewer links?
- [ ] Sending from your personal email client (not Mailchimp, ConvertKit, or other marketing platform)?
- [ ] Sending domain checked against MXToolbox blacklist (mxtoolbox.com/blacklists.aspx)?

If all boxes are checked: spam delivery is unlikely. If 1 or more are unchecked: address before Batch 1 send.

**If spam delivery suspected after send**: Follow up at Day 7 with: "I wanted to confirm this reached you — I sent a message on [date] about [topic]. Would you prefer I use a different channel?" **LOG** the follow-up and response (or non-response) in the tracking log.

---

## Tree 4: Non-Response

**Symptom**: No response has arrived from a contact. You are deciding whether this requires action.

**FIRST QUESTION**: How many days have passed since you sent the email?

### Branch 4A: Under the non-response window for this contact type

Non-response windows by contact type:
| Contact type | Non-response trigger day | Action |
|-------------|--------------------------|--------|
| Tier 1 Batch 1 (5 contacts) | Day 14 | Send one follow-up |
| Tier 1 broader (Batches 2–3) | Day 21 | Send one follow-up |
| Tier 2 state-level (Batches 4–5) | Day 30 | Send one follow-up |
| Domain 37 election-protection [PATH A+37] | Day 7 | Send one follow-up within 3 days of trigger |

**If you are still inside the non-response window** → **LOG** and continue. No action required. Check again at the trigger day.

---

### Branch 4B: At or past the non-response trigger day

**Q1**: Have you already sent one follow-up to this contact?

- YES — one follow-up sent, still no response → Close the contact as "no response — close" in the tracking log. Do not send a third email. Three contacts with no response from the same person damages sender credibility. **LOG** and move on.

- NO — no follow-up sent yet → Send exactly one follow-up using the template from Playbook Section 2.2. The follow-up should:
  - Reference the original email date
  - Include the Gist URL again
  - Offer an easy off-ramp ("if a different colleague would be a better contact, please let me know")
  - End with "no pressure either way"
  - Be shorter than the original email

  Log the follow-up date in the tracking spreadsheet. Set a reminder for 14 days after the follow-up.

---

### Branch 4C: Zero responses from Batch 1 after 14 days (early warning trigger)

This is not a single contact issue — it is a signal about the entire approach.

**Q1**: Did any of the 5 Batch 1 emails bounce?

- YES — one or more bounced → The apparent non-response may partly be a delivery failure. Resolve bounces (Tree 3A) before diagnosing engagement.

- NO — all 5 delivered (no bounces) → Proceed to Q2.

**Q2**: Are the Gist links in the emails working?

- Test the URLs from your sent email drafts. Do they load? If any Gist link is broken: this explains the non-response (recipients clicked to a 404). Resolve (Tree 1) and send corrected follow-up emails.

- All Gist links load correctly → Proceed to Q3.

**Q3**: Were the emails genuinely personalized, or do they read as a template with a name inserted?

- If you are not sure: re-read the sent drafts critically. Did each email reference a specific recent publication, case, or position of the contact? Or did it only use the contact's name and institution?

- Generic personalization → Before sending Batch 2, substantially revise the personalization. Each email should demonstrate you read something the contact published or worked on in the past 90 days.

- Strong personalization → The issue is likely timing or the subject line is not compelling. Revise the subject line approach for Batch 2.

**DISPOSITION**: Zero Batch 1 responses at Day 14 = **PAUSE** before Batch 2. Diagnose and adjust approach. Do not repeat the same email to 40 more contacts until you understand why 5 received no response.

---

## Tree 5: Engagement Failures — Opt-Outs and Hostile Responses

**Symptom**: A contact has replied asking not to be contacted, or has sent a hostile/dismissive response.

**FIRST QUESTION**: What did the contact say?

### Branch 5A: Explicit opt-out ("please do not contact me again")

**Action**:
1. Reply within 24 hours: "Understood — I will not contact you again. Apologies for the intrusion."
2. Mark as "opted out" in the tracking spreadsheet immediately.
3. Do not send a follow-up, a different angle, or a "just to clarify" message.

**LOG** the opt-out and any reason given (if they provided one).

**Pattern check**: If 3 or more contacts across all batches opt out:
- Check whether they share any characteristics (same sector, same tier, same framing of email).
- If they all received the same email template: the framing has a problem. Revise before the next batch.
- If they are spread across sectors and templates: likely individual preference mismatch. No template change needed.

**DISPOSITION**: Individual opt-out = **LOG**, **CONTINUE**. Three or more opt-outs = **PAUSE**, diagnose pattern, revise template before next batch.

---

### Branch 5B: Hostile or dismissive response (rude, condescending, or mocking)

**Action**:
1. Do not reply in kind. Do not argue.
2. If the hostility contains any specific substantive claim, log it for review — hostile responders sometimes identify real problems.
3. If it is purely dismissive with no content: reply only if a reply would serve a relationship purpose (e.g., if the contact is still potentially valuable and a gracious response could reset the interaction). Brief: "Thank you for your time." Otherwise: no reply required.

**DISPOSITION**: **LOG**. No impact on execution cadence.

---

### Branch 5C: Decline with redirect ("contact X at our organization instead")

This is a positive signal, not a failure.

**Action**:
1. Thank the contact who redirected you.
2. Identify the redirected contact.
3. Add them to the contact tracking spreadsheet under the same institution, marked as "internal referral from [contact name]."
4. Send a personalized email to the redirected contact, noting the referral: "Your colleague [Name] suggested I reach out to you directly about [topic]."

**DISPOSITION**: **LOG** as referral event. **CONTINUE** with elevated priority for the redirected contact.

---

## Tree 6: Institutional Feedback Surprises

**Symptom**: A contact has engaged substantively but in an unexpected or challenging way.

**FIRST QUESTION**: What type of challenge is this?

### Branch 6A: Framework scope is too broad to be actionable

**Immediate response** (send within 48 hours):
"The 35-domain scope reflects the research's diagnostic ambition. The five minimum-viable reforms in the executive summary are the near-term action set. Would a domain-specific deep dive be more useful for your work on [Domain X]?"

**If this feedback arrives from 3+ Tier 1 contacts independently**: The executive summary entry point needs clearer sequencing. Flag in `WORKLOG.md` as Phase 2 revision item. Do not modify domain content — modify the executive summary framing. **LOG**.

---

### Branch 6B: Specific methodology or framing challenge

**Q1**: Is the challenge a factual claim (the contact asserts specific data or events contradict the framework) or an interpretive disagreement (the contact prefers a different framing of the same evidence)?

- FACTUAL CLAIM → Verify against primary sources before responding. If the contact is correct: acknowledge the error, correct the Gist within 24 hours, thank the contact, log the correction in `WORKLOG.md`. If the contact is not correct: respond with the supporting source documentation.

- INTERPRETIVE DISAGREEMENT → Respond: "The framework supports this interpretation — though I recognize this is an active debate in the field. The underlying evidence I am working from is [sources]. I am interested in your counter-evidence if you have it." Do not revise framework content on the basis of a single interpretive objection.

**DISPOSITION**: Factual error confirmed = **PAUSE** (update Gist before continuing Gist-dependent sends). Interpretive disagreement = **LOG**, **CONTINUE**.

---

### Branch 6C: Framework interpreted as partisan advocacy

This is a credibility-sensitive scenario. The framework's institutional reach depends on its nonpartisan analytical framing.

**Q1**: Is the contact from an explicitly center-right or conservative institution (e.g., Cato, R Street, Niskanen)?

- YES → Take this critique seriously. Ask: "Can you identify the specific framing you found read as advocacy rather than analysis?" Listen for specific language, not general topic objection. If they identify specific phrases: assess whether those phrases can be reframed without changing the analytical conclusion. If yes, update the Gist. If the objection is to the topic itself rather than the framing: no revision warranted.

- NO → Still take seriously, but the threshold for revision is higher. Respond: "The framework analyzes what evidence from functioning democracies shows works. I am glad to discuss any specific framing you found read as partisan — that would help me strengthen the analysis."

**DISPOSITION**: Specific language identified that can be reframed neutrally = **PAUSE**, update Gist, **LOG**. General partisan objection = **LOG**, **CONTINUE**.

---

### Branch 6D: Contact requests domain content modification

**Q1**: Is the request based on new evidence the contact has (data, cases, developments not in the framework) or on policy preference (they prefer a different approach to the same problem)?

- NEW EVIDENCE → High value. Request the specific source. Assess whether it changes the analysis: if yes (it corrects a gap or error), update the Gist and notify the contact. If it is additive but not corrective, log it as a Phase 2 domain update item.

- POLICY PREFERENCE → Acknowledge the position: "Your organization's position on [X] is noted and I am glad to discuss the comparative evidence. The framework reflects one evidence-based approach; I welcome the debate." Do not modify content on the basis of a preference without supporting evidence.

- SAME MODIFICATION REQUEST FROM 3+ INDEPENDENT EXPERTS → This is a Phase 2 structural review signal. Log in `WORKLOG.md`, flag for Phase 2 domain revision. Do not revise during Phase 1 distribution — it creates version confusion for contacts who already received the earlier Gist.

---

### Branch 6E: Contact misreads the framework to reach unsupported conclusions

**Action**: Clarify promptly and privately. Send a correction within 24 hours: "The framework's [Domain X] analysis [does/does not] support [conclusion]. The specific section is: [link + quote of the relevant passage]."

Do not create a public dispute. One private correction is sufficient. If the contact publishes the misreading publicly despite your private correction, respond publicly with a brief, direct factual clarification (no more than 2 sentences) and a link to the relevant section.

**DISPOSITION**: **LOG**. **CONTINUE** unless the misreading is public and spreading, in which case: **PAUSE** other sends while you draft and send a correction (estimated 30 minutes).

---

## Tree 7: Channel Failures

**Symptom**: A distribution channel (Substack, Reddit, social media) is not working as expected.

### Branch 7A: Substack

**Q1**: Is this a login/access failure or a send failure?

- LOGIN FAILURE → Use account recovery (email or phone). Substack support response: 24–48 hours. Phase 1 Substack Post 1 is scheduled for T+7 — a 24-hour recovery delay does not materially affect the timeline. **CONTINUE** email sends. Return to Substack after recovery.

- POST NOT SENDING or delivery looks like it failed → Check https://status.substack.com. If platform incident: wait. If no incident: check whether the post was saved as Draft vs. Published. Re-publish if needed. Verify the subscriber list has at least one confirmed subscriber (yourself) before testing delivery.

- OPEN RATES ANOMALOUSLY LOW → This is a measurement issue, not necessarily a delivery failure. Some email clients block tracking pixels. Low open rates on Substack may mean Gmail "Promotions" tab filtering. Not directly fixable. **LOG**. Focus on direct reply counts rather than open rates as the primary engagement metric.

**DISPOSITION**: Substack issues are secondary channel failures. **CONTINUE** primary email sends. Address Substack in parallel.

---

### Branch 7B: Reddit

**Q1**: Was the post removed (deleted by moderators) or did it never appear (filtered before posting)?

- REMOVED → Common causes and next steps:
  - Subreddit age/karma requirements: if your account is under 30 days old, find subreddits without stated participation thresholds.
  - Self-promotion flag: reframe the post as a question or discussion prompt, put the Gist link in a comment rather than the post body.
  - General spam filter: participate in 3–5 substantive comment threads in the target subreddit before attempting a new post.
  Wait 24 hours before reposting. **CONTINUE** other distribution channels.

- NEVER APPEARED (posted but invisible to others) → Shadow removed. Same remediation as above. **LOG**, try repost after 24 hours with revised framing.

- LINK BLOCKED → Post as text-only, include the URL as plain text (not a hyperlink) within the body. GitHub Gist links are not typically on Reddit's blocked-domain list; this is likely an account reputation issue. **CONTINUE**.

**DISPOSITION**: Reddit is a tertiary distribution channel. Any single Reddit failure: **LOG**, retry once with adjusted approach. Do not invest significant time debugging Reddit filtering.

---

### Branch 7C: Email system classified as bulk

**Symptom**: You suspect institutional spam filters are routing your emails to bulk/promotions folders.

**Prevention checklist** (run before Batch 1):
- [ ] Not using email tracking pixels
- [ ] Subject line uses the contact's name and a specific topic (not newsletter-style)
- [ ] Sending from personal email client (not a marketing platform)
- [ ] Email body is under 400 words
- [ ] No more than 2 links in the email body

If all boxes checked: bulk classification is unlikely. If not: address the unchecked items before sending.

**If bulk classification suspected after send**: Follow up via LinkedIn or Twitter/X to confirm receipt. **LOG**. **CONTINUE**.

---

## Tree 8: Coordination Failures

**Symptom**: You may have sent a duplicate, or contacts from different batches are getting confused.

### Branch 8A: Possible duplicate send (same email sent twice to same person)

**Q1**: Check the tracking spreadsheet. Does the contact have more than one "sent" entry for the same template?

- YES → Accidental duplicate confirmed. Send a brief apology within 24 hours: "I inadvertently sent you a duplicate of my earlier email — apologies for the repetition. Please disregard the second copy." Keep it to one sentence. **LOG**.

- NO → Likely not a duplicate. Check if the contact appears in both Phase 1a and Phase 1b lists [PATH A+37]. If so: review whether the two emails are distinct (they should be — one is the general framework, one is the Domain 37 standalone). If they are distinct: not a failure, no action needed.

**Systematic duplicate prevention**: Before each batch send, filter the batch contact list against the "date sent" column in the tracking spreadsheet. Any contact with a date in that column has already been sent an email. Do not send again unless it is a deliberate follow-up.

---

### Branch 8B: Phase 1b sent before Phase 1a for the same contact [PATH A+37]

**Symptom**: One of the three crossover contacts (Weiser, Elias, Bassin) received the Domain 37 targeted email before receiving the general framework email.

This reverses the intended credibility-building sequence. The general framework email is the credential; the Domain 37 email is the targeted follow-up that assumes the credential.

**Response**: Send the Phase 1a general framework email immediately, with a brief note acknowledging the reversal: "I realize I sent you the Domain 37 briefing first — this is the broader framework it draws from. The general framework is the context for the targeted follow-up." This is a minor awkwardness, not a disqualifying error. **LOG**.

**Prevention for remaining Phase 1b contacts**: Phase 1b sends do not begin until Batch 1 Phase 1a emails are confirmed sent (Block 9 of checklist is Phase 1b prep only — drafts not sent on Day 0).

---

### Branch 8C: Version mismatch — Gist was updated after emails were sent

**Symptom**: You updated a domain source file and the Gist. Some contacts received the pre-update version via email.

**Q1**: Was the update a factual correction (errors removed) or an additive update (new material added)?

- FACTUAL CORRECTION → Notify contacts who already received the Gist link by email: "I updated [Document] on [date] to correct [specific issue]. The link you received now points to the updated version." This is worth a brief email to Batch 1 contacts. The Gist URL is the same — the correction is live at the original URL, which they already have. **LOG** the update in `WORKLOG.md`.

- ADDITIVE UPDATE → No notification required for most contacts. If a contact is actively using the Gist in a publication or litigation context [PATH A+37 Domain 37 specifically]: notify them directly. **LOG**.

---

## Tree 9: Data Quality Issues

**Symptom**: Contact information appears wrong, outdated, or inconsistent.

### Branch 9A: Hard bounce received — possible stale entry

**Q1**: Visit the contact's institutional website (staff/team page). Is the contact still listed at the institution?

- NO — person is no longer at the institution → Stale entry confirmed. Log departure in tracking spreadsheet. Find the most appropriate current contact at the same institution (deputy director, co-director, or institutional contact email). Assess whether the institutional relationship priority justifies finding a replacement:
  - Tier 1 institution: Yes — identify replacement and send within 7 days.
  - Tier 2 institution: Yes, if time permits.
  - Tier 3 institution: Low priority — skip and continue with higher-priority contacts.

- YES — still listed but email bounced → The institutional email format may have changed (org migration). Check the staff page for a contact email or use the institutional general inquiry address. Update the tracking spreadsheet.

---

### Branch 9B: Multiple bounces clustering in one sector

**Symptom**: 3 or more bounces from contacts in the same institutional sector (all think tanks, all law schools, all federal advocacy orgs).

**Q1**: Is there a common pattern in the bouncing addresses?

- Same domain format (e.g., all @organizationname.org rather than @org.org) → Possible domain migration. Search for "[organization name] email domain change" or "[organization name] new domain." If a migration is confirmed: update all affected contacts to the new domain format.

- Different domains but all from the same sector → Contact list for this sector is stale. **PAUSE** sends to this sector. Batch-verify all contacts in the sector against current institutional websites before continuing.

---

### Branch 9C: Contact data is missing required fields (domain relevance score, personalization notes)

**Q1**: Is this contact scheduled for the current batch or a future batch?

- CURRENT BATCH → Do not send to this contact without a domain relevance assessment. Remove from the current batch and move to the next batch. A generic email to a Tier 1 institutional contact is worse than no email. Complete the assessment (10–15 minutes per institution) before including the contact.

- FUTURE BATCH → Add a reminder to complete the assessment before that batch's send date. **LOG**.

---

## Tree 10: Metrics and Success Signals

**Symptom**: Something about the numbers looks wrong, or you are not sure whether Phase 1 is working.

### Branch 10A: No day 0 baseline was recorded

Without a baseline, you cannot interpret whether current Gist view counts mean anything.

**Immediate action**: Even if Day 0 has passed, record the current counts as the earliest available baseline. Note in `DISTRIBUTION_EXECUTION_LOG.md` that the baseline was recorded on [date] rather than before the first send. Imperfect baseline data is still better than none.

---

### Branch 10B: Gist view counts are very low after 7 days

**Q1**: Were Batch 1 emails confirmed sent (no SMTP errors, no bounces)?

- NO SMTP errors, but no bounces either, AND Gist views are flat → Suspected spam/bulk filtering or low open rates. Run the spam-prevention checklist in Tree 7C. If all boxes are checked and views are still flat: the email subject line or body call-to-action is not compelling enough to generate clicks. Assess the CTA before Batch 2.

- One or more bounces received → Bounce addresses did not receive the Gist link. Adjust view count expectation accordingly (1 bounce in Batch 1 of 5 = 20% of your Batch 1 links were never received).

**Minimum thresholds**:
| Metric | 7-day floor | If below floor |
|--------|-------------|----------------|
| Gist views (Proposal) | 20 | Diagnose link clickthrough |
| Batch 1 non-bounce delivery | 4 of 5 | Diagnose data quality |
| Batch 1 engagement (open or reply) | 1 of 5 | Review subject line and personalization |

---

### Branch 10C: Strong engagement on one contact, silence from all others

**Symptom**: One Batch 1 contact responded substantively; four are silent at Day 14.

This is a good sign, not a failure. One substantive response from Batch 1 confirms: the framework is coherent, the links work, the framing is credible to at least one expert. The other four contacts may be working on longer response cycles.

**Action**: Proceed to Batch 2 with confidence. The one responsive contact's institutional endorsement (even informal, in a private email) is usable: "I shared this framework with [Name] at [Institution], who [specific positive signal — e.g., raised a follow-up question about Domain 6]."

---

### Branch 10D: Early green flags — what to do when things go well

If you observe any of the following signals in the first 14 days, do not just continue — amplify.

| Green flag | Amplification action |
|-----------|---------------------|
| Contact offers to forward internally | Ask: "Is there a specific colleague I should send this to directly?" |
| Contact asks a substantive domain question | Respond with depth. This contact is reading seriously. Consider whether this is a Phase 2 candidate for deeper collaboration. |
| Gist link shared on social media | Repost and thank (by name if appropriate). Log the share. |
| Secondary distribution (forwarded to colleague) | Add the referred contact to the next batch with a note: "referred by [name]." Respond to the referrer to close the loop. |
| [PATH A+37] Election-protection org requests more Domain 37 data | Respond within 24 hours. This is a live operational use case. |

Secondary distribution is the most valuable early signal in Phase 1. Track every instance. A forwarded referral converts a cold outreach into a warm introduction.

---

### Branch 10E: Zero responses at Day 14 from Batch 1 (full early warning assessment)

Already covered in Tree 4, Branch 4C. Summary for quick reference:

1. Confirm delivery (no hidden bounces, no Gist link errors).
2. Confirm Gist links work.
3. Audit personalization quality.
4. Audit subject lines.
5. **PAUSE** before Batch 2. Adjust approach based on diagnosis. Do not repeat the same strategy to 40 more contacts without understanding why 5 generated zero response.

---

## Quick Reference: Severity and Disposition Matrix

| Failure type | Severity | Disposition | Max fix time |
|--------------|----------|-------------|-------------|
| GitHub platform outage | CRITICAL | STOP | External — wait |
| GitHub account suspended | CRITICAL | STOP | 30 min (mirror) |
| Gist accidentally deleted | HIGH | PAUSE | 15 min |
| Wrong URL in draft | HIGH | PAUSE | 2 min |
| Template placeholder unfilled (automatic) | HIGH | PAUSE | 10 min |
| Wrong path block in output | HIGH | PAUSE | 5 min |
| Hard bounce — Batch 1 | HIGH | PAUSE | 30 min |
| Hard bounce rate above 8% | HIGH | PAUSE | 1–2 hrs |
| Hard bounce rate above 15% | CRITICAL | STOP | data audit |
| SMTP authentication failure | HIGH | PAUSE | 10 min |
| Soft bounce | MEDIUM | CONTINUE (24-hr wait) | 0 min now |
| Non-response (within window) | LOW | LOG | — |
| Non-response (at trigger day) | MEDIUM | CONTINUE | 10 min (follow-up) |
| Zero Batch 1 response at Day 14 | HIGH | PAUSE | 30 min (diagnosis) |
| Opt-out received | LOW | LOG | 5 min (reply) |
| Three or more opt-outs | MEDIUM | PAUSE | 30 min (diagnosis) |
| Hostile response, no substance | LOW | LOG | — |
| Constructive critique, factual | HIGH | PAUSE (verify) | 1–2 hrs |
| Constructive critique, interpretive | LOW | LOG | — |
| Framework scope objection | LOW | LOG | 10 min (response) |
| Partisan framing objection (center-right source) | MEDIUM | PAUSE (assess) | 30 min |
| Substack login failure | MEDIUM | CONTINUE (secondary) | 24 hrs |
| Reddit post removed | LOW | LOG | 24 hrs (retry) |
| Suspected spam filtering | LOW | LOG | — |
| Accidental duplicate send | MEDIUM | CONTINUE | 5 min (apology) |
| Phase 1b before Phase 1a [A+37] | MEDIUM | CONTINUE | 10 min |
| Stale contact — individual | MEDIUM | CONTINUE | 15–30 min |
| Stale contact — sector cluster | HIGH | PAUSE | 1–2 hrs |
| Missing domain relevance score | MEDIUM | PAUSE (this contact) | 10–15 min |
| Gist views below floor at Day 7 | MEDIUM | PAUSE (before Batch 2) | 30 min |

---

*Failure Mode Decision Tree — Created May 6, 2026. Companion document: `phase-1-launch-risk-playbook.md`. Use this for rapid triage; use the playbook for full context on each failure type.*
