from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class AmazonSearchPage:
    URL = 'https://www.amazon.in/'

    # Locators

    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        print('Loading')
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
