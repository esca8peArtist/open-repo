---
layout: home
title: open-repo
description: A free, open, distributed library of human knowledge — guides, schematics, recipes, 3D models, and more
---

# open-repo

**A free, open, distributed library of human knowledge.**

Guides, schematics, recipes, 3D models, and procedures — available offline, federated across nodes, and accessible to anyone without an account.

---

## What is open-repo?

open-repo is a distributed content network designed for practical knowledge that should survive infrastructure failure. Think Wikipedia meets LibreOffice — but for doing things, not just knowing them.

**Every article in open-repo is**:
- Structured as JSON-LD for machine readability and federation
- Exportable as a ZIM file for offline access via [Kiwix](https://kiwix.org)
- Licensed for redistribution (CC BY-SA 4.0 or more permissive)
- Versioned by content hash (CID), not by server-assigned ID

**Content domains**:
- Medical reference (drug dosing, procedures, first aid)
- Water systems (sourcing, filtration, treatment)
- Botanical knowledge (plant ID, edible and medicinal species, seed saving)
- Seed preservation and food production
- Food preservation (canning, fermentation, root cellaring)
- Agriculture, energy, shelter, and electronics (via federation)

---

## Download for Offline Use

ZIM files can be downloaded and read on any device with [Kiwix](https://kiwix.org):

- **Kiwix Desktop** (Windows, macOS, Linux): [kiwix.org/en/downloads/](https://kiwix.org/en/downloads/)
- **Kiwix Android**: [Play Store](https://play.google.com/store/apps/details?id=org.kiwix.kiwixmobile)
- **kiwix-serve** (self-host on a local network or Raspberry Pi): `docker run -v /path/to/zim:/data kiwix/kiwix-serve /data/*.zim`

ZIM archives are published via the OPDS catalog at the open-repo node. See the project README for current download links.

---

## For Contributors

open-repo accepts content contributions in two forms:

### 1. Structured JSON-LD content items

Submit content using the Phase 5.2 content schemas:

| Content type | Schema |
|---|---|
| Medical articles (drug monographs, procedures, first aid) | [medical_article.schema.json](schemas/medical_article.schema.json) |
| Botanical knowledge (species cards, wild edibles, medicinals) | [botanical_knowledge.schema.json](schemas/botanical_knowledge.schema.json) |
| Water systems procedures | [water_systems.schema.json](schemas/water_systems.schema.json) |
| Seed preservation | [seed_preservation.schema.json](schemas/seed_preservation.schema.json) |
| Food preservation | [food_preservation.schema.json](schemas/food_preservation.schema.json) |

All schemas follow JSON Schema Draft-07. Submit validated JSON-LD objects as pull requests or via the federation API.

### 2. Markdown source documents

Well-sourced Markdown documents in the content domains above can be converted to structured content items by project maintainers. Include:
- Primary sources (WHO, USDA, ICRC, peer-reviewed literature) with URLs
- Specific quantities, measurements, and procedures — not general descriptions
- License statement confirming the content is your own work or appropriately licensed

### Medical content

All medical articles require a medical accuracy review before publication. If you are a physician, pharmacist, or wilderness medicine practitioner, see [Medical Reviewer Outreach](https://github.com/esca8peArtist/open-repo/blob/main/projects/open-repo/medical-reviewer-outreach-draft.md) for the review process.

---

## Architecture

open-repo uses an ActivityPub-based federation model:
- Nodes synchronize content via ActivityPub Create/Update/Delete activities
- Content is addressed by CID (SHA256 of normalized JSON-LD), not by server URL
- Any node can export its content to ZIM for offline distribution

See [FEDERATION_ARCHITECTURE.md](https://github.com/esca8peArtist/open-repo/blob/main/projects/open-repo/FEDERATION_ARCHITECTURE.md) for protocol details.

---

## Project Status

| Phase | Description | Status |
|---|---|---|
| Phase 1–4 | Core backend, accessibility, federation | Complete |
| Phase 5.1 | ZIM export pipeline (libzim integration) | Complete |
| Phase 5.2 | Medical, water, seed, botanical modules | In progress |
| Phase 6 | Public node federation and OPDS catalog | Planned |

---

## Links

- [GitHub Repository](https://github.com/esca8peArtist/open-repo)
- [Schema Documentation](schemas/)
- [Schema Reference (full)](https://github.com/esca8peArtist/open-repo/blob/main/projects/open-repo/SCHEMA_DOCUMENTATION.md)
- [Issue Tracker](https://github.com/esca8peArtist/open-repo/issues)

---

*open-repo is free and open-source. Content is CC BY-SA 4.0. Code is MIT-licensed.*
