import pytest
from pages.home_page import HomePage


def test_exercise_5_login_failure_screenshot(driver):
    home = HomePage(driver)
    login_modal = home.click_login()

    # Step 1: Submit user handle alongside an incorrect passcode
    alert_text = login_modal.login_with_credentials("valid_user_123", "wrong_password")

    # Step 2: Validate the actual alert message returned by Demoblaze
    assert alert_text == "Please fill out Username and Password."

    # Step 3: Trigger your intentional failure challenge to force the conftest screenshot hook
    assert alert_text == "Success", "Intentional failure to trigger Allure screenshot attachment."
