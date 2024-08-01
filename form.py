from input_data_functions import (input_data, input_data_and_press_enter,
                                  remove_default_value_and_input_data,
                                  select_option, upload_file, press_submit_button)

from web_driver import WebDriver
from field_locators import FormFieldLocator


FIELD_LOCATOR = FormFieldLocator(WebDriver)


class StudentRegistrationForm:
    def __init__(self):
        self.first_name = FIELD_LOCATOR.get_first_name_field()
        self.last_name = FIELD_LOCATOR.get_last_name_field()
        self.email = FIELD_LOCATOR.get_email_field()
        self.mobile = FIELD_LOCATOR.get_mobile_field()
        self.birth_date = FIELD_LOCATOR.get_birth_date_datepicker()
        self.subjects = FIELD_LOCATOR.get_subjects_field()
        self.picture = FIELD_LOCATOR.get_picture_file()
        self.address = FIELD_LOCATOR.get_address_field()
        self.state = FIELD_LOCATOR.get_state_selector()
        self.city = FIELD_LOCATOR.get_city_selector()
        self.submit = FIELD_LOCATOR.get_submit_button()

    def fill_in_firstname(self, first_name: str):
        input_data(self.first_name, first_name)

    def fill_in_last_name(self, last_name: str):
        input_data(self.last_name, last_name)

    def fill_in_email(self, email: str):
        input_data(self.email, email)

    def select_gender(self, gender: str):
        if gender.lower() == 'male':
            select_option(FIELD_LOCATOR.get_gender_male_radiobutton())
        elif gender.lower() == 'female':
            select_option(FIELD_LOCATOR.get_gender_female_radiobutton())
        elif gender.lower() == 'other':
            select_option(FIELD_LOCATOR.get_gender_other_radiobutton())

    def fill_in_mobile(self, mobile: str):
        input_data(self.mobile, mobile)

    def fill_in_birth_date(self, birth_date: str):
        remove_default_value_and_input_data(self.mobile, birth_date)

    def fill_in_subjects(self, subjects: list):
        if subjects:
            for subject in subjects:
                input_data_and_press_enter(self.subjects, subject)

    def select_hobby(self, hobbies):
        if hobbies:
            for hobby in hobbies:
                if hobby.lower() == 'sports':
                    select_option(FIELD_LOCATOR.get_hobby_sports_checkbox())
                elif hobby.lower() == 'reading':
                    select_option(FIELD_LOCATOR.get_hobby_reading_checkbox())
                elif hobby.lower() == 'music':
                    select_option(FIELD_LOCATOR.get_hobby_music_checkbox())

    def upload_picture(self, path: str):
        upload_file(self.picture, path)

    def fill_in_address(self, address: str):
        input_data(self.address, address)

    def select_state(self, state: str):
        input_data_and_press_enter(self.state, state)

    def select_city(self, city: str):
        input_data_and_press_enter(self.city, city)

    def submit_form(self):
        press_submit_button(self.submit)
