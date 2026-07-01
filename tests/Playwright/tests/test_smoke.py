from playwright.sync_api import expect

def test_smoke(postcard):
    expect(postcard.send_button).to_have_text("Отправить")