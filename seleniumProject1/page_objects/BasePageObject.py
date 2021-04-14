from selenium import webdriver
import yaml


class BasePageObject:

    _driver = None
    _services_urls = None

    @classmethod
    def get_params(cls):
        config_file_path = r'C:\Users\lshahar\PycharmProjects\seleniumProject1\test_occm_service\myConfigFile.yaml'
        with open(config_file_path, 'r') as file:
            parammeters = yaml.load(file, Loader=yaml.FullLoader)
            return parammeters['cloud_central_menu_items']






