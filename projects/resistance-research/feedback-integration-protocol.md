---
title: "Feedback Integration and Amendment Protocol — Democratic Renewal Framework"
date: 2026-05-06
version: 1.0.0
status: production-ready
purpose: >
  Governs how external feedback received after distribution is classified,
  evaluated, incorporated into published domain documents, and versioned.
  Distinct from stakeholder-feedback-integration-protocol.md, which governs
  how Phase 1 feedback drives Phase 2 domain selection.
cross_references:
  - democratic-renewal-proposal.md
  - stakeholder-feedback-integration-protocol.md
  - DISTRIBUTION_EXECUTION_LOG.md
  - WORKLOG.md
---

# Feedback Integration and Amendment Protocol

**Democratic Renewal Framework — Production Version**
**Effective: May 2026 | Framework Version at Adoption: 1.0.0**

---

## 1. Executive Summary

This protocol governs what happens after the Democratic Renewal Framework is distributed. Once law school clinics, think tanks, attorney general offices, labor unions, and academic researchers receive and begin using the 35-domain framework, feedback will arrive — factual corrections, new research findings, jurisdiction-specific adaptations, and interpretive disagreements. Without a governed process, that feedback creates fragmentation: different readers working from different corrections, amendments applied inconsistently, authority over content unclear.

The protocol resolves this by establishing five things: a taxonomy for classifying feedback, decision rules for what each type triggers, a semantic versioning system for tracking changes, a publication and archiving process, and a governance structure that makes authority explicit.

**Quick reference.** Feedback is submitted via a structured form (see Section 4). Factual corrections are resolved within one week. Interpretive amendments and new findings are resolved within two weeks. Jurisdiction-specific additions become supplementary documents rather than modifications to the base text. Anya holds final decision authority on all amendments; domain-area expertise is solicited for non-obvious corrections. Every change is documented in a per-domain changelog with attribution to the contributor.

The protocol is modeled on a hybrid of established precedents: the American Law Institute's council-approval governance model (used for the Model Penal Code since 1962), the IETF's principle that once a document is formally issued it is immutable but can be superseded, arXiv's versioned preprint system (permanent identifier + v1/v2/v3 history), and semantic versioning's MAJOR.MINOR.PATCH logic adapted for policy documents rather than software APIs.

---

## 2. Feedback Taxonomy

All feedback received after distribution is classified into one of five categories before any action is taken. Misclassification is the primary failure mode — treating an interpretation disagreement as a factual error, for instance, shortcuts a review process that exists for good reason.

### Category A: Factual Correction

A claim in the framework is objectively wrong — a number, date, jurisdiction count, case citation, or statutory reference is verifiably incorrect and the correct version is verifiable from primary sources.

**Examples**
- "Section 1.2 states the Shelby County decision was issued in 2012; it was 2013."
- "Domain 5 cites 12 states under active Section 2 VRA coverage — the current count is 15 as of May 2026."
- "The case citation for *Gonzalez v. ICE* is listed as No. 18-16973; the correct docket is No. 18-16969."

**What makes this category**: The correction is verifiable by looking up the primary source. There is no reasonable disagreement about the correct value once the source is consulted.

**Action path**: Immediate silent fix (patch version bump) if unambiguous; versioned patch with changelog entry in all cases.

---

### Category B: Interpretation Clarification

The feedback disagrees with or proposes refinement of an analytical judgment, framing choice, or causal claim in the framework — not a factual error, but a legitimate difference of interpretive emphasis.

**Examples**
- "The institutional recovery mechanism in Domain 6 assumes legislative capacity, but Congress has been in functional paralysis since 2025. The analysis should model a legislative-bypass pathway."
- "Domain 22's framing of reparations as primarily racial justice undersells the economic efficiency argument, which is more persuasive in conservative institutional contexts."
- "The comparative evidence in Domain 9 draws on German federalism as an analogue for American state autonomy, but the constitutional structures are too dissimilar to make this comparison load-bearing."

**What makes this category**: The feedback reflects a legitimate analytical disagreement, not an objective error. Reasonable experts could hold the original view or the proposed revision.

**Action path**: Versioned amendment if the revision strengthens the framework's analytical rigor; supplementary note if the disagreement is genuine and both views deserve documentation; deferral if the feedback requires research the current session cannot complete.

---

### Category C: New Finding

Peer-reviewed research, a major new case study, a judicial decision, or empirical data published after the domain was written that would materially strengthen, complicate, or update the framework's evidence base.

**Examples**
- "Hungary's 2025 election produced data that directly tests the media capture hypothesis in Domain 33 — the outcome aligns with the framework's prediction and would strengthen Section 33.4."
- "A March 2026 RAND study on ranked-choice voting in multi-jurisdictional settings is stronger evidence for Domain 1 than the Alaska/Maine comparisons currently cited."
- "The Supreme Court's June 2026 decision in *Moore v. Harper II* directly addresses the independent state legislature theory that Domain 1 treats as unresolved — the framework should reflect the ruling."

**What makes this category**: The finding is documented in a primary source (peer-reviewed journal, government report, judicial opinion) and post-dates the domain's most recent version. The contribution is additive, not merely corrective.

**Action path**: Versioned patch (single finding) or minor version bump (finding that materially extends or redirects a domain's analysis). New judicial decisions that resolve open legal questions in the framework are handled as minor version bumps.

---

### Category D: Localization

The feedback proposes an adaptation specific to a particular jurisdiction, organizational context, or implementation setting that does not apply to the framework as a whole.

**Examples**
- "This playbook won't work in Texas because of [state-specific law]. Here is an adaptation for Texas advocates."
- "Domain 17 (Labor & Employment) assumes National Labor Relations Board jurisdiction. Federal preemption makes this analysis inapplicable to agricultural and domestic workers — here is a supplement for those sectors."
- "Domain 5 (Tax Reform) needs a state-level companion for California specifically, where Proposition 13 creates constraints not present in the federal analysis."

**What makes this category**: The feedback is correct within its stated scope but that scope is not universal. Incorporating it into the base domain would make the base document misleading for readers outside that context.

**Action path**: Supplementary document (format: `domain-XX-supplement-[jurisdiction/context].md`). The base domain document is not modified. The supplement is indexed with a notation in the domain's changelog.

---

### Category E: Out of Scope

The feedback proposes content that is outside the framework's stated purpose, contradicts the framework's evidentiary standards, is not supported by documented primary sources, or requests advocacy positions rather than analytical positions.

**Examples**
- "You should add a domain on extraterrestrial governance."
- "Domain 22 should argue for reparations based on divine justice, not empirical evidence."
- "Your framing of democratic renewal is too optimistic — you should acknowledge that reform is impossible and encourage emigration."
- Generic partisan commentary without specific factual or analytical content.

**What makes this category**: The feedback either (a) falls outside the framework's documented scope, (b) fails the framework's evidentiary standard (every reform implemented somewhere, evidence documented, plausible political pathway), or (c) contradicts core design choices that are not up for revision without a major version process.

**Action path**: Documented rejection with written rationale. Stored in the domain's changelog as a rejected item for transparency. No changes to the document.

---

### Decision Tree: Classifying Incoming Feedback

```
Is the feedback correcting a specific verifiable claim?
  YES → Is there a primary source that definitively resolves it?
            YES → Category A (Factual Correction)
            NO  → Category B (Interpretation Clarification)
  NO  → Does it cite new documented research or case developments?
            YES → Category C (New Finding)
            NO  → Is it specific to a jurisdiction or implementation context?
                      YES → Category D (Localization)
                      NO  → Does it fall within the framework's stated scope and evidentiary standards?
                                YES → Category B (Interpretation Clarification)
                                NO  → Category E (Out of Scope)
```

---

## 3. Versioning Strategy

The framework uses an adapted semantic versioning scheme: **MAJOR.MINOR.PATCH** (e.g., `1.0.0`), with optional supplement suffixes for localized additions.

This approach is borrowed from software versioning but adapted for the specific stability requirements of a distributed policy document. The core principle: a reader who cites "Democratic Renewal Framework v1.0" should be able to retrieve that exact version indefinitely, and any amendment should be a distinct version with its own citable identifier.

### Version Number Definitions

**MAJOR version** (1.0 → 2.0)

Structural changes to the framework's architecture — adding or removing sections in the Proposal document itself, reorganizing the domain structure, significantly revising the theory of change, or changing the framework's stated scope. Major version bumps require a full review cycle and are expected to occur no more than once per 18–24 months. A major version bump does not invalidate prior versions; v1.x and v2.x coexist as separately citable documents.

Triggers: restructuring the Part I–V proposal architecture; adding more than 3 domains in a single release; fundamentally revising the implementation timeline based on changed conditions; retiring a domain as no longer applicable.

**MINOR version** (1.0 → 1.1)

Domain additions, significant new findings that materially extend a domain's analysis, or factual corrections that affect core claims across multiple domains simultaneously. Minor version bumps go through the standard two-week review cycle.

Triggers: adding one or two new domains; a Supreme Court decision that requires substantive reanalysis of a domain; new empirical research that significantly changes cost estimates or evidence base; a correction that touches more than one domain.

**PATCH version** (1.0.0 → 1.0.1)

Factual corrections, citation fixes, typographic errors, clarifications that do not change the analytical meaning of a section, and single new findings that add evidence without changing the domain's conclusions.

Triggers: correcting a date, number, or citation; adding a supporting case study that does not change the domain's primary argument; fixing a broken URL in a citation; clarifying ambiguous language without changing the intended meaning.

**Supplement** (1.0.0 → 1.0.0-supplement-[context])

Jurisdiction-specific or context-specific additions that do not modify the base domain text. Supplements have their own version tracking and are indexed separately. They inherit the version of the base domain they apply to (a California supplement to Domain 5 written when the framework is at v1.0.3 is tagged `v1.0.3-supplement-CA-domain5`).

### Versioning Examples

| Feedback Type | Example | Action | Version Change |
|---|---|---|---|
| Factual correction | Wrong year in Shelby County citation | Fix citation | 1.0.0 → 1.0.1 |
| New case study | RAND study strengthens Domain 1 evidence | Add to domain | 1.0.1 → 1.0.2 |
| New judicial decision | SCOTUS resolves open question in Domain 6 | Substantive revision | 1.0.2 → 1.1.0 |
| New domain added | Domain 38 completes Phase 2 research | Add to framework | 1.1.0 → 1.2.0 |
| Localization | Texas adaptation of Domain 17 | Supplementary file | 1.1.0 → 1.1.0-supplement-TX-domain17 |
| Structural reorganization | Theory of change revised for Phase 3 | Architecture change | 1.x → 2.0.0 |

### Backward Compatibility Guarantee

Every published version is permanently available via its GitHub release tag. A reader who cites "Democratic Renewal Framework v1.0.0, Domain 5, Section 5.3" will be able to retrieve that exact text at any future date. Version tags are never deleted, overwritten, or retroactively modified.

This mirrors arXiv's versioning model: arXiv.org maintains all prior versions of every preprint indefinitely under the same permanent identifier, with version numbers appended (e.g., `2401.12345v1`, `2401.12345v2`). The framework adopts the same principle: the permanent identifier is the document name and domain structure; the version suffix locates the reader in the revision history.

---

## 4. Amendment Process

### Step 1: Feedback Submission

All feedback is submitted via the structured submission template (see Appendix A below). Submissions without the required fields are not processed — this is not a courtesy restriction but a functional one. The taxonomy classification, the affected domain and section reference, and the supporting source citation are all required for the review process to function.

**Submission methods, in order of preference:**
1. GitHub Issue on the framework repository (preferred — creates a permanent public record with threading)
2. Email to the framework contact address with the template in the message body
3. Written memo from an institutional contact (law school, think tank, AG office) — acceptable for institutional partners with established relationships

**What is not accepted as feedback submission:** Social media replies, comment sections, verbal communications without follow-up written record, feedback embedded in unrelated correspondence.

### Step 2: Initial Classification (48 hours)

On receipt, the feedback is classified using the taxonomy in Section 2. If the classification is ambiguous, the reviewer documents the ambiguity and defaults to the more thorough review path (Category B over Category A; Category C over Category B).

Classification is logged in the domain changelog with: date received, submitter name (or "anonymous"), domain and section referenced, and assigned category.

### Step 3: Review

| Category | Reviewer | Timeline | Decision Authority |
|---|---|---|---|
| A (Factual) | Anya or designated domain reviewer | 1 week | Anya final |
| B (Interpretation) | Domain-area expert (if available) + Anya | 2 weeks | Anya final |
| C (New Finding) | Domain-area expert (if available) + Anya | 2 weeks | Anya final |
| D (Localization) | Submitter + Anya | 3 weeks (for supplement drafting) | Anya final |
| E (Out of Scope) | Anya | 1 week | Anya final; no external review required |

For Categories B and C, "domain-area expert" means: a law school faculty contact, a think tank researcher, or an institutional partner who has substantive expertise in the domain's subject matter and has indicated willingness to assist with framework quality. This is not a formal advisory board — it is ad hoc expert consultation on individual submissions.

### Step 4: Decision

The decision options are:

- **Accept as Patch**: Implement the change, bump the patch version, log in changelog.
- **Accept as Minor**: Implement the change, bump the minor version, log in changelog.
- **Accept as Supplement**: Draft supplementary document with submitter, publish separately, index in domain changelog.
- **Defer to Phase 2**: Change requires new research the current cycle cannot complete; log the request in the Phase 2 domain priority matrix.
- **Reject**: Document the rejection reasoning in the domain changelog. The rejection reasoning is public.

### Step 5: Implementation

Accepted changes are implemented directly in the relevant domain file and proposal document. The workflow:

1. Edit the domain file (e.g., `domain-XX-[name].md`) with the approved change.
2. Update the domain's changelog section with: version bump, date, submitter attribution (or "anonymous"), summary of change.
3. Update the framework's master version number in `democratic-renewal-proposal.md` YAML frontmatter.
4. Create a GitHub release tag matching the new version number with release notes summarizing all changes in the release.
5. Notify the submitter that their feedback has been incorporated (if they are identified and have provided contact information).

### Step 6: Publication

All version changes are announced in the framework's distribution channels:
- An update note appended to the top of `democratic-renewal-proposal.md` (mirroring the existing update log format already in the document)
- A GitHub release with the version tag and release notes
- For minor or major version bumps: a brief email to the Tier 1 distribution contacts who are actively using the framework

Patch version changes do not require distribution notification unless the correction affects claims that contacts may have already cited in published work.

---

## 5. Attribution and Governance

### Contributor Attribution

Feedback contributors are credited according to their preference:

- **Named attribution**: Contributor's name and institutional affiliation are recorded in the domain changelog. Example: "v1.0.1 (May 2026): Corrected Shelby County decision year. Submitted by [Name], [Institution]."
- **Anonymous contribution**: Recorded as "anonymous submission." The change is documented; the contributor is not identified.
- **Institutional contribution**: Where feedback comes from an institutional contact (e.g., a Brennan Center research team), the institution is credited if the individual chooses institutional rather than personal attribution.

The contributor index is maintained per domain in the changelog section of each domain file. There is no aggregate "contributor hall of fame" — attribution is attached to the specific change, not aggregated into a ranking.

### Governance Structure

**Authority**: Anya holds final decision authority on all amendments. This is not a consensus governance model — the framework is a single-author intellectual product with an open feedback process, not a collectively governed commons. The distinction matters: consensus governance (as used in W3C Working Groups or IETF Working Groups) is appropriate for technical standards that must interoperate. Policy frameworks that make substantive analytical judgments require a consistent authorial voice.

**Domain expertise consultation**: For Category B and C feedback in specialized domains (tax policy, military law, public health finance, international law), Anya may solicit review from a domain expert before deciding. The expert's view is advisory; Anya's decision is final.

**Conflict of interest**: If a submitter has a direct professional or financial interest in the amendment they are proposing (e.g., a pharmaceutical industry researcher proposing changes to Domain 11 healthcare), that interest must be disclosed in the submission. Anya discloses the conflict in the changelog entry if the amendment is accepted.

### Appeals Process

If a feedback submitter disagrees with a rejection decision:

1. The submitter may request a written elaboration of the rejection reasoning within 30 days of the rejection notice.
2. Anya provides a written response within two weeks.
3. If the submitter believes the rejection reflects an error of fact (not a difference of interpretation), they may submit additional primary source evidence for reconsideration. A second rejection on the same grounds is final.
4. There is no appeals body beyond Anya. The framework is not a legal document subject to administrative procedure — it is an analytical document with a governed but non-litigable review process.

### Domains Table (Template)

Each domain file maintains a metadata block at the bottom with this structure:

```
## Domain Changelog

| Version | Date | Change Summary | Category | Contributor |
|---------|------|----------------|----------|-------------|
| 1.0.0 | April 2026 | Initial publication | — | Anya Wank |
| 1.0.1 | [Date] | [Summary] | A/B/C/D | [Name/Anonymous] |
```

---

## 6. Risk Mitigation

### Fragmentation Risk

The primary risk in a distributed framework is citation fragmentation: different readers working from different versions, with no shared version reference in citations.

**Mitigation**: Version pinning in citations. The framework's preferred citation format includes the version number:

> Wank, A. (2026). *Democratic Renewal: An Integrated Proposal for Structural Reform*, v[X.Y.Z], Domain [N]: [Domain Title]. Available at: [URL/DOI]. Retrieved [date].

Because every version is permanently archived via GitHub release tag, a citation to v1.0.0 will resolve to the exact text the reader used, regardless of how many subsequent versions have been published. This is equivalent to citing a specific edition of a book or a specific v-number on arXiv.

**Secondary mitigation**: The framework's distribution channels announce version updates. Readers who subscribed to the framework at v1.0.0 are notified of minor and major version changes via the distribution email list.

### Authority Risk

If it becomes unclear who has authority to amend the framework, competing "corrected versions" may circulate without coordination.

**Mitigation**: Single-author authority is explicit and documented in this protocol. The canonical version of the framework is the one maintained in the official repository. Any document that describes itself as an amendment to the framework but was not processed through this protocol is not an amendment — it is a response paper or critique, and should be labeled as such by anyone circulating it.

The IETF model is instructive here: an RFC is only an RFC if it goes through the IETF process. A document that looks like an RFC but was not issued through that process is not an RFC. Similarly, a "Democratic Renewal Framework amendment" that was not processed through this protocol is not an amendment to the framework.

### Attribution Risk

Disputes may arise over whether a contributor's feedback was fairly credited, whether a rejection was properly reasoned, or whether an accepted change was materially altered from what the contributor submitted.

**Mitigation**: All submissions are logged with a timestamp in the domain changelog at receipt (not only at acceptance). The original submission is preserved in GitHub Issues (or equivalent) so the submitted text and the implemented text can be compared. Rejection reasoning is always documented in writing and stored in the changelog. This creates an auditable trail that resolves most attribution disputes.

### Long-Term Preservation

Policy frameworks have long adoption tails. The Model Penal Code is still cited from its 1962 Official Draft. The framework must remain citable and retrievable for at least ten years after distribution.

**Mitigation**: 
- GitHub repository is maintained with all release tags and version history intact.
- Domain files are plain Markdown — the simplest possible archival format, readable without specialized software.
- If the GitHub repository is ever migrated or discontinued, all versions are exported and archived before the migration.
- For high-visibility distribution (law school syllabi, AG office formal adoption), a DOI is obtained for the v1.0.0 release via Zenodo or an equivalent repository to create a stable, non-repository-dependent citation anchor.

---

## 7. Implementation Checklist

The following actions are required to operationalize this protocol before or during Phase 1 distribution.

### Pre-Distribution (Immediate)

- [ ] Create GitHub repository for the framework (if not yet exists) and tag current state as `v1.0.0`
- [ ] Add YAML frontmatter version field to `democratic-renewal-proposal.md` and all domain files
- [ ] Add `## Domain Changelog` section to each domain file with initial entry: v1.0.0 / April 2026 / Initial publication / Anya Wank
- [ ] Create a `CHANGELOG.md` at the repository root that aggregates all domain changelogs
- [ ] Create the feedback submission form (Google Form or GitHub Issue template) using Appendix A below
- [ ] Add a "How to Submit Feedback" note to the framework's distribution materials (one sentence: "For factual corrections or new research, use [URL]")

### Ongoing Operations

- [ ] Review incoming feedback submissions weekly (batch processing, not real-time)
- [ ] Log all submissions in domain changelogs within 48 hours of receipt, even before decision
- [ ] Create GitHub release tags for every version change, not just major ones
- [ ] Obtain DOI for v1.0.0 if the framework is formally cited in any law review, AG brief, or think tank publication
- [ ] Annual review: at the 12-month mark after initial distribution, conduct a structured review of all Category E (rejected) feedback to verify rejections were appropriate and nothing was miscategorized

### Domain Review Authority

For the initial version, all domains fall under Anya's direct review authority. As the framework scales and domain-specific experts engage, authority can be delegated per the following template:

| Domain | Subject Area | Delegated Reviewer (if any) |
|--------|-------------|----------------------------|
| 1 | Voting Rights & Electoral Systems | [TBD — election law contact] |
| 5 | Tax Reform | [TBD — tax policy contact] |
| 11 | Healthcare | [TBD — health policy contact] |
| 14 | Criminal Justice | [TBD — criminal law contact] |
| 22 | Reparations & Racial Justice | [TBD — civil rights contact] |
| 33 | Electoral Authoritarianism (comparative) | [TBD — comparative politics contact] |
| All others | — | Anya (default) |

---

## Appendix A: Feedback Submission Template

**Democratic Renewal Framework — Feedback Submission**

To submit feedback on the framework, complete the fields below and send to [feedback contact] or submit as a GitHub Issue.

---

**Submitter Information (optional — leave blank for anonymous)**
- Name:
- Institutional Affiliation:
- Contact Email:
- Attribution Preference: [ ] Named [ ] Institutional [ ] Anonymous

**Framework Reference**
- Domain Number and Title:
- Section Number (e.g., "Section 1.3" or "Subsection 5b"):
- Framework Version You Are Reviewing (e.g., "v1.0.0" — check top of document):

**Feedback Category** (check one)
- [ ] A — Factual Correction (verifiable error in a number, date, citation, or statutory reference)
- [ ] B — Interpretation Clarification (analytical disagreement or proposed reframing)
- [ ] C — New Finding (peer-reviewed research, judicial decision, or empirical data published after the domain)
- [ ] D — Localization (jurisdiction or context-specific adaptation that doesn't apply universally)
- [ ] E — Other (describe)

**Description of Feedback**
*(Describe the issue and your proposed change. Be specific about what text should change and what it should say.)*

**Supporting Source**
*(Required for Categories A and C. Provide a URL, citation, or other reference to the primary source that supports your feedback.)*

**Additional Context**
*(Optional. Any additional information, background, or context that would help evaluate this feedback.)*

---

*All submissions are logged and receive a response. Factual corrections are typically resolved within one week. Interpretation and new-finding submissions are typically resolved within two weeks. See the Feedback Integration and Amendment Protocol for full process details.*

---

## Appendix B: Worked Example — Hungary Electoral Dynamics (Domain 33)

**Scenario**: A comparative politics researcher at Harvard Kennedy School emails in September 2026 to say: "I've just published a peer-reviewed article in *Electoral Studies* showing that Hungary's 2025 parliamentary election produced an outcome that directly tests and confirms the media capture hypothesis in Domain 33 of your framework. The results are more robust than the 2022 case you cite. Here is the citation: [Researcher Name], 'Media Capture and Electoral Outcomes in Hungary, 2010–2025,' *Electoral Studies* 87 (2026). I'm happy to be credited by name."

**Classification**: Category C (New Finding). A peer-reviewed article published after the domain, providing new empirical data that strengthens an existing claim.

**Review process**: Anya reads the article and verifies that (a) the findings are as described, (b) they are consistent with and strengthen the domain's existing analysis (not contradictory), and (c) citing the article adds more than it complicates. If yes on all three: accept as patch.

**Implementation**: Add citation and a brief reference to the 2025 Hungary case in Domain 33's relevant section. Version bumps from `1.x.y` to `1.x.y+1`. Domain 33's changelog records: "v1.x.y+1 (September 2026): Added 2026 Hungary electoral outcome data from [Researcher Name], *Electoral Studies* 87, as supporting evidence for media capture hypothesis. Submitted by [Researcher Name], Harvard Kennedy School."

**Timeline from submission to publication**: Approximately 10 days (2 days classification + 5 days review + 3 days implementation and release).

**Notification**: Researcher receives email confirmation that feedback was incorporated, with the version number. If they have cited the v1.0.0 framework in their article, they may wish to add a footnote noting that Domain 33 was updated in v[X] to incorporate their findings.

---

*This protocol is self-referencing: any proposed changes to the protocol itself are handled as Category B or Major Version feedback and go through the same amendment process described here.*
