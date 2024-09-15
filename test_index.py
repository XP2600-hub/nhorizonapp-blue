# test_index.py

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os

def run_test():
    # BrowserStack credentials
    username = os.getenv('BROWSERSTACK_USERNAME')
    access_key = os.getenv('BROWSERSTACK_ACCESS_KEY')

    # Desired capabilities
    capabilities = {
        'browserstack.user': 'xp_wQRfve',
        'browserstack.key': 'Jxn4E9RzqwXjNVLyxkok',
        'browser': 'Chrome',
        'os': 'Windows',
        'os_version': '10',
        'name': 'Index HTML Test'
    }

    # Create WebDriver instance
    driver = webdriver.Remote(
        command_executor='https://hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=capabilities
    )

    # Load the HTML file from GitHub
    driver.get('https://raw.githubusercontent.com/XP2600-hub/nhorizonapp-blue/main/index.html')
    print("Title: ", driver.title)

    driver.quit()

if __name__ == "__main__":
    run_test()
