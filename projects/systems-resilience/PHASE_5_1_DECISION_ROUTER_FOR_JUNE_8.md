---
title: "Phase 5.1 Decision Router — Platform Choice June 8 18:00 UTC"
project: systems-resilience
phase: 5
wave: 1+2
status: AWAITING-DECISION
purpose: "Single-source decision document for Phase 5.1 platform choice. Evaluated June 8 18:00 UTC. Determines which deployment playbook will be activated for June 9 13:00 UTC publication."
decision_deadline: 2026-06-08T18:00:00Z
decision_authority: "[User]"
---

# Phase 5.1 Decision Router
## Platform Choice Decision — Due June 8 18:00 UTC

---

## Executive Summary

**Status**: ⏳ **AWAITING PLATFORM DECISION** (Due: June 8, 2026 18:00 UTC)

**What This Document Does**:
- Stores the platform choice decision made on June 8
- Routes deployment to the correct playbook (Nextcloud+Matrix vs Discourse)
- Enables immediate June 9 deployment execution (no additional decisions needed)

**Next Steps After Decision**:
1. Choose platform option below (A or B)
2. Mark selected option with ✅
3. Link to platform-specific deployment playbook
4. June 9: Deployment team uses linked playbook for publication execution

**Timeline**:
- June 8, 18:00 UTC: Decision deadline
- June 8, 18:30 UTC: This document updated with choice
- June 9, 12:30 UTC: Deployment pre-flight begins (using selected playbook)
- June 9, 13:00 UTC: Publication upload begins

---

## PLATFORM OPTIONS

### ✅ **Option A: Nextcloud + Matrix** (if chosen)

**Decision Made**: ⏳ PENDING | ✅ CHOSEN | ❌ REJECTED

**Platform-Specific Playbook**: 
📄 [DEPLOYMENT_PLAYBOOK_NEXTCLOUD_MATRIX.md](./DEPLOYMENT_PLAYBOOK_NEXTCLOUD_MATRIX.md)

**Architecture**:
- **Nextcloud** (file server): Hosts all Phase 5 documents (markdown + PDF)
- **Matrix/Synapse** (messaging): Community discussion and notifications
- **Database**: PostgreSQL (containerized)
- **Cache**: Redis (containerized)
- **Reverse Proxy**: nginx (local install)
- **Deployment Host**: raspby1 (100.70.184.84)
- **Access**: HTTPS on ports 80/443, local reverse proxy to 8080 (Nextcloud) + 8008 (Matrix)

**User Access Model**:
- **Document Access**: Via Nextcloud web interface (public link or login required)
- **Discussion/Notifications**: Via Matrix client (Element, Nheko, or web-based)
- **Federation**: Optionally federate with other Matrix homeservers

**Deployment Duration**: ~30 minutes (containers + initialization)
**Resource Requirements**: 1.3 GB disk, 1.5 GB RAM available
**Infrastructure Status**: ✅ **READY** (verified June 7)

**Scalability**:
- Single-instance (this deployment): 100–500 concurrent users
- Multi-instance: Requires database replication and load balancer
- Roadmap: Plan Phase 6 federation and replication

**Community Fit**:
- **Best For**: Communities wanting federated infrastructure, offline-first experience
- **Strong Points**: Privacy-focused, federation-ready, familiar file interface
- **Considerations**: Requires user account creation; larger learning curve for non-technical users

**Decision Validation** (if chosen):
- [ ] Community prefers federation + privacy-first approach
- [ ] Comfortable with Matrix for discussion/messaging
- [ ] Infrastructure team familiar with Nextcloud administration
- [ ] Contingency plan reviewed (see platform-specific playbook)

---

### ❌ **Option B: Discourse** (if chosen)

**Decision Made**: ⏳ PENDING | ✅ CHOSEN | ❌ REJECTED

**Platform-Specific Playbook**: 
📄 [DEPLOYMENT_PLAYBOOK_DISCOURSE.md](./DEPLOYMENT_PLAYBOOK_DISCOURSE.md)

**Architecture**:
- **Discourse** (forum platform): Integrated discussion + document hosting
- **Database**: PostgreSQL (in container)
- **Cache**: Redis (in container)
- **Reverse Proxy**: nginx (local install)
- **Deployment Host**: raspby1 (100.70.184.84) OR external VPS (recommended for >500 users)
- **Access**: HTTPS on ports 80/443, local reverse proxy to 3000 (Discourse)

**User Access Model**:
- **Document Access**: Via Discourse topics in "Phase 5 Published Research" category
- **Discussion**: Native Discourse threaded replies (familiar forum interface)
- **Notifications**: Built-in Discourse email/notification system

**Deployment Duration**: ~20 minutes (container + initialization)
**Resource Requirements**: 3.7 GB disk, 2 GB RAM available
**Infrastructure Status**: ✅ **READY** (verified June 7)

**Scalability**:
- Single-instance (raspby1): 200–1,000 concurrent users
- Multi-instance: Requires S3 object storage and load balancer (external)
- Roadmap: Consider external VPS for Phase 6 if user growth exceeds 500

**Community Fit**:
- **Best For**: Communities wanting familiar forum experience, integrated discussions
- **Strong Points**: Low learning curve, excellent moderation tools, built-in notifications
- **Considerations**: Not federation-compatible; single-instance or external deployment required

**Decision Validation** (if chosen):
- [ ] Community prefers integrated forum experience
- [ ] Discourse notification system meets community needs
- [ ] Comfortable with forum-based discussion model
- [ ] Plan for external VPS if user growth expected (Phase 6 consideration)

---

## DECISION RECORDING

### Date of Decision

**Decision Made**: _________________________ (Date, Time UTC)

**Authority**: [User Name], Project Lead

---

### PLATFORM CHOICE

**Select one option below**:

```
┌─────────────────────────────────────────────┐
│                                             │
│  [ ] Option A: Nextcloud + Matrix           │
│                                             │
│  [ ] Option B: Discourse                    │
│                                             │
└─────────────────────────────────────────────┘
```

**Selected Platform**: _______________________

**Decision Rationale**:
```
[Document the reasons for choosing the selected platform.
Include any community feedback, technical considerations, scalability plans, etc.]
```

---

### DECISION SIGN-OFF

**Recorded By**: _________________________ (Name)

**Date/Time**: _________________________ (UTC)

**Confirmation**: ✅ Decision entered and ready for deployment

---

## DEPLOYMENT ACTIVATION

### For Deployment Team (June 9, 12:30 UTC)

**Step 1**: Retrieve this decision document
```bash
cat /path/to/PHASE_5_1_DECISION_ROUTER_FOR_JUNE_8.md
```

**Step 2**: Identify selected platform
- If "Option A (Nextcloud + Matrix)" selected → Use `DEPLOYMENT_PLAYBOOK_NEXTCLOUD_MATRIX.md`
- If "Option B (Discourse)" selected → Use `DEPLOYMENT_PLAYBOOK_DISCOURSE.md`

**Step 3**: Follow selected playbook from Section 1 onwards

**No Additional Decisions Needed**: The playbook is complete and ready for execution.

---

## PRE-DECISION CHECKLIST (For Use Before June 8)

**If you're evaluating which platform to choose, use this checklist**:

### Infrastructure Readiness
- [ ] Docker verified operational on raspby1 (PHASE_5_1_DEPLOYMENT_INFRASTRUCTURE_AUDIT.md)
- [ ] 189GB disk space available (sufficient for both platforms)
- [ ] Ports 80/443 available (both platforms need reverse proxy)
- [ ] Network connectivity verified (both platforms need internet for image pulls)

### Content Readiness
- [ ] All 12 content files verified present (PHASE_5_1_CONTENT_READINESS.md)
- [ ] Content checksums validated
- [ ] Markdown and PDF files ready for platform-specific upload

### Community Considerations

**For Nextcloud+Matrix**:
- [ ] Community wants federated infrastructure?
- [ ] Users familiar with Matrix/Element clients?
- [ ] Privacy-first approach is priority?
- [ ] Offline-first capability needed?

**For Discourse**:
- [ ] Community wants integrated forum experience?
- [ ] Low learning curve for non-technical users is priority?
- [ ] Built-in moderation tools sufficient?
- [ ] Single-instance deployment acceptable, or plan for external VPS?

### Technical Considerations

**For Nextcloud+Matrix**:
- [ ] Infrastructure team can support Nextcloud administration?
- [ ] Matrix federation topology planned?
- [ ] User account creation process defined?
- [ ] Backup/restore procedures documented?

**For Discourse**:
- [ ] Backup and restore procedures known?
- [ ] S3 object storage plan (if scaling beyond single instance)?
- [ ] SMTP email configuration ready?
- [ ] Moderation policy and process documented?

### Scalability Plan

**For Nextcloud+Matrix**:
- [ ] Phase 6 federation strategy documented?
- [ ] Multi-instance database replication plan (if needed)?

**For Discourse**:
- [ ] User growth projections (to determine if external VPS needed for Phase 6)?
- [ ] S3/CDN strategy (if scaling beyond single instance)?

---

## CONTINGENCY DECISION PROTOCOL (If Deadline Approaches)

**If decision has not been made by June 8 16:00 UTC** (2 hours before deadline):

1. **Escalate to project lead**: Contact [User Name] with summary of evaluation
2. **Recommendation**: If no clear preference:
   - **DEFAULT: Nextcloud + Matrix** (federation-ready, privacy-first alignment with project)
   - Rationale: Systems Resilience project emphasizes decentralized, community-owned infrastructure
3. **Fallback**: If still undecided by 18:00 UTC:
   - **EXECUTE WITH DEFAULT**: Use Nextcloud + Matrix playbook
   - Document decision as "default due to deadline, no explicit community preference"
   - Plan for Phase 6 evaluation if community requests platform migration

---

## DOCUMENT CONTROL

**Version**: 1.0 (Template)
**Status**: Awaiting Decision
**Last Updated**: June 7, 2026 (created as template)
**Next Update**: June 8, 2026 18:00 UTC (platform choice decision)
**Valid Until**: June 9, 2026 15:00 UTC (deployment completion)

---

## RELATED DOCUMENTS

**Infrastructure Audit**: 
📄 [PHASE_5_1_DEPLOYMENT_INFRASTRUCTURE_AUDIT.md](./PHASE_5_1_DEPLOYMENT_INFRASTRUCTURE_AUDIT.md)
- Verifies Docker, network, disk, ports, thermal management

**Content Readiness**: 
📄 [PHASE_5_1_CONTENT_READINESS.md](./PHASE_5_1_CONTENT_READINESS.md)
- Verifies all 12 files present and checksummed

**Deployment Playbook (Platform-Agnostic)**: 
📄 [PHASE_5_1_DEPLOYMENT_PLAYBOOK_TEMPLATE.md](./PHASE_5_1_DEPLOYMENT_PLAYBOOK_TEMPLATE.md)
- Steps 1–5 identical for both platforms
- Step 4 platform-specific (Nextcloud or Discourse)

**Platform-Specific Playbooks** (to be selected based on decision):
📄 [DEPLOYMENT_PLAYBOOK_NEXTCLOUD_MATRIX.md](./DEPLOYMENT_PLAYBOOK_NEXTCLOUD_MATRIX.md) (if chosen)
📄 [DEPLOYMENT_PLAYBOOK_DISCOURSE.md](./DEPLOYMENT_PLAYBOOK_DISCOURSE.md) (if chosen)

---

**End of Decision Router Document**

Next step: Make platform choice June 8 18:00 UTC, then use selected playbook June 9 for deployment.
