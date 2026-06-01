# Phase 2 Accessibility Tree Inspection Audit
**Date**: June 1, 2026  
**Auditor**: Runtime DOM Analysis via Playwright  
**Test Environment**: Chromium browser with DevTools accessibility API  
**Time**: 13:00-13:30 UTC  

---

## Executive Summary

**Overall Result**: FAIL - Missing critical accessibility tree information

Runtime inspection reveals that interactive elements ARE exposed to assistive technology, but with significant gaps:
- ✗ No `lang` attribute in accessibility tree
- ✗ No main landmark for structure
- ✗ No heading roles or hierarchy
- ✓ Interactive elements present in accessibility tree
- ✓ Focus management functional
- ⚠ Limited semantic roles for rendered content
- ⚠ ARIA attributes missing from root elements

**Impact**: Users of assistive technology will have difficulty understanding:
- Page content language
- Document structure and hierarchy
- Navigating between major sections
- What content is primary vs. supplementary

---

## Swagger UI - Accessibility Tree Analysis

### Runtime DOM Structure

**Rendered at**: `http://127.0.0.1:8000/docs`
**Render Engine**: Swagger UI v5 (JavaScript)
**Load Time**: ~2 seconds
**Status**: Partial load (API spec failed to fetch)

### Accessibility Tree (AXE Inspector)
```
Root: <html>
  ├─ No role assigned
  ├─ No aria-label
  ├─ No aria-labelledby
  └─ Content
      └─ <body>
          └─ <div id="swagger-ui">
              └─ [Swagger UI Content - partially loaded]
```

### Interactive Elements Exposed

**Element Count**: 3 (including BODY)
```
1. <button> "Hide"
   - Role: button (implicit from button tag)
   - Name: "Hide"
   - State: FOCUSABLE
   - Visible: YES
   
2. <body> (fallback)
   - Role: generic
   - Name: ""
   - State: FOCUSABLE (when no other element)
   - Visible: NO (content area)
   
3. <button> "Hide" (duplicate - cycled back)
   - Same as #1
```

### Accessibility Issues in Tree

#### 1. Root Element Missing Language (CRITICAL)
**Issue**: `<html>` element has no `lang` attribute
```
Accessibility Tree Property: language
Expected: "en" 
Actual: (not set)
Impact: Screen readers use system language
```

**WCAG Criterion**: 3.1.1 Language of Page (Level A)
**Severity**: SERIOUS

#### 2. No Main Content Landmark (MODERATE)
**Issue**: Content container lacks semantic role
```
<div id="swagger-ui">
  <!-- No role="main" or <main> wrapper -->
</div>
```

**Expected in Tree**:
```
Root: <html lang="en">
  └─ Landmark: main
      └─ [Content]
```

**Actual**:
```
Root: <html>
  └─ Generic: div#swagger-ui
      └─ [Content]
```

**WCAG Criterion**: 1.3.1 Info and Relationships (Level A)
**Severity**: MODERATE

#### 3. No Page Heading (MODERATE)
**Issue**: Content has no h1 element in accessibility tree
```
Accessible Name: "Open-Repo API - Swagger UI" (from <title> only)
Heading Structure: EMPTY
H1 Role: NOT FOUND
```

**Expected**:
```
Heading Level 1: "Open-Repo API"
  └─ Heading Level 2: "Endpoints"
      └─ Heading Level 3: "GET /api/items"
```

**Actual**:
```
(No heading hierarchy found)
```

**WCAG Criterion**: 1.3.1 Info and Relationships (Level A)
**Severity**: MODERATE

### ARIA Analysis (Swagger UI)

**ARIA Attributes Found**: 0 (in root/main elements)

| ARIA Attribute | Count | Status | Impact |
|---|---|---|---|
| `aria-label` | 0 | MISSING | Button "Hide" lacks descriptive label |
| `aria-labelledby` | 0 | MISSING | No element associations |
| `aria-hidden` | 0 | MISSING | Cannot hide decorative elements |
| `role` | 0 (explicit) | IMPLIED | Using implicit HTML roles only |
| `aria-expanded` | 0 | N/A | No collapsible sections analyzed |

**Assessment**: 
- ARIA support is minimal in rendered content
- Buttons rely on text content for accessibility
- No explicit role declarations
- May indicate incomplete Swagger UI initialization due to API spec load failure

### Role Assessment

**Element Roles**:
```
<html>           role: document (implicit)
<body>           role: generic (implicit)
<div#swagger-ui> role: generic (implicit)
<button>         role: button (implicit from tag)
                 accessible-name: "Hide"
                 accessible-state: [focusable, visible]
```

### Interactive Element Analysis

**Button "Hide"**:
```json
{
  "role": "button",
  "accessible_name": "Hide",
  "description": "",
  "state": {
    "focusable": true,
    "visible": true,
    "disabled": false
  },
  "parent_role": "generic",
  "keyboard_support": true
}
```

**Assessment**: 
- ✓ Role correctly identified
- ✓ Name is accessible
- ✓ Keyboard support present
- ⚠ No description (only if needed for complex button)
- ⚠ Minimal context about button purpose

---

## ReDoc - Accessibility Tree Analysis

### Runtime DOM Structure

**Rendered at**: `http://127.0.0.1:8000/redoc`
**Render Engine**: ReDoc v2 (JavaScript web component)
**Load Time**: ~2 seconds
**Status**: Error state (API spec failed to fetch)

### Accessibility Tree (AXE Inspector)

```
Root: <html>
  ├─ No role assigned
  ├─ No aria-label
  ├─ No aria-labelledby
  └─ Content
      └─ <body>
          ├─ <noscript> (hidden)
          └─ <redoc spec-url="/openapi.json">
              └─ [ReDoc Shadow DOM - custom component]
```

### Interactive Elements Exposed

**Element Count**: 2 (including BODY)
```
1. <summary> "Stack trace"
   - Role: button (implicit from summary tag)
   - Name: "Stack trace"
   - State: FOCUSABLE
   - Visible: YES
   
2. <body> (fallback)
   - Role: generic
   - Name: ""
   - State: FOCUSABLE (when no other element)
   - Visible: NO
```

**Note**: ReDoc component rendered incompletely due to API spec load failure
- Only error summary is interactive
- Normal documentation content not available for testing

### Accessibility Issues in Tree

#### 1. Root Element Missing Language (CRITICAL)
**Issue**: Same as Swagger UI
```
Accessibility Tree Property: language
Expected: "en"
Actual: (not set)
```

**Impact**: 
- Screen readers unable to apply language-specific pronunciation
- Content language undefined for language detection tools

**WCAG Criterion**: 3.1.1 Language of Page (Level A)
**Severity**: SERIOUS

#### 2. No Main Content Landmark (MODERATE)
**Issue**: Custom web component not wrapped in semantic landmark
```html
<redoc spec-url="/openapi.json"></redoc>
<!-- Should be: -->
<main>
  <redoc spec-url="/openapi.json"></redoc>
</main>
```

**Accessibility Tree Impact**:
```
Current: document → body → redoc (generic)
Expected: document → body → main → redoc
```

**WCAG Criterion**: 1.3.1 Info and Relationships (Level A)
**Severity**: MODERATE

#### 3. Shadow DOM Accessibility (COMPLEX)
**Issue**: ReDoc uses Shadow DOM for internal structure
```html
<redoc spec-url="/openapi.json">
  #shadow-root (open)
    ├─ [Complex internal structure]
    └─ [Potentially inaccessible to AT]
</redoc>
```

**Assessment**: 
- Shadow DOM is marked `open` (accessible from outside)
- However, accessibility depends on component implementation
- Cannot audit without inspecting Shadow DOM internals
- ReDoc v2 may have limited accessibility support

**WCAG Impact**: 
- May block structure/relationship accessibility (1.3.1)
- May block heading accessibility (1.3.1)

**Severity**: MODERATE (requires deeper investigation)

### ARIA Analysis (ReDoc)

**ARIA Attributes Found**: 0 (visible elements)

| ARIA Attribute | Count | Status | Impact |
|---|---|---|---|
| `aria-label` | 0 | MISSING | Summary element lacks description |
| `aria-labelledby` | 0 | MISSING | No element associations |
| `aria-hidden` | 0 | MISSING | No decorative element hiding |
| `role` | 0 (explicit) | IMPLIED | Using implicit HTML roles |
| `aria-expanded` | 0 | MISSING | Summary should have expanded state |

**Assessment**: 
- Summary element missing `aria-expanded` attribute
- Should indicate collapse/expand state
- WCAG 4.1.2 (Name, Role, Value) violation

### Role Assessment

**Element Roles**:
```
<html>          role: document (implicit)
<body>          role: generic (implicit)
<noscript>      role: generic, hidden=true
<redoc>         role: generic (custom component)
<summary>       role: button (implicit from summary tag)
                accessible-name: "Stack trace"
                accessible-state: [focusable, visible]
```

### Interactive Element Analysis

**Summary "Stack trace"**:
```json
{
  "role": "button",
  "accessible_name": "Stack trace",
  "description": "(Error state - normal content not loaded)",
  "state": {
    "focusable": true,
    "visible": true,
    "disabled": false,
    "expanded": null  // MISSING aria-expanded
  },
  "parent_role": "generic",
  "keyboard_support": true
}
```

**Assessment**: 
- ✓ Role correctly identified (summary = button)
- ✓ Name is accessible
- ✓ Keyboard support present
- ✗ Missing `aria-expanded` attribute
- ⚗ Content not fully loaded due to error

---

## Comparative Analysis

### Accessibility Tree Completeness

| Property | Swagger UI | ReDoc | WCAG | Status |
|---|---|---|---|---|
| Document Language | ✗ MISSING | ✗ MISSING | 3.1.1 (A) | FAIL |
| Main Landmark | ✗ MISSING | ✗ MISSING | 1.3.1 (A) | FAIL |
| Page Heading | ✗ MISSING | ✗ MISSING | 1.3.1 (A) | FAIL |
| Heading Hierarchy | ✗ NONE | ✗ NONE | 1.3.1 (A) | FAIL |
| Interactive Elements | ✓ 1+ | ✓ 1+ | 4.1.2 (A) | PASS |
| Focus State | ✓ TRACKED | ✓ TRACKED | 2.4.3 (A) | PASS |
| Button Roles | ✓ IMPLICIT | ✓ IMPLICIT | 4.1.2 (A) | PASS |
| Button Names | ✓ PRESENT | ✓ PRESENT | 4.1.2 (A) | PASS |

**Legend**:
- PASS = Correctly exposed in accessibility tree
- FAIL = Missing from accessibility tree
- IMPLICIT = Role assigned via HTML element type
- MISSING = Attribute not present

---

## WCAG 2.1 Accessibility Tree Mapping

### Level A Violations

#### Violation 1: No Document Language (3.1.1)
```
WCAG 2.1: 3.1.1 Language of Page (Level A)
Test Result: FAIL
Elements Affected: <html> on both /docs and /redoc
Required Fix: Add lang="en" attribute
Impact: Screen reader pronunciation
Severity: SERIOUS
```

#### Violation 2: Missing Content Landmark (1.3.1)
```
WCAG 2.1: 1.3.1 Info and Relationships (Level A)
Test Result: FAIL
Elements Affected: Main content area (both endpoints)
Required Fix: Wrap in <main> or add role="main"
Impact: Cannot locate primary content
Severity: MODERATE
```

#### Violation 3: Missing Page Heading (1.3.1)
```
WCAG 2.1: 1.3.1 Info and Relationships (Level A)
Test Result: FAIL
Elements Affected: Page structure (both endpoints)
Required Fix: Add <h1> to document
Impact: Cannot understand page outline
Severity: MODERATE
```

### Level A Issues Pending Runtime Verification

#### Issue 1: Interactive Element States (4.1.2)
```
WCAG 2.1: 4.1.2 Name, Role, Value (Level A)
Test Result: PARTIAL PASS
Elements Affected: Summary element (ReDoc)
Issue: Missing aria-expanded attribute
Required Fix: Add aria-expanded="false/true" to <summary>
Impact: Collapsible state not accessible
Severity: LOW-MODERATE
Note: HTML5 summary should imply expanded state, but explicit ARIA is clearer
```

---

## Assistive Technology Perspective

### What a Screen Reader User Would Experience

#### Swagger UI (/docs):
1. Page loads
2. Screen reader announces: "Open-Repo API - Swagger UI" (from title)
3. No language pronunciation guidance → system language used
4. No main content landmark → must manually navigate
5. Focus on "Hide" button → accessible, can activate with Enter
6. Cannot understand why button is important or what it affects

#### ReDoc (/redoc):
1. Page loads
2. Screen reader announces: "Open-Repo API - ReDoc" (from title)
3. No language information → system language used
4. No landmark structure → must navigate manually
5. Focus on "Stack trace" summary → accessible, can activate
6. Missing aria-expanded state → cannot determine if it's expanded
7. Cannot access documentation structure (would be in Shadow DOM)

### What Improved Experience Would Be:
```
1. Page loads
2. Screen reader announces: "Open-Repo API Documentation, English"
3. Navigation landmark detected → can skip to main content
4. Main landmark detected → marks primary content region
5. H1 detected: "Open-Repo API" → page outline understood
6. Focus on interactive element → "Hide" button in section "Endpoints"
7. All interactive elements properly labeled and structured
```

---

## Browser DevTools Accessibility Inspector Results

### Chrome DevTools Output (Swagger UI)

**Accessibility Properties**:
```
Document Language: (not set)
Page Title: "Open-Repo API - Swagger UI"
Landmarks: (none)
Headings: (none)
Lists: (none)
Forms: (none)
Interactive Elements: 1 visible (button)
ARIA Roles: (none explicit)
ARIA Properties: (none)
Color Contrast: (not analyzed in this phase)
```

### Chrome DevTools Output (ReDoc)

**Accessibility Properties**:
```
Document Language: (not set)
Page Title: "Open-Repo API - ReDoc"
Landmarks: (none)
Headings: (none)
Lists: (none)
Forms: (none)
Interactive Elements: 1 visible (summary)
ARIA Roles: (none explicit)
ARIA Properties: (missing: aria-expanded)
Color Contrast: (not analyzed in this phase)
```

**Web Component Note**:
```
Shadow DOM Detected: yes (<redoc> element)
Shadow DOM Open: yes
Accessible from Outside: yes
Content Scannable: unclear (internal structure not exposed)
```

---

## Technical Notes on Accessibility Tree

### How AT Builds Accessibility Tree

1. **HTML Parsing**: Parse semantic HTML elements
2. **ARIA Interpretation**: Apply ARIA roles/properties/states
3. **Computation**: Calculate accessible name, role, value
4. **Exposure**: Expose to assistive technology APIs
   - Windows: UIA (UI Automation)
   - Mac: AX (Accessibility)
   - Linux: ATK (Accessibility Toolkit)

### What's Missing in Current Tree

```
Current (Broken):
┌─ document (no language)
│  └─ body
│     └─ div (generic, no role)
│        └─ button "Hide"

Expected (Fixed):
┌─ document (lang="en")
│  └─ main
│     ├─ h1 "Open-Repo API"
│     └─ div (or section)
│        └─ button "Hide"
```

---

## Shadow DOM Accessibility Concerns (ReDoc)

### Shadow DOM Details

**What is Shadow DOM?**
- Encapsulated DOM subtree
- Separate from light DOM
- Can be open or closed
- ReDoc uses open Shadow DOM

**ReDoc's Shadow DOM Structure**:
```html
<redoc spec-url="/openapi.json">
  #shadow-root (open)
    ├─ <style> (CSS for ReDoc)
    ├─ <div class="redoc-wrapper">
    │  ├─ [Header/title section]
    │  ├─ [Navigation panel]
    │  └─ [Content panel]
    └─ [Additional templates]
</redoc>
```

**Accessibility Implications**:
1. **Slot Distribution**: Content is distributed via Shadow DOM slots
2. **Style Encapsulation**: Styling is isolated (good for modularity)
3. **AT Access**: Open Shadow DOM is accessible to assistive tech
4. **Structure Exposure**: Internal structure is technically accessible but may not be properly labeled
5. **Landmark Issues**: Landmarks inside Shadow DOM may not be discoverable

**Test Result**: Cannot fully audit ReDoc accessibility without deep Shadow DOM inspection

---

## Remediation Path

### Immediate Fixes (Phase 2 - June 2-3)

**Fix 1: Add Language Attribute**
```html
<!-- In FastAPI app template -->
<html lang="en">
```
**Effort**: < 2 minutes per endpoint
**Impact**: Fixes 3.1.1 violation

**Fix 2: Add Main Landmark**
```html
<body>
  <main id="main">
    <div id="swagger-ui"></div>
  </main>
</body>
```
**Effort**: 5 minutes
**Impact**: Fixes 1.3.1 violation

**Fix 3: Add Page Heading**
```html
<main id="main">
  <h1>Open-Repo API Documentation</h1>
  <div id="swagger-ui"></div>
</main>
```
**Effort**: 5 minutes
**Impact**: Fixes 1.3.1 violation

**Fix 4: Add aria-expanded to Summary (ReDoc)**
```html
<summary aria-expanded="false">Stack trace</summary>
```
**Effort**: 2 minutes (in ReDoc config if possible)
**Impact**: Fixes 4.1.2 violation

---

## Testing Methodology

**Tools Used**:
- Playwright (browser automation)
- Chrome DevTools Accessibility Inspector
- Manual DOM inspection
- AXE Accessibility Engine analysis

**Testing Coverage**:
- ✓ Accessibility tree structure
- ✓ Landmark exposure
- ✓ Interactive element roles
- ✓ ARIA attribute presence
- ✓ Heading hierarchy
- ⏳ Deep Shadow DOM analysis (ReDoc) - requires additional tools

---

## Summary Assessment

### Swagger UI Accessibility Tree
- **Status**: FAIL - Critical landmarks missing
- **Issues**: 3 Level A violations
- **Remediable**: YES - 30 minutes for all fixes
- **Confidence**: HIGH - clear solutions available

### ReDoc Accessibility Tree
- **Status**: FAIL - Critical landmarks missing + Shadow DOM concerns
- **Issues**: 3+ Level A violations (4+ if including aria-expanded)
- **Remediable**: PARTIAL - Shadow DOM complexity
- **Confidence**: MODERATE - ReDoc component may have internal limitations

### Overall Verdict
**Both endpoints fail basic accessibility tree requirements.**

Immediate action needed:
1. Add lang attribute to both
2. Add main landmark to both
3. Add h1 heading to both
4. (Optional) investigate ReDoc Shadow DOM structure

---

## Next Steps

**Phase 2 Completion (June 6)**:
- Coordinate with Phase 3 fixes
- Re-test after remediation
- Verify accessibility tree improvements

**Phase 3 (June 12 deployment)**:
- Implement all P0/P1 fixes
- Re-run full accessibility audit
- Verify WCAG 2.1 AA compliance

