from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    alert_is_present
)

url = 'https://selenium.dunossauro.live/aula_11_a.html'
b = Chrome()
b.get(url)
b.maximize_window()

# Settings WebDriverWait
wdw = WebDriverWait(b, 10)

b.find_element(By.CSS_SELECTOR, '#alertd').click()

# Alert
alert = wdw.until(
    alert_is_present(),
    'Alert not found!'
)
print('Alert found!')
alert.accept()