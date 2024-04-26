import allure
import pytest

from locators.auth_module import AuthData
from pages.base_page import BasePage

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


class BaseTest:
    page: BasePage
    log_page: LoginPage
    login: login
    menu_page: MenuMod
    cart_page: CartPage
    inv_page: InventoryPage
    filter_page: FilterMod
    item_page: ItemPage
    order_page: OrderPage
    about_page: AboutPage
    form_page: FormPage

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, request, driver, login):
        request.cls.driver = driver
        request.cls.login = login
        request.cls.login_page = LoginPage(driver, URLs.url)
        request.cls.menu_page = MenuMod(driver, login)
        request.cls.inv_page = InventoryPage(driver, URLs.inventory_url)
        request.cls.filter_page = FilterMod(driver, login)
        request.cls.cart_page = CartPage(driver, URLs.cart_url)
        request.cls.item_page = ItemPage(driver, login)
        request.cls.order_page = OrderPage(driver, URLs.checkout_url)
        request.cls.about_page = AboutPage(driver, URLs.about_url)
        request.cls.form_page = FormPage(driver, FormLocs.form_url)
        request.cls.form_data = FormLocs()
        request.cls.urls = URLs()

