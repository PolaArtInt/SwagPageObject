import pytest
import allure

from pages.base_test import BaseTest
from pages.login_page import login
from locators.urls import URLs


class TestItem(BaseTest):
    @allure.id('3.1')
    @allure.epic('item page')
    @allure.feature('item card')
    @allure.title('go to product card by clicking the item image')
    @pytest.mark.positive
    def test_click_on_item_img(self, driver, login, inv_page, item_page):
        with allure.step('pick the item description'):
            item_desc = inv_page.item_descs()[2].text

        with allure.step('pick the item image and clicking it'):
            inv_page.item_imgs()[2].click()

        with allure.step('check if the url changed and we can get the same item'):
            item_card_desc = item_page.card_desc().text
            assert item_page.get_url() != URLs.inventory_url and \
                   item_desc == item_card_desc, 'Different item description or wrong url'

    @allure.id('3.2')
    @allure.epic('item page')
    @allure.feature('item card')
    @allure.title('go to product card by clicking on item title')
    @pytest.mark.positive
    def test_click_on_item_title(self, driver, login, inv_page, item_page):
        with allure.step('pick the item description'):
            item_desc = inv_page.item_descs()[3].text

        with allure.step('pick the item title and clicking it'):
            inv_page.item_names()[3].click()

        with allure.step('check if the url is changed and we can get the same item'):
            item_card_desc = item_page.card_desc().text
            assert item_desc == item_card_desc and item_page.get_url() != URLs.url, \
                'Different item description or wrong url'
