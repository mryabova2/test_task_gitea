import allure
from selene.support.shared.jquery_style import ss


class HeadNavigation:

    def __init__(self):
        self.registration_button = ss(".navbar-right .item")[0]

    @allure.step('Go to registration page')
    def go_to_registration(self):
        self.registration_button.click()
        return self
