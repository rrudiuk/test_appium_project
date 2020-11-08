from .base_page import BasePage
from .locators import BasePageLocators
from .locators import DemoPageLocators

from selenium.webdriver.common.by import By
import time


class DemoPage(BasePage):

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


class DemoSendCommandsPage(BasePage):
    def tap_debug_button(self):
        self.click_element(*DemoPageLocators.DEMO_DEBUG_BUTTON)

    def should_be_demo_molding_screen(self):
        actual_result = self.get_text(*BasePageLocators.TOOL_BAR_TITLE)
        expected_result = "Molding"
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_demo_debug_screen(self):
        actual_result = self.get_text(*BasePageLocators.TOOL_BAR_TITLE)
        expected_result = "Debug"
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def tap_first_commands_list_item(self):
        self.click_element(*DemoPageLocators.DEMO_FIRST_RESPONSE)

    def tap_second_commands_list_item(self):
        self.click_element(*DemoPageLocators.DEMO_SECOND_RESPONSE)
