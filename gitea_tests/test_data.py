from models.users import test_user
from pages.head_navigation import HeadNavigation
from pages.registration import RegistrationPage
from pages.sign_in import SignInPage
from pages.installation import InstallPage
from pages.repo_page import RepoPage
from pages.start_html_page import *


head_navigation = HeadNavigation()
registration = RegistrationPage()
sign_in = SignInPage()
install_page = InstallPage()
repo_page = RepoPage()
html = StartHtml()
right_menu = RightMenu()
left_menu = LeftMenu()

user = test_user
success_message = "Учётная запись успешно создана. Добро пожаловать!"
repo_name = "first_repo"
file_name = "first_file"
file_text = "Have a happy New Year!"
