from .base_page import BasePage
from .locators import BasePageLocators
from .locators import LandingPageLocators


class LandingPage(BasePage):
    def should_be_landing_page_title(self):
        expected_result = "Let’s Get Started"
        actual_result = self.get_text(*BasePageLocators.SCREEN_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_correct_landing_page_subtitle(self):
        expected_result = "Place your earbuds in the case with the lid open to get started."
        actual_result = self.get_text(*BasePageLocators.SCREEN_SUBTITLE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"

    def should_be_next_button(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_MAIN), "No Next button on the screen"
        expected_result = "Next"
        actual_result = self.get_text(*BasePageLocators.BUTTON_MAIN)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_next_button(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)
