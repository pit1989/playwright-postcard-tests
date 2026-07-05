import os

class PostcardPage:
    def __init__(self, page):
        self.page = page
        self.send_button = page.locator("#send")
        self.email_input = page.locator("#email")
        self.email_error = page.locator("div.email > h2")
        self.required_error = page.locator("div.photo-input__header > h2:nth-child(1)")
        self.upload_label = page.locator("div.photo-input__add label div")
        self.file_input = page.locator("input[type='file']")
        
        # Исправленный локатор превью (один .last вместо двух)
        self.preview_image = page.locator("#photoContainer img").last
        
        self.third_img_container = page.locator("#photoContainer > div").nth(1)
        self.second_img_container = page.locator("#photoContainer > div").nth(0)
        self.modal = page.locator("#modal")
        self.message_input = page.locator("#textarea")
        self.required_toHide_error = page.locator("h2.required.toHide.error, h2.requered.toHide.error")
        self.close_modal_button = page.locator("#cross")
        

    def open(self):
        self.page.goto("https://postcard.qa.studio/")

    def click_send(self):
        self.send_button.click()

    def upload_file(self, file_path):
        assert os.path.exists(file_path), f"Файл не найден: {file_path}"
        self.file_input.set_input_files(file_path)

    def select_third_image(self):
        self.third_img_container.click()

    def select_second_image(self):
        self.second_img_container.click()

    def fill_email(self, email):
        self.email_input.fill(email)
    
    def close_modal(self):
        self.close_modal_button.click()

    def fill_message(self, text):
        self.message_input.fill(text)

    def get_message_value(self):
        return self.message_input.input_value()
