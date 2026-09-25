from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from faker import Faker

fake = Faker('ru_RU')

BASE_URL = 'https://sn.rv-school.ru/'
EMPTY_LOGIN_ERROR = 'Введите телефон, email или логин и пароль.'


def test_empty_login_and_password(browser):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.click_login_button()
    assert LoginPage.get_error_message() == EMPTY_LOGIN_ERROR


def test_empty_password(browser):
    login_email = fake.email()

    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.fill_login_input(login_email)
    LoginPage.click_login_button()
    assert LoginPage.get_error_message() == EMPTY_LOGIN_ERROR
