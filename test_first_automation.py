from pages.first_automation_test_page import FirstAutomationTestPage


class TestFirstAutomation:
    def test_first_example(self, driver):
        first_example_test_page = FirstAutomationTestPage(driver)
        first_example_test_page.test_first_automation_test()