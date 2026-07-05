import os
import pytest
from playwright.sync_api import sync_playwright
from pages.postcard_page import PostcardPage

@pytest.fixture(scope="session")
def playwright_instance():
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()

@pytest.fixture(scope="session")
def browser(playwright_instance):
    is_ci = os.getenv("CI") == "true"
    browser = playwright_instance.chromium.launch(headless=is_ci)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def postcard(browser):
    context = browser.new_context()
    page = context.new_page()
    postcard = PostcardPage(page)
    postcard.open()
    yield postcard
    context.close()


