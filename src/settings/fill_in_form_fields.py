from os import getcwd
from os.path import join as os_path_join

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

from .locators import FormFieldsLocators, get_year_selector, get_month_selector, get_day_selector


def fill_in_text_field(locator: WebElement, data: str) -> None:
    """Fills the specified form field with data."""
    locator.send_keys(data)


def enter_and_select_state_city(locator: WebElement, data: str) -> None:
    """Selects one of the available values by entering text data."""
    locator.send_keys(data)
    locator.send_keys(Keys.ENTER)


def enter_and_select_subject(driver: webdriver, locator: WebElement, data: str) -> None:
    """Fills 'Subjects' field by checking for a valid value."""
    locator.send_keys(data)
    WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element_value(FormFieldsLocators.subjects_field, data))
    try:
        driver.find_element(*FormFieldsLocators.subject_is_valid)
    except NoSuchElementException:
        locator.send_keys(Keys.ESCAPE)
    else:
        locator.send_keys(Keys.ENTER)


def select_date(driver: webdriver, locator: WebElement, input_date: list) -> None:
    """Selects a date using a pop-up calendar."""
    b_year, b_month, b_day = input_date
    b_month_value = str(int(b_month) - 1)
    b_day = int(b_day)
    if b_day < 10:
        b_day_value = f'00{b_day}'
    else:
        b_day_value = f'0{b_day}'

    locator.click()
    select_year = Select(driver.find_element(*get_year_selector()))
    select_month = Select(driver.find_element(*get_month_selector()))
    select_year.select_by_value(b_year)
    select_month.select_by_value(b_month_value)
    b_day = driver.find_element(*get_day_selector(b_day_value))
    b_day.click()


def enter_date(locator: WebElement, input_date: str | list) -> None:
    """Fills the date field with a string value."""
    locator.send_keys(Keys.CONTROL, "a")
    locator.send_keys(input_date)
    locator.send_keys(Keys.ENTER)


def select_option(driver: webdriver, locator: WebElement) -> None:
    """Scrolls to the specified field and selects an option."""
    js_scroll_code = "arguments[0].scrollIntoView();"
    driver.execute_script(js_scroll_code, locator)
    locator.click()


def upload_file(locator: WebElement, path: str) -> None:
    """Uploads file."""
    locator.send_keys(os_path_join(getcwd(), 'pictures', path))


def push_submit_button(locator: WebElement) -> None:
    """Submits the form"""
    locator.submit()
