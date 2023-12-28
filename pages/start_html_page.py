import requests
from bs4 import BeautifulSoup


def parse_page(page):
    page = requests.get(page)
    parsed_page = BeautifulSoup(page.text, 'html.parser')
    return parsed_page


def button_text(menu, button_index):
    text = menu.contents[button_index].text.strip()
    return text


class StartHtml:
    def __init__(self):
        self.url = 'http://localhost:3000'
        self.title_text = 'Gitea: Git with a cup of tea'
        self.head_menu_tag = 'div'

    def get_title_text(self):
        text = parse_page(self.url).title.string
        return text

    # def get_menu(self, locator_menu):
    #     menu = parse_page(self.url).find(self.head_menu_tag, locator_menu)
    #     return menu


class LeftMenu(StartHtml):
    def __init__(self):
        super().__init__()
        self.left_locator = {'class': 'navbar-left'}
        self.explore_button_index = 5
        self.help_button_index = 7
        self.explore_button_text = 'Explore'
        self.help_button_text = 'Help'

    def find_left(self):
        left_menu = parse_page(self.url).find(self.head_menu_tag, attrs=self.left_locator)
        return left_menu


class RightMenu(StartHtml):
    def __init__(self):
        super().__init__()
        self.right_locator = {'class': 'navbar-right'}
        self.register_button_index = 1
        self.sign_in_button_index = 3
        self.register_button_text = 'Register'
        self.sign_in_button_text = 'Sign In'

    def find_right(self):
        right_menu = parse_page(self.url).find(self.head_menu_tag, attrs=self.right_locator)
        return right_menu
