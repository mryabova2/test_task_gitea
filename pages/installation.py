import allure
from selene import by, browser
from selene.support.shared.jquery_style import s


class InstallPage:

    def __init__(self):
        self.url = '/'
        self.button = s(by.text('Установить Gitea'))

    @allure.step('Open settings page')
    def open_page(self):
        browser.open(self.url)
        return self

    @allure.step('Confirm settings')
    def click_install_button(self):
        self.button.click()
