import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    options.add_argument("--headless")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=1280,1000")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    yield driver

    allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
    driver.quit()
