import pytest

from ..pages.welcome_page import WelcomePage
from ..pages.demo_page import DemoSendCommandsPage

import time

"""These are the tests that set up another tests so must be run first"""


class TestThatRunsFirst:
    @pytest.mark.activate_curing
    @pytest.mark.first_molding
    @pytest.mark.pair_earbuds_carousel
    @pytest.mark.smoke_test_not_molded
    def test_curring_mode_activation(self, driver):
        welcome_page = WelcomePage(driver)
        demo_commands_page = DemoSendCommandsPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_demo_screen_code()
        welcome_page.tap_screen_code_get_started()
        time.sleep(6)
        demo_commands_page.should_be_demo_molding_screen()
        demo_commands_page.tap_debug_button()
        demo_commands_page.activate_curring_mode()
