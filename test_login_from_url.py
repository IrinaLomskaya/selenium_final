import pytest
from .pages.login_page import LoginPage
from .pages.general_page import GeneralPage

link = ""

"""
Проверка присутствия элементов на странице авторизации
"""
def test_login_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.check_login_form()
    page.check_password_form()
    page.check_submit_button()

"""
Проверка авторизации. присутствия элементов на главной странице, переход по этим эдементам
"""
class TestGeneralPageUsage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.login_user(login="", password="")
        page.open()

    def test_general_page(self, browser):
        page_general = GeneralPage(browser, browser.current_url)
        page_general.open()
        page_general.check_digital_docs_menu()
        page_general.check_oper_data_menu()
        page_general.norm_prav_menu_url()
        page_general.exit_from_general_menu()

    def test_general_page_report_menu(self, browser):
        page_general = GeneralPage(browser, browser.current_url)
        page_general.open()
        page_general.check_reports_menu()
        page_general.reports_menu()
        page_general.exit_from_general_menu()
