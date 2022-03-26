"""
TODO: 1. Take all class links -> {'class name': 'link da aula'}
TODO: 2. Navigate to Exercise 3 -> find the url of exercise 3 and go there
"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

url = 'http://selenium.dunossauro.live/aula_04.html'
browser = Chrome()
browser.get(url)
sleep(2)

# UTILS 
def get_links(browser, element):
    """ Take all links inside an element

    Args:
        browser (object): browser intancia
        element (str): webelement ['aside', 'main', 'body']
    """
    result = {}
    element = browser.find_element(by=By.TAG_NAME, value=element)
    ancoras = element.find_elements(by=By.TAG_NAME, value='a')

    for ancora in ancoras:
        result.update({ancora.text : ancora.get_attribute('href')})
    
    return result

# 1 PART
classes = get_links(browser, 'aside')
pprint(classes)

# browser.get(result_1['Aula 3'])

# 2 PART
exercises = get_links(browser, 'main')
browser.get(exercises['Exercício 3'])

