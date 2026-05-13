Feature: Leave Application Workflow

  Scenario: Apply for Medical Leave and verify status
    Given the user is on the "Apply Leave" page
    When the user selects "Medical Leave" from the Leave Type dropdown
    And selects a valid date range
    And clicks the "Apply" button
    Then a success toast message should appear
    And the "Leave Balance" for Medical Leave should be reduced
    And the status of the request should be "Pending Approval"
