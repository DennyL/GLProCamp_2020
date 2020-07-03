import pytest
from homeworks_3_4.src.test.config import Browser
from homeworks_3_4.src.test.testdata.testdata import Credentials
from homeworks_3_4.src.test.pages.admin_page import AdminPage
from homeworks_3_4.src.test.pages.main_page import MainPage
from homeworks_3_4.src.test.pages.countries_page import CountriesPage


@pytest.fixture(scope='session')
def browser():
    browser = Browser(with_browser='Chrome')
    yield browser.driver
    browser.destroy_and_quit()


@pytest.fixture(params=Credentials.admin_credentials, scope='session')
def admin_page(browser, request):
    page = AdminPage(browser)
    page.open()
    page.login_with(request.param)
    yield page


@pytest.fixture(scope='session')
def main_page(browser):
    page = MainPage(browser)
    page.open()
    yield page


@pytest.fixture(scope='session')
def countries_page(browser, admin_page):
    page = CountriesPage(browser)
    page.open()
    # click on the first country in the list
    page.click_on(page.first_country_in_the_list)
    yield page
