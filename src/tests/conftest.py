from pytest import fixture
import allure

from src.settings import get_form_data, WebDriverSDET


@fixture(name='set_up')
def create_session_and_get_form_data():
    """Starts local driver, gets form URL, generates form data, and quit after test running."""
    allure.dynamic.title("setUp and tearDown")

    web_driver = WebDriverSDET()
    form_data = get_form_data()
    web_driver.get_form_url()

    yield form_data, web_driver.get_driver()

    web_driver.quit_browser()
