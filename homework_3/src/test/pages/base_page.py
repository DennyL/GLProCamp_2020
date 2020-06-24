from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.events import EventFiringWebDriver
from homework_3.src.test.listeners import listeners


class BasePage:

    """ The base object that contains methods common to all the page objects in the app """

    def __init__(self, with_browser='chrome'):
        if with_browser.lower() == 'chrome':
            self.plain_driver = webdriver.Chrome(ChromeDriverManager().install())
        elif with_browser.lower() == 'opera':
            self.plain_driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        else:
            raise Exception('Browser name is not defined')

        self.event_driver = EventFiringWebDriver(self.plain_driver, listeners.FindAndClickListener())

        self.driver = self.event_driver
        # in case event driver and listeners are not needed,
        # to switch to a plain driver
        # UNCOMMENT THE LINE BELOW:
        # self.driver = self.plain_driver

    def destroy_and_quit(self):
        self.driver.quit()

    def is_element_present_in_page(self, locator: tuple) -> bool:
        """ :param locator of the element to verify presence of
            :return: True is the element was found in the page, False otherwise
        """
        try:
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(locator))
            self.driver.find_element(*locator)
        except (NoSuchElementException, TimeoutException):
            return False
        return True
