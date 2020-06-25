import pytest
from selenium.webdriver.common.by import By
from homework_3.src.test.pages.admin_page import AdminPage
from homework_3.src.test.pages.countries_page import CountriesPage
from homework_3.src.test.testdata.testdata import Credentials


@pytest.fixture(params=Credentials.admin_credentials, scope='session')
def admin_page(browser, request):
    page = AdminPage(browser)
    page.open()
    page.login_to_the_system(request.param)
    yield page


@pytest.fixture(scope='session')
def countries_page(browser):
    page = CountriesPage(browser)
    page.open()
    # the page opened, click on the first country in the list
    page.click_on_element(page.first_country_in_the_list)
    return page


@pytest.mark.parametrize('page_locators', AdminPage.left_side_menu_items_locators)
@pytest.mark.parametrize('test_element_to_find', ((By.CSS_SELECTOR, 'div.panel-heading'),))
def test_presence_of_element_in_pages(admin_page, page_locators, test_element_to_find,):
    """ verifies if the element passed as a parameter is present
        in all the pages accessible from the left side menu in the admin page
    """
    for element_name, element_locator in page_locators.items():
        admin_page.click_on_element(element_locator)
        assert admin_page.is_element_present_in_page(test_element_to_find) is True


@pytest.mark.parametrize('external_links', CountriesPage.in_country_external_links_locators)
def test_countries_external_links(countries_page, external_links):
    """ verifies if a click on each external link in the first country page
        opens it in a new window in a browser. Then switches to that window and closes it
    """
    for element_name, element_locator in external_links.items():
        # passing the click on locator to the wrapper
        # that returns True if number of opened windows increased by 1 after the click
        # or False otherwise
        assert countries_page.is_new_window_opened(countries_page.click_on_element)(element_locator) is True
        root_window = countries_page.driver.window_handles[0]
        new_window = countries_page.driver.window_handles[1]
        countries_page.driver.switch_to.window(new_window)
        countries_page.driver.close()
        countries_page.driver.switch_to.window(root_window)
