from pages.welcome_page import WelcomePage
from pages.demo_page import DemoPage


class TestDemoPage:
    def test_can_access_demo_screen(self, driver):
        welcome_page = WelcomePage(driver)
        demo_page = DemoPage(driver)
        welcome_page.should_be_correct_welcome_title()
        welcome_page.tap_welcome_screen_10_times()
        welcome_page.should_be_welcome_code_screen_title()
        welcome_page.go_to_demo_screen_code()
        welcome_page.tap_screen_code_get_started()
        demo_page.should_be_correct_toolbar_title()
        demo_page.should_be_left_label()
        demo_page.should_be_right_label()
        demo_page.should_be_left_status()
        demo_page.should_be_right_status()
