import pytest
from playwright.sync_api import Page, expect, Browser

# Специальная фикстура, которая отключает проверку SSL-сертификатов на время теста
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True # Вот эта магия!
    }

def test_scroll_to_top_button_presence(page: Page):
    # 1. Предусловие: Открываем сайт
    page.goto("https://www.biblio-klin.ru/")
    
    # 2. Шаг 1: Имитируем скролл вниз на 1000 пикселей
    page.evaluate("window.scrollTo(0, 1000)")
    
    # Даем полсекунды на прогрузку анимации
    page.wait_for_timeout(500)
    
    # 3. Шаг 2: Ищем на странице кнопку «Наверх»
    up_button = page.locator("button:has-text('Наверх'), .scroll-to-top, #scrollUp")
    
    # 4. Проверка (Assert): Ожидаем, что кнопка видна на экране
    # Теперь тест упадет именно тут, потому что кнопки нет на сайте!
    expect(up_button).to_be_visible(timeout=3000)
