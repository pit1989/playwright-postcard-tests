from playwright.sync_api import expect

def test_empty_email(postcard):
    postcard.fill_email("")
    postcard.click_send()

    expect(postcard.required_error).to_be_visible()


def test_empty_form(postcard):
    postcard.click_send()

    expect(postcard.modal).not_to_be_visible()
    expect(postcard.required_error).to_be_visible()


def test_error_state_not_reset(postcard):
    postcard.fill_email("")
    postcard.click_send()

    expect(postcard.required_error).to_be_visible()

    postcard.fill_email("test@mail.com")

    expect(postcard.required_error).not_to_be_visible()