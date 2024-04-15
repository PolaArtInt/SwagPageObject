from pages.base_page import BasePage
from locators.menu_module import MenuLocs


class MenuMod(BasePage):
    def menu_btn(self):
        return self.find_el(MenuLocs.menu_btn)

    def all_items_btn(self):
        return self.is_clickable(MenuLocs.all_items_btn)

    def about_btn(self):
        return self.is_clickable(MenuLocs.about_btn)

    def logout_btn(self):
        return self.is_clickable(MenuLocs.logout_btn)

    def reset_btn(self):
        return self.is_clickable(MenuLocs.reset_btn)

    def x_btn(self):
        return self.is_clickable(MenuLocs.x_btn)
