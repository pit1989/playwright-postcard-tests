import pytest
from pages.postcard_page import PostcardPage

@pytest.fixture(scope="function")
def postcard(page):
    # Фикстура 'page' предоставляется плагином pytest-playwright автоматически!
    # Она сама создается в фоновом режиме (headless в CI и с окном локально).
    postcard = PostcardPage(page)
    postcard.open()
    yield postcard
    # Закрывать страницу вручную не нужно, плагин сделает это сам


