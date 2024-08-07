import ntpath

from bs4 import BeautifulSoup

from src.errors import ResultDataError
from .web_driver import WebDriver


def get_result_data() -> dict:
    html = WebDriver.page_source
    soup_object = BeautifulSoup(html, "lxml")
    result_table = soup_object.find('table', class_='table')
    all_rows = result_table.find_all('tr')
    result = dict()

    for data in all_rows[1:]:
        field, value = data.find_all('td')
        result[field.text] = value.text
    return result


def get_file_name(input_path: str) -> str | None:
    if not input_path:
        return None
    head, tail = ntpath.split(input_path)
    return tail or ntpath.basename(head)


def format_list_elements(input_data: list | str) -> list | None:
    if not input_data:
        return None
    output_data = list()
    if isinstance(input_data, str):
        input_data = input_data.split(', ')
    for item in input_data:
        output_data.append(item.capitalize())
    output_data.sort()
    return output_data


def result_validation(ini_data: dict) -> None:
    ini_full_name = f"{ini_data['first_name']} {ini_data['last_name']}"
    ini_email = ini_data['email']
    ini_gender = ini_data['gender'].capitalize()
    ini_mobile = ini_data['mobile']
    ini_birth_date = ini_data['birth_date']
    ini_subjects = format_list_elements(ini_data['subjects'])
    ini_hobbies = format_list_elements(ini_data['hobbies'])
    ini_picture = get_file_name(ini_data['picture'])
    ini_address = ini_data['address']
    if ini_data['state']:
        if ini_data['state'].upper() == 'NCR':
            ini_state_and_city = f"NCR {ini_data['city'].title()}"
        else:
            ini_state_and_city = f"{ini_data['state'].title()} {ini_data['city'].title()}"
    else:
        ini_state_and_city = None

    result_data = get_result_data()
    result_full_name = result_data['Student Name']
    result_email = result_data['Student Email']
    result_gender = result_data['Gender']
    result_mobile = result_data['Mobile']
    result_birth_date = result_data['Date of Birth']
    result_subjects = format_list_elements(result_data['Subjects'])
    # if result_subjects:
    #     result_subjects.sort()
    result_hobbies = format_list_elements(result_data['Hobbies'])
    # if result_hobbies:
    #     result_hobbies.sort()
    result_picture = result_data['Picture']
    result_address = result_data['Address']
    result_state_and_city = result_data['State and City']

    if ini_full_name != result_full_name:
        raise ResultDataError('Full name does not match')
        # print('Full name does not match')

    if ini_email != result_email:
        raise ResultDataError('Email does not match')
        # print('Email does not match')

    if ini_gender != result_gender:
        raise ResultDataError('Gender does not match')
        # print('Gender does not match')

    if ini_mobile != result_mobile:
        raise ResultDataError('Mobile number does not match')
        # print('Mobile number does not match')

    if ini_birth_date != result_birth_date:
        raise ResultDataError('Birth date does not match')
        # print('Birth date does not match')

    if ini_subjects != result_subjects:
        raise ResultDataError('Subjects does not match')
        # print('Subjects does not match')

    if ini_hobbies != result_hobbies:
        raise ResultDataError('Hobbies does not match')
        # print('Hobbies does not match')

    if ini_picture != result_picture:
        raise ResultDataError('Picture does not match')
        # print('Picture does not match')

    if ini_address != result_address:
        raise ResultDataError('Address does not match')
        # print('Address does not match')

    if ini_state_and_city != result_state_and_city:
        raise ResultDataError('State and City does not match')
        # print('State and City does not match')
