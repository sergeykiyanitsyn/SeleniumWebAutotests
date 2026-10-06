import allure

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import random


class RegistrationByPhonePageLocators(BasePage):
    @staticmethod
    def country_item(number):
        return (
            By.CSS_SELECTOR,
            f'[data-test-id="phone-country-option-{number}"]',
        )

    SEND_CODE_BUTTON = (By.CSS_SELECTOR, '[data-test-id="phone-send-code-btn"]')
    PHONE_INPUT = (By.CSS_SELECTOR, '[data-test-id="phone-number-input"]')
    COUNTRY_LIST = (By.CSS_SELECTOR, '[data-test-id="phone-country-select"]')


class RegistrationByPhonePageHelpers(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы Регистрации по телефону'):
            self.attach_screenshot()
        self.find_element(RegistrationByPhonePageLocators.PHONE_INPUT)
        self.find_element(RegistrationByPhonePageLocators.COUNTRY_LIST)
        self.find_element(RegistrationByPhonePageLocators.SEND_CODE_BUTTON)

    @allure.step('Выбираем случайную страну и возвращаем её код')
    def select_random_country(self):
        country_select = Select(
            self.find_element(RegistrationByPhonePageLocators.COUNTRY_LIST)
        )
        index = random.randrange(len(country_select.options))
        country_select.select_by_index(index)
        self.attach_screenshot()
        return country_select.first_selected_option.get_attribute("value")

    @allure.step('Получаем Код страны из поля "Код страны"')
    def get_phone_field_value(self):
        self.attach_screenshot()
        return self.find_element(RegistrationByPhonePageLocators.COUNTRY_LIST).get_attribute("value")
