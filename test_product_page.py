from .pages.product_page import ProductPage
from selenium import webdriver
import pytest
import time

# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_add_to_cart(browser, link):
    # url = link
    # page = ProductPage(browser, url)
    # page.open()
    # page.add_to_cart()
    # page.solve_quiz_and_get_code()
    # page.added_to_cart_message()
    # page.added_book_name()
    # page.added_book_price()
   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()
    
def test_success_messages2(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
        
def test_success_messages3(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_disappear()
    
def test_guest_should_see_login_link(browser):
    # link = "http://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, link)
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
    
@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
    page = ProductPage(browser, link)
    page.open()
    # page.add_to_cart()
    page.go_to_basket()
    # time.sleep(3)
    page.basket_is_empty()
    page.basket_is_empty_text() 