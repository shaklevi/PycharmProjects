# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import yaml


def write_config_file():
    config_file_path = r'C:\Users\lshahar\PycharmProjects\seleniumProject1\test_occm_service\myConfigFile.yaml'
    config_data = {'occm_url': 'https://staging.cloudmanager.netapp.com/#!/',
                   'services_urls': [
                       ("Cloud Volumes Service", "https://cloud.netapp.com/cloud-volumes-service-for-aws"),
                       ("Cloud Insights", "https://gateway.main-ci.cloudinsights-qa.netapp.com/"),
                       ("Cloud Sync", "https://staging.cloudmanager.netapp.com/sync"),
                       ("SaaS Backup", "https://saasbackup.netapp.com/login"),
                       ("Cloud Tiering", "https://staging.cloudmanager.netapp.com/tiering"),
                       ("Cloud Backup Service", "https://cloud-netapp-com.sandbox.hs-sites.com/cloud-backup-service")]}

    with open(config_file_path, 'w') as file:
        documents = yaml.dump(config_data, file, default_flow_style=False)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    write_config_file()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
