from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.common.exceptions import NoSuchElementException

class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        
    def open(self):
        self.browser.get(self.url)