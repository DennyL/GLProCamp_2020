from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:

    """ The base object that contains methods common to all the page objects in the app """

    def __init__(self, driver):
        self.driver = driver

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

    def click_on_element(self, locator):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @property
    def current_window_id(self):
        return self.driver.current_window_handle

    def is_new_window_opened(self, action):
        """ decorator that wraps an action passed as a parameter.
            Checks the number of opened windows before and after running the action
            :param action function to wrap
            :return :True if the difference before number of opened windows before and after is 1, False otherwise
        """
        def wrapper(locator):
            windows_before_click = self.driver.window_handles
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator))
            action(locator)
            windows_after_click = self.driver.window_handles
            return len(windows_after_click) - len(windows_before_click) == 1
        return wrapper

    def switch_to_root_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])

    def switch_to_newly_created_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def close_current_window(self):
        self.driver.close()
