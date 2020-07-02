from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from homework_3.src.test.pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class MainPageLocators:

    """ Locators for the Main Page """

    page_url = 'http://3.122.51.38/litecart/'

    first_product_in_page = (By.CSS_SELECTOR, 'section#box-campaign-products a.link[data-id="1"]')
    add_to_cart_button = (By.CSS_SELECTOR, 'button[name="add_cart_product"]')
    go_to_cart_button = (By.CSS_SELECTOR, 'div#cart a')
    cart_qty_badge = (By.CSS_SELECTOR, 'div#cart a .badge.quantity')


class MainPage(BasePage, MainPageLocators):

    """ Methods to work with the Main Page """

    def open(self):
        self.driver.get(self.page_url)

    def is_cart_qty_badge_number_grew(self, action):
        """ decorator that wraps an action passed as a parameter.
            Checks the number displayed on the cart quantity badge before running the action.
            Waits till the number increased by 1
            :param action function to wrap
            :return :True if after running the action the quantity increased by 1, False otherwise
        """
        def wrapper(locator):
            qty_badge = self.driver.find_element(*self.cart_qty_badge)
            qty_before_action = int(qty_badge.text) if qty_badge.text != '' else 0
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator))
            action(locator)
            try:
                WebDriverWait(self.driver, 5).until(
                    ec.text_to_be_present_in_element(self.cart_qty_badge, str(qty_before_action + 1))
                )
            except (TimeoutException, NoSuchElementException):
                return False
            return True
        return wrapper
