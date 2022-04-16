
# TODO: 1 - Open the page
# TODO: 2 - Wait for button
# TODO: 3 - Click in button


from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# * doing 1
url = 'https://selenium.dunossauro.live/aula_09_a.html'
b = Chrome() 
b.get(url)

# Settings webDriverWait and doing functions
wdw = WebDriverWait(b, 10, 0.5) # segundos

def wait_button(webdriver):
    """checks if the 'button' element is on the screen"""
    elements = webdriver.find_elements(By.CSS_SELECTOR, 'button') 
    return bool(elements)

def wait_success(webdriver):
    """checks if the success message is on the screen"""
    elements = webdriver.find_elements(By.CSS_SELECTOR, '#finished') 
    return bool(elements)

# * doing 2
wdw.until(wait_button, 'Button not found')

# * doing 3
b.find_element(By.TAG_NAME, 'button').click()

wdw.until(wait_success, "The success message did't appear")
success = b.find_element(By.CSS_SELECTOR, '#finished') 
assert success.text == 'Carregamento concluído'



