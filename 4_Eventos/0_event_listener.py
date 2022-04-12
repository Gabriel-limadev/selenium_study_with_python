from time import sleep
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
# Para utilizar EventListener use:
from selenium.webdriver.support.events import (
    EventFiringWebDriver,
    AbstractEventListener,
)

# Criando a classe que terá o EventListener
class Escuta(AbstractEventListener):
    def before_click(self, element, webdriver):
        if element.tag_name == 'input':
            print(webdriver.find_element(By.TAG_NAME, 'span').text)
        print(f'Before of click in {element.tag_name}')

    def after_click(self, element, webdriver):
        if element.tag_name == 'input':
            print(webdriver.find_element(By.TAG_NAME, 'span').text)
        print(f'After of click in {element.tag_name}')

# Configurando a página
url = 'https://selenium.dunossauro.live/aula_07_d'
b = Chrome()
b.get(url)

# Envelopando nosso eventListener com o EventFiring
new_browser = EventFiringWebDriver(b, Escuta())

# Pegando elementos
input_text = new_browser.find_element(By.TAG_NAME, 'input')
span = new_browser.find_element(By.TAG_NAME, 'span')
p = new_browser.find_element(By.TAG_NAME, 'p')

input_text.click()
print('I am clicking')