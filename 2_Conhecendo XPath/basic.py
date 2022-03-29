from selenium.webdriver import Chrome
from time import sleep
from pprint import pprint

url = 'https://rennerocha.github.io/xpath/'

browser = Chrome()
browser.get(url)

# Find elements H1
h1s = browser.find_elements_by_xpath("//h1")
# or
h1s = browser.find_elements_by_xpath("/html/body/h1")

for h1 in h1s:
    pprint(h1.text)

# Retorna a primeira tag abaixo de ul 
tag_abaixo = browser.find_elements_by_xpath("//ul/*")
pprint(tag_abaixo)

# Retorna todas as tags abaixo de ul (inclusive as que estão alinhadas)
tags_abaixo = browser.find_elements_by_xpath("//ul//*")
for tag in tags_abaixo:
    pprint(tags_abaixo)

# Pegando segundo li do primeiro ol -- no xpath o index começa em 1
li = browser.find_elements_by_xpath("//ol[1]/li[2]")
# or
li = browser.find_elements_by_xpath("(//ol/li)[2]")