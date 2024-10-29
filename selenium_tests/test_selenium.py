import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from constants import Constants


def test_find_iphone(browser):
    #Step 1
    browser.get(Constants.MAIN_PAGE_URL)

    #Step 2
    findInput = browser.find_element(By.CSS_SELECTOR, Constants.FIND_INPUT_SELECTOR)
    
    #Step 3
    findInput.send_keys(Constants.FIND_INPUT_TEXT)

    #Step 4
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, Constants.IPHONE_IN_FIND_SELECTOR)))
    iPhoneFind = browser.find_element(By.XPATH, Constants.IPHONE_IN_FIND_SELECTOR)
    iPhoneFind.click()
    
    #Assert
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, Constants.IPHONE_IN_CONSTRUCTOR_SELECTOR)))
    iPhoneConstruct = browser.find_element(By.XPATH, Constants.IPHONE_IN_CONSTRUCTOR_SELECTOR)
    assert iPhoneConstruct.is_displayed
