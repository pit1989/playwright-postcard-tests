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
    page.goto(URL)

    file_input = page.locator("input[type='file']")

    file_path = "C:/Users/Admin/Desktop/обл.png"

    file_input.set_input_files(file_path)

    preview = page.locator("#photoContainer > div:nth-child(3) > img")

    src = preview.get_attribute("src")
    assert src, "Превью не появилось или пустое"

def test_btn_input_upload_img(page):
    """
    SMK-5. Positive case input upload img
    """
    URL = "https://postcard.qa.studio/"
    page.goto(URL)

    # Проверяем видимость кнопки
    upload_label = page.locator("div.photo-input__add label div")
    assert upload_label.is_visible(), "Кнопка загрузки фото не видна"

def test_preview(page):
    """
    SMK-6. Проверка, что после загрузки файла появляется превью
    """
    import os

    URL = "https://postcard.qa.studio/"
    file_path = "C:/Users/Admin/Desktop/обл.png"

    assert os.path.exists(file_path), f"Файл не найден: {file_path}"

    page.goto(URL)

    # Загружаем файл
    file_input = page.locator("input[type='file']")
    file_input.set_input_files(file_path)

    # Проверяем появление превью
    preview = page.locator("#photoContainer > div:nth-child(3) > img")
    src = preview.get_attribute("src")
    assert src, "Превью изображения отсутствует"

    import os

def test_h1_title(page):
    page.goto(URL)
    header_text = page.locator("body > header > h1").inner_text()
    assert header_text != "", "Заголовок пустой"

def test_upload_button_visible(page):
    page.goto(URL)
    upload_btn = page.locator("div.photo-input__add label div")
    assert upload_btn.is_visible(), "Кнопка загрузки фото не видна"

def test_preview_visible(page):
    page.goto(URL)
    file_path = "C:/Users/Admin/Desktop/обл.png"

    file_input = page.locator("input[type='file']")
    file_input.set_input_files(file_path)

    preview = page.locator("#photoContainer > div:nth-child(3) > img")
    assert preview.is_visible(), "Превью изображения отсутствует"