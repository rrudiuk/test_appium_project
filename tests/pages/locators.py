from selenium.webdriver.common.by import By

APP_PACKAGE_NAME = "com.logitech.uefits"


# Add your locators below


class BasePageLocators:
    BACK_ARROW = (By.CLASS_NAME, "android.widget.ImageButton")
    BUTTON_MAIN = (By.ID, f"{APP_PACKAGE_NAME}:id/button")
    CLOSE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_close")
    MENU_ICON = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                           ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                           ".FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android"
                           ".view.ViewGroup/android.view.ViewGroup/android.widget.ImageButton")
    PROGRESS_BAR = (By.ID, f"{APP_PACKAGE_NAME}:id/progress_bar")
    SAVE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/item_save")
    SCREEN_MESSAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_message")
    SCREEN_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_title")
    SCREEN_SUBTITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_subtitle")
    TOOLBAR_SEPARATOR = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_toolbar")
    TOOLBAR_TITLE = (By.CLASS_NAME, "android.widget.TextView")


class WelcomePageLocators:
    WELCOME_SCREEN_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_next")
    WELCOME_SCREEN_EDIT_TEXT_CODE = (By.ID, f"{APP_PACKAGE_NAME}:id/edit_text_code")
    WELCOME_SCREEN_WHERE_IS_MY_CODE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_help")
    WELCOME_SETUP_CODE_TEXT = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg")
    WELCOME_SETUP_SCREEN_CLOSE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_close")


class AnalyticsPageLocators:
    ANALYTICS_SHARE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_main")
    ANALYTICS_NOT_SHARE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_secondary")
    ANALYTICS_REASON_DESCRIPTION = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_analytics_reasons")


class SebulbaDemoPageLocators:
    CONNECTION_STATUS = (By.ID, f"{APP_PACKAGE_NAME}:id/tv_connection_status")
    SELECT_FEATURE_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/tv_select_feature")
    SELECT_FEATURE_SPINNER = (By.ID, f"{APP_PACKAGE_NAME}:id/spinner_feature")
    SELECT_FUNCTION_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/tv_select_function")
    SELECT_FUNCTION_SPINNER = (By.ID, f"{APP_PACKAGE_NAME}:id/spinner_function")
    PAYLOAD_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/tv_payload_title")
    PAYLOAD_VALUE = (By.ID, f"{APP_PACKAGE_NAME}:id/et_payload_value")
    SEND_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/btn_send")
    I_ROOT = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView'
                        '/android.widget.TextView[1]')
    I_FEATURE_SET = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                               '.ListView/android.widget.TextView[2]')
    I_DEVICE_INFO = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                               '.ListView/android.widget.TextView[3]')
    I_DEVICE_NAME = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                               '.ListView/android.widget.TextView[4]')
    I_BT_HOST_INFO = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                '.ListView/android.widget.TextView[5]')
    I_HEADSET_PARA_EQ = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                   '.ListView/android.widget.TextView[6]')
    I_FITS_MOLDING = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                '.ListView/android.widget.TextView[7]')
    I_FITS_TAP_CONTROL = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                    '.ListView/android.widget.TextView[8]')
    I_FITS_PROXIMITY_DETECTION = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                            '.widget.ListView/android.widget.TextView[9]')
    I_FITS_MOTION_DETECTION = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                         '.widget.ListView/android.widget.TextView[10]')
    GET_MOLDING_PREP_MODE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                       '.widget.ListView/android.widget.TextView[1]')
    SET_MOLDING_PREP_MODE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                       '.widget.ListView/android.widget.TextView[2]')
    START_MOLDING = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                               '.ListView/android.widget.TextView[3]')
    STOP_MOLDING = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                              '.ListView/android.widget.TextView[4]')
    COMMAND_STATE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                               '.view.ViewGroup[1]/android.widget.TextView[11]')


class OhboyDemoPageLocators:
    DEMO_APP_VERSION = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_app_version")
    DEMO_LEFT_LABEL = (By.ID, f"{APP_PACKAGE_NAME}:id/left_label")
    DEMO_RIGHT_LABEL = (By.ID, f"{APP_PACKAGE_NAME}:id/right_label")
    DEMO_LEFT_STATUS = (By.ID, f"{APP_PACKAGE_NAME}:id/left_status")
    DEMO_RIGHT_STATUS = (By.ID, f"{APP_PACKAGE_NAME}:id/right_status")
    DEMO_IR_CALIBRATION = (By.ID, f"{APP_PACKAGE_NAME}:id/item_ir_calibration")
    DEMO_DEBUG_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/item_debug")
    DEMO_IR_SWITCHER_TEXT = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_ir_switcher")
    DEMO_IR_SWITCHER = (By.ID, f"{APP_PACKAGE_NAME}:id/switcher_ir")
    DEMO_BATTERY_MONITOR_TEXT = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_battery_monitor")
    DEMO_BATTERY_MONITOR_SWITCHER = (By.ID, f"{APP_PACKAGE_NAME}:id/switcher_battery_monitor")
    DEMO_TEST_DATA_MONITOR_TEXT = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_test_data_monitor")
    DEMO_TEST_DATA_MONITOR_SWITCHER = (By.ID, f"{APP_PACKAGE_NAME}:id/switcher_test_data_monitor")
    DEMO_LEFT_FW_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_left_firmware_title")
    DEMO_LEFT_FW_VALUE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_left_firmware_value")
    DEMO_RIGHT_FW_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_right_firmware_title")
    DEMO_RIGHT_FW_VALUE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_right_firmware_value")
    DEMO_START_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/start")
    DEMO_STATE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/state")
    DEMO_SHARE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/menu_share")
    DEMO_CLEAR_HISTORY_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/menu_clear_history")
    DEMO_VENDOR_ID_LABEL = (By.ID, f"{APP_PACKAGE_NAME}:id/vendor_id_label")
    # DEMO_VENDOR_ID = (By.ID, f"{APP_PACKAGE_NAME}:id/vendor_id")
    DEMO_VENDOR_ID = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".FrameLayout/android.view.ViewGroup/android.widget.EditText[1]")
    DEMO_COMMAND_LABEL = (By.ID, f"{APP_PACKAGE_NAME}:id/command_id_label")
    # DEMO_COMMAND = (By.ID, f"{APP_PACKAGE_NAME}:id/command_id")
    DEMO_COMMAND = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                              ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                              ".FrameLayout/android.view.ViewGroup/android.widget.EditText[2]")
    DEMO_PAYLOAD_LABEL = (By.ID, f"{APP_PACKAGE_NAME}:id/payload_label")
    # DEMO_PAYLOAD = (By.ID, f"{APP_PACKAGE_NAME}:id/payload")
    DEMO_PAYLOAD = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                              ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                              ".FrameLayout/android.view.ViewGroup/android.widget.EditText[3]")
    DEMO_SEND_COMMAND_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/send")
    DEMO_LIST_OF_RESPONSES = (By.ID, f"{APP_PACKAGE_NAME}:id/toolbar")
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
    DEMO_SENT_COMMAND_FIRST_PAYLOAD = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                 "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                 ".widget.FrameLayout/android.widget.FrameLayout/android.view"
                                                 ".ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view"
                                                 ".ViewGroup[1]/android.widget.TextView[6]")
    DEMO_SENT_COMMAND_SECOND = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                          ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                          "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                          ".widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[4]")
    DEMO_SENT_COMMAND_SECOND_STATUS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                 "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                 ".widget.FrameLayout/android.widget.FrameLayout/android.view"
                                                 ".ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view"
                                                 ".ViewGroup[2]/android.widget.TextView[7]")
    DEMO_SENT_COMMAND_SECOND_PAYLOAD = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                  "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                  ".widget.FrameLayout/android.widget.FrameLayout/android.view"
                                                  ".ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view"
                                                  ".ViewGroup[2]/android.widget.TextView[6]")


class EmailEntryPageLocators:
    SIGN_ME_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_main")
    NO_THANKS_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_secondary")
    EMAIL_ENTRY_REASON_DESCRIPTION = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_analytics_reasons")
    EMAIL_ENTRY_INPUT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                   ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                   ".widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android"
                                   ".widget.FrameLayout/android.widget.EditText")


class LandingPageLocators:
    pass


class MoldingPageLocators:
    MOLDING_TEXT_VIEW_MSG_TITLE1 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_title_1")
    MOLDING_TEXT_VIEW_MSG_TITLE2 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_title_2")
    MOLDING_TEXT_VIEW_MSG_TITLE3 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_title_3")
    MOLDING_TEXT_VIEW_MSG1 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_1")
    MOLDING_TEXT_VIEW_MSG2 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_2")
    MOLDING_TEXT_VIEW_MSG3 = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_msg_3")
    MOLDING_SMILE_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_smile")
    MOLDING_IMAGE_VOLUME = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_volume")
    MOLDING_BAR_ADJUST_VOLUME = (By.ID, f"{APP_PACKAGE_NAME}:id/seek_bar_adjust_volume")
    # MOLDING_CANCEL_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_cancel")
    MOLDING_CANCEL_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_cancel")
    MOLDING_START_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_start_title")
    MOLDING_START_SUBTITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_start_subtitle")
    TAKE_TOUR_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_take_tour")
    SKIP_FOR_NOW_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_skip_tour")
    # Mold new tips
    IMAGE_VIEW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view")
    SCROLL_ELEMENTS = (By.XPATH, "android.widget.HorizontalScrollView/android.widget.LinearLayout")
    # Congratulations
    FINISH_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_finish")


class PairYourEarbudsLocators:
    PAIR_YOUR_EARBUDS_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view")
    BLUETOOTH_SETTINGS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget"
                                    ".TextView")


class DialogPageLocators:
    DIALOG_MESSAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_message")
    DIALOG_ACTION_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_action")
    DIALOG_ADDITIONAL_ACTION_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_additional_action")


class HomePageLocators:
    EARBUDS_NAME = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_name")
    EARBUDS_STATUS = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_status")
    CONNECT_EARBUDS_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_connect")
    HOME_SCREEN_LEFT_MENU = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                       "/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android"
                                       ".widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup["
                                       "1]/android.widget.ImageButton")
    HOME_SCREEN_SETTINGS = (By.ID, f"{APP_PACKAGE_NAME}:id/item_settings")
    LEFT_EARBUD_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_left_earphone")
    RIGHT_EARBUD_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_right_earphone")
    CASE_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_case")
    LEFT_BATTERY_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_left_battery")
    RIGHT_BATTERY_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_right_battery")
    CASE_BATTERY_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_case_battery")
    LEFT_BATTERY_PERCENTS = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_left_percents")
    RIGHT_BATTERY_PERCENTS = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_right_percents")
    CASE_BATTERY_PERCENTS = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_case_percents")


class TutorialHomePageLocators:
    ARROW_TUTORIAL = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_skip_tutorial")
    CUSTOM_EQ_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_custom_eq_title")
    CUSTOM_EQ_MESSAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_custom_eq_message")
    GOT_IT_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_got_it")
    TUTORIAL_CONTAINER = (By.ID, f"{APP_PACKAGE_NAME}:id/container")
    TUTORIAL_MESSAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_message")
    TUTORIAL_NEXT_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_next")
    SKIP_TUTORIAL_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_skip_tutorial")


class EqPresetsPageLocators:
    # Toolbar locators
    TOOLBAR = (By.ID, f"{APP_PACKAGE_NAME}:id/toolbar")
    LEFT_BATTERY_IMAGE_COLLAPSED = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_left_battery_collapsed")
    RIGHT_BATTERY_IMAGE_COLLAPSED = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_right_battery_collapsed")
    CASE_BATTERY_IMAGE_COLLAPSED = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_case_battery_collapsed")
    SAVE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_save")
    # Expandable EQ block locators
    EXPANDABLE_BLOCK = (By.ID, f"{APP_PACKAGE_NAME}:id/group_expandable_part")
    CUSTOMIZE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_customize")
    DIVIDER_LINE = (By.ID, f"{APP_PACKAGE_NAME}:id/separator")
    PRESETS_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_presets")
    EDIT_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_edit")
    ADD_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_add")
    PRESETS_RECYCLER_VIEW = (By.ID, f"{APP_PACKAGE_NAME}:id/recycler_view_presets")
    PRESET_NAME = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view")
    PRESET_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view")
    PRESET_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator")
    EXPAND_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_expand")
    CHOSEN_PRESET_NAME = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_chosen_preset")
    EQ_CURVE_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/equalizer_view")
    # Edit Presets screen locators
    REMOVE_PRESET_ICON = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_remove")
    DRAG_PRESET_ICON = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_drag")
    EDIT_PRESETS_LIST = (By.ID, f"{APP_PACKAGE_NAME}:id/recycler_view")
    # Preset configurator locators
    EQ_EDITOR = (By.ID, f"{APP_PACKAGE_NAME}:id/equalizer_view")
    HISTORY_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_history_title")
    BACKWARD_ARROW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_backward")
    FORWARD_ARROW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_forward")
    PROGRESS_HISTORY_BAR = (By.ID, f"{APP_PACKAGE_NAME}:id/seek_bar_history")


class MenuPageLocators:
    HEADER_CONTAINER = (By.ID, f"{APP_PACKAGE_NAME}:id/navigation_header_container")
    APPLICATION_LOGO = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_logo")
    CLOSE_ICON = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_close")
    HOME_ITEM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                           ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                           ".FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout["
                           "1]/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget"
                           ".LinearLayoutCompat[1]/android.widget.CheckedTextView")
    MOLD_NEW_TIPS_ITEM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                    ".widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget"
                                    ".FrameLayout["
                                    "1]/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget"
                                    ".LinearLayoutCompat[2]/android.widget.CheckedTextView")
    TEST_YOUR_FIT_ITEM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                    ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                    ".widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget"
                                    ".FrameLayout["
                                    "1]/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget"
                                    ".LinearLayoutCompat[3]/android.widget.CheckedTextView")
    USER_GUIDE_ITEM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                 ".FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout["
                                 "1]/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget"
                                 ".LinearLayoutCompat[4]/android.widget.CheckedTextView")
    SUPPORT_ITEM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                              ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                              ".FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout["
                              "1]/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget"
                              ".LinearLayoutCompat["
                              "5]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView")
    EMAIL_ENTRY_ITEM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                  ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                  ".FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout["
                                  "1]/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget"
                                  ".LinearLayoutCompat[6]/android.widget.CheckedTextView")
    TAKE_SELFIE_ITEM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                  ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                  ".FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout["
                                  "1]/androidx.recyclerview.widget.RecyclerView/androidx.appcompat.widget"
                                  ".LinearLayoutCompat["
                                  "7]/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView")


class SupportPageLocators:
    FIRMWARE_ITEM = (By.ID, f"{APP_PACKAGE_NAME}:id/view_firmware_clickable")


class FirmwareUpdatePageLocators:
    ALL_SET_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_completed_title")
    ERROR_OCCURRED_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_error_title")
    ERROR_OCCURRED_SUBTITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_error_subtitle")
    ERROR_OCCURRED_INSTALL_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_install_now")
    ERROR_OCCURRED_CANCEL_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_cancel")
    UPDATE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_update")
    UPDATE_PROGRESS_BAR = (By.ID, f"{APP_PACKAGE_NAME}:id/progress_bar_updating")
    INSTALLING_TITLE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                  '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                  '.FrameLayout/android.view.ViewGroup/android.widget.TextView[1]')
    ROLLBACK_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_rollback")


class LearnMoreLocators:
    CAROUSEL_CONTROLS = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                   ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                   ".widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget"
                                   ".FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android"
                                   ".widget.LinearLayout")
    NOTICE_MESSAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_message_2")
    SCREEN_VIDEO = (By.ID, f"{APP_PACKAGE_NAME}:id/exo_subtitles")
    SCREEN_IMAGE = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                              ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                              ".FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx"
                              ".recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.view.ViewGroup"
                              "/android.view.ViewGroup")


class UGCPageLocators:
    TAKE_SELFIE_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_main")
    SKIP_FOR_NOW_BUTTON = (By.ID, f"{APP_PACKAGE_NAME}:id/button_secondary")
    IMAGE_COLLAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_collage")
    UGC_GIF = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                         ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                         ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup"
                         "/android.widget.FrameLayout/android.widget.FrameLayout["
                         "1]/android.widget.FrameLayout/android.view.View")


class UserGuidePageLocators:
    # Pairing
    PAIRING_ARROW = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                               '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                               '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                               '1]/android.widget.ImageView')
    PAIRING_DIVIDER = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                 '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                 '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                 '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                 '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                                 '1]/android.view.View')
    PAIRING_ITEM = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                              '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                              '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx'
                              '.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView')
    PAIRING_TEXT1 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                               '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                               '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]')
    PAIRING_TEXT2 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                               '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                               '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[2]')
    PAIRING_CASE_IMAGE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                    '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                                    '.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget'
                                    '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                    '.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout'
                                    '/android.widget.ImageView')
    OHBOY_PAIRING_WATCH_VIDEO = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                           '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                           '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                           '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                           '.widget.RecyclerView/android.widget.TextView[3]')
    OHBOY_PAIRING_VIDEO = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                     '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                     '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                     '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                     '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view'
                                     '.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout['
                                     '3]/android.widget.FrameLayout/android.view.View')
    OHBOY_PAIRING_ONE_NOT_CONNECTED = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                 '.widget.FrameLayout/android.widget.FrameLayout/androidx'
                                                 '.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                                 '/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                                 '.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget'
                                                 '.TextView[2]')
    SEBULBA_PAIRING_SELECT_UE_FITS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                '.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout'
                                                '.widget.DrawerLayout/android.widget.FrameLayout/android.widget'
                                                '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                                '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView')
    SEBULBA_PAIRING_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_phone")
    # Molding
    MOLDING_ARROW = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                               '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                               '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                               '2]/android.widget.ImageView')
    MOLDING_DIVIDER = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                 '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                 '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                 '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                 '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                                 '2]/android.view.View')
    MOLDING_ITEM = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                              '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                              '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                              '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx'
                              '.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView')
    MOLDING_A_FEW_THINGS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                      '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                      '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                      '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                      '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                      '.widget.TextView[1]')
    MOLDING_SOUND_TEST = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                    '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                                    '.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget'
                                    '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                    '.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[2]')
    MOLDING_ADJUST_BOTH_EARBUDS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                             '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                             '/android.widget.FrameLayout/android.view.ViewGroup/androidx'
                                             '.recyclerview.widget.RecyclerView/android.widget.TextView[3]')
    MOLDING_APPLY_GENTLE_PRESSURE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                               '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                               '.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout'
                                               '.widget.DrawerLayout/android.widget.FrameLayout/android.widget'
                                               '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                               '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[4]')
    MOLDING_AFTER_SOUND_TEST = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                          '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                          '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                          '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                          '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                          '.RecyclerView/android.widget.TextView[5]')
    MOLDING_MIX_AMD_MATCH = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                       '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                       '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                       '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                       '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                       '.widget.TextView[6]')
    MOLDING_SEVERAL_PAIRS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                       '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                       '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                       '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                       '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                       '.widget.TextView[7]')
    MOLDING_CLICK_ON_APP_MENU = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                           '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                           '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                           '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                           '.widget.RecyclerView/android.widget.TextView[8]')
    # Controls
    CONTROLS_ARROW = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                                '3]/android.widget.ImageView')
    CONTROLS_DIVIDER = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                  '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                  '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                  '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                  '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                                  '3]/android.view.View')
    CONTROLS_ITEM = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                               '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                               '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                               '3]/android.widget.TextView')
    CONTROLS_DOUBLE_AND_SINGLE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                            '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                            '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                            '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                            '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                            '.widget.RecyclerView/android.widget.TextView[1]')
    CONTROLS_EACH_FITS_EARBUD = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                           '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                           '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                           '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                           '.widget.RecyclerView/android.widget.TextView[2]')
    CONTROLS_PHONE_CALL = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                     '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                     '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                     '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                     '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                     '.widget.TextView[3]')
    CONTROLS_ENABLE_SINGLE_TAP = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                            '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                            '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                            '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                            '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                            '.widget.RecyclerView/android.widget.TextView[4]')
    CONTROLS_TO_USE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                 '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                 '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                 '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                 '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[5]')
    CONTROLS_HOW_TO_USE_IMAGE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                           '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                           '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                           '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                           '.widget.RecyclerView/android.widget.FrameLayout['
                                           '1]/android.widget.ImageView')
    CONTROLS_CUSTOMIZATION = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                        '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                        '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                        '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                        '.RecyclerView/android.widget.TextView[6]')
    CONTROLS_EACH_EARBUD = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                      '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                      '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                      '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                      '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                      '.widget.TextView[7]')
    CONTROLS_ACCESS_SETTINGS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                          '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                          '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                          '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                          '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                          '.RecyclerView/android.widget.FrameLayout[2]/android.widget.ImageView')
    # Connectivity and switching
    CONNECTIVITY_AND_SWITCHING_ARROW = (By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                        '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                        '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                        '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                        '.RecyclerView/android.view.ViewGroup[4]/android.widget.ImageView')
    CONNECTIVITY_AND_SWITCHING_DIVIDER = (By.XPATH,
                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                          '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                          '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                          '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                          '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                          '.RecyclerView/android.view.ViewGroup[4]/android.view.View')
    CONNECTIVITY_AND_SWITCHING_ITEM = (By.XPATH,
                                       '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                       '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                       '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                       '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                       '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                       '.view.ViewGroup[4]/android.widget.TextView')
    CONNECTIVITY_AND_SWITCHING_TITLE = (By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                        '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                        '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                        '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                        '.RecyclerView/android.widget.TextView[1]')
    CONNECTIVITY_AND_SWITCHING_IMAGE = (By.XPATH,
                                        '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                        '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                        '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                        '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                        '.RecyclerView/android.widget.FrameLayout/android.widget.ImageView')
    CONNECTIVITY_AND_SWITCHING_FIRST_ENSURE = (By.XPATH,
                                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                               '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                               '.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout'
                                               '.widget.DrawerLayout/android.widget.FrameLayout/android.widget'
                                               '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                               '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[2]')
    CONNECTIVITY_AND_SWITCHING_YOU_CAN_SWITCH = (By.XPATH,
                                                 '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                 '.widget.FrameLayout/android.widget.FrameLayout/androidx'
                                                 '.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                                 '/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                                 '.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget'
                                                 '.TextView[3]')
    CONNECTIVITY_AND_SWITCHING_CASE_INTERACTIONS = (By.XPATH,
                                                    '/hierarchy/android.widget.FrameLayout/android.widget'
                                                    '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                    '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                    '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                                    '.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                                    '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                                    '.RecyclerView/android.widget.TextView[4]')
    CONNECTIVITY_AND_SWITCHING_IN_CASE = (By.XPATH,
                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                          '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                          '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                          '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                          '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                          '.RecyclerView/android.widget.TextView[5]')
    CONNECTIVITY_AND_SWITCHING_AUTO_CONNECTION = (By.XPATH,
                                                  '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                  '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                  '.widget.FrameLayout/android.widget.FrameLayout/androidx'
                                                  '.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                                  '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                  '.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                                  '.widget.TextView[5]')
    CONNECTIVITY_AND_SWITCHING_USING_SINGLE_EARBUD = (By.XPATH,
                                                      '/hierarchy/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                      '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                                      '.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                                      '.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                                      '.widget.RecyclerView/android.widget.TextView[6]')
    CONNECTIVITY_AND_SWITCHING_TO_USE_SINGLE = (By.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                '.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout'
                                                '.widget.DrawerLayout/android.widget.FrameLayout/android.widget'
                                                '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                                '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView['
                                                '7]')
    CONNECTIVITY_AND_SWITCHING_STANDBY = (By.XPATH,
                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                          '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                          '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                          '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                          '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                          '.RecyclerView/android.widget.TextView[8]')
    CONNECTIVITY_AND_SWITCHING_AFTER_60 = (By.XPATH,
                                           '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                           '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                           '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                           '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                           '.widget.RecyclerView/android.widget.TextView[9]')
    CONNECTIVITY_AND_SWITCHING_TO_WAKE = (By.XPATH,
                                          '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                          '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                          '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                          '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                          '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                          '.RecyclerView/android.widget.TextView[6]')
    CONNECTIVITY_AND_SWITCHING_TO_APP = (By.XPATH,
                                         '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                         '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                         '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                         '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                         '.RecyclerView/android.widget.TextView[7]')
    CONNECTIVITY_AND_SWITCHING_WILL_CONNECT = (By.XPATH,
                                               '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                               '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                               '.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout'
                                               '.widget.DrawerLayout/android.widget.FrameLayout/android.widget'
                                               '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                               '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[8]')
    CONNECTIVITY_AND_SWITCHING_SECOND_DEVICE = (By.XPATH,
                                                '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                '.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout'
                                                '.widget.DrawerLayout/android.widget.FrameLayout/android.widget'
                                                '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                                '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView['
                                                '9]')
    CONNECTIVITY_AND_SWITCHING_APP_WILL_DISPLAY = (By.XPATH,
                                                   '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                   '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                   '.widget.FrameLayout/android.widget.FrameLayout/androidx'
                                                   '.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                                   '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                   '.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                                   '.widget.TextView[9]')
    # Charging
    CHARGING_ARROW = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                                '5]/android.widget.ImageView')
    CHARGING_DIVIDER = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                  '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                  '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                  '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                  '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                                  '5]/android.view.View')
    CHARGING_ITEM = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                               '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                               '/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                               '5]/android.widget.TextView')
    CHARGING_YOUR_DEVICE_TITLE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                            '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                            '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                            '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                            '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                            '.widget.RecyclerView/android.widget.TextView[1]')
    CHARGING_UE_FITS_WILL_SUPPORT = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                               '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                               '.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout'
                                               '.widget.DrawerLayout/android.widget.FrameLayout/android.widget'
                                               '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                               '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[2]')
    CHARGING_USB_C_CABLE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                      '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                      '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                      '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                      '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                      '.widget.TextView[3]')
    CHARGING_LED_INTERACTIONS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                           '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                           '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                           '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                           '.widget.RecyclerView/android.widget.TextView[4]')
    CHARGING_INDICATION_TABLE = (By.ID, f"{APP_PACKAGE_NAME}:id/view_container")
    # Adjusting EQ
    ADJUSTING_EQ_ARROW = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                    '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                                    '.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget'
                                    '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                    '.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                                    '6]/android.widget.ImageView')
    ADJUSTING_EQ_DIVIDER = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                      '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                      '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                      '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                      '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view'
                                      '.ViewGroup[6]/android.view.View')
    ADJUSTING_EQ_ITEM = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                   '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android'
                                   '.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget'
                                   '.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                   '.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup['
                                   '6]/android.widget.TextView')
    ADJUSTING_EQ_TO_ACCESS = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                        '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                        '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                        '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                        '.RecyclerView/android.widget.TextView[1]')
    ADJUSTING_EQ_TO_CHANGE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                        '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                        '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                        '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                        '.RecyclerView/android.widget.TextView[2]')
    ADJUSTING_EQ_TO_CREATE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                        '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                        '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                        '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                        '.RecyclerView/android.widget.TextView[3]')
    ADJUSTING_EQ_IMAGE = (By.ID, f"{APP_PACKAGE_NAME}:id/view_container")
    # TYF
    TYF_ARROW = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                           '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                           '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android'
                           '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx'
                           '.recyclerview.widget.RecyclerView/android.view.ViewGroup[7]/android.widget.ImageView')
    TYF_DIVIDER = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                             '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                             '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                             '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx'
                             '.recyclerview.widget.RecyclerView/android.view.ViewGroup[7]/android.view.View')
    TYF_ITEM = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                          '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                          '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android'
                          '.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx'
                          '.recyclerview.widget.RecyclerView/android.view.ViewGroup[7]/android.widget.TextView')
    TYF_GREAT_FIT = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                               '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                               '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                               '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                               '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[1]')
    TYF_BY_ANSWERING = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                  '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                  '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                  '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                  '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[2]')
    TYF_WHEN_USING = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                '.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget'
                                '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                '/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[3]')
    # Updating Firmware
    UPDATING_FIRMWARE_ARROW = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                         '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                         '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                         '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                         '.RecyclerView/android.view.ViewGroup[8]/android.widget.ImageView')
    UPDATING_FIRMWARE_DIVIDER = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                           '.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                           '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                           '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                           '/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview'
                                           '.widget.RecyclerView/android.view.ViewGroup[8]/android.view.View')
    UPDATING_FIRMWARE_ITEM = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                        '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                        '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                        '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                        '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                        '.RecyclerView/android.view.ViewGroup[8]/android.widget.TextView')
    UPDATING_FIRMWARE_IF_FW_UPDATE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                '.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout'
                                                '.widget.DrawerLayout/android.widget.FrameLayout/android.widget'
                                                '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                                '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView['
                                                '1]')
    UPDATING_FIRMWARE_UPDATES_CAN = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                               '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                               '.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout'
                                               '.widget.DrawerLayout/android.widget.FrameLayout/android.widget'
                                               '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                               '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[2]')
    UPDATING_FIRMWARE_TO_COMPLETE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                               '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                               '.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout'
                                               '.widget.DrawerLayout/android.widget.FrameLayout/android.widget'
                                               '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                               '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView[3]')
    UPDATING_FIRMWARE_MOST_UPDATES = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                '.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout'
                                                '.widget.DrawerLayout/android.widget.FrameLayout/android.widget'
                                                '.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup'
                                                '/androidx.recyclerview.widget.RecyclerView/android.widget.TextView['
                                                '4]')
    # Troubleshooting
    TROUBLESHOOTING_ARROW = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                       '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                       '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                       '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                       '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                       '.view.ViewGroup[9]/android.widget.ImageView')
    TROUBLESHOOTING_DIVIDER = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                         '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                         '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                         '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                         '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                         '.RecyclerView/android.view.ViewGroup[9]/android.view.View')
    TROUBLESHOOTING_ITEM = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                      '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                      '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android'
                                      '.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                      '/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view'
                                      '.ViewGroup[9]/android.widget.TextView')
    TROUBLESHOOTING_FIRST_ACTION = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                              '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                              '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                              '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                              '/android.widget.FrameLayout/android.view.ViewGroup/androidx'
                                              '.recyclerview.widget.RecyclerView/android.widget.TextView[1]')
    TROUBLESHOOTING_CONNECTING_ISSUES = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                   '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                   '.widget.FrameLayout/android.widget.FrameLayout/androidx'
                                                   '.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                                   '/android.widget.FrameLayout/android.widget.FrameLayout/android'
                                                   '.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android'
                                                   '.widget.TextView[2]')
    TROUBLESHOOTING_IF_YOU_HAVE_CONNECTING_ISSUES = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                               '.LinearLayout/android.widget.FrameLayout/android'
                                                               '.widget.LinearLayout/android.widget.FrameLayout'
                                                               '/android.widget.FrameLayout/androidx.drawerlayout'
                                                               '.widget.DrawerLayout/android.widget.FrameLayout'
                                                               '/android.widget.FrameLayout/android.widget'
                                                               '.FrameLayout/android.view.ViewGroup/androidx'
                                                               '.recyclerview.widget.RecyclerView/android.widget'
                                                               '.TextView[3]')
    TROUBLESHOOTING_TO_RESET = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                          '.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout'
                                          '/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                          '/android.widget.FrameLayout/android.widget.FrameLayout/android.widget'
                                          '.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget'
                                          '.RecyclerView/android.widget.TextView[4]')
    TROUBLESHOOTING_CONNECTING_ISSUES_NOTE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                        '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                        '/android.widget.FrameLayout/android.widget.FrameLayout'
                                                        '/android.widget.FrameLayout/android.view.ViewGroup/androidx'
                                                        '.recyclerview.widget.RecyclerView/android.widget.TextView[5]')
    TROUBLESHOOTING_CONNECTING_ISSUES_STANDBY = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget'
                                                           '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                           '.LinearLayout/android.widget.FrameLayout/android.widget'
                                                           '.FrameLayout/androidx.drawerlayout.widget.DrawerLayout'
                                                           '/android.widget.FrameLayout/android.widget.FrameLayout'
                                                           '/android.widget.FrameLayout/android.view.ViewGroup'
                                                           '/androidx.recyclerview.widget.RecyclerView/android.widget'
                                                           '.TextView[6]')
    TROUBLESHOOTING_CHARGING_ISSUES = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                                 '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                                                 '.widget.FrameLayout/android.widget.FrameLayout/androidx'
                                                 '.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout'
                                                 '/android.widget.FrameLayout/android.widget.FrameLayout/android.view'
                                                 '.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget'
                                                 '.TextView[7]')
    TROUBLESHOOTING_NOT_CHARGING = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                              '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                              '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                              '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                              '/android.widget.FrameLayout/android.view.ViewGroup/androidx'
                                              '.recyclerview.widget.RecyclerView/android.widget.TextView[7]')
    TROUBLESHOOTING_IF_CONTINUE = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
                                             '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                             '.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget'
                                             '.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout'
                                             '/android.widget.FrameLayout/android.view.ViewGroup/androidx'
                                             '.recyclerview.widget.RecyclerView/android.widget.TextView[8]')


class SettingsPageLocators:
    CHECK_MARK = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_selected")
    # NAME
    NAME_ITEM = (By.ID, f"{APP_PACKAGE_NAME}:id/view_name_clickable")
    NAME_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_name_hint")
    NAME_VALUE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_name")
    NAME_ACTION_ARROW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_name_action")
    NAME_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_name")
    # Edit name
    EDIT_NAME_INPUT = (By.ID, f"{APP_PACKAGE_NAME}:id/edit_text_name")
    EDIT_NAME_INPUT_CLEAR = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_clear")
    EDIT_NAME_MAX = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_max_name")
    EDIT_NAME_HINT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".FrameLayout/android.view.ViewGroup/android.widget.TextView[4]")
    # SINGLE TAP
    SINGLE_TAP_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_tap_title")
    SINGLE_TAP_STATUS_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_tap_status_title")
    SINGLE_TAP_SWITCHER = (By.ID, f"{APP_PACKAGE_NAME}:id/switcher_tap")
    SINGLE_TAP_STATUS_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_tap_status")
    # single tap left
    SINGLE_TAP_LEFT_ITEM = (By.ID, f"{APP_PACKAGE_NAME}:id/view_left_tap_clickable")
    SINGLE_TAP_LEFT_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_tap_left_hint")
    SINGLE_TAP_LEFT_STATE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_tap_left_tap")
    SINGLE_TAP_LEFT_ACTION_ARROW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_left_tap_action")
    SINGLE_TAP_LEFT_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_left_tap")
    # single tap right
    SINGLE_TAP_RIGHT_ITEM = (By.ID, f"{APP_PACKAGE_NAME}:id/view_right_tap_clickable")
    SINGLE_TAP_RIGHT_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_tap_right_hint")
    SINGLE_TAP_RIGHT_STATE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_right_tap")
    SINGLE_TAP_RIGHT_ACTION_ARROW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_right_tap_action")
    SINGLE_TAP_RIGHT_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_right_tap")
    # single tap items
    SINGLE_TAP_PLAY_PAUSE = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                       "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                       ".widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView")
    SINGLE_TAP_NEXT_TRACK = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                       "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                       ".widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
    SINGLE_TAP_PREVIOUS_TRACK = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                           ".widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                           ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx"
                                           ".recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                           "3]/android.widget.TextView")
    SINGLE_TAP_VOLUME_UP = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                      ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                      "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                      ".widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView")
    SINGLE_TAP_VOLUME_DOWN = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                        ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                        "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                        ".widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView")
    # DOUBLE TAP
    DOUBLE_TAP_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_double_tap_title")
    DOUBLE_TAP_STATUS_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_double_tap_status_title")
    DOUBLE_TAP_SWITCHER = (By.ID, f"{APP_PACKAGE_NAME}:id/switcher_double_tap")
    DOUBLE_TAP_STATUS_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_double_tap_status")
    DOUBLE_TAP_LEFT_ITEM = (By.ID, f"{APP_PACKAGE_NAME}:id/view_left_double_tap_clickable")
    DOUBLE_TAP_LEFT_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_double_tap_left_hint")
    DOUBLE_TAP_LEFT_STATE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_double_tap_left_tap")
    DOUBLE_TAP_LEFT_ACTION_ARROW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_left_double_tap_action")
    DOUBLE_TAP_LEFT_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_left_double_tap")
    DOUBLE_TAP_RIGHT_ITEM = (By.ID, f"{APP_PACKAGE_NAME}:id/view_right_double_tap_clickable")
    DOUBLE_TAP_RIGHT_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_double_tap_right_hint")
    DOUBLE_TAP_RIGHT_STATE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_right_double_tap")
    DOUBLE_TAP_RIGHT_ACTION_ARROW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_right_double_tap_action")
    DOUBLE_TAP_RIGHT_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_right_double_tap")
    # double tap items
    DOUBLE_TAP_GOOGLE_ASSISTANCE = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                              "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                              ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup"
                                              "/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                              "1]/android.widget.TextView")
    DOUBLE_TAP_PLAY_PAUSE = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                       "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                       ".widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
    DOUBLE_TAP_NEXT_TRACK = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                       "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                       ".widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView")
    DOUBLE_TAP_PREVIOUS_TRACK = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                           ".widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                           ".FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx"
                                           ".recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                           "4]/android.widget.TextView")
    DOUBLE_TAP_VOLUME_UP = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                      ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                      "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                      ".widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView")
    DOUBLE_TAP_VOLUME_DOWN = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                        ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                        "/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview"
                                        ".widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView")
    # DARK MODE
    DARK_MODE_ITEM = (By.ID, f"{APP_PACKAGE_NAME}:id/view_dark_mode_clickable")
    DARK_MODE_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_dark_mode_hint")
    DARK_MODE_VALUE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_dark_mode")
    DARK_MODE_ACTION_ARROW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_dark_mode_action")
    DARK_MODE_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_dark_mode")
    DARK_MODE_SWITCHER_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_dark_mode")
    DARK_MODE_SWITCHER = (By.ID, f"{APP_PACKAGE_NAME}:id/switcher_dark_mode")
    DARK_MODE_SWITCHER_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_dark_mode")
    DARK_MODE_DEVICE_DEFAULT_SWITCHER_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_auto_settings")
    DARK_MODE_DEVICE_DEFAULT_SWITCHER = (By.ID, f"{APP_PACKAGE_NAME}:id/switcher_auto_settings")
    DARK_MODE_DEVICE_DEFAULT_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_auto_settings")
    DARK_MODE_HINT = (By.XPATH, "hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".FrameLayout/android.view.ViewGroup/android.widget.TextView[4]")
    # LANGUAGE
    LANGUAGE_ITEM = (By.ID, f"{APP_PACKAGE_NAME}:id/view_language_clickable")
    LANGUAGE_TITLE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_language_hint")
    LANGUAGE_VALUE = (By.ID, f"{APP_PACKAGE_NAME}:id/text_view_language")
    LANGUAGE_ACTION_ARROW = (By.ID, f"{APP_PACKAGE_NAME}:id/image_view_language_action")
    LANGUAGE_DIVIDER = (By.ID, f"{APP_PACKAGE_NAME}:id/separator_language")
    # language items
    SYSTEM_DEFAULT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView")
    DEUTSCH = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView")
    ENGLISH = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView")
    SPANISH = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView")
    FRENCH = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView")
    ITALIAN = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView")
