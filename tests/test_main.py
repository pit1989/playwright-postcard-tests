"""
2026 (c) Hawaii
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


URL = "https://postcard.qa.studio/"
CASE = [0, 1]

def test_smoke(browser):
    """
    SMK-1. Smoke test
    """
    browser.get(URL)

    button = browser.find_element(By.ID, value="send")
    assert button.text == "Отправить", "Unexpected text on button"

def test_empty_input_send(browser):
    """
    SMK-2. Negative case
    """
    browser.get(URL)

    email_label = browser.find_element(By.CSS_SELECTOR, value="div.email h2")
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == 'requered', "Unexpected attribute class"

    button = browser.find_element(By.ID, "send")
    button.click()

    email_label = browser.find_element(By.CSS_SELECTOR, "div.email h2")
    email_label_text = email_label.get_attribute("class")
    assert email_label_text == 'requered error', "Unexpected attribute class"

    assert "Отправить" in button.text, "Unexpected text on button"


@pytest.mark.parametrize('case', CASE)


def test_send_postcard(browser, case):
    """
    SMK-3. Positive case
    """
    browser.get(URL)

    email = browser.find_element(By.ID, "email")
    email.click()
    email.send_keys("shopa1@hmail.com")

    cards = browser.find_elements(By.CSS_SELECTOR, value='[class*="photo-parent"]')
    cards[case].click()

    message = browser.find_element(By.ID, "textarea")
    message.click()
    message.send_keys("Я крутой!")

    button = browser.find_element(By.ID, "send")
    button.click()

    modal = browser.find_element(By.ID, "modal")
    assert modal.text == "Открытка успешно отправлена!", ""

def test_h1(browser):
        """
        SMK-4. Positive case h1
        """
        browser.get(URL)

        h1 = browser.find_element(By.TAG_NAME, "h1")

        assert h1.text != "", "Заголовок пустой"

def test_p(browser):
        """
        SMK-5. Positive case p
        """
        browser.get(URL)

        element = browser.find_element(By.XPATH, "/html/body/header/p")

        assert element.text != "", "Абзац пустой" 

def test_btn_upload_img(browser):
       """
        SMK-6. Positive case upload img
        """
       browser.get(URL)

       upload_btn = browser.find_element(By.CSS_SELECTOR, "body > main > div.photo-input__container > div.photo-input__photo.photo-input__photo-plus.toHide > label > img")

       assert upload_btn.is_displayed(), "Кнопка загрузки изображения не отображается"

def test_btn_input_upload_img(browser):
    """
    SMK-7. Positive case input upload img
    """
    browser.get(URL)

    # --- проверяем видимость кнопки (берём видимый div внутри label, без класса hidden) ---
    upload_label = browser.find_element(By.CSS_SELECTOR, "div.photo-input__add label div")
    assert upload_label.is_displayed(), "Кнопка загрузки фото не видна"

    # --- находим input[type='file'] и загружаем файл напрямую ---
    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")

    # путь к файлу (файл реально должен существовать!)
    file_path = "C:/Users/Admin/Desktop/обл.png"
    
    import os
    assert os.path.exists(file_path), f"Файл не найден: {file_path}"

    file_input.send_keys(file_path)

def test_preview(browser):
    """
    SMK-8. Проверка, что после загрузки файла появляется превью
    """
    browser.get(URL)

    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_path = "C:/Users/Admin/Desktop/обл.png"
    
    import os
    assert os.path.exists(file_path), f"Файл не найден: {file_path}"
    
    file_input.send_keys(file_path)

    preview = browser.find_element(By.CSS_SELECTOR, "#photoContainer > div:nth-child(3) > img")
    assert preview.is_displayed(), "Превью изображения отсуствует" 

def test_select_upload_chosen_random(browser):
    """
    SMK-9. Проверка, появления галочки после выбора картинки
    """
    browser.get(URL)

    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_path = "C:/Users/Admin/Desktop/обл.png"
    
    import os
    assert os.path.exists(file_path), f"Файл не найден: {file_path}"
    
    file_input.send_keys(file_path)

    preview = browser.find_element(By.CSS_SELECTOR, "#photoContainer > div:nth-child(3) > img")
    assert preview.is_displayed(), "Превью изображения отсуствует" 

    image_container = browser.find_element(By.CSS_SELECTOR, "div.photo-input__photo-parent")
    image_container.click()

    assert "chosen" in image_container.get_attribute("class"), "Картинка не выбрана (класс chosen не появился)"

def test_select_img_chosen(browser):
    """
    SMK-11. Проверка загрузки 3 картинки и появления галочки после выбора
    """
    browser.get(URL)

    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_path = "C:/Users/Admin/Desktop/обл.png"
    
    import os
    assert os.path.exists(file_path), f"Файл не найден: {file_path}"
    
    file_input.send_keys(file_path)

    preview = browser.find_element(By.XPATH, '//*[@id="photoContainer"]/div[3]/img')
    assert preview.is_displayed(), "Превью изображения отсуствует" 

    image_container = preview.find_element(By.XPATH, "..")
    image_container.click()

    # --- Проверяем, что класс chosen появился ---
    assert "chosen" in image_container.get_attribute("class"), "Картинка не выбрана (класс chosen не появился)"

def test_switch_chosen(browser):
    """
    SMK-12. Проверка переключения галочек при выборе разных картинок
    """
    browser.get(URL)

    file_input = browser.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_path = "C:/Users/Admin/Desktop/обл.png"

    import os
    assert os.path.exists(file_path), f"Файл не найден: {file_path}"

    # Загружаем картинку
    file_input.send_keys(file_path)

    # Находим превью картинок
    third_img_container = browser.find_element(By.XPATH, '//*[@id="photoContainer"]/div[3]')
    second_img_container = browser.find_element(By.XPATH, '//*[@id="photoContainer"]/div[2]')

    # Выбираем первую картинку
    third_img_container.click()
    assert "chosen" in third_img_container.get_attribute("class"), "Третья картинка не выбрана"

    # Выбираем вторую картинку
    second_img_container.click()
    assert "chosen" in second_img_container.get_attribute("class"), "Вторая картинка не выбрана"

    # Проверяем, что первая картинка больше не выбрана
    assert "chosen" not in third_img_container.get_attribute("class"), "Первая картинка должна была снять галочку"


def test_empty_input_send_red(browser):
    """
    SMK-13. Проверяем появление всех красных надписей
    """
    browser.get(URL)

    button = browser.find_element(By. ID, "send").click()

    wait = WebDriverWait(browser, 5)

    email_label = browser.find_element(By.ID, "email")
    error_message = browser.find_element(By.CSS_SELECTOR, "div.email > h2")
    assert error_message.text != "", "Нет красной надписи 'Email кому дарим'" 

    requered_error = browser.find_element(By. CSS_SELECTOR, "div.photo-input__header > h2:nth-child(1)")
    assert requered_error.text != "", "Нету надписи 'Выберите открытку'"

    requered_toHide = browser.find_element(By.CSS_SELECTOR, "div.photo-input__header > h2.requered.toHide.error")
    assert requered_toHide.text != "", "Нету надписи 'Или загрузите свою'"

