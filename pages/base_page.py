import allure
from selenium.webdriver import ActionChains

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        with allure.step('open the page'):
            self.driver.get(self.url)

    def get_url(self) -> str:
        with allure.step('get the current page url'):
            return self.driver.current_url

    def refresh(self):
        with allure.step('refresh the page'):
            self.driver.refresh()

    def find_elems(self, locator) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def find_el(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def is_visible(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located(locator))

    def are_visible(self, locator) -> list[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def is_invisible(self, locator) -> WebElement:
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def visibility_of(self, locator) -> WebElement:
        return self.wait.until(ec.visibility_of(locator))

    def is_clickable(self, locator) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(locator))

    def hold_mouse_on_element(self, locator):
        ActionChains(self.driver).move_to_element(self.is_visible(locator)).perform()
