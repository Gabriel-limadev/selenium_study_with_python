from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    new_window_is_opened,
    number_of_windows_to_be # Check if window number is different
)

# Setting page
url = 'https://selenium.dunossauro.live/aula_11_b.html'
b = Chrome()
b.get(url)
b.maximize_window()

# Setting WebDriverWait
wdw = WebDriverWait(b, 60)

btn = b.find_element(By.CSS_SELECTOR, '#popupd')
print(btn.text)
btn.click()

wdw.until(
    new_window_is_opened(b.window_handles),
    'Windon not found!'
)
wdw.until(
    number_of_windows_to_be(2)
)
print('Open the new Window')