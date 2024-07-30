<<<<<<< HEAD
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage): 


    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
=======
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)
>>>>>>> 033e072739ada8e5e72cb7bb7dc150c250e22106
