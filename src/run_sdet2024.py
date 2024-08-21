from src.settings import fill_in_fields_and_submit_form, get_form_data, validate_entered_form_data, WebDriverSDET


def main():
    web_driver = WebDriverSDET()
    form_data = get_form_data()
    web_driver.get_form_url()
    fill_in_fields_and_submit_form(web_driver.get_driver(), form_data)
    validate_entered_form_data(web_driver.get_driver(), form_data)
    web_driver.quit_browser()


if __name__ == '__main__':
    main()
