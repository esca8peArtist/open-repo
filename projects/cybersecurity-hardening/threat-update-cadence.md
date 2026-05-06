---
title: "Threat Update Cadence: Maintenance Schedule for Tier 2 Threat Intelligence"
project: cybersecurity-hardening
created: 2026-05-06
status: operational
purpose: >
  Establishes the maintenance schedule, update triggers, and distribution
  process for refreshing threat intelligence across the Tier 2 briefing set
  mid-campaign and post-campaign. Ensures briefings remain accurate and
  credible through the Tier 2 distribution window and into ongoing use.
---

# Threat Update Cadence

## Purpose

The Tier 2 threat briefings are dated May 2026 and grounded in a specific threat landscape. That landscape will shift. This document establishes:

1. A scheduled review cadence (when to look, regardless of specific events)
2. An event-triggered update protocol (what forces an immediate update)
3. A process for pushing mid-campaign updates to Tier 2 recipients already reached
4. A long-term sustainability model for keeping the corpus current beyond the initial distribution

---

## Why Cadence Matters

Threat briefings that go stale are worse than no briefing. An organization that adopts practices based on your May 2026 analysis and then finds that a cited statute has changed or a referenced tool has been patched will lose confidence in the full corpus. The goal of this cadence is not to update for its own sake — it is to ensure that every claim in every briefing remains defensible at the moment it reaches a new reader.

The campaign timeline runs approximately 6–8 weeks from Tier 1 execution through Tier 2 completion. After that, the corpus continues to circulate. Plan for two distinct update phases: **in-campaign** (while actively sending) and **post-campaign** (ongoing maintenance).

---

## Scheduled Review Cadence

### In-Campaign Schedule (May–July 2026)

| Review Date | Scope | Who Does It |
|-------------|-------|-------------|
| June 5, 2026 | FISA 702 status check; pre-deadline review | Primary researcher |
| June 13, 2026 | FISA 702 outcome; update all briefings' policy advocacy sections | Primary researcher |
| July 1, 2026 | Full briefing set review: 30-day check | Primary researcher |
| August 1, 2026 | Full briefing set review: 60-day check | Primary researcher |

### Post-Campaign Schedule (August 2026 onward)

| Review Frequency | Scope |
|-----------------|-------|
| Monthly (first week of each month) | Scan primary source categories below; document any changes in update log |
| Quarterly (September, December 2026, March 2027) | Full briefing accuracy review; update any stale claims |
| Event-triggered | See triggers section below — these supersede the monthly scan |

**Monthly scan takes approximately 2–3 hours** if scoped properly. The target is not comprehensive research — it is confirming that specific claims in specific briefings remain accurate. Use the Primary Source Check List below to structure the scan.

---

## Primary Source Check List

These are the sources that underpin time-sensitive claims. Check these directly on each monthly scan cycle.

### Legal and Legislative Sources

| Claim | Source to Check | What Changed Would Invalidate It |
|-------|----------------|----------------------------------|
| FISA Section 702 status | Security Boulevard, Congress.gov, Wyden press releases | Reauthorization with or without warrant reform; new deadline |
| IRS–ICE data sharing litigation | PACER (D.C. Circuit docket); Tax Notes | Injunction reinstated; case dismissed; appeal decided |
| Government Surveillance Reform Act (S.4082) | Wyden Senate press page; congress.gov | Bill passed; bill failed; new companion legislation |
| State legislation (polling place protections, 7 states) | Democracy Docket; state legislature tracking | State bills passed or failed |
| ACLU voter database lawsuit | ACLU case page | Injunction issued; case decided |

### Threat Actor and Capability Sources

| Claim | Source to Check | What Changed Would Invalidate It |
|-------|----------------|----------------------------------|
| ProKYC platform operational status | Cato CTRL blog; Biometric Update; dark web market monitoring (if available) | Platform taken down; pricing changed; new capability added |
| Shai-Hulud / TeamPCP campaign status | Microsoft Security Blog; Endor Labs; Socket.dev | New wave; campaign dormant; new attacker attributed |
| Bitwarden CLI compromise: remediation complete | Bitwarden official blog; Endor Labs | Follow-on incidents; incomplete remediation |
| LogoFAIL / BootKitty patch status | Binarly fwcheck blog; major vendor BIOS release notes | Widespread exploitation confirmed; patch deployed at scale |
| ELITE/ImmigrationOS capabilities | ACLU; EFF; USASpending.gov | Contract modification; capability expansion; litigation-blocked features |
| ICM biometric integration | FPDS.gov (contract tracking); Nextgov/FCW | Award date confirmed; scope changes |

### Institutional Sources

| Claim | Source to Check | What Changed Would Invalidate It |
|-------|----------------|----------------------------------|
| CISA workforce status | CISA official press; Nextgov/FCW | Hiring reversal; further reductions |
| EI-ISAC status | Center for Internet Security; Democracy Docket | Restoration of funding; full shutdown confirmed |
| NSA/Cyber Command ESG activation | CNN national security reporting; Nextgov | ESG reconvened; ESG explicitly disbanded |
| Palantir federal footprint | USASpending.gov; DefenseScoop; CNBC | New contracts; contract cancellations; capability modifications |
| USDA $300M BPA status | CNBC; State of Surveillance; FPDS | Contract modified; bossware component challenged |

---

## Event-Triggered Update Protocol

These events require an immediate briefing update — do not wait for the scheduled review cycle.

### Trigger Category 1: Immediate Update Required (within 48 hours)

| Trigger Event | Affected Briefings | Action |
|--------------|-------------------|--------|
| FISA 702 reauthorized with warrant protection | All (policy advocacy section becomes outdated) | Update all briefings' policy sections; remove advocacy CTAs |
| FISA 702 reauthorized without protection | All (deadline reference becomes stale) | Update deadline date; update advocacy language to next deadline |
| IRS–ICE injunction reinstated | Digital rights; journalist briefings | Update litigation status; note operational pause in data sharing |
| ProKYC platform taken down by law enforcement | All (threat still applies to clones/successors) | Update to note takedown; add note on successor tools |
| Major supply chain incident affecting security tools recommended in corpus | All | Update tool recommendation table; add compromised-window warning |
| New Palantir contract confirmed at a previously unlisted federal agency | All | Add to footprint table; assess impact on sector-specific risks |

### Trigger Category 2: Update Within 1 Week

| Trigger Event | Affected Briefings | Action |
|--------------|-------------------|--------|
| New Shai-Hulud wave detected (Wave 4 or later) | All | Update supply chain timeline; expand compromise window |
| ICM biometric contract awarded (September 2026) | Digital rights; researcher; journalist briefings | Document operational architecture as confirmed |
| CISA workforce hiring reversed | All | Update institutional status; revise election infrastructure section |
| ESG reconvened for 2026 midterm cycle | All (election infrastructure section) | Update operational status; revise defense deficit framing |
| Voice cloning / deepfake detection breakthrough (peer-reviewed) | All | Update detection failure rates; revise countermeasure hierarchy |
| Any tool in the recommended tool table compromised | All | Update tool table; add compromise notes |

### Trigger Category 3: Assess Within 2 Weeks (may or may not require update)

| Trigger Event | Assessment Question |
|--------------|-------------------|
| New academic paper on synthetic identity detection | Does it change the "detection has failed structurally" assessment? |
| Congressional hearing on Palantir / ICE surveillance | Does testimony change any capability claims? |
| State election security funding restored | Does it materially change the defense deficit assessment? |
| New FOIA disclosure on ELITE or ImmigrationOS | Does it contradict or extend existing capability claims? |
| Recipient organization reports a specific attack incident | Does it validate or complicate the threat model? |

---

## Update Process: How to Execute a Briefing Update

### For Scheduled Reviews (Monthly/Quarterly)

1. **Run the Primary Source Check List** — check each source against the current claim in the relevant briefing. Document any discrepancies in the update log (maintained as a section at the bottom of this document).

2. **Assess materiality** — a source URL changing is not material. A claim changing is material. Rate each discrepancy: High (changes the countermeasure or threat assessment), Medium (changes a supporting fact), Low (cosmetic or minor).

3. **Execute High-priority updates** — directly edit the affected briefing file. Increment the `updated` date in the YAML frontmatter. Add a one-line change note at the bottom of the Sources section.

4. **Log the update** — add an entry to the update log at the bottom of this document with date, briefing affected, and change description.

5. **Medium and Low priority** — batch these into the next quarterly review. Do not update for minor factual shifts that don't change the countermeasure recommendations.

### For Event-Triggered Updates (Immediate)

1. **Identify all affected briefings** from the trigger category table above.

2. **Write the minimum necessary update** — the goal is accuracy, not a full rewrite. Change only the specific claim that has become inaccurate. Use a clear editorial note (e.g., `[Updated June 13: FISA 702 was reauthorized without a warrant requirement. The June 12 deadline has passed. The next deadline is [X]. The countermeasure guidance is unchanged.]`) directly in the affected section.

3. **Update the YAML frontmatter** — change `status` from `ready-for-distribution` to `updated-[date]` and add an `updated:` field with the date.

4. **Push updates to in-progress distribution** — see next section.

5. **Log the update** — mandatory entry in the update log at the bottom of this document.

---

## Pushing Mid-Campaign Updates to Tier 2 Recipients

If a Trigger Category 1 event occurs while the Tier 2 campaign is actively in progress, recipients who have already received the briefing need to be notified.

### Who Gets a Mid-Campaign Update?

Send an update to:
- Every Tier 2 recipient who has acknowledged the briefing (confirmed receipt or replied)
- Every Tier 2 recipient who has forwarded it internally (if known)
- Do NOT send updates to contacts who have not yet replied to the initial email — their next email can simply use the updated briefing

### What the Mid-Campaign Update Says

Subject: `Update: [specific change] — [briefing title] correction`

Template:

```
[Name/Organization],

A brief correction to the May 2026 threat briefing I shared on [date]:

[One to two sentences describing what changed and what the accurate current status is.]

[If the countermeasure recommendations changed: "This means the guidance on [X] should now read: [new guidance]."]

[If only a background fact changed: "The countermeasure recommendations are unchanged."]

The updated briefing is attached / available at [link].

Thank you for using this material. Any feedback on the accuracy or usefulness of the briefing is welcome.

[Name]
```

**Keep the update email under 150 words.** The goal is to correct a specific claim, not to re-pitch the corpus. Recipients who have engaged positively will appreciate the accuracy signal — it demonstrates active maintenance. Keep it short.

### Update Email Send Window

- Trigger Category 1 events: send within 48 hours of confirmed change
- Trigger Category 2 events: send within 1 week, batched with any other pending corrections to the same briefing
- Never batch corrections from different trigger categories — if a Category 1 event occurs, send immediately, do not wait to consolidate

---

## Long-Term Sustainability Model

### The Problem With One-Person Maintenance

A single researcher maintaining a living threat corpus is a single point of failure. If that person is unavailable for two weeks during the FISA 702 deadline or the ICM contract award window, time-sensitive briefings go stale with no fallback.

### Practical Mitigation Steps

**1. Designate a backup reviewer** — identify one person who can run the Primary Source Check List in your absence. This person does not need to write; they need to be able to flag when a claim appears to have changed and know how to reach the primary researcher.

**2. Set calendar reminders for all date-certain events** — the ICM contract (September 2026), the next FISA deadline (to be determined), and the quarterly review dates should be calendar events, not tasks that get deferred.

**3. Set up Google Alerts or equivalent** — configure alerts for: "Palantir ICE", "Shai-Hulud", "FISA 702", "EI-ISAC", "ProKYC". These alerts are not a substitute for the Primary Source Check List, but they will surface major events before the monthly review cycle.

**4. Consider a handoff document for community continuity** — if this corpus is being used by digital rights organizations or journalists who have integrated it into training curricula, consider publishing a brief "how we maintain this" note so those organizations know what to expect in terms of update frequency and what to do if updates stop. Transparency about maintenance creates trust; unexplained staleness destroys it.

### When to Stop Maintaining

The corpus has a natural lifecycle. The threat vectors documented here (ELITE, FISA 702, ProKYC, Shai-Hulud) will eventually be superseded by new systems, new legislation, and new attack tooling. The signal to stop active maintenance is when:

- More than 50% of the specific claims in a briefing require substantive updates (at that point, a new briefing is more efficient than continuous patching)
- The primary platform (ELITE) is replaced by a successor system with a materially different architecture
- The policy landscape shifts enough that the advocacy sections require full rewrites rather than deadline updates

At that point, archive the May 2026 corpus as historical documentation and begin a new cycle if the resources exist.

---

## Update Log

*Append entries here in reverse chronological order (most recent at top). Format: `YYYY-MM-DD — [Briefing(s)] — [Change description] — [Source]`*

*(No entries yet — corpus current as of May 6, 2026)*

---

## Date-Certain Milestones (Pre-Populated)

| Date | Event | Briefings to Review | Action |
|------|-------|--------------------|-|
| June 5, 2026 | Pre-FISA deadline review | All (policy advocacy sections) | Verify June 12 deadline still accurate; prepare update |
| June 12, 2026 | FISA 702 deadline | All | Document outcome; update all policy sections same day |
| September 2026 | ICM biometric contract award window | Digital rights, researcher, journalist | Monitor FPDS; document operational scope when awarded |
| November 2026 | Midterm elections | All (election infrastructure sections) | Post-election: update defense deficit assessment with outcomes |
| Q4 2026 | Quarterly review | All | Full accuracy check against all primary sources |
| Q1 2027 | First annual review | All | Consider full corpus refresh vs. continued maintenance |
