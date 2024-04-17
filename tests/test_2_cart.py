import pytest
from locators.urls import URLs


# case 2.1
@pytest.mark.positive
def test_add_to_cart(driver, login, inv_page, cart_page):
    # pick item text:
    item_title = inv_page.item_names()[3].text

    # add item to cart:
    inv_page.add_btns()[3].click()

    # check if cart quantity tag is equal to 1 now:
    tag = cart_page.cart_tag().text
    assert int(tag) == 1, 'Wrong items quantity in cart'

    # go to cart:
    cart_page.cart_btn().click()

    # check if item picked is the same item in cart:
    cart_item_title = inv_page.item_name().text
    assert item_title == cart_item_title, 'Different item picked'

    # remove item from cart:
    cart_page.cart_remove_btn().click()

    # check if cart is empty:
    assert len(inv_page.item_names()) == 0, 'Cart is not empty'


# case 2.2
@pytest.mark.positive
def test_remove_from_cart(driver, login, inv_page, cart_page):
    # pick 3 items and add to cart:
    inv_page.add_btns()[5].click()
    inv_page.add_btns()[1].click()
    inv_page.add_btns()[3].click()

    # check if cart quantity tag is equal to 3:
    tag = cart_page.cart_tag().text
    assert int(tag) == 3, 'Cart is empty'

    # go to cart:
    cart_page.cart_btn().click()

    items_in_cart = inv_page.item_names()
    assert len(items_in_cart) == 3, 'Cart is empty'

    # remove all items from cart:
    cart_remove_btns = cart_page.cart_remove_btns()
    for btn in cart_remove_btns:
        btn.click()

    # check if cart is empty:
    items_in_cart = inv_page.item_names()
    assert len(items_in_cart) == 0, 'Cart is not empty'
    assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'


# case 2.3
@pytest.mark.positive
def test_add_item_from_item_card(driver, login, inv_page, cart_page, item_page):
    # pick item title click it and go to item card:
    item_title = inv_page.item_names()[3].text
    inv_page.item_names()[3].click()

    # check if item title is the same item title:
    card_item_title = item_page.card_name().text
    assert item_title == card_item_title, 'Wrong item'

    # add item to cart from item page:
    item_page.card_add_btn().click()

    # go to cart:
    cart_page.cart_btn().click()

    # check if item title is the same item title and url is cart url:
    cart_item_title = inv_page.item_name().text
    assert cart_item_title == card_item_title and driver.current_url == URLs.cart_url, 'Wrong url or different item'

    # remove item from cart:
    cart_page.cart_remove_btn().click()


# case 2.4
@pytest.mark.positive
def test_remove_item_from_item_card(driver, login, inv_page, cart_page, item_page):
    # pick item text and add item to cart:
    item_title_before = inv_page.item_names()[2].text
    inv_page.add_btns()[2].click()

    # check if items quantity in cart is equal to 1:
    tag = cart_page.cart_tag()
    assert int(tag.text) == 1, 'Wrong quantity of items'

    # go to item card:
    inv_page.item_names()[2].click()

    # check item title in card:
    item_title_after = item_page.card_name().text
    assert item_title_before == item_title_after, 'Wrong item title'

    # click remove button:
    item_page.card_remove_btn().click()

    # check the button changed:
    btn_txt = item_page.card_add_btn().text
    assert btn_txt == 'ADD TO CART', 'Button is not changed'

    # check if cart is empty:
    items_in_cart = inv_page.item_names()
    assert len(items_in_cart) == 0, 'Cart is not empty'

    assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'
