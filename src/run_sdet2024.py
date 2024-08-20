from src.settings import fill_in_form, get_full_form_data, result_validation, WebDriverSDET


def main():
    web_driver = WebDriverSDET()
    form_data = get_full_form_data()
    web_driver.get_form_url()
    fill_in_form(web_driver.get_driver(), form_data)
    result_validation(web_driver.get_driver(), form_data)
    web_driver.quit_browser()


if __name__ == '__main__':
    main()
