import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import EditPresetsDialogPage
from .pages.eq_presets_page import EditPresetsPage
from .pages.email_entry_page import EmailEntryPage
from .pages.eq_presets_page import EqPresetsPage
from .pages.eq_presets_page import EqPresetSetupPage
from .pages.dialogs_page import FwUpdateDialogPage
from .pages.home_page import HomePage
from .pages.welcome_page import WelcomePage

import time


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


class TestEqPresetsPage:
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
