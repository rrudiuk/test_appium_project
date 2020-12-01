import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import DialogPage
from .pages.eq_presets_page import EqPresetsPage
from .pages.landing_page import LandingPage
from .pages.home_page import HomePage
from .pages.welcome_page import WelcomePage

import time


@pytest.mark.test
class TestEqPresetsPage:
    def test_click_preset_connected(self, driver):
        analytics_page = AnalyticsPage(driver)
        dialog_page = DialogPage(driver)
        eq_presets_page = EqPresetsPage(driver)
        landing_page = LandingPage(driver)
        home_page = HomePage(driver)
        welcome_page = WelcomePage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_get_started()
        analytics_page.should_be_analytics_title()
        analytics_page.tap_share_analytics_button()
        landing_page.should_be_landing_page_title()
        time.sleep(10)
        dialog_page.should_be_welcome_dialog_title()
        dialog_page.should_be_welcome_dialog_message()
        dialog_page.tap_no_thanks_button()
        home_page.should_be_earbuds_name()
        home_page.should_be_connected_state()
        home_page.should_be_left_earbud_image()
        home_page.should_be_right_earbud_image()
        home_page.should_be_case_image()
        home_page.should_be_eq_expand_icon()
        home_page.should_be_eq_name()
        home_page.should_be_ue_signature_eq_selected()
        home_page.should_be_eq_curve_image()
        home_page.tap_eq_expand_icon()
        home_page.should_be_eq_expand_icon()
        home_page.should_be_eq_name()
        home_page.should_be_ue_signature_eq_selected()
        home_page.should_be_eq_curve_image()
        eq_presets_page.should_be_toolbar()
        eq_presets_page.should_be_customize_button()
        eq_presets_page.should_be_customize_button_text()
        eq_presets_page.should_be_expandable_part()
        eq_presets_page.should_be_divider_line()
        eq_presets_page.should_be_presets_title()
        eq_presets_page.should_be_edit_button()
        eq_presets_page.should_be_edit_button_text()
        eq_presets_page.should_be_add_button()
        eq_presets_page.should_be_presets_list()
        eq_presets_page.should_be_six_presets()
        eq_presets_page.should_be_initial_preset_order()
