from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    title_is, 
    title_contains
)

url = 'https://selenium.dunossauro.live/aula_10_c.html'
b = Chrome()
b.get(url)
b.maximize_window()

wdw = WebDriverWait(b, 10)

links = b.find_elements(By.TAG_NAME, '.body_b a')
links[0].click()

wdw.until(
    title_is('selenium'),
    'Title is not "selenium"'
)
wdw.until(
    title_contains('aula'),
    'Title does not contain the word "aula"'
)