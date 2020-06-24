from homework_3.src.test.pages.base_page import BasePage


class MainPageLocators:
    """ Locators for the Google Search Page """
    page_url = 'http://3.122.51.38/litecart/'


class MainPage(BasePage, MainPageLocators):
    """ Methods and helpers to work with the Main Page """

    def open(self):
        self.driver.get(self.page_url)
