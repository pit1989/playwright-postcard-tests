from playwright.sync_api import expect
import pytest

FILE = "C:/Users/Admin/Desktop/обл.png"


def test_valid_submit(postcard):
    postcard.fill_email("test@mail.com")
    postcard.select_second_image()

    postcard.click_send()

    expect(postcard.modal).to_be_visible()


def test_submit_without_email_bug(postcard):
    postcard.upload_file(FILE)
    postcard.select_second_image()

    postcard.click_send()

    expect(postcard.modal).to_be_visible()


@pytest.mark.parametrize(
    "email, upload_image, expected",
    [
        ("", False, "required_error"),
        ("123", False, "email_error"),
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