---
title: "Phase 5: Offline Export & Kiwix Integration — Architecture"
project: open-repo
phase: 5
status: pre-implementation research
date: 2026-04-27
author: research-agent
confidence: high
tags: [kiwix, zim, offline-export, openzim, libzim, architecture]
---

# Phase 5: Offline Export & Kiwix Integration

**Pre-implementation research document. Phase 4 (federation) is in PR review; this document removes the discovery phase from Phase 5.**

---

## 1. What Is Kiwix?

### Origin and Mission

Kiwix is a free, open-source offline web browser created in 2007 by Emmanuel Engelhart and Renaud Gaudin, originally to provide internet-disconnected access to Wikipedia. It has since grown into the primary ecosystem for packaging, distributing, and reading any web-based knowledge offline. As of early 2024, Kiwix reported upwards of 10 million ZIM file downloads in the first two months of that year alone. Content is available in more than 100 languages. The project is governed by the Kiwix Association, a Swiss nonprofit, and receives financial support from Wikimedia CH and the Wikimedia Foundation.

The license is **GPLv3** for all Kiwix reader applications, and the underlying file format library (libzim) is **LGPL**, meaning it can be embedded in proprietary applications without license contamination. This distinction matters for open-repo: using libzim or its Python bindings is legally unproblematic for an open-source project.

### Who Uses It and Why

Kiwix's primary user base falls into three overlapping groups. First are students and educators in regions with unreliable or expensive internet — the Afripedia Project deployed Kiwix across universities in 11 African countries, and One Laptop per Child has shipped it on devices. Second are people living under censorship or network restriction; the project has documented usage in North Korea smuggling operations. Third are operators who need resilient information access independent of network uptime — Antarctic research vessels, Senegalese Navy patrol ships, and humanitarian field workers.

For open-repo, the relevant use case is the third type: users who want to take a snapshot of the library (or a curated subset) and read it on a laptop, phone, or tablet without a server connection. This is directly analogous to how Wikipedia offline works today.

### Platforms and Ecosystem

Kiwix runs on Android (Kotlin), iOS (Swift), macOS, Windows, Linux, and as a browser extension (JavaScript). There is also **kiwix-serve**, a lightweight HTTP server that reads ZIM files and exposes them as a local web server accessible from any browser on the same network. The entire ecosystem — readers, server, format library, scrapers — is open-source and available at [github.com/kiwix](https://github.com/kiwix) and [github.com/openzim](https://github.com/openzim).

Notable existing ZIM content includes the full English Wikipedia (110 GB with images, 57 GB without, 7.4 GB introduction-only), Stack Exchange network dumps, Project Gutenberg's entire ebook catalog, Khan Academy videos, TED talks, and Crash Course videos. The breadth of this catalog demonstrates that the ZIM format handles heterogeneous content well — text, images, video, and full-text search indices coexist in a single file.

### Open Source Community

The openZIM GitHub organization hosts 40+ repositories covering the format specification, the C++ reference library, Python bindings, Node.js scrapers, command-line tools, and the Zimfarm pipeline (the automated factory that produces official ZIM files). Community contributions are active; the zimfarm pipeline continuously regenerates fresh ZIM files for Wikipedia, Stack Exchange, and other major sources. Any project can submit a "recipe" to the Zimfarm requesting automated generation of a ZIM file from a public source.

---

## 2. The ZIM File Format

### Internal Architecture

ZIM stands for "Zeno IMproved," replacing an older Zeno format. A ZIM file is a single binary container. Its architecture has three main layers:

**Header and Directory.** The file begins with a fixed-size header containing a magic number, version, UUID, article count, cluster count, and byte offsets to the directory and cluster sections. The directory is a sorted list of entries (articles, images, assets, metadata), each storing the entry's namespace, MIME type, URL path, title, and a pointer to its cluster.

**Clusters.** Content is not stored article-by-article. Instead, multiple articles are grouped into *clusters* and compressed together. This is the key to ZIM's compression efficiency: grouping similar content (many HTML articles) before compressing yields far better ratios than compressing each article independently. The format supports two compression algorithms: **Zstandard (zstd)** since libzim 7.0.0 (October 2021), which is the current default, and **LZMA2 (via XZ Utils)**, which achieves higher compression ratios at the cost of slower decompression. The ZIM specification indicates cluster values of `4` for LZMA2 and `5` for Zstandard. Cluster size is configurable: larger clusters compress better, smaller clusters allow faster random access to individual articles. The format supports compression ratios up to 3x compared to uncompressed storage.

**Full-Text Search Index.** ZIM files can embed a Xapian full-text search database as a set of internal entries. When libzim opens a file with an embedded index, it exposes a search API without requiring an external search server. This is what enables Kiwix to do keyword search across millions of articles instantly, even on a Raspberry Pi.

**Random Access Without Full Decompression.** Because the directory provides byte offsets to clusters, and clusters are independently compressed, a reader can decompress and serve a single article without touching the rest of the file. This is the critical property that makes ZIM suitable for large archives: a 100 GB file can serve individual articles in milliseconds.

### Namespaces

Before 2021, ZIM used single-letter namespaces (`A` for articles, `I` for images, `M` for metadata, `-` for non-article content) to separate entry types. Since 2021, the namespace scheme was simplified — all content is now in a flat namespace, and the `FRONT_ARTICLE` hint replaces the old `A` namespace convention for marking browsable articles. Old readers remain compatible with new files.

### File Sizes in Practice

The format's compression means open-repo's export sizes will be manageable. A text-heavy knowledge library with 100,000 articles and minimal images would likely compress to under 2 GB. A library with extensive images might reach 10-20 GB for a full export. Kiwix's Wikipedia-without-images at 57 GB covers 6+ million articles, suggesting open-repo's Phase 1 dataset would be a fraction of that.

---

## 3. How Comparable Systems Export to Offline Formats

### Wikipedia's Export Pipeline

Wikipedia's ZIM files are generated by **mwoffliner**, a Node.js scraper maintained by openZIM. The pipeline is: (1) fetch article list and content via the MediaWiki API, (2) parse Wikitext to HTML via the MediaWiki parser, (3) download and process images, (4) apply optimizations (WebP conversion, thumbnail generation), (5) pack everything into a ZIM file via libzim. The resulting files are stored on Kiwix's content server and updated monthly. mwoffliner requires Docker, Node.js 24, Redis, and the C++ libzim library. This complexity — a Node.js process with Redis as an intermediary — exists because Wikipedia's content is dynamically rendered Wikitext, not pre-rendered HTML. Open-repo's situation is simpler: the data is already structured JSON.

### Project Gutenberg's Export Pipeline

The openzim/gutenberg scraper (available on PyPI as `gutenberg2zim`) follows a three-phase pipeline: download ebook metadata and files from Project Gutenberg mirrors, convert EPUBs and HTML files into a consistent format, then package them into a ZIM file using python-libzim. The scraper builds a Vue.js frontend that is embedded in the ZIM file, providing a rich browsing experience. This is a Python-native pipeline and the closest architectural analogue to what open-repo would build.

### Zimit: Arbitrary Website to ZIM

**Zimit** converts any public website into a ZIM file. It uses Browsertrix Crawler to run a headless browser crawl, producing WARC (Web ARChive) files, then converts those WARCs to ZIM using **warc2zim**. This approach is generic but heavyweight: it requires Docker and is slower than a direct API-based export. For open-repo, which controls its own data model, Zimit is not the right tool — it is designed for scraping sites that have no export API.

### zimwriterfs: Directory to ZIM

The older **zimwriterfs** tool (now part of zim-tools) takes a local directory of self-contained HTML files (articles, images, stylesheets) and packs them into a ZIM file. The command-line interface is straightforward:

```
zimwriterfs \
  --welcome=index.html \
  --illustration=icon.png \
  --language=eng \
  --title="Open-Repo Export" \
  --description="Offline knowledge library snapshot" \
  --creator="Open-Repo Community" \
  --publisher="Open-Repo" \
  ./html_directory/ output.zim
```

This tool is useful for prototyping but is no longer the recommended approach for production pipelines. The Python libzim API is preferred.

### Zimfarm: Industrial-Scale Pipeline

The openZIM project operates **Zimfarm**, an automated factory that runs scrapers on a schedule and produces fresh ZIM files. It consists of a dispatcher API, worker nodes, a quarantine step using `zimcheck` (which validates ZIM file integrity), and an upload step to the public server. For open-repo's long-term roadmap, contributing a recipe to Zimfarm would allow the project's content to be indexed alongside Wikipedia — but this is optional and post-MVP.

---

## 4. Tools and Libraries for ZIM Generation

### python-libzim (Primary Recommendation)

**Repository**: [github.com/openzim/python-libzim](https://github.com/openzim/python-libzim)
**PyPI**: `pip install libzim`
**License**: LGPL

This is a thin Python wrapper over the C++ libzim library. Pre-built wheels are available for CPython on Linux (x86_64, armhf, aarch64), macOS (x86_64, arm64), and Windows (x64). It does not require a manual C++ build in most CI environments.

The core writer API centers on three classes. `Creator` is the context manager that manages ZIM file creation. `Item` is an abstract base class that callers subclass to represent each article or asset. `StringProvider` and `FileProvider` supply content. A minimal working example from the official documentation:

```python
from libzim.writer import Creator, Item, StringProvider, Hint

class ArticleItem(Item):
    def __init__(self, path, title, html):
        self.path = path
        self.title = title
        self.html = html

    def get_path(self):     return self.path
    def get_title(self):    return self.title
    def get_mimetype(self): return "text/html"
    def get_hints(self):    return {Hint.FRONT_ARTICLE: True}
    def get_contentprovider(self):
        return StringProvider(self.html)

with Creator("export.zim").config_indexing(True, "eng") as creator:
    creator.set_mainpath("index")
    creator.add_item(ArticleItem("index", "Home", "<h1>Welcome</h1>"))
    creator.add_metadata("Title", "Open-Repo Export")
    creator.add_metadata("Language", "eng")
    creator.add_metadata("Creator", "Open-Repo")
    creator.add_metadata("Date", "2026-04-27")
```

The `config_indexing(True, "eng")` call enables full-text search index generation. This is the correct approach for any content library.

**Threading note**: libzim disables the Python GIL on most C++ calls, but the writer API is not thread-safe. Use a single thread for `Creator` calls, or protect concurrent `add_item()` calls with a lock.

### libzim (C++ Reference Implementation)

**Repository**: [github.com/openzim/libzim](https://github.com/openzim/libzim)

The C++ library is the reference implementation of the ZIM specification. If open-repo ever needs to write a Go, Rust, or C service to generate ZIM files (e.g., for high-throughput batch export), bindings exist for several languages or can be built via FFI. For a Python backend, python-libzim is sufficient.

### zim-tools (Command-Line Utilities)

**Repository**: [github.com/openzim/zim-tools](https://github.com/openzim/zim-tools)

Useful for operational tasks:
- `zimcheck` — validates a ZIM file for corruption and internal consistency. Should be run after every export to verify the output before serving it to users.
- `zimdump` — inspects or dumps ZIM file contents for debugging.
- `zimsplit` — splits a large ZIM file into smaller chunks (useful for distribution over size-limited storage).
- `zimwriterfs` — converts a directory of HTML files to ZIM (useful for prototyping).

### Zimit / warc2zim

Not relevant for open-repo's direct-export path, but documented here for completeness. Zimit is the tool of choice when you want to archive a *website* you don't control. Since open-repo controls its data model, a direct python-libzim pipeline is always superior.

---

## 5. Incremental Exports

### Current State

True incremental ZIM updates (downloading only changed articles) are not currently available in production. The MediaWiki ZIM incremental update project (`zimdiff` / `zimpatch`) was proposed as a Google Summer of Code 2013 project. The tools were designed to compute a binary diff between two ZIM files and apply it client-side. The MediaWiki wiki page documenting this project (last updated March 2025) contains no evidence of production readiness or active maintenance. The Kiwix Android app's GitHub issues confirm that as of recent releases, users must download the full ZIM file when a new version is available.

### Practical Strategy for Open-Repo

For Phase 5, the pragmatic approach is **versioned full exports** rather than incremental diffs. This aligns with how all major ZIM publishers (Wikipedia, Stack Exchange, Project Gutenberg) currently operate. Each export run produces a new, complete, timestamped ZIM file. The previous version is kept available for users who have not yet downloaded the update.

The per-export cost is acceptable for open-repo's scale: a full export of the current dataset is unlikely to exceed a few gigabytes of text. The export job can run asynchronously on a schedule (nightly, weekly) and upload the output to an object store (S3, R2, Backblaze B2). Users download the latest version when they want an update.

If incremental updates become important later, the correct approach is to segment exports by category, tag, or date range, allowing users to download targeted sub-ZIM files (e.g., "Agriculture 2026") rather than a monolithic full export. This is simpler than binary diffing and more aligned with how Kiwix presents content to users (as separate topic-scoped files).

---

## 6. Integration Strategies

### Option A: Direct python-libzim Pipeline (Recommended)

Open-repo's backend queries its own database, renders each knowledge entry as self-contained HTML, and feeds those HTML strings directly into python-libzim's `Creator`. No intermediate files are written to disk during normal operation. The pipeline is a single Python process (or async task) that iterates over the entry set, calls `creator.add_item()` for each one, and finalizes the ZIM file.

**Pros:**
- Full control over HTML rendering (styling, navigation, internal links)
- No external process or Docker dependency in the happy path
- Single language (Python) — consistent with open-repo's backend
- Full-text search index is generated in the same pass by passing `config_indexing(True, "eng")` to `Creator`
- Smaller dependency surface area

**Cons:**
- Must maintain a custom HTML template for exported articles
- HTML rendering code must be kept in sync with the web UI

### Option B: Static Site Generation + zimwriterfs

The backend renders the library as a static HTML site to a temporary directory (using a template engine like Jinja2), then calls `zimwriterfs` as a subprocess to convert the directory to ZIM.

**Pros:**
- The HTML output can also serve as a standalone static site (dual-purpose)
- `zimwriterfs` handles asset discovery automatically

**Cons:**
- Writes the entire dataset to disk as HTML first (doubles the I/O and disk usage)
- Subprocess dependency on zim-tools (a compiled C++ binary)
- Less control over ZIM metadata and cluster configuration
- No longer actively recommended by openZIM for new pipelines

### Option C: Crawl the Running Open-Repo Server with Zimit

Run the Zimit Docker container against the live open-repo API/web interface.

**Pros:**
- Zero custom export code required
- Captures exactly what users see in the browser

**Cons:**
- Requires Docker; adds operational complexity
- Slow (headless browser crawl of thousands of articles)
- May miss API-only data not rendered in the browser
- Fragile: site structure changes break the crawl
- No control over ZIM structure or metadata

**Verdict**: Option A is the correct choice for Phase 5. It is the approach used by gutenberg2zim (the closest published analogue) and produces the most maintainable result. Option B is acceptable for rapid prototyping. Option C should not be used.

### Deployment Model

Two deployment modes are worth supporting:

**User-initiated download.** The open-repo web UI exposes a "Download offline copy" button. The server generates (or retrieves a pre-generated) ZIM file and streams it to the user. The user opens it in Kiwix desktop, Kiwix Android, or `kiwix-serve` on their own machine. This covers individuals wanting a personal offline library.

**Self-hosted kiwix-serve.** An institution (school, library, field office) downloads the ZIM file and runs `kiwix-serve` on a local machine. Any device on the local network can browse it via a web browser. The official Docker command is:

```
docker run -v /path/to/zims:/data -p 8080:8080 \
  ghcr.io/kiwix/kiwix-serve '*.zim'
```

Open-repo should document both modes. The ZIM file itself is the distribution unit — once generated and validated with `zimcheck`, it can be served via any CDN or direct download link.

---

## 7. Existing Open-Source Projects Doing This

Several Python projects demonstrate the direct libzim pattern that open-repo should follow:

- **gutenberg2zim** ([github.com/openzim/gutenberg](https://github.com/openzim/gutenberg), PyPI: `gutenberg2zim`): Python pipeline that downloads Project Gutenberg books, renders them as HTML with a Vue.js frontend, and packages them into a ZIM file using python-libzim. The v3.0.0 refactor eliminated filesystem intermediates and SQLite, moving to an in-memory data model. This is the closest analogue to open-repo's use case.

- **openzim/ifixit** ([github.com/openzim/ifixit](https://github.com/openzim/ifixit)): Python scraper for iFixit repair guides. Demonstrates how to export structured, category-organized content to ZIM.

- **llm-tools-kiwix** ([github.com/mozanunal/llm-tools-kiwix](https://github.com/mozanunal/llm-tools-kiwix)): Turns any ZIM archive into a searchable knowledge source for LLMs. Demonstrates programmatic reading of ZIM files via python-libzim — the inverse of what open-repo will do, but useful for understanding the read API.

- **openzim-mcp** ([github.com/cameronrye/openzim-mcp](https://github.com/cameronrye/openzim-mcp)): MCP server for querying ZIM archives. Shows the ecosystem extending into AI tooling.

---

## 8. Implementation Blueprint

### Step 1: Export Infrastructure (Days 1–5)

**Goal**: A working asynchronous export job that produces valid HTML output from the open-repo database.

Tasks:
1. Define an `ExportConfig` model (scope: all / by tag / by category / by date range, format: ZIM / HTML, language code).
2. Write an `ExportService` that queries the database for the requested scope, renders each knowledge entry as self-contained HTML (inline CSS, no external asset dependencies), and yields HTML strings.
3. Add an `ExportJob` background task (Celery or FastAPI BackgroundTasks) that runs the export asynchronously and stores the output in a configurable location (local path or S3-compatible bucket).
4. Expose a REST endpoint `POST /api/export` that enqueues an export job and returns a job ID, and `GET /api/export/{job_id}` for status polling and download.
5. Write unit tests for the export service using a small fixture dataset (20–50 entries).

**Dependencies**: No new packages required for Step 1; this is pure Python + existing ORM.

### Step 2: ZIM Generation (Days 6–12)

**Goal**: The export service produces a valid, searchable ZIM file using python-libzim.

Tasks:
1. Add `libzim` to project dependencies (`uv add libzim`).
2. Implement `ZimWriter` class that wraps the python-libzim `Creator` API. The class should accept an `ExportConfig` and a stream of `(path, title, html)` tuples, wrap each in a custom `Item` subclass, and call `creator.add_item()`.
3. Add standard ZIM metadata: `Title`, `Description`, `Language`, `Creator`, `Publisher`, `Date`, `Source` (the open-repo node URL), `Name` (e.g., `open-repo_en_all_2026-04`), `Flavour`.
4. Add an illustration (48x48 PNG icon) via `creator.add_illustration(48, icon_bytes)`.
5. Enable full-text indexing: `creator.config_indexing(True, language_code)`.
6. Set a main entry path pointing to the index/home page.
7. After generation, run `zimcheck` on the output file (via subprocess) to validate. Fail the export job and surface an error if `zimcheck` finds issues.
8. Write integration tests that generate a small ZIM file, then read it back using `libzim.reader.Archive` to verify article count, search index, and main path.

**Dependencies**: `libzim` (PyPI), `zim-tools` (system binary, installed in CI/CD via package manager or the openzim Docker image).

### Step 3: Distribution and User-Facing UI (Days 13–18)

**Goal**: Users can discover, download, and use ZIM exports without needing to understand ZIM internals.

Tasks:
1. **Export catalog endpoint**: `GET /api/exports` returns a list of available ZIM files with metadata (title, scope, date, size in bytes, SHA-256 checksum, download URL). This mirrors how Kiwix's official catalog (`library.kiwix.org`) exposes available ZIM files.
2. **Download endpoint**: Stream the ZIM file to the user via HTTP with correct `Content-Type: application/x-zim` and `Content-Disposition: attachment` headers. Support `Range` requests for resumable downloads (important for large files and mobile users).
3. **Signed URLs** (if using S3/R2): Generate pre-signed download URLs that expire after 24 hours, so the export service does not need to proxy large file transfers.
4. **Web UI integration**: Add a "Download Offline" section to the library UI. Explain what Kiwix is, link to Kiwix's app download pages, and show available exports with sizes and dates.
5. **Documentation**: Write a one-page user guide: "How to use open-repo offline." Cover Kiwix desktop, Kiwix Android, and kiwix-serve for institutional use.
6. **Scheduled regeneration**: Add a cron job or Celery Beat task to regenerate the default full export weekly (or nightly for smaller datasets).
7. **OPDS/catalog compatibility** (optional, post-MVP): The Kiwix library format uses an OPDS-style XML catalog. Implementing this would allow the open-repo export catalog to appear in Kiwix's in-app library browser automatically. This is non-trivial but high-value for discoverability.

**Dependencies**: CDN or object storage (S3/R2/B2) for hosting ZIM files, Celery Beat or equivalent for scheduling.

---

## 9. Dependency Summary

| Dependency | Purpose | Notes |
|---|---|---|
| `libzim` (PyPI) | ZIM file generation and reading | LGPL; pre-built wheels for Linux/macOS/Windows |
| `zim-tools` (system) | `zimcheck` validation after export | C++ binary; install via apt/brew or use openzim Docker image |
| Celery + broker | Async export jobs | Already likely present from Phase 4 |
| Object storage (S3/R2/B2) | Host generated ZIM files | Any S3-compatible service works |
| Jinja2 or equivalent | HTML rendering for ZIM entries | Already likely present |

---

## 10. Effort Estimate

For an experienced engineer familiar with open-repo's backend codebase:

| Step | Estimated Days |
|---|---|
| Step 1: Export infrastructure (service, background job, REST endpoints) | 4–6 days |
| Step 2: ZIM generation (libzim integration, metadata, validation) | 5–8 days |
| Step 3: Distribution, UI, scheduling | 4–6 days |
| Buffer (integration issues, CI/CD, documentation) | 2–3 days |
| **Total** | **15–23 days** |

The wide range in Step 2 reflects uncertainty around the HTML rendering complexity. If open-repo's existing templates can be reused with minimal modification for the offline context, it will be at the lower end. If the offline HTML needs to be significantly different (e.g., fully self-contained with inlined CSS and no server-side rendering), it will be at the upper end.

The libzim Python API is well-documented and the gutenberg2zim codebase serves as a working reference implementation. There is no fundamental technical risk in Step 2 — the risk is scoping the HTML rendering correctly.

---

## 11. Key Risks and Mitigations

**Risk: ZIM files become very large, making distribution impractical.**
Mitigation: Offer scoped exports (by tag, category, date range) in addition to full exports. Users download only the subset they need. This mirrors how Kiwix presents Wikipedia in different sizes (all articles, no video, introduction only).

**Risk: python-libzim's lack of thread safety causes corruption under concurrent export jobs.**
Mitigation: Serialize `Creator` calls within a single export job. Allow multiple export jobs to run in parallel only if each uses its own `Creator` instance and output file. Do not share a `Creator` across threads.

**Risk: `zimcheck` fails for reasons that are hard to debug.**
Mitigation: Write integration tests that round-trip a small ZIM file (write with python-libzim, validate with zimcheck, read back with libzim.reader.Archive). Catch problems in CI before they reach production.

**Risk: Users don't know what Kiwix is.**
Mitigation: The download UI must explain the tool and link to Kiwix directly. "Download for Android," "Download for Windows," "Run on your own server" links should be first-class UI elements adjacent to the export download button.

---

## Sources

- [Kiwix — Wikipedia](https://en.wikipedia.org/wiki/Kiwix)
- [ZIM (file format) — Wikipedia](https://en.wikipedia.org/wiki/ZIM_(file_format))
- [openZIM GitHub Organization](https://github.com/openzim)
- [python-libzim — GitHub](https://github.com/openzim/python-libzim)
- [python-libzim — PyPI](https://pypi.org/project/libzim/)
- [python-libzim — ReadTheDocs](https://python-libzim.readthedocs.io/)
- [libzim (C++ reference) — GitHub](https://github.com/openzim/libzim)
- [zim-tools — GitHub](https://github.com/openzim/zim-tools)
- [Zimit — GitHub](https://github.com/openzim/zimit)
- [mwoffliner — GitHub](https://github.com/openzim/mwoffliner)
- [gutenberg2zim — GitHub](https://github.com/openzim/gutenberg)
- [gutenberg2zim — PyPI](https://pypi.org/project/gutenberg2zim/)
- [Zimfarm — GitHub](https://github.com/openzim/zimfarm)
- [Kiwix/ZIM incremental updates — MediaWiki](https://www.mediawiki.org/wiki/Kiwix/ZIM_incremental_updates)
- [kiwix-tools Docker Server — GitHub](https://github.com/kiwix/kiwix-tools/blob/main/docker/server/README.md)
- [Kiwix Android — GitHub](https://github.com/kiwix/kiwix-android)
- [ZIM File Format — docs.fileformat.com](https://docs.fileformat.com/compression/zim/)
- [openzim-mcp (MCP server for ZIM) — GitHub](https://github.com/cameronrye/openzim-mcp)
- [llm-tools-kiwix — GitHub](https://github.com/mozanunal/llm-tools-kiwix)
- [Kiwix Offline Internet spotlight](https://www.offlineinternet.org/spotlight-on-kiwix/)
- [How to Create an Offline Version of Websites Using Kiwix — DEV Community](https://dev.to/free_programmers/how-to-create-an-offline-version-of-websites-using-kiwix-and-zim-files-3d9b)
- [Self-Hosting Wikipedia with Kiwix — DEV Community](https://dev.to/matthieusb/self-hosting-wikipedia-and-other-sites-with-kiwix-2nfn)
- [zimwriterfs man page — Ubuntu](https://manpages.ubuntu.com/manpages/focal/man1/zimwriterfs.1.html)
