import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome("C:\\Users\\lshahar\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    sleep(20)
    driver.close()
