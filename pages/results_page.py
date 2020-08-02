from selenium.webdriver.common.by import By


class AmazonResultPage:
    # Locators

    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')

    @classmethod
    def PHRASE_RESULTS(cls, phrase):
        xpath = "//div/h2/a/span[contains(text(),'"+phrase+"')]"
        return By.XPATH, xpath

    # Initializer

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def result_count_for_phrase(self, phrase):
        results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))

        return len(results)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')

    def title(self):
        return self.browser.title