import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def browser():
    options = Options()
    options.headless = True
    # Set up the Chrome WebDriver
    driver = webdriver.Chrome(options=options) # Make sure ChromeDriver is in your PATH
    yield driver
    driver.quit()