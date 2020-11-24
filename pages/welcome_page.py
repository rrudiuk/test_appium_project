from .base_page import BasePage
from .locators import WelcomePageLocators
from .locators import BasePageLocators

import time


class WelcomePage(BasePage):
    def should_be_correct_welcome_title(self):
        self.check_screen_title("Welcome to Your Perfect Fit")

    def should_be_correct_welcome_subtitle(self):
        self.check_screen_subtitle("In just a few minutes, you'll have a pair of perfectly fitting, incredibly "
                                   "comfortable earbuds.")

    def should_be_welcome_screen_button(self):
        assert self.is_element_present(*WelcomePageLocators.WELCOME_SCREEN_BUTTON)

    def should_be_welcome_get_started_button_text(self):
        expected_result = "Get Started"
        actual_result = self.get_text(*WelcomePageLocators.WELCOME_SCREEN_BUTTON)
        assert actual_result == expected_result, f"Incorrect button text '{actual_result}', should be '{expected_result}'"

    def tap_welcome_screen_get_started(self):
        self.click_element(*WelcomePageLocators.WELCOME_SCREEN_BUTTON)

    def tap_welcome_screen_10_times(self):
        self.click_element_10_times(*BasePageLocators.SCREEN_TITLE)

    def should_be_welcome_code_screen_title(self):
        # self.click_element_10_times(*BasePageLocators.SCREEN_TITLE)
        # expected_result = "WELCOME"
        # actual_result = self.get_text(*BasePageLocators.SCREEN_TITLE)
        # assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"
        self.check_screen_title("WELCOME")

    def should_be_welcome_edit_text_input(self):
        assert self.is_element_present(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE)

    def should_be_welcome_edit_text_input_text(self):
        expected_result = "ENTER YOUR CODE"
        actual_result = self.get_text(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"

    def should_be_welcome_send_code_button(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_MAIN)

    def should_be_welcome_code_get_started_button_text(self):
        expected_result = "GET STARTED"
        actual_result = self.get_text(*BasePageLocators.BUTTON_MAIN)
        assert actual_result == expected_result, f"Incorrect button text '{actual_result}', should be '{expected_result}'"

    def should_be_welcome_where_is_my_code(self):
        assert self.is_element_present(*WelcomePageLocators.WELCOME_SCREEN_WHERE_IS_MY_CODE)

    def should_be_welcome_where_is_my_code_text(self):
        expected_result = "WHERE IS MY CODE?"
        actual_result = self.get_text(*WelcomePageLocators.WELCOME_SCREEN_WHERE_IS_MY_CODE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"

    def tap_where_is_my_code(self):
        self.click_element(*WelcomePageLocators.WELCOME_SCREEN_WHERE_IS_MY_CODE)

    def should_be_correct_setup_code_title(self):
        self.check_screen_title("SETUP CODE")

    def should_be_correct_welcome_setup_code_text(self):
        expected_result = "Your setup code is the number written on the inside lid of your box."
        actual_result = self.get_text(*WelcomePageLocators.WELCOME_SETUP_CODE_TEXT)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def close_welcome_setup_code_screen(self):
        self.click_element(*WelcomePageLocators.WELCOME_SETUP_SCREEN_CLOSE)

    def go_to_demo_screen_code(self):
        text_input = self.locate_element(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE)
        text_input.send_keys("001")

    def go_to_home_screen_code(self):
        text_input = self.locate_element(*WelcomePageLocators.WELCOME_SCREEN_EDIT_TEXT_CODE)
        text_input.send_keys("002")

    def tap_screen_code_get_started(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)
        time.sleep(5)
