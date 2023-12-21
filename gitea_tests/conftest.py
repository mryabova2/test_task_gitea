import os
from time import sleep

import pytest
import requests
from selene import browser, by
from selenium.webdriver.chrome.options import Options
from selene.support.shared.jquery_style import s, ss
from requests.exceptions import ConnectionError


def is_responsive(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False


# @pytest.fixture(scope="session")
# def docker_compose_command():
#     return "docker compose --force-recreate"

@pytest.fixture(scope="session")
def docker_setup():
    return "up --build -d --force-recreate"


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join("C:\\Users\\m.ryabova\\PycharmProjects\\test_task_gitea", "docker-compose.yml")
    # return os.path.join(str(pytestconfig.rootpath), "test_task_gitea\\", "docker-compose.yml")


@pytest.fixture()
def set_browser():
    browser_version = "120.0"
    options = Options()
    capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        # "selenoid:options": {
        #     "enableVNC": True,
        #     "enableVideo": True
        # }
    }
    options.capabilities.update(capabilities)
    browser.config.driver_options = options
    browser.config.base_url = "http://localhost:3000"
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture(scope="session")
def wait_gitea_running(docker_ip, docker_services):
    url = "http://{}:{}".format(docker_ip, 3000)
    docker_services.wait_until_responsive(
        timeout=50.0, pause=0.1, check=lambda: is_responsive(url)
    )


@pytest.fixture()
def confirm_gitea_settings(wait_gitea_running, set_browser):
    browser.open("/")
    # sleep(500)
    browser.element(by.text("Установить Gitea")).click()
