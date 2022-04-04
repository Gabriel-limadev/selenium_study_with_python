from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = ''
browser = Chrome()
browser.get(url)

# ?CSS SELECTORS - SELETORES DE GRUPO
# Encontra qualquer tag label juntos com qualquer tag input
browser.find_elements(By.CSS_SELECTOR, 'label, input') 

# Encontra qualquer tag label que contenha o atributo for junto com qualquer type que termine em t
browser.find_elements(By.CSS_SELECTOR, 'label[for], *[type $= "t"]') 