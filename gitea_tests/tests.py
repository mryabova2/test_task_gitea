from selene import browser, be, have, command
from selene.support.shared.jquery_style import s, ss
from gitea_tests.test_data import *


def test_sign_up_new_user():
    browser.open('/user/login')
    ss(".navbar-right .item")[0].click()
    s("#user_name").type(user_name)
    s("#email").type(user_mail)
    s("#password").type(user_password)
    s("#retype").type(user_password)
    s(".field .button").click()
    assert s(".flash-success").should(be.visible)
    assert s(".flash-success").should(have.text(success_message))
    assert s(".truncated-item-name").should(have.text(user_name))


def test_create_repo():
    browser.open('/repo/create')
    s("#repo_name").should(be.visible).type(repo_name)
    s('.field .button').click()
    assert ss(".repo-title a")[0].should(have.text(user_name))
    assert ss(".repo-title a")[1].should(have.text(repo_name))
    s(f"[href='/{user_name}/{repo_name}/_new/main/']").click()
    s('#file-name').type(file_name)
    s('#edit_area').perform(command.js.set_value(file_text))
    s('#commit-button').click()
    assert s('.code-inner').should(have.text(file_text))

