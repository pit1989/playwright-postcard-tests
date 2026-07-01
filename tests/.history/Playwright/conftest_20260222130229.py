import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")  # можно "session" если один браузер на все тесты
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True если не нужно окно
        page = browser.new_page()
        yield page
        browser.close()