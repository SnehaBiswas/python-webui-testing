import pytest
from pages.amazon_search_page import AmazonSearchPage
from pages.results_page import AmazonResultPage


@pytest.mark.parametrize("searchItem", ("OnePlus", "randomitem"))
def test_amazon_search(browser, searchItem):
    search_page = AmazonSearchPage(browser)
    result_page = AmazonResultPage(browser)

    # searchItem = "bhytu"

    # Given the amazon home page is displayed
    search_page.load()

    # And the title contains "Amazon"
    assert "Amazon" in result_page.title()

    # When the user searches for item
    search_page.search(searchItem)

    # And the search result query is item
    assert searchItem == result_page.search_input_value()

    # And the search result links pertain to item
    assert result_page.result_count_for_phrase(searchItem) > 0
