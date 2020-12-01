from .base_page import BasePage
from .locators import EqPresetsPageLocators

import time

# Presets variables
ue_signature = "UE Signature"
bass_boost = "Bass Boost"
bright = "Bright"
hi_lo_boost = "Hi / Lo Boost"
loudness = "Loudness"
spoken_word = "Spoken Word"


class EqPresetsPage(BasePage):
    def should_be_toolbar(self):
        assert self.is_element_present(*EqPresetsPageLocators.PRESETS_TOOLBAR), "Toolbar is not shown"

    def should_be_customize_button(self):
        assert self.is_element_present(*EqPresetsPageLocators.CUSTOMIZE_BUTTON), "Customize button doesn't appear"

    def should_be_customize_button_text(self):
        expected_result = "Customize"
        actual_result = self.get_text(*EqPresetsPageLocators.CUSTOMIZE_BUTTON)
        assert actual_result == expected_result, f"Incorrect button '{actual_result}', should be '{expected_result}'"

    def tap_customize_button(self):
        self.click_element(*EqPresetsPageLocators.CUSTOMIZE_BUTTON)

    def should_be_expandable_part(self):
        assert self.is_element_present(*EqPresetsPageLocators.EXPANDABLE_BLOCK), "Expandable part doesn't appear"

    def should_not_be_expandable_part(self):
        assert self.is_not_element_present(*EqPresetsPageLocators.EXPANDABLE_BLOCK), "Expandable part still appears"

    def should_be_divider_line(self):
        assert self.is_element_present(*EqPresetsPageLocators.DIVIDER_LINE), "Divider line doesn't appear"

    def should_be_presets_title(self):
        expected_result = "PRESETS"
        actual_result = self.get_text(*EqPresetsPageLocators.PRESETS_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def should_be_edit_button(self):
        assert self.is_element_present(*EqPresetsPageLocators.EDIT_BUTTON), "Customize button doesn't appear"

    def should_be_edit_button_text(self):
        expected_result = "Edit"
        actual_result = self.get_text(*EqPresetsPageLocators.EDIT_BUTTON)
        assert actual_result == expected_result, f"Incorrect button '{actual_result}', should be '{expected_result}'"

    def tap_edit_button(self):
        self.click_element(*EqPresetsPageLocators.EDIT_BUTTON)

    def should_be_add_button(self):
        assert self.is_element_present(*EqPresetsPageLocators.ADD_BUTTON)

    def tap_add_button(self):
        self.click_element(*EqPresetsPageLocators.ADD_BUTTON)

    def should_be_presets_list(self):
        assert self.is_element_present(*EqPresetsPageLocators.PRESETS_RECYCLER_VIEW), "Presets recycler view doesn't " \
                                                                                      "appear "

    def tap_recycler_view_first_element(self):
        presets = self.locate_elements(*EqPresetsPageLocators.PRESET_NAME)
        first_element = presets[1]
        first_element.click()
        time.sleep(3)
        images = self.locate_elements(*EqPresetsPageLocators.PRESET_IMAGE)
        dividers = self.locate_elements(*EqPresetsPageLocators.PRESET_DIVIDER)
        print("number of presets: " + str(len(presets)) + "\n")
        print("number of images: " + str(len(images)) + "\n")
        print("number of dividers: " + str(len(dividers)) + "\n")
        print(first_element.text)

    def should_one_preset(self):
        self.presets_list_view_length(1)

    def should_be_two_presets(self):
        self.presets_list_view_length(2)

    def should_be_three_presets(self):
        self.presets_list_view_length(3)

    def should_be_four_presets(self):
        self.presets_list_view_length(4)

    def should_be_five_presets(self):
        self.presets_list_view_length(5)

    def should_be_six_presets(self):
        self.presets_list_view_length(6)

    def should_be_seven_presets(self):
        self.presets_list_view_length(7)

    def should_be_eight_presets(self):
        self.presets_list_view_length(8)

    def should_be_nine_presets(self):
        self.presets_list_view_length(9)

    def should_be_ten_presets(self):
        self.presets_list_view_length(10)

    def should_be_hundred_presets(self):
        self.presets_list_view_length(100)

    def presets_list_view_length(self, number_of_preset):
        expected_result = number_of_preset
        presets = len(self.locate_elements(*EqPresetsPageLocators.PRESET_NAME))
        images = len(self.locate_elements(*EqPresetsPageLocators.PRESET_IMAGE))
        dividers = len(self.locate_elements(*EqPresetsPageLocators.PRESET_DIVIDER))
        assert presets == expected_result and images == expected_result \
               and dividers == expected_result, f"There are {presets} presets, {images} images and {dividers} " \
                                                f"dividers. Should be {expected_result}"

    def should_be_initial_preset_order(self):
        self.check_preset_order(first_preset=ue_signature, second_preset=bass_boost, third_preset=bright,
                                fourth_preset=hi_lo_boost, fifth_preset=loudness, sixth_preset=spoken_word)

    def check_preset_order(self, first_preset, second_preset, third_preset, fourth_preset, fifth_preset, sixth_preset):
        presets = self.locate_elements(*EqPresetsPageLocators.PRESET_NAME)
        assert presets[0].text == first_preset and presets[1].text == second_preset and \
               presets[2].text == third_preset and presets[3].text == fourth_preset and \
               presets[4].text == fifth_preset and presets[5].text == sixth_preset, \
               f"First preset {first_preset}, should be {presets[0].text}, " \
               f"second preset {second_preset}, should be {presets[1].text}, " \
               f"third preset {third_preset}, should be {presets[2].text}, " \
               f"fourth preset {fourth_preset}, should be {presets[3].text}, " \
               f"fifth preset {fifth_preset}, should be {presets[4].text}, " \
               f"fourth preset {sixth_preset}, should be {presets[5].text}, "
