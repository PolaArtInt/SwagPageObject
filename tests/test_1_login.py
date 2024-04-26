import pytest
import requests
import allure
from allure_commons.types import AttachmentType

from pages.login_page import locked_out_log, problem_log, glitch_log
from locators.auth_module import AuthLocs, AuthData
from locators.urls import URLs


@allure.id('1.1')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('standard user authorization')
@pytest.mark.positive
def test_auth_positive(driver, inv_page, login):
    with allure.step('check the current url, the page header and the items presence on the inventory page'):
        assert driver.current_url == URLs.inventory_url, 'Wrong url'
        assert inv_page.inventory_header().text == 'Products', 'Wrong page header'
        assert len(inv_page.inventory_cards()) > 0, 'There are no item cards on the inventory page'

    print(f'\nStandard user...')
    allure.attach(driver.get_screenshot_as_png(), name='auth_positive', attachment_type=AttachmentType.PNG)


@allure.id('1.2')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('locked out user authorization')
@pytest.mark.positive
def test_auth_positive_locked_out_user(driver, locked_out_log, log_page):
    with allure.step('check the current url and the error message is provided'):
        assert driver.current_url == URLs.url, 'Wrong url'
        assert log_page.locked_msg() == AuthLocs.locked_msg, 'Login error'

    print(f'\nLocked out user... {log_page.locked_msg()}')
    allure.attach(driver.get_screenshot_as_png(), name='auth_locked_out_user', attachment_type=AttachmentType.PNG)


@allure.id('1.3')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('problem user authorization')
@pytest.mark.positive
def test_auth_positive_problem_user(driver, problem_log, inv_page):
    with allure.step('check the current url, the page header and the items presence on the inventory page'):
        assert driver.current_url == URLs.inventory_url, 'Wrong url'
        assert inv_page.inventory_header().text == 'Products', 'Wrong page header'
        assert len(inv_page.inventory_cards()) > 0, 'There are no item cards on the inventory page'

    print(f'\nProblem user...')
    allure.attach(driver.get_screenshot_as_png(), name='auth_problem_user', attachment_type=AttachmentType.PNG)


@allure.id('1.3.1')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('problem user authorization')
@pytest.mark.defect
@pytest.mark.negative
def test_problem_user_negative_inventory_imgs(driver, problem_log, inv_page):
    with allure.step('check there are broken images on the inventory page'):
        imgs = inv_page.item_imgs()
        broken_url_sample = 'WithGarbageOnItToBreakTheUrl'

        for img in imgs:
            response = requests.get(img.get_attribute('src'), stream=True)
            if response.status_code == 404:
                assert response.status_code == 404, 'Image is not found'
                assert broken_url_sample in img.get_dom_attribute('src'), 'Image is not visible'
                print(f'\n{response} Image: {img.get_dom_attribute('src')} is not visible')

    with allure.step('check the current url'):
        assert driver.current_url == URLs.inventory_url, 'Wrong url'
    print(f'\nProblem user...')
    allure.attach(
        driver.get_screenshot_as_png(), name='auth_problem_user_negative_inventory_imgs',
        attachment_type=AttachmentType.PNG)


@allure.id('1.4')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('perfomance glitch user authorization')
@pytest.mark.slow
@pytest.mark.positive
def test_auth_positive_performance_glitch_user(driver, glitch_log, inv_page):
    with allure.step('check the current url and the items presence on the inventory page'):
        assert driver.current_url == URLs.inventory_url, 'Wrong url'
        assert inv_page.inventory_header().text == 'Products', 'Wrong page header'
        assert len(inv_page.inventory_cards()) > 0, 'There are no item cards on the inventory page'

    print(f'\nPerfomance glitch user...')
    allure.attach(
        driver.get_screenshot_as_png(), name='auth_performance_glitch_user', attachment_type=AttachmentType.PNG)


@allure.id('1.5')
@allure.epic('auth page')
@allure.feature('auth')
@allure.title('wrong data authorization')
@pytest.mark.negative
def test_auth_negative_wrong_login(driver, log_page):
    log_page.open()
    with allure.step('log in with the wrong username and password'):
        log_page.input_user().send_keys(AuthData.wrong_user)
        log_page.input_pass().send_keys(AuthData.wrong_password)
        log_page.login_btn().click()

    with allure.step('check the current url and the error message is provided'):
        assert driver.current_url == URLs.url, 'Wrong url'
        assert log_page.login_err_msg() == AuthLocs.login_err_msg, 'Login error'

    print(f'\nWrong login user... {log_page.login_err_msg()}')
    allure.attach(driver.get_screenshot_as_png(), name='auth_negative_wrong_login', attachment_type=AttachmentType.PNG)
