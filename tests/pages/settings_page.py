from appium.webdriver.common.touch_action import TouchAction

from .base_page import BasePage
from .locators import BasePageLocators
from .locators import SettingsPageLocators


class SettingsPage(BasePage):
    def should_be_settings_title(self):
        self.check_screen_title("Settings")

    def scroll_down_settings_screen(self):
        el = self.locate_element(*SettingsPageLocators.DOUBLE_TAP_TITLE)
        TouchAction(self.driver).press(el).move_to(x=493, y=413).release().perform()

    def save_selection(self):
        self.is_element_present(*BasePageLocators.SAVE_BUTTON), "Save button not found"
        self.click_element(*BasePageLocators.SAVE_BUTTON)

    # Name
    def should_be_name_item(self):
        self.is_element_present(*SettingsPageLocators.NAME_ITEM), "Name item not found"
        self.check_message(*SettingsPageLocators.NAME_TITLE, "NAME")
        self.is_element_present(*SettingsPageLocators.NAME_VALUE), "Name of earbuds not found"
        self.is_element_present(*SettingsPageLocators.NAME_ACTION_ARROW), "Name action arrow not found"
        self.is_element_present(*SettingsPageLocators.NAME_DIVIDER), "Name divider not found"

    def tap_name_item(self):
        self.is_element_present(*SettingsPageLocators.NAME_ITEM), "Name item not found"
        self.click_element(*SettingsPageLocators.NAME_ITEM)

    # Edit name screen
    def should_be_edit_name_title(self):
        self.check_screen_title("Edit Name")

    def should_be_name_title(self):
        self.check_message(*SettingsPageLocators.NAME_TITLE, "NAME")

    def should_be_name_input(self):
        self.is_element_present(*SettingsPageLocators.EDIT_NAME_INPUT), "Name input not found"

    def should_be_name_input_clear(self):
        self.is_element_present(*SettingsPageLocators.EDIT_NAME_INPUT_CLEAR), "Clear X button in name input not found"

    def clear_name_input_field(self):
        self.click_element(*SettingsPageLocators.EDIT_NAME_INPUT_CLEAR)

    def should_be_edit_name_hint(self):
        self.check_message(*SettingsPageLocators.EDIT_NAME_HINT, "Your earbuds will restart in order to finish the "
                                                                 "renaming process.\n\nOnce restarted, you will need to"
                                                                 " pair your earbuds to your device again.")

    def should_be_update_name_button(self):
        self.check_button(*BasePageLocators.BUTTON_MAIN, "Update Name")

    def should_be_disabled_update_button(self):
        assert not self.is_element_enabled(*BasePageLocators.BUTTON_MAIN), "Update Name button is enabled, should " \
                                                                           "be disabled"

    def should_be_enabled_update_button(self):
        assert self.is_element_enabled(*BasePageLocators.BUTTON_MAIN), "Update Name button is disabled, should " \
                                                                           "be enabled"

    # Test names on edit name screen
    def should_be_empty_input_field(self):
        expected_result = ""
        name = self.get_text(*SettingsPageLocators.EDIT_NAME_INPUT)
        assert name == expected_result, f"Incorrect name '{name}', should be '{expected_result}'"

    def should_be_0_letters_shown_for_empty_input_field(self):
        expected_result = "0 of 16 characters"
        actual_result = self.get_text(*SettingsPageLocators.EDIT_NAME_MAX)
        assert actual_result == expected_result, f"Incorrect name '{actual_result}', should be '{expected_result}'"

    def enter_4_letter_name(self):
        self.clear_name_input_field()
        self.enter_text(*SettingsPageLocators.EDIT_NAME_INPUT, "NAME")

    def should_be_4_letter_name(self):
        expected_result = "NAME"
        name = self.get_text(*SettingsPageLocators.EDIT_NAME_INPUT)
        assert name == expected_result, f"Incorrect name '{name}', should be '{expected_result}'"

    def should_be_4_letters_shown_for_4_letters_name(self):
        expected_result = "4 of 16 characters"
        actual_result = self.get_text(*SettingsPageLocators.EDIT_NAME_MAX)
        assert actual_result == expected_result, f"Incorrect name '{actual_result}', should be '{expected_result}'"

    def enter_11_letter_name(self):
        self.clear_name_input_field()
        self.enter_text(*SettingsPageLocators.EDIT_NAME_INPUT, "hello world")

    def should_be_11_letter_name(self):
        expected_result = "hello world"
        name = self.get_text(*SettingsPageLocators.EDIT_NAME_INPUT)
        assert name == expected_result, f"Incorrect name '{name}', should be '{expected_result}'"

    def should_be_11_letters_shown_for_4_letters_name(self):
        expected_result = "11 of 16 characters"
        actual_result = self.get_text(*SettingsPageLocators.EDIT_NAME_MAX)
        assert actual_result == expected_result, f"Incorrect name '{actual_result}', should be '{expected_result}'"

    def enter_16_letter_name(self):
        self.clear_name_input_field()
        self.enter_text(*SettingsPageLocators.EDIT_NAME_INPUT, "hello world! hey")

    def should_be_16_letter_name(self):
        expected_result = "hello world! hey"
        name = self.get_text(*SettingsPageLocators.EDIT_NAME_INPUT)
        assert name == expected_result, f"Incorrect name '{name}', should be '{expected_result}'"

    def should_be_16_letters_shown_for_4_letters_name(self):
        expected_result = "16 of 16 characters"
        actual_result = self.get_text(*SettingsPageLocators.EDIT_NAME_MAX)
        assert actual_result == expected_result, f"Incorrect name '{actual_result}', should be '{expected_result}'"

    def enter_over_max_letter_name(self):
        self.clear_name_input_field()
        self.enter_text(*SettingsPageLocators.EDIT_NAME_INPUT, "hello world! hey hey hey!")

    # Single tap switcher
    def should_be_single_tap_switcher(self):
        self.check_message(*SettingsPageLocators.SINGLE_TAP_TITLE, "SINGLE TAP")
        self.check_message(*SettingsPageLocators.SINGLE_TAP_STATUS_TITLE, "Off / On")
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_SWITCHER), "Single tap switcher not found"
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_STATUS_DIVIDER), "Single tap divider not found"

    def single_tap_enabled_check(self):
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_SWITCHER), "Single tap switcher not found"
        expected_state = "ON"
        actual_state = self.get_text(*SettingsPageLocators.SINGLE_TAP_SWITCHER)
        assert actual_state == expected_state, f"Incorrect state '{actual_state}', should be '{expected_state}'"

    def single_tap_disabled_check(self):
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_SWITCHER), "Single tap switcher not found"
        expected_state = "OFF"
        actual_state = self.get_text(*SettingsPageLocators.SINGLE_TAP_SWITCHER)
        assert actual_state == expected_state, f"Incorrect state '{actual_state}', should be '{expected_state}'"

    def toggle_single_tap_state(self):
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_SWITCHER), "Single tap switcher not found"
        self.click_element(*SettingsPageLocators.SINGLE_TAP_SWITCHER)

    # Left single tap
    def should_be_left_single_tap_item(self):
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ITEM), "Left single tap item not found"
        self.check_message(*SettingsPageLocators.SINGLE_TAP_LEFT_TITLE, "LEFT")
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE), "Left single tap selection not found"
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ACTION_ARROW), "Left single tap arrow not found"
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_DIVIDER), "Left single tap divider not found"

    def should_not_be_left_single_tap_item(self):
        self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ITEM), "Left single tap item not found"
        self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE), "Left single tap selection not found"
        self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ACTION_ARROW), "Left single tap arrow " \
                                                                                         "not found"
        self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_DIVIDER), "Left single tap divider not found"

    def tap_left_single_tap_item(self):
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ITEM), "Left single tap item not found"
        self.click_element(*SettingsPageLocators.SINGLE_TAP_LEFT_ITEM)

    # Right single tap
    def should_be_right_single_tap_item(self):
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_ITEM), "Right single tap item not found"
        self.check_message(*SettingsPageLocators.SINGLE_TAP_RIGHT_TITLE, "RIGHT")
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE), "Right single tap selection not found"
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_ACTION_ARROW), "Right single tap arrow not found"
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_DIVIDER), "Right single tap divider not found"

    def should_not_be_right_single_tap_item(self):
        self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_ITEM), "Right single tap item not found"
        self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE), "Right single tap selection not" \
                                                                                   " found"
        self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_ACTION_ARROW), "Right single tap arrow" \
                                                                                          " not found "
        self.is_not_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_DIVIDER), "Right single tap divider not " \
                                                                                     "found "

    def tap_right_single_tap_item(self):
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_ITEM), "Right single tap item not found"
        self.click_element(*SettingsPageLocators.SINGLE_TAP_RIGHT_ITEM)

    # Single tap screen
    def should_be_single_tap_items_screen(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_PLAY_PAUSE, "Play/Pause")
        self.check_button(*SettingsPageLocators.SINGLE_TAP_NEXT_TRACK, "Next Track")
        self.check_button(*SettingsPageLocators.SINGLE_TAP_PREVIOUS_TRACK, "Previous Track")
        self.check_button(*SettingsPageLocators.SINGLE_TAP_VOLUME_UP, "Volume Up")
        self.check_button(*SettingsPageLocators.SINGLE_TAP_VOLUME_DOWN, "Volume Down")

    # Select each single tap item
    def select_single_tap_play_pause(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_PLAY_PAUSE, "Play/Pause")
        self.click_element(*SettingsPageLocators.SINGLE_TAP_PLAY_PAUSE)

    def select_single_tap_next_track(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_NEXT_TRACK, "Next Track")
        self.click_element(*SettingsPageLocators.SINGLE_TAP_NEXT_TRACK)

    def select_single_tap_previous_track(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_PREVIOUS_TRACK, "Previous Track")
        self.click_element(*SettingsPageLocators.SINGLE_TAP_PREVIOUS_TRACK)

    def select_single_tap_volume_up(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_VOLUME_UP, "Volume Up")
        self.click_element(*SettingsPageLocators.SINGLE_TAP_VOLUME_UP)

    def select_single_tap_volume_down(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_VOLUME_DOWN, "Volume Down")
        self.click_element(*SettingsPageLocators.SINGLE_TAP_VOLUME_DOWN)

    # Check if single tap left was selected correctly
    def should_be_play_pause_selected_single_tap_left(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE, "Play/Pause")

    def should_be_next_track_selected_single_tap_left(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE, "Next Track")

    def should_be_previous_track_selected_single_tap_left(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE, "Previous Track")

    def should_be_volume_up_selected_single_tap_left(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE, "Volume Up")

    def should_be_volume_down_selected_single_tap_left(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE, "Volume Down")

    # Check if single tap right was selected correctly
    def should_be_play_pause_selected_single_tap_right(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE, "Play/Pause")

    def should_be_next_track_selected_single_tap_right(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE, "Next Track")

    def should_be_previous_track_selected_single_tap_right(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE, "Previous Track")

    def should_be_volume_up_selected_single_tap_right(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE, "Volume Up")

    def should_be_volume_down_selected_single_tap_right(self):
        self.check_button(*SettingsPageLocators.SINGLE_TAP_RIGHT_STATE, "Volume Down")

    # Double tap switcher
    def should_be_double_tap_switcher(self):
        self.check_message(*SettingsPageLocators.DOUBLE_TAP_TITLE, "DOUBLE TAP")
        self.check_message(*SettingsPageLocators.DOUBLE_TAP_STATUS_TITLE, "Off / On")
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_SWITCHER), "Double tap switcher not found"
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_STATUS_DIVIDER), "Double tap divider not found"

    # Left double tap
    def should_be_left_double_tap_item(self):
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_ITEM), "Left double tap item not found"
        self.check_message(*SettingsPageLocators.DOUBLE_TAP_LEFT_TITLE, "LEFT")
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_STATE), "Left double tap selection not found"
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_ACTION_ARROW), "Left double tap arrow not found"
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_DIVIDER), "Left double tap divider not found"

    def tap_left_double_tap_item(self):
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_LEFT_ITEM), "Left double tap item not found"
        self.click_element(*SettingsPageLocators.DOUBLE_TAP_LEFT_ITEM)

    # Right single tap
    def should_be_right_double_tap_item(self):
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_ITEM), "Right double tap item not found"
        self.check_message(*SettingsPageLocators.DOUBLE_TAP_RIGHT_TITLE, "RIGHT")
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_STATE), "Right double tap selection not found"
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_ACTION_ARROW), "Right double tap arrow not found"
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_DIVIDER), "Right double tap divider not found"

    def tap_right_double_tap_item(self):
        self.is_element_present(*SettingsPageLocators.DOUBLE_TAP_RIGHT_ITEM), "Right double tap item not found"
        self.click_element(*SettingsPageLocators.DOUBLE_TAP_RIGHT_ITEM)

    # Dark mode
    def should_be_dark_mode_item(self):
        self.is_element_present(*SettingsPageLocators.DARK_MODE_ITEM), "Dark mode item not found"
        self.check_message(*SettingsPageLocators.DARK_MODE_TITLE, "DARK MODE")
        self.is_element_present(*SettingsPageLocators.DARK_MODE_VALUE), "Dark mode value not found"
        self.is_element_present(*SettingsPageLocators.DARK_MODE_ACTION_ARROW), "Dark mode action arrow not found"
        self.is_element_present(*SettingsPageLocators.DARK_MODE_DIVIDER), "Dark mode divider not found"

    def tap_dark_mode_item(self):
        self.is_element_present(*SettingsPageLocators.DARK_MODE_ITEM), "Dark mode item not found"
        self.click_element(*SettingsPageLocators.DARK_MODE_ITEM)

    # Language
    def should_be_language_item(self):
        self.is_element_present(*SettingsPageLocators.LANGUAGE_ITEM), "Language item not found"
        self.check_message(*SettingsPageLocators.LANGUAGE_TITLE, "LANGUAGE")
        self.is_element_present(*SettingsPageLocators.LANGUAGE_VALUE), "Language value not found"
        self.is_element_present(*SettingsPageLocators.LANGUAGE_ACTION_ARROW), "Language action arrow not found"
        self.is_element_present(*SettingsPageLocators.LANGUAGE_DIVIDER), "Language divider not found"

    def tap_language_item(self):
        self.is_element_present(*SettingsPageLocators.LANGUAGE_ITEM), "Language item not found"
        self.click_element(*SettingsPageLocators.LANGUAGE_ITEM)
