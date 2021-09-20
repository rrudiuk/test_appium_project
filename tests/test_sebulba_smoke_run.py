import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import EditPresetsDialogPage
from .pages.dialogs_page import FwUpdateDialogPage
from .pages.eq_presets_page import EditPresetsPage
from .pages.eq_presets_page import EqPresetsPage
from .pages.eq_presets_page import EqPresetSetupPage
from .pages.email_entry_page import EmailEntryPage
from .pages.firmware_update_page import FirmwareUpdatePage
from .pages.home_page import HomePage
from .pages.landing_page import LandingPage
from .pages.learn_more_page import LearnMorePage
from .pages.menu_page import MenuPage
from .pages.molding_page import MoldingPage, MoldNewTipsPage
from .pages.sebulba_demo_page import SebulbaDemoPage
from .pages.support_page import SupportPage
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


"""That's the set of tests from all test files intended to run smoke test
Requires connected earbuds via BT classic pulled off out of the case"""


@pytest.mark.sebulba_smoke_test
class TestSmokeTest:
    # Welcome page
    def test_should_be_welcome_screen(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_screen_button()
        welcome_page.should_be_welcome_get_started_button_text()

    @pytest.mark.xfail
    def test_should_be_welcome_screen_after_background(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_screen_button()
        welcome_page.should_be_welcome_get_started_button_text()
        welcome_page.background_app_for_5_seconds()
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_screen_button()
        welcome_page.should_be_welcome_get_started_button_text()

    def test_should_be_welcome_code_screen(self, driver):
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.should_be_welcome_edit_text_input()
        welcome_page.should_be_welcome_edit_text_input_text()
        welcome_page.should_be_welcome_send_code_button()
        welcome_page.should_be_welcome_code_get_started_button_text()
        welcome_page.should_be_welcome_where_is_my_code()
        welcome_page.should_be_welcome_where_is_my_code_text()

    # Email entry page
    def test_should_be_email_entry_screen(self, driver):
        email_entry_page = EmailEntryPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        email_entry_page.should_be_back_arrow()
        email_entry_page.should_be_email_entry_title()
        email_entry_page.should_be_correct_email_entry_subtitle()
        email_entry_page.should_be_email_entry_input()
        email_entry_page.should_be_correct_sign_me_button_text()
        email_entry_page.should_be_correct_no_thanks_button_text()

    def test_return_to_welcome_screen(self, driver):
        email_entry_page = EmailEntryPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        email_entry_page.should_be_back_arrow()
        email_entry_page.tap_back_arrow()
        welcome_page.should_be_correct_welcome_title()
        welcome_page.should_be_correct_welcome_subtitle()
        welcome_page.should_be_welcome_screen_button()
        welcome_page.should_be_welcome_get_started_button_text()

    # Analytics page
    def test_should_be_analytics_screen(self, driver):
        analytics_page = AnalyticsPage(driver)
        email_entry_page = EmailEntryPage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        email_entry_page.should_be_email_entry_title()
        email_entry_page.tap_no_thanks_button()
        analytics_page.should_be_back_arrow()
        analytics_page.should_be_analytics_title()
        analytics_page.should_be_correct_analytics_subtitle()
        analytics_page.should_be_correct_share_analytics_button_text()
        analytics_page.should_be_correct_not_share_analytics_button_text()

    # Demo page
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

    # Molding page
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

    # Activate curing for second molding
    def test_activate_curing1(self, driver):
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

    # EQ presets page
    def test_initial_presets_screen_setup(self, driver):
        initial_setup_non_molding(driver)
        eq_presets_page = EqPresetsPage(driver)
        # Access eq screen
        eq_presets_page.tap_eq_expand_icon()
        # Check if all items appear
        eq_presets_page.should_be_eq_expand_icon()
        eq_presets_page.should_be_eq_name()
        eq_presets_page.should_be_ue_signature_eq_selected()
        eq_presets_page.should_be_eq_curve_image()
        eq_presets_page.should_be_toolbar()
        eq_presets_page.should_be_customize_button()
        eq_presets_page.should_be_customize_button_text()
        eq_presets_page.should_be_expandable_part()
        eq_presets_page.should_be_divider_line()
        eq_presets_page.should_be_presets_title()
        eq_presets_page.should_be_edit_button()
        eq_presets_page.should_be_edit_button_text()
        eq_presets_page.should_be_add_button()
        eq_presets_page.should_be_presets_list()
        eq_presets_page.should_be_six_presets()
        eq_presets_page.should_be_initial_preset_order()

    def test_switching_between_eq_presets(self, driver):
        initial_setup_non_molding(driver)
        eq_presets_page = EqPresetsPage(driver)
        # Access eq screen
        eq_presets_page.tap_eq_expand_icon()
        # Check initial setup
        eq_presets_page.should_be_eq_expand_icon()
        eq_presets_page.should_be_eq_name()
        eq_presets_page.should_be_ue_signature_eq_selected()
        eq_presets_page.should_be_eq_curve_image()
        eq_presets_page.should_be_toolbar()
        eq_presets_page.should_be_expandable_part()
        # Select different presets
        eq_presets_page.select_6_preset()
        eq_presets_page.select_1_preset()
        eq_presets_page.select_5_preset()
        eq_presets_page.select_2_preset()
        eq_presets_page.select_3_preset()
        eq_presets_page.select_4_preset()

    def test_access_edit_presets_screen(self, driver):
        initial_setup_non_molding(driver)
        edit_preset_page = EditPresetsPage(driver)
        eq_presets_page = EqPresetsPage(driver)
        # Access eq screen
        eq_presets_page.tap_eq_expand_icon()
        # Check initial setup
        eq_presets_page.should_be_eq_expand_icon()
        eq_presets_page.should_be_eq_name()
        eq_presets_page.should_be_ue_signature_eq_selected()
        eq_presets_page.should_be_eq_curve_image()
        eq_presets_page.should_be_toolbar()
        eq_presets_page.should_be_expandable_part()
        # Access edit presets screen
        eq_presets_page.tap_edit_button()
        # Check all items
        edit_preset_page.should_be_toolbar()
        edit_preset_page.should_be_back_arrow()
        edit_preset_page.should_be_edit_preset_title()
        edit_preset_page.should_be_save_button()
        edit_preset_page.should_be_save_button_text()
        edit_preset_page.should_be_presets_list()
        edit_preset_page.should_be_six_presets()
        edit_preset_page.should_be_initial_preset_order()

    def test_preset_reorder_should_be_possible(self, driver):
        initial_setup_non_molding(driver)
        edit_preset_page = EditPresetsPage(driver)
        eq_presets_page = EqPresetsPage(driver)
        # Access eq screen
        eq_presets_page.tap_eq_expand_icon()
        # Access reordering screen
        eq_presets_page.tap_edit_button()
        # Reorder presets
        edit_preset_page.move_first_preset_to_fourth_position()
        edit_preset_page.move_six_preset_to_second_position()
        edit_preset_page.move_three_to_four_position()

    def test_reordering_should_not_be_saved_after_tapping_back_button(self, driver):
        initial_setup_non_molding(driver)
        edit_preset_page = EditPresetsPage(driver)
        eq_presets_page = EqPresetsPage(driver)
        # Access eq screen
        eq_presets_page.tap_eq_expand_icon()
        eq_presets_page.scroll_down()
        time.sleep(3)
        eq_presets_page.should_be_initial_preset_order()
        # Access reordering screen
        eq_presets_page.tap_edit_button()
        # Reorder presets
        edit_preset_page.move_second_preset_to_fourth_position()
        # Return back and check the order
        edit_preset_page.tap_back_arrow()
        time.sleep(3)
        eq_presets_page.should_be_initial_preset_order()

    @pytest.mark.xfail
    def test_reordering_should_be_saved_after_tapping_save_button(self, driver):
        initial_setup_non_molding(driver)
        edit_preset_page = EditPresetsPage(driver)
        eq_presets_page = EqPresetsPage(driver)
        # Access eq screen
        eq_presets_page.tap_eq_expand_icon()
        # Access reordering screen
        eq_presets_page.tap_edit_button()
        # Reorder presets
        edit_preset_page.move_first_preset_to_fourth_position()
        # Tap save
        edit_preset_page.tap_save_button()
        time.sleep(2)
        eq_presets_page.background_app_for_5_seconds()
        # Check the order
        eq_presets_page.should_be_ue_signature_eq_selected()
        eq_presets_page.should_be_preset_order_after_moving_ue_signature_to_fourth()

    def test_reorder_and_delete_first_item(self, driver):
        initial_setup_non_molding(driver)
        edit_preset_page = EditPresetsPage(driver)
        eq_presets_page = EqPresetsPage(driver)
        dialog_preset_page = EditPresetsDialogPage(driver)
        # Access eq screen
        eq_presets_page.tap_eq_expand_icon()
        # Access reordering screen
        eq_presets_page.tap_edit_button()
        # Reorder presets
        edit_preset_page.move_first_preset_to_fourth_position()
        # Delete top preset
        edit_preset_page.delete_top_preset()
        dialog_preset_page.should_be_dialog_title()
        dialog_preset_page.should_be_dialog_message()
        dialog_preset_page.tap_delete_button()
        edit_preset_page.should_be_five_presets()
        # Save and check the order
        edit_preset_page.tap_save_button()
        time.sleep(5)
        eq_presets_page.should_be_ue_signature_eq_selected()
        eq_presets_page.should_be_five_presets()

    def test_cancel_preset_deletion(self, driver):
        initial_setup_non_molding(driver)
        edit_preset_page = EditPresetsPage(driver)
        eq_presets_page = EqPresetsPage(driver)
        dialog_preset_page = EditPresetsDialogPage(driver)
        # Access eq screen
        eq_presets_page.tap_eq_expand_icon()
        # Access reordering screen
        eq_presets_page.tap_edit_button()
        # Delete preset
        edit_preset_page.delete_sixth_preset()
        dialog_preset_page.should_be_dialog_title()
        dialog_preset_page.should_be_dialog_message()
        dialog_preset_page.tap_cancel_button()
        edit_preset_page.should_be_six_presets()
        # Save and check the number of presets
        edit_preset_page.tap_save_button()
        time.sleep(5)
        eq_presets_page.should_be_ue_signature_eq_selected()
        eq_presets_page.should_be_six_presets()

    def test_delete_all_presets(self, driver):
        initial_setup_non_molding(driver)
        edit_preset_page = EditPresetsPage(driver)
        eq_presets_page = EqPresetsPage(driver)
        dialog_preset_page = EditPresetsDialogPage(driver)
        # Access eq screen
        eq_presets_page.tap_eq_expand_icon()
        # Access reordering screen
        eq_presets_page.tap_edit_button()
        # Delete preset #6
        edit_preset_page.delete_sixth_preset()
        dialog_preset_page.should_be_dialog_title()
        dialog_preset_page.should_be_dialog_message()
        dialog_preset_page.tap_delete_button()
        edit_preset_page.should_be_five_presets()
        # Delete preset #5
        edit_preset_page.delete_fifth_preset()
        dialog_preset_page.should_be_dialog_title()
        dialog_preset_page.should_be_dialog_message()
        dialog_preset_page.tap_delete_button()
        edit_preset_page.should_be_four_presets()
        # Delete preset #4
        edit_preset_page.delete_fourth_preset()
        dialog_preset_page.should_be_dialog_title()
        dialog_preset_page.should_be_dialog_message()
        dialog_preset_page.tap_delete_button()
        edit_preset_page.should_be_three_presets()
        # Delete preset #3
        edit_preset_page.delete_third_preset()
        dialog_preset_page.should_be_dialog_title()
        dialog_preset_page.should_be_dialog_message()
        dialog_preset_page.tap_delete_button()
        edit_preset_page.should_be_two_presets()
        # Delete preset #2
        edit_preset_page.delete_top_preset()
        dialog_preset_page.should_be_dialog_title()
        dialog_preset_page.should_be_dialog_message()
        dialog_preset_page.tap_delete_button()
        edit_preset_page.should_be_one_preset()
        edit_preset_page.tap_save_button()
        time.sleep(5)
        eq_presets_page.should_be_ue_signature_eq_selected()
        eq_presets_page.should_be_one_preset()

    def test_access_new_preset_editor(self, driver):
        initial_setup_non_molding(driver)
        eq_presets_page = EqPresetsPage(driver)
        eq_preset_setup_page = EqPresetSetupPage(driver)
        eq_presets_page.tap_eq_expand_icon()
        eq_presets_page.tap_add_button()
        eq_preset_setup_page.should_be_toolbar()
        eq_preset_setup_page.should_be_new_preset_setup_title()
        eq_preset_setup_page.should_be_eq_editor()
        eq_preset_setup_page.should_be_history_title()
        eq_preset_setup_page.should_be_backward_arrow()
        eq_preset_setup_page.should_be_forward_arrow()
        eq_preset_setup_page.should_be_history_progress_bar()
        eq_preset_setup_page.tap_back_arrow()
        eq_presets_page.should_be_initial_preset_order()

    # Home page
    def test_home_screen_connected(self, driver):
        initial_setup_non_molding(driver)
        eq_presets_page = EqPresetsPage(driver)
        home_page = HomePage(driver)
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
        home_page.should_be_case_battery_image()
        home_page.should_be_case_battery_percents()
        eq_presets_page.should_be_eq_expand_icon()
        eq_presets_page.should_be_eq_name()
        eq_presets_page.should_be_ue_signature_eq_selected()
        eq_presets_page.should_be_eq_curve_image()

    def test_home_screen_after_closing_presets_screen(self, driver):
        initial_setup_non_molding(driver)
        eq_presets_page = EqPresetsPage(driver)
        home_page = HomePage(driver)
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
        home_page.should_be_case_battery_image()
        home_page.should_be_case_battery_percents()
        eq_presets_page.should_be_eq_expand_icon()
        eq_presets_page.should_be_eq_name()
        eq_presets_page.should_be_ue_signature_eq_selected()
        eq_presets_page.should_be_eq_curve_image()
        eq_presets_page.tap_eq_expand_icon()
        eq_presets_page.tap_eq_expand_icon()
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
        home_page.should_be_case_battery_image()
        home_page.should_be_case_battery_percents()

    # Menu page
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

    # Mold new tips page
    def test_mold_new_tips_carousel(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        mold_new_tips_page = MoldNewTipsPage(driver)
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

    def test_mold_new_tips_molding(self, driver):
        initial_setup_non_molding(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        mold_new_tips_page = MoldNewTipsPage(driver)
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
        time.sleep(2)
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

    # FW update page
    def test_firmware_update1(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()

    def test_firmware_update2(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()

    def test_firmware_update3(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()

    def test_firmware_update4(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()

    def test_firmware_update5(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()

# run with
# pytest -s -v --reruns 1 -m sebulba_smoke_test --html=/Users/rudiuk/PyCharmProjects/test_appium_project/test_report/report.html --capture sys
