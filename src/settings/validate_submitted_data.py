import ntpath

from bs4 import BeautifulSoup

from src.errors import EnteredDataValidationError, SubmitError


MONTHS = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
          5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}


def get_output_data(driver) -> dict:
    """Scrapes a pop-up window with entered data."""
    try:
        html = driver.page_source
        soup_object = BeautifulSoup(html, "lxml")
        result_table = soup_object.find('table', class_='table')
        all_rows = result_table.find_all('tr')
    except Exception:
        raise SubmitError
    else:
        result = dict()
        for data in all_rows[1:]:
            field, value = data.find_all('td')
            result[field.text] = value.text
        return result


def convert_date(input_date: list) -> str | None:
    """Converts a date to the submitted form format."""
    if not input_date:
        return None
    b_year, b_month, b_day = input_date
    return f'{b_day} {MONTHS[int(b_month)]},{b_year}'


def get_file_name(input_path: str) -> str | None:
    """Returns the file name from the specified path."""
    if not input_path:
        return None
    head, tail = ntpath.split(input_path)
    return tail or ntpath.basename(head)


def validate_entered_form_data(driver, ini_data: dict) -> None:
    """Verifies the filled form data and the submitted data,
    if they do not match, an EnteredDataValidationError raises."""
    ini_full_name = f"{ini_data['first_name']} {ini_data['last_name']}"
    ini_email = ini_data['email']
    ini_gender = ini_data['gender']
    ini_mobile = ini_data['mobile']
    ini_birth_date = convert_date(ini_data['birth_date'])
    ini_subjects = ini_data['subjects']
    ini_hobbies = ini_data['hobbies']
    ini_picture = get_file_name(ini_data['picture'])
    ini_address = ini_data['address']
    if ini_data['state']:
        ini_state_and_city = f"{ini_data['state']} {ini_data['city']}"
    else:
        ini_state_and_city = None

    output_data = get_output_data(driver)
    output_full_name = output_data['Student Name']
    output_email = output_data['Student Email']
    output_gender = output_data['Gender']
    output_mobile = output_data['Mobile']
    output_birth_date = output_data['Date of Birth']

    output_subjects = list()
    if output_data['Subjects']:
        output_subjects = output_data['Subjects'].split(', ')

    output_hobbies = list()
    if output_data['Hobbies']:
        output_hobbies = output_data['Hobbies'].split(', ')

    output_picture = output_data['Picture']
    output_address = output_data['Address']
    output_state_and_city = output_data['State and City']

    if ini_full_name.strip() != output_full_name.strip():
        raise EnteredDataValidationError('Full name')

    elif ini_email != output_email:
        raise EnteredDataValidationError('Email')

    elif ini_gender != output_gender:
        raise EnteredDataValidationError('Gender')

    elif ini_mobile != output_mobile:
        raise EnteredDataValidationError('Mobile')

    elif ini_birth_date != output_birth_date:
        raise EnteredDataValidationError('Birth date')

    elif sorted(ini_subjects) != sorted(output_subjects):
        raise EnteredDataValidationError('Subjects')

    elif sorted(ini_hobbies) != sorted(output_hobbies):
        raise EnteredDataValidationError('Hobbies')

    elif ini_picture != output_picture:
        raise EnteredDataValidationError('Picture')

    elif ini_address.strip() != output_address.strip():
        raise EnteredDataValidationError('Address')

    elif ini_state_and_city != output_state_and_city:
        raise EnteredDataValidationError('State and City')

    else:
        print('Form data has been submitted')
