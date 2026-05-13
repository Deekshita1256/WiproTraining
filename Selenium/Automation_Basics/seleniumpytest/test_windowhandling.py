import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest_check as check

@pytest.fixture
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")
    yield driver
    driver.quit()

def test_multiple_windows_handle(driver):
    wait = WebDriverWait(driver, 10)
    parent_window = driver.current_window_handle
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    time.sleep(3)
    all_windows = driver.window_handles
    assert len(all_windows) == 2, "New window did not open"
    for cwindow in all_windows:
        if cwindow != parent_window:
            driver.switch_to.window(cwindow)
            time.sleep(3)
            break
    time.sleep(3)
    header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h3"))).text
    assert header == "New Window", 'New Window Switch did not happen'
    time.sleep(3)
    driver.close()
    driver.switch_to.window(parent_window)
    time.sleep(3)
    assert driver.title == "The Internet", 'Parent window switch did not happen'

def test_open_multiple_tabs(driver):
    new_window_link = driver.find_element(By.LINK_TEXT, "Click Here")

    for _ in range(3):
        new_window_link.click()
        time.sleep(3)

    handles = driver.window_handles
    assert len(handles) == 4, "Multiple Windows did not open"

    # Switch through each tab and verify header
    for handle in handles:
        driver.switch_to.window(handle)
        time.sleep(3)
        if handle != handles[0]:
            header = driver.find_element(By.TAG_NAME, "h3").text
            assert header == "New Window", 'New Window switch did not happen'
            driver.close()