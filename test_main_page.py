from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.common.exceptions import NoSuchElementException




def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()