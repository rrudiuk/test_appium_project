import pytest

from .pages.welcome_page import WelcomePage
from .pages.sebulba_demo_page import SebulbaDemoPage


@pytest.mark.sebulba_demo
class TestSebulbaDemoPage:
    def test_should_be_sebulba_debug_screen(self, driver):
        welcome_page = WelcomePage(driver)
        sebulba_demo_page = SebulbaDemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_centurion_screen_code()
        welcome_page.tap_screen_code_get_started()
        sebulba_demo_page.wait_for_connection()
        sebulba_demo_page.should_be_connected_state()
        sebulba_demo_page.should_be_select_feature_title()
        sebulba_demo_page.should_be_select_function_title()
        sebulba_demo_page.should_be_payload_title()
        sebulba_demo_page.should_be_payload_input()
        sebulba_demo_page.should_be_send_button()

    def test_activate_curing(self, driver):
        welcome_page = WelcomePage(driver)
        sebulba_demo_page = SebulbaDemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_centurion_screen_code()
        welcome_page.tap_screen_code_get_started()
        sebulba_demo_page.wait_for_connection()
        sebulba_demo_page.should_be_connected_state()
        sebulba_demo_page.tap_feature_spinner()
        sebulba_demo_page.select_i_fits_molding()
        sebulba_demo_page.tap_function_spinner()
        sebulba_demo_page.select_set_molding_prep_mode()
        sebulba_demo_page.input_payload_to_enable_curing_on_both_earbuds()
        sebulba_demo_page.should_be_send_button()
        sebulba_demo_page.should_be_payload_input()
        sebulba_demo_page.tap_send_button()
        sebulba_demo_page.should_be_success_state_after_sending_command()
