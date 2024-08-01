from os import environ

from selenium import webdriver

from errors import EnvVarError


def get_env_var(var_name: str) -> str:
    """Returns value of the environment variable if it is valid,
    otherwise the EnvVarError is raised."""
    try:
        var_value = environ[var_name]
    except KeyError:
        raise EnvVarError(var_name)
    else:
        if not var_value or var_value.isspace():
            raise EnvVarError(var_name)
        return var_value


FORM_URL = get_env_var('PRACTICE_FORM_URL')


WebDriver = webdriver.Chrome()
js_scroll_code = "arguments[0].scrollIntoView();"


def get_form_url() -> None:
    WebDriver.get(FORM_URL)


def scroll_to_element(locator) -> None:
    WebDriver.execute_script(js_scroll_code, locator)


def quit_browser() -> None:
    WebDriver.quit()


