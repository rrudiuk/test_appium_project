from pages.landing_page import LandingPage
from pages.analytics_page import AnalyticsPage
from pages.welcome_page import WelcomePage
from pages.molding_page import MoldingPage

import time


class TestLandingPage:
    def test_should_be_try_them_page(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        landing_page = LandingPage(driver)
        molding_page = MoldingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
        molding_page.should_be_try_them_page_title()
        molding_page.should_be_correct_try_them_page_subtitle()
        molding_page.should_be_main_button()

    def test_should_be_get_ready_page(self, driver):
        analytics_page = AnalyticsPage(driver)
        welcome_page = WelcomePage(driver)
        landing_page = LandingPage(driver)
        molding_page = MoldingPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
        molding_page.should_be_try_them_page_title()
        molding_page.tap_main_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.should_be_message_title1()
        molding_page.should_be_message_title2()
        molding_page.should_be_message_title3()
        molding_page.should_be_message1()
        molding_page.should_be_message2()
        molding_page.should_be_message3()
        molding_page.should_be_smile()
        molding_page.should_be_stand_by_mirror_text()
        molding_page.should_be_main_button()
