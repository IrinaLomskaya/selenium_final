import pytest
from selenium import webdriver

"""
Открытие/зактрытие браузера
"""
@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()
