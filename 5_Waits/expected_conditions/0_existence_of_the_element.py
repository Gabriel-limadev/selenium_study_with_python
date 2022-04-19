from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located
)

url = 'https://selenium.dunossauro.live/aula_10_a.html'
b = Chrome()
b.get(url)
wdw = WebDriverWait(b, 30)

locator = (By.CSS_SELECTOR, '#request')

wdw.until(
    presence_of_element_located(locator)
)
print('The button appeared')
b.find_element(*locator).click()