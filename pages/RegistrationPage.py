import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    DISPLAY_NAME_INPUT = (By.CSS_SELECTOR, "[data-test-id='display-name']")
    USERNAME_INPUT = (By.CSS_SELECTOR, "[data-test-id='username']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "[data-test-id='email']")
    PHONE_INPUT = (By.CSS_SELECTOR, "[data-test-id='phone']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test-id='register-password']")
    CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "[data-test-id='confirm-password']")
    REGISTER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[data-test-id='register-submit-btn']")
    PHONE_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[data-test-id='register-phone-toggle']")

    COUNTRY_LIST = (By.CSS_SELECTOR, "[data-test-id='phone-country-select']")
    COUNTRY_ITEM = (By.CSS_SELECTOR, "[data-test-id='phone-country-select'] option[data-test-id^='phone-country-option-']")
    PHONE_NUMBER_INPUT = (By.CSS_SELECTOR, "[data-test-id='phone-number-input']")
    SEND_CODE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='phone-send-code-btn']")
    PHONE_CANCEL_BUTTON = (By.CSS_SELECTOR, "[data-test-id='phone-cancel-btn']")

    SMS_CODE_INPUT = (By.CSS_SELECTOR, "[data-test-id='sms-code-input']")
    VERIFY_CODE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='phone-verify-code-btn']")
    CHANGE_PHONE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='phone-back-to-step-1']")

    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "[data-test-id='first-name-input']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "[data-test-id='last-name-input']")
    FINISH_REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[data-test-id='phone-finish-btn']")
    LOGIN_LINK = (By.CSS_SELECTOR, "[data-test-id='login-link-anchor']")


class RegistrationPageHelpersHelper(BasePageHelper):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы Регистрации'):
            self.attach_screenshot()
            for locator in (
                RegistrationPageLocators.DISPLAY_NAME_INPUT,
                RegistrationPageLocators.USERNAME_INPUT,
                RegistrationPageLocators.EMAIL_INPUT,
                RegistrationPageLocators.PHONE_INPUT,
                RegistrationPageLocators.PASSWORD_INPUT,
                RegistrationPageLocators.CONFIRM_PASSWORD_INPUT,
                RegistrationPageLocators.REGISTER_SUBMIT_BUTTON,
                RegistrationPageLocators.PHONE_REGISTRATION_BUTTON,
                RegistrationPageLocators.LOGIN_LINK,
            ):
                self.find_element(locator)

    @allure.step('Клик по кнопке "Регистрация по телефону"')
    def click_phone_registration_button(self):
        self.attach_screenshot()
        self.find_element(RegistrationPageLocators.PHONE_REGISTRATION_BUTTON).click()
