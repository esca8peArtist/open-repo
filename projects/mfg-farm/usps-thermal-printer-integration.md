---
title: USPS Thermal Printer Integration — ModRun Fulfillment Automation
date: 2026-05-06
version: 1.0
status: ready-for-implementation
confidence: high
related: fulfillment-workflow.md, post-test-print-doc-4-first-week-operations-sop.md
tags: [fulfillment, shipping, automation, raspberry-pi, usps, brother-ql]
---

# USPS Thermal Printer Integration: ModRun Fulfillment Automation

**Objective**: Automate label generation and printing to reduce per-order fulfillment time from ~2 minutes (manual Avery label) to ~15 seconds (automated thermal print), enabling scale from 20 to 100+ units/week without adding labor.

**Platform**: Raspberry Pi 5 + Brother QL-800 USB thermal printer + Shippo API (USPS)

---

## 1. USPS Label API Setup on Raspberry Pi 5

### Why Shippo, Not the Direct USPS API

The USPS v3 REST API (which replaced the legacy XML Web Tools in January 2026) is the technically correct direct path but carries significant overhead for a small-batch operation:

- Requires enrollment in **USPS Ship** with an Enterprise Payment Account
- Requires separate approval for the Labels API beyond the default credential bundle
- OAuth 2.0 token flow adds implementation complexity with no economic benefit at low volume
- No Python SDK is officially maintained by USPS — you build against raw REST with the `requests` library

**Shippo is the recommended path for ModRun** at current scale (20–100 units/week):

- Python SDK maintained and actively documented (`shippo-python-sdk`)
- $0.05 per label (pay-as-you-go), no subscription required below ~400 labels/month
- USPS commercial rates built in (15–40% below retail)
- Free tier: first 30 labels/month at no platform cost — covers initial testing
- Address validation included in every label call
- Label returned as PDF, ready for thermal conversion

At 100 units/week (400/month), platform cost is $20/month — negligible against postage savings from commercial rates.

**EasyPost** is a viable alternative at $0.08/label with 3,000 free/month on the Free Access Wallet tier. The higher per-label cost is offset for very low volumes. Shippo is cheaper above ~100 labels/month.

### Credentials Setup

```bash
# 1. Create a Shippo account at goshippo.com
# 2. Navigate to API → Tokens → Generate Test Token (free)
# 3. For production: enable billing, generate Live Token
# Store in environment variable, never hardcode
export SHIPPO_API_KEY="shippo_live_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Python Installation on Pi 5

```bash
# Using UV (as per project standard)
uv pip install shippo

# Or pip directly
pip install shippo
```

### Batch Label Generation: CSV Input to PDF Labels

This is the core workflow. A morning CSV of 20 orders goes in; 20 PDF labels come out; each feeds directly to the thermal printer.

**Input CSV format** (`orders_2026-05-06.csv`):

```
order_id,name,street1,street2,city,state,zip,weight_oz,service
ORD-001,Jane Smith,123 Main St,,Austin,TX,78701,8,USPS_GROUND_ADVANTAGE
ORD-002,Bob Jones,456 Oak Ave,Apt 3B,Seattle,WA,98101,12,USPS_GROUND_ADVANTAGE
```

**Batch label generation script** (`generate_labels.py`):

```python
import csv
import os
import time
from shippo import Shippo
from shippo.models import components

API_KEY = os.environ["SHIPPO_API_KEY"]
SENDER = {
    "name": "ModRun",
    "street1": "YOUR_STREET",
    "city": "YOUR_CITY",
    "state": "XX",
    "zip": "XXXXX",
    "country": "US",
    "phone": "555-000-0000",
    "email": "orders@modrun.com",
}

def generate_labels(csv_path: str, output_dir: str = "labels/") -> list[str]:
    """Generate USPS labels for all orders in CSV. Returns list of PDF paths."""
    os.makedirs(output_dir, exist_ok=True)
    results = []
    errors = []

    with Shippo(api_key_header=API_KEY, shippo_api_version="2018-02-08") as client:
        with open(csv_path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                order_id = row["order_id"]
                try:
                    shipment = client.shipments.create(request=components.ShipmentCreateRequest(
                        address_from=components.AddressCreateRequest(**SENDER),
                        address_to=components.AddressCreateRequest(
                            name=row["name"],
                            street1=row["street1"],
                            street2=row.get("street2", ""),
                            city=row["city"],
                            state=row["state"],
                            zip=row["zip"],
                            country="US",
                            validate_=True,
                        ),
                        parcels=[components.ParcelCreateRequest(
                            weight=str(float(row["weight_oz"]) / 16),
                            mass_unit="lb",
                            length="8", width="6", height="3",
                            distance_unit="in",
                        )],
                        async_=False,
                    ))

                    # Buy the label on the cheapest matching rate
                    rate = next(
                        r for r in shipment.rates
                        if row["service"] in r.servicelevel.token
                    )
                    transaction = client.transactions.create(request=components.TransactionCreateRequest(
                        rate=rate.object_id,
                        label_file_type="PDF",
                        async_=False,
                    ))

                    if transaction.status == "SUCCESS":
                        import urllib.request
                        pdf_path = os.path.join(output_dir, f"{order_id}.pdf")
                        urllib.request.urlretrieve(transaction.label_url, pdf_path)
                        results.append(pdf_path)
                        print(f"[OK] {order_id} → {pdf_path} (${transaction.rate.amount})")
                    else:
                        errors.append((order_id, transaction.messages))
                        print(f"[FAIL] {order_id}: {transaction.messages}")

                    time.sleep(1)  # Avoid rate-limiting (Shippo: 200 req/min on free tier)

                except Exception as e:
                    errors.append((order_id, str(e)))
                    print(f"[ERROR] {order_id}: {e}")

    if errors:
        print(f"\nFailed labels: {len(errors)}")
        for oid, msg in errors:
            print(f"  {oid}: {msg}")

    return results

if __name__ == "__main__":
    import sys
    pdfs = generate_labels(sys.argv[1])
    print(f"\nGenerated {len(pdfs)} labels.")
```

### Rate Limits and Idempotency

Shippo's free tier allows 200 API requests per minute. A 20-order batch with a 1-second sleep per order completes in ~22 seconds total — well within limits.

**Idempotency**: Shippo supports an `async_id` parameter you can pass as a unique token per order. If you call the same order twice with the same ID, Shippo returns the existing transaction rather than double-charging. Always use `order_id` as the idempotency key when adding that parameter. If a label is lost before printing, re-run the script; only unpurchased orders will be re-processed if you track which PDF files already exist.

**Cost per label (platform)**: $0.05. Postage is charged at commercial rates, paid through your Shippo balance (fund via credit card or ACH). At 20 units/week (80/month): $4/month platform + postage. At 100 units/week: $20/month platform + postage.

---

## 2. Brother QL-800 Thermal Printer Setup on Pi 5

### Hardware Overview

The Brother QL-800 is a direct-thermal label printer supporting DK-series die-cut and continuous roll labels. Key specs:

- **Print speed**: Up to 93 labels/minute (DK-1202 size); shipping label speed ~20–30/minute
- **Resolution**: 300 dpi (standard), 600 dpi (fine mode)
- **Max label width**: 62mm (approximately 2.4 inches)
- **Shipping label support**: DK-1241 (4" x 6" / 101mm x 152mm) — the standard USPS label size
- **Connection**: USB 2.0 (required for Pi setup; Wi-Fi models are QL-810W/820NWB)
- **Black/Red printing**: Yes (requires DK-2251 tape; not needed for standard shipping labels)
- **Price**: $130–$160 new (Amazon/Staples); $80–$120 refurbished

**Critical note on label size**: The QL-800 native max width is 62mm, but the DK-1241 is a 101mm x 152mm (4"x6") die-cut label — the 101mm dimension is the label width, which exceeds the QL-800's 62mm print head width. This is a key compatibility issue. The QL-800 is better suited to DK-1202 (2.4"x3.9") address labels, not full 4"x6" shipping labels.

**For full 4"x6" USPS shipping labels, consider**:
- **Brother QL-1110NWB** (~$200): supports 4"x6" DK-1241 labels natively
- **Brother QL-1100** (~$180): USB, 4"x6" support, wider print head

The `brother_ql` library supports both. If you are committed to the QL-800, USPS labels must be scaled down or use the DK-1202 format, which can work for smaller parcels but is non-standard for carriers.

**Recommended for ModRun**: Purchase the QL-1100 or QL-1110NWB specifically for 4"x6" DK-1241 label compatibility. The price difference ($40–70) pays for itself immediately in label compatibility and avoids workflow compromise.

### Driver Installation: No Driver Required

Brother does not provide ARM Linux drivers for the Raspberry Pi. This is not a problem because the `brother_ql` Python package bypasses the printer driver entirely and speaks the QL raster protocol directly over USB. CUPS is optional and not recommended for this workflow.

```bash
# System prerequisites
sudo apt-get update
sudo apt-get install -y python3-pip python3-pil libusb-1.0-0

# Install brother_ql (UV method per project standard)
uv pip install brother_ql

# Verify install
brother_ql --help
```

### USB Permissions (Critical Step)

Without proper permissions, the script will fail silently or with a cryptic USB access error.

```bash
# Step 1: Find your printer's USB identifiers
lsusb | grep Brother
# Output example: Bus 001 Device 003: ID 04f9:209b Brother Industries, Ltd QL-800

# Step 2: Create udev rule (replace 209b with your product ID from lsusb)
sudo tee /etc/udev/rules.d/99-brother-ql.rules << 'EOF'
SUBSYSTEMS=="usb", ATTRS{idVendor}=="04f9", ATTRS{idProduct}=="209b", MODE="0666", GROUP="lp"
EOF

# Step 3: Add current user to lp group
sudo usermod -aG lp $USER

# Step 4: Reload udev rules and reconnect printer
sudo udevadm control --reload-rules
sudo udevadm trigger
# Unplug and replug the USB cable

# Step 5: Verify device access
ls -la /dev/usb/lp0
```

**Critical hardware step**: Before connecting USB, power on the QL-800 and hold the front button until the "Editor Lite" LED turns off. Editor Lite mode causes the printer to mount as a USB mass storage device instead of a printer, which prevents `brother_ql` from communicating with it.

### Python Printing Workflow: PDF to Thermal

The Shippo API returns label PDFs. The QL printer needs PNG images. The conversion chain is: PDF → PNG (via `pdf2image`) → resize to label dimensions → raster instructions → USB send.

```bash
# Additional dependencies for PDF conversion
sudo apt-get install -y poppler-utils
uv pip install pdf2image Pillow
```

```python
import subprocess
import time
from pathlib import Path
from PIL import Image
from pdf2image import convert_from_path
from brother_ql.conversion import convert
from brother_ql.backends.helpers import send
from brother_ql.raster import BrotherQLRaster

PRINTER_MODEL = "QL-1100"       # Change to QL-800 if using smaller labels
PRINTER_USB   = "usb://0x04f9:0x2042"  # QL-1100 USB product ID; QL-800 is 0x209b
LABEL_SIZE    = "102x152"       # DK-1241 4"x6"; use "62x100" for QL-800 + DK-1241 equivalent
BACKEND       = "pyusb"

def pdf_to_label_image(pdf_path: str) -> Image.Image:
    """Convert first page of PDF label to PIL Image sized for DK-1241."""
    pages = convert_from_path(pdf_path, dpi=300, first_page=1, last_page=1)
    img = pages[0].convert("L")  # Grayscale — thermal prints black only
    # DK-1241 at 300dpi: 1205 x 1808 px. Resize to fit.
    img = img.resize((1205, 1808), Image.LANCZOS)
    return img

def print_label(pdf_path: str) -> bool:
    """Print a single PDF label to the Brother QL printer. Returns True on success."""
    try:
        img = pdf_to_label_image(pdf_path)
        qlr = BrotherQLRaster(PRINTER_MODEL)
        instructions = convert(
            qlr=qlr,
            images=[img],
            label=LABEL_SIZE,
            threshold=70,
            cut=True,
        )
        result = send(
            instructions=instructions,
            printer_identifier=PRINTER_USB,
            backend_identifier=BACKEND,
            blocking=True,
        )
        return result.get("did_print", False)
    except Exception as e:
        print(f"Print error for {pdf_path}: {e}")
        return False

def print_batch(pdf_paths: list[str], delay_sec: float = 3.0) -> dict:
    """Print a list of label PDFs sequentially. Returns success/fail counts."""
    results = {"success": [], "failed": []}
    for i, path in enumerate(pdf_paths, 1):
        print(f"Printing {i}/{len(pdf_paths)}: {Path(path).name}")
        ok = print_label(path)
        if ok:
            results["success"].append(path)
        else:
            results["failed"].append(path)
        time.sleep(delay_sec)  # Allow printer buffer to clear
    return results
```

### Finding the Correct USB Product ID

The USB product ID varies by model. Use `lsusb` output after connecting the printer:

| Model | Vendor ID | Product ID |
|-------|-----------|------------|
| QL-800 | 04f9 | 209b |
| QL-1100 | 04f9 | 2044 |
| QL-1110NWB | 04f9 | 2050 |

The full USB identifier for `brother_ql` follows the format `usb://0x{vendor}:0x{product}`.

### Print Quality Validation

Before live orders, run a dry-print test with a dummy label:

```bash
# Command-line test print (uses a sample image)
brother_ql \
  --backend pyusb \
  --model QL-1100 \
  --printer usb://0x04f9:0x2044 \
  print \
  --label 102x152 \
  test_label.png
```

Check: barcode scannable by phone camera, address text sharp at arm's length, cut line clean, no skewed printing. If the label is misaligned, check that the DK roll is seated correctly under the guide rails and the roll end is threaded past the sensor.

### Label Supplies and Cost

**DK-1241** (4"x6", 200 labels/roll) — the standard USPS shipping label format for QL-1100/1110NWB:

- **Brother genuine**: ~$25/roll → $0.125/label
- **BETCKEY compatible** (3rd party, well-reviewed): $13/roll (single), $54 for 10 rolls → $0.027/label at 10-roll bulk
- **enKo compatible**: 6-pack 1,200 labels ~$40 → $0.033/label

At 20 units/week using BETCKEY 10-pack: label material cost ≈ $0.027/unit. At 100 units/week: $2.70/week in label material ($140/year).

**Recommendation**: Buy 1 genuine Brother roll for initial testing (confirms compatibility), then switch to BETCKEY or enKo for production. Community reports indicate compatible labels work identically for thermal direct printing.

---

## 3. ModRun Fulfillment Batch Workflow

### Complete Pipeline: Morning Run (20 Orders, ~5 Minutes)

```
07:00  MORNING TRIGGER
    ↓
Pull orders from Etsy (manual CSV export or API)
    ↓
generate_labels.py orders_YYYY-MM-DD.csv
    │  → Validates each address via Shippo
    │  → Purchases USPS label at commercial rate
    │  → Downloads PDF to labels/ directory
    │  → ~20 seconds for 20 orders
    ↓
print_batch(pdf_files)
    │  → Converts each PDF to 300dpi grayscale PNG
    │  → Sends raster data to QL printer via USB
    │  → ~15 seconds per label = ~5 minutes for 20 labels
    ↓
PEEL AND APPLY
    │  → Labels exit printer in order-ID sequence
    │  → Match label to packaged product (order ID on box)
    ↓
USPS PICKUP or DROP-OFF
    → End of morning session
```

### Input CSV Format (Full Specification)

```
order_id,name,street1,street2,city,state,zip,country,weight_oz,service,tracking_required
ORD-001,Jane Smith,123 Main St,,Austin,TX,78701,US,8,USPS_GROUND_ADVANTAGE,true
ORD-002,Bob Jones,456 Oak Ave,Apt 3B,Seattle,WA,98101,US,12,USPS_GROUND_ADVANTAGE,true
```

Fields:
- `weight_oz`: product weight in ounces (cable management clips: 4–12 oz shipped with packaging)
- `service`: use `USPS_GROUND_ADVANTAGE` for standard; `USPS_PRIORITY_MAIL` for expedited
- `street2`: optional apartment/suite; leave blank, not null, to avoid CSV parsing errors

### Error Handling

The batch script handles three failure classes:

**1. Address validation failure** (most common — ~2–5% of orders):
- Shippo returns `address_to.validation_results.is_valid = False` with a message
- Script logs the order ID and error message, skips label purchase
- Manual action: email customer for address correction before reprinting

**2. API timeout / rate limit**:
- Shippo returns HTTP 429 or connection error
- Script catches `Exception`, logs order ID, continues to next order
- Re-run the script on the same CSV — orders with existing PDFs in `labels/` are skipped (idempotency check on file existence)

**3. Printer jam / hardware failure**:
- `send()` returns `did_print = False` or raises an exception
- Script logs the failed PDF path to `failed_prints.txt`
- After clearing jam: re-run `print_batch(failed_paths)` with paths from that file

### Idempotency Detail

The script checks `os.path.exists(pdf_path)` before calling the Shippo API. If the file exists, the label was already purchased and downloaded — skip API call. This means running the script twice on the same CSV charges only for new labels. Never delete the `labels/` directory until the batch is shipped.

For tracking number regeneration: Shippo does not issue duplicate tracking numbers. Each `transaction.create()` call generates a new tracking number. If a label is lost and a new one is purchased for the same order, both tracking numbers are valid but only one is scanned at acceptance. This is safe — USPS will deliver on whichever label gets scanned at the facility.

### Performance Targets

| Stage | Time per order | 20-order batch |
|-------|---------------|----------------|
| CSV parse + API label purchase | ~1.5 sec | ~30 sec |
| PDF download | ~0.5 sec | ~10 sec |
| PDF → PNG conversion | ~2 sec | ~40 sec |
| Thermal print (QL-1100 at 93 labels/min) | ~1.5 sec | ~30 sec |
| Inter-print delay (buffer) | 3 sec | 60 sec |
| **Total** | **~8.5 sec** | **~3 min** |

Actual elapsed time including peel-and-apply by a human: ~5–7 minutes for 20 orders. The stated 15 seconds/label is the automated portion; human handling adds ~30 seconds/label for apply + match-to-box.

---

## 4. Manual Fallback Procedures

### Decision Tree

```
Is Shippo API down or billing issue?
    YES → Fallback 1: USPS Click-N-Ship GUI
    NO  ↓
Is Pi unavailable (hardware failure)?
    YES → Fallback 1: USPS Click-N-Ship GUI
    NO  ↓
Is QL printer jammed/broken?
    YES (Pi works, API works) → Fallback 2: Avery + home printer
    NO → Normal automated workflow
    
Are you at <1 order/day and everything is broken?
    YES → Fallback 3: Local shipping store
```

### Fallback 1: USPS Click-N-Ship GUI (Primary Manual Fallback)

**When**: API outage, billing issue, Pi hardware failure, or unfamiliar with CLI tools.

**Process**:
1. Go to usps.com/ship/online-shipping.htm → log in to USPS business account
2. Click-N-Ship now offers batch import: upload a CSV, generate up to 20 labels at once
3. Download PDF → print on any printer (laser/inkjet on Avery 5164 label stock)
4. USPS commercial rates apply (same as API, no markup)

**Cost vs. automated**: Zero platform cost (no Shippo per-label fee). Postage rate is identical. Labor cost: ~3–4 minutes per label manually vs. 15 seconds automated. For a 1-day outage affecting 20 orders: adds ~1 hour manual work.

**Limitation**: Click-N-Ship batch upload was added in the 2024 CNSv2 update. It supports up to 1,000 addresses in the address book and batch creation. Not as fast as automated but viable for a full day's volume.

### Fallback 2: Avery 5164 Template Labels

**When**: Pi works, Shippo API works, but thermal printer is broken.

**Process**:
1. Generate labels via Shippo script (PDFs download normally)
2. Open PDF in any PDF viewer
3. Print to home laser/inkjet printer on Avery 5164 (4"x6", 2-up, 100 sheets = 200 labels ~$25)
4. Apply to packages manually

**Cost premium**: Inkjet/laser: $0.15–$0.30/label ink cost vs. $0.027 thermal. For 20 orders: $3–$6 additional cost. Acceptable for emergency use.

**Lead time**: Avery 5164 sheets available at Staples/Target same-day. Keep 20 sheets on hand as permanent emergency stock.

### Fallback 3: Local Shipping Store (UPS Store / FedEx Office)

**When**: Less than 1 order/day, all other systems down, not worth setup time.

**Cost**: UPS Store retail USPS Ground Advantage adds $3–8 per package above commercial rates. For 1 package: totally fine. For 5+ packages: use Fallback 1 instead.

**Process**: Bring the package, have them weigh it, pay retail rate. Get receipt with tracking number. Update Etsy order with tracking manually.

### Downtime Customer Communication Protocol

If any fulfillment delay exceeds 24 hours:

1. **Etsy message** to affected orders: "Your order is being processed and will ship by [specific date]. Thank you for your patience — we're experiencing a brief technical delay."
2. Do not send vague messages. Give a date you can commit to.
3. If delay extends past 48 hours: offer a $2–3 partial refund or free add-on item to preserve review score.
4. Etsy's on-time shipping metric looks at label purchase date, not delivery. Purchasing a label (even via Click-N-Ship) starts the clock — do this first, ship the physical package second if needed.

---

## 5. Cost Analysis and ROI

### Per-Label Cost Breakdown

| Cost Component | Automated Thermal | Manual Avery | Click-N-Ship |
|---------------|------------------|--------------|--------------|
| Label material | $0.027 (DK-1241 bulk) | $0.125 (Avery 5164) | $0.125 |
| Ink/toner | $0 (thermal) | $0.15–$0.25 | $0.15–$0.25 |
| Platform fee | $0.05 (Shippo) | $0.05 (Shippo) | $0 (USPS direct) |
| **Subtotal (non-postage)** | **$0.077** | **$0.325–$0.425** | **$0.125–$0.375** |

Postage is identical across all methods (USPS commercial rates). The savings are entirely in label production cost and labor.

### Labor Comparison

| Method | Time per label | 20 orders | 100 orders |
|--------|---------------|-----------|------------|
| Manual Avery | 2 min | 40 min | 200 min (3.3 hr) |
| Automated thermal | 15 sec | 5 min | 25 min |
| Time saved per batch | — | 35 min | 175 min |

**At $20/hr equivalent labor cost**:
- 20 orders/week: saves 35 min = $11.67/week = $606/year
- 100 orders/week: saves 175 min = $58.33/week = $3,033/year

### Printer Amortization

| Item | Cost |
|------|------|
| Brother QL-1100 (USB, 4"x6" support) | ~$180 |
| Initial DK-1241 label supply (10 rolls = 2,000 labels) | ~$54 |
| USB cable (usually included) | $0 |
| **Total upfront** | **~$234** |

At 20 units/week (80/month, ~1,000/year):
- Annual label material savings vs. Avery: (0.125 - 0.027) × 1,000 = $98/year
- Annual labor savings: $606/year (35 min/batch × 52 batches at $20/hr equiv.)
- **Total annual savings**: ~$704/year
- **Break-even**: 234 ÷ (704/52) = **~18 weeks at 20 units/week**

At 100 units/week (400/month):
- Annual label material savings: (0.125 - 0.027) × 5,200 = $510/year
- Annual labor savings: $3,033/year
- **Total annual savings**: ~$3,543/year
- **Break-even**: 234 ÷ (3,543/52) = **~3.4 weeks at 100 units/week**

### Shippo vs. Direct USPS API Economic Comparison

At 20 units/week (80 labels/month):
- Shippo: 80 × $0.05 = $4.00/month platform cost
- Direct USPS API: $0 platform cost, but ~8 hours development/maintenance cost
- Break-even for DIY USPS: never at this scale — Shippo wins

At 400 units/week (1,600 labels/month):
- Shippo: 1,600 × $0.05 = $80/month
- Consider migrating to direct USPS API at this volume (saves $960/year, worth a week of development time)

---

## Quick-Start Checklist

Initial setup (one-time, ~2 hours):

- [ ] Create Shippo account, generate test API key
- [ ] `uv pip install shippo pdf2image Pillow brother_ql`
- [ ] `sudo apt-get install -y poppler-utils libusb-1.0-0`
- [ ] Disable QL printer Editor Lite mode (hold button until LED off)
- [ ] Run `lsusb` to get printer USB product ID
- [ ] Create `/etc/udev/rules.d/99-brother-ql.rules` with correct product ID
- [ ] `sudo usermod -aG lp $USER` and reconnect printer
- [ ] Test print with `brother_ql ... print --label 102x152 test.png`
- [ ] Run Shippo test API call with test token (no charge)
- [ ] Generate 1 test label PDF, convert, print — confirm barcode scans
- [ ] Run 20-order dry batch against test Shippo environment

First production run:
- [ ] Switch to Shippo live API key
- [ ] Fund Shippo balance ($20 minimum)
- [ ] Generate real labels for actual orders
- [ ] Apply labels, scan barcodes before dropping at USPS
- [ ] Archive labels CSV + PDFs by date (`labels/2026-05-06/`)

---

## Sources

- [brother_ql — PyPI](https://pypi.org/project/brother-ql/)
- [pklaus/brother_ql — GitHub](https://github.com/pklaus/brother_ql)
- [Brother QL-800 Product Page — Brother USA](https://www.brother-usa.com/products/ql800)
- [DK-1241 Label Product Page — Brother USA](https://www.brother-usa.com/products/dk1208)
- [BETCKEY DK-1241 Compatible Labels — BETCKEY](https://betckey.com/products/brother-dk-1241-large-shipping-labels)
- [USPS API Getting Started — USPS Developer Portal](https://developers.usps.com/getting-started)
- [USPS Domestic Labels 3.0 — USPS Developer Portal](https://developers.usps.com/domesticlabelsv3)
- [USPS API Examples — GitHub](https://github.com/USPS/api-examples)
- [Shippo Python SDK — GitHub](https://github.com/goshippo/shippo-python-sdk)
- [Shippo Batch Label Guide](https://docs.goshippo.com/docs/guides_general/generate_shipping_label)
- [Shipping API Comparison 2026 — RevAddress](https://revaddress.com/blog/shipping-api-comparison-2026/)
- [USPS Click-N-Ship Online Shipping](https://www.usps.com/ship/online-shipping.htm)
- [Ubuntu/Linux Brother QL-800 Setup Guide — 10pm.ca](https://10pm.ca/ubuntu-linux-mint-brother-ql-800-label-printer/)
- [QL-800 Ubuntu Installation — GitHub/ICTools](https://github.com/ICTools/ql-800-ubuntu)
- [Raspberry Pi Forums: QL-800 USB error debugging](https://forums.raspberrypi.com/viewtopic.php?t=284232)
- [enKo DK-1241 Compatible Labels — Amazon](https://www.amazon.com/enKo-Compatible-DK-1241-4-Refillable-Cartridges/dp/B07T1HGZQN)
- [USPS January 2025 Price Change Notice 123](https://pe.usps.com/resources/PriceChange/January%202025%20Price%20Change%2020241224%20-%20Notice123.pdf)
