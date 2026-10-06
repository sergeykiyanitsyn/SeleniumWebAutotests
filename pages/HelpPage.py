import allure
from selenium.webdriver import ActionChains

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class HelpPageLocators:
    HELP_LINK = (By.CSS_SELECTOR, ".help_app_header a[href='/help']")
    ACTUAL_TOPICS_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/segodnya-aktualno']")
    REGISTRATION_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/registraciya']")
    MY_PROFILE_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/moi-profil']")
    COMMUNICATION_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/obshchenie']")
    PROFILE_ACCESS_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/dostup-k-profilu']")
    SECURITY_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/bezopasnost']")
    GROUPS_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/gruppy']")
    PAID_FEATURES_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/platnye-funkcii']")
    VIOLATIONS_AND_SPAM_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/narusheniya-i-spam']")
    GAMES_AND_APPS_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/igry-i-prilojeniya']")
    OTHER_SERVICES_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/drugie-servisy']")
    USEFUL_INFORMATION_LINK = (By.CSS_SELECTOR, ".help_app_list a[href='/help/poleznaya-informaciya']")


class HelpPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step("Проверяем корректность загрузки страницы FAQ"):
            self.attach_screenshot()
            self.find_element(HelpPageLocators.HELP_LINK)
            self.find_element(HelpPageLocators.ACTUAL_TOPICS_LINK)
            self.find_element(HelpPageLocators.REGISTRATION_LINK)
            self.find_element(HelpPageLocators.MY_PROFILE_LINK)

    @allure.step("Скролим к блоку 'Другие сервисы'")
    def scroll_to_other_service_link(self):
        self.scroll_to_item(HelpPageLocators.OTHER_SERVICES_LINK)

    def scroll_to_item(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).click(scroll_item).perform()