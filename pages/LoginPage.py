import allure

from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.CSS_SELECTOR, "[data-test-id='login-phone-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-test-id='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test-id='login-submit-btn']")
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, "[data-test-id='forgot-password-link']")
    QR_CODE_TAB = (By.CSS_SELECTOR, "[data-test-id='tab-qr']")
    QR_CODE = (By.CSS_SELECTOR, "[data-test-id='qr-placeholder']")
    ERROR_MESSAGE_LOGIN = (By.CSS_SELECTOR, "[data-test-id='login-error']")
    RESTORE_PROFILE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='lockout-recover-btn']")
    CANCEL_RESTORE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='lockout-cancel-btn']")
    LOCKOUT_REGISTER_PROFILE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='lockout-register-btn']")
    REGISTER_PROFILE_BUTTON = (By.CSS_SELECTOR, "[data-test-id='hero-register-btn']")



class LoginPageHelperHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы Логина"):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        self.find_element(LoginPageLocators.QR_CODE_TAB)

    @allure.step('Нажать на кнопку "Войти"')
    def click_login_button(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем сообщение об ошибке')
    def get_error_message(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_MESSAGE_LOGIN).text

    @allure.step('Заполняем поле логин')
    def fill_login(self, login):
        self.find_element(LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Заполняем поле пароль')
    def fill_password(self, password):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery_button(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RESTORE_PROFILE_BUTTON).click()

    @allure.step('Клик по кнопке "Зарегистрироваться"')
    def click_registration_button(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.REGISTER_PROFILE_BUTTON).click()
