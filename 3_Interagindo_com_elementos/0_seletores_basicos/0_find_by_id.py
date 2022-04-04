from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

url = 'https://selenium.dunossauro.live/aula_05_a.html'
browser = Chrome()
browser.get(url)
sleep(2)

#  Find by ID
div_python = browser.find_element(by=By.ID, value='python')
div_haskell = browser.find_element(by=By.ID, value='haskell')

pprint(div_python.text)
pprint(div_haskell.text)

browser.quit()