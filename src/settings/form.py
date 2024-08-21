from os.path import isfile, normpath

from selenium import webdriver

from .fill_in_form_fields import (fill_in_text_field, enter_and_select_state_city,
                                  enter_and_select_subject, select_date,
                                  enter_date,
                                  select_option, upload_file, push_submit_button)
from .locators import FormFieldsLocators


class StudentRegistrationForm:
    """Class for filling form fields with generated data using predefined locators."""

    def __init__(self, driver, first_name: str, last_name: str, email: str, gender: str,
                 mobile: str, birth_date: list, subjects: list, hobbies: list,
                 picture: str, address: str, state: str, city: str):
        self.driver = driver
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.mobile = mobile
        self.birth_date = birth_date
        self.subjects = subjects
        self.hobbies = hobbies
        self.picture = picture
        self.address = address
        self.state = state
        self.city = city

    def enter_firstname(self):
        field = self.driver.find_element(*FormFieldsLocators.first_name_field)
        fill_in_text_field(field, self.first_name)

    def enter_last_name(self):
        field = self.driver.find_element(*FormFieldsLocators.last_name_field)
        fill_in_text_field(field, self.last_name)

    def enter_email(self):
        field = self.driver.find_element(*FormFieldsLocators.email_field)
        fill_in_text_field(field, self.email)

    def select_gender(self):
        if self.gender.lower() == 'male':
            select_option(self.driver, self.driver.find_element(*FormFieldsLocators.gender_male_radiobutton))
        elif self.gender.lower() == 'female':
            select_option(self.driver, self.driver.find_element(*FormFieldsLocators.gender_female_radiobutton))
        elif self.gender.lower() == 'other':
            select_option(self.driver, self.driver.find_element(*FormFieldsLocators.gender_other_radiobutton))
        else:
            assert False, 'Gender not in (Male, Female, Other)'

    def enter_mobile(self):
        field = self.driver.find_element(*FormFieldsLocators.mobile_field)
        fill_in_text_field(field, self.mobile)

    def enter_birth_date(self):
        field = self.driver.find_element(*FormFieldsLocators.birth_date_field)
        enter_date(field, self.birth_date)

    def select_birth_date_in_calendar(self):
        calendar = self.driver.find_element(*FormFieldsLocators.birth_date_field)
        select_date(self.driver, calendar, self.birth_date)

    def enter_subjects(self):
        if self.subjects:
            for subject in self.subjects:
                field = self.driver.find_element(*FormFieldsLocators.subjects_field)
                enter_and_select_subject(self.driver, field, subject)

    def select_hobby(self):
        if self.hobbies:
            for hobby in self.hobbies:
                if hobby.lower() == 'sports':
                    select_option(self.driver, self.driver.find_element(*FormFieldsLocators.hobby_sports_checkbox))
                elif hobby.lower() == 'reading':
                    select_option(self.driver, self.driver.find_element(*FormFieldsLocators.hobby_reading_checkbox))
                elif hobby.lower() == 'music':
                    select_option(self.driver, self.driver.find_element(*FormFieldsLocators.hobby_music_checkbox))
                else:
                    assert False, 'Hobby not in (Sports, Reading, Music)'

    def upload_picture(self):
        if self.picture and isfile(normpath(self.picture)):
            file_selector = self.driver.find_element(*FormFieldsLocators.picture_file_selector)
            upload_file(file_selector, self.picture)

    def enter_address(self):
        field = self.driver.find_element(*FormFieldsLocators.address_field)
        fill_in_text_field(field, self.address)

    def select_state(self):
        field = self.driver.find_element(*FormFieldsLocators.state_selector)
        enter_and_select_state_city(field, self.state)

    def select_city(self):
        field = self.driver.find_element(*FormFieldsLocators.city_selector)
        enter_and_select_state_city(field, self.city)

    def submit_form(self):
        button = self.driver.find_element(*FormFieldsLocators.submit_button)
        push_submit_button(button)

    def fill_in_form_fields(self):
        self.enter_firstname()
        self.enter_last_name()
        self.enter_email()
        self.select_gender()
        self.enter_mobile()
        self.select_birth_date_in_calendar()
        self.enter_subjects()
        self.select_hobby()
        self.upload_picture()
        self.enter_address()
        self.select_state()
        self.select_city()


def fill_in_fields_and_submit_form(driver: webdriver, form_data: dict):
    """Fills the form fields with generated data and submits the form."""
    registration_form = StudentRegistrationForm(driver, **form_data)
    registration_form.fill_in_form_fields()
    registration_form.submit_form()
