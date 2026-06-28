---
title: "Systems Resilience Platform Decision Quickstart"
project: systems-resilience
phase: "5.1"
status: DECISION REQUIRED
decision_deadline: IMMEDIATE
created: 2026-06-28
context: "Phase 5.1 publication deployment blocking on platform choice. Two production-ready runbooks staged. User must choose ONE for immediate execution."
---

# Platform Decision Quickstart
## Binary Choice for Phase 5.1 Publication

**You must choose ONE platform now. Both are production-ready and executable. Your choice determines which runbook to execute.**

---

## Quick Comparison Matrix

| Factor | Nextcloud + Matrix | Discourse |
|--------|-------------------|-----------|
| **Pi5 Compatibility** | ✅ Zero blockers | ⚠️ IPv6 bug (3 workarounds) |
| **Setup Time** | 2–4 hours | 3–5 hours |
| **Offline Editing** | ✅ Native (desktop sync) | ❌ Browser-only |
| **End-to-End Encryption** | ✅ Matrix/Element E2E | ❌ None |
| **Complexity** | Moderate (5 containers) | High (1 complex container) |
| **SMTP Required** | Optional (nice-to-have) | Required (mandatory) |
| **Bootstrap Time on Pi5** | 20–30 min | 90–120 min |
| **Confidence Score** | **8/10** | **5/10** |
| **Recommendation** | **RECOMMENDED** | Alternative only |

---

## Decision Criteria

### Choose Nextcloud + Matrix IF:
- ✅ You want offline editing capability (desktop client caches files locally)
- ✅ You want E2E encryption for sensitive discussions
- ✅ You want faster initial deployment (2–4 hours vs 5+ hours)
- ✅ You want maximum compatibility with Pi5 (zero known blockers)
- ✅ You want simpler operations (5 standard Docker containers, no ARM64 compilation)
- ✅ You value file sync over forum-style threading

### Choose Discourse IF:
- ✅ You prefer a traditional forum interface (threading, voting, flagging)
- ✅ You have existing experience with Discourse
- ✅ You can provide SMTP credentials NOW (email is mandatory for Discourse)
- ✅ You're willing to apply 3 IPv6 workarounds and keep them applied permanently
- ✅ You can tolerate 90–120 minute bootstrap window on Pi5
- ✅ You want built-in moderation tools (topic locking, post deletion, user suspensions)

---

## The Pi5 IPv6 Bug Explained (Why Nextcloud is Safer)

**Issue**: Discourse on Raspberry Pi 5 64-bit has an open bug (meta.discourse.org #296408) where the hostname `localhost` sometimes resolves to IPv6 instead of IPv4. This breaks Redis communication and Sidekiq job processing.

**Workarounds Required** (all 3 must be applied permanently):
1. Force IPv4 in Redis client config
2. Disable IPv6 loopback in `/etc/hosts`
3. Set RAILS IPv4-only mode

**Impact of Bug**:
- Sidekiq jobs fail sporadically
- Email delivery fails
- Search indexing fails
- Workarounds are permanent (can't be undone)

**Nextcloud + Matrix**:
- Zero reported IPv6 issues
- Uses standard Docker networking (no localhost resolution)
- No ARM64 compilation needed
- All containers run as pre-built images

---

## Deployment Path Comparison

### Nextcloud + Matrix Path

**When to start**: Anytime (no external dependencies)

**Prerequisites**:
- None (SMTP is optional for notifications only)
- Docker + Compose already available

**Timeline**:
- Phase 1–2: Environment setup (30 min)
- Phase 3–5: Configuration (30 min)
- Phase 6–8: Container launch (60 min)
- Phase 9–11: Verification (30 min)
- **Total: 3–4 hours**

**Go/No-Go Criteria**:
- All 6 containers running ✅
- All health checks passing ✅
- Nextcloud OCC status = "ok" ✅
- Matrix versions endpoint responding ✅

**If deployment fails**: Rollback is 10 minutes (destroy volumes, delete data directories, restart). No data is persistent until you configure file sync.

**Runbook**: `SYSTEMS_RESILIENCE_NEXTCLOUD_DEPLOYMENT_RUNBOOK.md` (production-ready, 150+ steps)

---

### Discourse Path

**When to start**: ONLY after you have SMTP credentials

**Prerequisites** (REQUIRED):
- SMTP credentials from Brevo, AWS SES, Mailgun, or SendGrid
  - Brevo (free): https://www.brevo.com → Settings → SMTP credentials
  - Takes 5–10 minutes to set up
- Docker + Compose already available

**Timeline**:
- Phase 1–3: System checks (30 min)
- Phase 4: Bootstrap (90–120 min on Pi5, watching for ARM64 compilation)
- Phase 5: IPv6 workarounds (15 min)
- Phase 6–9: Config + users (60 min)
- Phase 10–11: Verification (45 min)
- **Total: 3.5–5 hours** (plus 2 hours waiting for bootstrap)

**Go/No-Go Criteria**:
- Bootstrap exit code = 0 ✅
- Container status = "up" ✅
- HTTPS returns 200 for `/about.json` ✅
- IPv6 workarounds verified (Redis ping successful) ✅

**If deployment fails**: Rollback takes 20–30 minutes (stop container, fix app.yml, rebuild). No data is persistent until day 2 when backups start running.

**Known Issues After Deployment**:
- IPv6 workarounds must remain applied forever
- Email delivery depends on SMTP (if misconfigured, silent failure)
- Bootstrap on Pi5 is slow (compile time is variable 90–120 min)

**Runbook**: `SYSTEMS_RESILIENCE_DISCOURSE_DEPLOYMENT_RUNBOOK.md` (production-ready, 150+ steps, includes 3 mandatory workarounds)

---

## Risk Analysis

### Nextcloud + Matrix Risks

| Risk | Severity | Mitigation |
|------|----------|-----------|
| Unfamiliar UI for authors | Low | Element Web is standard Matrix client; only 2–3 learning steps |
| File sync conflicts possible | Low | Nextcloud handles conflicts with dated copies; expected behavior |
| E2E encryption adds UX friction | Low | Optional; can be enabled per-room later |

**Overall Risk Level: LOW**

### Discourse Risks

| Risk | Severity | Mitigation |
|------|----------|-----------|
| IPv6 bug causes intermittent failures | Medium | 3 permanent workarounds required; keep applied forever |
| SMTP misconfiguration silently breaks email | Medium | Test SMTP after Phase 6; logs don't show errors clearly |
| Bootstrap takes 2 hours on Pi5 | Medium | Budget 3–5h; cannot interrupt bootstrap |
| ARM64 compilation slower than x86 | Medium | Expected; no mitigation other than wait time |

**Overall Risk Level: MEDIUM**

---

## Feature Fit for Phase 5.1

### Publication Requirements (Phase 5.1 Wave 1+2)

- 61,611 words of research across 5 documents
- 336+ citations and references
- PDF downloads required
- Public read access
- Author/editor accounts for team collaboration
- Archive-friendly (should work in 10+ years)

### Nextcloud Fit

✅ **Excellent** for content publication
- File storage with version history
- CalDAV/CardDAV for team coordination
- Markdown editor (Text app) for collaborative writing
- PDF downloads built-in (store PDFs in Files app)
- Offline access via desktop sync
- E2E encryption optional

### Discourse Fit

✅ **Good** for community forum (but overkill for publication archive)
- Threading is designed for discussion, not archive
- PDF attachments possible but clunky
- Strong moderation and anti-spam tools (not needed for closed community)
- Full-text search built-in
- User reputation system (nice-to-have)

**Verdict**: Both work. Nextcloud is more focused on content storage/collaboration. Discourse is more focused on discussion/community.

---

## Session 3563 Recommendation

From Session 3563 analysis:
- **Nextcloud + Matrix**: 8/10 confidence
- **Discourse**: 5/10 confidence
- **Reason for gap**: 
  - Nextcloud: Zero Pi5-specific blockers, faster bootstrap, simpler ops
  - Discourse: IPv6 bug requires permanent workarounds, slower bootstrap, higher ops complexity

**Recommendation: Nextcloud + Matrix (chosen by Session 3563 with 8/10 confidence)**

---

## Decision Checklist

Before you decide, confirm:

### If choosing Nextcloud + Matrix:
- [ ] I have Docker + Compose installed
- [ ] I have 32+ GB free disk space
- [ ] I have 3–4 hours to execute first deployment
- [ ] I'm comfortable with 5-container Docker stack
- [ ] I understand offline editing will be via desktop client (optional feature)

### If choosing Discourse:
- [ ] I have Docker + Compose installed
- [ ] I have 32+ GB free disk space
- [ ] **I have SMTP credentials ready** (from Brevo, SES, Mailgun, SendGrid)
- [ ] I have 3–5 hours to execute (including 2h bootstrap wait)
- [ ] I'm comfortable applying and keeping 3 IPv6 workarounds permanent
- [ ] I understand email delivery depends on SMTP (test after Phase 6)
- [ ] I'm comfortable with ARM64 compilation (90–120 min on Pi5)

---

## DECISION PROMPT

**Choose your platform now:**

```
WHAT IS YOUR CHOICE FOR PHASE 5.1 DEPLOYMENT?

A) Nextcloud + Matrix (Recommended: 8/10, faster, zero blockers)
B) Discourse (5/10, forum interface, IPv6 workarounds required)
```

**How to respond**:
1. Add to INBOX.md: `[phase-5-deployment] CHOICE=A` (or `CHOICE=B`)
2. If Discourse (B), also provide: `SMTP_HOST=` `SMTP_USER=` `SMTP_PASSWORD=` `SMTP_PORT=`
3. Orchestrator will detect your decision and execute the chosen runbook immediately

**Timeline after you decide**:
- Nextcloud + Matrix: Ready in 3–4 hours from start
- Discourse: Ready in 3.5–5 hours from start (including bootstrap wait)

---

## After Deployment

Both platforms will be running on raspby1 (100.70.184.84) and accessible via Tailscale or public DNS (if configured).

### Access URLs

**Nextcloud + Matrix**:
- Nextcloud: `https://nextcloud.resilience-hub.local`
- Matrix (Element Web): `https://element.resilience-hub.local`
- Admin account: See deployment runbook Phase 10

**Discourse**:
- Forum: `https://100.70.184.84` (or your configured hostname)
- Admin panel: `/admin`
- Admin account: See deployment runbook Phase 6

### Immediate Next Steps (Post-Deployment)

**For Nextcloud + Matrix**:
1. Create author accounts via Nextcloud admin panel
2. Install Nextcloud desktop client on each author machine
3. Create Matrix rooms in Element for team coordination
4. Upload PDF content to Nextcloud Files app

**For Discourse**:
1. Create author accounts via Rails console or web interface
2. Create categories for content organization
3. Configure permissions (public read, author-only post)
4. Upload PDF content as topic attachments

---

## Support and Troubleshooting

If deployment fails:
1. **Check Phase N criteria**: Each runbook phase has explicit "Verification" sections
2. **Stop at first failure**: Do not skip ahead. Fix and retry.
3. **Rollback is quick**: Both platforms support clean rollback (10–20 min)
4. **Restart deployment**: Fix the identified issue, then re-run from the failed phase

**Common issues**:
- Nextcloud: php-fpm not responding → restart container
- Discourse: IPv6 connection refused → apply workarounds (Phase 5)
- Both: Disk full → `docker system prune -f`

---

**MAKE YOUR DECISION NOW**

Add your choice to INBOX.md. The runbook is ready to execute immediately upon your decision.

Recommended: **Nextcloud + Matrix (A)**
