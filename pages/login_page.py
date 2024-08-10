from .locators import LoginPageLocators
from .base_page import BasePage
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        browser = webdriver.Chrome()
        browser.get(LoginPageLocators.LOGIN_URL)
        assert "login" in browser.current_url, "Login link is incorrect!"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is abscent!"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is abscent!"
