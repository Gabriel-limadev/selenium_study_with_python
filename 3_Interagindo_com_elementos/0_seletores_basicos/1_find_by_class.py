from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

url = 'https://selenium.dunossauro.live/aula_05_b.html'
browser = Chrome()
browser.get(url)
sleep(2)

# Find by Class
topico = browser.find_element(by=By.CLASS_NAME, value='topico')
linguagens = browser.find_elements(by=By.CLASS_NAME, value='linguagens')
pprint(topico.text)
for lin in linguagens:
    pprint(lin.text.replace('\n', ': '))

# Take h2 in each lin
pprint(f'{"-+-"*5} Take h2 in each lin {"-+-"*5}')
for lin in linguagens:
    pprint((
        (lin.find_element(by=By.TAG_NAME, value='h2').text),
        (lin.find_element(by=By.TAG_NAME, value='p').text)
    ))

browser.quit()