Feature: Employee Management

  Scenario Outline: Add multiple new employees
    Given the user is logged into the PIM module
    When the user clicks on the "Add Employee" button
    And enters "<FirstName>" and "<LastName>"
    And clicks the save button
    Then the new employee "<FirstName> <LastName>" should be successfully created

    Examples:

      | FirstName | LastName |
      | John      | Doe      |
      | Jane      | Smith    |
      | Alice     | Cooper   |
