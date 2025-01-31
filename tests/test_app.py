import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.timeout(30)
def test_ask_question():
    with sync_playwright() as p:
        # Launch the browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("http://localhost:8080")
        page.wait_for_load_state("networkidle")

        # Find the text input element and type the question
        text_input = page.locator("input[aria-label='Stelle eine Frage oder gib ein Stichwort ein']")
        text_input.fill("Wie sieht die Steuerpolitik der Parteien aus?")
        page.wait_for_timeout(200)

        # Find and click the "Frage stellen" button
        submit_button = page.locator("p:text('Frage stellen')")
        submit_button.click()

        page.wait_for_selector("h2#spd")

        error_elements = page.locator("text=Error").count()
        # Close the browser
        browser.close()

        assert error_elements == 0, "Found error messages on page"
