from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/aula_03.html'

# Opening Chrome
browser = Chrome()
# Finding url
browser.get(url)

# Awaiting five seconds to continue the code
sleep(5)

# Finding p
a = browser.find_element_by_tag_name("a")

# Clicking 10 times and always getting the last text of element p
for click in range(10):
    ps = browser.find_elements_by_tag_name("p")
    a.click()
    print(f'Value of P: {ps[-1].text}')
    print(f'Value of click: {click}') 

    print(f'Os valores são iguais: {int(ps[-1].text) == click}')


browser.quit()