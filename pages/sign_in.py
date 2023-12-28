from selene import browser
from selene.support.shared.jquery_style import s


class SignInPage:

    def __init__(self):
        self.url = '/user/login'
        self.name = s('#user_name')
        self.password = s('#password')
        self.confirm = s('.field .button')

    def sign_in(self, name, password):
        browser.open(self.url)
        self.name.type(name)
        self.password.type(password)
        self.confirm.click()
