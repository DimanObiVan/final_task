from selenium.webdriver.common.by import By


class BasketPageLocators():
    GOODS_IN_BASKET = (By.CSS_SELECTOR,".col-sm-6.h3")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR,"#content_inner p")

class ProductPageLocators():
    CART_URL = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"  
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CART_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner  strong")
    BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_CART_NEW = (By.CSS_SELECTOR, "li.col-xs-6:first-child .btn")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, ".alert-success .alertinner  strong")
    SUCCESS_MESSAGES = (By.CSS_SELECTOR,".alertinner strong")
    GOODS_IN_BASKET = (By.CSS_SELECTOR,".col-sm-6.h3")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"  
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".register_form .btn")
class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default") 
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    
