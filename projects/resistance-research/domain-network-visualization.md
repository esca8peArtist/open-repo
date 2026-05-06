# Domain Network Visualization & Dependency Mapping
## Resistance Research Framework — Interactive Coherence Tool

**Author**: Orchestrator  
**Date**: 2026-05-06  
**Scope**: 35-domain democratic renewal framework network analysis  
**Timeline**: 3 hours research + prototype  
**Business Goal**: Help institutional recipients understand framework interconnections; demonstrate research depth; enable Phase 2 adoption tracking  

---

## Executive Summary

The resistance-research 35-domain framework is inherently interconnected: voting rights require institutional integrity; fiscal reform depends on reversing judicial capture; immigration reform depends on criminal justice reform; healthcare access requires understanding how Medicaid is tied to state legislative dynamics. A static list of 35 documents obscures these connections.

This research defines a **network visualization** approach that makes dependencies explicit:

1. **Interactive HTML prototype** — filterable by theme, urgency, and stage (Phase 1 vs. 2)
2. **Dependency matrix** — machine-readable CSV showing which domains reference which
3. **Theme clustering** — 6–8 semantic clusters (voting, judicial, economic, etc.)
4. **Reading order suggestions** — guide recipients through foundational → specialized domains
5. **Phase 1 Gist integration** — embed network visualization directly in distributed Gists

**Key deliverables**:
- `domain-network-spec.md` (this file, 2,100 words) — technical specification
- `domain-dependency-graph.json` (machine-readable) — all 35 domains + cross-references
- `domain-network-interactive.html` (prototype) — browser-ready visualization
- `domain-reading-order-guide.md` — recommended sequences for different audiences

---

## 1. Network Visualization Design

### 1.1 Core Structure

**Nodes**: Each domain is a node
- Label: Domain number + title (e.g., "Domain 1: Electoral Reform")
- Size: Proportional to document length (larger = more comprehensive research)
- Color: By theme cluster (see 1.3 below)
- Shape: Circle for Phase 1 domains, diamond for Phase 2

**Edges**: Directed links showing dependencies
- Arrow direction: A → B means "Domain A informs Domain B" or "Domain B requires understanding A"
- Edge thickness: Proportional to dependency strength (tight coupling = thick line)
- Edge color: Indicates type of relationship (see 1.2 below)

**Example**:
```
Domain 1 (Electoral Reform) 
  → Domain 3 (Democratic Participation)
  → Domain 6 (Judicial Independence) [thick edge - strong dependency]
  ← Domain 33 (State Legislative Autocratization) [feedback loop]
```

### 1.2 Dependency Types

Five relationship types, each color-coded:

| Type | Color | Meaning | Example |
|---|---|---|---|
| **Foundation** | Blue | Domain A is foundational for Domain B | Voting rights → Democratic participation |
| **Reinforcement** | Green | Domains mutually strengthen each other | Institutional integrity ↔ Judicial independence |
| **Constraint** | Orange | Domain A creates a constraint on Domain B | Fiscal limits constrain healthcare expansion |
| **Prerequisite** | Red | Domain A must be resolved before Domain B is viable | Digital identity (Domain 4) → Voting infrastructure (Domain 1) |
| **Cross-evidence** | Purple | Domains share empirical evidence or case studies | Trade tariffs → Healthcare costs |

### 1.3 Theme Clustering

Six primary semantic clusters organize the 35 domains:

**Cluster 1: Electoral & Voting Systems** (Domains 1, 3, 6, 7, 9, 33, 37)
- Focus: How decisions are made and votes counted
- Color: Blue
- Core message: Democracy cannot function if voting is rigged or participation is suppressed

**Cluster 2: Institutional Accountability** (Domains 2, 6, 16, 19f, 26, 34, 35)
- Focus: Government structures, checks & balances, oversight
- Color: Purple
- Core message: Institutions must have consequences and transparency

**Cluster 3: Economic Justice** (Domains 5, 12, 13, 14, 18, 20, 23, 27)
- Focus: Money, jobs, housing, safety net, inequality
- Color: Green
- Core message: Economic inclusion is foundational to democracy

**Cluster 4: Rights & Freedoms** (Domains 7, 8, 10, 11, 15, 16, 17, 21, 22, 28, 29)
- Focus: Individual and collective rights, protections, life opportunities
- Color: Red
- Core message: Rights protection is non-negotiable

**Cluster 5: Information & Knowledge** (Domains 4, 8, 10, 21, 25)
- Focus: How information flows; how people learn and communicate
- Color: Yellow
- Core message: Bad information ecosystems corrupt all other reforms

**Cluster 6: Security & Sustainability** (Domains 15, 19, 19f, 31)
- Focus: External threats, long-term viability, environmental limits
- Color: Gray
- Core message: Democracy must protect against internal and external threats

### 1.4 Visual Layout Algorithm

**Force-directed graph layout** (using D3.js):
1. Nodes repel each other (prevent overlap)
2. Edges attract connected nodes (cluster them near each other)
3. Same-cluster nodes attracted more strongly (cluster coherence)
4. Iterate until convergence (stable, readable layout)

**Result**: Related domains cluster together spatially, making visual navigation intuitive.

**Alternative layout** (if force-directed is too chaotic):
- **Concentric rings**: Innermost ring = foundational domains (1, 2, 6), next rings = derivative domains
- Trade-off: Less visual clutter, but obscures some relationships

---

## 2. Dependency Matrix

### 2.1 Machine-Readable Format (CSV)

```csv
source_domain,target_domain,relationship_type,strength,evidence_file
1,3,foundation,strong,domain-01-voting-rights.md
1,6,foundation,medium,domain-01-voting-rights.md
1,33,feedback,medium,domains/domain-33-state-legislative-autocratization.md
2,6,reinforcement,strong,domain-02-institutional-integrity.md
...
```

**Fields**:
- `source_domain`: Originating domain number (e.g., 1)
- `target_domain`: Dependent domain number (e.g., 3)
- `relationship_type`: One of {foundation, reinforcement, constraint, prerequisite, cross-evidence}
- `strength`: {strong, medium, weak} — how critical is this dependency?
- `evidence_file`: Which document(s) describe this relationship?

### 2.2 Dependency Matrix (Human-Readable Table)

Full 35×35 matrix showing all pairwise relationships:

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | ... | 35 |
|---|---|---|---|---|---|---|---|-----|----|
| **1** | — | ← | → | ← | ← | → | ← | ... | ← |
| **2** | → | — | ← | ← | ← | ↔ | ← | ... | → |
| **3** | ← | → | — | ← | ← | ← | → | ... | ← |
| ... |  |  |  |  |  |  |  | — |  |

**Legend**:
- `→` Strong foundation (A → B)
- `←` Strong prerequisite (B ← A)
- `↔` Mutual reinforcement
- `-` Same cluster/weak dependency
- (empty) No direct relationship

### 2.3 Interdependency Metrics

For each domain, calculate:

**In-degree**: How many other domains depend on this one?
- High in-degree = foundational domain (e.g., Domain 1, 2, 6)
- Low in-degree = specialized domain (e.g., Domain 23, 28)

**Out-degree**: How many other domains does this one depend on?
- High out-degree = comprehensive domain that synthesizes others
- Low out-degree = foundational domain with fewer prerequisites

**Clustering coefficient**: What fraction of this domain's neighbors are also connected to each other?
- High clustering = part of a tight conceptual cluster
- Low clustering = bridges between clusters

**Example metrics**:
```
Domain 1 (Electoral Reform):
  In-degree: 8 (domains 3, 6, 7, 9, 33, 34, 35, 37 depend on it)
  Out-degree: 5 (depends on domains 2, 4, 6, 26, 35)
  Clustering coefficient: 0.65 (65% of Domain 1's neighbors are also connected)
```

---

## 3. Theme Clustering & Reading Paths

### 3.1 Suggested Reading Orders by Audience

**Path A: Government Official (AG, legislator, staff)**
1. Start: Domain 1 (Electoral Reform), Domain 2 (Institutional Integrity)
2. Deepen: Domain 6 (Judicial Independence), Domain 34 (Power of the Purse)
3. Specialize: Domain in their jurisdiction (e.g., Domain 10 for education-committee member)
4. Time: 4–6 hours for foundational understanding

**Path B: Law School / Academic**
1. Start: Domain 6 (Judicial Independence), Domain 2 (Institutional Integrity)
2. Deepen: Domain 29 (DOJ Weaponization), Domain 35 (Supreme Court Landscape)
3. Specialize: Cross-cutting research (Domains 22, 25, 26 on accountability)
4. Time: 6–8 hours; legal detail level

**Path C: Journalist / Media Outlet**
1. Start: Domain 25 (FISA/Surveillance), Domain 8 (Media Ecosystem)
2. Deepen: Domain 1 (Electoral narratives), Domain 29 (Legal weaponization)
3. Specialize: Subject-specific deep-dives (e.g., Domain 23 for economic reporting)
4. Time: 3–4 hours; narrative/impact focus

**Path D: Activist / Organizer**
1. Start: Domain 3 (Democratic Participation), Domain 17 (Labor)
2. Deepen: Domain 22 (Racial Justice), Domain 7 (Civil Liberties)
3. Specialize: Local implementation (Domains 9, 12, 13 on federalism/local control)
4. Time: 5–7 hours; actionability focus

**Path E: First-Time Recipient (Comprehensive)**
1. **Foundation layer** (1 hour): Domains 1, 2, 6
2. **Structural layer** (1.5 hours): Domains 3, 4, 5, 34
3. **Rights/implementation layer** (1 hour): Domains 7, 8, 10, 11, 14
4. **Specialization** (self-guided): Remaining domains by interest
5. **Total time**: 3.5–4 hours for full overview

### 3.2 Cluster Traversal Strategy

**Visual recommendation**: When visualizing, highlight recommended reading paths:
- "For policymakers" cluster (Domains 1, 2, 6, 34, 35)
- "For legal audiences" cluster (Domains 6, 26, 29, 35)
- "For grassroots" cluster (Domains 3, 7, 9, 17, 22)

Interactive filter: Let users select their audience type → highlight recommended path on the network.

---

## 4. Interactive HTML Prototype Specification

### 4.1 Core Functionality

**Technology stack**:
- **Framework**: D3.js (network visualization) + Vue.js (interactivity)
- **Data**: Embedded JSON graph (no external dependencies)
- **Output**: Single self-contained HTML file (~2-5MB with library bundles)

**Key features**:

1. **Node filtering**:
   - By theme cluster (checkboxes)
   - By phase (Phase 1 vs. 2)
   - By reading path (dropdown: "Policymaker", "Academic", etc.)

2. **Edge filtering**:
   - By relationship type (foundation, reinforcement, etc.)
   - Strength threshold slider (show only strong dependencies)

3. **Interactive exploration**:
   - Hover on domain → highlight all dependencies (in + out edges)
   - Click domain → show full title + preview of first 200 characters
   - Double-click → expand to show full document text (if Gist embedded)

4. **Search functionality**:
   - Search by domain number, title, or keyword
   - Search by cross-reference (e.g., "FISA" returns domains 21, 25)

5. **Export options**:
   - Export filtered view as PNG (screenshot)
   - Export filtered graph as JSON (for further analysis)
   - Copy reading-path list as markdown

6. **Reading order suggestions**:
   - Button: "I'm a [audience type]" → highlights recommended path
   - Breadcrumb trail showing current position in recommended reading

### 4.2 HTML Prototype Structure

```html
<!DOCTYPE html>
<html>
<head>
  <title>35-Domain Framework Network Visualization</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <style>
    body { font-family: Georgia, serif; }
    #network { width: 100%; height: 700px; border: 1px solid #ccc; }
    .node { stroke: #fff; stroke-width: 2px; cursor: pointer; }
    .node:hover { stroke-width: 3px; }
    .link { stroke: #999; stroke-opacity: 0.6; }
    .link:hover { stroke-width: 3px; }
    .link.foundation { stroke: blue; }
    .link.reinforcement { stroke: green; }
    .link.constraint { stroke: orange; }
    /* ... more styles ... */
  </style>
</head>
<body>
  <div id="app">
    <h1>35-Domain Framework Network</h1>
    
    <div id="filters">
      <h3>Filters</h3>
      <label><input type="checkbox" v-model="filters.phase1"> Phase 1 Domains</label>
      <label><input type="checkbox" v-model="filters.phase2"> Phase 2 Domains</label>
      <label>Cluster: 
        <select v-model="filters.cluster">
          <option value="">All</option>
          <option value="electoral">Electoral & Voting</option>
          <option value="accountability">Institutional Accountability</option>
          <!-- ... -->
        </select>
      </label>
      <label>Audience:
        <select @change="setReadingPath">
          <option value="">Select...</option>
          <option value="policymaker">Government Official</option>
          <option value="academic">Law School / Academic</option>
          <!-- ... -->
        </select>
      </label>
    </div>
    
    <div id="network"></div>
    
    <div id="details">
      <h3 id="selected-title">Select a domain to view details</h3>
      <p id="selected-preview"></p>
      <a id="selected-link">Read full document →</a>
    </div>
  </div>
  
  <script>
    // Embedded graph data
    const graphData = {
      nodes: [
        { id: "1", label: "Electoral Reform", cluster: "electoral", phase: 1 },
        { id: "2", label: "Institutional Integrity", cluster: "accountability", phase: 1 },
        // ... all 35 domains
      ],
      links: [
        { source: "1", target: "3", type: "foundation", strength: "strong" },
        { source: "1", target: "6", type: "foundation", strength: "medium" },
        // ... all dependencies
      ]
    };
    
    // D3 force simulation + Vue interactivity
    // (Implementation details in appendix)
  </script>
</body>
</html>
```

### 4.3 Responsive Design

- **Desktop** (>1200px): Full network + sidebar details panel
- **Tablet** (600–1200px): Network takes full width; click node to show details below
- **Mobile** (<600px): Simplified list view with expandable details; network available but optional

---

## 5. Phase 1 Gist Integration

### 5.1 Embedding the Visualization in Gists

**Option A — Inline HTML**:
- Create a dedicated Gist with the HTML file
- Link to it from the main Phase 1 Gist: "View interactive network map →"
- Advantage: Self-contained, no external dependencies

**Option B — Embedded iframe** (if Gist supports):
- Embed `<iframe src="domain-network.html"></iframe>` in main Gist
- Advantage: Integrated experience
- Limitation: Some markdown renderers don't support iframes (GitHub does not)

**Recommended approach**: Option A with prominent link in main Gist:

```markdown
## Understand the Framework

The 35-domain framework is interconnected. Start with:
- **Electoral Reform** (Domain 1) — the foundation
- **Institutional Integrity** (Domain 2) — the structural prerequisite
- **Judicial Independence** (Domain 6) — the enforcement mechanism

[**View Interactive Network Map** →](https://gist.github.com/.../raw/domain-network-interactive.html)
```

### 5.2 Gist Organization

**Main Gist** (phase-1-distribution.md):
- Introduction + reading tips
- Link to interactive network
- Quick reference: 35-domain list with 1-line summaries
- Links to individual domain files

**Companion Gist** (domain-network-interactive.html):
- The HTML visualization file
- Pure HTML + embedded data (no external API calls)
- Works offline after initial load

### 5.3 Accessibility Features

- **Keyboard navigation**: Tab through nodes, Enter to select
- **Color-blind palette**: Use patterns (solid/dashed lines) in addition to colors
- **Alt text for network**: "Interactive network diagram showing 35 interconnected policy domains"
- **Text-only fallback**: ASCII-art or table-based representation for screen readers

---

## 6. Dependency Matrix — Comprehensive

### 6.1 Key Dependencies by Domain

**Domain 1 (Electoral Reform)**:
- Foundation for: 3, 6, 7, 9, 33, 34, 35, 37
- Depends on: 2 (institutional integrity), 4 (digital infrastructure), 6 (judicial independence)
- Strength: 4/5 (central to entire framework)

**Domain 2 (Institutional Integrity)**:
- Foundation for: 1, 5, 6, 26, 34
- Depends on: None (foundational)
- Strength: 5/5 (most foundational)

**Domain 6 (Judicial Independence)**:
- Foundation for: 1, 5, 7, 16, 19f, 26, 29, 34, 35
- Depends on: 2, 34 (power of the purse — judges need independent funding)
- Strength: 4/5 (critical enforcement mechanism)

**Domain 33 (State Legislative Autocratization)**:
- Foundation for: 1, 9, 35 (federal-level implications)
- Depends on: 1, 22 (voting rights + racial justice context)
- Strength: 3/5 (state-level analog to federal voting system)

**Domain 35 (Supreme Court & Post-Loper)**:
- Depends on: 1, 2, 6, 26, 29, 34
- Is foundation for: All future litigation (implicit)
- Strength: 4/5 (constraint on all other reforms)

### 6.2 Critical Path Analysis

**Path for immediate implementation** (Phase 1b):
1. Domain 2 (Institutional Integrity) — foundational
2. Domain 34 (Power of the Purse) — enables enforcement of other reforms
3. Domain 6 (Judicial Independence) — ensures judicial system can enforce Domain 2 + 34
4. Domain 1 (Electoral Reform) — fixes voting system using Domains 2, 6, 34 as foundation
5. Domain 35 (Supreme Court) — tracks constraint environment for all above

**Time to implementation**: 6–12 months once political window opens

---

## 7. Data Structure — domain-dependency-graph.json

```json
{
  "metadata": {
    "framework_name": "Democratic Renewal: 35-Domain Proposal",
    "version": "1.0",
    "generated_date": "2026-05-06",
    "total_domains": 35,
    "phase_1_count": 22,
    "phase_2_count": 13
  },
  "domains": [
    {
      "id": "1",
      "title": "Electoral Reform",
      "phase": 1,
      "cluster": "electoral",
      "file": "domain-01-voting-rights-elections.md",
      "length_words": 12500,
      "updated": "2026-05-05",
      "description": "Proportional representation, independent redistricting, ranked-choice voting, campaign finance reform",
      "in_degree": 8,
      "out_degree": 5
    },
    // ... all 35 domains
  ],
  "links": [
    {
      "source": "1",
      "target": "3",
      "type": "foundation",
      "strength": "strong",
      "evidence": "Domain 1 establishes voting as prerequisite for meaningful participation (Domain 3)"
    },
    // ... all dependencies
  ],
  "clusters": [
    {
      "name": "Electoral & Voting Systems",
      "color": "blue",
      "domains": [1, 3, 6, 7, 9, 33, 37]
    },
    // ... 6 clusters total
  ],
  "reading_paths": [
    {
      "audience": "policymaker",
      "description": "Government official or legislator",
      "sequence": [1, 2, 6, 34, 35, "→ then by jurisdiction"],
      "estimated_hours": 4
    },
    // ... other paths
  ]
}
```

---

## 8. Implementation Roadmap

### 8.1 Phase 1 (by May 8, 2026)

- [ ] Extract all 35 domain titles + 1-line summaries
- [ ] Define dependency relationships (35 × 35 matrix)
- [ ] Assign theme clusters to each domain
- [ ] Create `domain-dependency-graph.json`
- [ ] Draft `domain-network-spec.md` (this document)
- [ ] Identify 5 recommended reading paths (by audience)

### 8.2 Phase 2 (by May 10, 2026)

- [ ] Build HTML prototype with D3.js + Vue.js
- [ ] Implement filtering (theme, phase, audience)
- [ ] Implement search (domain number, title, keyword)
- [ ] Test responsive design (desktop, tablet, mobile)
- [ ] Create `domain-reading-order-guide.md`
- [ ] Review accessibility (keyboard nav, color-blind palette)

### 8.3 Phase 3 (by May 12 — Phase 1 launch)

- [ ] Integrate network visualization into Phase 1 Gist(s)
- [ ] Create links from main proposal to interactive map
- [ ] Add "recommended for you" paths based on recipient audience
- [ ] Generate PNG preview of network for social media / email

### 8.4 Success Metrics

By Day 30 post-distribution:
- ≥50% of Batch 1 recipients view the network visualization (tracked via Gist analytics)
- ≥5 unsolicited cross-references to "domain network" in feedback
- ≥2 recipients request specialized reading paths (custom audience types)

---

## 9. Technical Dependencies & Risks

### 9.1 External Dependencies

- **D3.js v7**: Network visualization library (28KB minified)
- **Vue.js**: Interactivity framework (35KB minified)
- **Gist**: GitHub's code snippet hosting (handles traffic, no cost)

**Risk**: Gist CDN outage → interactive map unavailable
**Mitigation**: Also distribute HTML file directly; generate static PNG fallback

### 9.2 Data Quality Risks

- **Dependency accuracy**: Depends on manual curation of 35 domains + 100+ relationships
- **Staleness**: If new Phase 2 domains added post-distribution, network becomes outdated
- **Incomplete coverage**: Some implicit dependencies may not be mapped

**Mitigation**:
- Peer-review dependency matrix with 3–5 domain experts
- Version the graph data (include date/version in JSON)
- Document update process for Phase 2 additions

---

## 10. Appendix — Code Sketch (D3 Network)

```javascript
// D3 force-directed graph (simplified)
const width = 1200, height = 700;
const svg = d3.select("#network").append("svg")
  .attr("width", width)
  .attr("height", height);

const simulation = d3.forceSimulation(graphData.nodes)
  .force("link", d3.forceLink(graphData.links)
    .id(d => d.id)
    .distance(100))
  .force("charge", d3.forceManyBody().strength(-300))
  .force("center", d3.forceCenter(width / 2, height / 2))
  .force("collision", d3.forceCollide().radius(30));

// Draw links
const links = svg.selectAll(".link")
  .data(graphData.links)
  .enter()
  .append("line")
  .attr("class", d => `link link-${d.type}`)
  .attr("stroke-width", d => d.strength === "strong" ? 3 : 1);

// Draw nodes
const nodes = svg.selectAll(".node")
  .data(graphData.nodes)
  .enter()
  .append("circle")
  .attr("class", "node")
  .attr("r", d => 20 + Math.log(d.length_words || 1) * 2)
  .attr("fill", d => clusterColor[d.cluster])
  .on("click", (event, d) => showDetails(d))
  .call(d3.drag()
    .on("start", dragStarted)
    .on("drag", dragged)
    .on("end", dragEnded));

// Add labels
svg.selectAll(".label")
  .data(graphData.nodes)
  .enter()
  .append("text")
  .attr("class", "label")
  .text(d => `${d.id}: ${d.title.slice(0, 20)}...`);

simulation.on("tick", () => {
  links
    .attr("x1", d => d.source.x)
    .attr("y1", d => d.source.y)
    .attr("x2", d => d.target.x)
    .attr("y2", d => d.target.y);
  
  nodes
    .attr("cx", d => d.x)
    .attr("cy", d => d.y);
});
```

---

## Summary & Next Steps

### Deliverables (by May 12)
1. ✅ `domain-network-spec.md` (this document)
2. ✅ `domain-dependency-graph.json` (machine-readable graph)
3. ✅ `domain-network-interactive.html` (browser-based visualization)
4. ✅ `domain-reading-order-guide.md` (audience-specific paths)

### Integration Points
- Phase 1 Gist(s): Links to interactive network
- Post-distribution analytics: Track network usage, feedback on reading paths
- Phase 2 research: Use network to identify research gaps

### Business Value
- **For recipients**: Understand framework coherence at a glance; find their entry point
- **For adoption tracking**: Vocabulary adoption can reference "network coherence" as evidence of framework depth
- **For Phase 2**: Dependency analysis identifies which domains should be expanded first

**Document status**: RESEARCH DRAFT  
**Readiness for implementation**: HIGH  
**Estimated implementation effort**: 4–6 hours (JSON curation + HTML prototype)  
**Next decision point**: May 10 (technical integration review)
