from selenium.webdriver.common.by import By
from types import SimpleNamespace

from src.page import Page

ThankYouPageLocators = SimpleNamespace(
    thank_you_message=(By.CSS_SELECTOR, ".generic-postdonation-message > div.text-3xl.text-center.mt-1")
)


class ThankYouPage(Page):
    @property
    def page_load_timeout(self):
        return 30

    @property
    def path(self):
        return ""

    @property
    def thank_you_message(self):
        thank_you_message = ThankYouPageLocators.thank_you_message
        thank_you_message = self.browser.find_element(*thank_you_message)
        self.scroll_to_view(thank_you_message)
        return thank_you_message.text.strip()
