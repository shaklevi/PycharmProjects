import pytest
from selenium import webdriver
#import yaml


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome("C:\\Users\\lshahar\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption('--username', action='store', help='Repository user')
    parser.addoption('--password', action='store', help='Repository password')


@pytest.fixture
def username_param(request):
    return request.config.getoption("--username")


@pytest.fixture
def password_param(request):
    return request.config.getoption("--password")
