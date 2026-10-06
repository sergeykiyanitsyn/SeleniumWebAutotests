import allure
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class OtherLinksPageLocators:
    TITLE = (By.XPATH, '//span[text()="Другие сервисы"]')


class OtherLinksPageHelpers(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы Другие сервисы"):
            self.attach_screenshot()
        self.find_element(OtherLinksPageLocators.TITLE)