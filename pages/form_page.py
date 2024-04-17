import pytest
from pages.base_page import BasePage
from locators.form_data import FormLocs


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


class FormPage(BasePage):
    def open(self):
        self.driver.get(FormLocs.form_url)

    def form_header(self):
        return self.is_visible(FormLocs.form_header)

    def form_name(self):
        return self.is_visible(FormLocs.form_name)

    def form_pass(self):
        return self.is_visible(FormLocs.form_pass)

    def form_checkbox(self):
        return self.is_visible(FormLocs.form_check)

    def form_reg_btn(self):
        return self.is_visible(FormLocs.form_reg_btn)
