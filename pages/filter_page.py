from pages.base_page import BasePage
from locators.filter_module import FilterLocs


class FilterMod(BasePage):
    def filter_a_z(self):
        return self.is_visible(FilterLocs.drop_a_z)

    def filter_z_a(self):
        return self.is_visible(FilterLocs.drop_z_a)

    def filter_low_high(self):
        return self.is_visible(FilterLocs.drop_low_high)

    def filter_high_low(self):
        return self.is_visible(FilterLocs.drop_high_low)
