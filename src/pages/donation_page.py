from enum import Enum

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from types import SimpleNamespace

from src.page import Page
from src.pages.confirmation_page import ConfirmationPage


class PaymentType(Enum):
    PAYPAL = 1
    STRIPE_SEPA_DEBIT = 2
    STRIPE_CC = 3
    PAYDIREKT = 4
    DIRECT_DEPOSIT = 5


DonateLocators = SimpleNamespace(
    accept_cookies=(By.CSS_SELECTOR, "button.btn.btn-primary.btn-large.flex-grow.mb-3"),
    amount=(By.CSS_SELECTOR, "div.amount-input-wrapper > input"),
    payment_label=(By.CSS_SELECTOR, ".donation-form-payment-method-links .payment-method-radio"),
    payment_methods=(By.CSS_SELECTOR, "div.donation-form-payment-method-links.mb-3 > div.payment-method-radios.form-group"),
    payment_type=(By.CSS_SELECTOR, "div.payment-method-radios.form-group > label:nth-child({payment_type})"),
    first_name=(By.ID, "first_name"),
    last_name=(By.ID, "last_name"),
    email=(By.ID, "email"),
    pay_button=(By.CSS_SELECTOR, "div.form-fields > button")
)


class DonationPage(Page):
    @property
    def page_load_timeout(self):
        return 30

    @property
    def path(self):
        return "/de/donate/platform/projects/1114"

    def click_accept_cookies_button(self):
        accept_cookies = DonateLocators.accept_cookies
        self.wait_until_element_is_visible(*accept_cookies)
        self.browser.find_element(*accept_cookies).click()

    def set_amount(self, value):
        implicit_amount = DonateLocators.amount
        amount = self.browser.find_element(*implicit_amount)
        self.scroll_to_view(amount)

        amount.send_keys(Keys.BACK_SPACE)
        amount.send_keys(Keys.BACK_SPACE)

        amount.send_keys(value)

    def select_payment_type(self, payment_type):
        by, value = DonateLocators.payment_type
        element = self.browser.find_element(by, value.format(payment_type=payment_type))
        self.scroll_to_view(element)
        element.click()

    def _set_value(self, locator, value):
        element = self.browser.find_element(*locator)
        self.scroll_to_view(element)
        element.send_keys(value)

    def set_first_name(self, value):
        first_name = DonateLocators.first_name
        self._set_value(first_name, value)

    def set_last_name(self, value):
        last_name = DonateLocators.last_name
        self._set_value(last_name, value)

    def set_email(self, value):
        email = DonateLocators.email
        self._set_value(email, value)

    def click_pay_button(self):
        pay_button = DonateLocators.pay_button
        pay_button = self.browser.find_element(*pay_button)
        self.scroll_to_view(pay_button)
        pay_button.click()

    def fill_form_with_valid_data_and_submit(self, customer, amount):
        self.set_amount(amount)
        self.select_payment_type(PaymentType.DIRECT_DEPOSIT.value)
        self.set_first_name(customer.first_name)
        self.set_last_name(customer.last_name)
        self.set_email(customer.email)
        self.click_pay_button()
        return ConfirmationPage(
            self.base_url, self.env, self.browser, open_url=False
        )

    def get_width_of_payment_label(self):
        payment_label = DonateLocators.payment_label
        element = self.browser.find_element(*payment_label)
        return element.value_of_css_property('width')

    def get_width_of_payment_methods(self):
        payment_methods = DonateLocators.payment_methods
        element = self.browser.find_element(*payment_methods)
        return element.value_of_css_property('width')
