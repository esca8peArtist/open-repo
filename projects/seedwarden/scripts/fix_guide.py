"""
fix_guide.py — One-pass fixer for native-plants-regional-guide.md

Applies:
1. Page breaks before every ### heading
2. Fixes wrong Pickerelweed image (crinum-americanum.jpg → pontederia-cordata.jpg)
3. Moves misplaced Ribes/Currant image to after its ### header
4. Adds missing images for entries where image files exist
5. Reports remaining issues (no image file available, cross-references)
"""

import re
from pathlib import Path

GUIDE = Path(__file__).parent.parent / "products" / "native-plants-regional-guide.md"
IMG_DIR = Path(__file__).parent / "images" / "native-plants"
IMG_REL = "images/native-plants"
PAGE_BREAK = '<div style="page-break-before: always"></div>\n\n'

text = GUIDE.read_text(encoding="utf-8")
lines = text.splitlines(keepends=True)

# ── 1. Fix wrong Pickerelweed image ────────────────────────────────────────
text = text.replace(
    "![Pickerelweed (Pontederia cordata) — arrow-shaped leaves and blue-violet flower spikes in wetland](images/native-plants/crinum-americanum.jpg)",
    "![Pickerelweed (Pontederia cordata) — arrow-shaped leaves and blue-violet flower spikes in wetland](images/native-plants/pontederia-cordata.jpg)",
)

# ── 2. Fix misplaced Ribes image (it appears after Safety, move to header) ─
# Remove the floating image line from its current location
text = text.replace(
    "\n![Wax Currant (Ribes cereum) — small red berries on low shrub](images/native-plants/ribes-cereum.jpg)\n\n**Safety**",
    "\n\n**Safety**",
)
# And ensure the header block has the image right after the scientific name line
text = text.replace(
    "### Gooseberry and Currant\n*Ribes* spp. (*R. inerme*, *R. cereum*, *R. viscosissimum*, *R. aureum*)\n\n**Identification**",
    "### Gooseberry and Currant\n*Ribes* spp. (*R. inerme*, *R. cereum*, *R. viscosissimum*, *R. aureum*)\n\n![Wax Currant (Ribes cereum) — small red berries on low shrub](images/native-plants/ribes-cereum.jpg)\n\n**Identification**",
)

# ── 3. Add missing images where files exist ────────────────────────────────

MISSING_IMAGES = [
    # (anchor string that immediately follows the ### header block, image_md_to_insert)
    # Giant Shaggy Mane — Coprinus comatus
    (
        "### Giant Shaggy Mane\n*Coprinus comatus*\n\n**Identification**",
        "### Giant Shaggy Mane\n*Coprinus comatus*\n\n![Giant Shaggy Mane (Coprinus comatus) — white cylindrical shaggy-scaled cap before ink stage](images/native-plants/coprinus-comatus.jpg)\n\n**Identification**",
    ),
    # Hackberry — Celtis occidentalis
    (
        "### Hackberry\n*Celtis occidentalis* and related species\n\n**Identification**",
        "### Hackberry\n*Celtis occidentalis* and related species\n\n![Hackberry (Celtis occidentalis) — warty corky bark and small orange-purple berries](images/native-plants/celtis-occidentalis.jpg)\n\n**Identification**",
    ),
    # Pacific Crabapple — Malus fusca
    (
        "### Pacific Crabapple\n*Malus fusca*\n\n**Identification**",
        "### Pacific Crabapple\n*Malus fusca*\n\n![Pacific Crabapple (Malus fusca) — tiny apple-like fruit on thorny branches](images/native-plants/malus-fusca.jpg)\n\n**Identification**",
    ),
    # Valley Oak — Quercus lobata
    (
        "### Valley Oak\n*Quercus lobata*\n\n**Identification**",
        "### Valley Oak\n*Quercus lobata*\n\n![Valley Oak (Quercus lobata) — massive spreading canopy and large elongated acorns](images/native-plants/quercus-lobata.jpg)\n\n**Identification**",
    ),
    # Fennel — Foeniculum vulgare
    (
        "### Fennel\n*Foeniculum vulgare*\n\n**Identification**",
        "### Fennel\n*Foeniculum vulgare*\n\n![Fennel (Foeniculum vulgare) — feathery green fronds and flat-topped yellow flower umbel](images/native-plants/foeniculum-vulgare.jpg)\n\n**Identification**",
    ),
    # Meadow Mushroom — no file, add placeholder
    (
        "### Meadow Mushroom\n*Agaricus campestris*\n\n**Identification**",
        "### Meadow Mushroom\n*Agaricus campestris*\n\n*[Photo needed: Agaricus campestris — white-capped mushroom in lawn/meadow with pink gills. Source: iNaturalist CC0.]*\n\n**Identification**",
    ),
    # Mayhaw — no specific file, add placeholder
    (
        "### Mayhaw\n*Crataegus aestivalis / C. opaca*\n\n**Identification**",
        "### Mayhaw\n*Crataegus aestivalis / C. opaca*\n\n*[Photo needed: Crataegus aestivalis — small red spring-ripening haws on thorny branches in Gulf Coast bottomland. Source: iNaturalist CC0.]*\n\n**Identification**",
    ),
    # Oregon White Truffle — no file, add placeholder
    (
        "### Oregon White Truffle\n*Tuber oregonense* and *T. gibbosum*\n\n**Identification**",
        "### Oregon White Truffle\n*Tuber oregonense* and *T. gibbosum*\n\n*[Photo needed: Tuber oregonense — pale white hypogeous truffle with marbled interior, found under Douglas fir. Source: iNaturalist CC0.]*\n\n**Identification**",
    ),
    # Sea Rocket — no file, add placeholder
    (
        "### Sea Rocket\n*Cakile* spp. (*C. edentula*, *C. lanceolata*)\n\n**Identification**",
        "### Sea Rocket\n*Cakile* spp. (*C. edentula*, *C. lanceolata*)\n\n*[Photo needed: Cakile edentula or C. lanceolata — succulent branching coastal annual on sandy beach with four-petaled flowers. Source: iNaturalist CC0.]*\n\n**Identification**",
    ),
]

for old, new in MISSING_IMAGES:
    if old in text:
        text = text.replace(old, new, 1)
    else:
        print(f"WARNING: anchor not found:\n  {old[:80]}")

# ── 4. Add Wild Blueberry entry to Region 1 ───────────────────────────────
# Insert before Wintergreen (which follows it alphabetically and is the next entry)
WILD_BLUEBERRY_ENTRY = """### Wild Blueberry / Lowbush Blueberry
*Vaccinium angustifolium*

![Wild Blueberry (Vaccinium angustifolium) — low shrub with clusters of small dark blue berries](images/native-plants/vaccinium-angustifolium.jpg)

**Identification**
A low-growing shrub (6–24 inches) with small, elliptical, finely serrated alternate leaves. Tiny white to pink urn-shaped flowers in spring. Berries are small (¼–½ inch), blue-black with a waxy white bloom, growing in clusters. The five-pointed star-shaped calyx at the blossom end is the key identification feature — all *Vaccinium* species have it.

**Where to Find It**
Acidic, well-drained, sandy or rocky soils. Open barrens, forest edges, burned-over areas, heath-covered slopes. Very common throughout the Northeast, particularly in Maine and the Adirondacks.

**Season**
Berries ripen July–August. In productive years, hillsides turn blue.

**Edible Parts**
Ripe berries only.

**Preparation**
Fresh raw — intense flavor, far superior to cultivated blueberries. Jam, pie, muffins, syrup, dried. Freezes exceptionally well.

**Safety**
The five-pointed calyx crown at the berry tip is the key feature distinguishing blueberries from any toxic lookalike. No dangerous lookalikes once the crown is confirmed.

---

"""

# Insert before the Wintergreen entry in Region 1
text = text.replace(
    "### Wintergreen\n*Gaultheria procumbens*",
    WILD_BLUEBERRY_ENTRY + "### Wintergreen\n*Gaultheria procumbens*",
    1,  # only first occurrence (Region 1)
)

# ── 5. Add page breaks before all ### headings ─────────────────────────────
# Insert page break div before every line starting with ###
output_lines = []
for line in text.splitlines(keepends=True):
    if line.startswith("### "):
        output_lines.append('<div style="page-break-before: always"></div>\n\n')
    output_lines.append(line)

text = "".join(output_lines)

# ── 6. Write output ────────────────────────────────────────────────────────
GUIDE.write_text(text, encoding="utf-8")
print(f"Done. Written to {GUIDE}")
print(f"New size: {GUIDE.stat().st_size:,} bytes")

# ── 7. Report remaining issues ─────────────────────────────────────────────
see_refs = []
for i, line in enumerate(text.splitlines(), 1):
    if re.search(
        r"[Ss]ee \w+ entry|[Ss]ee \w+ \w+ entry|[Ss]ee previous entries|[Ss]ee Northeast|[Ss]ee Southeast|[Ss]ee Midwest|[Ss]ee Pacific|[Ss]ee Southwest|[Ss]ee Rocky|[Ss]ee Great",
        line,
    ):
        if not line.strip().startswith("**Safety"):
            see_refs.append((i, line.strip()[:100]))

print(f"\n=== {len(see_refs)} remaining cross-references to expand ===")
for lineno, snippet in see_refs[:30]:
    print(f"  line {lineno}: {snippet}")
if len(see_refs) > 30:
    print(f"  ... and {len(see_refs) - 30} more")
