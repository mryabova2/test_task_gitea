from selene import browser, have
from gitea_tests.test_data import *


def test_check_html(wait_gitea_loading_with_add_settings):
    right_menu = right_menu_html.find_right()
    left_menu = left_menu_html.find_left()

    assert html.get_title_text() == html.title_text
    assert button_text(left_menu, left_menu_html.explore_button_index) == left_menu_html.explore_text
    assert button_text(left_menu, left_menu_html.help_button_index) == left_menu_html.help_text
    assert button_text(right_menu, right_menu_html.register_button_index) == right_menu_html.register_text
    assert button_text(right_menu, right_menu_html.sign_in_button_index) == right_menu_html.sign_in_text


def test_sign_up_new_user():
    browser.open('/')
    head_navigation.go_to_registration()
    registration \
        .type_user_name(user.name) \
        .type_email(user.email) \
        .type_password(user.password) \
        .retype_password(user.password)

    registration.click_reg_button()

    assert registration.success_message.should(have.text(registration.success_message_text))
    assert registration.user_registered.should(have.text(user.name))


def test_create_repo(get_signed_in):
    repo_page \
        .open_create_repo() \
        .fill_repo_name(repo_name) \
        .confirm_create_repo()

    repo_page \
        .create_new_file() \
        .fill_file_name(file_name) \
        .fill_file_body(file_text) \
        .commit_changes()

    assert repo_page.repo_title_user.should(have.text(user.name))
    assert repo_page.repo_title_name.should(have.text(repo_name))
    assert repo_page.file_body.should(have.text(file_text))
