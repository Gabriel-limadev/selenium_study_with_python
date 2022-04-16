
# TODO: 1 - Open the page
# TODO: 2 - Wait for button
# TODO: 3 - Click in button
# TODO: 4 - wait for success message
# TODO: 5 - validate the message 

from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Creating class
class WaitElement:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, webdriver):
        if webdriver.find_elements(*self.locator):
            return True
        return False


locator_button = (By.CSS_SELECTOR, 'button')
locator_success = (By.ID, 'finished')

# * doing 1
url = 'https://selenium.dunossauro.live/aula_09_a.html'
b = Chrome() 
b.get(url)

# Settings webDriverWait
wdw = WebDriverWait(b, 10, 0.5) # segundos

# * doing 2
wdw.until(
    WaitElement(locator_button),
    'Button not found'
)

# * doing 3
b.find_element(By.TAG_NAME, 'button').click()

# * doing 4
wdw.until(
    WaitElement(locator_success), 
    "The success message did't appear"
)

# * doing 5
success = b.find_element(By.CSS_SELECTOR, '#finished') 
assert success.text == 'Carregamento concluído', "The success message is not right"