import pytest
from appium.webdriver.common.touch_action import TouchAction

from .pages.pair_your_earbuds_page import PairYourEarbudsPage
from .pages.landing_page import LandingPage
from .pages.analytics_page import AnalyticsPage
from .pages.welcome_page import WelcomePage

import time


@pytest.mark.pair_earbuds_carousel
class TestPairYourEarbudsPage:
    def test_pair_your_earbuds_carousel_first_screen(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        landing_page = LandingPage(driver)
        pair_your_earbuds = PairYourEarbudsPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
        pair_your_earbuds.should_be_pye_page_title()
        pair_your_earbuds.should_be_correct_pye_page_subtitle1()
        pair_your_earbuds.should_be_instructions_image()
        pair_your_earbuds.should_be_open_bluetooth_button()
        pair_your_earbuds.should_be_open_bluetooth_button_text()

    def test_pair_your_earbuds_carousel_second_screen(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        landing_page = LandingPage(driver)
        pair_your_earbuds = PairYourEarbudsPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
        pair_your_earbuds.should_be_pye_page_title()
        TouchAction(driver).press(x=855, y=1215).move_to(x=268, y=1222).release().perform()
        pair_your_earbuds.should_be_pye_page_title()
        pair_your_earbuds.should_be_correct_pye_page_subtitle2()
        pair_your_earbuds.should_be_instructions_image()
        pair_your_earbuds.should_be_open_bluetooth_button()
        pair_your_earbuds.should_be_open_bluetooth_button_text()

    def test_pair_your_earbuds_carousel_third_screen(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        landing_page = LandingPage(driver)
        pair_your_earbuds = PairYourEarbudsPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
        pair_your_earbuds.should_be_pye_page_title()
        TouchAction(driver).press(x=855, y=1215).move_to(x=268, y=1222).release().perform()
        pair_your_earbuds.should_be_pye_page_title()
        TouchAction(driver).press(x=855, y=1215).move_to(x=268, y=1222).release().perform()
        pair_your_earbuds.should_be_pye_page_title()
        pair_your_earbuds.should_be_correct_pye_page_subtitle3()
        pair_your_earbuds.should_be_instructions_image()
        pair_your_earbuds.should_be_open_bluetooth_button()
        pair_your_earbuds.should_be_open_bluetooth_button_text()

    def test_pair_your_earbuds_carousel_back_swipe(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        landing_page = LandingPage(driver)
        pair_your_earbuds = PairYourEarbudsPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
        pair_your_earbuds.should_be_correct_pye_page_subtitle1()
        TouchAction(driver).press(x=855, y=1215).move_to(x=268, y=1222).release().perform()
        pair_your_earbuds.should_be_correct_pye_page_subtitle2()
        TouchAction(driver).press(x=855, y=1215).move_to(x=268, y=1222).release().perform()
        pair_your_earbuds.should_be_correct_pye_page_subtitle3()
        TouchAction(driver).press(x=218, y=1176).move_to(x=829, y=1176).release().perform()
        pair_your_earbuds.should_be_correct_pye_page_subtitle2()
        TouchAction(driver).press(x=218, y=1176).move_to(x=829, y=1176).release().perform()
        pair_your_earbuds.should_be_correct_pye_page_subtitle1()
