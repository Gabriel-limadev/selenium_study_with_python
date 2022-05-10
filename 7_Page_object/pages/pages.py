from page_objects import Page
from .elements import Do, Doing, Done, Todo

class PageTodo(Page):
    do = Do()
    doing = Doing()
    done = Done()
    todo = Todo()