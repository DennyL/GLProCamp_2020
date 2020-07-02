import pytest
from homework_3.src.test.pages.main_page import MainPage


@pytest.fixture
def main_page(browser):
    page = MainPage(browser)
    page.open()
    yield page


def test_add_items_to_the_cart(main_page):
    """ verifies if items can be added to a cart
        and the qty number on the art badge increases by one as a new item added
    """
    main_page.click_on(main_page.first_product_in_page)
    # the click on locator function is being passed to the wrapper 'is_cart_qty_badge_number_grew'
    # that returns True if the qty number on the badge increased by 1 after the click, or False otherwise
    assert main_page.is_cart_qty_badge_number_grew(main_page.click_on)(main_page.add_to_cart_button) is True
