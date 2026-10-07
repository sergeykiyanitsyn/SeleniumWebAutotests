import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelperHelper
from faker import Faker

from pages.VKEcosystemPage import VKEcosystemPageHelper

BASE_URL = 'https://ok.ru/'


@allure.feature("Toolbar")
@allure.suite('Проверка кнопки "Навигация"')
@allure.title('Переход к проектам экосистемы VK')
def test_open_vk_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()

    current_window_page = BasePage.get_window_page_by_number(1)

    BasePage.click_vk_ecosystem()
    BasePage.click_more_button()

    new_window_page = BasePage.get_window_page_by_number(2)

    BasePage.switch_window(new_window_page)

    VKEcosystem = VKEcosystemPageHelper(browser)
    VKEcosystem.switch_window(current_window_page)

    BasePageHelper(browser)
