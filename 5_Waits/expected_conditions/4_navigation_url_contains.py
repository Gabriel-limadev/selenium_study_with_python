from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    url_contains, 
    url_matches
)

url = 'https://selenium.dunossauro.live/aula_10_c.html'
b = Chrome()
b.get(url)
b.maximize_window()

wdw = WebDriverWait(b, 10)

links = b.find_elements(By.TAG_NAME, '.body_b a')
links[0].click()

wdw.until(
    url_contains('selenium'),
    'Url does not contain the word "selenium"'
)

wdw.until(
    url_matches('http.*live'),
    'Url does not have this pattern'
)