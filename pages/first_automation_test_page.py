from .base_page import BasePage


class FirstAutomationTestPage(BasePage):
    def test_first_automation_test(self):
        if len(self.driver.find_elements_by_xpath("//*[@text='OK']")) > 0:
            self.driver.find_element_by_xpath("//*[@text='OK']").click()

        # Find location of Elements and perform actions
        self.driver.find_element_by_xpath("//*[@text='Username']").send_keys('company')
        self.driver.find_element_by_xpath("//*[@text='Password']").send_keys('company')
        self.driver.find_element_by_xpath("//*[@text='Login']").click()
