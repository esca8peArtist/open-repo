---
title: "Tier 2 Threat Briefing Slides: May 2026 Visual Summary"
project: cybersecurity-hardening
created: 2026-05-06
status: ready-for-distribution
audience: Tier 2 — all sectors; designed for presenter use or self-study
format: Markdown slides (Marp-compatible; also usable as Canva/Google Slides template)
depends-on: may-2026-advanced-threats.md, may-2026-tier2-threat-briefing.md
purpose: >
  Sector-agnostic master slide deck for Tier 2 distribution. 5-slide structure
  covers threat landscape, threat breakdown, immediate actions (30-day), and
  90-day roadmap. Sector-specific appendix slides follow the master deck.
  Presenters can use slides 1-5 as-is and add their sector appendix.
---

<!-- Master Deck — Slides 1–5 -->
<!-- Use with Marp (marp.app) for rendered output, or import headings into Canva/Google Slides -->
<!-- Presenter notes are in blockquotes below each slide -->

---

# May 2026 Threat Landscape
## What Civil Society Organizations Need to Know Now

**Cybersecurity Hardening Project**
May 2026 | Public distribution

> **Presenter notes**: This deck is designed for a 20–30 minute presentation or self-study. The full companion corpus (threat model + countermeasures playbook) is at https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108. All claims are sourced to FOIA disclosures, government contracts, and primary security research — appropriate for citation in published work.

---

## Slide 1: Five Threats That Changed in May 2026

```
┌─────────────────────────────────────────────────────────────────┐
│  MAY 2026: WHAT CHANGED                                         │
│                                                                 │
│  1. VOICE + VIDEO IDENTITY VERIFICATION HAS FAILED             │
│     Voice clone: 3-second sample → real-time conversation      │
│     Deepfake video: defeats liveness checks at $629/year        │
│     Human detection accuracy: < 30%                            │
│                                                                 │
│  2. DEVELOPER TOOLS COMPROMISED APRIL–MAY 2026                 │
│     Bitwarden CLI compromised April 22 (90-minute window)       │
│     1,800+ developer repos with stolen credentials             │
│     Supply chain campaign ongoing since September 2025          │
│                                                                 │
│  3. FEDERAL ELECTION SECURITY DISMANTLED                       │
│     CISA: lost 1,000 positions + EI-ISAC defunded              │
│     NSA/Cyber Command: election security group NOT reconvened   │
│     Russia: +$458M information operations budget for 2026       │
│                                                                 │
│  4. GOVERNMENT SURVEILLANCE EXPANDED TO EVERY AGENCY           │
│     Palantir: Pentagon (program-of-record), USDA ($300M),       │
│     IRS (relationship mapping), ICE (Sept 2026 deadline)        │
│     Architecture: same platform, every major federal agency     │
│                                                                 │
│  5. POLICY WINDOW: 90 DAYS TO ACT                              │
│     FISA 702 deadline: June 12                                  │
│     IRS–ICE data sharing: circuit court (active)               │
│     State election protection legislation: 7 states active     │
└─────────────────────────────────────────────────────────────────┘
```

> **Presenter notes**: Start with the discontinuities — what's different from April, not what's the same. The five items here are the ones that require updated organizational response. Each has a countermeasure and a timeline. Slide 2 goes deeper on each threat category.

---

## Slide 2: Threat Breakdown — Three Areas Requiring Immediate Response

```
┌──────────────────────────────┬───────────────────────────────────┐
│  SYNTHETIC IDENTITY + VOICE  │  SUPPLY CHAIN                     │
│  CLONING                     │                                   │
│                              │  What happened:                   │
│  The attack (confirmed 2026):│  Shai-Hulud campaign Wave 3       │
│  → Build synthetic identity  │  April–May 2026                   │
│    from breach data ($5)     │                                   │
│  → Clone voice from 3-sec    │  Bitwarden CLI: April 22          │
│    public audio sample       │  90-minute compromise             │
│  → Inject deepfake video     │  Via hijacked GitHub Action       │
│    into liveness check       │                                   │
│  → Combine all three         │  Also compromised:                │
│    simultaneously            │  • PyTorch Lightning (10M dls/mo) │
│                              │  • SAP enterprise packages        │
│  Cost: $629/year             │  • intercom-php client            │
│  Detection: < 30% accuracy   │                                   │
│                              │  Pattern: trusted tools targeted  │
│  What still works:           │  deliberately, not randomly       │
│  • Code word (no tech)       │                                   │
│  • Two-channel verification  │  Fix: official installers ONLY    │
│  • Signal safety numbers     │  Never: npm / pip / brew          │
└──────────────────────────────┴───────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────┐
│  FIRMWARE THREAT (Forward-Looking)                               │
│                                                                  │
│  LogoFAIL: UEFI vulnerability in 95% of x86 devices             │
│  BootKitty: working exploit (Linux, proof-of-concept, Nov 2024)  │
│  Persistence: survives OS reinstall, disk encryption, all EDR    │
│                                                                  │
│  Timeline: 12–24 months research-to-nation-state-deployment gap  │
│  Action now: apply UEFI firmware updates from device manufacturer│
└──────────────────────────────────────────────────────────────────┘
```

> **Presenter notes**: The supply chain and firmware threats are technical but the key message is simple: install security tools from official sources only, and apply firmware updates. The synthetic identity / voice cloning threat is the hardest shift for most audiences — the point is that technical detection has failed and the response is now procedural (code words, two-channel verification). Emphasize: a video call appearance is no longer reliable identity confirmation.

---

## Slide 3: Palantir Surveillance Expansion — What's New Since April

```
┌─────────────────────────────────────────────────────────────────┐
│  PALANTIR FEDERAL FOOTPRINT: MAY 2026 ADDITIONS                 │
│                                                                 │
│  ALREADY DOCUMENTED (April):                                    │
│  • ICE: ELITE + ImmigrationOS ($60M+) — deportation targeting   │
│  • IRS: $130M+ relationship mapping across financial networks   │
│  • DHS: $1B blanket purchase agreement (all components)         │
│                                                                 │
│  NEW IN APRIL–MAY 2026:                                        │
│  • Pentagon: Maven program-of-record (March 9, Feinberg memo)  │
│    → Protected budget line item; 10-year $10B Army contract     │
│    → The ICM / DHS model follows the Maven playbook            │
│                                                                 │
│  • USDA $300M (April 22):                                       │
│    → "One Farmer, One File" — every farmer in FSA/NRCS/RMA     │
│    → $75M sub-component: federal workforce BOSSWARE             │
│                                                                 │
│  • ICE ICM sole-source: September 2026 DEADLINE                │
│    → Biometric integration across all federal law enforcement   │
│    → Operational 2 months before November midterms             │
│                                                                 │
│  THE ARCHITECTURE:                                              │
│  Not a single master database — separate Foundry instances      │
│  at each agency, interoperable through a shared query API       │
│  → Cross-agency correlation without formal data sharing         │
└─────────────────────────────────────────────────────────────────┘
```

> **Presenter notes**: The key architectural point is the "mega API" framing. Palantir correctly states there is no single master database. But separate instances of the same platform with a shared query interface achieve the same correlational capability without requiring a formal cross-agency data sharing agreement. The IRS relationship-mapping and the ICE targeting system can reach each other through this architecture even without a formal MOU. The IRS–ICE data sharing litigation that's in circuit court addresses only one formal agreement — it does not address platform-layer interoperability.

---

## Slide 4: 30-Day Immediate Actions by Role

```
┌──────────────────────┬───────────────────────┬──────────────────┐
│  ANY ORGANIZATION    │  TECHNICAL STAFF       │  POLICY/ADVOCACY │
│                      │                        │                  │
│  THIS WEEK:          │  THIS WEEK:            │  JUNE 12:        │
│  □ Establish code    │  □ Audit GitHub        │  FISA 702 vote   │
│    word protocol     │    Actions — pin to    │  Data broker     │
│    with your team    │    commit SHA          │  loophole        │
│                      │                        │  provision       │
│  □ Two-channel       │  □ Migrate CI/CD to    │  S.4082          │
│    verification for  │    OIDC short-lived    │  Wyden/Lee/      │
│    any financial or  │    tokens              │  Davidson/Lofgren│
│    sensitive action  │                        │                  │
│                      │  □ Generate SBOM for   │  Contact your    │
│  □ Install/update    │    all production      │  senators before │
│    security tools:   │    tooling             │  June 5          │
│    OFFICIAL APP ONLY │                        │                  │
│    Never npm/pip     │  □ Rotate credentials  │  ONGOING:        │
│                      │    for any package     │  IRS–ICE         │
│  □ Hardware FIDO2    │    manager installs     │  circuit court   │
│    MFA on critical   │    April 21–May 31     │  appeal          │
│    accounts (YubiKey)│                        │  Amicus support  │
│                      │  □ Apply UEFI          │  available       │
│  □ Signal: verify    │    firmware updates    │                  │
│    safety numbers    │    from manufacturer   │  7 states:       │
│    with key contacts │                        │  election        │
│                      │  □ fwcheck.binarly.io  │  protection      │
│                      │    on organizational   │  legislation     │
│                      │    hardware            │  active          │
└──────────────────────┴───────────────────────┴──────────────────┘
```

> **Presenter notes**: The code word protocol and two-channel verification are the highest-impact, zero-cost actions for any organization regardless of technical capacity. These can be implemented in the time it takes to read this slide. The FIDO2 hardware MFA upgrade has a cost (~$50–$60 per key, order two per person) but is now the minimum reliable second factor given voice biometric and TOTP limitations under sophisticated attack. June 12 is the hard policy deadline — constituent engagement before June 5 is the practical window.

---

## Slide 5: 90-Day Roadmap + Resource Links

```
┌─────────────────────────────────────────────────────────────────┐
│  90-DAY ROADMAP: MAY – AUGUST 2026                              │
│                                                                 │
│  MAY (NOW):                                                     │
│  → Deploy code word + two-channel verification protocols        │
│  → Rotate credentials from April 21–May 31 package installs    │
│  → Order FIDO2 hardware tokens for high-priority staff          │
│  → Engage senators on FISA data broker provision (June 12)      │
│                                                                 │
│  JUNE:                                                          │
│  June 12: FISA 702 vote — watch for data broker loophole        │
│  → Apply UEFI firmware updates across organizational hardware   │
│  → Complete SBOM generation and Socket.dev integration          │
│  → Verify Signal safety numbers with all high-value contacts    │
│                                                                 │
│  JULY–AUGUST:                                                   │
│  → State election protection legislation windows active         │
│  → IRS–ICE circuit court ruling expected                        │
│  → ICE ICM deployment prep: document architecture for           │
│    September accountability moment                              │
│  → Deepfake political advertising: primary source verification  │
│    discipline for all electoral content before forwarding       │
│                                                                 │
│  SEPTEMBER (WATCH DATE):                                        │
│  → ICE ICM deployment deadline: biometric integration goes live │
│  → This is the most significant ICE surveillance capability     │
│    expansion since ELITE launched                               │
└─────────────────────────────────────────────────────────────────┘

RESOURCES:
  OpSec corpus:  https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
  EFF helpline:  https://www.eff.org/pages/digital-security-helpline
  Access Now:    security@accessnow.org
  UEFI scan:     https://fwcheck.binarly.io
  Supply chain:  https://socket.dev
```

> **Presenter notes**: The September 2026 ICE ICM deployment deadline is the most important forward-looking milestone in this deck. When the biometric-integrated Investigative Case Management system goes live, it will represent a qualitative expansion in ICE's operational capability — full biometric deduplication across all federal law enforcement databases, integrated with real-time investigative tracking. The civil society response to that deployment will require documented architecture analysis. Organizations with technical capacity should be preparing now to document what becomes operational in September.

---

<!-- SECTOR-SPECIFIC APPENDIX SLIDES -->
<!-- Add the appropriate appendix for your audience after Slide 5 -->

---

## Appendix A: Academic Institutions

```
┌─────────────────────────────────────────────────────────────────┐
│  FOR ACADEMIC PROGRAMS                                          │
│                                                                 │
│  RESEARCH GAPS (tractable, high-impact):                        │
│                                                                 │
│  1. Multimodal deepfake detection vs. ProKYC attack chain       │
│     → Standard benchmarks don't test against $629/year tools    │
│     → IEEE S&P 2027 or USENIX Security 2027 scope               │
│                                                                 │
│  2. Election trust architecture post-CISA                       │
│     → Alternative federal-state coordination design             │
│     → CISA replacement requires institutional architecture, not │
│       just funding restoration                                   │
│                                                                 │
│  3. Palantir cross-agency interoperability + Carpenter doctrine │
│     → "Mega API" architecture vs. third-party doctrine          │
│     → Active circuit court litigation = timely legal scholarship│
│                                                                 │
│  ACADEMIC FREEDOM CONCERN:                                      │
│  NIH/DOJ/NASA grantees are data subjects in Palantir Foundry    │
│  IRS relationship mapping extends to organizational connections  │
│  IRB informed consent language needs updating for this reality  │
│                                                                 │
│  Full briefing: tier-2-threat-briefing-academic.md              │
└─────────────────────────────────────────────────────────────────┘
```

---

## Appendix B: Research Communities

```
┌─────────────────────────────────────────────────────────────────┐
│  FOR SECURITY RESEARCHERS                                       │
│                                                                 │
│  OPEN DATASETS:                                                 │
│  • FaceForensics++ / DFDC: deepfake detection benchmarks        │
│  • ASVspoof 2019/2021: voice anti-spoofing challenge data       │
│  • Twitter SIO: state-linked information operations datasets    │
│  • MIT Election Lab: precinct-level historical election data    │
│                                                                 │
│  FORENSIC ANALYSIS ENTRY POINTS:                               │
│  • Shai-Hulud npm signatures: install hooks + Bun runtime       │
│    + GitHub exfiltration via attacker-controlled repos          │
│  • BootKitty UEFI: CVE-2023-40238, MokList manipulation         │
│  • USASpending.gov: primary Palantir contract documentation     │
│                                                                 │
│  PUBLICATION ETHICS:                                            │
│  Capability documentation from public sources = defensible      │
│  Share findings with civil society orgs before publication      │
│  USENIX Security ethics section is the field's current standard │
│                                                                 │
│  UPCOMING DEADLINES:                                            │
│  ACM CCS 2026: May 14 / June 18 | IEEE S&P 2027: Nov–Dec 2026  │
│                                                                 │
│  Full briefing: tier-2-threat-briefing-researcher-community.md  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Appendix C: Journalists and Press Freedom Organizations

```
┌─────────────────────────────────────────────────────────────────┐
│  FOR JOURNALISTS                                                │
│                                                                 │
│  THE TRAINING GAP:                                              │
│  Standard opsec training covers transport layer (Signal, etc.)  │
│  It misses the pre-contact commercial data layer that feeds     │
│  ICE ELITE deportation targeting                                │
│  → Add: data broker opt-out to source protection training       │
│                                                                 │
│  INTERVIEW SECURITY 2026:                                       │
│  → Power off phones before arriving at interview location       │
│  → Remote: SecureDrop/OnionShare for docs ONLY before in-person │
│    identity verification                                        │
│  → Never verify identity by video call alone                    │
│                                                                 │
│  DEEPFAKES YOU WILL ENCOUNTER:                                  │
│  → You as the target (fabricated video/audio of you)            │
│    → Pre-establish legal counsel now, not during the crisis     │
│  → Your sources as the target (impersonation of a source)       │
│    → Code word protocol with high-value sources                 │
│  → Political candidates (the NRSC Talarico model)               │
│    → Primary source verification before forwarding              │
│                                                                 │
│  Full briefing: tier2-journalists-threat-briefing.md            │
└─────────────────────────────────────────────────────────────────┘
```

---

## Appendix D: Technical Advocates

```
┌─────────────────────────────────────────────────────────────────┐
│  FOR TECHNICAL ADVOCATES                                        │
│                                                                 │
│  DOCUMENTATION UPDATES NEEDED:                                  │
│  □ "Voice/video no longer proves identity" — add to all guides  │
│  □ Code word + two-channel verification — add to quick-starts   │
│  □ Password manager: "official installer only, never npm"       │
│  □ MFA hierarchy: FIDO2 > TOTP > SMS; remove voice biometrics   │
│  □ Data broker opt-out = source protection (add to journalist   │
│    security and immigrant rights tooling)                       │
│                                                                 │
│  TOOLCHAIN HARDENING (YOUR OWN):                               │
│  □ GitHub Actions → commit SHA pinning                          │
│  □ CI/CD → OIDC short-lived tokens                              │
│  □ SBOM generation at build time (syft / CycloneDX)            │
│  □ Socket.dev integration for PR-level supply chain risk        │
│                                                                 │
│  UEFI FIRMWARE (forward-looking, time-sensitive):              │
│  □ Apply manufacturer updates now                               │
│  □ fwcheck.binarly.io for hardware without active update program│
│  □ Add UEFI update track record to hardware procurement criteria│
│                                                                 │
│  Full briefing: tier2-technical-advocates-threat-briefing.md    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Appendix E: Digital Rights Organizations

```
┌─────────────────────────────────────────────────────────────────┐
│  FOR DIGITAL RIGHTS ORGANIZATIONS                               │
│                                                                 │
│  POLICY PRIORITY MATRIX (by achievability × impact):           │
│                                                                 │
│  HIGH achievability, HIGH impact:                               │
│  → FISA data broker loophole provision (S.4082)                 │
│    Bipartisan sponsors; severable from warrant debate           │
│    June 12 deadline — contact senators NOW                      │
│                                                                 │
│  MEDIUM achievability, HIGH impact:                             │
│  → IRS–ICE data sharing circuit court appeal                    │
│    A ruling for plaintiffs = immediate data pipeline halt       │
│    Amicus engagement available                                  │
│                                                                 │
│  HIGH impact, LONGER timeline:                                  │
│  → EI-ISAC restoration / election security funding              │
│  → Palantir USDA workforce surveillance accountability          │
│  → Maven program-of-record human rights policy challenge        │
│                                                                 │
│  COMMUNITY-SPECIFIC VULNERABILITY:                              │
│  Undocumented / refugees / trans: synthetic identity fraud is   │
│  specifically exploits their documentation gaps                  │
│  Add synthetic identity fraud awareness to client safety plans  │
│                                                                 │
│  Full briefing: tier-2-threat-briefing-digital-rights.md        │
└─────────────────────────────────────────────────────────────────┘
```

---

## How to Use This Deck

**Presentation format (20–30 min)**:
- Slides 1–5: Full audience, no sector customization required (15–20 min)
- Appendix A, B, C, D, or E: Add the appropriate sector slide at the end (5 min)
- Q&A focused on the 30-day action checklist (5–10 min)

**Self-study format**:
- Read slides 1–5 for the threat overview
- Follow the 30-day action checklist on Slide 4
- Read the full sector briefing linked at the bottom of the relevant Appendix slide

**Canva / Google Slides conversion**:
The content in each slide is structured for direct translation into a presentation tool. Each box represents one slide section. The headers are the slide headers; the bullet points are the body content. Suggested visual treatment: dark background (#1a1a2e or similar), monospace font for code/tool references, sector color-coding for appendix slides.

**Marp rendering** (if using markdown slide tools):
Prepend `---` to each slide separator and add `<!-- style: default -->` to the front matter. Marp will render the ASCII-box content in a readable format; replace boxes with native Marp table syntax for cleaner output.

---

*All claims in this deck are sourced to primary records: FOIA disclosures, government procurement contracts, federal court filings, and peer-reviewed or primary security research. 38 primary sources underpin the May 2026 advanced threat analysis. Full source list in `may-2026-advanced-threats.md`.*
