from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from json import loads

url = 'https://selenium.dunossauro.live/exercicio_04.html'
browser = Chrome()
browser.get(url)
browser.maximize_window()
sleep(3)


def fill_form(browser, nome, email, senha, telefone):
    """ Fill the form with the user data

    Args:
        browser (class): Browser instance(firefox, Chrome...)
        nome (str): username
        email (str): user email 
        senha (str): user password
        telefone (str): user phone
    """
    browser.find_element(by=By.NAME, value='nome').send_keys(nome)
    browser.find_element(by=By.NAME, value='email').send_keys(email)
    browser.find_element(by=By.NAME, value='senha').send_keys(senha)
    browser.find_element(by=By.NAME, value='telefone').send_keys(telefone)
    browser.find_element(by=By.NAME, value='btn').click()

# Data to be sent
data = {
    'nome': 'Gabriel', 
    'email': 'gabriel.lima@gmail.com',
    'senha': '123456',
    'telefone': '(11)95946-1782'
}
fill_form(browser, **data)

# Validation

# User submission result and turning into a list
result = browser.find_element(by=By.TAG_NAME, value='textarea').text
result_better = result.replace('\'', "\"")
dic_result = loads(result_better)  
final_result = []
for k, v in dic_result.items():
    final_result.append(f'{k}: {v}')

# Taking URL and transforming it
url_query = urlparse(browser.current_url).query
url_query_list = url_query.split('&')

for i, re in enumerate(url_query_list):
    url_query_list[i] = re.replace('=', ': ')
    url_query_list[i] = url_query_list[i].replace('%40', '@')
    url_query_list[i] = url_query_list[i].replace('%28', '(')
    url_query_list[i] = url_query_list[i].replace('%29', ')')

# Removing the button part of the url
url_query_list.pop()

# Making the comparison
assert final_result == url_query_list

sleep(2)
browser.quit()