import allure
from faker import Faker

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelperHelper
from pages.RecoveryPage import RecoveryPageHelperHelper

fake = Faker('ru_RU')

BASE_URL = 'https://sn.rv-school.ru/'
LOGIN_EMAIL = fake.email()
PASSWORD = 'PASSWORD'

@allure.feature("Login")
@allure.suite('Check Recovery user login')
@allure.title('Check move to recovery user after some fail attempts authorization')
def test_go_to_recovery_after_many_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelperHelper(browser)
    LoginPage.fill_login(LOGIN_EMAIL)

    for _ in range(3):
        LoginPage.fill_password(PASSWORD)
        LoginPage.click_login_button()

    LoginPage.click_recovery_button()
    RecoveryPageHelperHelper(browser)