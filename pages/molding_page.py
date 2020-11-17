from .base_page import BasePage
from .locators import BasePageLocators
from .locators import MoldingPageLocators


class MoldingPage(BasePage):
    def should_be_molding_page_title(self):
        expected_result = "Try Them On"
        actual_result = self.get_text(*BasePageLocators.SCREEN_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_correct_molding_page_subtitle(self):
        expected_result = "Pop your earbuds into your ears. Gently adjust them until they feel comfortable and secure."
        actual_result = self.get_text(*BasePageLocators.SCREEN_SUBTITLE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"
