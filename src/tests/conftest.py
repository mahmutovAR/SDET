from pytest import fixture
from time import sleep

from src.settings import get_form_data, WebDriverSDET


@fixture(name='set_up')
def create_session_and_get_form_data():
    web_driver = WebDriverSDET()
    form_data = get_form_data()
    web_driver.get_form_url()
    sleep(2)

    yield form_data, web_driver

    web_driver.quit_browser()
