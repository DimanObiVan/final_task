from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.product_page import ProductPage

from selenium import webdriver
import pytest
import time


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "Qwerty123!!!"
        page.register_new_user(email, password)
        page = ProductPage(browser, link)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.added_to_cart_message()
        page.added_book_name()
        page.added_book_price()
@pytest.mark.need_review   
    
def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        # page.solve_quiz_and_get_code()
        page.added_to_cart_message()
        page.added_book_name()
        page.added_book_price()
        
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()
    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_disappear()
    
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_login_link()
    
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
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page.basket_is_empty()
    page.basket_is_empty_text() 
    
@pytest.mark.need_review 
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()