from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
# Usando ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Configurando a página
url = 'https://selenium.dunossauro.live/aula_08_a'
b = Chrome()
b.get(url)
b.maximize_window()

text = 'Gabriel'
# Hi-level
element = b.find_element(By.NAME, 'texto')
# text.send_keys(text)

# Low-level
# Configurando ActionChains 
ac = ActionChains(b)
ac.move_to_element(element)
ac.click(element)

def digita_com(key):
    for l in text:
        ac.key_down(key)
        ac.key_down(l)
        ac.key_up(l)
        ac.key_up(key)

digita_com(Keys.SHIFT)
digita_com((Keys.UP))
# perform é o executador de tudo que envolve actionChains
ac.perform() 