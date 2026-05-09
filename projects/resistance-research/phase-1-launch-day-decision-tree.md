---
title: "Phase 1 Launch Day Decision Tree — Rapid Triage Reference"
created: 2026-05-09
status: production-ready
purpose: "Single-page 30-second lookup for launch-day triage. Identifies symptom, maps to failure mode, returns protocol. For full protocols, see the companion documents below."
companion_docs:
  - phase-1-execution-contingency-playbook.md (SLAPP, scaling, reputational)
  - phase-1-launch-risk-playbook.md (technical, engagement, channel)
  - failure-mode-decision-tree.md (deep technical triage, Trees 1-10)
---

# Phase 1 Launch Day Decision Tree

**Format**: Identify your symptom in the index. Go to the matching tree. Answer binary questions until you reach a disposition. Each disposition links to the full protocol.

**Dispositions**:
- STOP — Halt all sends. Resolve before continuing.
- PAUSE — Finish current email. Resolve before next send.
- CONTINUE — Resolve in parallel with execution. No cadence change.
- LOG — Record and carry on. No immediate action.
- ESCALATE — Bring to user. Do not proceed without user input.

**Time budget**: This document is calibrated for under 30 seconds per lookup. If triage takes longer, you are in the wrong tree — use the companion documents.

---

## INDEX

| Symptom | Tree |
|---------|------|
| Gist URL not loading, 404 error | A |
| Email bounced or SMTP error | B |
| Domain blocklist suspected | C |
| No response from contacts | D |
| Hostile or negative reply received | E |
| Cease-and-desist or legal communication received | F |
| Template still shows {{placeholders}} | G |
| Substack formatting broken | H |
| Inbox flooded with replies | I |
| Press inquiry received | J |
| Framework misrepresented in media or online | K |
| Something else is wrong | L |

---

## Tree A — Gist URL Not Loading

**Is github.com reachable?** (visit github.com)

```
NO → GitHub is down.
     STOP. Do not send emails with Gist links.
     Monitor https://githubstatus.com
     Resume when GitHub confirms incident resolved.
     [Playbook: failure-mode-decision-tree.md Tree 1A]

YES ↓

Is the esca8peArtist account page loading?
(visit gist.github.com/esca8peArtist)

NO → Account suspended.
     STOP. Immediately create mirror Gists under backup account.
     Update DISTRIBUTION_GIST_URLS.md with new URLs.
     Re-run fill_templates.py with new URLs before any send.
     ESCALATE if no backup account available.
     [Playbook: failure-mode-decision-tree.md Tree 1A Q3]

YES — account loads but specific Gist is missing ↓

Was the Gist accidentally deleted?
(check if listed on account page)

YES — missing from account → PAUSE.
     Recreate from source in /projects/resistance-research/
     Record new URL in DISTRIBUTION_GIST_URLS.md.
     Recovery: 10-15 min per Gist.

NO — listed but link is wrong in your draft → PAUSE.
     Correct URL in email draft against DISTRIBUTION_GIST_URLS.md
     Recovery: 2 min.
```

---

## Tree B — Email Bounced or SMTP Error

**Did a bounce notification arrive (email after send) or did an error appear while sending?**

```
BOUNCE NOTIFICATION received ↓

Contains "5xx", "address not found", "user does not exist"?

YES → HARD BOUNCE. PAUSE sending to this contact.
     Visit institutional website — is there a new address?
     YES → Update log. Resend to new address within 24h.
     NO → Try institutional general address or social media.
     If 2 attempts fail → LOG "email delivery failed — social fallback."
     
     BATCH CHECK: Is bounce rate above 8% of this batch?
     YES → PAUSE full batch. Diagnose data quality.
     Is bounce rate above 15%?
     YES → STOP. ESCALATE.
     [Playbook: phase-1-launch-risk-playbook.md Section 1.3]

Contains "4xx", "try again later", "mailbox full"?

YES → SOFT BOUNCE. CONTINUE other sends.
     Wait 24 hours. Resend manually after 24h.
     If same address soft-bounces again → treat as hard bounce.

SMTP ERROR while sending ↓

"Authentication failed" or "password incorrect"?
YES → Re-authenticate in email client settings. PAUSE until resolved. 5-10 min.

"Could not connect" or "connection timed out"?
YES → Check internet and email provider status. PAUSE until resolved. 5-30 min.

"Daily send limit exceeded"?
YES → Switch to primary sending account (Phase 1 volumes do not hit Gmail limits).
     [Playbook: failure-mode-decision-tree.md Tree 3B]
```

---

## Tree C — Domain Blocklist Suspected

```
Have you run MXToolbox before this send?
(mxtoolbox.com/blacklists.aspx on your sending domain)

NO → Run it now. Takes 2 minutes.
     PAUSE this send until check is complete.

YES — blocklist detected ↓

Is Phase 1 distribution already in progress?

NO → Switch sending address to Gmail or Protonmail for Phase 1.
     Note domain issue in email signature.
     CONTINUE.

YES, emails already sent from blocked domain → 
     Switch address for Batch 2 and beyond.
     For Batch 1 bounces: wait 48h, resend from alternate address.
     LOG in DISTRIBUTION_EXECUTION_LOG.md.
     [Playbook: phase-1-execution-contingency-playbook.md Section 2.2]
```

---

## Tree D — No Response From Contacts

**How many days have passed since you sent the email?**

```
Under the non-response window for this contact type? ↓

Tier 1 Batch 1: < 14 days → LOG. No action.
Tier 1 broader: < 21 days → LOG. No action.
Tier 2 state-level: < 30 days → LOG. No action.
Domain 37 election-protection: < 7 days → LOG. No action.

AT or PAST the non-response window ↓

Have you already sent one follow-up?

YES → Close contact as "no response — close" in log.
      Do not send a third email. LOG. CONTINUE.

NO → Send one follow-up using template:
     "I wanted to follow up briefly on my email from [date].
     Summary is here: [Gist URL].
     If a different colleague would be a better contact, please let me know.
     No pressure either way. — [Name]"
     LOG the follow-up. Set reminder for 14 days.

SPECIAL CASE: Zero responses from all 5 Batch 1 contacts at Day 14 ↓

Confirm: were emails delivered without bounces?
NO → Resolve delivery issue first. See Tree B.

YES, delivered but no response →
Are Gist links in sent emails working?
NO → Link breakage. Send corrected follow-up. See Tree A.
YES → Audit personalization quality before Batch 2.
      PAUSE Batch 2 until diagnosis complete.
      [Playbook: failure-mode-decision-tree.md Tree 4C]
```

---

## Tree E — Hostile or Negative Reply Received

**What did the contact say?**

```
Explicit opt-out ("do not contact me again") ↓
   Reply within 24h: "Understood — I will not contact you again."
   Mark as opted out in tracking spreadsheet immediately.
   LOG.
   
   If 3+ opt-outs total across all batches →
   PAUSE before next batch. Check if opt-outs share a pattern.
   Revise template if same email framing is linked to opt-outs.

Hostile/dismissive (rude, condescending, no specific claim) ↓
   Do not argue. Do not reply unless a gracious reply serves a relationship purpose.
   If you reply: "Thank you for your time." One sentence.
   LOG. CONTINUE.

Policy-based institutional rejection ↓
   Reply within 24h: "Thank you for the response. I understand your distribution
   policies. If you find the research useful for internal review, the link remains
   publicly available: [Gist URL]."
   Do not modify framework. LOG. CONTINUE.

Substantive critique of methodology or content ↓
   Is this a factual claim or an interpretive disagreement?
   
   FACTUAL → Verify against primary sources before responding.
              If contact is correct: correct the Gist, thank the contact, LOG correction.
              If contact is wrong: respond with source documentation.
              PAUSE if Gist correction is needed before more sends.
   
   INTERPRETIVE → Respond acknowledging the debate.
                  Do not revise framework on single interpretive objection.
                  LOG. CONTINUE.
   [Playbook: failure-mode-decision-tree.md Tree 6B]
```

---

## Tree F — Legal Communication Received

**This tree is for any communication from an attorney or any document using legal demand language.**

```
Have you confirmed this is a real legal communication?
(letterhead, attorney name and bar number, specific legal theory stated)

NO — looks like template or informal demand → 
     Treat as hostile response. See Tree E.
     LOG. Monitor for escalation.

YES — confirmed legal communication ↓

ESCALATE IMMEDIATELY. Do not respond. Do not comply. Do not forward publicly.

Notify user within 24 hours with:
- What arrived (cease-and-desist, attorney letter, other)
- The specific claim made (defamation, copyright, other)
- Whether the claim identifies a specific factual error in the framework

While waiting for user direction:
- Do NOT cease distribution
- Do NOT delete Gists or documents
- Do NOT respond to the sending attorney

User will assess with legal resources:
- EFF (eff.org/issues/bloggers/legal) — online speech / defamation
- Reporters Committee (rcfp.org) — SLAPP and media law
- ACLU state affiliates — first amendment representation
- Public Participation Project (anti-slapp.org) — SLAPP referrals

Remember: A cease-and-desist letter has no legal authority on its own.
It is a demand, not a court order.
40 states have anti-SLAPP statutes enabling early dismissal of suits 
targeting public-interest speech.
[Playbook: phase-1-execution-contingency-playbook.md Section 3.2 Type 3]
```

---

## Tree G — Template Still Shows {{Placeholders}}

```
Search output files for "{{". How many placeholders remain?

Only manual placeholders remain?
({{RECENT_JUST_SECURITY_ARTICLE}}, {{RECENT_WEISER_PUBLICATION}}, etc.)
→ This is correct. These are filled by hand in Block 6 (email client draft).
   CONTINUE.

Automatic placeholders remain?
({{YOUR_NAME}}, {{PROPOSAL_URL}}, {{DOMAIN_37_URL}}, etc.) ↓

Did the script run without errors?
NO → Read error message. Fix syntax in FIELD_VALUES dict. Re-run. PAUSE.

YES — ran but placeholder remains →
Did you set the value in FIELD_VALUES for this placeholder?
NO → Add the value. Re-run. PAUSE.
YES — value is set but placeholder remains →
Check that the key in FIELD_VALUES matches the placeholder exactly
(case-sensitive, character-for-character). Correct and re-run. PAUSE.

PATH A+37 only: {{DOMAIN_37_URL}} still empty?
→ Block 2 (Domain 37 Gist creation) not yet complete.
   Complete Block 2 first, then return to Block 3.
   [Playbook: failure-mode-decision-tree.md Tree 2]
```

---

## Tree H — Substack Formatting Broken

```
Is this a login failure or a formatting/rendering problem?

LOGIN FAILURE →
   Use account recovery (email or phone).
   Substack support response: 24-48h.
   Phase 1 Substack Post 1 is scheduled T+7 — 24h delay is not critical.
   CONTINUE email sends. Return to Substack after recovery.

FORMATTING BROKEN (tables render as raw text, headers missing) ↓

Has the post been sent as email to subscribers yet?

NO → Edit post. Remove Markdown table. Rebuild using Substack's native table tool.
     Check both web preview and email preview before confirming.
     PAUSE Substack publish. CONTINUE primary email sends.

YES, already sent ↓
   Email cannot be recalled.
   Publish brief follow-up post: "The table in the previous post rendered incorrectly.
   Formatted version is at [Gist URL]."
   LOG. CONTINUE.

Note: Substack is a secondary channel. Formatting failures here do not affect
primary institutional email outreach.
[Playbook: phase-1-execution-contingency-playbook.md Section 4.1]
```

---

## Tree I — Inbox Flooded With Replies

```
How many replies are arriving per day?

Under 10/day → Normal response volume. Proceed with standard response windows.
               Tier 1: 24h. Tier 2: 48h. Tier 3: 7 days with template.

10-15/day → CONTINUE with triage template for Tier 3 contacts.
            Template: "Thank you. Framework is at [Gist URL]. I will add you to
            Phase 2 notification list. What domain area is most relevant to your work?"
            LOG all contacts in tracking spreadsheet.

Above 15/day for 3+ consecutive days → ESCALATE.
Secondary distribution is happening at scale beyond solo-operator capacity.

SPECIAL CASE: Replies from contacts not in your contact list ↓
   These are secondary distribution contacts — someone forwarded the framework.
   Treat same as primary contacts for response triage.
   LOG each secondary contact: who forwarded it (if mentioned), their institution.
   Do not proactively reach out — they already have the framework.
   ESCALATE if they represent a significantly different institutional audience than
   Phase 1 targets (e.g., state legislative staff, international organizations).
   [Playbook: phase-1-execution-contingency-playbook.md Section 5.2, 5.4]
```

---

## Tree J — Press Inquiry Received

```
What type of press inquiry is this?

Background request (journalist reviewing framework for possible coverage) ↓
   Respond within 2 hours:
   "Thank you for your interest. The full framework is publicly available at [Gist URL].
   I am available for a background conversation — please share your availability
   and I will follow up within 24 hours."
   LOG as "press interest" for Phase 2 amplification.
   AUTONOMOUS.

On-record interview request (wants quotes or interview for publication) ↓
   ESCALATE within 2 hours.
   Respond to journalist: "Thank you — I will be in touch within 24 hours regarding
   availability."
   Do not grant interview or provide quotes until user is involved.

Partnership or coordination request (offer to promote in exchange for joint messaging) ↓
   ESCALATE.
   No exclusive arrangements or messaging coordination for Phase 1.

MORE THAN 3 PRESS INQUIRIES within 7 days ↓
   ESCALATE immediately. Framework is being amplified by a high-reach source.
   Prepare one-paragraph written statement (see Section 5.3 of main playbook).
   Do not grant any on-record statements without user.
   [Playbook: phase-1-execution-contingency-playbook.md Section 5.3]
```

---

## Tree K — Framework Misrepresented in Media or Online

```
Where is the misrepresentation appearing?

Single social media post, account with under 5,000 followers ↓
   Is it being actively amplified (50+ retweets or shares)?
   NO → LOG. Do not correct. Correcting amplifies low-reach errors.
   YES → See below (amplifying misrepresentation).

Social media post being amplified (50+ retweets, boosted by large account) ↓
   Post a public correction thread:
   1st: "[Framework name] [Gist URL]: [1-2 sentence factual correction]."
   2nd: "The full analysis of [Domain X] is at: [specific section link]."
   3rd: "I am available to discuss methodology with researchers or journalists."
   Do not tag the misrepresenting account unless they are prominent and the
   misrepresentation will continue spreading without direct correction.
   AUTONOMOUS (under 280 characters, factual).
   ESCALATE if correction would itself create reputational risk.

Media outlet (institutional reach, publication with >50K monthly readers) ↓
   ESCALATE within 2 hours of detection.
   Prepare written correction request to outlet's editor:
   - Specific claim that is incorrect
   - Correct information with source citations
   - Gist URL for full framework
   - Request correction note be appended to original article.

High-stakes attribution error (official or organization invokes framework to
justify a position the framework explicitly contradicts) ↓
   ESCALATE immediately.
   Prepare public clarification statement.
   If the misusing party is a Phase 1 contact: reach out privately first.
   Issue public clarification within 24 hours if active harm is occurring.
   [Playbook: phase-1-execution-contingency-playbook.md Section 6.2]
```

---

## Tree L — Something Else Is Wrong

If your symptom is not in the index:

1. Is it a technical problem (something is broken or not loading)? → See `failure-mode-decision-tree.md` for comprehensive technical trees.

2. Is it a contact engagement problem (a response you did not expect)? → See `phase-1-launch-risk-playbook.md` Sections 2-3 for full engagement protocols.

3. Is it a legal communication of any kind? → Go to Tree F immediately.

4. Does it require spending money, making a public commitment, or creating an irreversible record? → ESCALATE before acting.

5. Is it a judgment call about the framework's strategic direction? → ESCALATE.

6. Everything else: LOG and CONTINUE. Most unexpected events during a Phase 1 distribution are noise, not signal. The signal is sustained pattern, not individual events.

---

## Quick Severity Reference

| What you're seeing | Severity | First action |
|-------------------|----------|-------------|
| GitHub down | CRITICAL | STOP |
| GitHub account suspended | CRITICAL | STOP + ESCALATE |
| Gist deleted | HIGH | PAUSE |
| Hard bounce (individual) | HIGH | PAUSE |
| Hard bounce rate >15% | CRITICAL | STOP + ESCALATE |
| SMTP auth failure | HIGH | PAUSE |
| Template unfilled (automatic) | HIGH | PAUSE |
| Legal communication any kind | HIGH | ESCALATE immediately |
| Inbox >15/day sustained | HIGH | ESCALATE |
| Press on-record request | HIGH | ESCALATE |
| Media outlet misrepresentation | HIGH | ESCALATE |
| High-stakes attribution error | HIGH | ESCALATE |
| Soft bounce | MEDIUM | CONTINUE (wait 24h) |
| Non-response (within window) | LOW | LOG |
| Zero Batch 1 response Day 14 | HIGH | PAUSE Batch 2 |
| Opt-out received | LOW | LOG |
| 3+ opt-outs | MEDIUM | PAUSE |
| Policy-based decline | LOW | LOG |
| Substack formatting broken | MEDIUM | CONTINUE primary sends |
| Reddit post removed | LOW | LOG |
| Secondary distribution | LOW | LOG (ESCALATE if large scale) |
| Social media misrepresentation | LOW-MEDIUM | LOG or correction thread |
| Press background inquiry | LOW | AUTONOMOUS response |

---

*Launch Day Decision Tree — Created May 9, 2026. Use for rapid triage under 30 seconds. For full protocols: `phase-1-execution-contingency-playbook.md` (SLAPP, scaling, reputational); `phase-1-launch-risk-playbook.md` (technical, engagement); `failure-mode-decision-tree.md` (comprehensive technical trees).*
