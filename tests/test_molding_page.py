import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import FwUpdateDialogPage
from .pages.eq_presets_page import EqPresetsPage
from .pages.email_entry_page import EmailEntryPage
from .pages.landing_page import LandingPage
from .pages.learn_more_page import LearnMorePage
from .pages.molding_page import MoldingPage
from .pages.home_page import HomePage
from .pages.ugc_page import UGCPage
from .pages.welcome_page import WelcomePage

import time


def initial_setup_molding(driver):
    analytics_page = AnalyticsPage(driver)
    email_entry_page = EmailEntryPage(driver)
    landing_page = LandingPage(driver)
    welcome_page = WelcomePage(driver)
    welcome_page.should_be_correct_welcome_title()
    welcome_page.tap_welcome_screen_get_started()
    email_entry_page.should_be_email_entry_title()
    email_entry_page.tap_no_thanks_button()
    analytics_page.tap_share_analytics_button()
    landing_page.should_be_landing_page_title()
    landing_page.wait_for_connection()


class TestMoldingPage:
    def test_should_be_try_them_page(self, driver):
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
        molding_page.should_be_try_them_page_title()
        molding_page.should_be_correct_try_them_page_subtitle()
        molding_page.should_be_main_button()

    def test_should_be_get_ready_page(self, driver):
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
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
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
        molding_page.should_be_try_them_page_title()
        molding_page.tap_main_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_main_button()
        time.sleep(2)
        molding_page.should_be_how_is_bass_title()
        molding_page.should_be_correct_how_is_bass_subtitle()
        molding_page.should_be_image_volume()
        molding_page.should_be_adjust_volume_bar()
        molding_page.should_be_cancel_button()
        molding_page.should_be_cancel_button_text()
        molding_page.tap_cancel_button()
        time.sleep(2)
        molding_page.should_be_get_ready_page_title()

    def test_should_start_soon_page1(self, driver):
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
        molding_page.should_be_try_them_page_title()
        molding_page.tap_main_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_main_button()
        time.sleep(2)
        molding_page.should_be_how_is_bass_title()
        time.sleep(19)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        molding_page.tap_cancel_button()
        molding_page.should_be_get_ready_page_title()

    def test_should_start_soon_page2(self, driver):
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
        molding_page.should_be_try_them_page_title()
        molding_page.tap_main_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_main_button()
        time.sleep(2)
        molding_page.should_be_how_is_bass_title()
        time.sleep(19)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(6)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        molding_page.tap_cancel_button()
        molding_page.should_be_get_ready_page_title()

    def test_cancel_molding_on_count(self, driver):
        initial_setup_molding(driver)
        molding_page = MoldingPage(driver)
        molding_page.should_be_try_them_page_title()
        molding_page.tap_main_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_main_button()
        time.sleep(2)
        molding_page.should_be_how_is_bass_title()
        time.sleep(19)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle1()
        time.sleep(6)
        molding_page.should_be_starting_soon_title()
        molding_page.should_be_starting_soon_subtitle2()
        time.sleep(4)
        molding_page.tap_cancel_button()
        time.sleep(2)
        molding_page.should_be_get_ready_page_title()

    @pytest.mark.ohboy_first_molding
    def test_molding_complete(self, driver):
        initial_setup_molding(driver)
        dialog_page = FwUpdateDialogPage(driver)
        eq_presets_page = EqPresetsPage(driver)
        home_page = HomePage(driver)
        molding_page = MoldingPage(driver)
        ugc_page = UGCPage(driver)
        molding_page.should_be_try_them_page_title()
        molding_page.tap_main_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_main_button()
        time.sleep(2)
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

        # UGC
        ugc_page.should_be_ugc_title()
        ugc_page.should_be_correct_ugc_subtitle()
        ugc_page.tap_skip_button()

        # Congratulations
        molding_page.should_congratulations_title()
        molding_page.should_congratulations_subtitle_after_first_molding()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_be_take_the_tour_button_text()
        molding_page.should_skip_for_now_button()
        molding_page.should_skip_for_now_button_text()
        molding_page.tap_skip_for_now_button()
        time.sleep(5)

        # Home screen
        dialog_page.check_dialog_and_close_it()
        home_page.should_be_earbuds_name()
        home_page.should_be_connected_state()
        home_page.should_be_hamburger_menu_icon()
        home_page.should_be_settings_icon()
        home_page.should_be_left_earbud_image()
        home_page.should_be_left_battery_image()
        home_page.should_be_left_battery_percents()
        home_page.should_be_right_earbud_image()
        home_page.should_be_right_battery_image()
        home_page.should_be_right_battery_percents()
        home_page.should_be_case_image()
        eq_presets_page.should_be_eq_expand_icon()
        eq_presets_page.should_be_eq_name()
        eq_presets_page.should_be_ue_signature_eq_selected()
        eq_presets_page.should_be_eq_curve_image()

    @pytest.mark.skip
    @pytest.mark.sebulba_first_molding
    def test_molding_complete_and_open_learn_more(self, driver):
        initial_setup_molding(driver)
        dialog_page = FwUpdateDialogPage(driver)
        learn_more_page = LearnMorePage(driver)
        molding_page = MoldingPage(driver)
        home_page = HomePage(driver)
        ugc_page = UGCPage(driver)
        molding_page.should_be_try_them_page_title()
        molding_page.tap_main_button()
        molding_page.should_be_get_ready_page_title()
        molding_page.tap_main_button()
        time.sleep(2)
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

        # UGC
        ugc_page.should_be_ugc_title()
        ugc_page.should_be_correct_ugc_subtitle()
        ugc_page.tap_skip_button()

        # Congratulations
        molding_page.should_congratulations_title()
        molding_page.should_congratulations_subtitle_after_first_molding()
        molding_page.should_skip_for_now_button()
        molding_page.should_skip_for_now_button_text()
        molding_page.should_be_take_the_tour_button()
        molding_page.should_be_take_the_tour_button_text()
        molding_page.tap_take_the_tour_button()

        # Double tap control
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_double_tap_control_title()
        learn_more_page.should_be_double_tap_control_message()
        learn_more_page.should_be_double_tap_control_video()
        learn_more_page.swipe_left()
        # Custom Control
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_custom_control_title()
        time.sleep(2)
        learn_more_page.should_be_custom_control_message()
        learn_more_page.should_be_custom_control_image()
        learn_more_page.swipe_left_modified()
        # Switching devices
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_switching_devices_title()
        learn_more_page.should_be_switching_devices_message()
        # learn_more_page.should_be_switching_devices_image()
        learn_more_page.swipe_left()
        # EQ Customization
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_eq_customization_title()
        learn_more_page.should_be_eq_customization_message()
        learn_more_page.should_be_eq_customization_image()
        learn_more_page.swipe_left()
        # Test Your Fit
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_tyf_title()
        learn_more_page.should_be_tyf_message()
        learn_more_page.should_be_tyf_image()
        learn_more_page.swipe_left()
        # Pair a new device
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_pair_device_title()
        learn_more_page.should_be_pair_device_message()
        learn_more_page.should_be_pair_device_animation()
        learn_more_page.should_be_pair_device_notice()
        learn_more_page.swipe_left()
        # Status indicators
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_status_indicators_title()
        learn_more_page.should_be_status_indicators_message()
        # learn_more_page.should_be_status_indicators_image()
        learn_more_page.should_be_status_indicators_notice()
        learn_more_page.swipe_right()
        # Pair a new device
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_pair_device_title()
        learn_more_page.should_be_pair_device_message()
        learn_more_page.should_be_pair_device_animation()
        learn_more_page.should_be_pair_device_notice()
        learn_more_page.swipe_right()
        # Test Your Fit
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_tyf_title()
        learn_more_page.should_be_tyf_message()
        learn_more_page.should_be_tyf_image()
        learn_more_page.swipe_right()
        # EQ Customization
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_eq_customization_title()
        learn_more_page.should_be_eq_customization_message()
        learn_more_page.should_be_eq_customization_image()
        learn_more_page.swipe_right()
        # Switching devices
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_switching_devices_title()
        learn_more_page.should_be_switching_devices_message()
        # learn_more_page.should_be_switching_devices_image()
        learn_more_page.swipe_right()
        # Custom Control
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_custom_control_title()
        learn_more_page.should_be_custom_control_message()
        learn_more_page.should_be_custom_control_image()
        learn_more_page.swipe_right()
        # Double tap control
        learn_more_page.should_be_close_button()
        learn_more_page.should_be_double_tap_control_title()
        learn_more_page.should_be_double_tap_control_message()
        learn_more_page.should_be_double_tap_control_video()
        # Quit
        learn_more_page.tap_close_button()
        dialog_page.check_dialog_and_close_it()
        home_page.should_be_earbuds_name()
