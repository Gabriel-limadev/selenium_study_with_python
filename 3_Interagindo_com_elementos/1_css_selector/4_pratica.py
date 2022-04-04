from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://selenium.dunossauro.live/aula_06_a.html'
b = Chrome()
b.get(url)
b.maximize_window()


b.find_element(By.CSS_SELECTOR, 'label[for="nome"] ~ input').send_keys('Gabriel Lima')
b.find_element(By.CSS_SELECTOR, 'div.form-group > input[type="password"]').send_keys('123456')
r = b.find_element(By.CSS_SELECTOR, 'div.form-group > input[name="l0c0" ]').click()