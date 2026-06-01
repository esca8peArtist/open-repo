# A11y Triage Checklist
## June 1, 2026 - Automated Scan Results

## P0 - Critical Issues (Must Fix Before Deployment)
**Count**: 0 violations


## P1 - Serious Issues (Should Fix Before Deployment)
**Count**: 3 violations

- [ ] **html-has-lang**: Ensure every HTML document has a lang attribute
- [ ] **color-contrast**: Ensure the contrast between foreground and background colors meets WCAG 2 AA minimum contrast ratio thresholds
- [ ] **html-has-lang**: Ensure every HTML document has a lang attribute

## P2 - Moderate Issues (Can Fix Post-Deployment)
**Count**: 4 violations

- [ ] **landmark-one-main**: Ensure the document has a main landmark
- [ ] **page-has-heading-one**: Ensure that the page, or at least one of its frames contains a level-one heading
- [ ] **landmark-one-main**: Ensure the document has a main landmark
- [ ] **region**: Ensure all page content is contained by landmarks

## P3 - Minor Issues (Future Enhancements)
**Count**: 0 violations


## Known Limitations & Third-Party Behaviors

- FastAPI Swagger UI (/docs): Third-party library, axe-core may flag CDN-delivered components
- ReDoc (/redoc): Third-party library, limited control over generated HTML
- Dynamic content: Items loaded post-initial-render not scanned (static analysis only)

## Triage Status

- Scanned: 2 pages
- Total violations: 7
- Critical: 0
- Serious: 3
- Moderate: 4
- Minor: 0