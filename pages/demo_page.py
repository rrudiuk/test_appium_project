from .base_page import BasePage
from .locators import BasePageLocators
from .locators import DemoPageLocators


class DemoPage(BasePage):
    def should_be_correct_toolbar_title(self):
        actual_result = self.get_text(*BasePageLocators.TOOL_BAR_TITLE)
        expected_result = "Scan"
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_app_version(self):
        assert self.is_element_present(*DemoPageLocators.DEMO_APP_VERSION)

    def should_be_left_label(self):
        actual_result = self.get_text(*DemoPageLocators.DEMO_LEFT_LABEL)
        expected_result = "Left:"
        assert actual_result == expected_result, f"Incorrect label '{actual_result}', should be '{expected_result}'"

    def should_be_right_label(self):
        actual_result = self.get_text(*DemoPageLocators.DEMO_RIGHT_LABEL)
        expected_result = "Right:"
        assert actual_result == expected_result, f"Incorrect label '{actual_result}', should be '{expected_result}'"

    def should_be_left_status(self):
        assert self.is_element_present(*DemoPageLocators.DEMO_LEFT_STATUS)

    def should_be_right_status(self):
        assert self.is_element_present(*DemoPageLocators.DEMO_RIGHT_STATUS)
