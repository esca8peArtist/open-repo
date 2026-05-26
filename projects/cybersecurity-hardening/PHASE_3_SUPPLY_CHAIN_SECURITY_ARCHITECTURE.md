---
title: "Phase 3 Supply Chain Security Architecture"
project: cybersecurity-hardening
phase: 3
status: research-complete
created: 2026-05-21
target-execution: June–July 2026
confidence: high
---

# Phase 3: Supply Chain Security Architecture

**Most critical finding**: In March 2026, Trivy — the most widely deployed open-source container scanner — suffered two coordinated supply chain compromises in two weeks, cascading into downstream projects including litellm. This is not a theoretical threat. Supply chain attacks are now the dominant initial-access vector for sophisticated actors, and every home lab and small project running unverified dependencies or unscanned container images carries real exposure.

---

## 1. Software Bill of Materials (SBOM) Generation

An SBOM is a machine-readable inventory of every component in a software artifact — libraries, licenses, checksums, and provenance. Without one, you cannot know what you are running. NIST CSF 2.0 now treats C-SCRM (Cybersecurity Supply Chain Risk Management) as a named category in the Govern function, making SBOM generation a baseline practice, not an advanced one.

### Tool Recommendations

**Syft (Anchore)** — Primary recommendation for home lab use.
- Supports CycloneDX and SPDX output formats
- Scans container images, directories, source trees, and compiled binaries
- Multi-ecosystem: Python, Node, Go, Rust, Java, Ruby, and more
- Free, open-source, CLI-first — ideal for scripting into CI pipelines
- Install: `curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin`
- Generate SBOM: `syft scan stockbot:latest -o cyclonedx-json > stockbot-sbom.json`

**cdxgen (OWASP CycloneDX)** — Best for reachability analysis.
- Official OWASP project; CycloneDX-only output but goes deeper
- Generates reachability evidence: proves whether vulnerable code is actually called in execution paths
- Supports 20+ languages; produces multiple BOM types (SBOM, SaaSBOM, OBOM)
- Can sign documents for tamper verification
- Better for Python projects like stockbot where you want to know if a CVE in a transitive dependency is actually reachable
- Install: `npm install -g @cyclonedx/cdxgen`

**Do not use Trivy for SBOM generation or scanning as of March 2026**. Use Grype (Anchore) as a companion vulnerability scanner alongside Syft instead.

### SBOM Formats: CycloneDX vs. SPDX

| Dimension | CycloneDX | SPDX |
|---|---|---|
| Governance | OWASP Foundation | Linux Foundation |
| Primary focus | Security context, vulnerability correlation | License compliance |
| Best for | Detecting CVEs in dependencies | Legal/compliance audits |
| Latest version | 1.6+ (2025) | 3.0 (2025) |
| Recommendation | Use for runtime security scanning | Use for license auditing |

For home lab projects (stockbot, seedwarden, open-repo), generate CycloneDX SBOMs on every container build and commit it to the repository alongside the artifact.

---

## 2. Continuous Dependency Scanning

### GitHub Dependabot (Free Tier — Primary)

Dependabot is free for all public and private GitHub repositories without restrictions on repository count or scan frequency. It automatically opens pull requests when a dependency has a known CVE.

Configuration (`.github/dependabot.yml`):
```yaml
version: 2
updates:
  - package-ecosystem: "pip"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
  - package-ecosystem: "docker"
    directory: "/"
    schedule:
      interval: "weekly"
```

Limitations: Dependabot does not perform deep container image layer scanning and does not assess reachability. It flags all CVEs in declared dependencies regardless of whether the vulnerable code path is exercised.

### Grype (Anchore) — Container and File System Scanning

Grype is the recommended Trivy replacement as of March 2026. It scans container images and directories against the Anchore vulnerability database (sourced from NVD, GitHub Advisory Database, and distro-specific sources).

```bash
# Install
curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin

# Scan a container image
grype stockbot:latest

# Scan against an SBOM (faster, offline-capable)
grype sbom:./stockbot-sbom.json

# Fail CI if any critical CVE found
grype stockbot:latest --fail-on critical
```

### OWASP Dependency-Check — Java/Node/Python Source Scanning

For projects where you have source access, OWASP Dependency-Check runs locally with no rate limits and no account required. Produces HTML and XML reports.

```bash
dependency-check --project "stockbot" --scan ./requirements.txt --format HTML --out ./reports/
```

### Snyk Free Tier — When to Use It

Snyk's free tier is limited to 200 open-source tests per month across up to 5 projects. Given Dependabot covers continuous PRs and Grype covers container scanning, Snyk is most valuable as a one-time deep audit of a new project before initial deployment, not for continuous monitoring at home-lab scale.

---

## 3. Artifact Verification and Code Signing

### Container Image Signing with Cosign (Sigstore)

Cosign (part of the Sigstore project) allows you to sign container images and verify signatures before running them. This detects tampered images even if a registry has been compromised.

```bash
# Install cosign
curl -LO https://github.com/sigstore/cosign/releases/latest/download/cosign-linux-amd64
sudo mv cosign-linux-amd64 /usr/local/bin/cosign && chmod +x /usr/local/bin/cosign

# Sign an image (keyless, using OIDC identity)
cosign sign ghcr.io/youruser/stockbot:latest

# Verify before deploying
cosign verify ghcr.io/youruser/stockbot:latest
```

For the Pi home lab, keyless signing via GitHub Actions OIDC is the simplest implementation. The signature is stored in the container registry alongside the image.

### Python Package Verification

Python packages from PyPI do not have mandatory signing as of 2026. Mitigations:
1. Pin all dependencies to exact versions and hashes in `requirements.txt` using `pip-compile --generate-hashes`
2. Use `uv` (already in use per project rules) which performs hash verification by default when a lockfile is present
3. Review `uv.lock` diffs in every dependency update PR

---

## 4. Third-Party Risk and Vendor Monitoring

### License Policy

**Acceptable licenses** for home lab and personal projects: MIT, Apache 2.0, BSD 2-Clause, BSD 3-Clause, ISC, MPL 2.0 (file-level copyleft only).

**Copyleft licenses requiring review**: GPL v2, GPL v3, AGPL v3. These require that derivative works also be open-source. For internal tools that never distribute outside the home lab, this is generally acceptable. For any code distributed to others, GPL/AGPL requires legal review.

**Unacceptable for any use**: Licenses with field-of-use restrictions, non-compete clauses, or that prohibit commercial use when a home lab project may monetize (e.g., stockbot).

Use `syft scan --output cyclonedx-json` and then `cdxgen --license` to audit license compliance per project before production deployment.

### Breach Monitoring

**Have I Been Pwned (HIBP) API** — Free tier allows checking email addresses for breach exposure. Register `wanka95@gmail.com` with HIBP notifications to receive alerts when credentials appear in new breach data dumps.

**GitHub Advisory Database** — Subscribe to security advisories for repositories you depend on. For each active project, go to the repository's Security tab and enable "Watch" for security advisories.

**CISA Known Exploited Vulnerabilities (KEV) Catalog** — CISA maintains a public list of CVEs with confirmed active exploitation. Cross-reference your SBOM against KEV before any production deployment: `https://www.cisa.gov/known-exploited-vulnerabilities-catalog`

---

## 5. Applying SBOM Scanning to Pi Home Lab Projects

### Per-Project Implementation

**stockbot** (Python, Raspberry Pi 5):
- Generate SBOM on every Docker build: `syft scan stockbot:latest -o cyclonedx-json > sbom/stockbot-$(date +%Y%m%d).json`
- Grype scan in CI before deploy: `grype sbom:sbom/stockbot-latest.json --fail-on critical`
- Dependabot enabled on the GitHub repository for weekly pip/Docker updates

**seedwarden** (Python, Pi):
- Same SBOM + Grype pipeline as stockbot
- Additional: scan any hardware interface libraries (GPIO, I2C drivers) which often have unmaintained transitive dependencies

**open-repo** (public-facing):
- Highest priority: this is externally visible
- Cosign image signing mandatory before any public release
- Monthly license audit via cdxgen to ensure no GPL contamination in distributed artifacts

### CI Pipeline Template (GitHub Actions)

```yaml
name: Supply Chain Security
on: [push, pull_request]
jobs:
  sbom-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Generate SBOM
        run: |
          curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
          syft scan . -o cyclonedx-json > sbom.json
      - name: Scan for vulnerabilities
        run: |
          curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin
          grype sbom:sbom.json --fail-on critical
      - name: Upload SBOM artifact
        uses: actions/upload-artifact@v4
        with:
          name: sbom
          path: sbom.json
```

---

## 6. Confidence Levels and Known Gaps

**High confidence**: Syft + Grype pipeline is production-ready for home lab use. Dependabot free tier is reliable for continuous monitoring.

**Medium confidence**: Cosign keyless signing workflow — the OIDC-based approach requires GitHub Actions; standalone Pi builds need a different signing workflow (keypair-based), which adds key management complexity.

**Known gap**: Runtime supply chain monitoring. SBOM scanning catches vulnerabilities at build time; a compromised package that exploits a zero-day after deployment will not be caught by pre-deployment SBOM scans. Wazuh (covered in Phase 3 APT document) provides partial runtime coverage through file integrity monitoring.

**Known gap**: Hardware supply chain. The Raspberry Pi 5 hardware itself is outside the scope of software SBOM tools. Firmware verification for the Pi requires checking against official Raspberry Pi Foundation release hashes.

---

## Sources

- [SBOM Generation Tools Comparison (sbomify, 2026)](https://sbomify.com/2026/01/26/sbom-generation-tools-comparison/)
- [Syft by Anchore — SBOM Generation](https://anchore.com/sbom/how-to-generate-an-sbom-with-free-open-source-tools/)
- [cdxgen — OWASP CycloneDX Generator](https://appsecsanta.com/cdxgen)
- [SPDX vs CycloneDX Format Comparison](https://www.herodevs.com/blog-posts/spdx-vs-cyclonedx-choosing-the-right-sbom-format-for-your-software-supply-chain)
- [NIST SP 800-161 Rev. 1 — C-SCRM Practices](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final)
- [NIST CSF 2.0 Supply Chain Governance](https://www.6clicks.com/resources/blog/nist-csf-supply-chain-risk-third-party-cybersecurity-2026)
- [CISA Defending Against Software Supply Chain Attacks](https://www.cisa.gov/resources-tools/resources/defending-against-software-supply-chain-attacks)
- [Snyk vs Dependabot Comparison (2026)](https://dev.to/rahulxsingh/snyk-vs-dependabot-developer-security-platform-vs-free-dependency-updates-2026-54c6)
- [SCA Tools in CI/CD (2026)](https://appsecsanta.com/sca-tools/sca-in-cicd)
- [Supply Chain Security: SBOM and Code Signing](https://dev.to/kanywst/supply-chain-security-a-deep-dive-into-sbom-and-code-signing-2n1l)
- [OpenSSF — Choosing an SBOM Generation Tool](https://openssf.org/blog/2025/06/05/choosing-an-sbom-generation-tool/)
