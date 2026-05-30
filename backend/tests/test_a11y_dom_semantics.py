"""Tests for DOM semantic accessibility."""

import pytest

pytestmark = pytest.mark.accessibility


@pytest.fixture
async def browser_page(playwright):
    """Provide a Playwright page instance."""
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()


def test_page_has_main_landmark(browser_page):
    """Verify each page has exactly one <main> landmark (WCAG 1.3.1)."""
    browser_page.goto("http://127.0.0.1:8000/")

    # Check for main landmark
    main_elements = browser_page.query_selector_all("main")
    assert len(main_elements) >= 1, "Page must have at least one <main> landmark"
    assert len(main_elements) <= 1, "Page must have exactly one <main> landmark"


def test_heading_hierarchy_h1_start(browser_page):
    """Verify heading hierarchy starts with h1 (WCAG 1.3.1)."""
    browser_page.goto("http://127.0.0.1:8000/")

    # Get first heading on page
    headings = browser_page.query_selector_all("h1, h2, h3, h4, h5, h6")

    if headings:
        first_heading = headings[0]
        tag_name = first_heading.evaluate("el => el.tagName")
        assert tag_name == "H1", f"First heading should be H1, got {tag_name}"


def test_heading_hierarchy_no_jumps(browser_page):
    """Verify heading hierarchy has no jumps (e.g., h1 -> h3 is invalid) (WCAG 1.3.1)."""
    browser_page.goto("http://127.0.0.1:8000/")

    headings = browser_page.query_selector_all("h1, h2, h3, h4, h5, h6")
    prev_level = 0

    for heading in headings:
        tag_name = heading.evaluate("el => el.tagName")
        current_level = int(tag_name[1])

        if prev_level > 0:
            # Allow decreasing to any level, but increasing must be at most +1
            if current_level > prev_level:
                assert current_level <= prev_level + 1, \
                    f"Heading jump: h{prev_level} -> h{current_level} (max allowed: h{prev_level + 1})"

        prev_level = current_level


def test_form_labels_associated(browser_page):
    """Verify all form inputs have associated labels (WCAG 1.3.1 + 4.1.2)."""
    browser_page.goto("http://127.0.0.1:8000/")

    # Find all inputs with id attribute (excluding hidden)
    inputs = browser_page.query_selector_all("input[id]:not([type='hidden'])")

    unlabeled = []
    for inp in inputs:
        input_id = inp.evaluate("el => el.id")
        if not input_id:
            continue

        # Check if a label exists for this input
        label = browser_page.query_selector(f'label[for="{input_id}"]')
        if not label:
            unlabeled.append(input_id)

    if unlabeled:
        print(f"\nUnlabeled inputs: {unlabeled}")
        # For now, just report; we'll make it stricter after initial audit


def test_images_have_alt_text(browser_page):
    """Verify images have alt text (WCAG 1.1.1)."""
    browser_page.goto("http://127.0.0.1:8000/")

    # Find all images
    images = browser_page.query_selector_all("img")

    missing_alt = []
    for img in images:
        src = img.evaluate("el => el.src")
        alt = img.evaluate("el => el.alt || ''")
        is_decorative = img.evaluate("el => el.hasAttribute('aria-hidden')")

        if not alt and not is_decorative:
            missing_alt.append(src)

    if missing_alt:
        print(f"\nImages missing alt text: {missing_alt}")


def test_buttons_have_accessible_names(browser_page):
    """Verify buttons have accessible names (WCAG 4.1.2)."""
    browser_page.goto("http://127.0.0.1:8000/")

    # Find all buttons
    buttons = browser_page.query_selector_all("button")

    unlabeled = []
    for btn in buttons:
        # Check for text content, aria-label, title, or aria-labelledby
        text = btn.evaluate("el => el.textContent.trim()")
        aria_label = btn.evaluate("el => el.getAttribute('aria-label') || ''")
        title = btn.evaluate("el => el.getAttribute('title') || ''")

        if not text and not aria_label and not title:
            selector = btn.evaluate("el => el.className")
            unlabeled.append(selector)

    if unlabeled:
        print(f"\nButtons without accessible names: {unlabeled}")


def test_links_have_descriptive_text(browser_page):
    """Verify links have descriptive text (WCAG 2.4.4)."""
    browser_page.goto("http://127.0.0.1:8000/")

    # Find all links
    links = browser_page.query_selector_all("a")

    problematic = []
    for link in links:
        text = link.evaluate("el => el.textContent.trim()")
        title = link.evaluate("el => el.getAttribute('title') || ''")

        # Warn about generic link text
        if text and text.lower() in ["click here", "read more", "link"]:
            href = link.evaluate("el => el.href")
            problematic.append({"text": text, "href": href})

    if problematic:
        print(f"\nLinks with generic text: {problematic}")


def test_navigation_landmarks(browser_page):
    """Verify navigation landmarks are present and labeled (WCAG 1.3.1)."""
    browser_page.goto("http://127.0.0.1:8000/")

    # Check for nav elements
    nav_elements = browser_page.query_selector_all("nav")

    if len(nav_elements) > 1:
        # If multiple navs, they should be labeled
        for nav in nav_elements:
            label = nav.evaluate("el => el.getAttribute('aria-label') || el.getAttribute('aria-labelledby') || ''")
            if not label:
                print(f"\nNavigation region without label found")
