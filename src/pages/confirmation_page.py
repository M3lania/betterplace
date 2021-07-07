from selenium.webdriver.common.by import By
from types import SimpleNamespace

from src.page import Page
from src.pages.thank_you_page import ThankYouPage

ConfirmationLocators = SimpleNamespace(
    amount=(By.CSS_SELECTOR, "div.col-md-12.offset-md-5 > div > div"),
    next_button=(By.CSS_SELECTOR, "div.payment-direct-deposits-show.bg-white > div.container.pt-4 > div > div.col-md-12.offset-md-5 > p:nth-child(3) > a")
)


class ConfirmationPage(Page):
    @property
    def page_load_timeout(self):
        return 30

    @property
    def path(self):
        return ""

    @property
    def amount(self):
        amount = ConfirmationLocators.amount
        self.wait_until_element_is_visible(*amount)
        return self.browser.find_element(*amount).text.strip()

    def proceed(self):
        next_button = ConfirmationLocators.next_button
        next_button = self.browser.find_element(*next_button)
        self.scroll_to_view(next_button)
        next_button.click()

        return ThankYouPage(
            self.base_url, self.env, self.browser, open_url=False)
