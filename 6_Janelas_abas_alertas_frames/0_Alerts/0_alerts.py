from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

url = 'https://selenium.dunossauro.live/aula_11_a.html'
b = Chrome()
b.get(url)
b.maximize_window()

b.find_element(By.CSS_SELECTOR, '#alert').click()

# Handles errors well -- Imports once and that's enough
alert = Alert(b) 

## no import, no error handling -- Use whenever alerting
# alert = b.switch_to.alert -> 

print(f'The alert is "{alert.text}"')
alert.accept()