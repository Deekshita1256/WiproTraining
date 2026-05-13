@Regression @Profile
Feature: Profile Update

  Scenario: Update Nick Name and Profile Photograph
    Given the user is on the "My Info" section
    When the user changes the Nick Name to "TechWizard"
    And the user uploads a profile photograph "profile_pic.jpg"
    And clicks the "Save" button
    Then the personal details should be updated successfully
    And the new profile picture should be visible
