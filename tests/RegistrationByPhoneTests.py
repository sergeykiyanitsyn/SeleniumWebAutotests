import allure
from faker import Faker

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelperHelper
from pages.RegistrationByPhonePage import RegistrationByPhonePageHelpersHelper
from pages.RegistrationPage import RegistrationPageHelpersHelper

BASE_URL = 'https://sn.rv-school.ru/'


@allure.feature("Login")
@allure.suite('Login By Phone')
@allure.title('Check select registration county code matches with selected code')
def test_registration_random_country(browser):
    BasePageHelper(browser).get_url(BASE_URL)

    LoginPage = LoginPageHelperHelper(browser)
    LoginPage.click_registration_button()

    RegistrationPage = RegistrationPageHelpersHelper(browser)
    RegistrationPage.click_phone_registration_button()

    RegistrationByPhonePage = RegistrationByPhonePageHelpersHelper(browser)

    selected_country_code = RegistrationByPhonePage.select_random_country()
    actual_country_code = RegistrationByPhonePage.get_phone_field_value()
    assert actual_country_code == selected_country_code
