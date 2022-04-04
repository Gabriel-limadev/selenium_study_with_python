from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = ''
browser = Chrome()
browser.get(url)

# ?CSS SELECTORS - COMBINADORES

#* IRMÃOS ADJACENTES (A + B)
# A partir do elemento selecionado A procure o elemento B
# Procura BR no mesmo nivel de DIV (não dentro de div)
browser.find_elements(By.CSS_SELECTOR, 'div + br')

# Procura a primeira div no mesmo nivel de h2
browser.find_element(By.CSS_SELECTOR, 'h2 + div')

# *GERAL DE IRMÃOS ou Geral adjacente (A ~ B)
# Procura todas as tags divs no mesmo nivel de h2
browser.find_elements(By.CSS_SELECTOR, 'h2 ~ div')

# *FILHOS (A > B)
# Procura todas as tags brs filhas de div
browser.find_elements(By.CSS_SELECTOR, 'div > br')

# *DESCENDENTES (A  B)
# Procura todas as tags brs filhas diretas ou indiretamente de form
browser.find_elements(By.CSS_SELECTOR, 'form br')
