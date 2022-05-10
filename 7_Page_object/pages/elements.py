from abc import ABC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException     
from page_objects import PageElement


class Todo(PageElement):
    name = (By.CSS_SELECTOR, '#todo-name')
    description = (By.CSS_SELECTOR, '#todo-desc')
    urgent = (By.CSS_SELECTOR, '#todo-next')
    submit = (By.CSS_SELECTOR, '#todo-submit')

    def create_todo(self, name, description, urgent=False):
        self.webdriver.find_element(*self.name).send_keys(name)
        self.webdriver.find_element(*self.description).send_keys(description)
        if urgent:
            self.webdriver.find_element(*self.urgent).click()
        self.webdriver.find_element(*self.submit).click()


class CardContainer(PageElement, ABC):
    @property
    def todos(self):
        cards = self.find_elements(self.card)
        po_cards = []
        [po_cards.append(Card(card)) for card in cards] 
        return po_cards


class Do(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_a fieldset')
    card = (By.CSS_SELECTOR, '.terminal-card')


class Doing(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_b fieldset')
    card = (By.CSS_SELECTOR, '.terminal-card')


class Done(CardContainer):
    fieldset = (By.CSS_SELECTOR, 'div.body_c fieldset')
    card = (By.CSS_SELECTOR, '.terminal-card')


class Card:
    def __init__(self, selenium_object):
        self.selenium_object = selenium_object
        self.name = (By.CSS_SELECTOR, 'header.name')
        self.description = (By.CSS_SELECTOR, 'div.description')
        self._button_do = (By.CSS_SELECTOR, 'button.do')
        self._button_cancel = (By.CSS_SELECTOR, 'button.cancel')
        self._load()
    
    def do_task(self):
        self.selenium_object.find_element(*self._button_do).click()
    
    def cancel_task(self):
        try:
            self.selenium_object.find_element(*self._button_cancel).click()
        except NoSuchElementException:
            print('Elemento isnt cancel button')

    def _load(self):
        self.name = self.selenium_object.find_element(*self.name).text
        self.description = self.selenium_object.find_element(*self.description).text
    
    def __repr__(self):
        return f'Card(name="{self.name}", description="{self.description}")'
