import os
import shutil

import pytest
from selene import browser
from selenium.webdriver.chrome.options import Options
from gitea_tests.test_data import *
from helpers.helpers import is_responsive, del_readonly
from helpers.attach import *


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='120.0'
    )
    parser.addoption(
        '--base_url',
        default='http://localhost:3000'
    )


@allure.step('Set browser')
@pytest.fixture(scope='session', autouse=True)
def set_browser(request):
    browser_version = request.config.getoption('--browser_version')
    base_url = request.config.getoption('--base_url')
    options = Options()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
    }
    options.capabilities.update(capabilities)
    browser.config.driver_options = options
    browser.config.base_url = base_url
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@allure.step('Close browser')
@pytest.fixture(scope='function', autouse=True)
def close_browser():
    yield

    add_html(browser)
    add_screenshot(browser)
    add_logs(browser)
    browser.quit()


@pytest.fixture(scope='session', autouse=True)
def docker_compose_file(pytestconfig):
    return os.path.join(os.path.dirname(os.path.abspath("docker-compose.yml")), "docker-compose.yml")


@allure.step('Wait gitea container running')
@pytest.fixture(scope='session')
def wait_gitea_running(docker_ip, docker_services, request):
    base_url = request.config.getoption('--base_url')
    docker_services.wait_until_responsive(
        timeout=50.0, pause=0.1, check=lambda: is_responsive(base_url)
    )


@pytest.fixture(scope='session', autouse=True)
def confirm_gitea_settings(wait_gitea_running, set_browser):
    install_page.open_page().click_install_button()


@allure.step('Wait gitea with settings running')
@pytest.fixture(scope='session', autouse=True)
def wait_gitea_loading_with_add_settings(confirm_gitea_settings, docker_ip, docker_services, request):
    base_url = request.config.getoption('--base_url')
    url = base_url + sign_in.url
    docker_services.wait_until_responsive(
        timeout=50.0, pause=0.1, check=lambda: is_responsive(url)
    )


@pytest.fixture(scope='function')
def get_signed_in():
    sign_in.sign_in(user.name, user.password)


@allure.step('Docker compose down')
@pytest.fixture(scope='session', autouse=True)
def docker_cleanup():
    return ' down -v --rmi all'


@allure.step('Delete gitea directory after tests')
@pytest.fixture(scope='session', autouse=True)
def delete_gitea_dir():
    yield

    shutil.rmtree('gitea', onerror=del_readonly)
