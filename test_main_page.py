from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium import webdriver
import pytest
import time

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()
        
@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    # page.add_to_cart()
    page.go_to_basket()
    # time.sleep(3)
    page.basket_is_empty()
    page.basket_is_empty_text() 

    
def test_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()
    browser.quit()
    
def test_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/" 
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()
    
def test_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/" 
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()