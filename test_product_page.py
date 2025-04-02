import pytest
import time

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

@pytest.mark.login_guest
class TestUserAddToBasketFromProductPage:
    login_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):  #создаем пользователя
        email = str(time.time()) + "@fakemail.org"
        password = "passwordDDDD"
        page = LoginPage(browser, self.login_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
    
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser): #Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        #Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара. 
        page = ProductPage(browser, self.link)
        page.open()
        page.test_guest_can_add_product_to_basket_in()
        
    @pytest.mark.xfail
    def test_user_cant_see_success_message (self, browser):
        page = ProductPage(browser, self.link)
        page.open()
        page.test_cant_see_success_message() #проверка отсутствия сообщения о удачном добавлении в корзину товара


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket_in()

def test_guest_cant_see_success_message (browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.test_cant_see_success_message() #проверка наличия сообщения о удачном добавлении в корзину товара


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.test_guest_basket_is_empty_message() #проверка наличия сообщения о пустой корзине
    basket_page.test_guest_basket_is_empty_no_products() #проверка отсутствия цены за все, значит корзина пуста
    
    
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
