from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from src.test.pages.base_page import BasePage


class GoogleSearchPageLocators:
    """ Locators for the Google Search Page """
    google_search_box = (By.NAME, 'q')


class GoogleSearchPage(BasePage):
    """ Methods and helpers to work with the Google Search Page """
    def open(self):
        self.driver.get('http://www.google.com')

    def search_for_a_word(self, word):
        self.driver.find_element(*GoogleSearchPageLocators.google_search_box).send_keys(word + Keys.ENTER)

    @property
    def search_results(self):
        return [result.text for result in self.driver.find_elements(By.TAG_NAME, 'h3')]


search_page = GoogleSearchPage()
