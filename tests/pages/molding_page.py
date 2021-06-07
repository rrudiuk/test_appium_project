from .base_page import BasePage
from .locators import BasePageLocators
from .locators import MoldingPageLocators


class MoldingPage(BasePage):
    # Try them on screen
    def should_be_try_them_page_title(self):
        self.check_screen_title("Try Them On")

    def should_be_correct_try_them_page_subtitle(self):
        self.check_screen_subtitle("Pop both earbuds into your ears. Gently adjust them until they feel comfortable "
                                   "and secure. You will mold both sides at the same time.")

    def should_be_main_button(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_MAIN)

    def tap_main_button(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)

    # Get ready screen
    def should_be_get_ready_page_title(self):
        self.check_screen_title("Get Ready")

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
        self.check_screen_subtitle("Try standing by a mirror for this part")

    # How is the bass screen
    def should_be_how_is_bass_title(self):
        self.check_screen_title("How’s the Bass?")

    def should_be_correct_how_is_bass_subtitle(self):
        self.check_screen_subtitle("Gently adjust both earbuds until you find the position that maximizes the bass.")

    def should_be_cancel_button(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_CANCEL_BUTTON)

    def should_be_cancel_button_text(self):
        expected_result = "Cancel"
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_CANCEL_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_cancel_button(self):
        self.click_element(*MoldingPageLocators.MOLDING_CANCEL_BUTTON)

    def should_be_image_volume(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_IMAGE_VOLUME)

    def should_be_adjust_volume_bar(self):
        assert self.is_element_present(*MoldingPageLocators.MOLDING_BAR_ADJUST_VOLUME)

    def should_be_starting_soon_title(self):
        expected_result = "Starting Soon"
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_START_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_starting_soon_subtitle1(self):
        expected_result = "During the molding process,\n" \
                          " the tips will feel warm\n" \
                          " as they mold to your ears."
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_START_SUBTITLE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"

    def should_be_starting_soon_subtitle2(self):
        expected_result = "Gently hold your earbuds in place the entire time."
        actual_result = self.get_text(*MoldingPageLocators.MOLDING_START_SUBTITLE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"

    def should_be_progress_bar(self):
        self.is_element_present(*BasePageLocators.PROGRESS_BAR)

    def should_congratulations_title(self):
        self.check_screen_title("Congratulations!")

    def should_congratulations_subtitle(self):
        self.check_screen_subtitle("You now have perfectly fitting earbuds. Throw on your favorite song and take them "
                                   "for a spin.")

    def should_congratulations_subtitle_after_first_molding(self):
        self.check_screen_subtitle("You now have perfectly fitting earbuds.\n\n"
                                   "Take the tour to learn about the features "
                                   "of the app and how to make the most of your UE FITS.")

    def should_be_finish_button(self):
        assert self.is_element_present(*MoldingPageLocators.FINISH_BUTTON)

    def should_be_finish_button_text(self):
        expected_result = "Finish"
        actual_result = self.get_text(*MoldingPageLocators.FINISH_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_finish_button(self):
        self.click_element(*MoldingPageLocators.FINISH_BUTTON)

    def should_be_take_the_tour_button(self):
        assert self.is_element_present(*MoldingPageLocators.TAKE_TOUR_BUTTON)

    def should_be_take_the_tour_button_text(self):
        expected_result = "Take the Tour"
        actual_result = self.get_text(*MoldingPageLocators.TAKE_TOUR_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_take_the_tour_button(self):
        self.click_element(*MoldingPageLocators.TAKE_TOUR_BUTTON)

    def should_skip_for_now_button(self):
        assert self.is_element_present(*MoldingPageLocators.SKIP_FOR_NOW_BUTTON)

    def should_skip_for_now_button_text(self):
        expected_result = "Skip For Now"
        actual_result = self.get_text(*MoldingPageLocators.SKIP_FOR_NOW_BUTTON)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_skip_for_now_button(self):
        self.click_element(*MoldingPageLocators.SKIP_FOR_NOW_BUTTON)


class MoldNewTipsPage(MoldingPage):
    def should_be_menu_icon(self):
        self.is_element_present(*BasePageLocators.MENU_ICON), "Menu icon not found"

    def tap_menu_icon(self):
        self.click_element(*BasePageLocators.MENU_ICON)

    def should_be_scroll_dots(self):
        self.is_element_present(*MoldingPageLocators.SCROLL_ELEMENTS), "Scrolling dots do not appear"

    def should_be_next_button(self):
        assert self.is_element_present(*BasePageLocators.BUTTON_MAIN)

    def should_be_next_button_text(self):
        expected_result = "Next"
        actual_result = self.get_text(*BasePageLocators.BUTTON_MAIN)
        assert actual_result == expected_result, f"Incorrect text '{actual_result}', should be '{expected_result}'"

    def tap_next_button(self):
        self.click_element(*BasePageLocators.BUTTON_MAIN)

    def next_button_enabled(self):
        assert self.is_element_enabled(*BasePageLocators.BUTTON_MAIN), "Next button is not enabled, but it should"

    def next_button_not_enabled(self):
        assert not self.is_element_enabled(*BasePageLocators.BUTTON_MAIN), "Next button is enabled, but it shouldn't"

    def should_be_image_item(self):
        self.is_element_present(*MoldingPageLocators.IMAGE_VIEW), "Image / Animation not located"

    # Change your tips screen
    def should_be_change_tips_title(self):
        self.check_screen_title("Change Your Tips")

    def should_be_change_tips_subtitle(self):
        self.check_screen_subtitle("To remove your current tips, position one finger at the top of the tip and gently "
                                   "peel off.")

    # Remove inserts screen
    def should_be_remove_inserts_title(self):
        self.check_screen_title("Remove Inserts")

    def should_be_remove_inserts_subtitle(self):
        self.check_screen_subtitle("Remove the hard plastic inserts from your new tips by pulling on the insert tab.")

    # Match them up screen
    def should_be_match_them_up_title(self):
        self.check_screen_title("Match Them Up")

    def should_be_match_them_up_subtitle(self):
        self.check_screen_subtitle("Match the tips to the correct earbud. You’ll see an ‘R’ and ‘L’ on the inside of "
                                   "the tips.")

    # Attach your tips screen
    def should_be_attach_your_tips_title(self):
        self.check_screen_title("Attach Your Tips")

    def should_be_attach_your_tips_subtitle(self):
        self.check_screen_subtitle("Insert each earbud into the tip. You won't have to press too hard to attach them.")

    # Check the fit screen
    def should_be_check_the_fit_title(self):
        self.check_screen_title("Check The Fit")

    def should_be_check_the_fit_subtitle(self):
        self.check_screen_subtitle("Make sure the tips are flush with the earbuds.")
