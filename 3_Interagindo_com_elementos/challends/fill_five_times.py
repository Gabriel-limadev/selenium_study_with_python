from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from urllib.parse import urlparse
from json import loads

url = 'https://selenium.dunossauro.live/exercicio_06.html'
b = Chrome()
b.get(url)
b.maximize_window()
sleep(1)

def fill_form(name_text, password_text):
    """Preenche o formulário de acordo com a descrição no titulo

    Args:
        name_text (str): nome a ser inserido no form
        password_text (str): senha a ser inserida no form
    """
    name_lin_col = b.find_element(By.CSS_SELECTOR, 'header span').text
    name = b.find_element(By.CSS_SELECTOR, f'.form-{name_lin_col} [type="text"]').send_keys(name_text)
    password = b.find_element(By.CSS_SELECTOR, f'.form-{name_lin_col} .form-group [type="password"]').send_keys(password_text)
    btn = b.find_element(By.CSS_SELECTOR, f'.form-{name_lin_col} [type="submit"]').click()

def validation_result_with_url():
    """
    Compara a url e o resultado obtido, verificando se são os mesmos.
    """
    result = b.find_element(By.CSS_SELECTOR, '#query > textarea').text
    result_better = result.replace('\'', "\"")
    dic_result = loads(result_better)
    final_result = []
    for k, v in dic_result.items():
        final_result.append(f'{k}: {v}')

    url_query = urlparse(b.current_url).query
    url_query = url_query.replace('=', ': ')
    url_query_list = url_query.split('&')
    url_query_list.pop()

    assert final_result == url_query_list


data = (
    {
        "name_text": "Gabriel",
        "password_text": "123456"
    }, 
    {
        "name_text": "Alisson",
        "password_text": "123456"
    }, 
    {
        "name_text": "Jaqueline",
        "password_text": "123456"
    }, 
    {
        "name_text": "Alessandro",
        "password_text": "123456"
    }, 
    {
        "name_text": "Alicia",
        "password_text": "123456"
    }, 
    
)

# Preenchendo 4 forms
for i in range(5):
    fill_form(**data[i])
    sleep(2)
    validation_result_with_url()