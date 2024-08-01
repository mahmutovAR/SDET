from selenium.webdriver.common.keys import Keys
from os.path import join as os_path_join
from os import getcwd


import web_driver


def input_data(locator, data):
    locator.send_keys(data)


def input_data_and_press_enter(locator, data):
    locator.send_keys(data)
    locator.send_keys(Keys.ENTER)


def remove_default_value_and_input_data(locator, data):
    locator.send_keys(Keys.CONTROL, "a")
    locator.send_keys(data)
    locator.send_keys(Keys.ENTER)


def select_option(locator):
    web_driver.scroll_to_element(locator)
    locator.click()


def upload_file(locator, path):
    locator.send_keys(os_path_join(getcwd(), 'pictures', path))


def press_submit_button(locator):
    locator.submit()
