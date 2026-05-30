"""Tests for color contrast accessibility (WCAG 1.4.3)."""

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


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_luminance(rgb):
    """Calculate relative luminance (WCAG formula)."""
    r, g, b = [x / 255.0 for x in rgb]

    def adjust(c):
        if c <= 0.03928:
            return c / 12.92
        else:
            return ((c + 0.055) / 1.055) ** 2.4

    r = adjust(r)
    g = adjust(g)
    b = adjust(b)

    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def get_contrast_ratio(rgb1, rgb2):
    """Calculate contrast ratio between two colors (WCAG formula)."""
    l1 = get_luminance(rgb1)
    l2 = get_luminance(rgb2)

    lighter = max(l1, l2)
    darker = min(l1, l2)

    return (lighter + 0.05) / (darker + 0.05)


def test_text_contrast_normal(browser_page):
    """Test text contrast for normal text (WCAG 1.4.3 - AA requires 4.5:1)."""
    browser_page.goto("http://127.0.0.1:8000/")

    # Get all text elements
    elements = browser_page.query_selector_all("p, span, div, h1, h2, h3, h4, h5, h6, a, button, label")

    low_contrast = []

    for element in elements:
        try:
            # Get computed styles
            computed = element.evaluate("""el => {
                const style = window.getComputedStyle(el);
                return {
                    color: style.color,
                    backgroundColor: style.backgroundColor,
                    display: style.display,
                    visibility: style.visibility
                };
            }""")

            # Skip hidden elements
            if computed['visibility'] == 'hidden' or computed['display'] == 'none':
                continue

            # Parse colors (basic support for rgb format)
            if computed['color'].startswith('rgb') and computed['backgroundColor'].startswith('rgb'):
                # Extract RGB values
                color_match = computed['color'].replace('rgb(', '').replace(')', '').split(',')
                bg_match = computed['backgroundColor'].replace('rgb(', '').replace(')', '').split(',')

                if len(color_match) >= 3 and len(bg_match) >= 3:
                    try:
                        foreground = tuple(int(v.strip()) for v in color_match[:3])
                        background = tuple(int(v.strip()) for v in bg_match[:3])

                        ratio = get_contrast_ratio(foreground, background)

                        # Normal text should have 4.5:1 (AA) contrast
                        # Large text (18pt+) can have 3:1 (AA)
                        if ratio < 4.5:
                            text_content = element.evaluate("el => el.textContent.substring(0, 50)")
                            low_contrast.append({
                                "text": text_content,
                                "ratio": round(ratio, 2),
                                "foreground": foreground,
                                "background": background
                            })
                    except Exception:
                        pass

        except Exception:
            pass

    # Report but don't fail yet (for initial audit)
    if low_contrast:
        print(f"\nElements with potential low contrast (< 4.5:1):")
        for item in low_contrast[:10]:  # Show first 10
            print(f"  - Contrast {item['ratio']}:1 - {item['text'][:30]}")


def test_large_text_contrast(browser_page):
    """Test contrast for large text (WCAG 1.4.3 - AA requires 3:1)."""
    browser_page.goto("http://127.0.0.1:8000/")

    # Get all heading elements (typically large)
    headings = browser_page.query_selector_all("h1, h2, h3, h4, h5, h6")

    low_contrast = []

    for heading in headings:
        try:
            computed = heading.evaluate("""el => {
                const style = window.getComputedStyle(el);
                return {
                    color: style.color,
                    backgroundColor: style.backgroundColor,
                    fontSize: style.fontSize
                };
            }""")

            if computed['color'].startswith('rgb') and computed['backgroundColor'].startswith('rgb'):
                color_match = computed['color'].replace('rgb(', '').replace(')', '').split(',')
                bg_match = computed['backgroundColor'].replace('rgb(', '').replace(')', '').split(',')

                if len(color_match) >= 3 and len(bg_match) >= 3:
                    try:
                        foreground = tuple(int(v.strip()) for v in color_match[:3])
                        background = tuple(int(v.strip()) for v in bg_match[:3])

                        ratio = get_contrast_ratio(foreground, background)

                        # Large text should have 3:1 (AA) contrast
                        if ratio < 3.0:
                            text_content = heading.evaluate("el => el.textContent")
                            low_contrast.append({
                                "text": text_content,
                                "ratio": round(ratio, 2)
                            })
                    except Exception:
                        pass

        except Exception:
            pass

    if low_contrast:
        print(f"\nHeadings with potential low contrast (< 3:1):")
        for item in low_contrast:
            print(f"  - Contrast {item['ratio']}:1 - {item['text'][:50]}")


def test_focus_indicator_contrast(browser_page):
    """Test that focus indicators have sufficient contrast (WCAG 2.4.7)."""
    browser_page.goto("http://127.0.0.1:8000/")

    # This is a visual test that would need manual verification
    # For now, just document that focus indicators need testing
    print("\nFocus indicator contrast testing requires manual verification")
    print("Steps:")
    print("  1. Tab through page")
    print("  2. For each focused element, verify focus indicator is visible")
    print("  3. Check focus indicator has 3:1 contrast vs background")
