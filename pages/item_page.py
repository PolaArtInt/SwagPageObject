from pages.base_page import BasePage
from locators.item_module import ItemLocs


class ItemPage(BasePage):
    def card_add_btn(self):
        return self.find_el(ItemLocs.card_add_btn)

    def card_add_btns(self):
        return self.find_elems(ItemLocs.card_add_btn)

    def card_remove_btn(self):
        return self.find_el(ItemLocs.card_remove_btn)

    def card_remove_btns(self):
        return self.find_elems(ItemLocs.card_remove_btn)

    def card_img(self):
        return self.find_el(ItemLocs.card_img)

    def card_imgs(self):
        return self.find_elems(ItemLocs.card_img)

    def card_name(self):
        return self.find_el(ItemLocs.card_name)

    def card_names(self):
        return self.find_elems(ItemLocs.card_name)

    def card_desc(self):
        return self.find_el(ItemLocs.card_desc)

    def card_descs(self):
        return self.find_elems(ItemLocs.card_desc)

    def card_price(self):
        return self.find_el(ItemLocs.card_price)

    def card_prices(self):
        return self.find_elems(ItemLocs.card_price)
