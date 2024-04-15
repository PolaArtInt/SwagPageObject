from pages.base_page import BasePage
from locators.cart_module import CartLocs


class CartPage(BasePage):
    def cart_header(self):
        return self.is_visible(CartLocs.cart_header)

    def cart_tag(self):
        return self.is_visible(CartLocs.cart_tag)

    def cart_tag_invisible(self):
        return self.is_invisible(CartLocs.cart_tag)

    def cart_container(self):
        return self.is_visible(CartLocs.cart)

    def cart_quantity_num(self):
        return self.is_visible(CartLocs.cart_quantity_num)

    def cart_btns(self):
        return self.find_elems(CartLocs.cart_btn)

    def cart_btn(self):
        return self.find_el(CartLocs.cart_btn)

    def cart_remove_btns(self):
        return self.find_elems(CartLocs.cart_remove_btn)

    def cart_remove_btn(self):
        return self.find_el(CartLocs.cart_remove_btn)
