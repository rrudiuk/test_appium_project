import pytest

from .pages.welcome_page import WelcomePage
from .pages.ohboy_demo_page import OhboyDemoPage
from .pages.ohboy_demo_page import OhboyDemoSendCommandsPage

import time


@pytest.mark.ohboy_demo
class TestOhboyDemoPage:
    # only when no available earbuds
    @pytest.mark.skip
    def test_can_access_demo_screen(self, driver):
        welcome_page = WelcomePage(driver)
        demo_page = OhboyDemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_demo_screen_code()
        welcome_page.tap_screen_code_get_started()
        demo_page.should_be_left_label()
        demo_page.should_be_right_label()
        demo_page.should_be_left_status()
        demo_page.should_be_right_status()

    def test_access_demo_molding_screen(self, driver):
        welcome_page = WelcomePage(driver)
        demo_commands_page = OhboyDemoSendCommandsPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_demo_screen_code()
        welcome_page.tap_screen_code_get_started()
        time.sleep(5)
        demo_commands_page.should_be_demo_initial_screen()

    def test_access_demo_debug_screen(self, driver):
        welcome_page = WelcomePage(driver)
        demo_commands_page = OhboyDemoSendCommandsPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_demo_screen_code()
        welcome_page.tap_screen_code_get_started()
        time.sleep(5)
        demo_commands_page.should_be_demo_initial_screen()
        demo_commands_page.tap_debug_button()
        demo_commands_page.should_be_demo_debug_screen()

    def test_check_first_two_items_codes(self, driver):
        welcome_page = WelcomePage(driver)
        demo_commands_page = OhboyDemoSendCommandsPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_demo_screen_code()
        welcome_page.tap_screen_code_get_started()
        time.sleep(5)
        demo_commands_page.should_be_demo_initial_screen()
        demo_commands_page.tap_debug_button()
        demo_commands_page.should_be_demo_debug_screen()
        demo_commands_page.tap_first_commands_list_item()
        demo_commands_page.tap_second_commands_list_item()

    @pytest.mark.ohboy_activate_curing
    @pytest.mark.ohboy_first_molding
    def test_curring_mode_activation(self, driver):
        welcome_page = WelcomePage(driver)
        demo_commands_page = OhboyDemoSendCommandsPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_demo_screen_code()
        welcome_page.tap_screen_code_get_started()
        time.sleep(6)
        demo_commands_page.should_be_demo_initial_screen()
        demo_commands_page.tap_debug_button()
        demo_commands_page.activate_curring_mode()

    def test_tap_feature_activation(self, driver):
        welcome_page = WelcomePage(driver)
        demo_commands_page = OhboyDemoSendCommandsPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_demo_screen_code()
        welcome_page.tap_screen_code_get_started()
        time.sleep(5)
        demo_commands_page.should_be_demo_initial_screen()
        demo_commands_page.tap_debug_button()
        demo_commands_page.enable_tap_feature()
        time.sleep(2)
        demo_commands_page.get_tap_feature_status_enabled()
        time.sleep(2)

    def test_tap_feature_deactivation(self, driver):
        welcome_page = WelcomePage(driver)
        demo_commands_page = OhboyDemoSendCommandsPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_demo_screen_code()
        welcome_page.tap_screen_code_get_started()
        time.sleep(5)
        demo_commands_page.should_be_demo_initial_screen()
        demo_commands_page.tap_debug_button()
        demo_commands_page.disable_tap_feature()
        time.sleep(2)
        demo_commands_page.get_tap_feature_status_disabled()
        time.sleep(2)
