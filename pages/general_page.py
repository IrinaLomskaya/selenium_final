import time

from .base_page import BasePage
from .locators import BasePageLocators


class GeneralPage(BasePage):
    def check_norm_prav_menu(self):
        assert self.is_element_present(*BasePageLocators.NORM_PRAV_MENU), "Normatino pravovoe menu is not present"

    def check_oper_data_menu(self):
        assert self.is_element_present(*BasePageLocators.OPER_DATA_MENU), "Oper data menu is not present"

    def check_reports_menu(self):
        assert self.is_element_present(*BasePageLocators.REPORTS_MENU), "Reports menu is not present"

    def check_digital_docs_menu(self):
        assert self.is_element_present(*BasePageLocators.DIGITAL_DOCS_MENU), "Digital docs menu is not present"

    def norm_prav_menu_url(self):
        norm_prav_element = self.browser.find_element(*BasePageLocators.NORM_PRAV_MENU)
        time.sleep(1)
        norm_prav_element.click()
        time.sleep(1)
        assert 'nciminobr' in self.browser.current_url, "Norm prav is not in url"

    def reports_menu(self):
        reports_menu_element = self.browser.find_element(*BasePageLocators.REPORTS_MENU)
        time.sleep(1)
        reports_menu_element.click()
        time.sleep(1)
        assert '/report/' in self.browser.current_url, "Report menu is not in url"

    def exit_from_general_menu(self):
        exit_button = self.browser.find_element(*BasePageLocators.EXIT_BUTTON)
        assert self.is_element_present(*BasePageLocators.EXIT_BUTTON), "Exit button is not here"
        exit_button.click()

