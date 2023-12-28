import os
import shutil

import pytest
import requests
from bs4 import BeautifulSoup
from selene import browser
from selenium.webdriver.chrome.options import Options
from gitea_tests.test_data import *
from helpers.helpers import is_responsive, del_readonly


@pytest.fixture(scope='session', autouse=True)
def set_browser():
    browser_version = "120.0"
    options = Options()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
    }
    options.capabilities.update(capabilities)
    browser.config.driver_options = options
    browser.config.base_url = "http://localhost:3000"
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope='function', autouse=True)
def close_browser():
    yield
    browser.quit()


@pytest.fixture(scope='session', autouse=True)
def docker_compose_file(pytestconfig):
    print(os.path.abspath("docker-compose.yml"))
    return os.path.join(os.path.dirname(os.path.abspath("docker-compose.yml")), "docker-compose.yml")


@pytest.fixture(scope='session')
def wait_gitea_running(docker_ip, docker_services):
    url = f"http://{docker_ip}:{3000}"
    docker_services.wait_until_responsive(
        timeout=50.0, pause=0.1, check=lambda: is_responsive(url)
    )


@pytest.fixture(scope='session', autouse=True)
def confirm_gitea_settings(wait_gitea_running, set_browser):
    install_page.open_page().click_install_button()


@pytest.fixture(scope='session', autouse=True)
def wait_gitea_loading_with_add_settings(confirm_gitea_settings, docker_ip, docker_services):
    url = "http://{}:{}/user/login".format(docker_ip, 3000)
    docker_services.wait_until_responsive(
        timeout=50.0, pause=0.1, check=lambda: is_responsive(url)
    )

    # start_page1 = requests.get("http://localhost:3000")

    # soup = BeautifulSoup(start_page1.text, "html.parser")
    # left_nav_menu = soup.find('div', attrs={"class": "navbar-left"})
    # right_nav_menu = soup.find('div', attrs={"class": "navbar-right"})
    #
    # assert soup.title.string == 'Gitea: Git with a cup of tea'
    # assert soup.select('#navbar')
    # assert right_nav_menu.contents[1].text.strip() == "Register"
    # assert right_nav_menu.contents[3].text.strip() == "Sign In"
    # assert left_nav_menu.contents[5].text.strip() == "Explore"
    # assert left_nav_menu.contents[7].text.strip() == "Help"


@pytest.fixture(scope='function')
def get_signed_in():
    sign_in.sign_in(user.name, user_password)


@pytest.fixture(scope='session', autouse=True)
def docker_cleanup():
    return ' down -v --rmi all'


@pytest.fixture(scope='session', autouse=True)
def delete_gitea_dir():
    yield

    shutil.rmtree('gitea', onerror=del_readonly)
