from abc import ABC

class SeleniumObject:
    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)


class Page(ABC, SeleniumObject):
    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url

    def open(self):
        self.webdriver.get(self.url)
        self.webdriver.maximize_window()
        self.__reflection()

    def __reflection(self):
        for attribute in dir(self):
            real_attribute = getattr(self, attribute)
            if isinstance(real_attribute, PageElement): 
                real_attribute.webdriver = self.webdriver


class PageElement(ABC, SeleniumObject):
    def __init__(self, webdriver=None):
        self.webdriver = webdriver