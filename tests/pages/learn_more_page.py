from .base_page import BasePage
from .locators import LearnMoreLocators


class LearnMorePage(BasePage):
    def should_be_double_tap_control_title(self):
        self.check_screen_title("Double Tap Control")

    def should_be_double_tap_control_message(self):
        self.check_screen_message("Double-tap the left or right earbud to Play/Pause audio or Answer/End calls.")

    def should_be_double_tap_control_video(self):
        self.is_element_present(*LearnMoreLocators.SCREEN_VIDEO), "Animation video not found"

    def should_be_close_button(self):
        self.is_element_present(*LearnMoreLocators.CLOSE_BUTTON), "Close button not found"

    def tap_close_button(self):
        self.click_element(*LearnMoreLocators.CLOSE_BUTTON)
