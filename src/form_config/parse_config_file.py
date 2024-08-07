from configparser import ConfigParser
from os.path import isfile, normpath

from src.errors import ConfigError
from .form_data import FormData


def parse_config_file(input_file: str) -> (str, dict):
    """Checks for the presence of 'config.ini', if the file is not found DataFileError will be raised.
    Validates the configuration data from the given configuration file.
    Returns ConfigData class object with the main configuration arguments."""
    if not isfile(normpath(input_file)):
        raise ConfigError(f'Not found: {input_file}')
    try:
        config_data = ConfigParser()
        config_data.read(input_file)

        form_data_section = config_data['form_data']
        student_data_section = config_data['student_data']

        student_data = {'first_name': student_data_section.get('first_name'),
                        'last_name': student_data_section.get('last_name'),
                        'email': student_data_section.get('email'),
                        'gender': student_data_section.get('gender'),
                        'mobile': student_data_section.get('mobile'),
                        'birth_date': student_data_section.get('birth_date'),
                        'subjects': student_data_section.get('subjects').split(', '),
                        'hobbies': student_data_section.get('hobbies').split(', '),
                        'picture': student_data_section.get('picture'),
                        'address': student_data_section.get('address'),
                        'state': student_data_section.get('state'),
                        'city': student_data_section.get('city')}

        form_data_url = form_data_section.get('url')

    except KeyError as err:
        raise ConfigError(err)
    except ValueError:
        raise ConfigError(ValueError)
    except Exception as exc:
        exc.add_note('The parsing of the form_config data file raised an exception:')
        raise
    else:
        ini_data = FormData(**student_data)
        ini_data.verify_form_data()
        ini_data = ini_data.get_form_data()
        return form_data_url, ini_data
