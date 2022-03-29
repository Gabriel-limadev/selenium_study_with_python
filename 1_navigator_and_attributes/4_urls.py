from selenium.webdriver import Chrome
from urllib.parse import urlparse

url = 'http://selenium.dunossauro.live/aula_04.html'
browser = Chrome()
browser.get(url)

# Testing urllib
url_teste = urlparse(browser.current_url)