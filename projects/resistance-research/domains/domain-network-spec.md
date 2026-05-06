---
title: "Domain Network Visualization & Dependency Mapping — Design Specification"
created: "2026-05-06"
session: "General Research Agent"
status: "Production-ready spec — implementation-ready post-Phase-1-decision"
word_count: ~2200
purpose: "Specification for an interactive network visualization of the 35-domain framework; companion to domain-dependency-graph.json"
---

# Domain Network Visualization & Dependency Mapping — Design Specification

**Purpose**: This document specifies an interactive network visualization tool for the 35-domain Democratic Renewal framework. It covers visual design, cluster architecture, dependency sequencing, HTML prototype design, distribution integration, and usage measurement. The companion file `domain-dependency-graph.json` provides the machine-readable data layer this spec describes.

---

## Section 1: Network Design Overview

The network is a directed graph. Each node is a domain. Each edge encodes a relationship type between domains. The visualization serves one primary audience goal: help an institutional recipient — a law professor, a policy analyst, a Senate staffer — understand, in under three minutes, how these domains relate to each other and where to start reading.

### Node Specification

Every node carries four pieces of visible data:

- **Domain ID** — short label (e.g., "D1", "D37", "Civil-Service")
- **Short title** — four to six words (e.g., "Voting Rights & Elections")
- **Urgency indicator** — color ring: red (critical/2026 window), amber (medium), grey (research-only/longer-horizon)
- **Completion badge** — filled circle if production-ready; hollow if scope-document only

Node size should encode approximate word count as a proxy for research depth. The largest nodes (Domain 19f at 29,600 words, Domain 33 at ~9,200, Domain 29 at ~9,300) visually signal where the deepest evidence lives.

Node color fill encodes cluster membership (see Section 2). Urgency is shown by border color, not fill, so the two visual channels do not compete.

### Edge Specification

Three edge types, visually distinct:

| Edge type | Visual encoding | Meaning |
|---|---|---|
| **Prerequisite** | Solid arrow, weight 2 | Domain A must be understood before Domain B is actionable; reading order dependency |
| **Cross-reference** | Dashed line, weight 1 | The two domains reference each other's evidence; helpful but not required |
| **Structural link** | Dotted arrow, weight 1.5 | Domain B provides the enforcement mechanism, constitutional basis, or reform vehicle for Domain A |

Edge direction on prerequisite arrows points toward the dependent domain (reads: "read A before B"). Cross-reference edges are undirected. Structural links are directed toward the domain that depends on the other for implementation.

---

## Section 2: Domain Themes and Clusters

Seven clusters cover the full 35-domain scope. Each cluster is visually separated by fill color. Clusters are not hermetically sealed — many domains have strong cross-cluster connections — but they provide the primary navigation layer.

### Cluster A: Voting, Elections, and Democratic Participation (blue)
Core electoral infrastructure: how votes are cast, counted, and manipulated.
- Domain 1 (Electoral Reform / Voting Rights)
- Domain 3 (Democratic Participation)
- Domain 7 (Rights Protection and Civil Liberties — ballot/assembly rights)
- Domain 33 (State Legislative Autocratization — gerrymandering, ballot initiative suppression)
- Domain 37 (Federal Executive Interference in 2026 Midterms)
- Phase 3-6 (Democratic Participation & Election Security)

### Cluster B: Judiciary, SCOTUS, and Rule of Law (dark red)
Courts as democratic infrastructure: how law is interpreted and who controls interpretation.
- Domain 6 (Judicial Independence and Reform)
- Domain 35 (Supreme Court OT2026 / Post-Loper Landscape)
- Domain-Judicial-Independence-Recovery (structural recovery mechanisms)
- Domain 29 (Prosecutorial Weaponization and DOJ Capture)

### Cluster C: Executive Power, Civil Service, and Accountability (orange)
Executive branch: what the president can do unilaterally and who checks it.
- Domain 2 (Institutional Integrity / Civil Service)
- Domain 19f (War Powers Reform — Iran)
- Domain 28 (War Powers / Venezuela Military Unilateralism)
- Domain 26 (Government Accountability and Institutional Resilience)
- Domain 34 (Congressional Power-of-the-Purse Fiscal Authority)
- Domain-Civil-Service-Resilience
- Phase 3-8 (Civil Service Hiring Protections)
- Domain-Legislative-Branch-Capacity

### Cluster D: Surveillance, Privacy, and Information (purple)
The data layer of democracy: surveillance, AI, information access, and media.
- Domain 21 (Data Privacy and Digital Surveillance)
- Domain 25 (FISA Section 702 — April 2026 Outcome)
- Domain 36 (AI Governance and Algorithmic Accountability)
- Domain-Information-Access-Recovery (FOIA and transparency)
- Domain-Media-Freedom-Recovery (press independence)
- Phase 3-7 (Technology Governance and Digital Rights)

### Cluster E: Economic, Fiscal, and Financial Architecture (green)
Money as democratic infrastructure: taxation, trade, financial independence.
- Domain 4 (Digital Government Infrastructure)
- Domain 5 (Fiscal Reform)
- Domain 23 (Trade Policy and Tariff Unilateralism)
- Domain 34 (Congressional Power-of-the-Purse — also in Cluster C; dual-cluster)
- Domain 38 (Financial Sector Independence)
- Phase 3-5 (Finance and Fiscal Architecture)
- Domain 31 (Healthcare Access / Medicaid / OBBBA)
- Domain 31x (Healthcare-Tariff Collision)

### Cluster F: State-Level and Federalism (teal)
The states as the terrain where democratic erosion or resilience is won or lost.
- Domain 9 (Federalism and Local Democracy)
- Domain 33 (State Legislative Autocratization — also in Cluster A; dual-cluster)
- Domain 27 (Higher Education and Academic Freedom)
- Domain 37b (State Election Security Coordination — scope doc)
- Domain 37a (Post-Election Section 3 Litigation — scope doc)

### Cluster G: International, Security, and Foreign Interference (slate)
External threats and international legal frameworks.
- Domain 19 (National Security and Foreign Policy)
- Domain-Foreign-Interference-in-Democratic-Institutions
- Domain 37-Foreign-Transnational (Foreign/Transnational Interference)
- Domain 28 (also Cluster C, dual-cluster)

### Domains spanning multiple clusters

Domain 33, Domain 28, Domain 34, and Domain 6 each carry strong connections to two clusters. The visualization should allow a node to display membership in two clusters simultaneously — a half-and-half fill — rather than forcing an arbitrary single assignment. This dual-cluster visual representation accurately communicates that, for example, the judiciary cluster and the executive accountability cluster are not separable in practice.

---

## Section 3: Dependency Map

### Foundation Layer — Read First

Six domains form the foundation that all other reading depends on. Without these, the specific reform domains lack the structural context that explains why the proposed changes are necessary:

1. **Domain 1** (Electoral Reform) — establishes the electoral system failure that is the root mechanism
2. **Domain 2** (Institutional Integrity / Civil Service) — establishes how the executive undermines institutional checks
3. **Domain 6** (Judicial Independence) — establishes the judicial backstop failure
4. **Domain 34** (Congressional Power-of-the-Purse) — establishes the fiscal enforcement gap
5. **Domain 35** (SCOTUS / Post-Loper) — establishes the doctrinal landscape that constrains all litigation-based reform
6. **Domain 29** (DOJ Capture) — establishes that enforcement cannot be assumed even when law is clear

These six domains are the critical path. A recipient who reads only these six will understand the structural problem. Every other domain deepens one or more of these foundational diagnoses.

### Secondary Layer — Thematic Depth

After the foundation, reading follows cluster lines. Within each cluster, the natural sequencing is:

- **Voting cluster**: D1 → D33 → D37 → D37b (if election-focused reader) → D37a
- **Judiciary cluster**: D6 → D35 → D-Judicial-Independence-Recovery → D29
- **Executive cluster**: D2 → D26 → D19f → D28 → D34 → D-Civil-Service
- **Surveillance cluster**: D21 → D25 → D36 → D-Information-Access → D-Media-Freedom
- **Economic cluster**: D5 → D23 → D38 → D31 → D34 → Phase3-5
- **State cluster**: D9 → D33 → D27 → D37b

### Are There Circular Dependencies?

Yes, three genuine circular dependency clusters exist:

**Circle 1**: D6 (Judicial Independence) ↔ D29 (DOJ Capture). Judicial independence requires an independent DOJ to enforce court orders; DOJ capture enables judicial erosion. Neither is fully upstream of the other.

**Circle 2**: D34 (Congressional Power-of-the-Purse) ↔ D19f/D28 (War Powers). Congressional fiscal authority is the enforcement mechanism for war powers constraints; war powers violations deplete fiscal capacity and normalize executive fiscal unilateralism.

**Circle 3**: D1 (Electoral Reform) ↔ D33 (State Autocratization). Electoral system reform is blocked by gerrymandering; gerrymandering is an electoral reform problem. Both are prerequisites for the other's solution.

These circles should be visualized with bidirectional arrows of the "structural link" type, not the "prerequisite" type — they indicate interdependence, not sequential ordering. In the visualization, they should be highlighted rather than hidden; the circular dependencies are among the most important analytical findings in the framework.

### Critical Path for Institutional Recipients

For a recipient who has limited time (a staffer, a think-tank analyst with 90 minutes), the critical path is:
1. Domain 1 + Domain 2 (30 min each) — diagnosis
2. Domain 6 + Domain 35 (30 min each) — judicial landscape
3. Domain 37 (45 min) — immediate 2026 stakes
4. Implementation Roadmap domain (30 min) — sequencing

This six-domain, approximately 3.5-hour path communicates the core framework coherently. The visualization should allow a "quick read path" filter that highlights just these nodes and their edges.

---

## Section 4: Interactive HTML Prototype Design

### Technology Recommendation

The visualization should be a self-contained HTML file using the D3.js force-directed graph layout, with all dependencies bundled inline. Self-contained HTML has zero server requirements, can be attached to an email, opened from a Gist, or served from GitHub Pages without a build step. A recipient who saves the file to their desktop can use it offline. This is the correct technical choice for the distribution context.

Target file size: under 2 MB including bundled D3. This is achievable with minified D3 v7 (~250 KB) and the JSON graph data.

### Core Interaction Features

**Node click**: Opens a side panel with:
- Domain title, urgency indicator, word count
- Two-sentence summary of the domain's central finding
- Link to the full domain file (relative path or absolute GitHub/Gist URL)
- List of prerequisite domains (clickable, highlights those nodes)
- List of cross-reference domains (clickable)

**Filter controls** (top bar):
- By cluster (checkboxes, color-coded to match node fills)
- By urgency (critical 2026 / medium / research-only)
- By production status (production-ready / scope-doc)
- Quick-path button: "Show critical path" — highlights the 6-domain foundation layer

**Pan and zoom**: D3's built-in zoom behavior. Double-click resets to fit-to-window. The graph with 35+ nodes will not fit readably at initial scale; zoom is not optional.

**Edge toggle**: A control to hide cross-reference edges (showing only prerequisite/structural edges) reduces visual noise for first-time viewers. Show all edges by default; "simplified view" hides dashed edges.

**Search**: A text input that highlights nodes matching the typed string, dims all others, and displays matching domains in a side list.

### Layout Strategy

The force-directed layout should use:
- **Cluster gravity**: A weak attractive force pulling same-cluster nodes together (D3's `forceCluster` or a custom centering force per cluster centroid)
- **Foundation pinning**: The six foundation-layer domains are softly pinned to the center of the canvas. All other nodes float around them.
- **Minimum edge length**: Prerequisite edges enforce a minimum separation to prevent foundation domains from clustering too tightly.

Initial state should show all nodes with cluster coloring, no filters active, and a brief instruction overlay ("Click a node to explore. Drag to reposition. Scroll to zoom. Filter by theme in the top bar.") that dismisses on first click.

### Accessibility

- All colors must pass WCAG AA contrast on white background
- Cluster differentiation must not rely on color alone; use node shape (square vs. circle vs. diamond) as a secondary channel to encode urgency
- The side panel must be keyboard-navigable (Tab through node list, Enter to select)
- Alt text for the SVG container should describe the graph purpose

---

## Section 5: Phase 1 Distribution Integration

### Option A: GitHub Pages (Recommended for Institutional Outreach)

Create a GitHub Pages site at `[username].github.io/democratic-renewal/` with:
- `index.html` — the interactive visualization (standalone file)
- `domains/` — static copies of all production-ready domain `.md` files, rendered as HTML via Jekyll or a static generator
- A landing page with a one-paragraph description and "Start here" pointer to the critical path

**Advantages**: Persistent URL, no cost, version-controlled, can be updated as domains are added. The Gist distribution URLs are shareable but not navigable as a site. GitHub Pages provides the permanent home.

**Disadvantages**: Requires a public GitHub repository, which is a visibility decision. Given the project is currently private-local-only, this requires an explicit decision to publish.

### Option B: Embedded in Gist (Quick Deploy)

A single-file HTML visualization can be embedded in a GitHub Gist using the `bl.ocks.org` or `gistpreview.github.io` pattern. The Gist URL remains shareable. Distribution emails can link to `https://gistpreview.github.io/?[gist-id]`.

**Advantages**: Consistent with existing Gist-based distribution infrastructure. No new repository needed. Can be deployed in under 30 minutes once the HTML file is built.

**Disadvantages**: Gist previews are fragile (third-party rendering services). The visualization does not integrate with the domain files as a navigable site; links in the node side-panel would point to separate Gist URLs for each domain file.

### Option C: Companion to Email Distribution

A simpler static PNG or SVG export of the network graph can be embedded directly in the email distribution, with a link to the full interactive version. This gives recipients an immediate visual impression before clicking.

Tools for static export from D3: `d3-node` (Node.js server-side rendering) produces a static SVG. This serves recipients in email clients that block JavaScript and as a fallback for the HTML version.

### Recommended Sequence

1. Build the interactive HTML file (spec + JSON are now complete; HTML build is a ~4-hour task post-approval)
2. Export a static SVG/PNG for email attachment
3. Deploy HTML to GitHub Pages (parallel to Gist distribution; separate decision)
4. Include the static image in institutional outreach emails with the caption "Interactive version at [URL]"

---

## Section 6: Measurement and Usage

### What Success Looks Like

The network visualization is a comprehension tool, not a conversion tool. The right success metric is: "Did recipients who engaged with the visualization demonstrate deeper understanding of framework coherence than those who did not?" This is hard to measure directly, but proxies exist.

### Measurable Indicators

**GitHub Pages / Gist analytics** (if deployed):
- Unique page visits to the visualization URL
- Bounce rate (single-visit with no node clicks = did not engage)
- Time on page (under 30 seconds = did not engage; over 5 minutes = substantive engagement)
- Click-through rate to individual domain documents from the visualization

These metrics are available from GitHub Insights (Pages) and do not require a third-party analytics service.

**Institutional adoption signals**:
- Inbound links or embeds of the visualization from external sites (Google Search Console)
- References to specific domain numbers in email replies from contacts — recipients who reference "Domain 34" or "the prosecution cluster" have internalized the framework structure, which the visualization is designed to enable
- Requests for the underlying JSON data (indicates researchers or developers want to work with the graph programmatically)

**Distribution email A/B signal** (if the outreach infrastructure supports it):
- Email variant A: text-only with domain list
- Email variant B: includes static network image + link to interactive version
- Compare response rate, click-through on domain links, and depth of follow-up questions between variants

### Feedback Loop Integration

Add one question to the follow-up survey (if deployed via adoption-feedback-template.md):
> "Did you use the interactive domain map? (Yes / No / Didn't notice it)"
> "If yes: did it help you understand how the domains relate? (1-5 scale)"

This captures qualitative signal without requiring behavioral tracking infrastructure.

### Confidence Level on Measurement

Low-to-medium. The distribution infrastructure is currently email-first with no analytics layer. GitHub Pages provides basic analytics, but attributing comprehension improvement to the visualization specifically requires a controlled comparison that the current distribution plan does not support. The more realistic success signal is qualitative: do institutional contacts reference the visualization in follow-up communications, and do their follow-up questions demonstrate understanding of cross-domain structure rather than treating the domains as independent documents?

---

## Implementation Notes

**What this spec does not address**: The spec assumes the HTML prototype is built by a developer or by the orchestrator in a future session. It does not specify the exact D3 API calls, the CSS, or the bundling pipeline. Those decisions are implementation details that should follow the design decisions made here.

**Single-file constraint**: The "self-contained HTML" requirement is non-negotiable for the distribution context. All CSS, JavaScript, and JSON data must be inlined. No CDN dependencies, no external API calls, no server-side rendering.

**Data freshness**: The `domain-dependency-graph.json` companion file is the authoritative data source. The HTML should load the JSON data at build time (inlined as a JavaScript variable) so the visualization reflects the exact domain inventory at the time of distribution.

**Scope documents**: Domain-37a, Domain-37b, and Domain-31x are scope documents, not full research domains. The visualization should include them as nodes but style them distinctly (hollow node, lower opacity) to accurately represent their status to recipients.
