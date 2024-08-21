from pytest import fixture, mark, raises

from src.errors import EnteredDataValidationError
from src.settings import validate_entered_form_data, StudentRegistrationForm


VALID_BIRTH_DATE = {'01 jan 1972': ['1972', '01', '01'],
                    '   05    dec     2009': ['2009', '12', '05'],
                    '1 mArCh 2002': ['2002', '03', '01'],
                    '27dEcEmbER1974': ['1974', '12', '27'],
                    '2001-05-08': ['2001', '05', '08'],
                    '1983 02 11 ': ['1983', '02', '11'],
                    '1975 / 12 / 08 ': ['1975', '12', '08'],
                    '2001 aug 9': ['2001', '08', '09'],
                    '1973 02 sep': ['1973', '09', '02'],
                    '1999  .   01    7 ': ['1999', '01', '07'],
                    ' - 01 .  oct /  1972': ['1972', '10', '01'],
                    '  / 15  , jun  .  1989': ['1989', '06', '15'],
                    ' jul 05 1963': ['1963', '07', '05'],
                    'apr 1987 02': ['1987', '04', '02'],
                    '06 / 2003 . november ': ['2003', '11', '06'],
                    '01/02/2006': ['2006', '01', '02'],
                    '09 / 03    2003': ['2003', '09', '03'],
                    '06-17-1965': ['1965', '06', '17']}

INVALID_BIRTH_DATE = {'27 . 03 . 1952': ['1952', '03', '27'],
                      '25 - - oct 97	': ['1997', '10', '25'],
                      '02 09 987': ['1987', '02', '09'],
                      '28-05-1982': ['1982', '05', '28']}


@mark.parametrize("valid_birth_date", VALID_BIRTH_DATE)
def test_valid_birth_date(set_up: fixture, valid_birth_date: str):
    data, driver = set_up
    data['birth_date'] = valid_birth_date

    user_form = StudentRegistrationForm(driver.get_driver(), **data)
    user_form.enter_firstname()
    user_form.enter_last_name()
    user_form.enter_email()
    user_form.select_gender()
    user_form.enter_mobile()
    user_form.enter_birth_date()
    user_form.enter_subjects()
    user_form.select_hobby()
    user_form.upload_picture()
    user_form.enter_address()
    user_form.select_state()
    user_form.select_city()
    user_form.submit_form()
    data['birth_date'] = VALID_BIRTH_DATE[valid_birth_date]
    validate_entered_form_data(driver.get_driver(), data)


@mark.parametrize("invalid_birth_date", INVALID_BIRTH_DATE)
def test_invalid_birth_date(set_up: fixture, invalid_birth_date: str):
    data, driver = set_up
    data['birth_date'] = invalid_birth_date

    user_form = StudentRegistrationForm(driver.get_driver(), **data)
    user_form.enter_firstname()
    user_form.enter_last_name()
    user_form.enter_email()
    user_form.select_gender()
    user_form.enter_mobile()
    user_form.enter_birth_date()
    user_form.enter_subjects()
    user_form.select_hobby()
    user_form.upload_picture()
    user_form.enter_address()
    user_form.select_state()
    user_form.select_city()
    user_form.submit_form()

    data['birth_date'] = INVALID_BIRTH_DATE[invalid_birth_date]
    with raises(EnteredDataValidationError):
        validate_entered_form_data(driver.get_driver(), data)
