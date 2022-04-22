from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

url = 'https://selenium.dunossauro.live/aula_11_a.html'
b = Chrome()
b.get(url)
b.maximize_window()

# Settings Alerts
alert = Alert(b)

def fill_alerts(name):
    b.find_element(By.CSS_SELECTOR, '#all').click()
    alert.accept()
    alert.send_keys(name)
    [alert.accept() for i in range(2)]
        
fill_alerts('Example')
fill_alerts('Example 2')
