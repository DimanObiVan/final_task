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

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is abscent!"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is abscent!"
    
    def register_new_user(self, email, password):
        browser = webdriver.Chrome()
        mail = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        mail.send_keys(email)
        password1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password1.send_keys(password)
        confirmPassword = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        confirmPassword.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
        
