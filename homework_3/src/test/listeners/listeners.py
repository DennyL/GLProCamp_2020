from selenium.webdriver.support.events import AbstractEventListener
from homework_3.src.test.helpers.helpers import highlight_element


class FindAndClickListener(AbstractEventListener):

    def __init__(self):
        super().__init__()
        self.clicked_element_name = None

    def before_find(self, by, value, driver):
        print(f'[Starting search for element]: >>> {value} <<<')

    def after_find(self, by, value, driver):
        print(f'[Element has been found]: >>> {value} <<<')

    def before_click(self, element, driver):
        self.clicked_element_name = element.text
        print(f'[Clicking on element]: >>> {self.clicked_element_name} <<<')
        # NB: element highlighting extends time of the test run
        # set the highlight_time just enough for your purposes,
        # or disable thoroughly, if not needed
        highlight_element(element, driver, highlight_time=.2)

    def after_click(self, element, driver):
        print(f'[Element has been clicked]: >>> {self.clicked_element_name} <<<')

    def on_exception(self, exception, driver):
        print(f'[ISSUE FOUND]: !!! {exception} !!!')
