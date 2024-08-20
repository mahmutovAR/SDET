from os.path import join as os_path_join
from pathlib import Path

from pytest import fixture, mark, raises

from src.errors import EnteredDataValidationError, SubmitError
from src.settings import fill_in_fields_and_submit_form, validate_entered_form_data


NAME_ISSPACE = [[' ', ' '],
                ['  ', ' '],
                [' ', '  '],
                ['  ', '  '],
                ['  A G  n', '  '],
                ['  ', '   F TR  '],
                ['  ERT ', '  KLD']]

NO_NAME = [['', ''],
           ['', 'DF.RT'],
           ['DF.RT', '']]

ADDRESS_ISSPACE = [' ', '   ', '   4529 rd, FRA   ', '   4529 rd, FRA', '4529 rd, FRA   ']

INVALID_MOBILE = ['', '123', 'abc', 'a1b2c3', 'abcdefghij', '123456789']

INVALID_EMAIL = [' ', 'abc', 'abc@', '@def', 'abc@def', 'abc @def.yz', 'abc @ def. yz']

INVALID_SUBJECTS = [['Engineering'],
                    ['Astrophysics', 'Geograpy', 'Sports'],
                    ['Geograpy', 'Economics', 'Social Studies', 'Sleeping'],
                    ['Physics', 'Geograpy', 'History', 'Swimming', 'Running'],
                    ['Swimming', 'Sleeping', 'Chemistry'],
                    ['Maths', 'Geograpy', 'Computer Science']]

INVALID_PICTURE = [os_path_join(Path(__file__).resolve().parents[1], 'pictures', 'photo.jpg'),
                   os_path_join(Path(__file__).resolve().parents[1], 'pictures')]


def test_valid_data(set_up: fixture):
    """Tests form filling with valid generated data."""
    data, driver = set_up
    fill_in_fields_and_submit_form(driver.get_driver(), data)
    validate_entered_form_data(driver.get_driver(), data)


@mark.parametrize("name_isspace", NAME_ISSPACE)
def test_name_isspace(set_up: fixture, name_isspace: str):
    """
    """
    data, driver = set_up
    data['first_name'], data['last_name'] = name_isspace
    fill_in_fields_and_submit_form(driver.get_driver(), data)
    validate_entered_form_data(driver.get_driver(), data)


@mark.parametrize("address_isspace", ADDRESS_ISSPACE)
def test_address_isspace(set_up: fixture, address_isspace: str):
    """
    """
    data, driver = set_up
    data['address'] = address_isspace
    fill_in_fields_and_submit_form(driver.get_driver(), data)
    validate_entered_form_data(driver.get_driver(), data)


@mark.parametrize("no_name", NO_NAME)
def test_no_name(set_up: fixture, no_name: str):
    """."""
    data, driver = set_up
    data['first_name'], data['last_name'] = no_name
    fill_in_fields_and_submit_form(driver.get_driver(), data)
    with raises(SubmitError):
        validate_entered_form_data(driver.get_driver(), data)


@mark.parametrize("invalid_mobile", INVALID_MOBILE)
def test_invalid_mobile(set_up: fixture, invalid_mobile: str):
    data, driver = set_up
    data['mobile'] = invalid_mobile
    fill_in_fields_and_submit_form(driver.get_driver(), data)
    with raises(SubmitError):
        validate_entered_form_data(driver.get_driver(), data)


def test_mobile_more_than_10_digits(set_up: fixture):
    data, driver = set_up
    data['mobile'] = '123456789012345'
    fill_in_fields_and_submit_form(driver.get_driver(), data)
    with raises(EnteredDataValidationError):
        validate_entered_form_data(driver.get_driver(), data)


@mark.parametrize("invalid_email", INVALID_EMAIL)
def test_invalid_email(set_up: fixture, invalid_email: str):
    data, driver = set_up
    data['email'] = invalid_email
    fill_in_fields_and_submit_form(driver.get_driver(), data)
    with raises(SubmitError):
        validate_entered_form_data(driver.get_driver(), data)


@mark.parametrize("invalid_subjects", INVALID_SUBJECTS)
def test_invalid_subjects(set_up: fixture, invalid_subjects: list):
    data, driver = set_up
    data['subjects'] = invalid_subjects
    fill_in_fields_and_submit_form(driver.get_driver(), data)
    with raises(EnteredDataValidationError):
        validate_entered_form_data(driver.get_driver(), data)


@mark.parametrize("invalid_picture", INVALID_PICTURE)
def test_invalid_picture(set_up: fixture, invalid_picture: str):
    data, driver = set_up
    data['picture'] = invalid_picture
    fill_in_fields_and_submit_form(driver.get_driver(), data)
    with raises(EnteredDataValidationError):
        validate_entered_form_data(driver.get_driver(), data)


def test_select_state_without_city(set_up: fixture):
    data, driver = set_up
    data['city'] = ''
    fill_in_fields_and_submit_form(driver.get_driver(), data)
    with raises(EnteredDataValidationError):
        validate_entered_form_data(driver.get_driver(), data)
