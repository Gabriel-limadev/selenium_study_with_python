
# TODO: 1 - Open the page
# TODO: 2 - Wait for p and button
# TODO: 3 - Find for class .selenium 

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from functools import partial

# * doing 1
url = 'https://selenium.dunossauro.live/exercicio_09.html'
b = Chrome()
b.get(url)
b.maximize_window()

# Creating functions
def wait_element(element, browser):
    if browser.find_element(By.TAG_NAME, element):
        return True
    return False

def wait_class(element, browser):
    if browser.find_element(By.CSS_SELECTOR, element):
        return True
    return False

# Creating parcials
wait_p = partial(wait_element, 'p')
wait_class_selenium = partial(wait_class, '.selenium')

# Settings webDriverWait
wdw = WebDriverWait(b, 30, 0.1)

# * doing 2
wdw.until(wait_p, 'Element p not found!')
print(b.find_element(By.TAG_NAME, 'p').text)

# * doing 3

wdw.until(wait_class_selenium, 'Class .selenium not found!')
print(f'Class .selenium found!')