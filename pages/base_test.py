import allure
import pytest

from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.menu_page import MenuMod
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.filter_page import FilterMod
from pages.item_page import ItemPage
from pages.order_page import OrderPage
from pages.about_page import AboutPage
from pages.form_page import FormPage

from locators.auth_module import AuthLocs, AuthData
from locators.menu_module import MenuLocs
from locators.form_data import FormLocs
from locators.urls import URLs


class BaseTest:
    log_page: LoginPage
    menu_page: MenuMod
    cart_page: CartPage
    inv_page: InventoryPage
    filter_page: FilterMod
    item_page: ItemPage
    order_page: OrderPage
    about_page: AboutPage
    form_page: FormPage

    @pytest.fixture(scope='function', autouse=True)
    def pages_init(self, request, driver):
        request.cls.log_page = LoginPage(driver, URLs.url)
        request.cls.menu_page = MenuMod(driver, URLs.url)
        request.cls.inv_page = InventoryPage(driver, URLs.inventory_url)
        request.cls.filter_page = FilterMod(driver, URLs.login_url)
        request.cls.cart_page = CartPage(driver, URLs.cart_url)
        request.cls.item_page = ItemPage(driver, URLs.login_url)
        request.cls.order_page = OrderPage(driver, URLs.checkout_url)
        request.cls.about_page = AboutPage(driver, URLs.about_url)
        request.cls.form_page = FormPage(driver, FormLocs.form_url)

    @pytest.fixture()
    def fake(self):
        from faker import Faker
        fake = Faker()
        return fake

    @pytest.fixture()
    def in_out(self, driver):
        page = BasePage(driver, URLs.url)
        page.open()
        page.is_visible(AuthLocs.input_user).send_keys(AuthData.standard_user)
        page.is_visible(AuthLocs.input_pass).send_keys(AuthData.pass_word)
        page.is_clickable(AuthLocs.login_btn).click()
        print(f'\nlogin...')

        yield

        page.find_el(MenuLocs.menu_btn).click()
        page.is_clickable(MenuLocs.logout_btn).click()
        print(f'\nlogout...')

    @pytest.fixture()
    def form_conditions(self, driver):
        form_page = FormPage(driver, FormLocs.form_url)
        form_page.open()

        with allure.step('check the current url...'):
            assert driver.current_url == FormLocs.form_url and \
                   FormLocs.form_header == 'Register', 'Wrong page'

        name_field = form_page.form_name()
        pass_field = form_page.form_pass()
        checkbox = form_page.form_checkbox()

        with allure.step('check if the form fields are empty...'):
            if checkbox.is_selected() or name_field.text != '' or pass_field.text != '':
                checkbox.click()
                name_field.clear()
                pass_field.clear()

            assert name_field.text == '', 'The Email input is filled'
            assert pass_field.text == '', 'The Password input is filled'
            assert not checkbox.is_selected(), 'The checkbox is selected'

        yield self
