from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.common.exceptions import NoSuchElementException

<<<<<<< HEAD
class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        
    def open(self):
        self.browser.get(self.url)
=======
link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)
>>>>>>> 033e072739ada8e5e72cb7bb7dc150c250e22106
