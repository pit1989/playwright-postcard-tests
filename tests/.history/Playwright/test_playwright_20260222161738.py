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

def test_upload_photo(page):
    """
    SMK-4. Проверка загрузки фото
    """
    # 1. Открываем страницу
    page.goto(URL)

    # 2. Находим input для файлов
    file_input = page.locator("input[type='file']")

    # 3. Путь к файлу (лучше без кириллицы в имени файла)
    file_path = "C:/Users/Admin/Desktop/обл.png"

    # 4. Загружаем файл напрямую через input
    file_input.set_input_files(file_path)

    # 5. Ждём появления превью
    preview = page.locator("#photoContainer > div:nth-child(3) > img")
    preview.wait_for(state="visible", timeout=10000)  # ждём до 10 секунд

    # 6. Проверка, что src превью не пустой
    src = preview.get_attribute("src")
    assert src, "Превью не появилось или пустое"