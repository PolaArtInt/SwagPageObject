import pytest

from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.menu_page import MenuMod
from pages.login_page import LoginPage
from pages.about_page import AboutPage

from locators.urls import URLs


# case 6.1
@pytest.mark.positive
def test_positive_logout(driver, standard_auth):
    menu_page = MenuMod(driver, standard_auth)
    log_page = LoginPage(driver, standard_auth)

    # find and click burger menu:
    menu_page.menu_btn().click()

    # find and click 'logout' button:
    menu_page.logout_btn().click()

    # check if we are on login page and 'Login' button appears:
    assert driver.current_url == URLs.login_url, 'Wrong url'

    log_btn = log_page.login_btn()
    assert log_page.login_btn(), 'Login button not appearing'
    assert log_btn.get_attribute('value') == 'LOGIN', 'Login button not found'


@pytest.mark.positive
# case 6.2
def test_positive_about_btn(driver, standard_auth):
    menu_page = MenuMod(driver, standard_auth)
    about_page = AboutPage(driver, standard_auth)

    # find and click burger menu:
    menu_page.menu_btn().click()

    # find and click 'about' button:
    menu_page.about_btn().click()

    # check expected url and title:
    curr_title = driver.title
    assert driver.current_url == URLs.about_url and \
           curr_title == about_page.exp_title(), 'Wrong page url or title'


@pytest.mark.defect
@pytest.mark.positive
# case 6.3
def test_reset_app_state_positive(driver, standard_auth):
    inv_page = InventoryPage(driver, standard_auth)
    cart_page = CartPage(driver, standard_auth)
    menu_page = MenuMod(driver, standard_auth)

    # add two items to cart:
    inv_page.add_btns()[4].click()
    inv_page.add_btns()[4].click()

    # check if cart quantity tag is 2:
    tag = cart_page.cart_tag()
    assert int(tag.text) == 2, 'Wrong items quantity in cart'

    # find and click burger menu:
    menu_page.menu_btn().click()

    # find and click 'reset app state' button:
    menu_page.reset_btn().click()

    # check if cart is empty:
    assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'

    try:
        assert len(inv_page.item_names()) == 0, 'Cart is not empty'
    except AssertionError:
        print(f'Cart is not empty. There are {len(inv_page.item_names())} items in it')

    driver.refresh()


@pytest.mark.defect
@pytest.mark.negative
# case 6.4
def test_reset_app_state_negative(driver, standard_auth):
    inv_page = InventoryPage(driver, standard_auth)
    cart_page = CartPage(driver, standard_auth)
    menu_page = MenuMod(driver, standard_auth)

    # check 'add to cart' buttons quantity before:
    add_btns_before = inv_page.add_btns()

    # add two items to cart:
    inv_page.add_btns()[0].click()
    inv_page.add_btns()[1].click()

    tag = cart_page.cart_tag()
    assert int(tag.text) == 2, 'Wrong items quantity in cart'

    # find and click burger menu:
    menu_page.menu_btn().click()

    # find and click 'reset app state' button:
    menu_page.reset_btn().click()

    # check if cart is empty:
    assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'

    # and check if some items are in cart:
    items_in_cart = cart_page.cart_remove_btns()
    assert len(items_in_cart) == 0, f'There are {len(items_in_cart)} items in a cart'

    # check if all 'add to cart' buttons are unpressed by its quantity before and after
    add_btns_after = inv_page.add_btns()

    try:
        assert len(add_btns_before) == len(add_btns_after), 'Buttons are not unpressed after reset the app'
    except AssertionError:
        print(f'\nThere are {len(add_btns_after)} "ADD TO CART" buttons instead of {len(add_btns_before)}')
        print(f'\nButtons are not unpressed after reset the app')

    driver.refresh()
