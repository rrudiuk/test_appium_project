from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LearnMoreLocators


class LearnMorePage(BasePage):
    # Launch after molding
    def should_be_close_button(self):
        assert self.is_element_present(*BasePageLocators.CLOSE_BUTTON), "Close button not found"

    def tap_close_button(self):
        self.click_element(*BasePageLocators.CLOSE_BUTTON)

    # Menu icon
    def should_be_menu_icon(self):
        assert self.is_element_present(*BasePageLocators.MENU_ICON), "Menu icon not found"

    def tap_menu_icon(self):
        self.click_element(*BasePageLocators.MENU_ICON)

    # Double tap control
    def should_be_carousel_controls(self):
        assert self.is_element_present(*LearnMoreLocators.CAROUSEL_CONTROLS), "No carousel controls"

    def should_be_double_tap_control_title(self):
        self.check_screen_title("Double Tap Control")

    def should_be_double_tap_control_message(self):
        self.check_screen_message("Double-tap the left or right earbud to Play/Pause audio or Answer/End calls.")

    def should_be_double_tap_control_video(self):
        assert self.is_element_present(*LearnMoreLocators.SCREEN_VIDEO), "Double tap control video not found"

    # Custom Control
    def should_be_custom_control_title(self):
        self.check_screen_title("Custom Control")

    def should_be_custom_control_message(self):
        self.check_screen_message("Left and Right Double tap controls can be customized independently in "
                                  "the settings menu")

    def should_be_custom_control_image(self):
        assert self.is_element_present(*LearnMoreLocators.SCREEN_IMAGE), "Custom Control image not found"

    # Switching devices
    def should_be_switching_devices_title(self):
        self.check_screen_title("Switching Devices")

    def should_be_switching_devices_message(self):
        self.check_screen_message("To connect to another device that has been previously paired, go to the Bluetooth "
                                  "menu of the new device and select UE FITS.")

    def should_be_switching_devices_image(self):
        assert self.is_element_present(*LearnMoreLocators.SCREEN_IMAGE), "Switching devices image not found"

    # EQ Customization
    def should_be_eq_customization_title(self):
        self.check_screen_title("EQ Customization")

    def should_be_eq_customization_message(self):
        self.check_screen_message("Select from fine-tuned default UE presets or tap customize to create your own.")

    def should_be_eq_customization_image(self):
        assert self.is_element_present(*LearnMoreLocators.SCREEN_IMAGE), "EQ Customization image not found"

    # Test Your Fit
    def should_be_tyf_title(self):
        self.check_screen_title("Test Your Fit")

    def should_be_tyf_message(self):
        self.check_screen_message("Your fit is guaranteed for 30 days.\nFrom the main menu you can take a short quiz"
                                  " to confirm you have the perfect fit.")

    def should_be_tyf_image(self):
        assert self.is_element_present(*LearnMoreLocators.SCREEN_IMAGE), "Test Your Fit image not found"

    # Pair a new device
    def should_be_pair_device_title(self):
        self.check_screen_title("Pair a New Device")

    def should_be_pair_device_message(self):
        self.check_screen_message("To pair with a new device, place your earbuds in the case and press the case "
                                  "button until the earbuds flash white.")

    def should_be_pair_device_animation(self):
        assert self.is_element_present(*LearnMoreLocators.SCREEN_VIDEO), "Pair a new device animation not found"

    def should_be_pair_device_notice(self):
        expected_result = "Note: You can only have one device connected at any given time."
        assert self.is_element_present(*LearnMoreLocators.NOTICE_MESSAGE), f"Title {expected_result} not found"
        actual_result = self.get_text(*LearnMoreLocators.NOTICE_MESSAGE)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"

    # Status indicators
    def should_be_status_indicators_title(self):
        self.check_screen_title("Status Indicators")

    def should_be_status_indicators_message(self):
        self.check_screen_message("Lighting indicators on the charging case and the earbud indicate charging status"
                                  " of UE FITS.")

    def should_be_status_indicators_image(self):
        assert self.is_element_present(*LearnMoreLocators.SCREEN_IMAGE), "Status indicators image not found"

    def should_be_status_indicators_notice(self):
        expected_result = "*To reset your earbuds, press and hold the case button until the earbuds blink amber."
        assert self.is_element_present(*LearnMoreLocators.NOTICE_MESSAGE), f"Title {expected_result} not found"
        actual_result = self.get_text(*LearnMoreLocators.NOTICE_MESSAGE)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"
