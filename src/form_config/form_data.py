import re
from datetime import datetime
from os.path import isfile, normpath

from src.errors import ConfigError


SUBJECTS = ['accounting', 'arts', 'biology', 'chemistry', 'civics',
            'commerce', 'computer science', 'economics', 'english', 'hindi',
            'history', 'maths', 'physics', 'social studies']

GENDER = ['male', 'female', 'other']

MONTHS = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
          5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}

DATE_SEPARATORS = [' ', '.', ',', '-', '/']

HOBBIES = ['sports', 'reading', 'music']

STATE_CITY = {'ncr': ['delhi', 'gurgaon', 'noida'],
              'uttar pradesh': ['agra', 'lucknow', 'merrut'],
              'haryana': ['karnal', 'panipat'],
              'rajasthan': ['jaipur', 'jaiselmer']}


class FormData:
    def __init__(self, first_name: str, last_name: str, email: str, gender: str,
                 mobile: str, birth_date: str, subjects: list, hobbies: list,
                 picture: str, address: str, state: str, city: str):
        """Creates an object of the FormData class,
        assigns values to the main script parameters from a configuration file."""
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

    def verify_form_data(self) -> None:
        """Validates configuration data.
        The data file type, output file type, analysis mode,
        and math point value (only for 'AFFL' mode) are checked for correctness.
        The data file and output file directory are checked for existence.
        If the check fails, an appropriate exception will be raised."""

        if self.birth_date:
            self.birth_date = self.parse_and_verify_birth_date()

        email_template = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if not re.fullmatch(email_template, self.email):
            raise ConfigError(f'Email is invalid: {self.email}')

        if self.gender.lower() not in GENDER:
            raise ConfigError(f'Gender is invalid: {self.gender}')

        mobile_template = re.compile(r'([0-9]{10})')
        if not re.fullmatch(mobile_template, self.mobile):
            raise ConfigError(f'Mobile number is invalid: {self.mobile}')

        for subject in self.subjects:
            if subject.lower() not in SUBJECTS:
                raise ConfigError(f'Subject is invalid: {subject}')

        for hobby in self.hobbies:
            if hobby.lower() not in HOBBIES:
                raise ConfigError(f'Hobby is invalid: {hobby}')

        if self.picture and not isfile(normpath(self.picture)):
            raise ConfigError(f'Picture not found: {self.picture}')

        if self.state.lower() not in STATE_CITY:
            raise ConfigError(f'State is invalid: {self.state}')

        if self.city.lower() not in STATE_CITY[self.state.lower()]:
            raise ConfigError(f'City is invalid: {self.city}')

    def get_form_data(self) -> dict:
        """Returns the data file format."""
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'email': self.email,
                'gender': self.gender,
                'mobile': self.mobile,
                'birth_date': self.birth_date,
                'subjects': self.subjects,
                'hobbies': self.hobbies,
                'picture': self.picture,
                'address': self.address,
                'state': self.state,
                'city': self.city}

    def parse_and_verify_birth_date(self):
        formatted_date = list()
        try:
            for sep in DATE_SEPARATORS:
                if self.birth_date.count(sep) == 2:
                    formatted_date = self.birth_date.split(sep)

            b_day, b_month, b_year = formatted_date
            if b_month.isalpha():
                b_month = format_month(b_month)
            b_date = datetime(int(b_year), int(b_month), int(b_day))
            if b_date > datetime.today():
                raise ConfigError
            if int(b_day) < 10:
                b_day = f'0{b_day}'

        except Exception:
            raise ConfigError
        else:
            return f'{b_day} {MONTHS[int(b_month)]},{b_year}'


def format_month(month: str) -> int:
    month = month.lower()
    if month == 'january' or 'jan':
        return 1
    elif month == 'february' or 'feb':
        return 2
    elif month == 'march' or 'mar':
        return 3
    elif month == 'april' or 'apr':
        return 4
    elif month == 'may' or 'may':
        return 5
    elif month == 'june' or 'jun':
        return 6
    elif month == 'july' or 'jul':
        return 7
    elif month == 'august' or 'aug':
        return 8
    elif month == 'september' or 'sep':
        return 9
    elif month == 'october' or 'oct':
        return 10
    elif month == 'november' or 'nov':
        return 11
    elif month == 'december' or 'dec':
        return 12
    else:
        raise ConfigError
