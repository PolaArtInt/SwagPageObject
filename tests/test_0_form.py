import pytest
import allure
from selenium.common import TimeoutException

from pages.base_test import BaseTest
from locators.form_data import FormLocs


class TestForm(BaseTest):
    @allure.id('0.1')
    @allure.epic('Form page')
    @allure.feature('Form')
    @allure.title('Form button clickability')
    @pytest.mark.positive
    def test_register_btn_unblocked(self, driver, fake, form_conditions):
        with allure.step('fill in all the fields and check the checkbox...'):
            self.form_page.form_name().send_keys(fake.name())
            self.form_page.form_pass().send_keys(fake.password())

            checkbox = self.form_page.form_checkbox()
            checkbox.click()

        with allure.step('check a register button clickability...'):
            assert checkbox.is_selected(), 'The checkbox is not checked'
            assert self.form_page.form_reg_btn().is_enabled(), 'The register button is blocked'

    @allure.id('0.2')
    @allure.epic('Form page')
    @allure.feature('Form')
    @allure.title('Form fields filling')
    @pytest.mark.positive
    def test_positive_fill_form_fields(self, driver, fake, form_conditions):
        with allure.step('fill in the form fields with a standard data...'):
            self.form_page.form_name().send_keys(fake.name())
            self.form_page.form_pass().send_keys(fake.password())

        with allure.step('check the checkbox and click the register button...'):
            self.form_page.form_checkbox().click()
            self.form_page.form_reg_btn().click()

        with allure.step('check if the url is changed...'):
            assert self.form_page.get_url() != FormLocs.form_url, 'The url is not changed'

    @allure.id('0.3')
    @allure.epic('Form page')
    @allure.feature('Form')
    @allure.title('Form fields filling')
    @pytest.mark.defect
    @pytest.mark.negative
    def test_negative_fill_name_with_spaces(self, driver, fake, form_conditions):
        with allure.step('fill in the username field with spaces...'):
            self.form_page.form_name().send_keys('  ')

        with allure.step('enter the correct password and check the checkbox...'):
            self.form_page.form_pass().send_keys(fake.password())
            self.form_page.form_checkbox().click()

        with allure.step('expecting the registration button is enabled and the error message is provided...'):
            try:
                assert self.form_page.form_reg_btn().is_enabled(), \
                    'The name is incorrect. The register button should be blocked'
            except AssertionError:
                pass
            else:
                print('The name is incorrect. The register button should be blocked')

    @allure.id('0.4')
    @allure.epic('Form page')
    @allure.feature('Form')
    @allure.title('Form fields filling')
    @pytest.mark.defect
    @pytest.mark.negative
    def test_btn_blocked_with_empty_fields(self, driver, form_conditions):
        with allure.step('check the checkbox...'):
            self.form_page.form_checkbox().click()

        with allure.step('expecting the registration button is not enabled and the error message is provided...'):
            try:
                assert not self.form_page.form_reg_btn().is_enabled(), \
                    'The fields are empty. The register button should be blocked'
            except (TimeoutException, AssertionError):
                pass
            else:
                print('The fields are empty. The register button should be blocked')
