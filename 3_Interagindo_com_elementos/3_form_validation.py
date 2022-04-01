from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint
from urllib.parse import urlparse
from json import loads

url = 'https://selenium.dunossauro.live/aula_05.html'
browser = Chrome()
browser.get(url)
browser.maximize_window()
sleep(3)

def fill_form(browser, nome, email, senha, telefone):
    browser.find_element(by=By.NAME, value='nome').send_keys(nome)
    browser.find_element(by=By.NAME, value='email').send_keys(email)
    browser.find_element(by=By.NAME, value='senha').send_keys(senha)
    browser.find_element(by=By.NAME, value='telefone').send_keys(telefone)
    browser.find_element(by=By.NAME, value='btn').click()


data = {
    'nome': 'Gabriel Lima', 
    'email': 'gabriel.lima@gmail.com', 
    'senha': '123456', 
    'telefone': '(11)95946-1782'
}

fill_form(browser, **data)

sleep(2)

# Validation
result_text = browser.find_element(by=By.ID, value='result').text
""" or
parsed_url    = urlparse(browser.current_url)
returned_data = parsed_url.query.split('&')
""" 
result_better = result_text.replace('\'', "\"")
result_better = result_better.replace('+', ' ')
dic_result = loads(result_better)  

assert dic_result == data

sleep(2)
browser.quit()