from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

url = 'http://selenium.dunossauro.live/aula_04_a.html'
browser = Chrome()
browser.get(url)

sleep(3)

# Searching all 'uls'
ul = browser.find_elements(by=By.TAG_NAME, value='ul')
# Searching content 'li' from the first 'ul'
lis = ul[0].find_elements(by=By.TAG_NAME, value='li')
# Searching content 'a' of the first 'li'
a = lis[0].find_element(by=By.TAG_NAME, value='a')
# Printing content of 'a'
print(a.text)


# DOM hierarchy for understanding
"""
ul 
    li
        a
            text
    li
        a
            text
...

"""