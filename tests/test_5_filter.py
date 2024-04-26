import pytest
import allure
from allure_commons.types import AttachmentType

from pages.login_page import login


@allure.id('5.1')
@allure.epic('filter module')
@allure.feature('filter')
@allure.title('checking a to z filter')
@pytest.mark.positive
def test_a_to_z_filter(driver, login, inv_page, filter_page):
    with allure.step('sort the items by a a-z order before clicking the a-z filter'):
        items_before_a_z = inv_page.item_names()
        before_a_z = []
        for item in items_before_a_z:
            before_a_z.append(item.text)

        before_a_z.sort(reverse=False)
        print(f'\n{before_a_z}')

    with allure.step('click the a-z filter'):
        filter_page.filter_a_z().click()

    with allure.step('check if the filter works properly'):
        items_after_a_z = inv_page.item_names()
        after_a_z = []
        for item in items_after_a_z:
            after_a_z.append(item.text)
        print(f'\n{after_a_z}')

        assert before_a_z == after_a_z, 'Filter A to Z doesn\'t work properly'

    inv_page.refresh()
    allure.attach(driver.get_screenshot_as_png(), name='a_to_z_filter', attachment_type=AttachmentType.PNG)


@allure.id('5.2')
@allure.epic('filter module')
@allure.feature('filter')
@allure.title('checking z to a filter')
@pytest.mark.positive
def test_z_to_a_filter(driver, login, inv_page, filter_page):
    with allure.step('sort the items by a z-a order before clicking the a-z filter'):
        items_before_z_a = inv_page.item_names()
        before_z_a = []
        for item in items_before_z_a:
            before_z_a.append(item.text)

        before_z_a.sort(reverse=True)
        print(f'\n{before_z_a}')

    with allure.step('click the z-a filter'):
        filter_page.filter_z_a().click()

    with allure.step('check if the filter works properly'):
        items_after_z_a = inv_page.item_names()
        after_z_a = []
        for item in items_after_z_a:
            after_z_a.append(item.text)
        print(f'\n{after_z_a}')

        assert before_z_a == after_z_a, 'Filter Z to A doesn\'t work properly'

    inv_page.refresh()
    allure.attach(driver.get_screenshot_as_png(), name='z_to_a_filter', attachment_type=AttachmentType.PNG)


@allure.id('5.3')
@allure.epic('filter module')
@allure.feature('filter')
@allure.title('checking low to high filter')
@pytest.mark.positive
def test_low_to_high_filter(driver, login, inv_page, filter_page):
    with allure.step('sort the items by a low-high order before clicking the a-z filter'):
        prices_before_lo_hi = inv_page.item_prices()
        before_lo_hi = []
        for item in prices_before_lo_hi:
            before_lo_hi.append(float(item.text.lstrip('$')))

        before_lo_hi.sort(reverse=False)
        print(f'\n{before_lo_hi}')

    with allure.step('click the low-high filter'):
        filter_page.filter_low_high().click()

    with allure.step('check if the filter works properly'):
        prices_after_lo_hi = inv_page.item_prices()
        after_lo_hi = []
        for item in prices_after_lo_hi:
            after_lo_hi.append(float(item.text.lstrip('$')))
        print(f'\n{after_lo_hi}')

        assert before_lo_hi == after_lo_hi, 'Filter Low to High doesn\'t work properly'

    inv_page.refresh()
    allure.attach(driver.get_screenshot_as_png(), name='low_to_high_filter', attachment_type=AttachmentType.PNG)


@allure.id('5.4')
@allure.epic('filter module')
@allure.feature('filter')
@allure.title('checking high to low filter')
@pytest.mark.positive
def test_high_to_low_filter(driver, login, inv_page, filter_page):
    with allure.step('sort the items by a high-low order before clicking the a-z filter'):
        prices_before_hi_lo = inv_page.item_prices()
        before_hi_lo = []
        for item in prices_before_hi_lo:
            before_hi_lo.append(float(item.text.lstrip('$')))

        before_hi_lo.sort(reverse=True)
        print(f'\n{before_hi_lo}')

    with allure.step('click the high-low filter'):
        filter_page.filter_high_low().click()

    with allure.step('check if the filter works properly'):
        prices_after_hi_lo = inv_page.item_prices()
        after_hi_lo = []
        for item in prices_after_hi_lo:
            after_hi_lo.append(float(item.text.lstrip('$')))
        print(f'\n{after_hi_lo}')

        assert before_hi_lo == after_hi_lo, 'Filter Low to High doesn\'t work properly'

    inv_page.refresh()
    allure.attach(driver.get_screenshot_as_png(), name='high_to_low_filter', attachment_type=AttachmentType.PNG)
