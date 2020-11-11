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
    DEMO_IR_CALIBRATION = (By.ID, "com.logitech.uefits:id/item_ir_calibration")
    DEMO_DEBUG_BUTTON = (By.ID, "com.logitech.uefits:id/item_debug")
    DEMO_IR_SWITCHER_TEXT = (By.ID, "com.logitech.uefits:id/text_view_ir_switcher")
    DEMO_IR_SWITCHER = (By.ID, "com.logitech.uefits:id/switcher_ir")
    DEMO_BATTERY_MONITOR_TEXT = (By.ID, "com.logitech.uefits:id/text_view_battery_monitor")
    DEMO_BATTERY_MONITOR_SWITCHER = (By.ID, "com.logitech.uefits:id/switcher_battery_monitor")
    DEMO_TEST_DATA_MONITOR_TEXT = (By.ID, "com.logitech.uefits:id/text_view_test_data_monitor")
    DEMO_TEST_DATA_MONITOR_SWITCHER = (By.ID, "com.logitech.uefits:id/switcher_test_data_monitor")
    DEMO_LEFT_FW_TITLE = (By.ID, "com.logitech.uefits:id/text_view_left_firmware_title")
    DEMO_LEFT_FW_VALUE = (By.ID, "com.logitech.uefits:id/text_view_left_firmware_value")
    DEMO_RIGHT_FW_TITLE = (By.ID, "com.logitech.uefits:id/text_view_right_firmware_title")
    DEMO_RIGHT_FW_VALUE = (By.ID, "com.logitech.uefits:id/text_view_right_firmware_value")
    DEMO_START_BUTTON = (By.ID, "com.logitech.uefits:id/start")
    DEMO_STATE_BUTTON = (By.ID, "com.logitech.uefits:id/state")
    DEMO_SHARE_BUTTON = (By.ID, "com.logitech.uefits:id/menu_share")
    DEMO_CLEAR_HISTORY_BUTTON = (By.ID, "com.logitech.uefits:id/menu_clear_history")
    DEMO_VENDOR_ID_LABEL = (By.ID, "com.logitech.uefits:id/vendor_id_label")
    DEMO_VENDOR_ID = (By.ID, "com.logitech.uefits:id/vendor_id")
    DEMO_COMMAND_LABEL = (By.ID, "com.logitech.uefits:id/command_id_label")
    # DEMO_COMMAND = (By.ID, "com.logitech.uefits:id/command_id")
    DEMO_COMMAND = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                              ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                              ".FrameLayout/android.view.ViewGroup/android.widget.EditText[2]")
    DEMO_PAYLOAD_LABEL = (By.ID, "com.logitech.uefits:id/payload_label")
    DEMO_PAYLOAD = (By.ID, "com.logitech.uefits:id/payload")
    DEMO_SEND_COMMAND_BUTTON = (By.ID, "com.logitech.uefits:id/send")
    DEMO_LIST_OF_RESPONSES = (By.ID, "com.logitech.uefits:id/toolbar")
    DEMO_FIRST_RESPONSE = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                     ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                     "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget"
                                     ".RecyclerView/android.view.ViewGroup[1]")
    DEMO_SECOND_RESPONSE = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                      ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                      "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                      ".widget.RecyclerView/android.view.ViewGroup[2]")
    DEMO_SENT_COMMAND_FIRST = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                         ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                         "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                         ".widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[4]")
    DEMO_SENT_COMMAND_FIRST_STATUS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                ".widget.FrameLayout/android.widget.FrameLayout/android.view"
                                                ".ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view"
                                                ".ViewGroup[1]/android.widget.TextView[7]")
    DEMO_SENT_COMMAND_SECOND = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                          ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                          "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                          ".widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[4]")
    DEMO_SENT_COMMAND_SECOND_STATUS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                 "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                 ".widget.FrameLayout/android.widget.FrameLayout/android.view"
                                                 ".ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view"
                                                 ".ViewGroup[2]/android.widget.TextView[7]")
    # DEMO_EL = (By.ID, "")
