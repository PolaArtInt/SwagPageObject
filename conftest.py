import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from pages.login_page import LoginPage, login
from pages.menu_page import MenuMod
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.filter_page import FilterMod
from pages.item_page import ItemPage
from pages.order_page import OrderPage
from pages.about_page import AboutPage
from pages.form_page import FormPage

from locators.form_data import FormLocs
from locators.urls import URLs


@pytest.fixture(scope="function", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    options.add_argument("--headless")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=1280,1000")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    yield driver

    allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)
    driver.quit()


@pytest.fixture()
def fake():
    from faker import Faker
    fake = Faker()
    return fake


@pytest.fixture()
def rand_num(num):
    import random
    return random.randint(0, num - 1)


# pages:
@pytest.fixture()
def log_page(driver):
    log_page = LoginPage(driver, URLs.url)
    return log_page


@pytest.fixture()
def menu_page(driver, login):
    menu_page = MenuMod(driver, login)
    return menu_page


@pytest.fixture()
def inv_page(driver):
    inv_page = InventoryPage(driver, URLs.inventory_url)
    return inv_page


@pytest.fixture()
def filter_page(driver, login):
    filter_page = FilterMod(driver, login)
    return filter_page


@pytest.fixture()
def cart_page(driver):
    cart_page = CartPage(driver, URLs.cart_url)
    return cart_page


@pytest.fixture()
def item_page(driver, login):
    item_page = ItemPage(driver, login)
    return item_page


@pytest.fixture()
def order_page(driver):
    order_page = OrderPage(driver, URLs.checkout_url)
    return order_page


@pytest.fixture()
def about_page(driver):
    about_page = AboutPage(driver, URLs.about_url)
    return about_page


@pytest.fixture()
def form_page(driver):
    form_page = FormPage(driver, FormLocs.form_url)
    return form_page
