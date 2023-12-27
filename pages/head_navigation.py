from selene import by, browser
from selene.support.shared.jquery_style import s, ss


class HeadNavigation:

    def __init__(self):
        self.registration_button = ss(".navbar-right .item")[0]

    def go_to_registration(self):
        self.registration_button.click()
        return self
