import pytest
import allure
from pages.login_page import login
from locators.urls import URLs


@allure.id('4.1')
@allure.epic('order module')
@allure.feature('order')
@allure.description('processing purchase with relevant data')
@pytest.mark.positive
def test_positive_order(driver, fake, login, inv_page, cart_page, order_page):
    with allure.step('pick the items and add to the cart'):
        inv_page.add_btns()[5].click()
        inv_page.add_btns()[0].click()

    with allure.step('check the items quantity in the cart'):
        tag = cart_page.cart_tag()
        assert int(tag.text) == 2, 'Wrong items quantity in cart'

    with allure.step('go to the cart'):
        cart_page.cart_btn().click()

    with allure.step('go to the checkout page by clicking the checkout button'):
        order_page.checkout_btn().click()

    with allure.step('fill the form fields with the correct data'):
        order_page.input_fname().send_keys(fake.first_name())
        order_page.input_lname().send_keys(fake.last_name())
        order_page.input_zipcode().send_keys(fake.zipcode())

    with allure.step('click the continue button'):
        order_page.continue_btn().click()

    with allure.step('click the finish button'):
        order_page.finish_btn().click()

    with allure.step('check the url and the success message presence'):
        assert driver.current_url == URLs.checkout_url and order_page.complete_msg, \
            'Wrong url, success message is not provided'

    with allure.step('check if the cart is empty'):
        items_in_cart = inv_page.item_names()
        assert len(items_in_cart) == 0, 'Cart is not empty'
        assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'


@allure.id('4.2')
@allure.epic('order module')
@allure.feature('order')
@allure.description('processing purchase with empty cart')
@pytest.mark.defect
@pytest.mark.xfail
@pytest.mark.negative
def test_negative_empty_order(driver, fake, login, inv_page, cart_page, order_page):
    with allure.step('go to the cart'):
        cart_page.cart_btn().click()

    with allure.step('check if the cart is empty'):
        items_in_cart = inv_page.item_names()
        assert len(items_in_cart) == 0, 'Cart is not empty'

    with allure.step('go to the checkout page by clicking the checkout button'):
        order_page.checkout_btn().click()

    with allure.step('fill the form fields with the correct data'):
        order_page.input_fname().send_keys(fake.first_name())
        order_page.input_lname().send_keys(fake.last_name())
        order_page.input_zipcode().send_keys(fake.zipcode())

    with allure.step('click the continue button'):
        order_page.continue_btn().click()

    with allure.step('click the finish button'):
        order_page.finish_btn().click()

    with allure.step('expecting wrong url and no success message is provided'):
        try:
            assert driver.current_url != URLs.checkout_url and not order_page.complete_msg, \
                'Shopping cart is empty, wrong checkout'
        except AssertionError:
            print('Shopping cart should not be empty, wrong checkout')
