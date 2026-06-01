# Accessibility Audit Findings Report
## June 1, 2026 - Automated Scanning Phase

**Audit Timestamp**: 2026-06-01T12:14:56.590717
**Base URL**: http://localhost:8000

## Executive Summary

- **Total Violations Found**: 7
- **Violations by Severity**:
  - Serious: 3
  - Moderate: 4

## Findings by Page

### Swagger UI (FastAPI /docs)
**Total violations**: 3

#### SERIOUS Violations (1)

**1. html-has-lang**
- **Description**: Ensure every HTML document has a lang attribute
- **Impact**: serious
- **Help**: <html> element must have a lang attribute
- **WCAG Criteria**: wcag2a, wcag311
- **Affected Elements**: 1
  - html
- **Recommended Fix**: https://dequeuniversity.com/rules/axe/4.11/html-has-lang?application=axeAPI

#### MODERATE Violations (2)

**1. landmark-one-main**
- **Description**: Ensure the document has a main landmark
- **Impact**: moderate
- **Help**: Document should have one main landmark
- **Affected Elements**: 1
  - html
- **Recommended Fix**: https://dequeuniversity.com/rules/axe/4.11/landmark-one-main?application=axeAPI

**2. page-has-heading-one**
- **Description**: Ensure that the page, or at least one of its frames contains a level-one heading
- **Impact**: moderate
- **Help**: Page should contain a level-one heading
- **Affected Elements**: 1
  - html
- **Recommended Fix**: https://dequeuniversity.com/rules/axe/4.11/page-has-heading-one?application=axeAPI

### ReDoc (API documentation)
**Total violations**: 4

#### SERIOUS Violations (2)

**1. color-contrast**
- **Description**: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds
- **Impact**: serious
- **Help**: Elements must meet minimum color contrast ratio thresholds
- **WCAG Criteria**: wcag2aa, wcag143
- **Affected Elements**: 4
  - small:nth-child(2)
  - summary
  - small:nth-child(4)
  - ... and 1 more
- **Recommended Fix**: https://dequeuniversity.com/rules/axe/4.11/color-contrast?application=axeAPI

**2. html-has-lang**
- **Description**: Ensure every HTML document has a lang attribute
- **Impact**: serious
- **Help**: <html> element must have a lang attribute
- **WCAG Criteria**: wcag2a, wcag311
- **Affected Elements**: 1
  - html
- **Recommended Fix**: https://dequeuniversity.com/rules/axe/4.11/html-has-lang?application=axeAPI

#### MODERATE Violations (2)

**1. landmark-one-main**
- **Description**: Ensure the document has a main landmark
- **Impact**: moderate
- **Help**: Document should have one main landmark
- **Affected Elements**: 1
  - html
- **Recommended Fix**: https://dequeuniversity.com/rules/axe/4.11/landmark-one-main?application=axeAPI

**2. region**
- **Description**: Ensure all page content is contained by landmarks
- **Impact**: moderate
- **Help**: All page content should be contained by landmarks
- **Affected Elements**: 4
  - h1
  - small:nth-child(2)
  - small:nth-child(4)
  - ... and 1 more
- **Recommended Fix**: https://dequeuniversity.com/rules/axe/4.11/region?application=axeAPI

## Pass/Fail Metrics by WCAG Criterion

- WCAG143: 1 violations
- WCAG2A: 2 violations
- WCAG2AA: 1 violations
- WCAG311: 2 violations

## Next Steps

1. **Triage violations** by severity (P0/P1/P2/P3)
2. **Prioritize critical issues** for immediate remediation
3. **Create remediation tasks** for each violation
4. **Plan manual testing** phase (June 2-3)
5. **Document known limitations** and third-party library behaviors