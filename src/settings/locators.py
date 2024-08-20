from selenium.webdriver.common.by import By


class FormFieldsLocators:
    """Form field locator class."""

    first_name_field = (By.ID, "firstName")
    last_name_field = (By.ID, "lastName")
    email_field = (By.CSS_SELECTOR, "input[id=userEmail]")
    gender_male_radiobutton = (By.XPATH, "//label[@for='gender-radio-1']")
    gender_female_radiobutton = (By.XPATH, "//label[@for='gender-radio-2']")
    gender_other_radiobutton = (By.XPATH, "//label[@for='gender-radio-3']")
    mobile_field = (By.ID, "userNumber")
    birth_date_field = (By.XPATH, "//input[@id='dateOfBirthInput']")
    subjects_field = (By.CSS_SELECTOR, "input[id=subjectsInput]")
    subject_is_valid = (By.XPATH, "//div[contains(@class, 'subjects-auto-complete__menu')]")
    hobby_sports_checkbox = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
    hobby_reading_checkbox = (By.XPATH, "//label[@for='hobbies-checkbox-2']")
    hobby_music_checkbox = (By.XPATH, "//label[@for='hobbies-checkbox-3']")
    picture_file_selector = (By.XPATH, "//input[@type='file']")
    address_field = (By.ID, "currentAddress")
    state_selector = (By.CSS_SELECTOR, "input[id=react-select-3-input]")
    city_selector = (By.CSS_SELECTOR, "input[id=react-select-4-input]")
    submit_button = (By.XPATH, "//button[@type='submit']")


def get_year_selector() -> tuple:
    """Returns the locator of a year selector in a calendar."""
    return By.XPATH, "//select[contains(@class, 'react-datepicker__year-select')]"


def get_month_selector() -> tuple:
    """Returns the locator of a month selector in a calendar."""
    return By.XPATH, "//select[contains(@class, 'react-datepicker__month-select')]"


def get_day_selector(day: str) -> tuple:
    """Returns the locator of a day selector in a calendar."""
    return By.XPATH, f"//div[contains(@class, 'day--{day}') and (not(contains(@class,'outside-month')))]"
