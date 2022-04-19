from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    staleness_of # Checks if element is active 
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'
b = Chrome()
b.get(url)
wdw = WebDriverWait(b, 30)

element = b.find_element(By.TAG_NAME, 'button')

wdw.until(
    staleness_of(element), "Element ins't able"
)