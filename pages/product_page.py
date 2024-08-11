from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators



class ProductPage(BasePage): 
    def add_to_cart(self):
        add = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        add.click()

    def added_to_cart_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "No success message"
    
    def added_book_name(self):
        bookName = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        addedBookName = self.browser.find_element(*ProductPageLocators.ADDED_BOOK_NAME).text
        assert bookName == addedBookName, "Added book name is incorrect"

    def added_book_price(self):
        bookPrice = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        addedBookPrice = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        assert bookPrice == addedBookPrice, "Added book price is incorrect"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGES), "success message is present!"
        
    
    def should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGES), "success message is present!"
        
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET), "Basket is not empty!"
        
    def basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "No Basket is not empty text!"
    