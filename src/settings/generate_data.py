from datetime import date, timedelta
from os.path import join as os_path_join
from pathlib import Path
from random import choice, randrange, sample

import rstr


GENDER = ['Male', 'Female', 'Other']

SUBJECTS = ['Accounting', 'Arts', 'Biology', 'Chemistry', 'Civics',
            'Commerce', 'Computer Science', 'Economics', 'English', 'Hindi',
            'History', 'Maths', 'Physics', 'Social Studies']

HOBBIES = ['Sports', 'Reading', 'Music']

STATE_CITY = {'NCR': ['Delhi', 'Gurgaon', 'Noida'],
              'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
              'Haryana': ['Karnal', 'Panipat'],
              'Rajasthan': ['Jaipur', 'Jaiselmer']}

PICTURE = picture_path = [os_path_join(Path(__file__).resolve().parents[1], 'pictures', 'ebersteiger.jpg'),
                          os_path_join(Path(__file__).resolve().parents[1], 'pictures', 'gl-ramos'),
                          os_path_join(Path(__file__).resolve().parents[1], 'pictures', 'Lorem ipsum')]


def generate_name() -> str:
    """Returns a string value."""
    name_1 = rstr.letters(4, 8).title()
    name_2 = rstr.letters(0, 3).title()
    name_3 = rstr.letters(3, 6).title()
    return f"{name_1} {name_2} {name_3}"


def generate_email() -> str:
    """Returns a string matching the email address pattern."""
    user_name = rstr.normal(12, include=['-', '_'], exclude=' ')
    domain_1 = rstr.domainsafe(8)
    domain_2 = rstr.letters(3)
    return f"{user_name}@{domain_1}.{domain_2}"


def generate_gender() -> str:
    """Returns a random value from the specified list."""
    return choice(GENDER)


def generate_mobile_number() -> str:
    """Returns a string matching the mobile number pattern."""
    return rstr.digits(10)


def generate_birth_date() -> list:
    """Returns date in 'yyyy' 'mm' 'dd' format as a list."""
    calendar_start = date(1900, 1, 1)
    calendar_end = date(2100, 12, 31)
    days_range = (calendar_end - calendar_start).days
    random_diff = randrange(0, days_range + 1)
    return str(calendar_start + timedelta(days=random_diff)).split('-')


def generate_subjects() -> list:
    """Returns a random list of elements from the specified list."""
    num = randrange(0, len(SUBJECTS))
    return sample(SUBJECTS, k=num)


def generate_hobbies() -> list:
    """Returns a random list of elements from the specified list."""
    num = randrange(0, len(HOBBIES))
    return sample(HOBBIES, k=num)


def generate_picture() -> str:
    """Returns a random value from the specified list of paths."""
    return choice(PICTURE)


def generate_address() -> str:
    """Returns a string matching the address pattern."""
    address_1 = rstr.uppercase(6, 8)
    address_2 = rstr.letters(4, 12).title()
    address_3 = rstr.letters(6, 15).title()
    address_4 = rstr.letters(5, 10).title()
    address_5 = rstr.digits(4)
    return f'{address_1} {address_2} Rd, {address_3} {address_4} {address_5}'


def generate_state_city() -> (str, str):
    """Returns a random pair value from the specified dictionary."""
    state = choice(list(STATE_CITY.keys()))
    city = choice(STATE_CITY[state])
    return state, city


def get_form_data() -> dict:
    """Returns the generated form data."""
    state, city = generate_state_city()
    return {'first_name': generate_name(),
            'last_name': generate_name(),
            'email': generate_email(),
            'gender': generate_gender(),
            'mobile': generate_mobile_number(),
            'birth_date': generate_birth_date(),
            'subjects': generate_subjects(),
            'hobbies': generate_hobbies(),
            'picture': generate_picture(),
            'address': generate_address(),
            'state': state,
            'city': city}
