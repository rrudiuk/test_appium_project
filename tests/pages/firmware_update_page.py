from .base_page import BasePage
from .locators import BasePageLocators
from .locators import FirmwareUpdatePageLocators

import time


class FirmwareUpdatePage(BasePage):
    def should_be_page_title(self):
        assert self.is_element_present(*BasePageLocators.SCREEN_TITLE), 'Screen title not found'

    def activate_fw_update(self):
        tries = 5
        while tries > 0:
            title = self.get_text(*BasePageLocators.SCREEN_TITLE)
            if title == 'Up to Date':
                self.click_element_10_times(*BasePageLocators.SCREEN_TITLE)
                tries = tries - 1
                time.sleep(5)
            elif self.locate_element(*FirmwareUpdatePageLocators.ROLLBACK_BUTTON):
                self.click_element(*FirmwareUpdatePageLocators.ROLLBACK_BUTTON)
                break
            else:
                self.click_element(*BasePageLocators.BUTTON_MAIN)
                self.should_be_ready_to_update_title()
                self.tap_install_now_button()
                break

    def tap_page_title_10_times(self):
        self.click_element_10_times(*BasePageLocators.SCREEN_TITLE)

    def should_be_update_available_title(self):
        self.check_screen_title("Update Available")

    def tap_update_earbuds_button(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)

    def tap_rollback_button(self):
        assert self.is_element_present(*FirmwareUpdatePageLocators.ROLLBACK_BUTTON), "Rollback button not found"
        self.click_element(*FirmwareUpdatePageLocators.ROLLBACK_BUTTON)

    def should_be_ready_to_update_title(self):
        self.check_screen_title("Ready to Update")

    def should_be_all_set_title(self):
        expected_result = "You’re All Set!"
        assert self.locate_element(*FirmwareUpdatePageLocators.ALL_SET_TITLE), "All set title not found"
        actual_result = self.get_text(*FirmwareUpdatePageLocators.ALL_SET_TITLE)
        assert actual_result == expected_result, f"{expected_result} is shown instead of All set title"

    def tap_install_now_button(self):
        self.click_element(*FirmwareUpdatePageLocators.UPDATE_BUTTON)

    def check_active_update(self):
        print("Start checking")
        tries = 30
        check_period = 30
        installing_title = "Installing"
        print(f"Start {installing_title} tries {tries} left")
        while tries > 0:
            print("while")
            if self.get_text(*FirmwareUpdatePageLocators.INSTALLING_TITLE) != installing_title:
                # if self.is_installing_title(installing_title):
                print(f"Stop {installing_title} tries {tries} left")
                break
            print('Continue')
            tries = tries - 1
            time.sleep(check_period)

        print("I'm here")

        if self.get_text(*BasePageLocators.SCREEN_TITLE) == "Restarting":
            print("Restarting is shown")
            time.sleep(45)

        if self.locate_element(*FirmwareUpdatePageLocators.ALL_SET_TITLE):
            self.should_be_all_set_title()
        elif self.locate_element(*FirmwareUpdatePageLocators.ERROR_OCCURRED_TITLE):
            tries = 3
            while tries > 0:
                self.click_element_10_times(*FirmwareUpdatePageLocators.ERROR_OCCURRED_TITLE)
                if self.get_text(*BasePageLocators.SCREEN_TITLE) == "Error":
                    pass
                    # Take a screenshot
                    break
                tries = tries - 1
        else:
            # Take a screenshot
            pass

        self.should_be_all_set_title()

    def is_installing_title(self, installing_title):
        if self.get_text(*FirmwareUpdatePageLocators.INSTALLING_TITLE) != installing_title:
            return True
        return False
