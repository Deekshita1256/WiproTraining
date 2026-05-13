import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest_check as check

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    yield driver
    driver.quit()

def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    assert "amazon" in driver.title, 'Title for amazon is not correct'
    print("\nOpened Amazon Homepage. Title verified.")

def test_search_product(driver):
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("wireless mouse")

    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()
    assert driver.current_url.__contains__('wireless'), 'Search result page did not load'
    assert driver.title.__contains__('wireless'), 'Search result page did not load'
    print("\nsearch results page loaded successfully")