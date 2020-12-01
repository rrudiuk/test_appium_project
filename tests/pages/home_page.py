from .base_page import BasePage
from .locators import HomePageLocators


class HomePage(BasePage):
    def should_be_earbuds_name(self):
        self.is_element_present(*HomePageLocators.EARBUDS_NAME)

    def should_be_connected_state(self):
        expected_result = "Connected"
        actual_result = self.get_text(*HomePageLocators.EARBUDS_STATUS)
        assert actual_result == expected_result, f"State {actual_result} is shown, should be {expected_result}"

    def should_be_scanning_state(self):
        expected_result = "Scanning"
        actual_result = self.get_text(*HomePageLocators.EARBUDS_STATUS)
        assert actual_result == expected_result, f"State {actual_result} is shown, should be {expected_result}"

    def should_be_button_connect_earbuds(self):
        self.is_element_present(*HomePageLocators.CONNECT_EARBUDS_BUTTON), "Button doesn't appear"
        expected_result = "Connect Earbuds"
        actual_result = self.get_text(*HomePageLocators.CONNECT_EARBUDS_BUTTON)
        assert actual_result == expected_result, f"Text {actual_result} is shown, should be {expected_result}"

    def tap_button_connect_earbuds(self):
        self.click_element(*HomePageLocators.CONNECT_EARBUDS_BUTTON)

    def should_be_hamburger_menu(self):
        self.is_element_present(*HomePageLocators.HOME_SCREEN_LEFT_MENU)

    def tap_hamburger_menu_icon(self):
        self.click_element(*HomePageLocators.HOME_SCREEN_LEFT_MENU)

    def should_be_settings_icon(self):
        self.is_element_present(*HomePageLocators.HOME_SCREEN_SETTINGS)

    def tap_settings_icon(self):
        self.click_element(*HomePageLocators.HOME_SCREEN_SETTINGS)

    def should_be_left_earbud_image(self):
        self.is_element_present(*HomePageLocators.LEFT_EARBUD_IMAGE)

    def should_be_right_earbud_image(self):
        self.is_element_present(*HomePageLocators.RIGHT_EARBUD_IMAGE)

    def should_be_case_image(self):
        self.is_element_present(*HomePageLocators.CASE_IMAGE)

    def should_be_left_battery_image(self):
        self.is_element_present(*HomePageLocators.LEFT_BATTERY_IMAGE)

    def should_be_right_battery_image(self):
        self.is_element_present(*HomePageLocators.RIGHT_BATTERY_IMAGE)

    def should_be_case_battery_image(self):
        self.is_element_present(*HomePageLocators.CASE_BATTERY_IMAGE)

    def should_be_left_battery_percents(self):
        self.is_element_present(*HomePageLocators.LEFT_BATTERY_PERCENTS)

    def should_be_right_battery_percents(self):
        self.is_element_present(*HomePageLocators.RIGHT_BATTERY_PERCENTS)

    def should_be_case_battery_percents(self):
        self.is_element_present(*HomePageLocators.CASE_BATTERY_PERCENTS)

    def should_be_eq_expand_icon(self):
        self.is_element_present(*HomePageLocators.EXPAND_IMAGE)

    def should_be_eq_name(self):
        self.is_element_present(*HomePageLocators.CHOSEN_PRESET_NAME)

    def should_be_ue_signature_eq_selected(self):
        expected_result = "UE Signature"
        actual_result = self.get_text(*HomePageLocators.CHOSEN_PRESET_NAME)
        assert actual_result == expected_result, f"Preset {actual_result} is selected, should be {expected_result}"

    def should_be_eq_curve_image(self):
        self.is_element_present(*HomePageLocators.EQ_CURVE_IMAGE)
