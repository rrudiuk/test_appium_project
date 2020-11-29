import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import DialogPage
from .pages.landing_page import LandingPage
from .pages.home_page import HomePage
from .pages.welcome_page import WelcomePage

import time


class TestHomePage:
    @pytest.mark.smoke_test_molded
    def test_home_screen_connected(self, driver):
        analytics_page = AnalyticsPage(driver)
        dialog_page = DialogPage(driver)
        landing_page = LandingPage(driver)
        home_page = HomePage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
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

    def test_home_screen_not_connected(self, driver):
        dialog_page = DialogPage(driver)
        home_page = HomePage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_home_screen_code()
        welcome_page.tap_screen_code_get_started()
        dialog_page.should_be_welcome_dialog_title()
        dialog_page.should_be_welcome_dialog_message()
        dialog_page.tap_no_thanks_button()
        home_page.should_be_earbuds_name()
        home_page.should_be_scanning_state()
        home_page.should_be_hamburger_menu()
        home_page.should_be_settings_icon()
        home_page.should_be_left_earbud_image()
        home_page.should_be_right_earbud_image()
        home_page.should_be_case_image()
        home_page.should_be_eq_expand_icon()
        home_page.should_be_eq_name()
        home_page.should_be_ue_signature_eq_selected()
        home_page.should_be_eq_curve_image()
        assert not home_page.should_be_left_battery_image()

# run with
# pytest -v --reruns 2 --tb=line -m test --html=report.html
# pytest -v --reruns 2 --tb=line -m test --html=C:\app\test_report\report.html
