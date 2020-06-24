from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from homework_2.src.test.pages.base_page import BasePage


class GoogleSearchPageLocators:
    """ Locators for the Google Search Page """
    page_url = 'http://www.google.com'
    google_search_box = (By.NAME, 'q')


class GoogleSearchPage(BasePage, GoogleSearchPageLocators):
    """ Methods and helpers to work with the Google Search Page """

    def open(self):
        self.driver.get(self.page_url)

    def search_for_a_word(self, word):
        self.driver.find_element(*self.google_search_box).send_keys(word + Keys.ENTER)

    def clear_search_box(self):
        self.driver.find_element(*self.google_search_box).clear()

    @property
    def search_top_result(self):
        return self.driver.find_element(By.TAG_NAME, 'h3').text
