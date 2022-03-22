from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser = Chrome()
browser.get(url)

sleep(5)

h1 = browser.find_element(by=By.TAG_NAME, value='h1')
ps = browser.find_elements(by=By.TAG_NAME, value='p')

texts = {}
for i in range(0,3):
    texts.update({f'text{i+1}': ps[i].text})

dict1 = {h1.text:texts}   
print(dict1)

browser.quit()