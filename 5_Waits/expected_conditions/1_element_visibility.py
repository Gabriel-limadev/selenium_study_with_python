from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    visibility_of, # Checks if the element is visible
    invisibility_of_element, # Checks if the element is invisible
    visibility_of_element_located, # using locator
    invisibility_of_element_located, # using locator
    visibility_of_any_elements_located, # Checks if any passed element is visible
    visibility_of_all_elements_located # Checks if all elements that were passed are visible
)

url = 'https://selenium.dunossauro.live/aula_10_b.html'
b = Chrome()
b.get(url)
wdw = WebDriverWait(b, 30)

# *------ USING SIMPLE ELEMENT --------
# element = b.find_element(By.TAG_NAME, 'h1')

# wdw.until(
#     visibility_of(element), "Element ins't visible in 30 seconds"
# )
# wdw.until_not(
#     invisibility_of_element(element), "Element ins't visible in 30 seconds"
# )
# print('h1 available')

# *------ USING LOCATOR --------
# element = (By.TAG_NAME, 'h1') # No matter call it locator or element
# wdw.until(
#     visibility_of_element_located(element), "Element ins't visible in 30 seconds"
# )
# wdw.until_not(
#     invisibility_of_element_located(element), "Element ins't visible in 30 seconds"
# )
# print('h1 available')

# *------ USING VISIBILITY ANY OR ALL --------
element = (By.TAG_NAME, 'h1') # No matter call it locator or element
wdw.until(
    visibility_of_any_elements_located(element), "Element ins't visible in 30 seconds"
)
wdw.until(
    visibility_of_all_elements_located(element), "Element ins't visible in 30 seconds"
)
