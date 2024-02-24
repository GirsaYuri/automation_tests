import time

from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'Not found "login" in url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Not found login form'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Not found register form'

    def register_new_user(self):
        email = str(time.time()) + '@mail.ru'
        password = str(time.time()) + '123'
        self.browser.find_element(*LoginPageLocators.EMAIL_FORM).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FORM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
        assert self.browser.find_element(*BasePageLocators.USER_ICON), 'Guest not can register'
