from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec


class Page:

    def __init__(self, base_url, env, browser, open_url=True):
        self.base_url = base_url
        self.env = env
        self.browser = browser

        self.wait = Wait(self.browser, 5)

        self.full_url = f"{self.base_url}{self.path}"

        if open_url:
            self.get_page(self.full_url)

    @property
    def path(self):
        raise NotImplementedError()

    @property
    def page_load_timeout(self):
        raise NotImplementedError()

    def scroll_to_view(self, element):
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_until_element_is_visible(self, by, value, timeout=10):
        message = (
            f'\nWaited {timeout} seconds before timing out.'
            f'\nExpected element to be visible: {value}'
            f'\nCurrent url: {self.browser.current_url}'
        )
        Wait(self.browser, timeout).until(
            ec.visibility_of_element_located((by, value)), message=message
        )

    def get_page(self, url):
        self.browser.set_page_load_timeout(self.page_load_timeout)
        try:
            self.browser.get(url)
        except TimeoutException as err:
            err.msg = (
                f'\nTimeout while waiting for page load to complete.'
                f'\n{self.__class__.__name__} Timeout: {self.page_load_timeout}'
                f'\nURL: {url}'
            )
            raise

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.base_url}', '{self.env}', "
            f"'{self.browser.name}')"
        )

    def __str__(self):
        return (
            f"{self.__class__.__name__} instance: "
            f"base_url='{self.base_url}', browser='{self.browser.name}', "
            f"url='{self.full_url}'"
        )
