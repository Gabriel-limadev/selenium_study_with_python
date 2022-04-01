from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep
from pprint import pprint

url = 'https://selenium.dunossauro.live/aula_05_c.html'
browser = Chrome()
browser.get(url)
sleep(3)
    
# Find by NAME and writing my responses in forms
def best_movie(browser, movie, email, phone):
    """ Fill in the form with the best movie

    Args:
        browser (intancie): _description_
        movie (str): the best movie
        email (str): the user email 
        phone (str): the user phone
    """
    browser.find_element(by=By.NAME, value='filme').send_keys(movie)
    browser.find_element(by=By.NAME, value='email').send_keys(email)
    browser.find_element(by=By.NAME, value='telefone').send_keys(phone)
    browser.find_element(by=By.NAME, value='enviar').click()

best_movie(browser, 'The Batman', 'gabriel.lima@gmail.com', '(11)95946-1782')

# browser.quit()