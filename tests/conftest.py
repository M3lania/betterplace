import pytest

from src.pages.confirmation_page import ConfirmationPage
from src.pages.donation_page import DonationPage
from src.pages.thank_you_page import ThankYouPage


@pytest.fixture()
def donation_page(base_url, env, browser):
    return DonationPage(base_url, env, browser)


@pytest.fixture()
def mobile_donation_page(base_url, env, mobile_browser):
    return DonationPage(base_url, env, mobile_browser)


@pytest.fixture()
def confirmation_page(base_url, env, browser):
    return ConfirmationPage(base_url, env, browser)


@pytest.fixture()
def thank_you_page(base_url, env, browser):
    return ThankYouPage(base_url, env, browser)
