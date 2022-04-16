
# TODO: 1 - Open the page
# TODO: 2 - Wait for button
# TODO: 3 - Click in button
# TODO: 4 - wait for success message
# TODO: 5 - validate the message 

from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from functools import partial

# Creating global functions
def wait_element(by, element, webdriver):
    """Checks if the element is on the screen"""
    if webdriver.find_element(by, element):
        return True
    return False

# Creating parcials
wait_button  = partial(wait_element, By.CSS_SELECTOR, 'button')
wait_success = partial(wait_element, By.ID, 'finished')

# * doing 1
url = 'https://selenium.dunossauro.live/aula_09_a.html'
b = Chrome() 
b.get(url)

# Settings webDriverWait
wdw = WebDriverWait(b, 10, 0.5) # segundos

# * doing 2
wdw.until(
    wait_button, 
    'Button not found'
)

# * doing 3
b.find_element(By.TAG_NAME, 'button').click()

# * doing 4
wdw.until(
    wait_success,
    "The success message did't appear"
)

# * doing 5
success = b.find_element(By.CSS_SELECTOR, '#finished') 
assert success.text == 'Carregamento concluído', "The success message is not right"