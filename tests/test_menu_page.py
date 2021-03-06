import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.home_page import HomePage
from .pages.menu_page import MenuPage
from .pages.welcome_page import WelcomePage


class TestMenuPage:
    def test_all_menu_items_appear(self, driver):
        analytics_page = AnalyticsPage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.tap_share_analytics_button()
        home_page.wait_for_connection()
        home_page.should_be_earbuds_name()
        home_page.tap_hamburger_menu_icon()
        menu_page.should_be_header()
        menu_page.should_be_app_logo()
        menu_page.should_be_exit_x_button()
        menu_page.should_be_home_item()
        menu_page.should_be_mold_new_tips_item()
        menu_page.should_be_test_your_fit_item()
        menu_page.should_be_learn_more_item()
        menu_page.should_be_support_item()
        menu_page.tap_exit_x_button()
        home_page.should_be_earbuds_name()
