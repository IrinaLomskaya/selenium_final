import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def check_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def check_password_form(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FORM)

    def check_submit_button(self):
        assert self.is_element_present(*LoginPageLocators.SUBMIT_BUTTON)

    def login_user(self, login, password):
        input_login = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        input_login.send_keys(login)
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        input_password.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_button.click()
        time.sleep(2)
