---
title: "GitHub Gist API Integration Guide"
created: 2026-05-06
status: production-ready
purpose: "Authoritative reference for creating, reading, and updating GitHub Gists via the REST API. Includes curl and Python examples, authentication, rate limits, and update patterns."
companion_files:
  - gist-template-structure.md — Gist layout and structure
  - field-fill-automation-spec.md — batch field replacement script
---

# GitHub Gist API Integration Guide

The six canonical Gists are already live and do not need to be created via API.
This guide covers: programmatic creation for the Domain 37 Gist (Path A+37) and any
future Gists, updating existing Gists without breaking external links, and optional
monitoring of Gist engagement.

---

## 1. Authentication

### 1.1 Personal Access Token (PAT)

**Required scope**: `gist` only. No other scopes needed.

**Generate**:
1. Go to https://github.com/settings/tokens (classic token view)
2. Click "Generate new token (classic)"
3. Set expiration: 90 days (covers Phase 1 + Phase 2 distribution)
4. Check: `gist` scope only
5. Click "Generate token"
6. Copy the token immediately — GitHub shows it once

**Store as environment variable**:

```bash
export GITHUB_PAT="ghp_your_token_here"
# Add to ~/.bashrc or ~/.zshrc for persistence across sessions
echo 'export GITHUB_PAT="ghp_your_token_here"' >> ~/.bashrc
```

**Never** write the token value into a script file or commit it to the repository.

### 1.2 Token Verification

Verify the token works and has Gist scope before running any creation calls:

```bash
curl -s -H "Authorization: Bearer $GITHUB_PAT" \
     -H "Accept: application/vnd.github+json" \
     https://api.github.com/user | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('login', 'ERROR: ' + str(d)))"
```

**Expected output**: `esca8peArtist` (your GitHub username)

If you see an error, the token is invalid or does not have the correct scope.

---

## 2. Gist Creation

### 2.1 Minimal curl Example

```bash
curl -s \
  -H "Authorization: Bearer $GITHUB_PAT" \
  -H "Accept: application/vnd.github+json" \
  -X POST \
  https://api.github.com/gists \
  -d '{
    "description": "Domain 37 — Federal Executive Interference in the 2026 Midterms | Democratic Renewal Research Framework",
    "public": true,
    "files": {
      "domain-37-federal-executive-interference-2026-midterms.md": {
        "content": "# YOUR DOCUMENT CONTENT HERE"
      }
    }
  }'
```

**Response fields to capture**:
- `html_url`: The public URL for the Gist (e.g., `https://gist.github.com/esca8peArtist/abc123`)
- `id`: The Gist hash (needed for update calls)
- `created_at`: ISO timestamp of creation

### 2.2 Full Python Example (Recommended for Long Documents)

The curl approach requires escaping the document content as JSON. For documents over
a few hundred characters, Python is cleaner because it handles the JSON encoding.

```python
#!/usr/bin/env python3
"""
create_gist.py — Create a single Gist from a local markdown file.

Usage:
  uv run python scripts/create_gist.py \
    --file "projects/resistance-research/domains/domain-37-federal-executive-interference-2026-midterms.md" \
    --description "Domain 37 — Federal Executive Interference in the 2026 Midterms | Democratic Renewal Research Framework" \
    --gist-filename "domain-37-federal-executive-interference-2026-midterms.md"

Requires:
  GITHUB_PAT environment variable set with gist scope.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

try:
    import requests
except ImportError:
    print("Install requests: uv pip install requests")
    sys.exit(1)

API_BASE = "https://api.github.com"
HEADERS = {
    "Authorization": f"Bearer {os.environ.get('GITHUB_PAT', '')}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}


def create_gist(content: str, gist_filename: str, description: str, public: bool = True) -> dict:
    """Create a new GitHub Gist. Returns the full API response dict."""
    if not os.environ.get("GITHUB_PAT"):
        raise ValueError("GITHUB_PAT environment variable is not set.")

    payload = {
        "description": description,
        "public": public,
        "files": {
            gist_filename: {"content": content}
        },
    }

    response = requests.post(
        f"{API_BASE}/gists",
        headers=HEADERS,
        data=json.dumps(payload),
        timeout=30,
    )

    if response.status_code == 201:
        return response.json()
    else:
        raise RuntimeError(
            f"Gist creation failed: HTTP {response.status_code}\n{response.text}"
        )


def main():
    parser = argparse.ArgumentParser(description="Create a GitHub Gist from a local file.")
    parser.add_argument("--file", required=True, help="Path to local markdown file")
    parser.add_argument("--description", required=True, help="Gist description (one sentence)")
    parser.add_argument("--gist-filename", required=True, help="Filename for the Gist (e.g., doc.md)")
    parser.add_argument("--secret", action="store_true", help="Create as secret Gist (default: public)")
    args = parser.parse_args()

    source = Path(args.file)
    if not source.exists():
        print(f"ERROR: File not found: {source}")
        sys.exit(1)

    content = source.read_text(encoding="utf-8")
    if len(content) < 100:
        print(f"WARNING: File content is very short ({len(content)} chars). Verify file path.")

    print(f"Creating Gist for: {source.name}")
    print(f"  Description: {args.description}")
    print(f"  Visibility: {'secret' if args.secret else 'public'}")
    print(f"  Content length: {len(content):,} characters")

    result = create_gist(
        content=content,
        gist_filename=args.gist_filename,
        description=args.description,
        public=not args.secret,
    )

    print(f"\nGist created successfully:")
    print(f"  URL:        {result['html_url']}")
    print(f"  ID:         {result['id']}")
    print(f"  Created at: {result['created_at']}")
    print(f"\nRecord this URL in DISTRIBUTION_GIST_URLS.md")


if __name__ == "__main__":
    main()
```

**Usage for Domain 37 Gist (Path A+37)**:

```bash
# First, ensure the source file has the header/footer blocks prepended
# (see gist-template-structure.md for the header/footer content)
# Then:
uv run python scripts/create_gist.py \
  --file "projects/resistance-research/domains/domain-37-with-header-footer.md" \
  --description "Domain 37 — Federal Executive Interference in the 2026 Midterms | Democratic Renewal Research Framework" \
  --gist-filename "domain-37-federal-executive-interference-2026-midterms.md"
```

### 2.3 Rate Limit Notes for Creation

- Each Gist creation is one POST request.
- Authenticated rate limit: 5,000 requests/hour.
- For this distribution (1-7 Gists maximum), rate limits are irrelevant.
- GitHub recommends a minimum 1-second gap between mutating requests to the same endpoint.
  Add `time.sleep(1)` between calls in any batch loop.

---

## 3. Gist Update (PATCH)

**Critical principle**: Always PATCH an existing Gist rather than creating a new one.
PATCH preserves the existing URL, so all emails, citations, and bookmarks pointing to
the Gist continue to work with the updated content.

### 3.1 Finding the Gist ID

The Gist ID is the hash in the URL: `https://gist.github.com/esca8peArtist/[GIST_ID]`

All six canonical Gist IDs are in `DISTRIBUTION_GIST_URLS.md`. Example:
- Proposal Gist: `2dec7fd03b08ab5b41c55d402f44c261`
- Litigation Tracker: `418d51bda087f15a04d685ab171a5ee0`

### 3.2 curl PATCH Example

```bash
GIST_ID="418d51bda087f15a04d685ab171a5ee0"   # Litigation Tracker

curl -s \
  -H "Authorization: Bearer $GITHUB_PAT" \
  -H "Accept: application/vnd.github+json" \
  -X PATCH \
  "https://api.github.com/gists/${GIST_ID}" \
  -d '{
    "description": "Litigation Tracker 2026 — Updated May 2026",
    "files": {
      "litigation-tracker-2026.md": {
        "content": "# UPDATED CONTENT HERE"
      }
    }
  }'
```

**Note on PATCH semantics**: PATCH only updates the fields you include. Omitting
`description` keeps the existing description. Including a filename in `files` updates
that file's content. You cannot delete a file via PATCH (set content to null, but
this is rarely needed for this distribution).

### 3.3 Python PATCH Example

```python
def update_gist(gist_id: str, gist_filename: str, new_content: str,
                new_description: str = None) -> dict:
    """Update an existing Gist's file content and optionally its description."""
    if not os.environ.get("GITHUB_PAT"):
        raise ValueError("GITHUB_PAT environment variable is not set.")

    payload = {
        "files": {
            gist_filename: {"content": new_content}
        }
    }
    if new_description:
        payload["description"] = new_description

    response = requests.patch(
        f"{API_BASE}/gists/{gist_id}",
        headers=HEADERS,
        data=json.dumps(payload),
        timeout=30,
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise RuntimeError(
            f"Gist update failed: HTTP {response.status_code}\n{response.text}"
        )
```

### 3.4 When to Update vs. When to Create New

| Situation | Action |
|-----------|--------|
| Tracker update (new cases added, currency date updated) | PATCH existing Gist |
| Domain analysis updated (new developments) | PATCH existing Gist |
| Proposal minor corrections | PATCH existing Gist |
| Document structurally reorganized (split into parts) | Create new Gist; update old Gist with redirect notice |
| Adding a new domain file not previously published | Create new Gist |

---

## 4. Retrieving Gist Data

### 4.1 Read a Gist (Unauthenticated)

Reading Gist content does not require authentication (for public Gists):

```bash
GIST_ID="2dec7fd03b08ab5b41c55d402f44c261"

curl -s \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/gists/${GIST_ID}" \
  | python3 -c "
import sys, json
d = json.load(sys.stdin)
print('Description:', d['description'])
print('Created:', d['created_at'])
print('Updated:', d['updated_at'])
for fname, fdata in d['files'].items():
    print(f'File: {fname} ({fdata[\"size\"]} bytes)')
"
```

### 4.2 List All Gists for the Account

```bash
curl -s \
  -H "Authorization: Bearer $GITHUB_PAT" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/users/esca8peArtist/gists" \
  | python3 -c "
import sys, json
gists = json.load(sys.stdin)
for g in gists:
    files = list(g['files'].keys())
    print(g['html_url'], '|', g['description'][:60], '|', files[0] if files else '')
"
```

---

## 5. Webhook Setup for Monitoring (Optional)

GitHub Gist does not support webhooks natively. The options for monitoring Gist
engagement are limited but sufficient for this distribution:

### 5.1 View Count via Gist Analytics

GitHub shows view counts for your own Gists at:
```
https://gist.github.com/esca8peArtist/[GIST_ID]/analytics
```
This requires being logged in as the Gist author. It shows daily view counts for
the past 30 days. No API access to these analytics is available.

**Recommended workflow**: Check Gist analytics once per week during Phase 1
(T+7, T+14, T+21, T+30 days). Record the cumulative view count per Gist in the
contact log or a simple tracking spreadsheet.

### 5.2 Comment Monitoring via API

Gist comments can be monitored via API:

```bash
GIST_ID="2dec7fd03b08ab5b41c55d402f44c261"

curl -s \
  -H "Authorization: Bearer $GITHUB_PAT" \
  -H "Accept: application/vnd.github+json" \
  "https://api.github.com/gists/${GIST_ID}/comments"
```

For this distribution, Gist comments are unlikely to be a primary feedback channel
(most engagement will come via email or Reddit discussion). Monitor weekly rather
than setting up automated polling.

### 5.3 Google Alerts as a Proxy

Set up Google Alerts for each Gist URL to detect external citations:

1. Go to https://www.google.com/alerts
2. Create an alert for: `site:gist.github.com/esca8peArtist`
3. This alerts on any new web page that links to your Gist domain
4. Also create alerts for: `"democratic renewal proposal"` and `"35-domain framework"`
   to catch citations that don't link directly

These alerts cover the more valuable signal: the framework being cited in articles,
legal briefs, or organizational documents — not just Gist views.

---

## 6. Error Handling Reference

| HTTP Status | Meaning | Response |
|-------------|---------|----------|
| 201 Created | Gist created successfully | Capture `html_url` and `id` from response |
| 200 OK | Gist updated successfully | Verify `updated_at` timestamp changed |
| 401 Unauthorized | Invalid or missing token | Re-generate PAT; check `GITHUB_PAT` is set |
| 403 Forbidden | Token lacks gist scope | Re-generate PAT with `gist` scope only |
| 404 Not Found | Gist ID does not exist | Verify Gist ID from `DISTRIBUTION_GIST_URLS.md` |
| 422 Unprocessable | Malformed request body | Check JSON syntax; verify `files` key structure |
| 429 Too Many Requests | Rate limit exceeded | Wait 1 hour; add `time.sleep(1)` between calls |
| 500 Server Error | GitHub infrastructure issue | Retry after 5 minutes |

---

## 7. Quick Reference: All Six Canonical Gist IDs

| Document | Gist ID | Used In |
|----------|---------|---------|
| Proposal (35 domains) | `2dec7fd03b08ab5b41c55d402f44c261` | All template files |
| Executive Summary | `2869da6eaeb15a47246ade3bbbc4a3f4` | All template files |
| Litigation Tracker | `418d51bda087f15a04d685ab171a5ee0` | Institutional emails, Reddit/law |
| First Amendment Tracker | `10d0a86e386e6c3c11c3830295a6503c` | Institutional emails |
| Environmental Rollbacks | `87e2bdb931b77480e56a08044c567bc4` | Institutional emails |
| Police Consent Decrees | `1f5cb28527c98d12526c14302c725731` | Institutional emails |

Domain 37 Gist ID: PENDING (record here after creation)
Domain 37 Gist ID: `______________________________`

---

*Created May 6, 2026. The six canonical Gists are live (Session 678). This guide*
*covers API operations for new Gists and updates to existing ones.*
