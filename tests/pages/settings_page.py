from appium.webdriver.common.touch_action import TouchAction

from .base_page import BasePage
from .locators import SettingsPageLocators


class SettingsPage(BasePage):
    def should_be_settings_title(self):
        self.check_screen_title("Settings")

    def scroll_down_settings_screen(self):
        el = self.locate_element(*SettingsPageLocators.DOUBLE_TAP_TITLE)
        TouchAction(self.driver).press(el).move_to(x=493, y=413).release().perform()

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

    # Single tap switcher
    def should_be_single_tap_switcher(self):
        self.check_message(*SettingsPageLocators.SINGLE_TAP_TITLE, "SINGLE TAP")
        self.check_message(*SettingsPageLocators.SINGLE_TAP_STATUS_TITLE, "Off / On")
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_SWITCHER), "Single tap switcher not found"
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_STATUS_DIVIDER), "Single tap divider not found"

    # Left single tap
    def should_be_left_single_tap_item(self):
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ITEM), "Left single tap item not found"
        self.check_message(*SettingsPageLocators.SINGLE_TAP_LEFT_TITLE, "LEFT")
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_STATE), "Left single tap selection not found"
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_ACTION_ARROW), "Left single tap arrow not found"
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_LEFT_DIVIDER), "Left single tap divider not found"

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

    def tap_right_single_tap_item(self):
        self.is_element_present(*SettingsPageLocators.SINGLE_TAP_RIGHT_ITEM), "Right single tap item not found"
        self.click_element(*SettingsPageLocators.SINGLE_TAP_RIGHT_ITEM)

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
