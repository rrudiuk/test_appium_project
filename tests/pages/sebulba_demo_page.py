from .base_page import BasePage
from .locators import SebulbaDemoPageLocators


class SebulbaDemoPage(BasePage):
    def should_be_connected_state(self):
        actual_result = self.get_text(*SebulbaDemoPageLocators.CONNECTION_STATUS)
        expected_result = "Connected"
        assert actual_result == expected_result, f"Incorrect connection status '{actual_result}', should be " \
                                                 f"'{expected_result}'"

    def should_be_connecting_state(self):
        actual_result = self.get_text(*SebulbaDemoPageLocators.CONNECTION_STATUS)
        expected_result = "Connecting"
        assert actual_result == expected_result, f"Incorrect connection status '{actual_result}', should be " \
                                                 f"'{expected_result}'"

    def should_be_select_feature_title(self):
        actual_result = self.get_text(*SebulbaDemoPageLocators.SELECT_FEATURE_TITLE)
        expected_result = "Select feature"
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_select_function_title(self):
        actual_result = self.get_text(*SebulbaDemoPageLocators.SELECT_FUNCTION_TITLE)
        expected_result = "Select function"
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def tap_feature_spinner(self):
        assert self.is_element_present(*SebulbaDemoPageLocators.SELECT_FEATURE_SPINNER), "Select feature spinner not " \
                                                                                         "located"
        self.click_element(*SebulbaDemoPageLocators.SELECT_FEATURE_SPINNER)

    def tap_function_spinner(self):
        assert self.is_element_present(*SebulbaDemoPageLocators.SELECT_FUNCTION_SPINNER), "Select function spinner " \
                                                                                          "not located"
        self.click_element(*SebulbaDemoPageLocators.SELECT_FUNCTION_SPINNER)

    def select_i_fits_molding(self):
        assert self.is_element_present(*SebulbaDemoPageLocators.I_FITS_MOLDING), "IFitsMolding item not found"
        self.click_element(*SebulbaDemoPageLocators.I_FITS_MOLDING)

    def select_set_molding_prep_mode(self):
        assert self.is_element_present(*SebulbaDemoPageLocators.SET_MOLDING_PREP_MODE), "SetMoldingPrepMode item not" \
                                                                                        " found"
        self.click_element(*SebulbaDemoPageLocators.SET_MOLDING_PREP_MODE)

    def should_be_payload_title(self):
        actual_result = self.get_text(*SebulbaDemoPageLocators.PAYLOAD_TITLE)
        expected_result = "Payload: 0x"
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_payload_input(self):
        assert self.is_element_present(*SebulbaDemoPageLocators.PAYLOAD_VALUE), "Payload input not located"

    def input_payload_to_enable_curing_on_both_earbuds(self):
        payload = self.locate_element(*SebulbaDemoPageLocators.PAYLOAD_VALUE)
        payload.send_keys("03")

    def should_be_send_button(self):
        assert self.is_element_present(*SebulbaDemoPageLocators.SEND_BUTTON), "Send button not located"

    def tap_send_button(self):
        self.click_element(*SebulbaDemoPageLocators.SEND_BUTTON)

    def should_be_success_state_after_sending_command(self):
        actual_result = self.get_text(*SebulbaDemoPageLocators.COMMAND_STATE)
        expected_result = "Success"
        assert actual_result == expected_result, f"Incorrect command result state '{actual_result}', should be " \
                                                 f"'{expected_result}'"
