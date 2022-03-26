from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'http://selenium.dunossauro.live/aula_04_b.html'
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

box_names = ['um', 'dois', 'tres', 'quatro']
for name in box_names:
    find_by_text(browser, 'div', name).click()

for name in box_names:
    sleep(0.2)
    browser.back()


for name in box_names:
    sleep(0.2)
    browser.forward()