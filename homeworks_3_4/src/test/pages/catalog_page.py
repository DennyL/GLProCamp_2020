from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from homeworks_3_4.src.test.pages.base_page import BasePage


class CatalogPageLocators:

    add_new_product_button = (By.XPATH, '//ul[@class="list-inline"]//li[2]/a')
    add_new_category_button = (By.XPATH, '//ul[@class="list-inline"]//li[1]/a')

    # Add New Product subpage locators
    general_tab = (By.XPATH, '//a[contains(text(), "General")]')
    information_tab = (By.XPATH, '//a[contains(text(), "Information")]')
    prices_tab = (By.XPATH, '//a[contains(text(), "Prices")]')
    save_new_product_button = (By.CSS_SELECTOR, 'button[value="Save"]')
    delete_product_button = (By.CSS_SELECTOR, 'button[value="Delete"]')


class CatalogPage(BasePage, CatalogPageLocators):

    """ Methods to work with the Catalog Page """

    def open(self):
        page_locator = (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=catalog]')
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(page_locator))
        self.driver.find_element(*page_locator).click()
