import pytest
from appium import webdriver

from pathlib import Path


@pytest.fixture(scope="function")
def driver(request):
    """Runs before and after each test. Sets up and quits driver"""
    dc = {}
    driver = None

    # This is the Application and ‘app’ desired capability to specify a path to Appium
    path_to_current_directory = Path().absolute()
    dc['app'] = str(path_to_current_directory) + '/app/app-debug.apk'
    # appPackage and appActivity desired capability specify app details to Appium
    dc['appPackage'] = ''
    # dc['appActivity'] = ".MainActivity"
    # platformName desired capability specify platform detail to Appium
    dc['platformName'] = 'Android'
    # deviceName desired capability specify the device id detail to Appium
    # device id is got from running adb devices command in PC
    # dc['deviceName'] = device_name
    # accept alerts and grant permissions
    dc['autoAcceptAlerts'] = 'true'
    dc['autoGrantPermissions'] = 'true'
    # Creating the Driver by passing Desired Capabilities
    driver = webdriver.Remote('http://localhost:4723/wd/hub', dc)

    yield driver

    print("\nquit driver..")
    driver.quit()
