from pages.base_page import BasePage
from locators.form_data import FormLocs


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
