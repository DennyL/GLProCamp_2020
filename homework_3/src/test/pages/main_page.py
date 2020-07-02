from selenium.webdriver.common.by import By
from homework_3.src.test.pages.base_page import BasePage


class MainPageLocators:

    """ Locators for the Main Page """

    page_url = 'http://3.122.51.38/litecart/'

    first_product_in_page = (By.CSS_SELECTOR, 'section#box-campaign-products a.link[data-id="1"]')
    add_to_cart_button = (By.CSS_SELECTOR, 'button[name="add_cart_product"]')
    go_to_cart_button = (By.CSS_SELECTOR, 'div#cart a')


class MainPage(BasePage, MainPageLocators):

    """ Methods to work with the Main Page """
    pass
