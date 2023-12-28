import allure
from selene import browser, command
from selene.support.shared.jquery_style import s, ss


class RepoPage:
    def __init__(self):
        self.url = '/repo/create'
        self.repo_name = s('#repo_name')
        self.confirm_create_button = s('.field .button')
        self.repo_title_user = ss('.repo-title a')[0]
        self.repo_title_name = ss('.repo-title a')[1]
        self.new_file = ss('.repo-button-row .button')[0]
        self.file_name = s('#file-name')
        self.file_edit_body = s('#edit_area')
        self.commit_button = s('#commit-button')
        self.file_body = s('.code-inner')

    @allure.step('Open create repo page')
    def open_create_repo(self):
        browser.open(self.url)
        return self

    @allure.step('Fill in repo name')
    def fill_repo_name(self, name):
        self.repo_name.type(name)
        return self

    @allure.step('Confirm new repo creation')
    def confirm_create_repo(self):
        self.confirm_create_button.click()

    @allure.step('Create new file in repo')
    def create_new_file(self):
        self.new_file.click()
        return self

    @allure.step('Fill in file name')
    def fill_file_name(self, name):
        self.file_name.type(name)
        return self

    @allure.step('Fill in file body')
    def fill_file_body(self, body):
        self.file_edit_body.perform(command.js.set_value(body))
        return self

    @allure.step('Commit new file')
    def commit_changes(self):
        self.commit_button.click()
