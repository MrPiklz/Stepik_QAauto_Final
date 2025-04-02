from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):  #проверка что текущая страница - страница логина
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self): #проверка что в URL содержится "login"
        assert 'login' in self.browser.current_url, 'not login page'

    def should_be_login_form(self): #проверка наличия формы авторизации окна емаил
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_INPUT), "NO INPUT EMAIL ELEMENT"

    def should_be_register_form(self): #проверка наличия формы авторизации окна пасс
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS_INPUT), "NO INPUT PASS ELEMENT"
    
        
    def register_new_user(self, email, password): #проверка, что страница - форма логина. Проверка наличия url+форма email\pass
        # реализуем регистарцию пользователя
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_REG_INPUT).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASS_REG_INPUT_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASS_REG_INPUT_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()        


        