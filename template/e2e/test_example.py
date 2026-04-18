import pytest
from playwright.sync_api import Page, expect


@pytest.mark.e2e
def test_homepage_loads(page: Page):
    """Test that the homepage loads successfully."""
    page.goto("http://localhost:8000/")
    page.wait_for_load_state("networkidle")
    expect(page).to_have_title(/{{ project_name }}/i)


@pytest.mark.e2e
def test_form_submission(page: Page):
    """Test that form submission works."""
    page.goto("http://localhost:8000/")
    page.wait_for_load_state("networkidle")

    name = page.locator('#name')
    message = page.locator('#message')
    submit = page.locator('button[type="submit"]')

    name.fill("Test User")
    message.fill("Hello from e2e test!")
    submit.click()

    page.wait_for_timeout(500)
    expect(page.locator('.greeting')).to_contain_text("Test User")