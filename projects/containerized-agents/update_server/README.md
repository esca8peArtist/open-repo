# AgentCore Update Server

## Architecture Overview

The update server is the **only always-on server-side component** in the AgentCore product. It is a static file distribution system — no compute, no database, no running processes. It consists of:

- An **S3 bucket** (`agentcore-updates`) containing a signed `manifest.json` and release artifacts.
- A **CloudFront distribution** serving the bucket over HTTPS at `https://updates.agentcore.io`.
- A **CI/CD publishing script** (`publish_release.py`) that generates the signed manifest and uploads to S3.

On-device, the AgentCore admin dashboard includes a "Check for Updates" button that fetches `manifest.json`, verifies the Ed25519 signature, and presents available updates to the operator.

---

## How the Update Manifest Works

The manifest is a single JSON file at `https://updates.agentcore.io/manifest.json`.

**Structure:**

```
manifest.json
├── schema_version       — integer, currently 1
├── published_at         — ISO8601 UTC timestamp
├── latest               — shortcut: latest version per hardware tier
├── releases[]           — ordered list (newest first) of release objects
│   ├── version          — semver
│   ├── published_at
│   ├── min_version      — minimum version that can upgrade to this (optional)
│   ├── changelog        — Markdown, shown in dashboard
│   ├── critical         — bool, triggers prominent warning in dashboard
│   └── components
│       ├── agentcore    — Docker image tar.gz: url, sha256, size_bytes
│       ├── wizard       — Docker image tar.gz: url, sha256, size_bytes
│       └── models[]     — Model file updates: name, version, tiers, sha256
└── signature            — Ed25519 hex signature over canonical JSON of all other fields
```

See `manifest_schema.json` for the full JSON Schema and `example_manifest.json` for a real example.

**Signature coverage:** The signature covers the canonical JSON (keys sorted, no extra whitespace) of the entire manifest object *excluding* the `signature` field itself. Clients must verify this before trusting any release data.

---

## How to Publish a New Release

### Prerequisites

1. Install dependencies:
   ```bash
   pip install boto3 cryptography click
   ```

2. Set environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID=...
   export AWS_SECRET_ACCESS_KEY=...
   export AWS_REGION=us-east-1
   export S3_BUCKET=agentcore-updates
   export CLOUDFRONT_DISTRIBUTION=E1ABCDEFGHIJKL
   export UPDATE_SIGNING_KEY=<64-char hex Ed25519 private key>
   ```

   The `UPDATE_SIGNING_KEY` is the 32-byte Ed25519 private key encoded as 64 hex characters. Store it in your CI/CD secrets manager (e.g. AWS Secrets Manager, GitHub Actions secrets). **Never commit it to the repository.**

### Publishing a release

```bash
python publish_release.py \
    --version 1.2.0 \
    --changelog "## v1.2.0\n\n- Feature A\n- Bug fix B" \
    --agentcore-image /path/to/agentcore-1.2.0.tar.gz \
    --wizard-image /path/to/wizard-1.2.0.tar.gz \
    --min-version 1.0.0
```

**What happens:**
1. SHA-256 digests are computed for each image file.
2. Image files are uploaded to `s3://agentcore-updates/releases/<version>/`.
3. The existing `manifest.json` is downloaded from S3.
4. The new release is prepended to the releases list.
5. The manifest is signed with the Ed25519 private key.
6. The signed manifest is uploaded to `s3://agentcore-updates/manifest.json`.
7. A CloudFront invalidation is created for `/manifest.json` (TTL is 60s via Cache-Control; invalidation ensures instant propagation for critical updates).

**Dry run (test without uploading):**
```bash
python publish_release.py --version 1.2.0 --changelog "..." --dry-run
```

### Critical security updates

Add `--critical` to show a prominent warning banner in the admin dashboard:

```bash
python publish_release.py --version 1.2.1 --changelog "Security patch" --critical ...
```

---

## Security Model

### Signing

- **Algorithm:** Ed25519 (fast, small signatures, not vulnerable to fault attacks that affect ECDSA)
- **Key size:** 32-byte private key → 64-byte public key → 64-byte signatures
- **What is signed:** Canonical JSON (UTF-8, keys sorted, minimal whitespace) of the entire manifest excluding the `signature` field
- **Public key:** Embedded in the AgentCore binary at build time via `UPDATE_PUBLIC_KEY_HEX` build variable. Cannot be changed after build without a software update.
- **Private key:** Stored in CI/CD secrets only. Never touches on-device hardware.

### On-device verification (update_checker.py)

Before acting on any manifest data:
1. Fetch `manifest.json` over HTTPS (TLS 1.2+ enforced by CloudFront).
2. Reconstruct canonical JSON excluding `signature`.
3. Verify Ed25519 signature using the embedded public key.
4. Reject the manifest entirely if verification fails.

A tampered or forged manifest cannot pass signature verification without the private key.

### SHA-256 verification

Before applying any downloaded component:
1. Download to a temp file.
2. Compute SHA-256 of the downloaded file.
3. Compare (constant-time) against the `sha256` field from the verified manifest.
4. Reject and delete if mismatch.

This prevents:
- Corrupted downloads (network errors)
- CDN cache poisoning attacks
- Man-in-the-middle attacks that bypass TLS

---

## S3 Bucket Structure

```
agentcore-updates/
├── manifest.json                          ← Always-current signed manifest
├── releases/
│   ├── 1.0.0/
│   │   ├── agentcore-1.0.0.tar.gz
│   │   └── wizard-1.0.0.tar.gz
│   ├── 1.1.0/
│   │   ├── agentcore-1.1.0.tar.gz
│   │   └── wizard-1.1.0.tar.gz
│   └── 1.2.0/
│       ├── agentcore-1.2.0.tar.gz
│       └── wizard-1.2.0.tar.gz
└── models/
    ├── qwen2.5-7b-instruct-q4_k_m.gguf
    ├── qwen2.5-14b-instruct-q4_k_m.gguf
    └── ...
```

**Bucket policy:** Objects are publicly readable (served via CloudFront). Only the CI/CD IAM role has write access.

**Versioning:** S3 versioning is enabled on the bucket. Previous `manifest.json` versions are retained for 90 days for audit purposes.

---

## Generating a New Signing Key Pair

```python
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
key = Ed25519PrivateKey.generate()
private_bytes = key.private_bytes_raw()
public_bytes = key.public_key().public_bytes_raw()
print("Private (UPDATE_SIGNING_KEY):", private_bytes.hex())
print("Public  (UPDATE_PUBLIC_KEY_HEX):", public_bytes.hex())
```

- Store the private key in your secrets manager.
- Embed the public key hex in the AgentCore build via the `UPDATE_PUBLIC_KEY_HEX` environment variable.
- **If the private key is compromised:** rotate immediately. You must ship a software update containing the new public key before the old key is revoked. Keep both keys active during the transition window.
