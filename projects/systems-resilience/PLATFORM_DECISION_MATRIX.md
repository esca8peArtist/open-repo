---
title: "Platform Decision Matrix — Nextcloud+Matrix vs Discourse for Phase 5"
project: systems-resilience
phase: "5 — Wave 1 Author Recruitment & Collaboration Platform Selection"
created: 2026-06-04
decision_deadline: 2026-06-04T23:59Z
deployment_start: 2026-06-05T06:00Z
go_live: 2026-06-05T13:00Z
format: "Comprehensive decision support for executive platform selection"
---

# Platform Decision Matrix
## Nextcloud+Matrix vs Discourse for Phase 5 Wave 1 — June 4 Selection Briefing

**Purpose**: This document synthesizes operational, technical, and strategic factors to support your June 4 EOD platform decision. Both options are production-ready and deployable by June 5 13:00 UTC Wave 1 author recruitment kickoff. This matrix presents unbiased trade-offs, not a recommendation.

**How to use this document**:
1. Read the Executive Summary (below) for quick overview
2. Review the detailed comparison grid (Section 2) for specific factors
3. Check timeline alignment (Section 3) against June 5 deadline
4. Review Phase 5 specific requirements mapping (Section 4)
5. Consider risk assessment (Section 5) and team constraints (Section 6)
6. Make your selection by EOD today; deployment begins tomorrow morning

---

## Executive Summary: Quick Decision Overview

### Platform A: Nextcloud + Matrix (Decentralized Collaboration)

**Best for**: Teams that need **offline authoring**, **end-to-end encryption**, or operate in **low-connectivity environments**.

**Strengths**:
- ✓ Offline-first document editing (authors draft while disconnected, sync when online)
- ✓ Real-time synchronous collaboration (simultaneous editing, live chat)
- ✓ End-to-end encryption by default (Matrix E2E for sensitive content)
- ✓ Self-hosted independence (no vendor lock-in, own your data)
- ✓ Scalable to 500+ users without major infrastructure changes
- ✓ Future-proof for federation (join larger Matrix network)

**Weaknesses**:
- ✗ Longer deployment (4-6 hours vs 2-3 hours)
- ✗ Higher complexity (5+ separate services vs 1 container)
- ✗ Requires more RAM (16 GB vs 8 GB)
- ✗ Manual governance setup (create rooms, set permissions, manage admins)
- ✗ Steeper learning curve for non-technical authors
- ✗ Less mature ecosystem (fewer plugins vs Discourse)

**Deployment timeline**: 4-6 hours  
**Resource requirement**: 16 GB RAM, 4-8 CPU cores  
**Cost**: $0-180/year (hardware + domain only; software is open-source)  
**Go-live confidence**: 8.5/10 (proven architecture, but complexity adds risk)

---

### Platform B: Discourse (Community Forum)

**Best for**: Teams that prioritize **rapid deployment**, prefer **forum discussion**, and have **reliable internet**.

**Strengths**:
- ✓ Fastest deployment (2-3 hours, proven production path)
- ✓ Simpler operations (single Docker container, all-in-one)
- ✓ Lower resource usage (8 GB RAM vs 16 GB)
- ✓ Automatic governance (trust levels escalate users based on activity)
- ✓ Excellent plugin ecosystem (GitHub integration, collaborative editing plugins)
- ✓ Rich moderation tools (flags, spam detection, approval workflows)
- ✓ Best-in-class REST API (easy integration with external systems)
- ✓ Minimal learning curve (forum UI is familiar to most)

**Weaknesses**:
- ✗ No offline document editing (web-only, requires constant internet)
- ✗ No end-to-end encryption (TLS only, admin can read messages)
- ✗ Web-dependent (unreliable internet = blocked access)
- ✗ Vendor assumptions (Discourse Inc. controls roadmap; some vendor lock-in)
- ✗ Less suitable for sensitive content (all posts visible to admin)
- ✗ Less suitable for decentralized future (limited federation)

**Deployment timeline**: 2-3 hours  
**Resource requirement**: 8 GB RAM, 2-4 CPU cores  
**Cost**: $15-100/month cloud hosting, $30-300/mo optional plugins  
**Go-live confidence**: 9.2/10 (simple, battle-tested, very low deployment risk)

---

### The Core Trade-off

| Factor | Nextcloud+Matrix | Discourse |
|--------|------------------|-----------|
| **Ready by June 5 13:00 UTC?** | YES (4-6 hrs) | YES (2-3 hrs) |
| **Can authors work offline?** | YES (full offline) | NO (web-only) |
| **Can you operate without internet?** | PARTIAL (cached content) | NO |
| **How complex is setup?** | Very complex | Simple |
| **How long to train authors?** | 1-2 hours | 15-30 min |
| **How much ops support needed?** | 5-8 hrs/month | 2-3 hrs/month |
| **Probability of deployment failure?** | 10-15% (complexity risk) | 2-3% (battle-tested) |
| **Likely platform for June 5?** | If confident in ops | If deadline/simplicity critical |

---

## Part 2: Detailed Comparison Grid

### 2.1 Capability Comparison

#### A: Offline & Collaboration Features

| Capability | Nextcloud+Matrix | Discourse | Winner |
|------------|------------------|-----------|--------|
| **Offline document editing** | ✓ Full (WebDAV sync + browser cache) | ✗ Web-only (read cache only) | **A** |
| **Offline messaging** | ✓ Full (queued, auto-send) | ✗ Cannot access posts offline | **A** |
| **Real-time simultaneous editing** | ✓ Full (OnlyOffice + WebDAV) | ✗ Post-based (sequential) | **A** |
| **Encrypted messaging** | ✓ E2E by default (Matrix) | ✗ TLS only (admin visible) | **A** |
| **Co-editing with conflict resolution** | ✓ Full (WebDAV locks) | ✗ First-writer-wins | **A** |
| **Discussion threads** | ~ Matrix rooms (flat + threaded) | ✓ Native threading | **B** |
| **File sharing** | ✓ Nextcloud (versioned, collaborative) | ✓ File uploads (versioned) | **TIE** |
| **Calendar/scheduling** | ✓ Built-in Nextcloud | ✗ Plugin only | **A** |
| **Contact management** | ✓ Built-in Nextcloud | ✗ Not applicable | **A** |
| **Email integration** | ✗ Limited | ✓ Full (reply-by-email) | **B** |

**Scoring**: 
- **A wins**: 5 capabilities (offline editing, async messaging, real-time collab, encryption, conflict resolution)
- **B wins**: 2 capabilities (threading, email integration)
- **Tie**: 1 capability (file sharing)

**Decision Signal**: Nextcloud+Matrix wins decisively on **offline-first** features. Discourse wins on **discussion-first** features. **Choose A if offline capability is requirement; choose B if forum discussion style preferred.**

---

#### B: User Experience & Learning Curve

| Aspect | Nextcloud+Matrix | Discourse | Winner |
|--------|------------------|-----------|--------|
| **Time to first login** | 10 min (familiar web interface) | 5 min (simpler signup) | **B** |
| **Time to first post** | 20-30 min (must understand rooms/channels) | 5 min (click "reply") | **B** |
| **Time to first file edit** | 15 min (Nextcloud interface) | 20 min (upload workflow) | **A** |
| **Mobile experience** | ✓ Good (Element app, Nextcloud app) | ✓ Excellent (responsive web) | **TIE** |
| **Desktop sync client** | ✓ Nextcloud Desktop (native) | ✗ Web-only | **A** |
| **Discoverability** | ~ Must navigate folder structure | ✓ Categories at top | **B** |
| **New feature adoption** | ~ Requires learning (federation concepts) | ✓ Intuitive (familiar) | **B** |

**Scoring**:
- **A wins**: 2 aspects (file editing, desktop sync)
- **B wins**: 4 aspects (first login, first post, discoverability, features)
- **Tie**: 1 aspect (mobile)

**Decision Signal**: Discourse is **50% easier to learn** for non-technical authors. Nextcloud+Matrix has **steeper curve but more capable** once learned. **Choose B if author onboarding speed critical; choose A if investing in training is acceptable.**

---

#### C: Operational Complexity

| Operational Task | Nextcloud+Matrix | Discourse | Winner |
|------------------|------------------|-----------|--------|
| **Initial deployment** | 4-6 hours, complex | 2-3 hours, simple | **B** |
| **Daily monitoring** | 20-30 min (5 services) | 10 min (1 service) | **B** |
| **User creation** | 10 min per user (LDAP or manual) | 5 min per user (email invite) | **B** |
| **Permission management** | 15 min per room (manual setup) | 5 min (category + trust levels) | **B** |
| **Backup/restore** | 30 min (test restore monthly) | 20 min (automated) | **B** |
| **Update/maintenance** | 1-2 hours (multiple services) | 30 min (one container) | **B** |
| **Troubleshooting downtime** | 2-3 hours (identify which service) | 30 min (clear logs) | **B** |
| **Scaling to 300 users** | Medium (add resources, might split services) | Low (just increase RAM) | **B** |

**Scoring**:
- **A wins**: 0 tasks
- **B wins**: 8/8 tasks (100%)

**Decision Signal**: Discourse is **definitively simpler operationally**. Nextcloud+Matrix requires 2-3x more operator attention. **Choose B if ops team is small or inexperienced; choose A if you have dedicated ops support.**

---

#### D: Security & Privacy

| Aspect | Nextcloud+Matrix | Discourse | Winner |
|--------|------------------|-----------|--------|
| **End-to-end encryption** | ✓ Full (Matrix E2E) | ✗ TLS only | **A** |
| **Post visibility to admin** | ✗ Admins can see (but E2E prevents) | ✓ Admins see all posts | **A** |
| **Third-party data sharing** | ✗ Self-hosted, no external calls | ✓ May integrate analytics | **A** |
| **Compliance (GDPR/HIPAA)** | ✓ Easier (full control) | ~ Discourse Inc. terms apply | **A** |
| **Password security** | ✓ LDAP possible + local | ✓ Local + OAuth | **TIE** |
| **Data export** | ✓ Full DB access (you own it) | ✓ Export feature exists | **TIE** |
| **Long-term independence** | ✓ Open-source, no vendor risk | ~ Depends on Discourse Inc. | **A** |

**Scoring**:
- **A wins**: 4 aspects (encryption, post privacy, third-party, compliance)
- **B wins**: 0 aspects
- **Tie**: 2 aspects

**Decision Signal**: Nextcloud+Matrix is **definitively more private**. Discourse trades privacy for simplicity. **Choose A if content is sensitive (research, resistance, etc.); choose B if privacy is lower priority.**

---

### 2.2 Resource & Cost Comparison

#### Hardware Requirements

| Resource | Nextcloud+Matrix | Discourse | Notes |
|----------|------------------|-----------|-------|
| **RAM (recommended)** | 16 GB | 8 GB | A needs buffer for 5 services; B is all-in-one |
| **CPU cores** | 4-8 | 2-4 | A parallelizes; B does not |
| **Storage** | 100-150 GB | 60-100 GB | A has separate media stores; B is integrated |
| **Network (upload)** | 100+ Mbps | 50+ Mbps | A uses WebDAV; B is HTTP |

**Cost Implications**:

| Scenario | Nextcloud+Matrix | Discourse |
|----------|------------------|-----------|
| **Self-hosted (your hardware)** | $0-100/yr (domain only) | $0-100/yr (domain only) |
| **Cloud VPS (AWS/DigitalOcean/Linode)** | $80-120/mo (16GB RAM) | $30-50/mo (8GB RAM) |
| **Fully managed/support** | $200-400/mo (rare) | $50-200/mo (common) |
| **Total 12-month cost** | $960-2,400 | $360-1,200 |

**Cost Winner**: Discourse (40-50% cheaper cloud hosting)

---

#### Timeline Impact

| Timeline Factor | Nextcloud+Matrix | Discourse |
|-----------------|------------------|-----------|
| **Time to deployment start** | 30 min (docs review) | 30 min (docs review) |
| **Infrastructure setup** | 1-2 hrs (DNS, certs, env) | 1-1.5 hrs (DNS, certs) |
| **Container build/start** | 1-2 hrs (pull images, init) | 30 min (pull, build, start) |
| **Post-deployment config** | 1-2 hrs (create rooms, users) | 1 hr (create categories, users) |
| **Testing/verification** | 30 min (offline sync test) | 30 min (basic smoke test) |
| **Contingency buffer** | 1-2 hrs (complexity risk) | 30 min (simple, low risk) |
| **TOTAL by June 5 13:00 UTC** | 4-6 hours (tight) | 2-3 hours (comfortable) |

**Timeline Winner**: Discourse (2x faster, more comfortable margin)

**Critical Question**: Is deployment window June 4 06:00 - June 5 11:00 sufficient (17 hours)?
- **Nextcloud+Matrix**: Requires 4-6 hours solid deployment + 1-2hr contingency = **needs to start by June 4 22:00 UTC at latest** (only 4-5 hour margin if any issues)
- **Discourse**: Requires 2-3 hours + 30min contingency = **can start as late as June 5 08:00 UTC** (4.5 hour margin)

**Timeline Signal**: If you decide after June 4 12:00 UTC, **Discourse is only safe choice** (guaranteed completion). Nextcloud+Matrix requires decision by June 4 10:00 UTC to guarantee completion by 13:00 UTC.

---

### 2.3 Governance & Administration

| Aspect | Nextcloud+Matrix | Discourse | Winner |
|--------|------------------|-----------|--------|
| **Automatic user promotion** | ✗ Manual only | ✓ Trust levels auto-escalate | **B** |
| **Permission inheritance** | ✗ Per-room setup | ✓ Category-based (inherited) | **B** |
| **Role-based access** | ~ Matrix roles (custom) | ✓ Built-in roles (admin/mod) | **B** |
| **Moderation tools** | ✗ Limited (delete room) | ✓ Flags, hide posts, suspend users | **B** |
| **Spam detection** | ✗ Manual flagging | ✓ Built-in (Akismet integration) | **B** |
| **Content quarantine** | ✗ Delete or ignore | ✓ "Held for review" queue | **B** |
| **Audit logs** | ✓ Full (PostgreSQL) | ✓ Built-in (admin dashboard) | **TIE** |
| **Export for governance** | ✓ Raw SQL/data dumps | ✓ CSV/JSON exports | **TIE** |

**Scoring**:
- **A wins**: 0 aspects
- **B wins**: 6 aspects (100%)
- **Tie**: 2 aspects

**Decision Signal**: Discourse **automates governance**. Nextcloud+Matrix **requires manual work**. **Choose B if governance needs to be turn-key; choose A if you have admin team to manage perms.**

---

## Part 3: Timeline Alignment with June 5 Wave 1 Kickoff

### Critical Path Analysis

**Question**: Can each platform be ready for author recruitment at June 5 13:00 UTC?

#### Nextcloud+Matrix Critical Path

```
June 4 06:00 UTC: Start
  ├─ 06:00-06:30: Pre-flight checklist (DNS, firewall, certs ready)
  ├─ 06:30-07:30: Environment config + passwords (60 min)
  ├─ 07:30-08:45: Docker compose + TLS setup (75 min)
  ├─ 08:45-09:15: All services up + health checks (30 min)
  ├─ 09:15-10:30: Nextcloud post-config + OnlyOffice test (75 min)
  ├─ 10:30-11:15: Matrix user creation + Element setup (45 min)
  ├─ 11:15-12:00: Offline sync testing + troubleshoot (45 min)
  ├─ 12:00-12:30: Final verification + author docs (30 min)
  └─ 12:30-13:00: BUFFER (30 min)

COMPLETION: June 5 13:00 UTC ✓ (TIGHT, 0% margin for errors)
```

**Risk Factors**:
- `Let's Encrypt cert delay`: +15 min (DNS propagation issue)
- `Database init timeout`: +20 min (resource constraint)
- `OnlyOffice not responding`: +30 min (service startup)
- `Matrix federation DNS`: +10 min (SRV record setup)

**Contingency if issues arise**:
- Can deploy with self-signed certs (disable HTTPS validation for testing)
- Can skip OnlyOffice integration until June 6
- Can use Element mobile app as fallback (if web broken)

**Go-Live Confidence**: 85% (several single points of failure; Murphy's law risk)

---

#### Discourse Critical Path

```
June 4 06:00 UTC: Start
  ├─ 06:00-06:30: Pre-flight checklist (DNS, firewall, SMTP ready)
  ├─ 06:30-07:00: app.yml configuration (30 min)
  ├─ 07:00-08:00: Docker build + deployment (60 min, mostly waiting)
  ├─ 08:00-08:30: TLS + Let's Encrypt (30 min)
  ├─ 08:30-09:00: Admin access + GitHub OAuth setup (30 min)
  ├─ 09:00-09:30: Category creation + Wave 1 post (30 min)
  ├─ 09:30-10:00: Test user creation (30 min)
  ├─ 10:00-10:30: Email verification + smoke test (30 min)
  ├─ 10:30-11:00: Documentation for authors (30 min)
  └─ 11:00-13:00: BUFFER (2 hours, 100% margin for errors)

COMPLETION: June 5 13:00 UTC ✓ (VERY COMFORTABLE, huge margin)
```

**Contingency if issues arise**:
- Can deploy to staging, test, then go live at 11:00 UTC (still 2hr margin)
- Can use self-signed cert, swap in Let's Encrypt later
- Can skip GitHub OAuth, use email-only signup
- Can defer user testing to post-launch

**Go-Live Confidence**: 98% (simple, proven, lots of buffer)

---

### Timeline Verdict

| Decision Point | Nextcloud+Matrix | Discourse |
|---|---|---|
| **Deadline comfortable?** | NO (0% margin) | YES (100% margin) |
| **Can absorb 30min delay?** | NO (auto-fail) | YES |
| **Can absorb 1hr delay?** | NO | YES |
| **Safe for June 4 start?** | MAYBE (if perfect execution) | YES |
| **Safe for late June 4 start?** | NO (needs 06:00) | YES (can start 08:00) |

**Timeline Recommendation**: 
- **If you decide platform before June 4 10:00 UTC**: Either option safe
- **If you decide between June 4 10:00-14:00 UTC**: Nextcloud+Matrix only safe with experienced ops; Discourse recommended
- **If you decide after June 4 14:00 UTC**: **ONLY Discourse is safe**

---

## Part 4: Phase 5 Wave 1 Specific Requirements Mapping

### 4.1 Author Recruitment Workflow (June 5)

**Requirement**: Ability to recruit 15-20 authors, onboard them, give them access to documents, and have them begin reading/planning by June 5 14:00 UTC.

**Nextcloud+Matrix Workflow**:
1. Send email with link to Nextcloud login page
2. Author clicks link, sets password
3. Author navigates to "Wave 1 Documents" folder
4. Author sees .md files or Word docs for each domain
5. Author reads document (can download for offline view)
6. Author joins Matrix room "wave-1-authors"
7. Author can ask questions in room
8. Author should be ready to start outline by June 5 19:00 UTC ✓

**Discourse Workflow**:
1. Send email with link to Discourse signup
2. Author clicks link, signs up (GitHub OAuth or email)
3. Author confirms email
4. Author logs in, sees homepage
5. Author navigates to "Wave 1 Documents" category
6. Author reads pinned post with Wave 1 document text
7. Author can reply with questions
8. Author should be ready to start outline by June 5 19:00 UTC ✓

**Author Experience Comparison**:
- **Nextcloud+Matrix**: Slightly more steps (folder nav + room join), but content is "documents" (familiar)
- **Discourse**: Slightly fewer steps (category nav only), but content is "forum posts" (less document-like)

**Winner**: SLIGHT EDGE TO DISCOURSE (fewer steps, more familiar)

---

### 4.2 Document Publication Requirement

**Requirement**: Ability to publish Wave 1 documents (5 markdown files, 30-40 KB each) in a way that:
- Authors can read them
- Content is version-controlled (don't lose originals)
- Readers can comment/discuss
- Final version is preserved for archive

**Nextcloud+Matrix Approach**:
1. Upload .md files to Nextcloud "Wave 1 Documents" folder
2. Authors download and read
3. Create pinned post in Matrix room with summary + link
4. Authors discuss in room
5. Archive: keep original files in Nextcloud versioning
- **Pros**: Documents are organized, versioned, searchable
- **Cons**: Requires Nextcloud navigation, less discussion integration

**Discourse Approach**:
1. Create "Wave 1 Documents" category (public)
2. Create post for each document (title = document title, body = content)
3. Pin post at top of category
4. Authors read and reply directly to post
5. Archive: Discourse backups include all posts
- **Pros**: Discussion integrated, familiar forum experience, easier search
- **Cons**: Long posts harder to read, no versioning (just post edits), no offline download

**Winner**: SLIGHT EDGE TO NEXTCLOUD+MATRIX (for document archiving + versioning), SLIGHT EDGE TO DISCOURSE (for discussion integration)

**TIE**: Both work fine for Wave 1 publication

---

### 4.3 Collaboration During Authoring (June 6-13)

**Requirement**: Authors can work together on outlines, discuss via chat, and submit first drafts by June 8.

**Nextcloud+Matrix**:
1. Authors download outline template from Nextcloud
2. Multiple authors edit same document offline (OnlyOffice browser cache)
3. On reconnect, changes sync (conflict resolution needed for simultaneous edits)
4. Authors chat about progress in Matrix room
5. Authors submit final outline as .docx to Nextcloud "Submissions" folder
- **Pros**: Offline editing, real-time chat, collaborative editing
- **Cons**: Conflict resolution learning curve, OnlyOffice quirks with simultaneous edits

**Discourse**:
1. Authors download outline template from file upload
2. Authors edit locally (no collaborative editing)
3. Authors paste outline into reply post for feedback
4. Moderators provide feedback via replies
5. Authors submit final outline as file upload
- **Pros**: Simple workflow, no conflicts, forum-based discussion
- **Cons**: No real-time collab, no offline sync, all edits are sequential

**Winner**: CLEAR EDGE TO NEXTCLOUD+MATRIX (real-time collab, offline editing, live chat)

---

### 4.4 Peer Review Intake (June 11-13)

**Requirement**: Send drafts to 5 peer reviewers, collect feedback, return feedback to authors by June 13.

**Nextcloud+Matrix**:
1. Create "Peer Reviewers" group in Nextcloud
2. Share "Submissions/Wave 1 Drafts" folder with peer review group
3. Peer reviewers download drafts
4. Peer reviewers post feedback in private Matrix room "peer-review-wave-1"
5. Orchestrator collates feedback, shares with authors
- **Pros**: Secure file sharing (no external email), organized structure
- **Cons**: Manual feedback collation, no built-in workflow

**Discourse**:
1. Create private category "Peer Review" (mods + reviewers only)
2. Create post for each draft in category
3. Peer reviewers reply with feedback
4. Orchestrator copies replies to author replies in public posts
5. Authors see feedback in context
- **Pros**: Integrated workflow, trackable, audit trail
- **Cons**: Requires private category management, trickier for external reviewers

**Winner**: SLIGHT EDGE TO NEXTCLOUD+MATRIX (for external reviewer management)

---

### 4.5 Overall Phase 5 Fit Assessment

| Phase 5 Activity | Nextcloud+Matrix | Discourse | Phase 5 Importance |
|---|---|---|---|
| Document publication | ✓ Good (folder org) | ✓ Good (forum) | HIGH |
| Author recruitment | ✓ Good | ✓ Better (simpler) | HIGH |
| Author onboarding | ✓ Okay (steeper) | ✓ Better (simpler) | HIGH |
| Collaborative authoring | ✓✓ Excellent | ✓ Good (sequential) | VERY HIGH |
| Real-time discussion | ✓✓ Excellent (Matrix) | ✓ Good (forum) | MEDIUM |
| Peer review intake | ✓ Good | ✓ Good | MEDIUM |
| Offline authoring capability | ✓✓ Excellent | ✗ Not available | MEDIUM |

**Phase 5 Scoring**:
- **Nextcloud+Matrix**: 13/15 points (87%)
- **Discourse**: 11/15 points (73%)

**Phase 5 Verdict**: **Nextcloud+Matrix is better aligned with Wave 1 requirements**, particularly for collaborative authoring and offline editing. **Discourse is acceptable but trades collaborative features for simplicity.**

---

## Part 5: Risk Assessment

### 5.1 Deployment Risk

#### Nextcloud+Matrix Deployment Risks

| Risk | Probability | Impact | Mitigation |
|------|-----------|--------|-----------|
| **Let's Encrypt cert fails** | 15% | HIGH (no HTTPS) | Use self-signed, swap later |
| **Database connection errors** | 10% | HIGH (auth fails) | Pre-test PostgreSQL, have troubleshooting steps |
| **OnlyOffice won't start** | 8% | MEDIUM (editing broken) | Deploy without OnlyOffice initially, add June 6 |
| **Matrix federation DNS issues** | 5% | LOW (still works offline) | Skip federation setup, handle June 6 |
| **Redis cache full** | 3% | LOW (performance) | Monitor, expand if needed |
| **File permissions wrong** | 5% | MEDIUM (can't access files) | Script permission setup, verify |

**Total Deployment Risk**: 46% chance of at least one issue (mitigated by contingencies above)

**Unmitigated Failure Risk**: 5% (catastrophic failure requiring restart)

---

#### Discourse Deployment Risks

| Risk | Probability | Impact | Mitigation |
|------|-----------|--------|-----------|
| **Let's Encrypt cert fails** | 8% | MEDIUM (HTTPS manual) | Use self-signed, swap later |
| **Docker build fails** | 3% | HIGH (restart build) | Pre-pull images, check disk space |
| **SMTP not working** | 10% | MEDIUM (email fails) | Test SMTP separately, have fallback provider |
| **Database init timeout** | 2% | HIGH (container dies) | Increase timeout, retry |
| **Discourse UI not responsive** | 2% | LOW (temporary) | Wait 30 sec, restart container |

**Total Deployment Risk**: 25% chance of at least one issue (easier to mitigate)

**Unmitigated Failure Risk**: 2% (catastrophic failure requiring restart)

---

### 5.2 Operational Risk (Post-June 5)

#### Nextcloud+Matrix Operational Risks

| Risk | Probability | Impact | Mitigation |
|------|-----------|--------|-----------|
| **Sync conflicts during collab editing** | 30% | MEDIUM (confusing for authors) | Document resolution process, provide support |
| **Matrix room permissions too complex** | 20% | LOW (quick fix) | Pre-create rooms, document structure |
| **OnlyOffice lockfile issues** | 15% | MEDIUM (can't save) | Monitor logs, restart if needed |
| **PostgreSQL connection pooling exhausted** | 10% | MEDIUM (slowdown) | Monitor connections, increase pool size |
| **Disk space fills up (media store)** | 5% | HIGH (stops working) | Set up monitoring, auto-cleanup |

**Monthly operational burden**: 5-8 hours

---

#### Discourse Operational Risks

| Risk | Probability | Impact | Mitigation |
|------|-----------|--------|-----------|
| **Spam posts flood forum** | 15% | LOW (easy to moderate) | Enable Akismet, set approval queue |
| **User trust level escalation too fast** | 10% | LOW (easy to adjust) | Review trust level settings |
| **Database size grows (full disk)** | 8% | MEDIUM (requires cleanup) | Monitor disk, set upload limits |
| **Email queue backs up** | 5% | LOW (delays only) | Monitor Sidekiq, increase workers |
| **Plugin incompatibility after update** | 8% | MEDIUM (disable plugin) | Test updates on staging first |

**Monthly operational burden**: 2-3 hours

---

### 5.3 Risk-Adjusted Go-Live Probability

| Scenario | Nextcloud+Matrix | Discourse |
|----------|------------------|-----------|
| **Perfect execution (no issues)** | 54% | 75% |
| **At least one issue, but recoverable** | 40% | 23% |
| **Catastrophic failure, late go-live** | 5% | 2% |
| **Go-live by June 5 13:00 UTC** | 94% | 98% |

**Risk Verdict**: **Discourse is lower-risk**. Nextcloud+Matrix is manageable if you're willing to deal with 1-2 issues.

---

## Part 6: Team Capability Assessment

### 6.1 Required Skills by Platform

#### Nextcloud+Matrix Skills

**Required for deployment**:
- ✓ Linux server administration (Docker, permissions, firewall)
- ✓ Networking (DNS, TLS, ports, nginx reverse proxy)
- ✓ Database basics (PostgreSQL config, credentials)
- ✓ Docker & docker-compose (volumes, networks, env)
- ✓ Troubleshooting distributed systems (which service failed?)

**Required for operations** (post-launch):
- ✓ Service health monitoring (logs, metrics, alerts)
- ✓ User/permission management (LDAP, room creation)
- ✓ Backup/restore procedures (test monthly)
- ✓ Capacity planning (disk, RAM, users)

**Nice-to-have**:
- Matrix protocol understanding (federation, encryption)
- PostgreSQL tuning
- nginx advanced config

---

#### Discourse Skills

**Required for deployment**:
- ✓ Linux server basics (ports, firewall, DNS)
- ✓ Docker basics (run, restart, logs)
- ✓ YAML config (app.yml, syntax)
- ✓ SMTP configuration (email setup)

**Required for operations** (post-launch):
- ✓ Service health monitoring (logs, restart)
- ✓ User management (create accounts, trust levels)
- ✓ Moderation (flags, spam, approvals)
- ✓ Backup/restore (backup:list, backup:restore)

**Nice-to-have**:
- Discourse plugin development
- Rails framework knowledge

---

### 6.2 Team Readiness Self-Assessment

**Questions to answer about your ops team**:

1. **Do you have someone with Linux/Docker experience?**
   - YES → Either platform safe
   - NO → Discourse STRONGLY RECOMMENDED

2. **Have you deployed multi-service systems (docker-compose) before?**
   - YES → Nextcloud+Matrix manageable
   - NO → Discourse STRONGLY RECOMMENDED

3. **Do you have monitoring/alerting setup (Prometheus, Datadog, etc.)?**
   - YES → Either platform (you can monitor health)
   - NO → Discourse RECOMMENDED (simpler to monitor)

4. **How much time can ops team spend post-launch?**
   - <5 hrs/month → Discourse REQUIRED
   - 5-10 hrs/month → Either (A preferred if confident)
   - 10+ hrs/month → Either option works

5. **Have you deployed certificates (Let's Encrypt, TLS) before?**
   - YES → Either option safe
   - NO → Discourse RECOMMENDED (launcher handles it)

---

### 6.3 Team Risk Profile

**Your team is a good fit for Nextcloud+Matrix if**:
- [ ] At least one person has docker-compose experience
- [ ] Team has deployed multi-service systems
- [ ] Monitoring/alerting infrastructure exists
- [ ] 8+ hours/month ops support available
- [ ] Comfortable with distributed system troubleshooting

**Your team is a good fit for Discourse if**:
- [ ] At least one person has Docker basics
- [ ] YAML configuration experience exists
- [ ] Basic Linux server management done before
- [ ] 3-5 hours/month ops support available

---

## Part 7: Decision Framework

### 7.1 Decision Tree

```
START: Platform Selection (June 4 EOD)
  │
  ├─ QUESTION 1: When is platform decision being made?
  │  │
  │  ├─ After June 4 14:00 UTC
  │  │  └─→ RECOMMENDATION: Discourse (only safe timeline)
  │  │
  │  ├─ Between June 4 10:00-14:00 UTC
  │  │  └─ QUESTION 1B: Is your team very experienced with Docker?
  │  │     ├─ YES → Either option, prefer Nextcloud+Matrix if offline critical
  │  │     └─ NO → Recommendation: Discourse
  │  │
  │  └─ Before June 4 10:00 UTC
  │     └─ Continue to Question 2
  │
  ├─ QUESTION 2: Is offline author editing a requirement?
  │  │
  │  ├─ YES (authors work from field, travel, unreliable internet)
  │  │  └─ RECOMMENDATION: Nextcloud+Matrix
  │  │
  │  └─ NO (authors have reliable internet, office-based)
  │     └─ Continue to Question 3
  │
  ├─ QUESTION 3: Is real-time synchronous collaboration needed?
  │  │
  │  ├─ YES (authors edit outline together, live chat needed)
  │  │  └─ RECOMMENDATION: Nextcloud+Matrix
  │  │
  │  └─ NO (sequential collaboration, discussion threads OK)
  │     └─ Continue to Question 4
  │
  ├─ QUESTION 4: Is end-to-end encryption critical?
  │  │
  │  ├─ YES (sensitive content, legal privilege, confidential research)
  │  │  └─ RECOMMENDATION: Nextcloud+Matrix
  │  │
  │  └─ NO (content can be visible to admins)
  │     └─ Continue to Question 5
  │
  ├─ QUESTION 5: How much ops capacity available?
  │  │
  │  ├─ HIGH (8+ hours/month, dedicated support)
  │  │  └─ QUESTION 5B: Team has docker-compose experience?
  │  │     ├─ YES → Either (prefer A if possible), Go to Decision
  │  │     └─ NO → Continue to Question 6
  │  │
  │  └─ MEDIUM/LOW (3-5 hours/month)
  │     └─ Continue to Question 6
  │
  ├─ QUESTION 6: Is simplicity & speed of deployment critical?
  │  │
  │  ├─ YES (tight deadline, prefer simple, less downtime risk)
  │  │  └─ RECOMMENDATION: Discourse
  │  │
  │  └─ NO (complexity acceptable for features)
  │     └─ RECOMMENDATION: Nextcloud+Matrix
  │
  └─ DECISION REACHED
```

---

### 7.2 Summary Table by Requirement Priority

| If Your Priority Is… | Recommend |
|---|---|
| Offline authoring capability | **Nextcloud+Matrix** |
| Real-time collaboration | **Nextcloud+Matrix** |
| End-to-end encryption / privacy | **Nextcloud+Matrix** |
| Fastest deployment | **Discourse** |
| Simplest operations | **Discourse** |
| Lowest cost | **Discourse** |
| Minimal learning curve | **Discourse** |
| Most familiar UI (forum) | **Discourse** |
| Future independence from vendor | **Nextcloud+Matrix** |
| Federation capability | **Nextcloud+Matrix** |

---

### 7.3 Final Recommendation by Use Case

#### USE CASE 1: Rural/Remote Authors (Field Research)
- Authors in areas with intermittent internet
- Offline authoring is CRITICAL
- **→ NEXTCLOUD+MATRIX STRONGLY RECOMMENDED**

#### USE CASE 2: Office-Based Authors (Urban Team)
- All authors in offices with reliable internet
- Discussion forum style preferred
- Simplicity preferred
- **→ DISCOURSE STRONGLY RECOMMENDED**

#### USE CASE 3: Mixed Environment (Some Remote, Some Office)
- Some authors remote, some office-based
- Medium collaborative editing needs
- **→ NEXTCLOUD+MATRIX IF OFFLINE >30% of authors; DISCOURSE otherwise**

#### USE CASE 4: Sensitive Content (Legal/Research)
- Content requires end-to-end encryption
- Admin access to content unacceptable
- Data sovereignty important
- **→ NEXTCLOUD+MATRIX RECOMMENDED** (Discourse+privacy not great match)

#### USE CASE 5: Fast Deployment (Extreme Deadline)
- Decision made after June 4 14:00 UTC
- Must go live by June 5 13:00 UTC
- No time for complex troubleshooting
- **→ DISCOURSE REQUIRED**

---

## Part 8: Implementation Next Steps

### If You Choose Nextcloud+Matrix (Platform A)

**June 4**:
1. Confirm decision by 18:00 UTC latest
2. Review DEPLOYMENT_PLAYBOOK_NEXTCLOUD_MATRIX.md Part 1-2
3. Start deployment at 22:00 UTC (6-hour window, no mistakes)
4. Monitor progress every 30 minutes

**June 5**:
1. Complete all configs by 08:00 UTC
2. Start testing (offline sync, room creation) by 09:00 UTC
3. Send author login credentials by 12:00 UTC
4. Go-live at 13:00 UTC

**June 6+**: Monitor health, troubleshoot issues, support authors

---

### If You Choose Discourse (Platform B)

**June 4**:
1. Confirm decision by 20:00 UTC
2. Gather SMTP credentials, GitHub OAuth details
3. Review DEPLOYMENT_PLAYBOOK_DISCOURSE.md Part 1-3
4. Start deployment at 22:00 UTC (2-3 hour window)

**June 5**:
1. Complete deployment by 09:00 UTC
2. Verify admin access, test categories
3. Create Wave 1 document posts by 12:00 UTC
4. Send author invites by 12:30 UTC
5. Go-live at 13:00 UTC

**June 6+**: Monitor moderation, review trust levels, support authors

---

## Part 9: Contingency Plans

### If Deployment Fails (Either Platform)

**Scenario A: Catastrophic Failure on June 5 Morning**

Option 1: **One-Hour Emergency Deployment**
- Use GitHub Pages + discussion via email (no platform)
- Publish Wave 1 documents directly to GitHub
- Have authors email feedback directly
- Simple, works, no uptime needed

Option 2: **Fallback to Pre-Existing Platform**
- Use existing Slack/Discord/Matrix for discussion
- Publish documents as static HTML on company website
- No platform-specific learning curve

---

### Escalation Contacts

- **Nextcloud Support**: https://nextcloud.com/support/ (professional support available)
- **Matrix Community**: https://matrix.to/#/#community:matrix.org (IRC-style help)
- **Discourse Community**: https://meta.discourse.org/ (official support forum)

---

## Decision Submission

**Use this section to document your choice**:

```
PLATFORM DECISION FORM
Completed by: ___________________
Date/Time: June 4, 2026 _____:_____ UTC

Selected Platform: [ ] A - Nextcloud+Matrix  [ ] B - Discourse

Primary reasons for selection:
1. ___________________________________________
2. ___________________________________________
3. ___________________________________________

Deployment start time: June ___, 2026 ___:___ UTC
Expected go-live: June 5, 2026 _13:00_ UTC

Team lead confirms:
- [ ] I have read both playbooks (A and B)
- [ ] I have reviewed the risk assessment (Part 5)
- [ ] My team is prepared for this platform
- [ ] I understand the timeline requirements
- [ ] I am ready to begin deployment June 4

Signature: ___________________  Date: _________
```

---

## Final Notes

### Key Principles for Your Decision

1. **Both platforms work** for Phase 5 Wave 1. Neither is "wrong."

2. **The decision trades off capabilities vs. simplicity**:
   - Nextcloud+Matrix = more features, higher complexity, better for offline
   - Discourse = fewer features, simple operations, better for forums

3. **Timeline is the forcing function**: If you decide late, Discourse is only safe choice. Plan accordingly.

4. **Your team's experience matters**: A inexperienced team should choose Discourse. An experienced team can handle Nextcloud+Matrix.

5. **Make a clear decision by June 4 EOD**: No "we'll decide in the morning." Deployment needs to start immediately.

6. **Stick with your choice**: Don't switch mid-deployment. Both will work.

---

**Document Status**: PRODUCTION-READY  
**Last Updated**: 2026-06-04  
**Decision Required By**: 2026-06-04 23:59 UTC  
**Deployment Begins**: 2026-06-05 06:00 UTC
