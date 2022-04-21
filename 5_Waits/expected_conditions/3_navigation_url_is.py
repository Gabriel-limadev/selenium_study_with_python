from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    url_changes,
    url_to_be
)

url = 'https://selenium.dunossauro.live/aula_10_c.html'
b = Chrome()
b.get(url)
b.maximize_window()

wdw = WebDriverWait(b, 10)

link = b.find_element(By.TAG_NAME, '.body_b a')
link.click()
wdw.until(
    url_changes(url),
    "URL hasn't changed"
)
print(f'{url} \n{b.current_url}')

wdw.until(
    url_to_be(url+'#'),
    'Url changed'
)