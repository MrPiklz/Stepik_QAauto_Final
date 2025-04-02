from .base_page import BasePage
from .locators import ProductPageLocators

from selenium.common.exceptions import NoAlertPresentException # в начале файла

import time
import math


class ProductPage(BasePage):
    
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
  

    def test_add_busket_slove_quize(self):
        self.browser.delete_all_cookies()
        #WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
        self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON_ADD).click()
        self.solve_quiz_and_get_code()
        time.sleep(2)
        
    def test_check_price_after_adding_in_basket_product(self):  #проверка соответствия цены товара и цены добавленного в корзину товара
        assert self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text == self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_AFTER_ADDED_IN_BASKET).text, "bad:("
    
    def test_check_name_after_adding_in_basket_product(self):  #проверка соответствия имени товара и имени добавленного в корзину товара
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text == self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_AFTER_ADD_IN_BUSKET).text, "not found name"
        
    def test_guest_can_add_product_to_basket_in(self): #Проверка после добавления товара в корзину имени и цены в сообщении и товара
        price = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON_ADD).click()
        self.test_check_price_after_adding_in_basket_product()  #check by price
        self.test_check_name_after_adding_in_basket_product()   #check by name
    
    def test_cant_see_success_message(self):  #проверка что не видно сообщения о удачном добавлении товара
        assert self.is_not_element_present(*ProductPageLocators.SUCSEES_MESSAGE_AFTER_ADD_PRODUCT_IN_BASKET)

