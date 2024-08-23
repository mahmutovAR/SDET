from random import choice

import allure
from pytest import fixture

from src.settings import FormFieldsLocators, SUBJECTS


def test_form_fields_locators(set_up: fixture):
    """Tests all available form fields locators."""
    allure.dynamic.feature("Locators")
    allure.dynamic.title("All locators")

    data, driver = set_up
    driver.find_element(*FormFieldsLocators.first_name_field)
    driver.find_element(*FormFieldsLocators.last_name_field)
    driver.find_element(*FormFieldsLocators.email_field)
    driver.find_element(*FormFieldsLocators.gender_male_radiobutton)
    driver.find_element(*FormFieldsLocators.gender_female_radiobutton)
    driver.find_element(*FormFieldsLocators.gender_other_radiobutton)
    driver.find_element(*FormFieldsLocators.mobile_field)
    driver.find_element(*FormFieldsLocators.birth_date_field)
    driver.find_element(*FormFieldsLocators.subjects_field)
    driver.find_element(*FormFieldsLocators.hobby_sports_checkbox)
    driver.find_element(*FormFieldsLocators.hobby_reading_checkbox)
    driver.find_element(*FormFieldsLocators.hobby_music_checkbox)
    driver.find_element(*FormFieldsLocators.picture_file_selector)
    driver.find_element(*FormFieldsLocators.address_field)
    driver.find_element(*FormFieldsLocators.state_selector)
    driver.find_element(*FormFieldsLocators.city_selector)
    driver.find_element(*FormFieldsLocators.submit_button)


def test_valid_subject(set_up: fixture):
    """Tests 'Subjects' field locators if a valid value is entered."""
    allure.dynamic.feature("Locators")
    allure.dynamic.title("Subjects field")

    data, driver = set_up
    subject_field = driver.find_element(*FormFieldsLocators.subjects_field)
    subject_field.send_keys(choice(SUBJECTS))
    driver.find_element(*FormFieldsLocators.subject_is_valid)


def test_calendar(set_up: fixture):
    """Tests if the popup calendar is available."""
    allure.dynamic.feature("Locators")
    allure.dynamic.title("Date of birth field")

    data, driver = set_up
    driver.find_element(*FormFieldsLocators.birth_date_field).click()
    driver.find_element(*FormFieldsLocators.calendar)
