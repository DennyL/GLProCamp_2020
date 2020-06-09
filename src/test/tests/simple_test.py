import pytest
from src.test.pages.search_page import search_page


@pytest.fixture
def fixture():
    search_page.open()
    yield
    search_page.destroy_and_quit()


@pytest.mark.parametrize('word', ('Selenium',))
def test_search_in_google_com(fixture, word):
    """ verifies is Google Search page returns results for the words given as parameters """
    search_page.search_for_a_word(word)
    assert word in search_page.search_results
