from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        
    

    def test_add_busket_clove_quize(self):
        self.browser.delete_all_cookies()
        #WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify")))
        self.browser.find_element(*ProductPageLocators.BUSKET_BUTTON_ADD).click()
        self.solve_quiz_and_get_code()
        time.sleep(3)
