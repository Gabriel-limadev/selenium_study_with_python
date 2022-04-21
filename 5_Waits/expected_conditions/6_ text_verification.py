from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    text_to_be_present_in_element,
    text_to_be_present_in_element_value
)

url = 'https://selenium.dunossauro.live/aula_10_d.html'
b = Chrome()
b.get(url)
b.maximize_window()

wdw = WebDriverWait(b, 30)

locator_h4 = (By.TAG_NAME, 'h4')
locator_email = (By.CSS_SELECTOR, 'input[name="email"]')

wdw.until(
    text_to_be_present_in_element(locator_h4, 'Digite'),
    "Element does not have 'Digite' text"
)
b.find_element(By.CSS_SELECTOR, 'input[name="nome"]').send_keys('João')

wdw.until(
    text_to_be_present_in_element_value(locator_email, 'disponível'),
    "Element does not have 'disponível' value"
)
b.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys('exemplo@gmail.com.br')