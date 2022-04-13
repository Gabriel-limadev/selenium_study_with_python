from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
# Usando ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Configurando a página
url = 'https://selenium.dunossauro.live/caixinha'
b = Chrome()
b.get(url)
b.maximize_window()

box = b.find_element(By.ID, 'caixa')
span = b.find_element(By.TAG_NAME, 'span')

ac = ActionChains(b)
def box_color(key1, key2=None):
    ac.key_down(key1)
    if key2:
        ac.key_down(key2)

    ac.pause(1)
    ac.move_to_element(box)
    ac.pause(1)
    ac.click()
    ac.pause(1)
    ac.double_click()
    ac.pause(1)
    ac.move_to_element(span)
    ac.key_up(key1)
    if key2:
        ac.key_up(key2)

box_color(Keys.SHIFT)
box_color(Keys.CONTROL)
box_color(Keys.SHIFT, Keys.CONTROL)
ac.context_click()
ac.pause(1)
ac.perform()