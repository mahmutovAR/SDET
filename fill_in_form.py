from os import environ
environ['PRACTICE_FORM_URL'] = 'https://demoqa.com/automation-practice-form'


from form import StudentRegistrationForm
from os.path import join as os_path_join
from os import getcwd
import web_driver


web_driver.get_form_url()
User_form = StudentRegistrationForm()

form_data = {'first_name': 'Joseph David',
             'last_name': 'Smith',
             'email': 'jd.koln@td-group.com',
             'gender': 'MaLe',
             'mobile': '8087971551',
             'birth_date': '15 05 1978',
             'subjects': ['Accounting', 'Arts', 'Biology', 'Chemistry', 'Civics', 'Commerce'],
             'hobbies': ['Sports', 'Reading', 'Music'],
             'picture': os_path_join(getcwd(), 'pictures', 'ebersteiger.jpg'),
             'address': 'Gramin Rd, Kapil Sharad 3451',
             'state': 'Haryana',
             'city': 'Panipat'}


User_form.fill_in_firstname(form_data['first_name'])
User_form.fill_in_last_name(form_data['last_name'])
User_form.fill_in_email(form_data['email'])
User_form.select_gender(form_data['gender'])
User_form.fill_in_mobile(form_data['mobile'])
User_form.fill_in_birth_date(form_data['birth_date'])
User_form.fill_in_subjects(form_data['subjects'])
User_form.select_hobby(form_data['hobbies'])
User_form.upload_picture(form_data['picture'])
User_form.fill_in_address(form_data['address'])
User_form.select_state(form_data['state'])
User_form.select_city(form_data['city'])
User_form.submit_form()

print('assert results')

web_driver.quit_browser()

