import pytest
from selenium.webdriver.common.by import By
from homeworks_3_4.src.test.pages.admin_page import AdminPage
from homeworks_3_4.src.test.pages.countries_page import CountriesPage


@pytest.mark.parametrize('page_locators', AdminPage.left_side_menu_items_locators)
@pytest.mark.parametrize('test_element_to_find', ((By.CSS_SELECTOR, 'div.panel-heading'),))
def test_presence_of_element_in_pages(admin_page, page_locators, test_element_to_find,):
    """ verifies if the element passed as a parameter is present
        in all the pages accessible from the left side menu in the admin page
    """
    for element_name, element_locator in page_locators.items():
        admin_page.click_on(element_locator)
        assert admin_page.is_element_present_in_page(test_element_to_find) is True


@pytest.mark.parametrize('external_links', CountriesPage.in_country_external_links_locators)
def test_countries_external_links(countries_page, external_links):
    """ verifies if a click on each external link in the first country page
        opens it in a new window in a browser. Then switches to that window and closes it
    """
    for element_name, element_locator in external_links.items():
        # the click on locator function is being passed to the wrapper 'is_new_window_opened'
        # that returns True if number of opened windows increased by 1 after the click, or False otherwise
        assert countries_page.is_new_window_opened(countries_page.click_on)(element_locator) is True
        countries_page.switch_to_newly_created_window()
        countries_page.close_current_window()
        countries_page.switch_to_root_window()
