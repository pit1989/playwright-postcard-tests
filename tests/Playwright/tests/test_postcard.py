import pytest
import re
from playwright.sync_api import expect

import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

FILE = os.path.join(CURRENT_DIR, "..", "resources", "kniga.png")


def test_fine_case(postcard):
    postcard.fill_email("manrock1989@mail.ru")
    postcard.select_second_image()
    
    postcard.click_send()

    expect(postcard.modal).to_be_visible()


def test_smoke(postcard):
    expect(postcard.send_button).to_have_text("Отправить")


def test_email_label(postcard):
    postcard.fill_email("")
    postcard.click_send()
    expect(postcard.required_error).to_be_visible()


def test_upload_button_visible(postcard):
    expect(postcard.upload_label).to_be_visible()


def test_upload_image(postcard):
    postcard.upload_file(FILE)
    expect(postcard.preview_image).to_be_visible()

def test_switch_image(postcard):
    postcard.upload_file(FILE)

    postcard.select_third_image()
    expect(postcard.third_img_container).to_have_class(re.compile("chosen"))

    postcard.select_second_image()
    expect(postcard.second_img_container).to_have_class(re.compile("chosen"))
    expect(postcard.third_img_container).not_to_have_class(re.compile("chosen"))


@pytest.mark.parametrize(
    "email, upload_image, expected",
    [
        ("", False, "required_error"),
        ("123", False, "email_error"),

        # ⚠️ ВАЖНО: без картинки логика может быть required_error
        ("test@example.com", False, "required_error"),

        ("test@example.com", True, "modal"),
    ]
)
def test_send(postcard, email, upload_image, expected):

    postcard.fill_email(email)

    if upload_image:
        postcard.upload_file(FILE)
        postcard.select_third_image()

    postcard.click_send()

    expect(getattr(postcard, expected)).to_be_visible()

def test_message_length_limit(postcard):
    postcard.fill_email("test@example.com")

    postcard.upload_file(FILE)
    postcard.select_third_image()

    postcard.fill_message("x" * 250)

    value = postcard.message_input.input_value()
    assert len(value) <= 250

def test_empty_no_modal(postcard):
    postcard.fill_email("")

    postcard.click_send()

    expect(postcard.modal).not_to_be_visible()
    expect(postcard.required_error).to_be_visible()
    expect(postcard.required_toHide_error).to_be_visible()

def test_empty_big_text_no_modal(postcard):
    postcard.fill_email("")
    postcard.fill_message("x" * 250)

    postcard.click_send()

    expect(postcard.modal).not_to_be_visible()
    expect(postcard.required_error).to_be_visible()
    expect(postcard.required_toHide_error).to_be_visible()

def test_empty_message(postcard):
    postcard.fill_email("test@example.com")

    postcard.upload_file(FILE)
    postcard.select_third_image()

    postcard.click_send()

    expect(postcard.modal).to_be_visible()

def test_image_selection_switch(postcard):
    postcard.upload_file(FILE)

    postcard.select_third_image()

    postcard.select_second_image()

    postcard.click_send()

    expect(postcard.modal).to_be_visible()

def test_image_selection_switch(postcard):
    postcard.upload_file(FILE)

    postcard.select_third_image()
    postcard.select_second_image()

    expect(postcard.second_img_container).to_have_class(re.compile("chosen"))
    expect(postcard.third_img_container).not_to_have_class(re.compile("chosen"))

def test_image_selection_switch_again(postcard):
    postcard.upload_file(FILE)

    postcard.select_third_image()

    postcard.select_second_image()

    postcard.click_send()

    expect(postcard.modal).to_be_visible()

    postcard.close_modal()

    postcard.select_second_image()

    postcard.click_send()

    expect(postcard.modal).to_be_visible()

def test_send_without_email_but_with_image(postcard):
    postcard.upload_file(FILE)
    postcard.select_second_image()

    postcard.click_send()

    expect(postcard.modal).to_be_visible()
    
@pytest.mark.xfail(reason="Реальный баг сайта: ошибка не исчезает при вводе email")
def test_error_state_not_reset(postcard):
    postcard.fill_email("")
    postcard.click_send()

    expect(postcard.required_error).to_be_visible()

    postcard.fill_email("test@mail.com")

    expect(postcard.required_error).not_to_be_visible()

def test_message_limit_not_enforced(postcard):
    postcard.fill_email("test@mail.com")
    postcard.upload_file(FILE)
    postcard.select_second_image()

    postcard.fill_message("x" * 300)
    postcard.click_send()

    expect(postcard.modal).to_be_visible()

def test_empty_form_send(postcard):
    postcard.click_send()

    expect(postcard.modal).not_to_be_visible()
    expect(postcard.required_error).to_be_visible()