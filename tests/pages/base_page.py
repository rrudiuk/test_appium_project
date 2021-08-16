import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators

from pathlib import Path


class BasePage:

    def __init__(self, driver, timeout=6):
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def background_app_for_5_seconds(self):
        self.driver.background_app(5)

    def check_screen_message(self, expected_result):
        actual_result = self.get_text(*BasePageLocators.SCREEN_MESSAGE)
        assert actual_result == expected_result, f"Incorrect message '{actual_result}', should be '{expected_result}'"

    def check_screen_title(self, expected_result):
        assert self.is_element_present(*BasePageLocators.SCREEN_TITLE), f"Title {expected_result} not found"
        actual_result = self.get_text(*BasePageLocators.SCREEN_TITLE)
        assert actual_result == expected_result, f"Incorrect title '{actual_result}', should be '{expected_result}'"

    def check_screen_subtitle(self, expected_result):
        actual_result = self.get_text(*BasePageLocators.SCREEN_SUBTITLE)
        assert actual_result == expected_result, f"Incorrect subtitle '{actual_result}', should be '{expected_result}'"

    def click_element(self, how, what):
        try:
            self.driver.find_element(how, what).click()
        except NoSuchElementException:
            return False
        return True

    def click_element_10_times(self, how, what):
        try:
            for i in range(12):
                self.driver.find_element(how, what).click()
        except NoSuchElementException:
            return False
        return True

    def count_elements(self, how, what):
        try:
            return len(self.driver.find_elements(how, what))
        except NoSuchElementException:
            return 0

    def get_text_no_encode(self, how, what):

        try:
            text = self.driver.find_element(how, what).text
        except NoSuchElementException:
            return False
        return text

    def get_text(self, how, what, encoding=None):

        try:
            text = self.driver.find_element(how, what).text
        except NoSuchElementException:
            return False
        return text.encode(encoding) if encoding else text

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

    def is_element_enabled(self, how, what):
        try:
            return self.driver.find_element(how, what).is_enabled()
        except NoSuchElementException:
            return False

    def is_element_selected(self, how, what):
        try:
            return self.driver.find_element(how, what).is_selected()
        except NoSuchElementException:
            return False

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

    def should_be_back_arrow(self):
        assert self.is_element_present(*BasePageLocators.BACK_ARROW)

    def swipe_left(self):
        TouchAction(self.driver).press(x=855, y=1215).move_to(x=268, y=1222).release().perform()

    def swipe_left_modified(self):
        TouchAction(self.driver).press(x=900, y=350).move_to(x=150, y=350).release().perform()

    def swipe_right(self):
        TouchAction(self.driver).press(x=218, y=1176).move_to(x=829, y=1176).release().perform()

    def scroll_down(self):
        TouchAction(self.driver).press(x=443, y=1965).move_to(x=436, y=1470).release().perform()

    def take_screenshot(self):
        ts = time.strftime("%Y_%m_%d_%H%M%S")
        path_to_current_directory = Path().absolute()
        path_to_screenshots_folder = str(path_to_current_directory) + '/Screenshots/'
        self.driver.save_screenshot(path_to_screenshots_folder + ts + ".png")

    def tap_back_arrow(self):
        self.click_element(*BasePageLocators.BACK_ARROW)

    def wait_for_connection(self):
        time.sleep(14)
