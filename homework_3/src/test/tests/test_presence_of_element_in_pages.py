import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from homework_3.src.test.pages.admin_page import AdminPage
from homework_3.src.test.testdata.testdata import Credentials


@pytest.fixture(params=Credentials.admin_credentials, scope='session')
def page(request):
    admin_page = AdminPage()
    admin_page.open()
    admin_page.login_to_the_system(request.param)
    yield admin_page
    admin_page.destroy_and_quit()


@pytest.mark.parametrize('page_locator', AdminPage.left_side_menu_items_locators)
@pytest.mark.parametrize('test_element_to_find', ((By.CSS_SELECTOR, 'div.panel-heading'),))
def test_presence_of_element_in_pages(page, page_locator, test_element_to_find,):
    """ verifies if the element passes as a parameter is present
        in all the pages accessible from the left side menu
    """
    WebDriverWait(page.driver, 5).until(ec.element_to_be_clickable(page_locator))
    page.driver.find_element(*page_locator).click()
    assert page.is_element_present_in_page(test_element_to_find) is True
