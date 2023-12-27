from selene import by, browser
from selene.support.shared.jquery_style import s


class RegistrationPage:

    def __init__(self):
        self.user_name = s('#user_name')
        self.email = s('#email')
        self.password = s('#password')
        self.retype_password = s('#retype')
        self.confirm_button = s('.field .button')
        self.success_message = s('.flash-success')
        self.user_registered = s('.truncated-item-name')

    def type_user_name(self, name):
        self.user_name.type(name)

    def type_email(self, email):
        self.email.type(email)

    def type_password(self, password):
        self.password.type(password)

    def retype_password(self, password):
        self.retype_password.type(password)

    def click_confirm_button(self):
        self.confirm_button.click()
