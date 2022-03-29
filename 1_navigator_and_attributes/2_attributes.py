from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'http://selenium.dunossauro.live/aula_04_a.html'
browser = Chrome()
browser.get(url)

sleep(3)

def find_by_text(browser, tag, text):
    """Find the element with the text 'text'

    Args:
        browser (list): Browser instance(firefox, Chrome...)
        text (str): Content that must be in the tag
        tag (str): Where the text will be searched
    """
    elements = browser.find_elements(by=By.TAG_NAME, value=tag)
    for element in elements:
        if element.text == text:
            return element


def find_by_href(browser, link):
    """Find element 'a' with text 'link

    Args:
        browser (list): Browser instance(firefox, Chrome...)
        link (str): Link that will be searched for in all 'as'
    """
    elements = browser.find_elements(by=By.TAG_NAME, value='a')

    for element in elements:
        if link in element.get_attribute('href'):
            return element
        

# element_ddg = find_by_text(browser, 'li', 'DuckDuckGo')
element_ddg = find_by_href(browser, 'ddg')
print(element_ddg.text)