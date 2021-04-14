from seleniumProject1.page_objects.BasePageObject import BasePageObject
import pytest
from time import sleep


class Pytest:
    pass


@pytest.mark.usefixtures("setup")
class CloudBackupServicePage(BasePageObject):
    _driver = None

    def __init__(self, web_driver):
        self._driver = web_driver

    def test_main_title(self):
        title = self._driver.find_element_by_css_selector('.product-name + h2>span')
        assert title.text == 'Fully Integrated Cloud Backup and Restore Service'

    def test_cloud_backup_logo(self):
        self._driver.find_element_by_css_selector('.product-name>span>img')

    def test_number_of_cloud_central_menu_items(self):
        menu_items = self._driver.find_elements_by_css_selector('.has-child-menu')
        assert len(menu_items) == 6

    def test_menu_items_names(self, cloud_central_menu_items_names):
        menu_items = self._driver.find_elements_by_css_selector('.has-child-menu')
        menu_items_texts = [item.text for item in menu_items]
        for menu_item_name in cloud_central_menu_items_names:
            assert menu_item_name in menu_items_texts
