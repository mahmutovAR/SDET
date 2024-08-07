from configparser import ConfigParser
from os import getcwd
from os.path import abspath, dirname
from os.path import join as os_path_join


def generate_datafile(input_file_path: str, input_form_url: str, input_data: dict) -> None:
    """Generates datafile at given path."""
    temp_config_ini = ConfigParser()

    temp_config_ini['form_data'] = {'url': input_form_url}

    temp_config_ini['student_data'] = {'first_name': input_data['first_name'],
                                       'last_name': input_data['last_name'],
                                       'email': input_data['email'],
                                       'gender': input_data['gender'],
                                       'mobile': input_data['mobile'],
                                       'birth_date': input_data['birth_date'],
                                       'subjects': input_data['subjects'],
                                       'hobbies': input_data['hobbies'],
                                       'picture': input_data['picture'],
                                       'address': input_data['address'],
                                       'state': input_data['state'],
                                       'city': input_data['city']}

    with open(input_file_path, 'w') as config_file:
        temp_config_ini.write(config_file)


def main():
    """The script creates sample configuration and data files in the same directory as itself.
    Then running "run_math_sets_analyser" outputs a result file."""
    script_dir = abspath(dirname(__file__))
    data_file = os_path_join(script_dir, 'config.ini')

    form_url = 'https://demoqa.com/automation-practice-form'
    temp_data = {'first_name': 'Joseph David',
                 'last_name': 'Smithsen',
                 'email': 'jd.smithsen@td-kolner.com',
                 'gender': 'MaLe',
                 'mobile': '8087971551',
                 'birth_date': '29 02 2004',
                 'subjects': 'phYSics, mAthS, cOmpUter scIEnce',
                 'hobbies': 'MuSIc, SpORts',
                 'picture': os_path_join(getcwd(), 'pictures', 'ebersteiger.jpg'),
                 'address': 'Gramin Rd, Kapil Sharad 3451',
                 'state': 'utTar PrADEsh',
                 'city': 'MeRRut'}
    try:
        generate_datafile(data_file, form_url, temp_data)
    except Exception as exc:
        exc.add_note('Generating the "config.ini" raised an exception')
        raise


if __name__ == '__main__':
    main()
