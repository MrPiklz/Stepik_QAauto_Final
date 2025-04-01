from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators ():
    LOGIN_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_EMAIL_REG_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    LOGIN_PASS_REG_INPUT_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    LOGIN_PASS_REG_INPUT_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    BUSKET_BUTTON_ADD = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, "h1+p")
    PRICE_PRODUCT_AFTER_ADDED_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner>p>strong")
    NAME_OF_PRODUCT =  (By.TAG_NAME, "h1")
    NAME_OF_PRODUCT_AFTER_ADD_IN_BUSKET = (By.CSS_SELECTOR, "div.alertinner>strong")
    SUCSEES_MESSAGE_AFTER_ADD_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner>strong")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group>.btn-default")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BUTTON_BASKET = (By.CSS_SELECTOR, ".btn-group>.btn-default")

    
class BasketPageLocators():
    MESSAGE_BUSKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    TOTAL_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".total.align-right")


