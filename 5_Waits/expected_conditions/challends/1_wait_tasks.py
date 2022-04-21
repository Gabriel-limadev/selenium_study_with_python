"""
TODO: 1 - open the page
TODO: 2 - fill the form
TODO: 3 - wait for area do
TODO: 4 - wait for area doing
TODO: 5 - wait for area done
"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import (
    text_to_be_present_in_element    
)

# Creating functions
def fill_form(browser, task_name, task_description, checkbox=False):
    browser.find_element(By.CSS_SELECTOR, '#todo-name').send_keys(task_name)
    browser.find_element(By.CSS_SELECTOR, '.form-group > [name="tarea"]').send_keys(task_description)
    if checkbox:
        checkbox = browser.find_element(By.CSS_SELECTOR, '[for="check"] + [type="checkbox"]')
        ac.move_to_element(checkbox)
        ac.click(checkbox)
        ac.perform() 
    browser.find_element(By.CSS_SELECTOR, '#todo-submit').click()

#* Doing 1
url = 'https://selenium.dunossauro.live/exercicio_10.html'
b = Chrome()
b.get(url)
b.maximize_window()

# Settings WebDriverWair
wdw = WebDriverWait(b, 10)

# Setting ActionChains
ac = ActionChains(b)

#* Doing 2
fill_form(b, 'Do exercise', 'Exercise number 10', checkbox=True)

#* Doing 3
locator = (By.CSS_SELECTOR, '#todo button[class*="do"]')
wdw.until(text_to_be_present_in_element(locator, 'Fazer'), 'Button "Fazer" not found')
b.find_element(By.CSS_SELECTOR, '#todo button[class*="do"]').click()

#* Doing 4
locator = (By.CSS_SELECTOR, '#doing button[class*="do"]')
wdw.until(text_to_be_present_in_element(locator, 'Pronto'), 'Button "Pronto" not found')
b.find_element(By.CSS_SELECTOR, '#doing button[class*="do"]').click()

#* Doing 5
locator = (By.CSS_SELECTOR, '#done button[class*="do"]')
wdw.until(text_to_be_present_in_element(locator, 'Refazer'), 'Button "Refazer" not found')
b.find_element(By.CSS_SELECTOR, '#done button[class*="do"]').click()

print('Finished')