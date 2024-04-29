import pytest
import allure

from pages.base_test import BaseTest
from locators.urls import URLs


class TestItem(BaseTest):
    @allure.id('3.1')
    @allure.epic('Item page')
    @allure.feature('Item card')
    @allure.title('Go to a product card by clicking on the item image')
    @pytest.mark.positive
    def test_click_on_item_img(self, driver):
        self.log_page.login('standard_user')

        with allure.step('pick the item description...'):
            item_desc = self.inv_page.item_descs()[2].text

        with allure.step('pick the item image and click on it...'):
            self.inv_page.item_imgs()[2].click()

        with allure.step('check if the url changed and we can get the same item...'):
            item_card_desc = self.item_page.card_desc().text
            assert self.item_page.get_url() != URLs.inventory_url and \
                   item_desc == item_card_desc, 'A different item description or wrong url'

    @allure.id('3.2')
    @allure.epic('Item page')
    @allure.feature('Item card')
    @allure.title('Go to product card by clicking on item title')
    @pytest.mark.positive
    def test_click_on_item_title(self, driver):
        self.log_page.login('standard_user')

        with allure.step('pick the item description...'):
            item_desc = self.inv_page.item_descs()[3].text

        with allure.step('pick the item title and click on it...'):
            self.inv_page.item_names()[3].click()

        with allure.step('check if the url is changed and we can get the same item...'):
            item_card_desc = self.item_page.card_desc().text
            assert item_desc == item_card_desc and self.item_page.get_url() != URLs.url, \
                'A different item description or wrong url'
