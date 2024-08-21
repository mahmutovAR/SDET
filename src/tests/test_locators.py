from random import choice
from time import sleep
# from allure.dynamic import

from bs4 import BeautifulSoup
from pytest import fixture, raises
from selenium.common.exceptions import NoSuchElementException

from src.settings import FormFieldsLocators
from src.settings.generate_data import SUBJECTS
from src.settings.fill_in_form_fields import select_date


def test_form_fields_locators(set_up: fixture):
    # title("Test Locators")
    # description("Tests locators to find all available form fields.")
    # severity(allure.severity_level.CRITICAL)
    """."""
    data, driver = set_up
    driver.get_driver().find_element(*FormFieldsLocators.first_name_field)
    driver.get_driver().find_element(*FormFieldsLocators.last_name_field)
    driver.get_driver().find_element(*FormFieldsLocators.email_field)
    driver.get_driver().find_element(*FormFieldsLocators.gender_male_radiobutton)
    driver.get_driver().find_element(*FormFieldsLocators.gender_female_radiobutton)
    driver.get_driver().find_element(*FormFieldsLocators.gender_other_radiobutton)
    driver.get_driver().find_element(*FormFieldsLocators.mobile_field)
    driver.get_driver().find_element(*FormFieldsLocators.birth_date_field)
    driver.get_driver().find_element(*FormFieldsLocators.subjects_field)
    driver.get_driver().find_element(*FormFieldsLocators.hobby_sports_checkbox)
    driver.get_driver().find_element(*FormFieldsLocators.hobby_reading_checkbox)
    driver.get_driver().find_element(*FormFieldsLocators.hobby_music_checkbox)
    driver.get_driver().find_element(*FormFieldsLocators.picture_file_selector)
    driver.get_driver().find_element(*FormFieldsLocators.address_field)
    driver.get_driver().find_element(*FormFieldsLocators.state_selector)
    driver.get_driver().find_element(*FormFieldsLocators.city_selector)
    driver.get_driver().find_element(*FormFieldsLocators.submit_button)


def test_valid_subject(set_up: fixture):
    data, driver = set_up
    subject_field = driver.get_driver().find_element(*FormFieldsLocators.subjects_field)
    subject_field.send_keys(choice(SUBJECTS))
    driver.get_driver().find_element(*FormFieldsLocators.subject_is_valid)


def test_invalid_subject(set_up: fixture):
    data, driver = set_up
    subject_field = driver.get_driver().find_element(*FormFieldsLocators.subjects_field)
    subject_field.send_keys('123sdf')
    sleep(0.5)
    with raises(NoSuchElementException):
        driver.get_driver().find_element(*FormFieldsLocators.subject_is_valid)


def test_calendar(set_up: fixture):
    data, driver = set_up
    calendar = driver.get_driver().find_element(*FormFieldsLocators.birth_date_field)
    select_date(driver.get_driver(), calendar, ['1964', '04', '12'])

    html = driver.get_driver().page_source
    soup_object = BeautifulSoup(html, "lxml")
    birth_date_html = soup_object.find('input', {'id': 'dateOfBirthInput'})
    assert '12 Apr 1964' == birth_date_html.get('value')
