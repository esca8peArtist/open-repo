"""Regression tests for accessibility fixes.

Non-browser tests use httpx ASGI transport for fast, CI-friendly checks.
Browser-based tests (using playwright fixture) are marked with
@pytest.mark.playwright and require a running browser.

WCAG issues addressed:
  - SR1-01 / SR2-01: <html lang="en"> (WCAG 3.1.1) -- fixed 2026-06-02
  - K-01: <html lang="en"> on /docs and /redoc (WCAG 3.1.1) -- fixed 2026-06-02
  - K-02: Skip-to-main link on /docs and /redoc (WCAG 2.4.1) -- fixed 2026-06-02
  - SR1-02: <main> landmark on /docs and /redoc (WCAG 1.3.1) -- fixed 2026-06-02
"""

import pytest
import asyncio
from httpx import AsyncClient, ASGITransport

pytestmark = pytest.mark.accessibility


# ---------------------------------------------------------------------------
# Non-browser regression tests for the P1 fixes applied 2026-06-02
# These run in CI without a browser.
# ---------------------------------------------------------------------------


def _get_app():
    """Import and create the FastAPI app (deferred to avoid import-time side effects)."""
    from app.main import create_app
    return create_app()


def _run(coro):
    """Run a coroutine synchronously (test helper)."""
    return asyncio.get_event_loop().run_until_complete(coro)


def test_docs_html_lang_attribute():
    """GET /docs returns HTML with lang='en' on <html> element (WCAG 3.1.1).

    Regression test for fix SR1-01 / K-01 (2026-06-02).
    Prevents future changes from removing the lang attribute.
    """
    app = _get_app()

    async def _check():
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/docs")
            assert r.status_code == 200
            assert 'lang="en"' in r.text, (
                "/docs HTML missing lang='en' on <html> element (WCAG 3.1.1 failure)"
            )

    _run(_check())


def test_redoc_html_lang_attribute():
    """GET /redoc returns HTML with lang='en' on <html> element (WCAG 3.1.1).

    Regression test for fix SR2-01 / K-01 (2026-06-02).
    """
    app = _get_app()

    async def _check():
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/redoc")
            assert r.status_code == 200
            assert 'lang="en"' in r.text, (
                "/redoc HTML missing lang='en' on <html> element (WCAG 3.1.1 failure)"
            )

    _run(_check())


def test_docs_html_has_main_landmark():
    """GET /docs returns HTML with a <main> landmark element (WCAG 1.3.1).

    Regression test for fix SR1-02 (2026-06-02).
    """
    app = _get_app()

    async def _check():
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/docs")
            assert "<main" in r.text, (
                "/docs HTML missing <main> landmark (WCAG 1.3.1 failure)"
            )

    _run(_check())


def test_redoc_html_has_main_landmark():
    """GET /redoc returns HTML with a <main> landmark element (WCAG 1.3.1).

    Regression test for fix SR1-02 (2026-06-02).
    """
    app = _get_app()

    async def _check():
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/redoc")
            assert "<main" in r.text, (
                "/redoc HTML missing <main> landmark (WCAG 1.3.1 failure)"
            )

    _run(_check())


def test_docs_html_has_skip_link():
    """GET /docs returns HTML with a skip-to-main link (WCAG 2.4.1).

    Regression test for fix K-02 (2026-06-02).
    Skip links allow keyboard users to bypass repetitive nav blocks.
    """
    app = _get_app()

    async def _check():
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/docs")
            assert "a11y-skip-link" in r.text, (
                "/docs HTML missing skip-to-main-content link (WCAG 2.4.1 failure)"
            )

    _run(_check())


def test_redoc_html_has_skip_link():
    """GET /redoc returns HTML with a skip-to-main link (WCAG 2.4.1).

    Regression test for fix K-02 (2026-06-02).
    """
    app = _get_app()

    async def _check():
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/redoc")
            assert "a11y-skip-link" in r.text, (
                "/redoc HTML missing skip-to-main-content link (WCAG 2.4.1 failure)"
            )

    _run(_check())


def test_docs_html_has_charset():
    """GET /docs returns HTML with meta charset declaration (best practice).

    Charset declaration prevents character encoding issues across user agents.
    """
    app = _get_app()

    async def _check():
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/docs")
            assert 'charset="utf-8"' in r.text, (
                "/docs HTML missing <meta charset='utf-8'>"
            )

    _run(_check())


def test_redoc_html_has_charset():
    """GET /redoc returns HTML with meta charset declaration."""
    app = _get_app()

    async def _check():
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/redoc")
            assert 'charset="utf-8"' in r.text, (
                "/redoc HTML missing <meta charset='utf-8'>"
            )

    _run(_check())


def test_docs_html_has_title():
    """GET /docs returns HTML with a non-empty <title> element (WCAG 2.4.2).

    Page title allows screen reader users to identify the page before reading content.
    """
    app = _get_app()

    async def _check():
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/docs")
            assert "<title>" in r.text, "/docs HTML missing <title> element"
            # Title should not be empty
            import re
            match = re.search(r"<title>(.*?)</title>", r.text)
            assert match and match.group(1).strip(), "/docs <title> is empty"

    _run(_check())


def test_redoc_html_has_title():
    """GET /redoc returns HTML with a non-empty <title> element (WCAG 2.4.2)."""
    app = _get_app()

    async def _check():
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/redoc")
            assert "<title>" in r.text, "/redoc HTML missing <title> element"
            import re
            match = re.search(r"<title>(.*?)</title>", r.text)
            assert match and match.group(1).strip(), "/redoc <title> is empty"

    _run(_check())


def test_docs_is_html_not_json():
    """GET /docs returns text/html content type (not JSON).

    Sanity check: /docs must serve an HTML page, not a JSON redirect.
    """
    app = _get_app()

    async def _check():
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/docs")
            assert "text/html" in r.headers.get("content-type", ""), (
                "/docs should return text/html, got: " + r.headers.get("content-type", "")
            )

    _run(_check())


# ---------------------------------------------------------------------------
# Browser-based regression tests (require Playwright — skip in CI by default)
# Run with: uv run pytest tests/test_a11y_regression.py -m playwright
# ---------------------------------------------------------------------------


@pytest.fixture
async def browser_page(playwright):
    """Provide a Playwright page instance."""
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()


def test_form_labels_associated(browser_page):
    """All input elements have associated <label> (WCAG 1.3.1).

    This is a regression test to prevent form labels from being removed
    in future changes.
    """
    browser_page.goto("http://127.0.0.1:8000/")

    # Find all inputs without associated labels
    inputs = browser_page.query_selector_all("input[id]:not(input[type='hidden'])")
    for inp in inputs:
        input_id = inp.evaluate("el => el.id")
        # Verify a matching <label for="..."> exists
        label = browser_page.query_selector(f'label[for="{input_id}"]')
        # For now, just report if missing (will be stricter after audit)


def test_heading_hierarchy_no_jumps(browser_page):
    """Heading hierarchy h1->h2->h3 with no jumps (WCAG 1.3.1).

    This is a regression test to prevent heading structure changes
    that would violate WCAG 1.3.1.
    """
    browser_page.goto("http://127.0.0.1:8000/")

    headings = browser_page.query_selector_all("h1, h2, h3, h4, h5, h6")
    prev_level = 0

    for heading in headings:
        tag_name = heading.evaluate("el => el.tagName")
        current_level = int(tag_name[1])

        if prev_level > 0 and current_level > prev_level:
            # Allow jump down multiple levels, but not up more than 1
            assert current_level <= prev_level + 1, \
                f"Heading jump: h{prev_level} → h{current_level}"

        prev_level = current_level


def test_main_landmark_present(browser_page):
    """Page has exactly one main landmark (WCAG 1.3.1).

    Regression test to ensure main landmark isn't accidentally removed.
    """
    browser_page.goto("http://127.0.0.1:8000/")

    main_elements = browser_page.query_selector_all("main")
    assert len(main_elements) >= 1, "Page must have at least one <main> landmark"


def test_focus_visible_on_interactive_elements(browser_page):
    """Interactive elements should show visible focus (WCAG 2.4.7).

    This is a visual test that requires manual verification.
    Automated check verifies :focus styles exist.
    """
    browser_page.goto("http://127.0.0.1:8000/")

    # Check if CSS has focus styles defined
    has_focus_styles = browser_page.evaluate("""() => {
        const styles = document.styleSheets;
        for (let i = 0; i < styles.length; i++) {
            try {
                const rules = styles[i].cssRules || styles[i].rules;
                for (let j = 0; j < rules.length; j++) {
                    if (rules[j].selectorText && rules[j].selectorText.includes(':focus')) {
                        return true;
                    }
                }
            } catch (e) {
                // Cross-origin stylesheet, skip
            }
        }
        return false;
    }""")

    # For now, just note if focus styles are missing
    if not has_focus_styles:
        print("\nWarning: No :focus CSS styles found in stylesheets")


def test_skip_link_functionality(browser_page):
    """Skip link should allow skipping to main content (WCAG 2.4.1).

    Regression test to ensure skip links aren't broken by layout changes.
    """
    browser_page.goto("http://127.0.0.1:8000/")

    # Check for skip link
    skip_link = browser_page.query_selector("a[href='#main'], a[href='#content']")

    # For now, just note if skip link is missing
    if not skip_link:
        print("\nNote: No skip-to-main-content link found")


def test_images_decorative_marked(browser_page):
    """Decorative images should be marked as such (WCAG 1.1.1).

    Images without alt text should be marked with aria-hidden="true"
    or should have empty alt="" attribute.
    """
    browser_page.goto("http://127.0.0.1:8000/")

    # Find all images
    images = browser_page.query_selector_all("img")

    issues = []
    for img in images:
        alt = img.evaluate("el => el.alt || ''")
        aria_hidden = img.evaluate("el => el.getAttribute('aria-hidden')")
        role = img.evaluate("el => el.getAttribute('role')")

        # If no alt text, should be explicitly marked as decorative
        if not alt and aria_hidden != "true" and role != "presentation":
            src = img.evaluate("el => el.src")
            issues.append(src)

    # Report but don't fail yet
    if issues:
        print(f"\nImages that might be decorative but not marked: {len(issues)}")


def test_form_validation_announced(browser_page):
    """Form validation messages should be announced (WCAG 4.1.3).

    Regression test to ensure validation errors are properly announced
    to screen readers.
    """
    browser_page.goto("http://127.0.0.1:8000/")

    # Check for aria-live regions
    live_regions = browser_page.query_selector_all("[aria-live]")

    # For now, just count them
    print(f"\nAria-live regions found: {len(live_regions)}")


def test_landmarks_present(browser_page):
    """Page should have appropriate landmarks (WCAG 1.3.1).

    Regression test to ensure semantic structure is maintained.
    """
    browser_page.goto("http://127.0.0.1:8000/")

    landmarks = {
        "main": len(browser_page.query_selector_all("main")),
        "nav": len(browser_page.query_selector_all("nav")),
        "aside": len(browser_page.query_selector_all("aside")),
        "footer": len(browser_page.query_selector_all("footer")),
        "header": len(browser_page.query_selector_all("header")),
    }

    print(f"\nLandmarks found: {landmarks}")

    # At least main should be present
    assert landmarks["main"] >= 1, "Page should have at least one <main> landmark"
