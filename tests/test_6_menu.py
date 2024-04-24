import pytest
import allure
from pages.login_page import login
from locators.urls import URLs


@allure.id('6.1')
@allure.epic('menu module')
@allure.feature('menu')
@allure.title('checking logout')
@pytest.mark.positive
def test_positive_logout(driver, login, log_page, menu_page):
    with allure.step('find and click the burger menu'):
        menu_page.menu_btn().click()

    with allure.step('find and click the logout button'):
        menu_page.logout_btn().click()

    with allure.step('check if we are on the login page and the login button appears'):
        assert driver.current_url == URLs.login_url, 'Wrong url'

        log_btn = log_page.login_btn()
        assert log_page.login_btn(), 'Login button not appearing'
        assert log_btn.get_attribute('value') == 'LOGIN', 'Login button not found'


@allure.id('6.2')
@allure.epic('menu module')
@allure.feature('menu')
@allure.title('checking about button clickability')
@pytest.mark.positive
def test_positive_about_btn(driver, login, menu_page, about_page):
    with allure.step('find and click the burger menu'):
        menu_page.menu_btn().click()

    with allure.step('find and click the about button'):
        menu_page.about_btn().click()

    with allure.step('check the expected url and the title'):
        curr_title = driver.title
        assert driver.current_url == URLs.about_url and \
               curr_title == about_page.exp_title(), 'Wrong page url or title'


@allure.id('6.3')
@allure.epic('menu module')
@allure.feature('menu')
@allure.title('checking reset button')
@pytest.mark.defect
@pytest.mark.positive
def test_reset_app_state_positive(driver, login, inv_page, cart_page, menu_page):
    with allure.step('add 2 items to the cart'):
        inv_page.add_btns()[4].click()
        inv_page.add_btns()[4].click()

    with allure.step('check if the cart quantity tag shows 2'):
        tag = cart_page.cart_tag()
        assert int(tag.text) == 2, 'Wrong items quantity in cart'

    with allure.step('find and clic the burger menu'):
        menu_page.menu_btn().click()

    with allure.step('find and click the reset app state button'):
        menu_page.reset_btn().click()

    with allure.step('check if the cart is empty'):
        assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'

    with allure.step('check if the items quantity in the cart is equal to 0'):
        try:
            assert len(inv_page.item_names()) == 0, 'Cart is not empty'
        except AssertionError:
            print(f'Cart is not empty. There are {len(inv_page.item_names())} items in it')

    cart_page.refresh()


@allure.id('6.4')
@allure.epic('menu module')
@allure.feature('menu')
@allure.title('checking app state after clicking on reset button')
@pytest.mark.defect
@pytest.mark.negative
def test_reset_app_state_negative(driver, login, inv_page, cart_page, menu_page):
    with allure.step('check the add to cart buttons quantity before'):
        add_btns_before = inv_page.add_btns()

    with allure.step('add 2 items to the cart'):
        inv_page.add_btns()[0].click()
        inv_page.add_btns()[1].click()

    with allure.step('check the items quantity in the cart is equal to 2'):
        tag = cart_page.cart_tag()
        assert int(tag.text) == 2, 'Wrong items quantity in cart'

    with allure.step('find and click the burger menu'):
        menu_page.menu_btn().click()

    with allure.step('find and click the reset app state button'):
        menu_page.reset_btn().click()

    with allure.step('check if the cart is empty'):
        assert cart_page.cart_tag_invisible(), 'Tag is visible, cart is not empty'

    with allure.step('check there are no items in the cart'):
        items_in_cart = cart_page.cart_remove_btns()
        assert len(items_in_cart) == 0, f'There are {len(items_in_cart)} items in a cart'

    with allure.step('check there are all add to cart buttons are unpressed by its quantity before and after'):
        add_btns_after = inv_page.add_btns()

        try:
            assert len(add_btns_before) == len(add_btns_after), 'Buttons are not unpressed after reset the app'
        except AssertionError:
            print(f'\nThere are {len(add_btns_after)} "ADD TO CART" buttons instead of {len(add_btns_before)}')
            print(f'\nButtons are not unpressed after reset the app')

    cart_page.refresh()
