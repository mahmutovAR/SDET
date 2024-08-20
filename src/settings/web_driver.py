from selenium import webdriver


class WebDriverSDET:
    """Class to start local driver, get specified URL and quit after test case running."""
    def __init__(self):
        self.web_driver = webdriver.Chrome()
        self.form_url = 'https://demoqa.com/automation-practice-form'
        self.web_driver.maximize_window()

    def get_driver(self) -> webdriver:
        return self.web_driver

    def get_form_url(self) -> None:
        self.web_driver.get(self.form_url)

    def quit_browser(self) -> None:
        self.web_driver.quit()
