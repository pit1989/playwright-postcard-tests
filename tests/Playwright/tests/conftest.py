import pytest
from pages.postcard_page import PostcardPage

@pytest.fixture
def postcard(page):
    page.goto("https://postcard.qa.studio/")
    return PostcardPage(page)