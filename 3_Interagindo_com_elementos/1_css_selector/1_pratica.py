from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://selenium.dunossauro.live/aula_06_a.html'
b = Chrome()
b.get(url)
b.maximize_window()

sleep(2)

# Using attr type [attr=value]
name     = b.find_element(By.CSS_SELECTOR, '[type="text"]')
password = b.find_element(By.CSS_SELECTOR, '[type="password"]')
btn      = b.find_element(By.CSS_SELECTOR, '[type="submit"]')

# Using [attr*=value]
# name     = b.find_element(By.CSS_SELECTOR, '[name *= "ome"]')

# Using [attr^=value]
# name     = b.find_element(By.CSS_SELECTOR, '[type ^= "pass"]')

# Using [attr$=value]
# name     = b.find_element(By.CSS_SELECTOR, '[type $= "word"]')


name.send_keys('Gabriel')
password.send_keys('123456')
btn.click()