from .base_page import BasePage
from .locators import BasketPageLocators

from selenium.common.exceptions import NoAlertPresentException 

import time
import math


class BasketPage(BasePage):
    
    def test_guest_basket_is_empty_message(self): ##CHECK add product in basket by name and price
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BUSKET_IS_EMPTY), 'basket is notempty' #проверка наличия сообщения о пустой корзине
    
    def test_guest_basket_is_empty_no_products(self):
        assert self.is_not_element_present(*BasketPageLocators.TOTAL_PRICE_IN_BASKET) #проверка отсутствия цены за все, значит корзина пуста

