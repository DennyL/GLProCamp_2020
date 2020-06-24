from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager


class BasePage:

    """ The base object that contains common to all the page objects in the app """

    def __init__(self, with_browser='chrome'):
        if with_browser.lower() == 'chrome':
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        elif with_browser.lower() == 'opera':
            self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        else:
            raise Exception('Browser name is not defined')

    def destroy_and_quit(self):
        self.driver.quit()
