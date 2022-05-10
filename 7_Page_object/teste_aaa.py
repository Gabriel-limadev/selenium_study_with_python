from selenium.webdriver import Chrome
from pages.pages import PageTodo

browser = Chrome()
url = 'https://selenium.dunossauro.live/todo_list.html'

# Arrange ------------------------
page = PageTodo(browser, url)
page.open()

# Act     ------------------------
page.todo.create_todo(
    'comer', 
    'salada todos os dias', 
    urgent=True
)

# Assert  ------------------------
first_todo = page.do.todos[0]
assert first_todo.name == 'comer'
assert first_todo.description == 'salada todos os dias'