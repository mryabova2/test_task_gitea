import os
import stat

import requests
from requests.exceptions import ConnectionError


def is_responsive(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except ConnectionError:
        return False


def del_readonly(func, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)
