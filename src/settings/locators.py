from selenium.webdriver.common.by import By


class FormFieldLocator:
    def __init__(self, driver):
        self.driver = driver

    def get_first_name_field(self):
        return self.driver.find_element(By.ID, 'firstName')

    def get_last_name_field(self):
        return self.driver.find_element(By.ID, 'lastName')

    def get_email_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id=userEmail]")

    def get_gender_male_radiobutton(self):
        return self.driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")

    def get_gender_female_radiobutton(self):
        return self.driver.find_element(By.XPATH, "//label[@for='gender-radio-2']")

    def get_gender_other_radiobutton(self):
        return self.driver.find_element(By.XPATH, "//label[@for='gender-radio-3']")

    def get_mobile_field(self):
        return self.driver.find_element(By.ID, 'userNumber')

    def get_birth_date_date_picker(self):
        return self.driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']")

    def get_subjects_field(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id=subjectsInput]")

    def get_hobby_sports_checkbox(self):
        return self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")

    def get_hobby_reading_checkbox(self):
        return self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-2']")

    def get_hobby_music_checkbox(self):
        return self.driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-3']")

    def get_picture_file(self):
        return self.driver.find_element(By.XPATH, "//input[@type='file']")

    def get_address_field(self):
        return self.driver.find_element(By.ID, 'currentAddress')

    def get_state_selector(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id=react-select-3-input]")

    def get_city_selector(self):
        return self.driver.find_element(By.CSS_SELECTOR, "input[id=react-select-4-input]")

    def get_submit_button(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")
