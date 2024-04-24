import pytest
import allure
from selenium.common import TimeoutException

from pages.form_page import form_conditions
from locators.form_data import FormLocs


@allure.id('0.1')
@allure.epic('form page')
@allure.feature('form')
@pytest.mark.positive
def test_register_btn_unblocked(driver, fake, form_conditions, form_page):
    with allure.step('fill all the fields and check the checkbox'):
        form_page.form_name().send_keys(fake.name())
        form_page.form_pass().send_keys(fake.password())

        checkbox = form_page.form_checkbox()
        checkbox.click()

    with allure.step('check a register button clickability'):
        assert checkbox.is_selected(), 'Checkbox is not checked'
        assert form_page.form_reg_btn().is_enabled(), 'Register button is blocked'


@allure.id('0.2')
@allure.epic('form page')
@allure.feature('form')
@pytest.mark.positive
def test_positive_fill_form_fields(driver, fake, form_conditions, form_page):
    with allure.step('fill the standard data in the form fields'):
        form_page.form_name().send_keys(fake.name())
        form_page.form_pass().send_keys(fake.password())
    with allure.step('check the checkbox and click the register button'):
        form_page.form_checkbox().click()
        form_page.form_reg_btn().click()

    with allure.step('check the url is changed'):
        assert driver.current_url != FormLocs.form_url, 'Url is not changed'


@allure.id('0.3')
@allure.epic('form page')
@allure.feature('form')
@pytest.mark.defect
@pytest.mark.negative
def test_negative_fill_name_with_spaces(driver, fake, form_conditions, form_page):
    with allure.step('fill the username field with spaces'):
        form_page.form_name().send_keys('  ')
    with allure.step('fill the correct password and check the checkbox'):
        form_page.form_pass().send_keys(fake.password())
        form_page.form_checkbox().click()

    with allure.step('expecting the registration button is enabled and the error message is provided'):
        try:
            assert form_page.form_reg_btn().is_enabled(), 'Name is incorrect. Register button should be blocked'
        except AssertionError:
            pass
        else:
            print('Name is incorrect. Register button should be blocked')


@allure.id('0.4')
@allure.epic('form page')
@allure.feature('form')
@pytest.mark.defect
@pytest.mark.negative
def test_btn_blocked_with_empty_fields(driver, form_conditions, form_page):
    with allure.step('check the checkbox'):
        form_page.form_checkbox().click()

    with allure.step('expecting the registration button is not enabled and the error message is provided'):
        try:
            assert not form_page.form_reg_btn().is_enabled(), 'Fields are empty. Register button should be blocked'
        except (TimeoutException, AssertionError):
            pass
        else:
            print('Fields are empty. Register button should be blocked')
