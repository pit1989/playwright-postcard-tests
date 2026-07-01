URL = "https://postcard.qa.studio/"

def test_smoke(page):
    """
    SMK-1. Positive case p
    """
    page.goto(URL)
    button_text = page.locator("#send").inner_text()
    assert button_text == "Отправить", "Unexpected text on button"

def test_email_error(page):
    """
    SMK-2. Проверка email ошибки
    """
    page.goto(URL)
    page.locator("#email").fill("test@mail.com")
    page.locator("#send").click()
    error_text = page.locator("div.email > h2").inner_text()
    assert error_text != "", "Нет запрещающего слогана"

def test_paragraph_not_empty(page):
    """
    SMK-3. Проверка абзаца
    """
    page.goto(URL)
    paragraph_text = page.locator("body > header > p").inner_text()
    assert paragraph_text != "", "Абзац пустой"