from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.live/aula_09_a.html'
b = Chrome()
b.get(url)
b.implicitly_wait(30)

button = b.find_element(By.CSS_SELECTOR, 'button')
button.click()
box_success = b.find_element(By.CSS_SELECTOR, '#finished')
assert box_success.text == 'Carregamento concluído'


