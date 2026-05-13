import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest_check as check

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    yield driver
    driver.quit()

def test_simple_is_alert(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Alert", 'Alert Text was wrong'
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, 'result').text
    assert "You successfully clicked an alert" in result, 'Result text was wrong'


def test_js_confirmdismiss(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm", 'Alert Text was wrong'
    time.sleep(3)
    alert.dismiss()
    time.sleep(3)
    result = driver.find_element(By.ID, 'result').text
    assert "You clicked: Cancel" in result, "Result text was wrong"

def test_js_confirmok(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS Confirm", 'Alert Text was wrong'
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, 'result').text
    assert "You clicked: Ok" in result, "Result text was wrong"

def test_js_prompt(driver):
    driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
    alert = driver.switch_to.alert
    assert alert.text == "I am a JS prompt", 'Alert Text was wrong'
    alert.send_keys("Selenium Python")
    time.sleep(3)
    alert.accept()
    time.sleep(3)
    result = driver.find_element(By.ID, 'result').text
    assert "Selenium Python" in result, "Result text was wrong"