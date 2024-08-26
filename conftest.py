import pytest
from selenium import webdriver
from data import SCOOTER_WEBSITE, SCREEN_RESOLUTION


@pytest.fixture(scope="function")
def driver():
    firefox_options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(*SCREEN_RESOLUTION)
    driver.get(SCOOTER_WEBSITE)
    yield driver
    driver.quit()
