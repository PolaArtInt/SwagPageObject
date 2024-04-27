import pytest

from pages.login_page import LoginPage
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


class BaseTest:
    @pytest.fixture()
    def fake(self):
        from faker import Faker
        fake = Faker()
        return fake

    # pages:
    @pytest.fixture()
    def log_page(self, driver):
        log_page = LoginPage(driver, URLs.url)
        return log_page

    @pytest.fixture()
    def menu_page(self, driver, login):
        menu_page = MenuMod(driver, login)
        return menu_page

    @pytest.fixture()
    def inv_page(self, driver):
        inv_page = InventoryPage(driver, URLs.inventory_url)
        return inv_page

    @pytest.fixture()
    def filter_page(self, driver, login):
        filter_page = FilterMod(driver, login)
        return filter_page

    @pytest.fixture()
    def cart_page(self, driver):
        cart_page = CartPage(driver, URLs.cart_url)
        return cart_page

    @pytest.fixture()
    def item_page(self, driver, login):
        item_page = ItemPage(driver, login)
        return item_page

    @pytest.fixture()
    def order_page(self, driver):
        order_page = OrderPage(driver, URLs.checkout_url)
        return order_page

    @pytest.fixture()
    def about_page(self, driver):
        about_page = AboutPage(driver, URLs.about_url)
        return about_page

    @pytest.fixture()
    def form_page(self, driver):
        form_page = FormPage(driver, FormLocs.form_url)
        return form_page

    # page: BasePage
    # log_page: LoginPage
    # menu_page: MenuMod
    # cart_page: CartPage
    # inv_page: InventoryPage
    # filter_page: FilterMod
    # item_page: ItemPage
    # order_page: OrderPage
    # about_page: AboutPage
    # form_page: FormPage

    # @pytest.fixture(scope='function', autouse=True)
    # def setup(self, request, driver):
    #     request.cls.driver = driver
    #     request.cls.login_page = LoginPage(driver, URLs.url)
    #     request.cls.menu_page = MenuMod(driver, URLs.url)
    #     request.cls.inv_page = InventoryPage(driver, URLs.inventory_url)
    #     request.cls.filter_page = FilterMod(driver, URLs.login_url)
    #     request.cls.cart_page = CartPage(driver, URLs.cart_url)
    #     request.cls.item_page = ItemPage(driver, URLs.login_url)
    #     request.cls.order_page = OrderPage(driver, URLs.checkout_url)
    #     request.cls.about_page = AboutPage(driver, URLs.about_url)
    #     request.cls.form_page = FormPage(driver, FormLocs.form_url)

