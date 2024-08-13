from selenium import webdriver

from .input_data_functions import (input_data, input_data_and_press_enter,
                                   remove_default_value_and_input_data,
                                   select_option, upload_file, press_submit_button)
from .locators import FormFieldLocator


class StudentRegistrationForm:
    def __init__(self, driver):
        self.driver = driver
        self.locator = FormFieldLocator(self.driver)
        self.first_name = self.locator.get_first_name_field()
        self.last_name = self.locator.get_last_name_field()
        self.email = self.locator.get_email_field()
        self.mobile = self.locator.get_mobile_field()
        self.birth_date = self.locator.get_birth_date_date_picker()
        self.subjects = self.locator.get_subjects_field()
        self.picture = self.locator.get_picture_file()
        self.address = self.locator.get_address_field()
        self.state = self.locator.get_state_selector()
        self.city = self.locator.get_city_selector()
        self.submit = self.locator.get_submit_button()

    def fill_in_firstname(self, first_name: str):
        input_data(self.first_name, first_name)

    def fill_in_last_name(self, last_name: str):
        input_data(self.last_name, last_name)

    def fill_in_email(self, email: str):
        input_data(self.email, email)

    def select_gender(self, gender: str):
        if gender.lower() == 'male':
            select_option(self.driver, self.locator.get_gender_male_radiobutton())
        elif gender.lower() == 'female':
            select_option(self.driver, self.locator.get_gender_female_radiobutton())
        elif gender.lower() == 'other':
            select_option(self.driver, self.locator.get_gender_other_radiobutton())

    def fill_in_mobile(self, mobile: str):
        input_data(self.mobile, mobile)

    def fill_in_birth_date(self, birth_date: str):
        remove_default_value_and_input_data(self.birth_date, birth_date)

    def fill_in_subjects(self, subjects: list):
        if subjects:
            for subject in subjects:
                input_data_and_press_enter(self.subjects, subject)

    def select_hobby(self, hobbies: list):
        if hobbies:
            for hobby in hobbies:
                if hobby.lower() == 'sports':
                    select_option(self.driver, self.locator.get_hobby_sports_checkbox())
                elif hobby.lower() == 'reading':
                    select_option(self.driver, self.locator.get_hobby_reading_checkbox())
                elif hobby.lower() == 'music':
                    select_option(self.driver, self.locator.get_hobby_music_checkbox())

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


def fill_in_form(driver: webdriver, form_data: dict):
    registration_form = StudentRegistrationForm(driver)
    registration_form.fill_in_firstname(form_data['first_name'])
    registration_form.fill_in_last_name(form_data['last_name'])
    registration_form.fill_in_email(form_data['email'])
    registration_form.select_gender(form_data['gender'])
    registration_form.fill_in_mobile(form_data['mobile'])
    registration_form.fill_in_birth_date(form_data['birth_date'])
    registration_form.fill_in_subjects(form_data['subjects'])
    registration_form.select_hobby(form_data['hobbies'])
    registration_form.upload_picture(form_data['picture'])
    registration_form.fill_in_address(form_data['address'])
    registration_form.select_state(form_data['state'])
    registration_form.select_city(form_data['city'])
    registration_form.submit_form()
