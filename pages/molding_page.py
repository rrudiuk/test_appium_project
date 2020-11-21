from .base_page import BasePage
from .locators import BasePageLocators
from .locators import MoldingPageLocators


class MoldingPage(BasePage):
    def should_be_try_them_page_title(self):
        expected_result = "Try Them On"
        actual_result = self.get_text(*BasePageLocators.SCREEN_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_correct_try_them_page_subtitle(self):
        expected_result = "Pop your earbuds into your ears. Gently adjust them until they feel comfortable and secure."
        actual_result = self.get_text(*BasePageLocators.SCREEN_SUBTITLE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"

    def should_be_main_button(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_MAIN)

    def tap_main_button(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)

    def should_be_get_ready_page_title(self):
        expected_result = "Get Ready"
        actual_result = self.get_text(*BasePageLocators.SCREEN_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_message_title1(self):
        expected_result = "1"
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG_TITLE1)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_message_title2(self):
        expected_result = "2"
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG_TITLE2)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_message_title3(self):
        expected_result = "3"
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG_TITLE3)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_message1(self):
        expected_result = "We'll do a quick sound test to ensure a sound-isolating fit before we mold."
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG1)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"

    def should_be_message2(self):
        expected_result = "We'll share some quick tips for achieving the best mold."
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG2)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"

    def should_be_message3(self):
        expected_result = "The 60 second molding magic starts."
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_TEXT_VIEW_MSG3)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"

    def should_be_smile(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_SMILE_IMAGE)

    def should_be_stand_by_mirror_text(self):
        expected_result = "Try standing by a mirror for this part"
        actual_result = self.get_text(*BasePageLocators.SCREEN_SUBTITLE)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"
