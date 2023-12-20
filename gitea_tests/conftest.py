import pytest
import requests
from requests.adapters import HTTPAdapter
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib3 import Retry

pytest_plugins = ["docker_compose"]


# @pytest.fixture
# def wait_gitea_up(function_scoped_container_getter):
#     request_session = requests.Session()
#     retries = Retry(total=5,
#                     backoff_factor=0.1,
#                     status_forcelist=[500, 502, 503, 504])
#     request_session.mount('http://', HTTPAdapter(max_retries=retries))
#
#     service = function_scoped_container_getter.get("gitea").network_info[0]
#     api_url = "http://%s:%s/" % (service.hostname, service.host_port)
#     assert request_session.get(api_url)
#     return request_session, api_url


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
    browser.config.base_url = "https://demoqa.com/"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
