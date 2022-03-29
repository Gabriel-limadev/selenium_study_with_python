"""
TODO: 1. Take all main links -> {'main text: 'main link'}
TODO: 2. Navigate to start link -> find the url of start and go there
TODO: 3. Take all links of page 1 and Click on the wrong answer to go to the next page
TODO: 4. Take all links of page 2 and click on the answer that is the same as the page title
TODO: 5. Take all links of page 3 and click on the answer that is the same as the path of the url
TODO: 6. Reload the page
TODO: 7. Go to course page
"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
from time import sleep
from pprint import pprint

url = 'https://selenium.dunossauro.live/exercicio_03.html'
browser = Chrome()
browser.get(url)

sleep(3)


# UTILS
def get_links(browser, element):
    """ Take all links inside an element

    Args:
        browser (object): browser instance
        element (str): webelement ['aside', 'main', 'body']
    """
    result = {}
    element = browser.find_element(by=By.TAG_NAME, value=element)
    links = element.find_elements(by=By.TAG_NAME, value='a')
    for link in links:
        result.update({link.text : link.get_attribute('href')})
    return result

# ------------START PAGE ------------
# PART 1 and 2 
start = get_links(browser, 'main')
browser.get(start['Começar por aqui'])

# ------------PAGE 1 ------------
# PART 3 
sleep(2)
links_page_1 = browser.find_elements(by=By.TAG_NAME, value='a')
wrong_link = [link for link in links_page_1 if link.get_attribute('attr') == 'errado']
wrong_link[0].click()

sleep(15)
# ------------PAGE 2 ------------
# PART 4
links_page_2 = browser.find_elements(by=By.TAG_NAME, value='a')
# -- I got it by not doing it the same way as part 3 just to practice another logic
right_link = [link for link in links_page_2 if link.text == browser.title]
right_link[0].click()

sleep(3)

# ------------PAGE 3 ------------
# PART 5
links_page_3 = browser.find_elements(by=By.TAG_NAME, value='a')
right_link = [link for link in links_page_3 if link.text in urlparse(browser.current_url).path]
right_link[0].click()

sleep(3)

# ------------PAGE 4 ------------
# PART 6
course = get_links(browser, 'header')
browser.refresh()
sleep(3)

# PART 7 
browser.get(course['Curso'])