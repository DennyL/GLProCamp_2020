from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.support.events import EventFiringWebDriver
from homeworks_3_4.src.test.listeners import listeners


class Links:
    LINK_TO_IMAGES_FOLDER = 'src/test/testdata/images'


class Browser:
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
        self.driver.maximize_window()

    def destroy_and_quit(self):
        self.driver.quit()
