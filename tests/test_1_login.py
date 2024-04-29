import pytest
import requests
import allure

from pages.base_test import BaseTest
from locators.auth_module import AuthLocs, AuthData
from locators.urls import URLs


class TestLogin(BaseTest):
    @allure.id('1.1')
    @allure.epic('Auth page')
    @allure.feature('Auth')
    @allure.title('Standard user authorization')
    @pytest.mark.positive
    def test_auth_positive(self, driver):
        self.log_page.login('standard_user')

        with allure.step('check the current url, the page header and the items presence on the inventory page...'):
            assert self.inv_page.get_url() == URLs.inventory_url, 'Wrong url'
            assert self.inv_page.inventory_header().text == 'Products', 'Wrong page header'
            assert len(self.inv_page.inventory_cards()) > 0, 'There are no item cards on the inventory page'

    @allure.id('1.2')
    @allure.epic('Auth page')
    @allure.feature('Auth')
    @allure.title('Locked out user authorization')
    @pytest.mark.positive
    def test_auth_positive_locked_out_user(self, driver):
        self.log_page.login('locked_user')

        with allure.step('check the current url and the error message is provided...'):
            assert self.log_page.get_url() == URLs.url, 'Wrong url'
            assert self.log_page.locked_msg() == AuthLocs.locked_msg, 'Login error'

        print(f'\n{self.log_page.locked_msg()}')

    @allure.id('1.3')
    @allure.epic('Auth page')
    @allure.feature('Auth')
    @allure.title('Problem user authorization')
    @pytest.mark.positive
    def test_auth_positive_problem_user(self, driver):
        self.log_page.login('problem_user')

        with allure.step('check the current url, the page header and the items presence on the inventory page...'):
            assert self.inv_page.get_url() == URLs.inventory_url, 'Wrong url'
            assert self.inv_page.inventory_header().text == 'Products', 'Wrong page header'
            assert len(self.inv_page.inventory_cards()) > 0, 'There are no item cards on the inventory page'

    @allure.id('1.3.1')
    @allure.epic('Auth page')
    @allure.feature('Auth')
    @allure.title('Problem user authorization')
    @pytest.mark.defect
    @pytest.mark.negative
    def test_problem_user_negative_inventory_imgs(self, driver):
        self.log_page.login('problem_user')

        with allure.step('check if there are broken images on the inventory page...'):
            imgs = self.inv_page.item_imgs()
            broken_url_sample = 'WithGarbageOnItToBreakTheUrl'

            for img in imgs:
                response = requests.get(img.get_attribute('src'), stream=True)
                if response.status_code == 404:
                    assert response.status_code == 404, 'The image is not found'
                    assert broken_url_sample in img.get_dom_attribute('src'), 'The image is not visible'
                    print(f'\n{response} Image: {img.get_dom_attribute('src')} is not visible')

        with allure.step('check the current url...'):
            assert self.inv_page.get_url() == URLs.inventory_url, 'Wrong url'

    @allure.id('1.4')
    @allure.epic('Auth page')
    @allure.feature('Auth')
    @allure.title('Perfomance glitch user authorization')
    @pytest.mark.slow
    @pytest.mark.positive
    def test_auth_positive_performance_glitch_user(self, driver):
        self.log_page.login('glitch_user')

        with allure.step('check the current url and the items presence on the inventory page...'):
            assert self.inv_page.get_url() == URLs.inventory_url, 'Wrong url'
            assert self.inv_page.inventory_header().text == 'Products', 'Wrong page header'
            assert len(self.inv_page.inventory_cards()) > 0, 'There are no item cards on the inventory page'

    @allure.id('1.5')
    @allure.epic('Auth page')
    @allure.feature('Auth')
    @allure.title('Wrong data authorization')
    @pytest.mark.negative
    def test_auth_negative_wrong_login(self, driver):
        with allure.step('open the login page...'):
            self.log_page.open()

        with allure.step('log in with the wrong username and password...'):
            self.log_page.login(AuthData.wrong_user, AuthData.wrong_password)

        with allure.step('check the current url and the error message is provided...'):
            assert self.log_page.get_url() == URLs.url, 'Wrong url'
            assert self.log_page.login_err_msg() == AuthLocs.login_err_msg, 'Login error'

    @allure.id('1.6')
    @allure.epic('Auth page')
    @allure.feature('Auth')
    @allure.title('All users authorization')
    @pytest.mark.positive
    def test_login_with_all_users_from_list(self, driver):
        with allure.step('make standard user auth...'):
            self.log_page.open()
            self.log_page.login('standard_user')

        with allure.step('check if the current url is the inventory page url...'):
            assert self.inv_page.get_url() == URLs.inventory_url, 'Wrong url'

        self.menu_page.logout()

        with allure.step('make problem user auth'):
            self.log_page.open()
            self.log_page.login('problem_user')

        with allure.step('check if the current url is the inventory page url...'):
            assert self.inv_page.get_url() == URLs.inventory_url, 'Wrong url'

        self.menu_page.logout()

        with allure.step('make perfomance glitch user auth...'):
            self.log_page.open()
            self.log_page.login('glitch_user')

        with allure.step('check if the current url is the inventory page url...'):
            assert self.inv_page.get_url() == URLs.inventory_url, 'Wrong url'

        self.menu_page.logout()

        with allure.step('make locked out user auth...'):
            self.log_page.open()
            self.log_page.login('locked_user')

        with allure.step('check if the current url is the login page url and the error message is provided...'):
            assert self.log_page.get_url() == URLs.url, 'Wrong url'
            assert self.log_page.locked_msg() == AuthLocs.locked_msg, 'Login error'

    @allure.id('1.7')
    @allure.epic('Auth page')
    @allure.feature('Auth')
    @allure.title('Standard login and logout')
    @pytest.mark.positive
    def test_login_logout(self, driver, in_out):
        with allure.step('login as a standard user, verify the inventory url and logout...'):
            assert self.inv_page.get_url() == URLs.inventory_url, 'Wrong url'
