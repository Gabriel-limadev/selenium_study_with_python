from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = ''
browser = Chrome()
browser.get(url)

# ?CSS SELECTORS  - BÁSICOS
#* FIND ID
browser.find_element(by=By.CSS_SELECTOR, value='#python')

#* FIND TAG
browser.find_element(by=By.CSS_SELECTOR, value='form')
browser.find_elements(by=By.CSS_SELECTOR, value='div')

#* FIND CLASS
browser.find_element(By.CSS_SELECTOR, '.form-group')
browser.find_elements(By.CSS_SELECTOR, 'div.form-group') # ttivs que tenham a class form-group

#* FIND ATTRIBUTE
browser.find_elements(By.CSS_SELECTOR, '[for]')
browser.find_elements(By.CSS_SELECTOR, '[type]')
browser.find_elements(By.CSS_SELECTOR, '[name]')

#*FIND ATTRIBUTE OPERATOR VALUE
"""
[attr  = value] -> exatamente igual
[attr *= value] -> todos que tenham a palavra (value) incluida 
[attr |= value] -> deve ser exatamente ou iniciar ex: meu teste -> attr |= "meu" -- daria certo
[attr ^= value] -> iniciado em 
[attr $= value] -> terminado em
[attr ~= value] -> Um deve ser exatamente igual
"""
browser.find_elements(By.CSS_SELECTOR, '[class="form-group"]')

# *UNIVERSAL
browser.find_elements(By.CSS_SELECTOR, '*')

# *COMBINADOS
browser.find_elements(By.CSS_SELECTOR, 'input[type $= "t"]') # qualquer input que terminal em t no atributo type
browser.find_elements(By.CSS_SELECTOR, 'input[for *= "n"]') # qualquer input que tenha a letra n no atributo for
browser.find_elements(By.CSS_SELECTOR, '*[for *= "n"]') # qualquer elemento que tenha a letra n no atributo for