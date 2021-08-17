import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import FwUpdateDialogPage
from .pages.email_entry_page import EmailEntryPage
from .pages.home_page import HomePage
from .pages.menu_page import MenuPage
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
    def test_all_menu_items_appear(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        home_page.should_be_earbuds_name()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_header()
        menu_page.should_be_app_logo()
        menu_page.should_be_exit_x_button()
        menu_page.should_be_home_item()
        menu_page.should_be_mold_new_tips_item()
        menu_page.should_be_test_your_fit_item()
        menu_page.should_be_user_guide_item()
        menu_page.should_be_support_item()
        menu_page.should_be_email_entry_item()
        menu_page.should_be_take_selfie_item()
        menu_page.tap_exit_x_button()
        home_page.should_be_earbuds_name()
