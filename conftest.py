import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from pages.form_page import FormPage

from locators.auth_module import AuthData
from locators.form_data import FormLocs
from locators.urls import URLs


@pytest.fixture(scope="function", autouse=True)
def driver():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    # chrome_options.add_argument("--headless")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--window-size=1280,1000")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


@pytest.fixture()
def fake():
    from faker import Faker
    fake = Faker()
    return fake


@pytest.fixture()
def standard_auth(driver):
    page = LoginPage(driver, URLs.url)
    page.open()

    page.input_user().send_keys(AuthData.user)
    page.input_pass().send_keys(AuthData.pass_word)
    page.login_btn().click()


@pytest.fixture()
def locked_out_auth(driver):
    page = LoginPage(driver, URLs.url)
    page.open()

    page.input_user().send_keys(AuthData.locked_user)
    page.input_pass().send_keys(AuthData.pass_word)
    page.login_btn().click()


@pytest.fixture()
def problem_auth(driver):
    page = LoginPage(driver, URLs.url)
    page.open()

    page.input_user().send_keys(AuthData.problem_user)
    page.input_pass().send_keys(AuthData.pass_word)
    page.login_btn().click()


@pytest.fixture()
def glitch_auth(driver):
    page = LoginPage(driver, URLs.url)
    page.open()

    page.input_user().send_keys(AuthData.glitch_user)
    page.input_pass().send_keys(AuthData.pass_word)
    page.login_btn().click()


@pytest.fixture()
def form_conditions(driver):
    page = FormPage(driver, FormLocs.form_url)
    page.open()

    assert driver.current_url == FormLocs.form_url and \
           FormLocs.form_header == 'Register', 'Wrong page'

    name_field = page.form_name()
    pass_field = page.form_pass()
    checkbox = page.form_checkbox()

    if checkbox.is_selected() or name_field.text != '' or pass_field.text != '':
        checkbox.click()
        name_field.clear()
        pass_field.clear()

    assert name_field.text == '', 'Input Email is filled'
    assert pass_field.text == '', 'Input Password is filled'
    assert not checkbox.is_selected(), 'Checkbox is selected'

    yield form_conditions
    # page.open()
