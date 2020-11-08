from selenium.webdriver.common.by import By
# Add your locators below


class BasePageLocators:
    SCREEN_TITLE = (By.ID, "com.logitech.uefits:id/text_view_title")
    SCREEN_SUBTITLE = (By.ID, "com.logitech.uefits:id/text_view_subtitle")


class WelcomePageLocators:
    # WELCOME_SCREEN_TITLE = (By.ID, "com.logitech.uefits:id/text_view_title")
    # WELCOME_SCREEN_SUBTITLE = (By.ID, "com.logitech.uefits:id/text_view_subtitle")
    WELCOME_SCREEN_BUTTON = (By.ID, "com.logitech.uefits:id/button_next")
    WELCOME_SCREEN_EDIT_TEXT_CODE = (By.ID, "com.logitech.uefits:id/edit_text_code")
    WELCOME_SCREEN_BUTTON_SEND_CODE = (By.ID, "com.logitech.uefits:id/button")
    WELCOME_SCREEN_WHERE_IS_MY_CODE = (By.ID, "com.logitech.uefits:id/text_view_help")
    WELCOME_SETUP_CODE_TEXT = (By.ID, "com.logitech.uefits:id/text_view_msg")
    WELCOME_SETUP_SCREEN_CLOSE = (By.ID, "com.logitech.uefits:id/image_view_close")


class AnalyticsPageLocators:
    # ANALYTICS_PAGE_TITLE = (By.ID, "com.logitech.uefits:id/text_view_title")
    # ANALYTICS_SCREEN_SUBTITLE = (By.ID, "com.logitech.uefits:id/text_view_subtitle")
    ANALYTICS_SHARE_BUTTON = (By.ID, "com.logitech.uefits:id/button_main")
    ANALYTICS_NOT_SHARE_BUTTON = (By.ID, "com.logitech.uefits:id/button_secondary")
    ANALYTICS_REASON_DESCRIPTION = (By.ID, "com.logitech.uefits:id/text_view_analytics_reasons")
    ANALYTICS_BACK_ARROW = (By.CLASS_NAME, "android.widget.ImageButton")

