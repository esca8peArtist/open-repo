---
title: "Domain 38 Gist Creation Steps"
created: 2026-05-30
purpose: 10-step GitHub Gist creation procedure for Domain 38 (AI regulatory capture)
prerequisite: domain-38-ai-regulatory-capture-governance.md (production-ready)
distribution_date: June 11–14, 2026 (create Gist before June 15 Tier A send)
status: execution-ready
---

# Domain 38 Gist Creation Steps
## GitHub Gist — 10-Step Procedure for June 11–14 Pre-Production

*This procedure is identical in structure to the Domain 39 Gist creation template (DOMAIN_39_GIST_CREATION_TEMPLATE.md). Follow the same 10 steps in the same order. The content pasted into the Gist editor is the full text of domain-38-ai-regulatory-capture-governance.md.*

---

## Time Required and Prerequisites

**Time required**: 5–10 minutes  
**Prerequisites**: GitHub account logged in at github.com; domain-38-ai-regulatory-capture-governance.md open for copying

**Create Gist before**: June 14, 2026 (one day before first Tier A send on June 15)

---

## Step 1 — Navigate to Gist

Go to: https://gist.github.com

Confirm you are logged into your GitHub account. The page should show your username in the top right corner and a blank Gist creation form.

---

## Step 2 — Enter the Gist Description

In the **"Gist description..."** field at the top, enter exactly:

```
Domain 38: Regulatory Capture in AI Governance — How Industry Shapes the Rules That Were Supposed to Govern It
```

This description appears in the Gist header and in any external citations. Keep it exactly as written — it matches the source document title.

---

## Step 3 — Enter the Filename

In the **filename field** (the field that shows "Filename including extension..." in grey placeholder text), enter exactly:

```
domain-38-ai-regulatory-capture-governance.md
```

The `.md` extension is essential — GitHub Gist will render the file as formatted Markdown (headings, bold, links) rather than plain text. Without it, the document displays as unformatted text.

---

## Step 4 — Paste the Full Document Text

Open `/home/awank/dev/SuperClaude_Framework/projects/resistance-research/domain-38-ai-regulatory-capture-governance.md` and copy the entire contents of that file.

Paste the copied text into the **large text editor area** below the filename field.

Do not add any wrapper text, header, or footer — paste only the raw document contents. The Gist editor will render the Markdown.

**Document structure to verify after pasting (scroll through the editor):**

- [ ] YAML frontmatter block is at the top (starts with `---`)
- [ ] "Leading Finding" section is visible (the xAI/Colorado case opening)
- [ ] Section 1 header: "The Statutory Vacuum"
- [ ] Section 2 header: "The Four Capture Mechanisms"
- [ ] Section 3 header present (revolving door and ownership stake)
- [ ] Section 4 header present (preemption EO and state law dismantlement)
- [ ] Section 5 header present (reform architecture)
- [ ] Sources section visible at end (43 citations)
- [ ] No visible truncation at the bottom of the editor

---

## Step 5 — Set Visibility

**Recommended setting: Secret Gist**

On the bottom-right of the Gist creation form, there is a dropdown button. Set it to **"Create secret gist"**.

- Secret: Anyone with the URL can view the document, but it does not appear in GitHub's public Gist search or on your profile's public Gist list. Appropriate for targeted professional distribution.
- Public: Appears in search and is visible on your profile. Use if you want broad organic discovery in addition to direct distribution.

For Domain 38 distribution to AI governance policy professionals (Tier A contacts), Secret is appropriate. The Tier C/D social distribution can reference the Gist URL regardless of which setting you choose — Secret Gists are fully accessible to anyone with the link.

---

## Step 6 — Create the Gist

Click the **"Create secret gist"** button (or "Create public gist" if you chose Public in Step 5).

GitHub will create the Gist and redirect you to a URL that looks like:

```
https://gist.github.com/[your-username]/[32-character-hash]
```

Example format: `https://gist.github.com/esca8peArtist/a1b2c3d4e5f6...`

Copy this URL immediately.

---

## Step 7 — Record the Gist URL

Paste the Gist URL in the placeholder below:

```
DOMAIN 38 GIST URL: _______________________________________________
```

Record this URL in:
- The email templates in DOMAIN_38_CONTACT_STRATIFICATION.md (replace "[Gist URL — insert before send]" in each email)
- DISTRIBUTION_EXECUTION_LOG.md (Domain 38 section)
- PROJECTS.md (update Domain 38 distribution status)

---

## Step 8 — Test the Gist (Post-Creation Checklist)

Open the Gist URL in a **private/incognito browser window** to verify it is accessible without authentication.

Complete the following verification checks:

- [ ] URL opens without requiring GitHub login
- [ ] Document renders as **formatted Markdown** — headings display as larger bold text, not as `#` symbols
- [ ] YAML frontmatter block at the top renders cleanly (as a table or fenced block — either is correct)
- [ ] The **"Leading Finding"** section header is clearly visible near the top
- [ ] The **xAI/Colorado case** text is present in the Leading Finding section
- [ ] **Section 2.1 "The Revolving Door"** header is visible and linked or bold
- [ ] The **EU AI Act August 2 deadline** text appears in the document
- [ ] The **Sources section** (43 citations) is present at the bottom
- [ ] All source URLs are clickable blue links (not plain text)
- [ ] Scroll from top to bottom without any visible truncation or missing sections
- [ ] Copy the raw URL from the incognito window address bar and confirm it matches the URL you recorded in Step 7

If all checklist items pass: the Gist is ready for distribution.

If any item fails: see troubleshooting in Step 10 below.

---

## Step 9 — Pre-Fill Email Templates

Before the June 15 Tier A send, insert the Gist URL into all five planned email templates.

**Search in email drafts for**: `[Gist URL — insert before send]`  
**Replace with**: The URL from Step 7

This should be done on June 14 (one day before send) or the morning of June 15 before beginning the send sequence.

**Email templates requiring Gist URL insertion**:
- Georgetown Law ITLP template (if using personalized email)
- EFF template
- CDT template
- AI Now template
- Public Knowledge template

For organizations contacted via web form rather than email (AI Now, Harvard Berkman Klein), paste the Gist URL directly into the web form message body.

---

## Step 10 — Troubleshooting

**Problem**: Gist shows as plain text (no formatting)  
**Solution**: Verify the filename ends in `.md`. Edit the Gist (pencil icon), correct the filename, and save. GitHub Gist re-renders automatically.

**Problem**: Gist text appears truncated  
**Solution**: Edit the Gist, scroll to the bottom of the editor, and verify the full Sources section (43 citations) is present. If not, the paste was incomplete — paste again from the source document.

**Problem**: URL requires login to access  
**Solution**: Verify the Gist was created as "Secret" or "Public" (not "Private to you" — GitHub Gists do not have a private-to-owner setting; all Gists are either secret or public). Secret Gists are accessible without authentication to anyone with the URL.

**Problem**: Source URL links are not clickable in rendered view  
**Solution**: This is a rendering environment issue — all Markdown `[text](url)` links render as clickable links in GitHub Gist. If links are not rendering, the Gist filename may not have the `.md` extension. Correct per above.

**Problem**: Gist creation account has a different username than the Domain 39 Gist  
**Solution**: This is not a problem — Gist URLs are unique regardless of username. Record the new URL and proceed. The two Gists do not need to be on the same account.

---

## Domain 38 Gist Content Structure

The following sections must be present in the Gist (in this order). Use this as a verification checklist while scrolling through the rendered document:

**Zone A — Urgency and Context**
- YAML frontmatter (title, hard_deadline: August 2, 2026, distribution_target: July 15, primary_audiences)
- Leading Finding (xAI/Colorado case, EU AI Act August 2 deadline statement)
- Section 1: The Statutory Vacuum (1.1 What Doesn't Exist; 1.2 Dismantling of Biden's Architecture; 1.3 Post-Loper Fragility)

**Zone B — Analysis and Mechanisms**
- Section 2: The Four Capture Mechanisms (2.1 Revolving Door; 2.2 Standards Body Capture; 2.3 Preemption Executive Order; 2.4 [fourth mechanism])
- Section 3: The Colorado Case Study (or equivalent case study section)
- Section 4: EU-US Regulatory Arbitrage (Article 50 enforcement; DSA comparison)

**Zone C — Reform and Action**
- Section 5: Reform Architecture (statutory authority; independent enforcement; capture-resistant standards)
- Movement leverage points for recipients
- Sources (43 citations in numbered format)

If any Zone A, B, or C section is missing from the rendered Gist, re-paste from the source document before distributing.

---

## Quick Reference: Domain 38 vs. Domain 39 Gist Comparison

| Element | Domain 39 Gist | Domain 38 Gist |
|---------|---------------|----------------|
| Source file | domain-39-healthcare-access-democratic-infrastructure.md | domain-38-ai-regulatory-capture-governance.md |
| Gist description | "Domain 39: Healthcare Access as Democratic Infrastructure..." | "Domain 38: Regulatory Capture in AI Governance..." |
| Gist filename | domain-39-healthcare-access-democratic-infrastructure.md | domain-38-ai-regulatory-capture-governance.md |
| Hard deadline in document | June 1, 2026 (HHS rule) | August 2, 2026 (EU AI Act) |
| Citation count | 47 | 43 |
| Create before | May 29, 2026 | June 14, 2026 |
| Gist URL recorded in | DISTRIBUTION_EXECUTION_LOG.md (Domain 39 section) | DISTRIBUTION_EXECUTION_LOG.md (Domain 38 section) |

The 10-step procedure is identical. Only the content and metadata differ.

---

## Post-Gist Creation Action Log

After creating the Gist and completing Steps 7–9, record the following in DISTRIBUTION_EXECUTION_LOG.md:

```
Domain 38 Gist created: [DATE]
Gist URL: [URL]
Gist visibility: [Secret / Public]
Checklist passed: [Yes / No — list any failures]
Email templates pre-filled: [Yes / No]
Ready for June 15 Tier A send: [Yes / No]
```

---

*Procedure created May 30, 2026. Follows exact structure of DOMAIN_39_GIST_CREATION_TEMPLATE.md. Source document domain-38-ai-regulatory-capture-governance.md is production-ready (status: production-ready, 43 citations, ~6,800 words).*
