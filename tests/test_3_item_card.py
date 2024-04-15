import pytest

from pages.inventory_page import InventoryPage
from pages.item_page import ItemPage

from locators.urls import URLs


@pytest.mark.positive
# case 3.1
def test_click_on_item_img(driver, standard_auth):
    inv_page = InventoryPage(driver, standard_auth)
    item_page = ItemPage(driver, standard_auth)

    # pick item description:
    item_desc = inv_page.item_descs()[2].text

    # pick item image and click:
    inv_page.item_imgs()[2].click()

    # check if url changed and we can get the same item:
    item_card_desc = item_page.card_desc().text
    assert driver.current_url != URLs.inventory_url and \
           item_desc == item_card_desc, 'Different item description or wrong url'


@pytest.mark.positive
# case 3.2
def test_click_on_item_title(driver, standard_auth):
    inv_page = InventoryPage(driver, standard_auth)
    item_page = ItemPage(driver, standard_auth)

    # pick item description:
    item_desc = inv_page.item_descs()[3].text

    # pick item title and click:
    inv_page.item_names()[3].click()

    # check if url changed and we can get the same item:
    item_card_desc = item_page.card_desc().text
    assert item_desc == item_card_desc and driver.current_url != URLs.url, 'Different item description or wrong url'
