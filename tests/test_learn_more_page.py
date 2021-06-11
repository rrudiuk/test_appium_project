import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.home_page import HomePage
from .pages.learn_more_page import LearnMorePage
from .pages.menu_page import MenuPage
from .pages.welcome_page import WelcomePage


class TestMoldNewTips:
    def test_learn_more_carousel(self, driver):
        analytics_page = AnalyticsPage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        learn_more_page = LearnMorePage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.tap_share_analytics_button()
        home_page.wait_for_connection()
        home_page.should_be_earbuds_name()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_learn_more_item()
        # Double tap control
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_double_tap_control_title()
        learn_more_page.should_be_double_tap_control_message()
        learn_more_page.should_be_double_tap_control_video()
        learn_more_page.swipe_left()
        # Custom Control
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_custom_control_title()
        learn_more_page.should_be_custom_control_message()
        learn_more_page.should_be_custom_control_image()
        learn_more_page.swipe_left()
        # Switching devices
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_switching_devices_title()
        learn_more_page.should_be_switching_devices_message()
        learn_more_page.should_be_switching_devices_image()
        learn_more_page.swipe_left()
        # EQ Customization
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_eq_customization_title()
        learn_more_page.should_be_eq_customization_message()
        learn_more_page.should_be_eq_customization_image()
        learn_more_page.swipe_left()
        # Test Your Fit
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_tyf_title()
        learn_more_page.should_be_tyf_message()
        learn_more_page.should_be_tyf_image()
        learn_more_page.swipe_left()
        # Pair a new device
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_pair_device_title()
        learn_more_page.should_be_pair_device_message()
        learn_more_page.should_be_pair_device_animation()
        learn_more_page.should_be_pair_device_notice()
        learn_more_page.swipe_left()
        # Status indicators
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_status_indicators_title()
        learn_more_page.should_be_status_indicators_message()
        learn_more_page.should_be_status_indicators_image()
        learn_more_page.should_be_status_indicators_notice()
        learn_more_page.swipe_right()
        # Pair a new device
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_pair_device_title()
        learn_more_page.should_be_pair_device_message()
        learn_more_page.should_be_pair_device_animation()
        learn_more_page.should_be_pair_device_notice()
        learn_more_page.swipe_right()
        # Test Your Fit
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_tyf_title()
        learn_more_page.should_be_tyf_message()
        learn_more_page.should_be_tyf_image()
        learn_more_page.swipe_right()
        # EQ Customization
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_eq_customization_title()
        learn_more_page.should_be_eq_customization_message()
        learn_more_page.should_be_eq_customization_image()
        learn_more_page.swipe_right()
        # Switching devices
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_switching_devices_title()
        learn_more_page.should_be_switching_devices_message()
        learn_more_page.should_be_switching_devices_image()
        learn_more_page.swipe_right()
        # Custom Control
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_custom_control_title()
        learn_more_page.should_be_custom_control_message()
        learn_more_page.should_be_custom_control_image()
        learn_more_page.swipe_right()
        # Double tap control
        learn_more_page.should_be_menu_icon()
        learn_more_page.should_be_double_tap_control_title()
        learn_more_page.should_be_double_tap_control_message()
        learn_more_page.should_be_double_tap_control_video()
        # Return to menu
        learn_more_page.tap_menu_icon()
        menu_page.should_be_learn_more_item()
