import pytest

from .pages.analytics_page import AnalyticsPage
from .pages.dialogs_page import FwUpdateDialogPage
from .pages.email_entry_page import EmailEntryPage
from .pages.firmware_update_page import FirmwareUpdatePage
from .pages.home_page import HomePage
from .pages.menu_page import MenuPage
from .pages.support_page import SupportPage
from .pages.welcome_page import WelcomePage

import time


def initial_setup_non_molding(driver):
    analytics_page = AnalyticsPage(driver)
    dialog_page = FwUpdateDialogPage(driver)
    email_entry_page = EmailEntryPage(driver)
    home_page = HomePage(driver)
    welcome_page = WelcomePage(driver)
    welcome_page.should_be_correct_welcome_title()
    welcome_page.tap_welcome_screen_get_started()
    email_entry_page.should_be_email_entry_title()
    email_entry_page.tap_no_thanks_button()
    analytics_page.tap_share_analytics_button()
    home_page.wait_for_connection()
    dialog_page.check_dialog_and_close_it()
    home_page.should_be_connected_state()


class TestFirmwareUpdatePage:
    def test_firmware_update(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()

    def test_firmware_update1(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()

    def test_firmware_update2(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()

    def test_firmware_update3(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()

    def test_firmware_update4(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()

    def test_firmware_update5(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()

    def test_firmware_update6(self, driver):
        initial_setup_non_molding(driver)
        firmware_update_page = FirmwareUpdatePage(driver)
        home_page = HomePage(driver)
        menu_page = MenuPage(driver)
        support_page = SupportPage(driver)
        home_page.should_be_earbuds_name()
        home_page.should_be_hamburger_menu_icon()
        home_page.tap_hamburger_menu_icon()
        menu_page.tap_support_item()
        support_page.should_be_firmware_item()
        support_page.tap_firmware_item()
        time.sleep(5)
        firmware_update_page.should_be_page_title()
        firmware_update_page.activate_fw_update()
        time.sleep(10)
        firmware_update_page.check_active_update()
