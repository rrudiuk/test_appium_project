from .base_page import BasePage
from .locators import EmailEntryPageLocators


class EmailEntryPage(BasePage):
    def should_be_email_entry_title(self):
        self.check_screen_title("Never Miss A Beat")

    def should_be_correct_email_entry_subtitle(self):
        self.check_screen_subtitle("Stay up to date on firmware updates, giveaways, beta testing opportunities, "
                                   "and more.")

    def should_be_correct_sign_me_button_text(self):
        expected_result = "Sign Me Up"
        actual_result = self.get_text(*EmailEntryPageLocators.SIGN_ME_BUTTON)
        assert actual_result == expected_result, f"Incorrect button text '{actual_result}', should be " \
                                                 f"'{expected_result}'"

    def tap_sign_me_button(self):
        self.click_element(*EmailEntryPageLocators.SIGN_ME_BUTTON)

    def should_be_correct_no_thanks_button_text(self):
        expected_result = "No Thanks"
        actual_result = self.get_text(*EmailEntryPageLocators.NO_THANKS_BUTTON)
        assert actual_result == expected_result, f"Incorrect button text '{actual_result}', " \
                                                 f"should be '{expected_result}'"

    def tap_not_no_thanks_button(self):
        self.click_element(*EmailEntryPageLocators.NO_THANKS_BUTTON)

    def should_be_reason_description(self):
        expected_result = "This can be changed from the Main Menu under Support. Learn more about our Privacy Policy."
        actual_result = self.get_text(*EmailEntryPageLocators.EMAIL_ENTRY_REASON_DESCRIPTION)
        assert actual_result == expected_result, f"Incorrect description text '{actual_result}', " \
                                                 f"should be '{expected_result}'"

    def should_be_email_entry_input(self):
        self.is_element_present(*EmailEntryPageLocators.EMAIL_ENTRY_INPUT), "Email entry input not found"
