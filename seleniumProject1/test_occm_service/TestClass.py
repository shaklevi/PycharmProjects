# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import pytest
from time import sleep

@pytest.mark.usefixtures("setup")
class TestClass:
    def test_login(self, username, password):
#         Send this url as parameter
        self.driver.get('https://staging.cloudmanager.netapp.com/#!/')
        sleep(7)
        login_input_element = self.driver.find_element_by_css_selector("[type=email]")
        login_input_element.send_keys(username)
        password_input_element = self.driver.find_element_by_css_selector("[type=password]")
        password_input_element.send_keys(password)
        login_button = self.driver.find_element_by_css_selector("[type=submit]")
        login_button.click()
        sleep(5)
        occm_header = self.driver.find_element_by_css_selector(".MainHeader_main-link__3Kle5")
        assert occm_header.text == "Cloud Manager"


    @pytest.mark.parametrize("service_name,expected_url",
                             [("Cloud Volumes Service","https://cloud.netapp.com/cloud-volumes-service-for-aws"),
                              ("Cloud Insights","https://gateway.main-ci.cloudinsights-qa.netapp.com/"),
                              ("Cloud Sync","https://staging.cloudmanager.netapp.com/sync"),
                              ("SaaS Backup","https://saasbackup.netapp.com/login"),
                              ("Cloud Tiering","https://staging.cloudmanager.netapp.com/tiering"),
                              ("Cloud Backup Service","https://cloud-netapp-com.sandbox.hs-sites.com/cloud-backup-service")])
    def test_switch_to_service(self, service_name, expected_url):
        iframe = self.driver.find_element_by_css_selector("#portal-widget-frame-container>iframe")
        self.driver.switch_to.frame(iframe)
        services_button_closed_menu = service_list_items = self.driver.find_element_by_css_selector("#portal-widget-root > div > div.portal-widget-button > button")
        services_button_closed_menu.click()
        service_list_items = self.driver.find_elements_by_css_selector(".service-selector>a")
        for service_item in service_list_items:
            if service_item.text == service_name:
                service_item.click()
                sleep(7)
                assert expected_url in self.driver.current_url
                self.driver.get("https://staging.cloudmanager.netapp.com/working-environments?view=clouds")
                sleep(10)
                break
