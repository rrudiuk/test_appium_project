import time

import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import FwUpdateDialogPage
from .pages.email_entry_page import EmailEntryPage
from .pages.home_page import HomePage
from .pages.settings_page import SettingsPage
from .pages.welcome_page import WelcomePage


def initial_setup_non_molding(driver):
    analytics_page = AnalyticsPage(driver)
    dialog_page = FwUpdateDialogPage(driver)
    email_entry_page = EmailEntryPage(driver)
    home_page = HomePage(driver)
    welcome_page = WelcomePage(driver)
    welcome_page.should_be_correct_welcome_title()
    welcome_page.tap_welcome_screen_get_started()
    email_entry_page.should_be_email_entry_title()
    email_entry_page.tap_no_thanks_button()
    analytics_page.tap_share_analytics_button()
    home_page.wait_for_connection()
    dialog_page.check_dialog_and_close_it()
    home_page.should_be_connected_state()


class TestMenuPage:
    def test_all_items_appear_on_settings_screen(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        settings_page = SettingsPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_settings_icon()
        home_page.tap_settings_icon()
        settings_page.should_be_settings_title()
        settings_page.should_be_back_arrow()
        settings_page.should_be_name_item()
        settings_page.should_be_single_tap_switcher()
        settings_page.should_be_left_single_tap_item()
        settings_page.should_be_right_single_tap_item()
        settings_page.should_be_double_tap_switcher()
        settings_page.should_be_left_double_tap_item()
        settings_page.should_be_right_double_tap_item()
        settings_page.scroll_down_settings_screen()
        settings_page.should_be_dark_mode_item()
        settings_page.should_be_language_item()
