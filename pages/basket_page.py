from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators



class BasketPage(BasePage):         
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.GOODS_IN_BASKET), "Basket is not empty!"
        
    def basket_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), "No Basket is not empty text!"