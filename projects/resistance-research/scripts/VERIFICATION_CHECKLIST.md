# Phase 1 Adoption Tracking — Verification Checklist

**Deadline:** May 31, 2026 23:59 UTC (tomorrow)

Use this checklist to verify the adoption tracking system is production-ready before June 1 08:00 UTC distribution.

---

## Installation Verification (5 minutes)

- [ ] **Python 3.10+ installed**
  ```bash
  python3 --version
  # Should show: Python 3.10.x or higher
  ```

- [ ] **Script is executable**
  ```bash
  ls -la phase-1-adoption-tracking.py
  # Should show: -rwxr-xr-x or similar
  ```

- [ ] **Script syntax is valid**
  ```bash
  python3 -m py_compile phase-1-adoption-tracking.py
  # Should complete without errors
  ```

- [ ] **Help text displays**
  ```bash
  python3 phase-1-adoption-tracking.py --help
  # Should show usage options
  ```

---

## Configuration Verification (5 minutes)

- [ ] **Config file exists**
  ```bash
  ls -la phase-1-adoption-tracking.json
  ```

- [ ] **Config file is valid JSON**
  ```bash
  python3 -c "import json; json.load(open('phase-1-adoption-tracking.json'))"
  # Should complete without errors
  ```

- [ ] **GitHub username is set**
  ```bash
  grep github_username phase-1-adoption-tracking.json
  # Should show a non-empty username
  ```

- [ ] **CSV paths are accessible**
  ```bash
  ls -la data/gist-views.csv
  # Should show the file exists
  ```

---

## Data Files Verification (3 minutes)

- [ ] **Gist views CSV initialized**
  ```bash
  head -1 data/gist-views.csv
  # Should show: timestamp,gist_label,gist_id,...
  ```

- [ ] **Log directory exists**
  ```bash
  ls -ld logs/
  # Should show: drwxr-xr-x or similar
  ```

- [ ] **Monitoring directory exists**
  ```bash
  ls -ld monitoring/
  # Should show: drwxr-xr-x or similar
  ```

---

## Functional Verification (10 minutes)

### Test 1: Initialize CSV

```bash
python3 phase-1-adoption-tracking.py --init-csv
```

Expected output:
```
2026-05-30 21:22:35 [INFO] Initializing CSV data files...
2026-05-30 21:22:35 [INFO] Created Gist tracking CSV: .../gist-views.csv
2026-05-30 21:22:35 [INFO] CSV initialization complete
```

- [ ] Command completes without errors
- [ ] No exceptions in output
- [ ] Log file updated: `tail logs/adoption-tracking.log`

### Test 2: Run Collection

```bash
timeout 30 python3 phase-1-adoption-tracking.py --run-now
```

Expected output:
```
======================================================================
PHASE 1 ADOPTION TRACKING — Weekly Collection
======================================================================
[1/3] Fetching Gist view counts...
[2/3] Fetching recent email replies...
[3/3] Checking leading-indicator alerts...

Weekly collection complete
  Gists tracked: 4
  Email replies: 0
  Alerts triggered: 0 or 1 (ZERO_REPLIES expected)
======================================================================
```

- [ ] Command completes (no infinite loop)
- [ ] Both email and Gist collection attempted
- [ ] Summary saved to file
- [ ] No unhandled exceptions

### Test 3: Check Output Files

```bash
ls -la monitoring/adoption-summary-*.md
```

- [ ] Summary file was created
- [ ] File is readable
- [ ] Contains Gist View Counts section
- [ ] Contains Email Replies section

### Test 4: Verify CSV Updated

```bash
wc -l data/gist-views.csv
```

- [ ] File has at least 2 lines (header + 1 data row)
- [ ] Can parse with: `python3 -c "import csv; list(csv.DictReader(open('data/gist-views.csv')))"`

---

## Scheduling Verification (5 minutes)

### Test 1: View Cron Entry

```bash
python3 phase-1-adoption-tracking.py --schedule-weekly
```

- [ ] Output shows valid cron command
- [ ] Path is absolute (starts with `/`)
- [ ] Includes `--run-now` flag

### Test 2: Add to Crontab (if first time)

```bash
python3 phase-1-adoption-tracking.py --schedule-weekly | grep "^0 8" | xargs crontab -e
```

Or manually:
```bash
crontab -e
# Paste the line from --schedule-weekly output
```

### Test 3: Verify Cron Installation

```bash
crontab -l | grep adoption-tracking
```

- [ ] Output shows the cron entry
- [ ] Entry includes absolute path to script
- [ ] Entry includes `--run-now` flag
- [ ] Time is correct (0 8 * * 1 = Monday 08:00 AM)

### Test 4: Verify Cron Syntax

```bash
crontab -l | python3 -c "
import sys
for line in sys.stdin:
    if 'adoption-tracking' not in line:
        continue
    parts = line.split()
    if len(parts) >= 5:
        print('✓ Cron syntax appears valid')
    else:
        print('✗ Cron syntax may be invalid')
"
```

---

## Log File Verification (3 minutes)

```bash
tail -50 logs/adoption-tracking.log
```

- [ ] File contains INFO and ERROR messages
- [ ] Most recent entry is from today
- [ ] No "Traceback" or uncaught exceptions
- [ ] File is writable: `touch logs/adoption-tracking.log`

---

## Email Monitoring Verification (5 minutes, if using manual log)

### If using manual email log:

- [ ] Template file exists: `data/email-replies-template.csv`
- [ ] Template has correct columns: `date,from_email,from_name,subject,snippet,reply_type`
- [ ] Can parse with: `python3 -c "import csv; list(csv.DictReader(open('data/email-replies-template.csv')))"`

### If using Gmail API:

- [ ] Credentials file exists: `path-in-config.json`
- [ ] File is readable and valid JSON: `python3 -c "import json; json.load(open('path'))"`
- [ ] Config points to credentials: `grep gmail_credentials phase-1-adoption-tracking.json`

---

## Dashboard Integration Verification (5 minutes, optional)

If configured for Google Sheets:

- [ ] Sheets credentials exist and are valid JSON
- [ ] Spreadsheet ID is in config: `grep spreadsheet_id phase-1-adoption-tracking.json`
- [ ] Test sync by running: `python3 phase-1-adoption-tracking.py --run-now`
- [ ] Check dashboard for updated values

---

## Full System Test (15 minutes total)

Run this complete test sequence:

```bash
# 1. Clean and reinitialize
rm -f data/gist-views.csv monitoring/adoption-summary-*.md
python3 phase-1-adoption-tracking.py --init-csv

# 2. Run collection
python3 phase-1-adoption-tracking.py --run-now

# 3. Check results
echo "=== CSV Data ===" && wc -l data/gist-views.csv
echo "=== Summary File ===" && ls -lh monitoring/adoption-summary-*.md
echo "=== Log Entry ===" && tail -20 logs/adoption-tracking.log

# 4. Verify cron is scheduled
echo "=== Cron Status ===" && crontab -l | grep adoption-tracking
```

**All checks should pass with no errors.**

---

## Critical Checks (Must Pass Before 23:59 UTC May 31)

| Check | Status | Command |
|-------|--------|---------|
| Python 3.10+ | [ ] | `python3 --version` |
| Script syntax | [ ] | `python3 -m py_compile phase-1-adoption-tracking.py` |
| Config file valid | [ ] | `python3 -c "import json; json.load(open('phase-1-adoption-tracking.json'))"` |
| Test run succeeds | [ ] | `python3 phase-1-adoption-tracking.py --run-now` |
| Summary created | [ ] | `ls monitoring/adoption-summary-*.md` |
| Cron scheduled | [ ] | `crontab -l \| grep adoption-tracking` |

**All 6 critical checks must show [ X ] before June 1.**

---

## Issue Resolution Guide

### If any check FAILS:

1. **Note the failure:** Which step failed and what was the error?
2. **Check logs:** `tail -100 logs/adoption-tracking.log`
3. **Review config:** `cat phase-1-adoption-tracking.json`
4. **Test dependencies:** `python3 -c "import requests; print('✓')"`
5. **Consult documentation:**
   - Syntax errors → See ADOPTION_TRACKING_DEPLOYMENT_GUIDE.md § Troubleshooting
   - Config issues → See phase-1-adoption-tracking.json.example
   - Scheduling issues → Run `--schedule-weekly` again and manually verify crontab

### Common Issues & Fixes

| Issue | Root Cause | Fix |
|-------|-----------|-----|
| "ModuleNotFoundError: requests" | Dependencies not installed | `pip3 install requests` |
| "Gist analytics 404 error" | Wrong GitHub username | Update `github_username` in config |
| "Cron not running" | Cron service not active | `sudo systemctl start cron` |
| "Permission denied on CSV" | Incorrect permissions | `chmod 644 data/*.csv` |
| "Config file not found" | Path doesn't match | Check config path in command |

---

## Sign-Off

Date: ________________

Verified by: ________________

All critical checks passed: [ ] Yes  [ ] No

Status for June 1 execution:

- [ ] Ready — All checks passed, script scheduled and working
- [ ] Partial — Some checks failed; see resolution needed below
- [ ] Not ready — Major issues remain

Notes/Issues:

```
(Add any issues found during verification)




```

---

## Next: June 1 Morning (06:00 UTC)

1. Wake up the system (if Jetson Pi was powered down)
2. Verify cron is still scheduled: `crontab -l | grep adoption-tracking`
3. Check that script ran automatically: `ls -la monitoring/adoption-summary-*.md`
4. If any issues, debug and re-run: `python3 phase-1-adoption-tracking.py --run-now`
5. Proceed with Phase 1 distribution (08:00 UTC wave launch)

---

*This checklist ensures June 1 adoption tracking deployment is production-ready.*
