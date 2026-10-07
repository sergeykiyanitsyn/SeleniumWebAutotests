import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelperHelper
from faker import Faker

fake = Faker('ru_RU')

BASE_URL = 'https://sn.rv-school.ru/'
EMPTY_LOGIN_ERROR = 'Введите телефон, email или логин и пароль.'


@allure.feature("Login")
@allure.suite('Check form authorisation')
@allure.title('Empty form authorisation return error')
def test_empty_login_and_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelperHelper(browser)
    LoginPage.click_login_button()
    assert LoginPage.get_error_message() == EMPTY_LOGIN_ERROR


@allure.feature("Login")
@allure.suite('Check form authorisation')
@allure.title('Empty password return error')
def test_empty_password(browser):
    login_email = fake.email()

    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelperHelper(browser)
    LoginPage.fill_login(login_email)
    LoginPage.click_login_button()
    assert LoginPage.get_error_message() == EMPTY_LOGIN_ERROR
