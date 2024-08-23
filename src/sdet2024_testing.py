from os import mkdir
from os import system as os_system
from os.path import join as os_path_join
from os.path import isdir
from webbrowser import open as webbrowser_open


FILES_DIR = os_path_join('allure_files')
REPORT_HTML = os_path_join('allure-report', 'index.html')
ENVIRONMENT_FILE = os_path_join(FILES_DIR, 'environment.properties')
ENVIRONMENT_INFORMATION = ['os_platform = Linux\n',
                           'os_release = 6.8.0-40-generic\n',
                           'os_version = Ubuntu 24.04 LTS\n',
                           'python_version = Python 3.10.14']


def main():
    set_up_allure_report()
    run_tests()
    generate_and_open_report()


def set_up_allure_report():
    if not isdir(FILES_DIR):
        mkdir(FILES_DIR)
        print('  1> make dir')

    with open(ENVIRONMENT_FILE, 'w') as env_file:
        for line in ENVIRONMENT_INFORMATION:
            env_file.write(line)


def run_tests():
    os_system(f'pytest tests/ -n 4 --alluredir={FILES_DIR} --clean-alluredir')


def generate_and_open_report():
    os_system(f'allure generate --single-file {FILES_DIR}')
    webbrowser_open(REPORT_HTML)


if __name__ == '__main__':
    main()
