import pytest
from time import sleep
import yaml

from seleniumProject1.page_objects.CloudBackupServicePage import CloudBackupServicePage

@pytest.mark.usefixtures("setup")
class TestClassCloudBackupService:


    _page = None

    @pytest.fixture(scope="session")
    def tests_params(self):
        config_file_path = r'C:\Users\lshahar\PycharmProjects\seleniumProject1\test_occm_service\myConfigFile.yaml'
        with open(config_file_path, 'r') as file:
            url_parammeters = yaml.load(file, Loader=yaml.FullLoader)
            return url_parammeters

    @pytest.fixture(scope="module")
    def occm_url(self, tests_params):
        return tests_params['occm_url']

    @pytest.fixture(scope="module")
    def services_urls(self, tests_params):
        return tests_params['services_urls']

    @pytest.fixture(scope="class")
    def page(self, services_urls):
        self.driver.get(services_urls[5][1])
        return CloudBackupServicePage(self.driver)

    def test_main_title(self, page):
        page.test_main_title()

    def test_cloud_backup_title(self, page):
        page.test_cloud_backup_logo()

    def test_number_of_cloud_central_menu_items(self, page):
        page.test_number_of_cloud_central_menu_items()

    @pytest.fixture
    def cloud_central_menu_items_names(self, tests_params):
        return tests_params['cloud_central_menu_items']

    def test_menu_items_names(self, cloud_central_menu_items_names, page):
        page.test_menu_items_names(cloud_central_menu_items_names)
