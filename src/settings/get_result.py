import ntpath

from bs4 import BeautifulSoup

from src.errors import ResultDataError


def get_result_data(driver) -> dict:
    try:
        html = driver.page_source
        soup_object = BeautifulSoup(html, "lxml")

    except Exception:
        raise ResultDataError('The form was not submitted')
    else:
        title = 'Thanks for submitting the form'
        title_found = soup_object.find(text=title)
        if title_found:
            result_table = soup_object.find('table', class_='table')
            all_rows = result_table.find_all('tr')
            result = dict()

            for data in all_rows[1:]:
                field, value = data.find_all('td')
                result[field.text] = value.text
            return result
        raise ResultDataError('The form was not submitted')


def get_file_name(input_path: str) -> str | None:
    if not input_path:
        return None
    head, tail = ntpath.split(input_path)
    return tail or ntpath.basename(head)


def result_validation(driver, ini_data: dict) -> None:
    ini_full_name = f"{ini_data['first_name']} {ini_data['last_name']}"
    ini_email = ini_data['email']
    ini_gender = ini_data['gender'].capitalize()
    ini_mobile = ini_data['mobile']
    ini_birth_date = ini_data['birth_date']
    ini_subjects = ini_data['subjects']
    ini_hobbies = ini_data['hobbies']
    ini_picture = get_file_name(ini_data['picture'])
    ini_address = ini_data['address']
    if ini_data['state']:
        ini_state_and_city = f"{ini_data['state']} {ini_data['city']}"
    else:
        ini_state_and_city = None

    result_data = get_result_data(driver)
    result_full_name = result_data['Student Name']
    result_email = result_data['Student Email']
    result_gender = result_data['Gender']
    result_mobile = result_data['Mobile']
    result_birth_date = result_data['Date of Birth']

    result_subjects = list()
    if result_data['Subjects']:
        result_subjects = result_data['Subjects'].split(', ')

    result_hobbies = list()
    if result_data['Hobbies']:
        result_hobbies = result_data['Hobbies'].split(', ')

    result_picture = result_data['Picture']
    result_address = result_data['Address']
    result_state_and_city = result_data['State and City']

    if ini_full_name != result_full_name:
        raise ResultDataError('Full name does not match')

    if ini_email != result_email:
        raise ResultDataError('Email does not match')

    if ini_gender != result_gender:
        raise ResultDataError('Gender does not match')

    if ini_mobile != result_mobile:
        raise ResultDataError('Mobile number does not match')

    if ini_birth_date != result_birth_date:
        raise ResultDataError('Birth date does not match')

    if ini_subjects != result_subjects:
        raise ResultDataError('Subjects does not match')

    if ini_hobbies != result_hobbies:
        raise ResultDataError('Hobbies does not match')

    if ini_picture != result_picture:
        raise ResultDataError('Picture does not match')

    if ini_address != result_address:
        raise ResultDataError('Address does not match')

    if ini_state_and_city != result_state_and_city:
        raise ResultDataError('State and City does not match')
