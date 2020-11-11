import pytest
from appium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    """Runs before and after each test. Sets up and quits driver"""
    dc = {}
    driver = None

    # This is the Application and ‘app’ desired capability to specify a path to Appium
    dc['app'] = "C://app/app-debug.apk"
    # appPackage and appActivity desired capability specify app details to Appium
    dc['appPackage'] = "com.logitech.uefits"
    # dc['appActivity'] = ".MainActivity"
    # platformName desired capability specify platform detail to Appium
    dc['platformName'] = 'Android'
    # deviceName desired capability specify the device id detail to Appium
    # device id is got from running adb devices command in PC
    dc['deviceName'] = 'RF8N8376WMV'
    # accept alerts and grant permissions
    dc['autoAcceptAlerts'] = 'true'
    dc['autoGrantPermissions'] = 'true'
    # Creating the Driver by passing Desired Capabilities
    driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)

    yield driver

    print("\nquit driver..")
    driver.quit()
