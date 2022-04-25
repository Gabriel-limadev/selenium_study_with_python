from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

url = 'https://selenium.dunossauro.live/aula_11_b.html'
b = Chrome()
b.get(url)
b.maximize_window()

def find_window(url: str):
    """Find the window with url text

    Args:
        url (str): url text for be found in our window
    """
    wids = b.window_handles
    for window in wids:
        b.switch_to.window(window)
        if url in b.current_url:
            print('Url found!')
            break
    else:
        print('Url not found!')

find_window('buscafe')