# Accessibility Audit Findings Report
## June 1, 2026 - Automated Scanning Phase

**Audit Timestamp**: 2026-06-03T01:57:42.095482
**Base URL**: http://localhost:8000

## Executive Summary

- **Total Violations Found**: 2
- **Violations by Severity**:
  - Serious: 1
  - Moderate: 1

## Findings by Page

### Swagger UI (FastAPI /docs)
**Total violations**: 1

#### MODERATE Violations (1)

**1. heading-order**
- **Description**: Ensure the order of headings is semantically correct
- **Impact**: moderate
- **Help**: Heading levels should only increase by one
- **Affected Elements**: 1
  - .title
- **Recommended Fix**: https://dequeuniversity.com/rules/axe/4.11/heading-order?application=axeAPI

### ReDoc (API documentation)
**Total violations**: 1

#### SERIOUS Violations (1)

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

## Pass/Fail Metrics by WCAG Criterion

- WCAG143: 1 violations
- WCAG2AA: 1 violations

## Next Steps

1. **Triage violations** by severity (P0/P1/P2/P3)
2. **Prioritize critical issues** for immediate remediation
3. **Create remediation tasks** for each violation
4. **Plan manual testing** phase (June 2-3)
5. **Document known limitations** and third-party library behaviors