from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

url = 'https://selenium.dunossauro.live/aula_11_a.html'
b = Chrome()
b.get(url)
b.maximize_window()

# Settings Alerts
alert = Alert(b)

b.find_element(By.CSS_SELECTOR, '#prompt').click()
alert.send_keys('My name')
alert.accept()