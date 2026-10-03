import allure
from faker import Faker

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper
from pages.RegistrationByPhonePage import RegistrationByPhonePageHelpers
from pages.RegistrationPage import RegistrationPageHelpers

BASE_URL = 'https://sn.rv-school.ru/'


@allure.feature("Login")
@allure.suite('Login By Phone')
@allure.title('Check select registration county code matches with selected code')
def test_registration_random_country(browser):
    BasePage(browser).get_url(BASE_URL)

    LoginPage = LoginPageHelper(browser)
    LoginPage.click_registration_button()

    RegistrationPage = RegistrationPageHelpers(browser)
    RegistrationPage.click_phone_registration_button()

    RegistrationByPhonePage = RegistrationByPhonePageHelpers(browser)

    selected_country_code = RegistrationByPhonePage.select_random_country()
    actual_country_code = RegistrationByPhonePage.get_phone_field_value()
    assert actual_country_code == selected_country_code
