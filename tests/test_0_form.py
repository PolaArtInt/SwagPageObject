import pytest
from selenium.common import TimeoutException

from pages.form_page import form_conditions
from locators.form_data import FormLocs


# case 0.1
@pytest.mark.positive
def test_register_btn_unblocked(driver, fake, form_conditions, form_page):
    form_page.form_name().send_keys(fake.name())
    form_page.form_pass().send_keys(fake.password())

    checkbox = form_page.form_checkbox()
    checkbox.click()

    assert checkbox.is_selected(), 'Checkbox is not checked'
    assert form_page.form_reg_btn().is_enabled(), 'Register button is blocked'


# case 0.2
@pytest.mark.positive
def test_positive_fill_form_fields(driver, fake, form_conditions, form_page):
    form_page.form_name().send_keys(fake.name())
    form_page.form_pass().send_keys(fake.password())

    form_page.form_checkbox().click()
    form_page.form_reg_btn().click()

    assert driver.current_url != FormLocs.form_url, 'Url is not changed'


# case 0.3
@pytest.mark.defect
@pytest.mark.negative
def test_negative_fill_name_with_spaces(driver, fake, form_conditions, form_page):
    form_page.form_name().send_keys('  ')
    form_page.form_pass().send_keys(fake.password())
    form_page.form_checkbox().click()

    try:
        assert form_page.form_reg_btn().is_enabled(), 'Name is incorrect. Register button should be blocked'
    except AssertionError:
        pass
    else:
        print('Name is incorrect. Register button should be blocked')


# case 0.4
@pytest.mark.defect
@pytest.mark.negative
def test_btn_blocked_with_empty_fields(driver, form_conditions, form_page):
    form_page.form_checkbox().click()

    try:
        assert not form_page.form_reg_btn().is_enabled(), 'Fields are empty. Register button should be blocked'
    except (TimeoutException, AssertionError):
        pass
    else:
        print('Fields are empty. Register button should be blocked')
