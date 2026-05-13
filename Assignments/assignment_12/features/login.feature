Feature: User Authentication

  Background:
    Given the user navigates to the login page "https://opensource-demo.orangehrmlive.com/"

  @Smoke
  Scenario: Successful login with valid credentials
    When the user enters username "Admin" and password "admin123"
    And clicks the login button
    Then the user should be redirected to the Dashboard

  Scenario: Unsuccessful login with invalid password
    When the user enters username "Admin" and password "wrong123"
    And clicks the login button
    Then an error message "Invalid credentials" should be displayed
