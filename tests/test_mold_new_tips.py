import time

import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.molding_page import MoldNewTipsPage
from .pages.home_page import HomePage
from .pages.menu_page import MenuPage
from .pages.welcome_page import WelcomePage


class TestMoldNewTips:
    def test_mold_new_tips_carousel(self, driver):
        analytics_page = AnalyticsPage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        mold_new_tips_page = MoldNewTipsPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.tap_share_analytics_button()
        home_page.wait_for_connection()
        home_page.should_be_earbuds_name()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_mold_new_tips_item()
        # Change your tips
        mold_new_tips_page.should_be_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.should_be_next_button_text()
        mold_new_tips_page.next_button_not_enabled()
        mold_new_tips_page.should_be_image_item()
        mold_new_tips_page.should_be_change_tips_title()
        mold_new_tips_page.should_be_change_tips_subtitle()
        # Remove inserts
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.should_be_next_button_text()
        mold_new_tips_page.next_button_not_enabled()
        mold_new_tips_page.should_be_image_item()
        mold_new_tips_page.should_be_remove_inserts_title()
        mold_new_tips_page.should_be_remove_inserts_subtitle()
        # Match them up
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.should_be_next_button_text()
        mold_new_tips_page.next_button_not_enabled()
        mold_new_tips_page.should_be_image_item()
        mold_new_tips_page.should_be_match_them_up_title()
        mold_new_tips_page.should_be_match_them_up_subtitle()
        # Attach your tips
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.should_be_next_button_text()
        mold_new_tips_page.next_button_not_enabled()
        mold_new_tips_page.should_be_image_item()
        mold_new_tips_page.should_be_attach_your_tips_title()
        mold_new_tips_page.should_be_attach_your_tips_subtitle()
        # Check the fit
        mold_new_tips_page.swipe_left()
        mold_new_tips_page.should_be_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.should_be_next_button_text()
        mold_new_tips_page.next_button_enabled()
        mold_new_tips_page.should_be_image_item()
        mold_new_tips_page.should_be_check_the_fit_title()
        mold_new_tips_page.should_be_check_the_fit_subtitle()
        # Attach your tips
        mold_new_tips_page.swipe_right()
        mold_new_tips_page.should_be_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.should_be_next_button_text()
        mold_new_tips_page.next_button_enabled()
        mold_new_tips_page.should_be_image_item()
        mold_new_tips_page.should_be_attach_your_tips_title()
        mold_new_tips_page.should_be_attach_your_tips_subtitle()
        # Match them up
        mold_new_tips_page.swipe_right()
        mold_new_tips_page.should_be_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.should_be_next_button_text()
        mold_new_tips_page.next_button_enabled()
        mold_new_tips_page.should_be_image_item()
        mold_new_tips_page.should_be_match_them_up_title()
        mold_new_tips_page.should_be_match_them_up_subtitle()
        # Remove inserts
        mold_new_tips_page.swipe_right()
        mold_new_tips_page.should_be_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.should_be_next_button_text()
        mold_new_tips_page.next_button_enabled()
        mold_new_tips_page.should_be_image_item()
        mold_new_tips_page.should_be_remove_inserts_title()
        mold_new_tips_page.should_be_remove_inserts_subtitle()
        # Change your tips
        mold_new_tips_page.swipe_right()
        mold_new_tips_page.should_be_menu_icon()
        mold_new_tips_page.should_be_scroll_dots()
        mold_new_tips_page.should_be_next_button()
        mold_new_tips_page.should_be_next_button_text()
        mold_new_tips_page.next_button_enabled()
        mold_new_tips_page.should_be_image_item()
        mold_new_tips_page.should_be_change_tips_title()
        mold_new_tips_page.should_be_change_tips_subtitle()
        # Return to Home screen
        mold_new_tips_page.tap_menu_icon()
        menu_page.tap_home_item()
        home_page.should_be_earbuds_name()

    @pytest.mark.test
    def test_mold_new_tips_molding(self, driver):
        analytics_page = AnalyticsPage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        mold_new_tips_page = MoldNewTipsPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.tap_share_analytics_button()
        home_page.wait_for_connection()
        home_page.should_be_earbuds_name()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_mold_new_tips_item()
        # Change your tips
        mold_new_tips_page.should_be_change_tips_title()
        mold_new_tips_page.swipe_left()
        # Remove inserts
        mold_new_tips_page.should_be_remove_inserts_title()
        mold_new_tips_page.swipe_left()
        # Match them up
        mold_new_tips_page.should_be_match_them_up_title()
        mold_new_tips_page.swipe_left()
        # Attach your tips
        mold_new_tips_page.should_be_attach_your_tips_title()
        mold_new_tips_page.swipe_left()
        # Check the fit
        mold_new_tips_page.should_be_check_the_fit_title()
        mold_new_tips_page.tap_next_button()
        # Try them on
        mold_new_tips_page.wait_for_connection()
        mold_new_tips_page.should_be_try_them_page_title()
        mold_new_tips_page.tap_main_button()
        mold_new_tips_page.should_be_get_ready_page_title()
        mold_new_tips_page.tap_main_button()
        mold_new_tips_page.should_be_how_is_bass_title()
        time.sleep(19)
        mold_new_tips_page.should_be_starting_soon_title()
        mold_new_tips_page.should_be_starting_soon_subtitle1()
        time.sleep(6)
        mold_new_tips_page.should_be_starting_soon_title()
        mold_new_tips_page.should_be_starting_soon_subtitle2()
        time.sleep(45)
        mold_new_tips_page.should_be_progress_bar()
        time.sleep(40)
        # Congratulations
        mold_new_tips_page.should_congratulations_title()
        mold_new_tips_page.should_be_finish_button()
        mold_new_tips_page.should_be_finish_button_text()
        mold_new_tips_page.tap_finish_button()
        # Home screen
        home_page.should_be_earbuds_name()
