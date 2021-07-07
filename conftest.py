from dataclasses import dataclass

from faker import Faker
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


BASE_URL = {
    "QA": "https://www.bp42.com",
    "PROD": "https://www.betterplace.org"
}

MOBILE_USER_AGENT = (
    "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) "
    "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
)


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        dest="env",
        default="QA",
        choices=("PROD", "QA"),
        help="The environment for the application under test.",
    )
    parser.addoption(
        '--chromedriver',
        action="store",
        required=True,
        dest="chromedriver",
        help="Provide the absolute path to chromedriver"
    )


@pytest.fixture(scope="session")
def env(request):
    e = request.config.getoption("--env")
    return e.upper()


@pytest.fixture(scope="session")
def chromedriver(request):
    return request.config.getoption("--chromedriver")


@pytest.fixture(scope="session")
def base_url(env):
    return BASE_URL[env]


@pytest.fixture()
def browser(chromedriver):
    browser = webdriver.Chrome(chromedriver)
    yield browser
    browser.close()


@pytest.fixture()
def mobile_browser(chromedriver):
    mobile_emulation = {
        "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        "userAgent": MOBILE_USER_AGENT
    }
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    browser = webdriver.Chrome(chromedriver, chrome_options=chrome_options)
    yield browser
    browser.close()


@pytest.fixture(scope='class')
def customer():
    faker = Faker()

    @dataclass
    class Customer:
        first_name: str
        last_name: str
        email: str

    c = Customer(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        email=f"{faker.first_name()}@betterplace.org"
    )
    yield c
