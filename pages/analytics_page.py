from .base_page import BasePage
from .locators import AnalyticsPageLocators
from .locators import BasePageLocators


class AnalyticsPage(BasePage):

    def should_be_analytics_title(self):
        expected_result = "Help Us Improve Our Products"
        actual_result = self.get_text(*BasePageLocators.SCREEN_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_correct_analytics_subtitle(self):
        expected_result = "Help Ultimate Ears improve its products and services by automatically sending diagnostic " \
                          "and usage data."
        actual_result = self.get_text(*BasePageLocators.SCREEN_SUBTITLE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"

    def should_be_correct_share_analytics_button_text(self):
        expected_result = "Yes, Share Analytics Data"
        actual_result = self.get_text(*AnalyticsPageLocators.ANALYTICS_SHARE_BUTTON)
        assert actual_result == expected_result, f"Incorrect button text '{actual_result}', should be '{expected_result}'"

    def tap_share_analytics_button(self):
        self.click_element(*AnalyticsPageLocators.ANALYTICS_SHARE_BUTTON)

    def should_be_correct_not_share_analytics_button_text(self):
        expected_result = "NO THANKS"
        actual_result = self.get_text(*AnalyticsPageLocators.ANALYTICS_NOT_SHARE_BUTTON)
        assert actual_result == expected_result, f"Incorrect button text '{actual_result}', should be '{expected_result}'"

    def tap_not_share_analytics_button(self):
        self.click_element(*AnalyticsPageLocators.ANALYTICS_NOT_SHARE_BUTTON)
