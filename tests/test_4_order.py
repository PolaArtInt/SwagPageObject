import pytest
import allure

from pages.base_test import BaseTest
from locators.urls import URLs


class TestOrder(BaseTest):
    @allure.id('4.1')
    @allure.epic('Order module')
    @allure.feature('Order')
    @allure.title('Processing a purchase with a relevant data')
    @pytest.mark.positive
    def test_positive_order(self, driver, fake):
        self.log_page.login('standard_user')

        with allure.step('pick the items and add them to the cart...'):
            btns_list = self.inv_page.add_btns()
            pick_num = self.rand_num(len(btns_list))
            self.inv_page.add_btns()[pick_num].click()
            self.inv_page.add_btns()[pick_num].click()

        with allure.step('check the items quantity in the cart...'):
            tag = self.cart_page.cart_tag()
            assert int(tag.text) == 2, 'Wrong items quantity in cart'

        with allure.step('go to the cart...'):
            self.cart_page.cart_btn().click()

        with allure.step('go to the checkout page by clicking the checkout button...'):
            self.order_page.checkout_btn().click()

        with allure.step('fill the form fields with the correct data...'):
            self.order_page.input_fname().send_keys(fake.first_name())
            self.order_page.input_lname().send_keys(fake.last_name())
            self.order_page.input_zipcode().send_keys(fake.zipcode())

        with allure.step('click the continue button...'):
            self.order_page.continue_btn().click()

        with allure.step('click the finish button...'):
            self.order_page.finish_btn().click()

        with allure.step('check the url and the success message presence...'):
            assert self.order_page.get_url() == URLs.checkout_url and self.order_page.complete_msg(), \
                'Wrong url, a success message is not provided'

        with allure.step('check if the cart is empty...'):
            items_in_cart = self.inv_page.item_names()
            assert len(items_in_cart) == 0, 'The cart is not empty'
            assert self.cart_page.cart_tag_invisible(), 'The tag is visible, the cart is not empty'

    @allure.id('4.2')
    @allure.epic('Order module')
    @allure.feature('Order')
    @allure.title('Processing a purchase with an empty cart')
    @pytest.mark.defect
    @pytest.mark.xfail
    @pytest.mark.negative
    def test_negative_empty_order(self, driver, fake):
        self.log_page.login('standard_user')

        with allure.step('go to the cart...'):
            self.cart_page.cart_btn().click()

        with allure.step('check if the cart is empty...'):
            items_in_cart = self.inv_page.item_names()
            assert len(items_in_cart) == 0, 'The cart is not empty'

        with allure.step('go to the checkout page by clicking the checkout button...'):
            self.order_page.checkout_btn().click()

        with allure.step('fill in the form fields with a correct data...'):
            self.order_page.input_fname().send_keys(fake.first_name())
            self.order_page.input_lname().send_keys(fake.last_name())
            self.order_page.input_zipcode().send_keys(fake.zipcode())

        with allure.step('click the continue button...'):
            self.order_page.continue_btn().click()

        with allure.step('click the finish button...'):
            self.order_page.finish_btn().click()

        with allure.step('expecting wrong url and no success message is provided...'):
            try:
                assert self.order_page.get_url() != URLs.checkout_url and not self.order_page.complete_msg(), \
                    'The shopping cart is empty, wrong checkout'
            except AssertionError:
                print('The shopping cart should not be empty, wrong checkout')
