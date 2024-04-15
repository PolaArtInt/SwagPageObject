import pytest

from pages.inventory_page import InventoryPage
from pages.filter_page import FilterMod


@pytest.mark.positive
# case 5.1
def test_a_to_z_filter(driver, standard_auth):
    inv_page = InventoryPage(driver, standard_auth)
    filter_page = FilterMod(driver, standard_auth)

    # sort items a-z before clicking on a-z filter:
    items_before_a_z = inv_page.item_names()
    before_a_z = []
    for item in items_before_a_z:
        before_a_z.append(item.text)

    before_a_z.sort(reverse=False)
    print(f'\n{before_a_z}')

    # click a-z filter:
    filter_page.filter_a_z().click()

    # check if filter works properly:
    items_after_a_z = inv_page.item_names()
    after_a_z = []
    for item in items_after_a_z:
        after_a_z.append(item.text)
    print(f'\n{after_a_z}')

    assert before_a_z == after_a_z, 'Filter A to Z doesn\'t work properly'

    driver.refresh()


@pytest.mark.positive
# case 5.2
def test_z_to_a_filter(driver, standard_auth):
    inv_page = InventoryPage(driver, standard_auth)
    filter_page = FilterMod(driver, standard_auth)

    # sort items z-a before clicking on a-z filter:
    items_before_z_a = inv_page.item_names()
    before_z_a = []
    for item in items_before_z_a:
        before_z_a.append(item.text)

    before_z_a.sort(reverse=True)
    print(f'\n{before_z_a}')

    # click z-a filter:
    filter_page.filter_z_a().click()

    # check if filter works properly:
    items_after_z_a = inv_page.item_names()
    after_z_a = []
    for item in items_after_z_a:
        after_z_a.append(item.text)
    print(f'\n{after_z_a}')

    assert before_z_a == after_z_a, 'Filter Z to A doesn\'t work properly'

    driver.refresh()


@pytest.mark.positive
# case 5.3
def test_low_to_high_filter(driver, standard_auth):
    inv_page = InventoryPage(driver, standard_auth)
    filter_page = FilterMod(driver, standard_auth)

    # sort items low-high before clicking on low-high filter:
    prices_before_lo_hi = inv_page.item_prices()
    before_lo_hi = []
    for item in prices_before_lo_hi:
        before_lo_hi.append(float(item.text.lstrip('$')))

    before_lo_hi.sort(reverse=False)
    print(f'\n{before_lo_hi}')

    # click low-high filter:
    filter_page.filter_low_high().click()

    # check if filter works properly:
    prices_after_lo_hi = inv_page.item_prices()
    after_lo_hi = []
    for item in prices_after_lo_hi:
        after_lo_hi.append(float(item.text.lstrip('$')))
    print(f'\n{after_lo_hi}')

    assert before_lo_hi == after_lo_hi, 'Filter Low to High doesn\'t work properly'

    driver.refresh()


@pytest.mark.positive
# case 5.4
def test_high_to_low_filter(driver, standard_auth):
    inv_page = InventoryPage(driver, standard_auth)
    filter_page = FilterMod(driver, standard_auth)

    # sort items high-low before clicking on low-high filter:
    prices_before_hi_lo = inv_page.item_prices()
    before_hi_lo = []
    for item in prices_before_hi_lo:
        before_hi_lo.append(float(item.text.lstrip('$')))

    before_hi_lo.sort(reverse=True)
    print(f'\n{before_hi_lo}')

    # click high-low filter:
    filter_page.filter_high_low().click()

    # check if filter works properly:
    prices_after_hi_lo = inv_page.item_prices()
    after_hi_lo = []
    for item in prices_after_hi_lo:
        after_hi_lo.append(float(item.text.lstrip('$')))
    print(f'\n{after_hi_lo}')

    assert before_hi_lo == after_hi_lo, 'Filter Low to High doesn\'t work properly'

    driver.refresh()
