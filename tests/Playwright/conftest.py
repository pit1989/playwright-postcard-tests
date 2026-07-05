import os
import pytest
from playwright.sync_api import sync_playwright
from pages.postcard_page import PostcardPage

@pytest.fixture(scope="session")
def playwright_instance():
    # Запускаем сам движок Playwright на всю сессию
    playwright = sync_playwright().start()
    yield playwright
    playwright.stop()

@pytest.fixture(scope="session")
def browser(playwright_instance):
    # Проверяем, запущен ли тест в облаке GitHub Actions (там всегда переменная CI равна 'true')
    is_ci = os.getenv("CI") == "true"
    
    # Если в CI — запускаем скрыто (headless=True), если у тебя на компе — с окном (headless=False)
    browser = playwright_instance.chromium.launch(headless=is_ci)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def postcard(browser):
    # Для каждого теста создаем чистый изолированный контекст и страницу
    context = browser.new_context()
    page = context.new_page()
    postcard = PostcardPage(page)
    postcard.open()
    yield postcard
    context.close() # Контекст закроет и страницу автоматически

