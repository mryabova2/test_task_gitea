import allure
from selene.support.shared.jquery_style import s


class RegistrationPage:

    def __init__(self):
        self.user_name = s('#user_name')
        self.email = s('#email')
        self.password = s('#password')
        self.password_again = s('#retype')
        self.confirm_button = s('.field .button')
        self.success_message = s('.flash-success')
        self.user_registered = s('.truncated-item-name')
        self.success_message_text = 'Учётная запись успешно создана. Добро пожаловать!'

    @allure.step('Fill in user name')
    def type_user_name(self, name):
        self.user_name.type(name)
        return self

    @allure.step('Fill in user email')
    def type_email(self, email):
        self.email.type(email)
        return self

    @allure.step('Fill in password')
    def type_password(self, password):
        self.password.type(password)
        return self

    @allure.step('Retype password')
    def retype_password(self, password):
        self.password_again.type(password)
        return self

    @allure.step('Confirm registration')
    def click_reg_button(self):
        self.confirm_button.click()
        return self
