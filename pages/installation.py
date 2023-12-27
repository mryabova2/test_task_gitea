from selene import by, browser
from selene.support.shared.jquery_style import s


class InstallPage:

    def __init__(self):
        self.url = '/'
        self.button = s(by.text('Установить Gitea'))

    def open_page(self):
        browser.open(self.url)
        return self

    def click_install_button(self):
        self.button.click()
