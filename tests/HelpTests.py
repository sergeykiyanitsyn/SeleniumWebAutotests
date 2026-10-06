import allure

from core.BaseTest import browser
from pages.BasePage import BasePage
from pages.HelpPage import HelpPageHelper
from pages.OtherLinksPage import OtherLinksPageHelpers

BASE_URL = 'https://ok.ru/help'

def test_help_page(browser):
    BasePage(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scroll_to_other_service_link()
    OtherLinksPageHelpers(browser)