"""
Download plant identification images for the Seedwarden Native Plants Regional Guide.

Strategy (in order of preference):
  1. Wikipedia REST API summary endpoint — returns the curated main article image,
     which is typically a high-quality botanical photograph or scientific illustration
     showing the whole plant and its identifying features.
  2. iNaturalist API (CC0/CC-BY research-grade observations, sorted by votes) as fallback.

All downloads overwrite previous files so re-running improves quality.
"""

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

IMAGES_DIR = Path(__file__).parent / "images" / "native-plants"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

# (slug, scientific_name, common_name, wikipedia_article_title)
# wikipedia_article_title is the exact Wikipedia article name when it differs from the
# scientific name (e.g. common plants have common-name articles with better images).
SPECIES = [
    # ── UBIQUITOUS ────────────────────────────────────────────────────────────
    ("allium-tricoccum", "Allium tricoccum", "Ramps", "Allium tricoccum"),
    ("amaranthus-retroflexus", "Amaranthus retroflexus", "Amaranth", "Amaranth"),
    ("apios-americana", "Apios americana", "Groundnut", "Apios americana"),
    ("arctium-lappa", "Arctium lappa", "Burdock", "Burdock"),
    ("asarum-canadense", "Asarum canadense", "Wild Ginger", "Asarum canadense"),
    ("asclepias-syriaca", "Asclepias syriaca", "Common Milkweed", "Asclepias syriaca"),
    (
        "asparagus-officinalis",
        "Asparagus officinalis",
        "Wild Asparagus",
        "Asparagus officinalis",
    ),
    ("asimina-triloba", "Asimina triloba", "Pawpaw", "Asimina triloba"),
    ("chenopodium-album", "Chenopodium album", "Lamb's Quarters", "Chenopodium album"),
    ("cichorium-intybus", "Cichorium intybus", "Chicory", "Chichorium intybus"),
    ("coprinus-comatus", "Coprinus comatus", "Shaggy Mane", "Coprinus comatus"),
    ("daucus-carota", "Daucus carota", "Queen Anne's Lace", "Daucus carota"),
    ("epilobium-angustifolium", "Chamerion angustifolium", "Fireweed", "Fireweed"),
    (
        "fallopia-japonica",
        "Reynoutria japonica",
        "Japanese Knotweed",
        "Japanese knotweed",
    ),
    (
        "fragaria-virginiana",
        "Fragaria virginiana",
        "Wild Strawberry",
        "Fragaria virginiana",
    ),
    ("glechoma-hederacea", "Glechoma hederacea", "Ground Ivy", "Glechoma hederacea"),
    (
        "helianthus-tuberosus",
        "Helianthus tuberosus",
        "Jerusalem Artichoke",
        "Jerusalem artichoke",
    ),
    (
        "matteuccia-struthiopt",
        "Matteuccia struthiopteris",
        "Ostrich Fern",
        "Matteuccia struthiopteris",
    ),
    ("nasturtium-officinale", "Nasturtium officinale", "Watercress", "Watercress"),
    ("nelumbo-lutea", "Nelumbo lutea", "American Lotus", "Nelumbo lutea"),
    ("oxalis-stricta", "Oxalis stricta", "Wood Sorrel", "Oxalis stricta"),
    ("portulaca-oleracea", "Portulaca oleracea", "Purslane", "Purslane"),
    (
        "rubus-allegheniensis",
        "Rubus allegheniensis",
        "Wild Blackberry",
        "Rubus allegheniensis",
    ),
    ("stellaria-media", "Stellaria media", "Chickweed", "Stellaria media"),
    ("taraxacum-officinale", "Taraxacum officinale", "Dandelion", "Dandelion"),
    ("typha-latifolia", "Typha latifolia", "Cattail", "Typha latifolia"),
    ("urtica-dioica", "Urtica dioica", "Stinging Nettle", "Urtica dioica"),
    ("viola-sororia", "Viola sororia", "Common Blue Violet", "Viola sororia"),
    # ── NORTHEAST ────────────────────────────────────────────────────────────
    (
        "alliaria-petiolata",
        "Alliaria petiolata",
        "Garlic Mustard",
        "Alliaria petiolata",
    ),
    ("amelanchier", "Amelanchier canadensis", "Serviceberry", "Serviceberry"),
    ("calvatia-gigantea", "Calvatia gigantea", "Giant Puffball", "Calvatia gigantea"),
    (
        "cantharellus-cibarius",
        "Cantharellus cibarius",
        "Chanterelle",
        "Cantharellus cibarius",
    ),
    ("carya-ovata", "Carya ovata", "Shagbark Hickory", "Carya ovata"),
    (
        "corylus-americana",
        "Corylus americana",
        "American Hazelnut",
        "Corylus americana",
    ),
    (
        "craterellus-cornucop",
        "Craterellus cornucopioides",
        "Black Trumpet",
        "Craterellus cornucopioides",
    ),
    (
        "diospyros-virginiana",
        "Diospyros virginiana",
        "American Persimmon",
        "Diospyros virginiana",
    ),
    (
        "elaeagnus-umbellata",
        "Elaeagnus umbellata",
        "Autumn Olive",
        "Elaeagnus umbellata",
    ),
    (
        "gaultheria-procumbens",
        "Gaultheria procumbens",
        "Wintergreen",
        "Gaultheria procumbens",
    ),
    ("grifola-frondosa", "Grifola frondosa", "Hen of the Woods", "Grifola frondosa"),
    ("hericium-erinaceus", "Hericium erinaceus", "Lion's Mane", "Hericium erinaceus"),
    ("juglans-nigra", "Juglans nigra", "Black Walnut", "Juglans nigra"),
    (
        "laetiporus-sulphureus",
        "Laetiporus sulphureus",
        "Chicken of the Woods",
        "Laetiporus sulphureus",
    ),
    ("lindera-benzoin", "Lindera benzoin", "Spicebush", "Lindera benzoin"),
    ("morchella", "Morchella esculenta", "Morel Mushroom", "Morchella esculenta"),
    (
        "pleurotus-ostreatus",
        "Pleurotus ostreatus",
        "Oyster Mushroom",
        "Pleurotus ostreatus",
    ),
    ("prunus-americana", "Prunus americana", "Wild Plum", "Prunus americana"),
    ("rhus-typhina", "Rhus typhina", "Staghorn Sumac", "Rhus typhina"),
    ("rosa-carolina", "Rosa carolina", "Wild Rose", "Rosa carolina"),
    ("rubus-idaeus", "Rubus idaeus", "Wild Raspberry", "Rubus idaeus"),
    ("sambucus-canadensis", "Sambucus canadensis", "Elderberry", "Sambucus canadensis"),
    (
        "vaccinium-angustifolium",
        "Vaccinium angustifolium",
        "Wild Blueberry",
        "Vaccinium angustifolium",
    ),
    (
        "vaccinium-corymbosum",
        "Vaccinium corymbosum",
        "Highbush Blueberry",
        "Vaccinium corymbosum",
    ),
    # ── SOUTHEAST ─────────────────────────────────────────────────────────────
    ("carya-illinoinensis", "Carya illinoinensis", "Pecan", "Pecan"),
    ("crataegus", "Crataegus monogyna", "Hawthorn", "Crataegus"),
    (
        "hypomyces-lactifluorum",
        "Hypomyces lactifluorum",
        "Lobster Mushroom",
        "Hypomyces lactifluorum",
    ),
    ("morus-rubra", "Morus rubra", "Red Mulberry", "Morus rubra"),
    ("passiflora-incarnata", "Passiflora incarnata", "Maypop", "Passiflora incarnata"),
    (
        "podophyllum-peltatum",
        "Podophyllum peltatum",
        "Mayapple",
        "Podophyllum peltatum",
    ),
    ("prunus-serotina", "Prunus serotina", "Black Cherry", "Prunus serotina"),
    ("pueraria-montana", "Pueraria montana", "Kudzu", "Kudzu"),
    (
        "tradescantia-ohiensis",
        "Tradescantia ohiensis",
        "Spiderwort",
        "Tradescantia ohiensis",
    ),
    (
        "vitis-rotundifolia",
        "Vitis rotundifolia",
        "Muscadine Grape",
        "Vitis rotundifolia",
    ),
    # ── MIDWEST ───────────────────────────────────────────────────────────────
    ("allium-canadense", "Allium canadense", "Wild Garlic", "Allium canadense"),
    ("prunus-virginiana", "Prunus virginiana", "Chokecherry", "Prunus virginiana"),
    ("vitis-labrusca", "Vitis labrusca", "Fox Grape", "Vitis labrusca"),
    # ── GREAT PLAINS ──────────────────────────────────────────────────────────
    (
        "astragalus-crassicarpus",
        "Astragalus crassicarpus",
        "Ground Plum",
        "Astragalus crassicarpus",
    ),
    ("celtis-occidentalis", "Celtis occidentalis", "Hackberry", "Celtis occidentalis"),
    (
        "opuntia-polyacantha",
        "Opuntia polyacantha",
        "Plains Prickly Pear",
        "Opuntia polyacantha",
    ),
    (
        "pediomelum-esculentum",
        "Pediomelum esculentum",
        "Prairie Turnip",
        "Pediomelum esculentum",
    ),
    ("rhus-glabra", "Rhus glabra", "Smooth Sumac", "Rhus glabra"),
    (
        "shepherdia-argentea",
        "Shepherdia argentea",
        "Buffalo Berry",
        "Shepherdia argentea",
    ),
    # ── SOUTHWEST ─────────────────────────────────────────────────────────────
    ("arctostaphylos-pungens", "Arctostaphylos pungens", "Manzanita", "Manzanita"),
    (
        "atriplex-canescens",
        "Atriplex canescens",
        "Fourwing Saltbush",
        "Atriplex canescens",
    ),
    ("carnegiea-gigantea", "Carnegiea gigantea", "Saguaro", "Saguaro"),
    (
        "celtis-reticulata",
        "Celtis reticulata",
        "Netleaf Hackberry",
        "Celtis reticulata",
    ),
    ("lycium-pallidum", "Lycium pallidum", "Wolfberry", "Lycium pallidum"),
    (
        "opuntia-engelmannii",
        "Opuntia engelmannii",
        "Engelmann Prickly Pear",
        "Opuntia engelmannii",
    ),
    ("prosopis-glandulosa", "Prosopis glandulosa", "Honey Mesquite", "Mesquite"),
    ("salvia-columbariae", "Salvia columbariae", "Desert Chia", "Salvia columbariae"),
    ("yucca-baccata", "Yucca baccata", "Banana Yucca", "Yucca baccata"),
    # ── PACIFIC NORTHWEST ─────────────────────────────────────────────────────
    ("boletus-edulis", "Boletus edulis", "King Bolete / Porcini", "Penny bun"),
    (
        "cantharellus-formosus",
        "Cantharellus formosus",
        "Pacific Chanterelle",
        "Cantharellus formosus",
    ),
    ("camassia-quamash", "Camassia quamash", "Common Camas", "Camassia quamash"),
    (
        "claytonia-perfoliata",
        "Claytonia perfoliata",
        "Miner's Lettuce",
        "Claytonia perfoliata",
    ),
    ("gaultheria-shallon", "Gaultheria shallon", "Salal", "Gaultheria shallon"),
    ("heracleum-maximum", "Heracleum maximum", "Cow Parsnip", "Heracleum maximum"),
    ("hydnum-repandum", "Hydnum repandum", "Hedgehog Mushroom", "Hydnum repandum"),
    (
        "mahonia-aquifolium",
        "Berberis aquifolium",
        "Oregon Grape",
        "Berberis aquifolium",
    ),
    ("malus-fusca", "Malus fusca", "Pacific Crabapple", "Malus fusca"),
    ("rubus-parviflorus", "Rubus parviflorus", "Thimbleberry", "Rubus parviflorus"),
    ("rubus-spectabilis", "Rubus spectabilis", "Salmonberry", "Rubus spectabilis"),
    (
        "tricholoma-magnivelare",
        "Tricholoma magnivelare",
        "American Matsutake",
        "Tricholoma magnivelare",
    ),
    (
        "vaccinium-membranaceum",
        "Vaccinium membranaceum",
        "Mountain Huckleberry",
        "Vaccinium membranaceum",
    ),
    # ── ROCKY MOUNTAINS ───────────────────────────────────────────────────────
    ("allium-cernuum", "Allium cernuum", "Nodding Wild Onion", "Allium cernuum"),
    ("pinus-edulis", "Pinus edulis", "Pinon Pine", "Pinus edulis"),
    ("quercus-gambelii", "Quercus gambelii", "Gambel Oak", "Quercus gambelii"),
    ("ramaria", "Ramaria aurea", "Coral Fungi", "Ramaria"),
    ("ribes-cereum", "Ribes cereum", "Wax Currant", "Ribes cereum"),
    (
        "shepherdia-canadensis",
        "Shepherdia canadensis",
        "Canada Buffaloberry",
        "Shepherdia canadensis",
    ),
    ("sorbus-scopulina", "Sorbus scopulina", "Mountain Ash", "Sorbus scopulina"),
    # ── CALIFORNIA ────────────────────────────────────────────────────────────
    ("arbutus-menziesii", "Arbutus menziesii", "Pacific Madrone", "Arbutus menziesii"),
    ("brassica-nigra", "Brassica nigra", "Black Mustard", "Brassica nigra"),
    (
        "cantharellus-californicus",
        "Cantharellus californicus",
        "California Chanterelle",
        "Cantharellus californicus",
    ),
    ("foeniculum-vulgare", "Foeniculum vulgare", "Fennel", "Fennel"),
    (
        "heteromeles-arbutifolia",
        "Heteromeles arbutifolia",
        "Toyon",
        "Heteromeles arbutifolia",
    ),
    (
        "hypochaeris-radicata",
        "Hypochaeris radicata",
        "Cat's Ear",
        "Hypochaeris radicata",
    ),
    (
        "lactarius-rubidus",
        "Lactarius rubidus",
        "Candy Cap Mushroom",
        "Lactarius rubidus",
    ),
    ("malva-neglecta", "Malva neglecta", "Common Mallow", "Malva neglecta"),
    (
        "quercus-kelloggii",
        "Quercus kelloggii",
        "California Black Oak",
        "Quercus kelloggii",
    ),
    ("quercus-lobata", "Quercus lobata", "Valley Oak", "Quercus lobata"),
    ("raphanus-sativus", "Raphanus sativus", "Wild Radish", "Raphanus sativus"),
    ("sonchus-oleraceus", "Sonchus oleraceus", "Sow Thistle", "Sonchus oleraceus"),
    (
        "umbellularia-californica",
        "Umbellularia californica",
        "California Bay Laurel",
        "Umbellularia californica",
    ),
    (
        "vitis-californica",
        "Vitis californica",
        "California Wild Grape",
        "Vitis californica",
    ),
    # ── GULF COAST ────────────────────────────────────────────────────────────
    ("coccoloba-uvifera", "Coccoloba uvifera", "Sea Grape", "Coccoloba uvifera"),
    ("ilex-vomitoria", "Ilex vomitoria", "Yaupon Holly", "Ilex vomitoria"),
    ("pontederia-cordata", "Pontederia cordata", "Pickerelweed", "Pontederia cordata"),
    ("sabal-palmetto", "Sabal palmetto", "Cabbage Palm", "Sabal palmetto"),
    ("salicornia-bigelovii", "Salicornia bigelovii", "Sea Beans", "Salicornia"),
    ("serenoa-repens", "Serenoa repens", "Saw Palmetto", "Serenoa repens"),
]

HEADERS = {"User-Agent": "Seedwarden/1.0 plant-guide (educational nonprofit)"}


def get_wikipedia_image(article_title: str) -> str | None:
    """Return the best image URL from Wikipedia's article summary."""
    title = article_title.replace(" ", "_")
    url = (
        f"https://en.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(title)}"
    )
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read())
            # Prefer original high-res; fall back to thumbnail but ask for 800px
            orig = data.get("originalimage", {}).get("source", "")
            thumb = data.get("thumbnail", {}).get("source", "")
            if orig:
                return orig
            if thumb:
                # Request larger size from Wikimedia image servers
                return thumb.replace("/320px-", "/800px-").replace("/200px-", "/800px-")
            return None
        except Exception as e:
            if "429" in str(e) and attempt < 3:
                wait = 60 * (2**attempt)  # 60s, 120s, 240s
                print(f"    rate-limited, waiting {wait}s before retry...")
                time.sleep(wait)
                continue
            break
    return None


def get_inat_image(scientific_name: str) -> str | None:
    """Fallback: top-voted CC0 research-grade photo from iNaturalist."""
    taxon = urllib.parse.quote(scientific_name)
    url = (
        f"https://api.inaturalist.org/v1/observations"
        f"?taxon_name={taxon}&quality_grade=research&photos=true"
        f"&photo_license=cc0,cc-by&per_page=1&order_by=votes"
    )
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        results = data.get("results", [])
        if not results:
            return None
        photos = results[0].get("photos", [])
        if not photos:
            return None
        url_t = photos[0].get("url", "").replace("square", "medium")
        return url_t or None
    except Exception:
        return None


def download_image(slug: str, sci: str, common: str, wiki_title: str) -> bool:
    # Try Wikipedia first (curated, high-quality botanical images)
    img_url = get_wikipedia_image(wiki_title)
    source = "Wikipedia"
    if not img_url:
        img_url = get_inat_image(sci)
        source = "iNaturalist"
    if not img_url:
        print(f"  ✗ {common} — no image found")
        return False

    for attempt in range(4):
        try:
            req = urllib.request.Request(img_url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
                content_type = resp.headers.get("Content-Type", "")
            ext = ".png" if "png" in content_type.lower() else ".jpg"
            out_path = IMAGES_DIR / f"{slug}{ext}"
            # Remove any previously downloaded version in the other format
            for old_ext in (".jpg", ".png"):
                old = IMAGES_DIR / f"{slug}{old_ext}"
                if old.exists() and old_ext != ext:
                    old.unlink()
            out_path.write_bytes(data)
            print(f"  ✓ {common} ({source}, {len(data) // 1024}KB)")
            return True
        except Exception as e:
            if "429" in str(e) and attempt < 3:
                wait = 60 * (2**attempt)  # 60s, 120s, 240s
                print(f"    rate-limited on image fetch, waiting {wait}s...")
                time.sleep(wait)
                continue
            print(f"  ✗ {common} — download error: {e}")
            return False
    return False


def main():
    print(f"Downloading {len(SPECIES)} plant images to: {IMAGES_DIR}\n")
    ok = fail = 0
    for slug, sci, common, wiki in SPECIES:
        # Check existence before sleeping — no delay needed for already-cached files
        already_exists = any(
            (IMAGES_DIR / f"{slug}{ext}").exists() for ext in (".jpg", ".png")
        )
        if already_exists:
            print(f"  - {common} (already exists)")
            ok += 1
            continue
        # Polite crawl delay — only when we are about to make network requests.
        # 3 seconds gives comfortable headroom to stay under Wikimedia rate limits.
        time.sleep(3.0)
        if download_image(slug, sci, common, wiki):
            ok += 1
        else:
            fail += 1
    print(f"\nDone. {ok} downloaded, {fail} failed.")


if __name__ == "__main__":
    main()
