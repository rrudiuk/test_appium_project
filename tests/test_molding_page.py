import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import DialogPage
from .pages.landing_page import LandingPage
from .pages.molding_page import MoldingPage
from .pages.home_page import HomePage
from .pages.welcome_page import WelcomePage

import time


@pytest.mark.bt_connected
@pytest.mark.smoke_test_not_molded
class TestMoldingPage:
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

    def test_should_be_how_is_bass_page(self, driver):
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
        molding_page.tap_main_button()
        molding_page.should_be_how_is_bass_title()
        molding_page.should_be_correct_how_is_bass_subtitle()
        molding_page.should_be_image_volume()
        molding_page.should_be_adjust_volume_bar()
        molding_page.should_be_cancel_button()
        molding_page.should_be_cancel_button_text()
        molding_page.tap_cancel_button()

    def test_should_start_soon_page1(self, driver):
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
        molding_page.tap_main_button()
        molding_page.should_be_how_is_bass_title()
        time.sleep(19)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        molding_page.tap_cancel_button()

    def test_should_start_soon_page2(self, driver):
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
        molding_page.tap_main_button()
        molding_page.should_be_how_is_bass_title()
        time.sleep(19)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(6)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        molding_page.tap_cancel_button()

    def test_cancel_molding_on_count(self, driver):
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
        molding_page.tap_main_button()
        molding_page.should_be_how_is_bass_title()
        time.sleep(19)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(6)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        time.sleep(5)
        molding_page.tap_cancel_button()

    @pytest.mark.first_molding
    def test_molding_complete(self, driver):
        analytics_page = AnalyticsPage(driver)
        dialog_page = DialogPage(driver)
        landing_page = LandingPage(driver)
        molding_page = MoldingPage(driver)
        home_page = HomePage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.should_be_landing_page_title()
        time.sleep(12)
        molding_page.should_be_try_them_page_title()
        molding_page.tap_main_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_main_button()
        molding_page.should_be_how_is_bass_title()
        time.sleep(19)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(6)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        time.sleep(45)
        molding_page.should_be_progress_bar()
        time.sleep(40)
        molding_page.should_congratulations_title()
        molding_page.should_congratulations_subtitle()
        molding_page.should_finish_button()
        molding_page.should_finish_button_text()
        molding_page.tap_finish_button()
        dialog_page.should_be_welcome_dialog_title()
        dialog_page.should_be_welcome_dialog_message()
        dialog_page.tap_no_thanks_button()
        home_page.should_be_earbuds_name()
        home_page.should_be_connected_state()
        home_page.should_be_hamburger_menu()
        home_page.should_be_settings_icon()
        home_page.should_be_left_earbud_image()
        home_page.should_be_left_battery_image()
        home_page.should_be_left_battery_percents()
        home_page.should_be_right_earbud_image()
        home_page.should_be_right_battery_image()
        home_page.should_be_right_battery_percents()
        home_page.should_be_case_image()
        home_page.should_be_case_battery_image()
        home_page.should_be_case_battery_percents()
        home_page.should_be_eq_expand_icon()
        home_page.should_be_eq_name()
        home_page.should_be_ue_signature_eq_selected()
        home_page.should_be_eq_curve_image()
