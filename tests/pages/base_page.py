from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators


class BasePage:

    def __init__(self, driver, timeout=6):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def background_app_for_10_seconds(self):
        self.driver.background_app(10)

    def click_element(self, how, what):
        try:
            self.driver.find_element(how, what).click()
        except NoSuchElementException:
            return False
        return True

    def click_element_10_times(self, how, what):
        try:
            for i in range(10):
                self.driver.find_element(how, what).click()
        except NoSuchElementException:
            return False
        return True

    def count_elements(self, how, what):
        try:
            return len(self.driver.find_elements(how, what))
        except NoSuchElementException:
            return 0

    def locate_element(self, how, what):
        try:
            return self.driver.find_element(how, what)
        except NoSuchElementException:
            return False

    def locate_elements(self, how, what):
        try:
            return self.driver.find_elements(how, what)
        except NoSuchElementException:
            return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def get_text(self, how, what, encoding=None):

        try:
            text = self.driver.find_element(how, what).text
        except NoSuchElementException:
            return False
        return text.encode(encoding) if encoding else text

    def should_be_back_arrow(self):
        assert self.is_element_present(*BasePageLocators.BACK_ARROW)

    def tap_back_arrow(self):
        self.click_element(*BasePageLocators.BACK_ARROW)

    def check_screen_title(self, expected_result):
        actual_result = self.get_text(*BasePageLocators.SCREEN_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def check_screen_subtitle(self, expected_result):
        actual_result = self.get_text(*BasePageLocators.SCREEN_SUBTITLE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"