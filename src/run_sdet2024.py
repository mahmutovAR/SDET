from form_config.form import StudentRegistrationForm
from os.path import join as os_path_join
from os import getcwd
from form_config import web_driver, result_validation, parse_config_file


def main(input_path: str) -> None:
    url, form_data = parse_config_file(input_path)

    web_driver.get_form_url(url)
    user_form = StudentRegistrationForm()

    user_form.fill_in_firstname(form_data['first_name'])
    user_form.fill_in_last_name(form_data['last_name'])
    user_form.fill_in_email(form_data['email'])
    user_form.select_gender(form_data['gender'])
    user_form.fill_in_mobile(form_data['mobile'])
    user_form.fill_in_birth_date(form_data['birth_date'])
    user_form.fill_in_subjects(form_data['subjects'])
    user_form.select_hobby(form_data['hobbies'])
    user_form.upload_picture(form_data['picture'])
    user_form.fill_in_address(form_data['address'])
    user_form.select_state(form_data['state'])
    user_form.select_city(form_data['city'])
    user_form.submit_form()

    result_validation(form_data)

    web_driver.quit_browser()


if __name__ == '__main__':
    config_file_path = os_path_join(getcwd(), 'config.ini')
    main(config_file_path)
