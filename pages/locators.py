from selenium.webdriver.common.by import By
# Add your locators below


class BasePageLocators:
    BACK_ARROW = (By.CLASS_NAME, "android.widget.ImageButton")
    SCREEN_TITLE = (By.ID, "com.logitech.uefits:id/text_view_title")
    SCREEN_SUBTITLE = (By.ID, "com.logitech.uefits:id/text_view_subtitle")
    TOOL_BAR_TITLE = (By.CLASS_NAME, "android.widget.TextView")


class WelcomePageLocators:
    WELCOME_SCREEN_BUTTON = (By.ID, "com.logitech.uefits:id/button_next")
    WELCOME_SCREEN_EDIT_TEXT_CODE = (By.ID, "com.logitech.uefits:id/edit_text_code")
    WELCOME_SCREEN_BUTTON_SEND_CODE = (By.ID, "com.logitech.uefits:id/button")
    WELCOME_SCREEN_WHERE_IS_MY_CODE = (By.ID, "com.logitech.uefits:id/text_view_help")
    WELCOME_SETUP_CODE_TEXT = (By.ID, "com.logitech.uefits:id/text_view_msg")
    WELCOME_SETUP_SCREEN_CLOSE = (By.ID, "com.logitech.uefits:id/image_view_close")


class AnalyticsPageLocators:
    ANALYTICS_SHARE_BUTTON = (By.ID, "com.logitech.uefits:id/button_main")
    ANALYTICS_NOT_SHARE_BUTTON = (By.ID, "com.logitech.uefits:id/button_secondary")
    ANALYTICS_REASON_DESCRIPTION = (By.ID, "com.logitech.uefits:id/text_view_analytics_reasons")


class DemoPageLocators:
    DEMO_APP_VERSION = (By.ID, "com.logitech.uefits:id/text_view_app_version")
    DEMO_LEFT_LABEL = (By.ID, "com.logitech.uefits:id/left_label")
    DEMO_RIGHT_LABEL = (By.ID, "com.logitech.uefits:id/right_label")
    DEMO_LEFT_STATUS = (By.ID, "com.logitech.uefits:id/left_status")
    DEMO_RIGHT_STATUS = (By.ID, "com.logitech.uefits:id/right_status")
