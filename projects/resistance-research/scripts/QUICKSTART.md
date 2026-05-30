# Adoption Tracking — Quick Start

## 3-Minute Setup

### 1. Install Dependencies

```bash
pip3 install requests
```

### 2. Initialize Data Files

```bash
python3 phase-1-adoption-tracking.py --init-csv
```

### 3. Run Test Collection

```bash
python3 phase-1-adoption-tracking.py --run-now
```

### 4. Schedule Weekly Runs

```bash
python3 phase-1-adoption-tracking.py --schedule-weekly
crontab -e
# Paste the suggested line and save
```

## Done!

The script now runs automatically every Monday at 08:00 AM. View summaries in:
```
monitoring/adoption-summary-YYYY-MM-DD.md
```

---

## Manual Email Monitoring (Optional)

If you don't have Gmail API credentials, manually log replies:

1. Copy template: `cp data/email-replies-template.csv data/email-replies-manual.csv`
2. Edit the CSV file each Monday with new replies
3. Create config file:

```json
{
  "github_username": "your-username",
  "gmail_manual_log": "data/email-replies-manual.csv"
}
```

---

## Full Setup

See `ADOPTION_TRACKING_DEPLOYMENT_GUIDE.md` for complete configuration options including Gmail API and Google Sheets integration.
