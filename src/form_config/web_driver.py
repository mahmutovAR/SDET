from selenium import webdriver


WebDriver = webdriver.Chrome()
js_scroll_code = "arguments[0].scrollIntoView();"


def get_form_url(input_url) -> None:
    WebDriver.get(input_url)


def scroll_to_element(locator) -> None:
    WebDriver.execute_script(js_scroll_code, locator)


def quit_browser() -> None:
    WebDriver.quit()


