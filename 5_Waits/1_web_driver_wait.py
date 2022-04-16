from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait

"""
wdw = WebDriverWait(
    driver,  # *WebDriver
    timeout, # *Tempo de espera até o erro
    poll_frequency=0.5,     # *Tempo entre uma tentativa e outra
    ignored_exceptions=None # *Lista de coisas que vamos ignorar
)
"""

b = Chrome() 
wdw = WebDriverWait(driver, 10) # segundos

"""
UNTIL = Executa até que o Callable seja True, ou até estourar o timeout de wdw
wdw.until(
    Callable, # *Operação que vai ser executada
    message   # *Mensagem caso o erro ocorra
)

UNTIL NOT = Executa até que o Callable seja False, ou até estourar o timeout de wdw
wdw.until_not(
    Callable, # *Operação que vai ser executada
    message   # *Mensagem caso o erro ocorra
)
"""


