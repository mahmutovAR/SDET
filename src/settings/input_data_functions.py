from os import getcwd
from os.path import join as os_path_join

from selenium.webdriver.common.keys import Keys


def input_data(locator, data):
    locator.send_keys(data)


def input_data_and_press_enter(locator, data):
    locator.send_keys(data)
    locator.send_keys(Keys.ENTER)


def remove_default_value_and_input_data(locator, data):
    locator.send_keys(Keys.CONTROL, "a")
    locator.send_keys(data)
    locator.send_keys(Keys.ENTER)


def select_option(driver, locator):
    js_scroll_code = "arguments[0].scrollIntoView();"
    driver.execute_script(js_scroll_code, locator)
    locator.click()


def upload_file(locator, path):
    locator.send_keys(os_path_join(getcwd(), 'pictures', path))


def press_submit_button(locator):
    locator.submit()
