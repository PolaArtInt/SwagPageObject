import pytest
from pages.login_page import login
from locators.urls import URLs


# case 3.1
@pytest.mark.positive
def test_click_on_item_img(driver, login, inv_page, item_page):
    # pick item description:
    item_desc = inv_page.item_descs()[2].text

    # pick item image and click:
    inv_page.item_imgs()[2].click()

    # check if url changed and we can get the same item:
    item_card_desc = item_page.card_desc().text
    assert driver.current_url != URLs.inventory_url and \
           item_desc == item_card_desc, 'Different item description or wrong url'


# case 3.2
@pytest.mark.positive
def test_click_on_item_title(driver, login, inv_page, item_page):
    # pick item description:
    item_desc = inv_page.item_descs()[3].text

    # pick item title and click:
    inv_page.item_names()[3].click()

    # check if url changed and we can get the same item:
    item_card_desc = item_page.card_desc().text
    assert item_desc == item_card_desc and driver.current_url != URLs.url, 'Different item description or wrong url'
