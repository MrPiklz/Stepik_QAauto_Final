from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import time
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_its_a_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self                       
    def test_guest_can_go_to_login_page(self, browser):     
         # реализация теста
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_url()
        
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()