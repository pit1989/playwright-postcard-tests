from playwright.sync_api import expect
import re

FILE = "C:/Users/Admin/Desktop/обл.png"

def test_upload_image(postcard):
    postcard.upload_file(FILE)

    expect(postcard.preview_image).to_be_visible()


def test_switch_image(postcard):
    postcard.upload_file(FILE)

    postcard.select_third_image()
    postcard.select_second_image()

    expect(postcard.second_img_container).to_have_class(re.compile("chosen"))
    expect(postcard.third_img_container).not_to_have_class(re.compile("chosen"))