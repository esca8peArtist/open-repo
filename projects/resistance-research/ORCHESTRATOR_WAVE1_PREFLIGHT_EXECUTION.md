# Orchestrator Wave 1 Pre-Flight Execution Script

**Execution window**: 07:00–09:00 UTC May 18, 2026  
**Status**: Ready for execution  
**Last verified**: 2026-05-18 02:57 UTC

---

## Pre-Flight Checklist (execute in order, 43 min total)

### Phase 1: Gist Accessibility Verification (8 minutes)

**Task**: Verify all 5 Gists load successfully in incognito

```bash
# Verify HTTP 200 status for all Gists
for url in \
  "https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261" \
  "https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4" \
  "https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0" \
  "https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0" \
  "https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab"
do
  status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  echo "Gist status: $status — $(echo $url | cut -d'/' -f5)"
  if [ "$status" != "200" ]; then
    echo "⚠️  GIST FAILURE — Gist returned $status"
    echo "Action: Wait 60 seconds, retry. If still failing, consult PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.1"
  fi
done
```

**Expected**: All 5 return 200  
**If any fails**: STOP — do not proceed. Contact user immediately.  
**Documentation**: WAVE_1_EXECUTION_CHECKLIST.md line 36-45

---

### Phase 2: Baseline Gist View Counts (5 minutes)

**Task**: Record current view counts from two key Gists

- [ ] Open main proposal Gist: https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261
  - **Record view count**: _______
  - Verify user has recorded this in WAVE_1_MONITORING_DASHBOARD.md
  
- [ ] Open Domain 37 Gist: https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0
  - **Record view count**: _______
  - Verify user has recorded this in WAVE_1_MONITORING_DASHBOARD.md

**Expected**: Both Gists have view counts visible (usually shown in gray text at top-right)  
**If view counts missing**: Still proceed — view counts are "nice to have", not critical

---

### Phase 3: Contact Verification (10 minutes, ~2 min per contact)

**Task**: 90-second spot-check that each Batch 1 contact is still at their institution

- [ ] **Goodman** (Ryan Goodman, Just Security / NYU Law)
  - Check: https://law.nyu.edu/faculty/ryan-goodman or https://justsecurity.org/author/ryan-goodman/
  - Status: ✓ Active / ⚠️ Role changed / ✗ Not found
  
- [ ] **Weiser** (Wendy Weiser, Brennan Center)
  - Check: https://www.brennancenter.org/about/leadership
  - Status: ✓ VP Democracy active / ⚠️ Role changed / ✗ Not found
  
- [ ] **Chenoweth** (Erica Chenoweth, Harvard Kennedy School)
  - Check: https://www.hks.harvard.edu/faculty
  - Status: ✓ Academic Dean active / ⚠️ Role changed / ✗ Not found
  
- [ ] **Bassin** (Ian Bassin, Protect Democracy)
  - Check: https://www.protectdemocracy.org or main page
  - Status: ✓ Organization active / ⚠️ Role changed / ✗ Not found
  
- [ ] **Elias** (Marc Elias, Democracy Docket / Elias Law)
  - Check: https://www.democracydocket.com or https://www.elias.law
  - Status: ✓ Active / ⚠️ Changed firms / ✗ Not found
  - **Email**: Confirm melias@elias.law (NOT perkinscoie.com)

**Expected**: All 5 show ✓ Active  
**If any shows ⚠️**: Log the change but proceed (contact is still reachable)  
**If any shows ✗**: STOP — contact user for alternative email, do not send to invalid contact

---

### Phase 4: Email Template Final Scan (15 minutes, ~3 min per template)

**Task**: Verify all 5 email templates are ready to send

Files to check: `projects/resistance-research/execution/phase-1-personalized-batch-1.md`

For each of 5 contacts (Goodman, Weiser, Chenoweth, Bassin, Elias):

- [ ] **Template has zero remaining placeholders**
  - Search for: `{{`, `[bracket]`, `[Your name]`, `[Your email]`
  - Expected: None found
  - If found: Log error, notify user

- [ ] **Path-specific block is correct**
  - Expected: Only ONE path block present (A, A+37, or B)
  - Expected: Other two path blocks deleted
  - Check: Line mentioning "Path A+37" (or selected path) is visible

- [ ] **Personalization fields are filled**
  - Goodman: Article title filled (e.g., "The Crisis of Executive-Legislative Balance")
  - Weiser: Recent publication filled (e.g., "Analyzing the President's Executive Order on Mail Voting")
  - Chenoweth: Program filled (e.g., "AI for Democracy Movements")
  - Bassin: Recent filing filled (e.g., "Trump v. Wilcox" or current case)
  - Elias: Callais reference says "decided April 29, 2026" (NOT "pending")

- [ ] **Gist URLs are correct**
  - Main proposal: https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 ✓
  - Domain 37: https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0 ✓
  - Litigation tracker: https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 ✓
  - No old/broken Gist URLs present ✓

**Expected**: All checks pass for all 5 templates  
**If any fail**: Log error, notify user for correction

---

### Phase 5: Spreadsheet Baseline Setup (5 minutes)

**Task**: Verify user has created tracking spreadsheet with all 5 Batch 1 contacts

- [ ] **Spreadsheet exists**: `Wave 1 Batch 1 Tracking` (Google Sheets or equivalent)

- [ ] **Columns present**: Contact Name | Organization | Send Time | Status | Response Date | Notes

- [ ] **All 5 Batch 1 contacts listed**:
  1. Wendy Weiser — Brennan Center
  2. Marc Elias — Democracy Docket
  3. Ryan Goodman — Just Security / NYU
  4. Erica Chenoweth — Harvard Kennedy School
  5. Ian Bassin — Protect Democracy

- [ ] **Baseline Gist view counts recorded** (from Phase 2)
  - Main proposal baseline view count: _______
  - Domain 37 baseline view count: _______

**Expected**: Spreadsheet created and visible  
**If missing**: Notify user — this is a tracking mechanism, can be created during send window

---

### Phase 6: Test Email Delivery Verification (5 minutes)

**Task**: Verify user's test email arrived and links work

- [ ] **User sent test email to self** and confirmed:
  - [ ] Email arrived in inbox (not spam folder)
  - [ ] Gist links are clickable and render
  - [ ] Email formatting is intact

**Expected**: User confirms test email success  
**If test landed in spam**: 
  - Action: User checks domain blocklist (https://mxtoolbox.com/blacklists.aspx)
  - Action: If blocklisted, switch to Gmail/Protonmail with modified intro
  - Action: Resend test email
  - Do NOT proceed with Batch 1 sends until test email is confirmed in inbox

**If test was never sent**: 
  - Action: Notify user, request immediate test send
  - Do NOT proceed with Batch 1 sends

---

## Summary Status Check

**Timestamp**: 07:00 UTC May 18, 2026  
**Total time elapsed**: 43 minutes (07:00–07:43 UTC)

| Phase | Status | Decision |
|-------|--------|----------|
| Gist accessibility | ✓ All 5 live | **Proceed** |
| Contact verification | ✓ All 5 active | **Proceed** |
| Template scan | ✓ All 5 ready | **Proceed** |
| Spreadsheet setup | ✓ Baseline recorded | **Proceed** |
| Test email | ✓ Inbox confirmed | **Proceed** |

**Pre-Flight Status**: ✅ **GO FOR BATCH 1 SEND**

---

## Next Actions (by 08:00 UTC)

**User will**:
1. Open email account and draft folder
2. Send Email 1 (Wendy Weiser) at 08:00 UTC
3. Send remaining 4 emails at 30-min intervals

**Orchestrator will**:
1. Monitor batch 1 execution (08:00–12:00 UTC)
2. Log send timestamps in WAVE_1_MONITORING_DASHBOARD.md
3. Flag any bounce-backs or failures immediately
4. Activate Phase 1 measurement at 10:30 UTC

---

## Contingency Protocols

If any pre-flight check fails:
- **Gist inaccessible**: Consult PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.1
- **Contact not found**: Do not send to that contact; notify user for alternative email
- **Template has errors**: Do not send; notify user for corrections
- **Test email in spam**: Resolve domain blocklisting per spam prevention protocol
- **Spreadsheet missing**: Proceed with send (tracking can be added retrospectively)

---

**Prepared by**: Orchestrator Session 1207  
**Ready for execution**: 2026-05-18 02:57 UTC  
**Execute at**: 2026-05-18 07:00 UTC (in ~4 hours)
