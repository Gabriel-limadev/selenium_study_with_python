from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    frame_to_be_available_and_switch_to_it,
    element_to_be_clickable
)

# Setting page
url = 'https://selenium.dunossauro.live/aula_11_d.html'
b = Chrome()
b.get(url)
b.maximize_window()

# Setting WebDriverWait
wdw = WebDriverWait(b, 30)

# Going for iframe
locator = (By.CSS_SELECTOR, 'iframe')
wdw.until(
    frame_to_be_available_and_switch_to_it(locator)
)

# Fill name for test
wdw.until(
    element_to_be_clickable(
        ('name', 'nome')
    )
)
nome = b.find_element(By.CSS_SELECTOR, '#nome' )
nome.send_keys('Gabriel')