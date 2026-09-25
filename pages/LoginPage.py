from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.CSS_SELECTOR, "[data-test-id='login-phone-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-test-id='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test-id='login-submit-btn']")
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, "[data-test-id='forgot-password-link']")
    QR_CODE_TAB = (By.CSS_SELECTOR, "[data-test-id='tab-qr']")
    QR_CODE = (By.CSS_SELECTOR, "[data-test-id='qr-placeholder']")


class LoginPageHelper(BasePage):
    pass
