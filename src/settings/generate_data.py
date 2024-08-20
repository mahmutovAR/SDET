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


def generate_name() -> str:
    name_1 = rstr.letters(4, 8).title()
    name_2 = rstr.letters(0, 3).title()
    name_3 = rstr.letters(3, 6).title()
    return f"{name_1} {name_2}.{name_3}"


def generate_email() -> str:
    user_name = rstr.normal(12, include=['-', '_'], exclude=' ')
    domain_1 = rstr.domainsafe(8)
    domain_2 = rstr.letters(3)
    return f"{user_name}@{domain_1}.{domain_2}"


def generate_gender():
    return choice(GENDER)


def generate_mobile_number() -> str:
    return rstr.digits(10)


def generate_birth_date() -> str:
    calendar_start = date(1900, 1, 1)
    calendar_end = date(2100, 12, 31)
    days_range = (calendar_end - calendar_start).days
    random_diff = randrange(0, days_range + 1)
    b_year, b_month, b_day = str(calendar_start + timedelta(days=random_diff)).split('-')
    months = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
              5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    return f'{b_day} {months[int(b_month)]},{b_year}'


def generate_subjects():
    num = randrange(0, len(SUBJECTS))
    return sample(SUBJECTS, k=num)


def generate_hobbies():
    num = randrange(0, len(HOBBIES))
    return sample(HOBBIES, k=num)


def generate_picture():
    picture_path = [os_path_join(Path(__file__).resolve().parents[1], 'pictures', 'ebersteiger.jpg'),
                    os_path_join(Path(__file__).resolve().parents[1], 'pictures', 'gl-ramos'),
                    os_path_join(Path(__file__).resolve().parents[1], 'pictures', 'Lorem ipsum')]
    return choice(picture_path)


def generate_address() -> str:
    address_1 = rstr.uppercase(6, 8)
    address_2 = rstr.letters(4, 12).title()
    address_3 = rstr.letters(6, 15).title()
    address_4 = rstr.letters(5, 10).title()
    address_5 = rstr.digits(4)
    return f'{address_1} {address_2} Rd, {address_3} {address_4} {address_5}'


def generate_state_city() -> (str, str):
    state = choice(list(STATE_CITY.keys()))
    city = choice(STATE_CITY[state])
    return state, city


def get_full_form_data():
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


def get_required_form_data():
    pass
