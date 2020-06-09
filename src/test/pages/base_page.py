from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager


class BasePage:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # self.driver = webdriver.Opera(executable_path=OperaDriverManager().install())

    def open_page(self, url):
        self.driver.get(url)

    def destroy_and_quit(self):
        self.driver.quit()
