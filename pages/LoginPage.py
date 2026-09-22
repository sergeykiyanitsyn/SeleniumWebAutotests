from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FIELD = (By.CSS_SELECTOR, "[data-test-id='login-input']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-test-id='password-input']")
    SHOW_PASSWORD_BUTTON = (
        By.XPATH,
        "//*[@data-test-id='password-input']"
        "/ancestor::*[.//button][1]//button[@type='button']",
    )
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[data-test-id='enter-action']")
    QR_LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='button'][label]")
    FORGOT_PASSWORD_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test-id='forgot-password-link']",
    )
    REGISTRATION_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test-id='registration-action']",
    )

    VK_LOGIN_LINK = (
        By.CSS_SELECTOR,
        "[data-module='registration/vkconnect']",
    )
    MAIL_LOGIN_LINK = (
        By.CSS_SELECTOR,
        "[data-module='registration/socialSignIn'][data-provider='MAILRU']",
    )
    GOOGLE_LOGIN_LINK = (
        By.CSS_SELECTOR,
        "[data-module='registration/socialSignIn'][data-provider='GOOGLE_PLUS']",
    )
    YANDEX_LOGIN_LINK = (
        By.CSS_SELECTOR,
        "[data-module='registration/socialSignIn'][data-provider='YANDEX']",
    )
    APPLE_LOGIN_LINK = (
        By.CSS_SELECTOR,
        "[data-module='registration/socialSignIn'][data-provider='APPLE']",
    )

    LOGIN_TAB = (
        By.CSS_SELECTOR,
        "[role='tablist'] [role='tab'][data-l='t,login_tab']",
    )
    QR_CODE_TAB = (
        By.CSS_SELECTOR,
        "[role='tablist'] [role='tab'][data-l='t,qr_tab']",
    )


class LoginPageHelper(BasePage):
    pass
