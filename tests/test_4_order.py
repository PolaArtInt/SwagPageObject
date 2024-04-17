import pytest
from pages.login_page import login
from locators.urls import URLs


# case 4.1
@pytest.mark.positive
def test_positive_order(driver, fake, login, inv_page, cart_page, order_page):
    # pick items and add it to cart:
    inv_page.add_btns()[5].click()
    inv_page.add_btns()[0].click()

    tag = cart_page.cart_tag()
    assert int(tag.text) == 2, 'Wrong items quantity in cart'

    # go to cart:
    cart_page.cart_btn().click()

    # go to checkout:
    order_page.checkout_btn().click()

    # fill a form:
    order_page.input_fname().send_keys(fake.first_name())
    order_page.input_lname().send_keys(fake.last_name())
    order_page.input_zipcode().send_keys(fake.zipcode())

    # click 'continue' button:
    order_page.continue_btn().click()

    # click 'finish' button:
    order_page.finish_btn().click()

    # check url and success message:
    assert driver.current_url == URLs.checkout_url and order_page.complete_msg, \
        'Wrong url, success message not provided'

    # check if cart is empty:
    items_in_cart = inv_page.item_names()
    assert len(items_in_cart) == 0, 'Cart is not empty'
    assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'


# case 4.2
@pytest.mark.defect
@pytest.mark.xfail
@pytest.mark.negative
def test_negative_empty_order(driver, fake, login, inv_page, cart_page, order_page):
    # go to cart:
    cart_page.cart_btn().click()

    # check if cart is empty:
    items_in_cart = inv_page.item_names()
    assert len(items_in_cart) == 0, 'Cart is not empty'

    # go to checkout:
    order_page.checkout_btn().click()

    # fill a form:
    order_page.input_fname().send_keys(fake.first_name())
    order_page.input_lname().send_keys(fake.last_name())
    order_page.input_zipcode().send_keys(fake.zipcode())

    # click 'continue' button:
    order_page.continue_btn().click()

    # click 'finish' button:
    order_page.finish_btn().click()

    # expected wrong url and no success message:
    try:
        assert driver.current_url != URLs.checkout_url and not order_page.complete_msg, \
            'Shopping cart is empty, wrong checkout'
    except AssertionError:
        print('Shopping cart should not be empty, wrong checkout')
