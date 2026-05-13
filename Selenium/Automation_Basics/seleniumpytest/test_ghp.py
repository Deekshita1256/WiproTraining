import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest_check as check

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.google.com")
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle = driver.title
    assert pagetitle == 'Google', 'google Home Page Not Loaded'

def test_imagepageload(driver):
    driver.find_element(By.LINK_TEXT, "Images").click()
    pagetitle = driver.title
    assert pagetitle == 'Google Images', 'Image Page Not Found'

def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT, "Business").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_contains('Business'))
    # assert 'Business' in driver.title, 'Business Page Not Loaded - Title Check'
    # assert 'business' in driver.current_url, 'Business Page Not Loaded - URL Check'
    check.is_in("Business", driver.title, "Business Page Not Loaded - Title Check")
    #check.equal(driver.title, 'Business', "Business Page Not Loaded - Title Check")
    check.is_in('business', driver.current_url, "Business Page Not Loaded - URL Check")
