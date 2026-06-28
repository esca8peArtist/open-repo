---
title: "Phase 3 Remediation Checklist — Source and Contact Corrections"
created: "2026-06-28"
session: "Item 12 Validation"
status: "Production-ready — action items before November 4, 2026 launch"
parent_documents:
  - "PHASE_3_SOURCE_ACCESSIBILITY_AUDIT.md (source status)"
  - "PHASE_3_EXPERT_CONTACT_CURRENCY_AUDIT.md (contact status)"
---

# Phase 3 Remediation Checklist
## Action Items Before November 4, 2026 Launch

**Purpose:** Consolidated action list for resolving all RED and YELLOW items from the Phase 3 accessibility and contact audits. Organized by urgency and timing. All items are solvable — no research pivots required.

**Overall posture:** Phase 3 infrastructure is production-ready with minor remediation. 2 source URLs need replacement (both have verified alternates). 4 expert contact URLs need minor correction. 1 contact status needs confirmation (Wehle post-sabbatical). 1 major case (Trump v. Slaughter) needs the ruling added when issued.

---

## IMMEDIATE ACTIONS (Do Now — Before July 10, 2026)

### A1. Replace Presidential Commission Report URL in DOMAIN_K_SOURCE_MASTER_DATABASE.md
- **Issue:** presidentialcommission.gov domain has expired. Source 25 in the anchor set is currently a dead link.
- **File to update:** `DOMAIN_K_SOURCE_MASTER_DATABASE.md` — Source 25 (Presidential Commission Report, Zone 2.2)
- **Current URL:** https://presidentialcommission.gov/2021/12/07/presidential-commission-on-the-supreme-court-of-the-united-states-december-2021-final-report/
- **Replacement URL (primary):** https://www.presidency.ucsb.edu/documents/final-report-the-presidential-commission-the-supreme-court-of-the-united-states
  - Host: UC Santa Barbara American Presidency Project
  - Status: 200 OK confirmed
  - Quality: Stable archival host for presidential documents; this is the standard academic citation
- **Replacement URL (secondary):** https://scholarship.law.columbia.edu/faculty_scholarship/3779/
  - Host: Columbia Law School academic repository
  - Status: 200 OK confirmed
- **Also update:** Any other document that cites the presidentialcommission.gov URL (check DOMAIN_H_CONSTITUTIONAL_RESILIENCE_ARCHITECTURE.md Zone 3.2 footnotes).
- **Confidence rating impact:** None — the document itself is unchanged; only the hosting URL changed.

### A2. Replace Goldman-Booker SCEIA URL in DOMAIN_K_SOURCE_MASTER_DATABASE.md
- **Issue:** https://goldman.house.gov/media-press-releases/goldman-booker-reintroduce-supreme-court-ethics-and-investigations-act-restore returns HTTP 404.
- **File to update:** `DOMAIN_K_SOURCE_MASTER_DATABASE.md` — Source 8 (Zone 1.2)
- **Current URL:** https://goldman.house.gov/media-press-releases/goldman-booker-reintroduce-supreme-court-ethics-and-investigations-act-restore
- **Replacement URL (primary):** https://www.booker.senate.gov/news/press/03/05/2026/booker-goldman-introduce-bill-to-strengthen-ethics-oversight-on-the-us-supreme-court
  - Host: Senator Cory Booker's official Senate website
  - Status: 200 OK confirmed
  - Note: This is the Senate companion press release from March 5, 2026; it covers the same bill introduction. The Booker Senate URL is actually more reliable than a House member press release (Senate URLs tend to be more stable).
- **Confidence rating impact:** None — the fact of the bill's introduction is confirmed.

### A3. Add Trump v. Slaughter Ruling When Issued
- **Issue:** Source K8 in anchor set references "Trump v. Slaughter (expected June-July 2026)" — ruling has not yet issued as of June 28, 2026. Case is still pending per SCOTUSblog monitoring.
- **File to update:** `DOMAIN_K_SOURCE_MASTER_DATABASE.md` — Source 22 (Zone 2.1); also `DOMAIN_H_CONSTITUTIONAL_RESILIENCE_ARCHITECTURE.md` references (Zone 1.2 where Loper Bright / independent agency pattern is discussed).
- **Action:** Monitor supremecourt.gov daily through July 10 (last expected day of term). When ruling issues:
  1. Update Source 22 confidence from "9 (background analysis)" to "10 when ruling issues"
  2. Add the ruling's actual URL to the source entry
  3. If ruling overturns Humphrey's Executor (as oral argument signaled), add note: "Zone 4 coalition scope expansion trigger confirmed — Humphrey's Executor overruled, removing for-cause protections for NLRB, MSPB, FEC, EEOC"
  4. If ruling does NOT overturn (unexpected outcome), note that Domain K Zone 2 framing needs revision
- **Monitoring URL:** https://www.scotusblog.com/case-files/cases/trump-v-slaughter/ (or search Trump v. Slaughter at scotusblog.com when ruling issues)

---

## PRE-OUTREACH ACTIONS (Complete Before September 1, 2026)

### B1. Correct Yaniv Roznai Contact URL
- **Issue:** DOMAIN_H_EXPERT_CONTACT_FRAMEWORK.md T2.3 lists herzliya.ac.il as the institutional domain for Roznai. Reichman University has changed its primary domain to runi.ac.il.
- **File to update:** `DOMAIN_H_EXPERT_CONTACT_FRAMEWORK.md` — T2.3 contact routing
- **Current routing:** "herzliya.ac.il; through IDEA blog"
- **Corrected routing:** https://www.runi.ac.il/en/faculty/yroznai (Reichman University faculty page — confirmed accessible in browser; HTTP 247 Cloudflare challenge-pass)
- **Also update:** Any other framework file that references herzliya.ac.il for Roznai
- **Why urgent:** Roznai is the July 2026 first-priority outreach contact (Israel selection law ruling timing). Need correct routing before July outreach.

### B2. Correct Kim Wehle Profile URL
- **Issue:** DOMAIN_H_EXPERT_CONTACT_FRAMEWORK.md T2.8 lists law.ubalt.edu/faculty/profiles/wehle_kim.cfm — that URL redirects to UB Law homepage (not Wehle's profile).
- **File to update:** `DOMAIN_H_EXPERT_CONTACT_FRAMEWORK.md` — T2.8 contact routing
- **Current URL:** law.ubalt.edu/faculty/profiles/wehle_kim.cfm
- **Corrected URL:** https://www.ubalt.edu/directory/profile/kwehle (200 OK confirmed)
- **Also update:** Note her media platform has shifted from CBS News to ABC News. Bulwark outreach channel unchanged (submissions@thebulwark.com).

### B3. Confirm Kim Wehle Sabbatical Return
- **Issue:** Wehle completed a 2024-2025 Fulbright Scholarship at University of Leiden (Netherlands). Unclear if she has fully returned to teaching at University of Baltimore for the 2025-2026 academic year.
- **Action:** Check her current status on https://www.ubalt.edu/directory/profile/kwehle or kimberlywehle.com before September 2026 outreach.
- **If still abroad or partially remote:** Route initial contact via kimberlywehle.com personal website contact form or The Bulwark editorial (submissions@thebulwark.com) rather than UB Law institutional directory.
- **Why this matters:** Wehle is the only Domain H contact with direct access to The Bulwark's center-right readership — the 22nd Amendment defense campaign specifically requires this channel.

### B4. Verify Fix the Court Site Operational Status
- **Issue:** Fix the Court (fixthecourt.com) is returning HTTP 500 errors to all automated requests as of June 28, 2026. This affects the Fix the Court annual review, recusal database, and term limits resources cited in Domain K.
- **Action:** Check fixthecourt.com in browser by August 15, 2026.
- **If site remains down:** 
  - Replace Fix the Court statistics with Brennan Center shadow docket tracker (already GREEN)
  - Escalate Gabe Roth (T1.1) contact to August instead of September, asking about site status
  - Designation: Brennan Center (Rosenfeld) as primary coalition coordination contact rather than secondary
- **If site is back up (expected):** 500 server errors to curl are common for WordPress sites with bot protection enabled — browser access was likely always operational. September outreach to Roth proceeds normally.

### B5. Verify Pamela Karlan Stanford Profile URL
- **Issue:** https://law.stanford.edu/faculty/pamela-s-karlan/ returns 404.
- **Action:** Before November 2026 outreach, search Stanford Law directory at law.stanford.edu for Karlan.
- **Suggested URL to try:** https://law.stanford.edu/directory/pamela-s-karlan/
- **Impact:** Contact routing only. Karlan is confirmed at Stanford (co-directs the Supreme Court Litigation Clinic — that page is live).

### B6. Verify Justin Weinstein-Tull ASU Profile URL
- **Issue:** law.asu.edu/profile/justin-weinstein-tull returns 404.
- **Action:** Search ASU Law faculty at law.asu.edu/faculty before November 2026 outreach.
- **Impact:** Contact routing only. Weinstein-Tull confirmed active through WashU Law May 2026.

---

## PRE-LAUNCH MONITORING (Complete Before November 1, 2026)

### C1. Kansas Supreme Court Amendment Result (August 4, 2026)
- **Issue:** Source K78 (Ballotpedia — Kansas Elections for Supreme Court Justices Amendment, August 4, 2026) is pre-event. The result is not yet available.
- **Action:** Check Ballotpedia August 5, 2026 for result and update Domain K source note.
- **If voters approve direct partisan elections:** Document as public appetite for changing selection systems (reform framing — either partisan elections or merit selection, not the status quo of political appointment without term limits).
- **If voters reject:** Document as public support for merit selection independence (independence framing).
- **Note for Domain K:** Either outcome is useful for the reform coalition messaging; the framing differs but both validate the reform agenda.

### C2. Fix the Court Final Status Check
- **Issue:** See B4 above.
- **Action:** Recheck in browser October 2026 before any coalition coordination outreach. Note for Gabe Roth outreach: if site is still unstable, raise this directly in September outreach email.

### C3. V-Dem Judicial Independence Sub-Indicator Verification
- **Issue:** Source K/H49 (V-Dem 2026 US downgrade) notes that verification is needed: "did judicial independence indicators specifically drive the downgrade?"
- **Action:** Contact V-Dem Institute (v-dem.net/about/contact/) by July 2026 with specific query about judicial independence sub-indicators in the 2026 US assessment.
- **File where this matters:** `DOMAIN_K_SOURCE_MASTER_DATABASE.md` — Source 49 research note. Also Domain H Zone 2.4 reference.
- **Expected response time:** 2-3 weeks. Send in July to have answer before October coalition outreach.
- **Note:** The V-Dem US downgrade fact itself is confirmed and can be cited regardless of sub-indicator question. The specific question is whether the judicial independence sub-score specifically declined — useful for Domain K Zone 2 comparative framing but not required for the core claim.

### C4. IDI: Israel Judicial Selection Law Ruling Update
- **Issue:** The Israel Supreme Court ruling on the March 2025 judicial selection law was expected June-July 2026. Not yet issued as of June 28.
- **Action:** Monitor en.idi.org.il/tags-en/48951 (confirmed live tracker) and NPR/Lawfare through July 2026.
- **When ruling issues:** Update Domain K Source 46 (Library of Congress Israel Knesset Reform, April 2025) and Domain H Zone 2.4 Israel case study with outcome.
- **Why this matters:** If the Israeli Supreme Court strikes down the 2025 selection law (as with the 2023 Reasonableness Amendment), it strengthens Domain H's core argument that courts can and do defend their own structural integrity. If it upholds the law, the case study framing shifts to "judicial capture succeeded despite resistance."
- **Pre-launch deadline:** Update these sources before finalizing Phase 3 documents in October 2026.

### C5. SCOTUSblog Trump v. Slaughter Confirmation
- **Issue:** See A3 above. If ruling issues after July 10, update references accordingly.
- **By November 1:** All Domain K Zone 2 and Domain H Zone 1.2 references to Trump v. Slaughter should reflect the actual ruling outcome rather than "expected."

---

## PAYWALL WORKAROUNDS (For Research Use)

These sources are paywalled or bot-blocked but needed for November 4 research depth. Workarounds below.

| Source | Paywall Issue | Workaround |
|--------|--------------|-----------|
| Science Advances: "Has SCOTUS Become Just Another Political Branch?" (doi:10.1126/sciadv.adk9590) | Science/AAAS paywall | (1) Check PubMed Central: this study may be deposited there. (2) Key findings (approval collapse post-Dobbs) are cited in Brennan Center polling compilation (already GREEN) — use Brennan Center for the statistic, Science Advances for the peer-review citation. |
| Tandfonline: Varying Effect of Court-Curbing — Hungary/Poland | Taylor & Francis institutional paywall | (1) JSTOR (many T&F journals included). (2) Request through interlibrary loan. (3) Author preprint may be on SSRN — search "court-curbing Hungary Poland" at ssrn.com. Non-anchor source; abstract sufficient for the Domain H Zone 1.2 point. |
| Journal of Democracy: Scheppele Hungary | JoD enforces paywall | (1) Princeton scholarly repository: check scholar.princeton.edu/kls for author-deposited preprint. (2) JoD sometimes releases articles after 12 months — check free access. (3) University library. Essential source for Zone 1.1 autocratic legalism framework; pursue before September Scheppele outreach. |
| ScienceDirect: Turkey Judicial Independence | Elsevier paywall | ALREADY RESOLVED: arXiv preprint confirmed in source database at https://arxiv.org/pdf/2410.02439 — this is open access and can be used directly. Update any citation that uses the ScienceDirect URL to use the arXiv URL instead. |
| Cambridge Core: Bill C-9 PDF | Direct PDF accessible (200 OK); article page may require paywall | Use the direct PDF URL (confirmed live): https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0D4357A9A6150E706CC261B86BA47733/S0008423923000793a.pdf — no paywall on direct PDF link. |
| Constitutional Court Review 2025 (SAFLII) | journals.co.za blocks curl; SAFLII direct also blocked | Open in browser — both are public-domain South African repositories. Accessible via browser despite curl blocking. |
| Time.com: Virginia NPV (April 2026) | Soft paywall (HTTP 406) | Free Time account allows access. Alternatively: Virginia NPV announcement is independently verifiable at nationalpopularvote.com/state-status (200 OK, free), which shows Virginia's current status in the compact. Use nationalpopularvote.com as the citation for the Virginia addition fact. |

---

## REPLACEMENT SOURCES FOR RED ITEMS (Ready to Drop In)

### For Source K25 (Presidential Commission Report, 2021)

**Old citation:**
> Presidential Commission on the Supreme Court — Final Report (December 7, 2021). URL: https://presidentialcommission.gov/2021/12/07/presidential-commission-on-the-supreme-court-of-the-united-states-december-2021-final-report/

**New citation (use either or both):**
> Presidential Commission on the Supreme Court — Final Report (December 7, 2021). UC Santa Barbara American Presidency Project (permanent archive). URL: https://www.presidency.ucsb.edu/documents/final-report-the-presidential-commission-the-supreme-court-of-the-united-states [200 OK, June 2026]
>
> Also archived at Columbia Law Scholarship: https://scholarship.law.columbia.edu/faculty_scholarship/3779/ [200 OK, June 2026]

**Nothing else changes.** The content, authorship, date, confidence score, and research notes in the source database are all accurate. Only the URL.

---

### For Source K8 (Goldman-Booker SCEIA)

**Old citation:**
> Supreme Court Ethics and Investigations Act (Goldman-Booker). URL: https://goldman.house.gov/media-press-releases/goldman-booker-reintroduce-supreme-court-ethics-and-investigations-act-restore

**New citation:**
> Supreme Court Ethics and Investigations Act (Goldman-Booker). Booker Senate press release (March 5, 2026). URL: https://www.booker.senate.gov/news/press/03/05/2026/booker-goldman-introduce-bill-to-strengthen-ethics-oversight-on-the-us-supreme-court [200 OK, June 2026]

**Content note:** The Booker press release confirms the same bill reintroduction (Goldman companion in the House). The bill text, date, and provisions are unchanged.

---

### For ScienceDirect Turkey Article (Domain H Zone 1.1)

**Old URL:** https://www.sciencedirect.com/science/article/abs/pii/S0144818825000572

**Replacement URL:** https://arxiv.org/pdf/2410.02439 (arXiv preprint — open access, confirmed in source database)

**Action:** Update DOMAIN_H_CONSTITUTIONAL_RESILIENCE_ARCHITECTURE.md Zone 1.1 footnote to use arXiv URL instead of ScienceDirect.

---

## TIMELINE IMPACT ASSESSMENT

**Does any source accessibility issue require a 2-3 week access delay that could affect the November 4 launch timeline?**

No. All RED items have immediate replacement URLs that are already verified GREEN. All YELLOW paywall items can be accessed via institutional library (no special request timeline) or have open-access alternates. The Trump v. Slaughter ruling (expected within days) will be freely available same-day on SCOTUSblog.

**Specific timeline risks:**
- V-Dem sub-indicator query (C3): 2-3 week response time. Send July 2026. Non-blocking — the V-Dem downgrade can be cited regardless of whether the sub-indicator question is answered.
- IDI Israel selection law ruling (C4): Unknown timeline (ruling expected July 2026 per last available information). Monitor; update when issued. The Domain H Zone 2.4 case study can be finalized with either outcome — both outcomes support the core resilience argument.
- Journal of Democracy Scheppele preprint (paywall workaround): 1-2 weeks to locate or access. Non-urgent — this is a Zone 1 background source, not an anchor source. Alternative: cite the autocratic legalism argument from Scheppele's NYRB February 2026 article (confirmed accessible without paywall) or from her congressional testimony record.

**Bottom line: Phase 3 research infrastructure is viable for the November 4 launch with no timeline-blocking access issues.**

---

## CHECKLIST SUMMARY

### Immediate (Before July 10)
- [ ] A1: Update Presidential Commission URL in DOMAIN_K_SOURCE_MASTER_DATABASE.md
- [ ] A2: Update Goldman press release URL in DOMAIN_K_SOURCE_MASTER_DATABASE.md
- [ ] A3: Monitor supremecourt.gov for Trump v. Slaughter ruling — update when issued

### Pre-Outreach (Before September 1)
- [ ] B1: Update Roznai contact URL to runi.ac.il in DOMAIN_H_EXPERT_CONTACT_FRAMEWORK.md
- [ ] B2: Update Wehle profile URL to ubalt.edu/directory/profile/kwehle in DOMAIN_H_EXPERT_CONTACT_FRAMEWORK.md
- [ ] B3: Check Wehle sabbatical return status before outreach
- [ ] B4: Check Fix the Court site status in browser; if still broken, designate Brennan Center as primary contact
- [ ] B5: Find correct Karlan Stanford URL for November outreach
- [ ] B6: Find correct Weinstein-Tull ASU URL for November outreach

### Pre-Launch Monitoring (Before November 1)
- [ ] C1: Update Kansas ballot result after August 4, 2026
- [ ] C2: Final Fix the Court site status check October 2026
- [ ] C3: Contact V-Dem re: judicial independence sub-indicators (July send)
- [ ] C4: Update IDI Israel selection law ruling when issued
- [ ] C5: Confirm Trump v. Slaughter ruling integrated into all references

### Paywall Workarounds (Ongoing)
- [ ] W1: Update ScienceDirect Turkey URL to arXiv preprint
- [ ] W2: Source Journal of Democracy Scheppele via Princeton preprint or NYRB February 2026 alternative
- [ ] W3: Note Time.com Virginia NPV soft paywall — use nationalpopularvote.com as primary citation for Virginia addition

---

*Document created June 28, 2026. All remediation items verified against source audit (PHASE_3_SOURCE_ACCESSIBILITY_AUDIT.md) and contact audit (PHASE_3_EXPERT_CONTACT_CURRENCY_AUDIT.md). Zero research pivots required. All RED items have replacement sources already identified and confirmed accessible.*
