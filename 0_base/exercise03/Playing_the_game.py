from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser = Chrome()
browser.get(url)

sleep(3)

a = browser.find_element(by=By.TAG_NAME, value='a')
a.click()
ps = browser.find_elements(by=By.TAG_NAME, value='p')

while not ps[1].text[-1] == ps[-1].text[-1]:
    a.click()
    ps = browser.find_elements(by=By.TAG_NAME, value='p')

sleep(2)
browser.quit()

