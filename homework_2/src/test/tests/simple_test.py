import pytest
from homework_2.src.test.pages.search_page import GoogleSearchPage


@pytest.fixture(scope='session')
def page():
    search_page = GoogleSearchPage(with_browser='Chrome')
    search_page.open()
    yield search_page
    search_page.destroy_and_quit()


@pytest.mark.parametrize('word', ('Selenium', 'Python', 'Groovy'))
def test_search_in_google_com(page, word):
    """ verifies is Google Search page returns results for the words given as parameters """
    page.clear_search_box()
    page.search_for_a_word(word)
    assert word in page.search_top_result
