
# TODO: 1 - open the page
# TODO: 2 - fill the form
# TODO: 3 - wait for area "Do exercise"
# TODO: 4 - wait for area "Do exercise"
# TODO: 5 - wait for area "Do exercise"

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from functools import partial

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
    
def wait_element(element, browser):
    if browser.find_element(By.CSS_SELECTOR, element):
        return True
    return False

def advance_button():
    b.find_element(By.CSS_SELECTOR, '.buttons > .btn-primary').click()

# * doing 1
url = 'https://selenium.dunossauro.live/exercicio_10.html'
b = Chrome()
b.get(url)
b.maximize_window()

# Setting ActionChains 
ac = ActionChains(b)

# Creating partials
wait_todo = partial(wait_element, '#todo .buttons')
wait_doing = partial(wait_element, '#doing .buttons')
wait_done = partial(wait_element, '#done .buttons')


# Setting WebDriverWait 
wdw = WebDriverWait(b, 15)

# * doing 2
fill_form(b, 'Do exercise', 'Exercise number 10', checkbox=True)

# * doing 3
wdw.until(wait_todo, 'Area "A fazer" not found!')
advance_button()

# * doing 4
wdw.until(wait_doing, 'Area "Fazendo" not found!')
advance_button()

# * doing 5
wdw.until(wait_done, 'Area "Feito" not found!')
print('Task completed')