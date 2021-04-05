import pytest
from time import sleep
import yaml


def occm_url_params():
    config_file_path = r'C:\Users\lshahar\PycharmProjects\seleniumProject1\test_occm_service\myConfigFile.yaml'
    with open(config_file_path, 'r') as file:
        url_parammeters = yaml.load(file, Loader=yaml.FullLoader)
        return url_parammeters


occm_url = occm_url_params()['occm_url']
services_urls = occm_url_params()['services_urls']


@pytest.mark.usefixtures("setup")
class TestClass:
    """This  function tests a valid login to OCCM and varifies correct navigation to OCCM's main page"""

    def test_login(self, username_param, password_param):
        self.driver.get(occm_url)
        sleep(7)
        login_input_element = self.driver.find_element_by_css_selector("[type=email]")
        login_input_element.send_keys(username_param)
        password_input_element = self.driver.find_element_by_css_selector("[type=password]")
        password_input_element.send_keys(password_param)
        login_button = self.driver.find_element_by_css_selector("[type=submit]")
        login_button.click()
        sleep(5)
        occm_header = self.driver.find_element_by_css_selector(".MainHeader_main-link__3Kle5")
        assert occm_header.text == "Cloud Manager"

    """This function tests navigation to each of the available services that appear on the left side bar. """

    @pytest.mark.parametrize("service_name,expected_url", services_urls)
    def test_switch_to_service(self, service_name, expected_url):
        iframe = self.driver.find_element_by_css_selector("#portal-widget-frame-container>iframe")
        self.driver.switch_to.frame(iframe)
        services_button_closed_menu = service_list_items = self.driver.find_element_by_css_selector(
            "#portal-widget-root > div > div.portal-widget-button > button")
        services_button_closed_menu.click()
        service_list_items = self.driver.find_elements_by_css_selector(".service-selector>a")
        for service_item in service_list_items:
            if service_item.text == service_name:
                service_item.click()
                sleep(8)
                assert expected_url in self.driver.current_url
                self.driver.get("https://staging.cloudmanager.netapp.com/working-environments?view=clouds")
                sleep(10)
                break
