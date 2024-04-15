import pytest
import requests

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

from locators.auth_module import AuthLocs, AuthData
from locators.urls import URLs


# case 1.1
# standard auth:
@pytest.mark.positive
def test_auth_positive(driver, standard_auth):
    inv_page = InventoryPage(driver, URLs.inventory_url)

    assert driver.current_url == URLs.inventory_url, 'Wrong url'
    assert inv_page.inventory_header().text == 'Products', 'Wrong page header'
    assert len(inv_page.inventory_cards()) > 0, 'There are no item cards on the inventory page'

    print(f'\nStandard user...')


# case 1.2
# locked out auth:
@pytest.mark.positive
def test_auth_positive_locked_out_user(driver, locked_out_auth):
    log_page = LoginPage(driver, URLs.url)

    assert driver.current_url == URLs.url, 'Wrong url'
    assert log_page.locked_msg() == AuthLocs.locked_msg, 'Login error'

    print(f'\nLocked out user... {log_page.locked_msg()}')


# case 1.3
# problem auth:
@pytest.mark.positive
def test_auth_positive_problem_user(driver, problem_auth):
    inv_page = InventoryPage(driver, URLs.inventory_url)

    assert driver.current_url == URLs.inventory_url, 'Wrong url'
    assert inv_page.inventory_header().text == 'Products', 'Wrong page header'
    assert len(inv_page.inventory_cards()) > 0, 'There are no item cards on the inventory page'

    print(f'\nProblem user...')


# case 1.3.1
# problem auth:
@pytest.mark.defect
@pytest.mark.negative
def test_auth_positive_problem_user(driver, problem_auth):
    inv_page = InventoryPage(driver, problem_auth)

    imgs = inv_page.item_imgs()
    broken_url_sample = 'WithGarbageOnItToBreakTheUrl'

    for img in imgs:
        response = requests.get(img.get_attribute('src'), stream=True)
        if response.status_code == 404:
            assert response.status_code == 404, 'Image is not found'
            assert broken_url_sample in img.get_dom_attribute('src'), 'Image is not visible'
            print(f'\n{response} Image: {img.get_dom_attribute('src')} is not visible')

    assert driver.current_url == URLs.inventory_url, 'Wrong url'


# case 1.4
# perfomance glitch auth:
@pytest.mark.slow
@pytest.mark.positive
def test_auth_positive_performance_glitch_user(driver, glitch_auth):
    inv_page = InventoryPage(driver, URLs.inventory_url)

    assert driver.current_url == URLs.inventory_url, 'Wrong url'
    assert inv_page.inventory_header().text == 'Products', 'Wrong page header'
    assert len(inv_page.inventory_cards()) > 0, 'There are no item cards on the inventory page'

    print(f'\nPerfomance glitch user...')


# case 1.5
# wrong auth:
@pytest.mark.negative
def test_auth_negative_wrong_login(driver):
    log_page = LoginPage(driver, URLs.url)
    log_page.open()

    log_page.input_user().send_keys(AuthData.wrong_user)
    log_page.input_pass().send_keys(AuthData.wrong_password)
    log_page.login_btn().click()

    assert driver.current_url == URLs.url, 'Wrong url'
    assert log_page.login_err_msg() == AuthLocs.login_err_msg, 'Login error'

    print(f'\nWrong login user... {log_page.login_err_msg()}')
