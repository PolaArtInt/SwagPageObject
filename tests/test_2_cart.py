import pytest
import allure
from locators.urls import URLs


@allure.id('#2.1')
@allure.feature('cart module')
@allure.story('adding items to cart')
@pytest.mark.positive
def test_add_to_cart(driver, login, inv_page, cart_page):
    with allure.step('pick the item text and add the item to the cart'):
        item_title = inv_page.item_names()[3].text
        inv_page.add_btns()[3].click()

    with allure.step('check if the items quantity in the cart is equal to 1'):
        tag = cart_page.cart_tag().text
        assert int(tag) == 1, 'Wrong items quantity in cart'

    with allure.step('go to the cart'):
        cart_page.cart_btn().click()

    with allure.step('check if the item picked is the same item in the cart'):
        cart_item_title = inv_page.item_name().text
        assert item_title == cart_item_title, 'Different item picked'

    with allure.step('remove the item from the cart'):
        cart_page.cart_remove_btn().click()

    with allure.step('check if the cart is empty'):
        assert len(inv_page.item_names()) == 0, 'Cart is not empty'


@allure.id('#2.2')
@allure.feature('cart module')
@allure.story('removing items from cart')
@pytest.mark.positive
def test_remove_from_cart(driver, login, inv_page, cart_page):
    with allure.step('pick 3 items and add to the cart'):
        inv_page.add_btns()[5].click()
        inv_page.add_btns()[1].click()
        inv_page.add_btns()[3].click()

    with allure.step('check if the items quantity in the cart is equal to 3'):
        tag = cart_page.cart_tag().text
        assert int(tag) == 3, 'Cart is empty'

    with allure.step('go to the cart'):
        cart_page.cart_btn().click()

    with allure.step('check if the items quantity in the cart is equal to 3'):
        items_in_cart = inv_page.item_names()
        assert len(items_in_cart) == 3, 'Cart is empty'

    with allure.step('remove the items from the cart'):
        cart_remove_btns = cart_page.cart_remove_btns()
        for btn in cart_remove_btns:
            btn.click()

    with allure.step('check if the cart is empty'):
        items_in_cart = inv_page.item_names()
        assert len(items_in_cart) == 0, 'Cart is not empty'
        assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'


@allure.id('#2.3')
@allure.feature('cart module')
@allure.story('adding items to cart from item card')
@pytest.mark.positive
def test_add_item_from_item_card(driver, login, inv_page, cart_page, item_page):
    with allure.step('pick the item text and go to the item card'):
        item_title = inv_page.item_names()[3].text
        inv_page.item_names()[3].click()

    with allure.step('check if the item title is the same item title'):
        card_item_title = item_page.card_name().text
        assert item_title == card_item_title, 'Wrong item'

    with allure.step('add the item to the cart from the item page'):
        item_page.card_add_btn().click()

    with allure.step('go to the cart'):
        cart_page.cart_btn().click()

    with allure.step('check if the item title is the same item title and the url is the cart url'):
        cart_item_title = inv_page.item_name().text
        assert cart_item_title == card_item_title and driver.current_url == URLs.cart_url, 'Wrong url or different item'

    with allure.step('remove the item from the cart'):
        cart_page.cart_remove_btn().click()


@allure.id('#2.4')
@allure.feature('cart module')
@allure.story('removing items from cart from item card')
@pytest.mark.positive
def test_remove_item_from_item_card(driver, login, inv_page, cart_page, item_page):
    with allure.step('pick the item text and add the item to the cart'):
        item_title_before = inv_page.item_names()[2].text
        inv_page.add_btns()[2].click()

    with allure.step('check if the items quantity in the cart is equal to 1'):
        tag = cart_page.cart_tag()
        assert int(tag.text) == 1, 'Wrong quantity of items'

    with allure.step('go to the cart'):
        inv_page.item_names()[2].click()

    with allure.step('check the item title in the card'):
        item_title_after = item_page.card_name().text
        assert item_title_before == item_title_after, 'Wrong item title'

    with allure.step('click the remove button'):
        item_page.card_remove_btn().click()

    with allure.step('check if the button is changed'):
        btn_txt = item_page.card_add_btn().text
        assert btn_txt == 'ADD TO CART', 'Button is not changed'

    with allure.step('check if the cart is empty'):
        items_in_cart = inv_page.item_names()
        assert len(items_in_cart) == 0, 'Cart is not empty'

    with allure.step('check if the cart tag is not presenting on the page'):
        assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'
