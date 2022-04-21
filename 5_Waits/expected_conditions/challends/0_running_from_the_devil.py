"""
TODO: 1 - Open the page
TODO: 2 - Start the exercise
TODO: 3 - Answering first question
TODO: 4 - Find Correct Title
TODO: 5 - Response last question
TODO: 6 - Find the unicorn
"""

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
    url_contains,
    title_is,
    text_to_be_present_in_element
)

#* Doing 1
url = 'https://selenium.dunossauro.live/exercicio_03.html'
b = Chrome()
b.get(url)
b.maximize_window()

# Settings WebDriverWair
wdw = WebDriverWait(b, 30)

#*Doing 2
locator_start = (By.CSS_SELECTOR, '#main a[href="page_1.html"]')
wdw.until(
    presence_of_element_located(locator_start),
    'Link for start not found!'
)
b.find_element(By.CSS_SELECTOR, '#main a[href="page_1.html"]').click()

#* Doing 3
wdw.until(
    url_contains('page_1.html'),
    'Page 1 has not yet opened'
)

b.find_element(By.CSS_SELECTOR, '#main a[href="page_2.html"]').click()

#* Doing 4
locator_page2 = (By.CSS_SELECTOR, '#main h1')
wdw.until(
    text_to_be_present_in_element(locator_page2, 'página 2'), 
    'Page 2 has not yet opened'
)
title = b.find_element(By.CSS_SELECTOR, '#main a[attr="certo"]')
wdw.until(
    title_is(title.text),
    f'{title} is not page title'
)
title.click()

#* Doing 5
locator_page2 = (By.CSS_SELECTOR, '#main h1')
wdw.until(
    text_to_be_present_in_element(locator_page2, 'página 3'), 
    'Page 3 has not yet opened'
)

final_url = b.find_element(By.CSS_SELECTOR, '#main a[href="page_4.html"]')
wdw.until(
    url_contains(final_url.text)
)
final_url.click()

#* Doing 6
locator_last_page = (By.CSS_SELECTOR, '#main p')
locator_last_page_unicorn = (By.CSS_SELECTOR, '#main pre')
wdw.until(
    text_to_be_present_in_element(locator_last_page, 'diabão')
)
b.refresh()
wdw.until(
    text_to_be_present_in_element(locator_last_page_unicorn, 'unicórnio')
)
print('Game finished')