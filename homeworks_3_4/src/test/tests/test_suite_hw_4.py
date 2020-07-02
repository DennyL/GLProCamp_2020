import pytest
from homeworks_3_4.src.test.pages.main_page import MainPage


@pytest.fixture(scope='session')
def main_page(browser):
    page = MainPage(browser)
    page.open()
    yield page


def test_add_items_to_the_cart(main_page):
    """ verifies if items can be added to a cart,
        and the qty number on the cart badge increases by one as a new item added
    """
    for item in main_page.popular_products_locators(qty=3):
        main_page.click_on(item)
        # the click on locator function is being passed to the wrapper 'is_cart_qty_badge_number_grew'
        # that returns True if the qty number on the badge increased by 1 after the click, or False otherwise
        assert main_page.is_cart_qty_badge_number_grew(main_page.click_on)(main_page.add_to_cart_button) is True
        main_page.open()


def test_remove_all_items_from_cart(main_page):
    """ verifies if items can be removed from a cart,
        and the qty number on the cart badge displays nothing after all items were removed
    """
    main_page.open()
    main_page.open_the_cart()
    main_page.remove_all_items_in_cart()
    main_page.open()
    assert main_page.cart_badge_number == 0

