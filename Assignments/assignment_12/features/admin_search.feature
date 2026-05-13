Feature: Admin User Search

  Scenario: Filter users based on specific criteria
    Given the user is on the Admin User Management page
    When the user filters for users with the following details:

      | Username | User Role | Status  |
      | Admin    | Admin     | Enabled |

    And clicks the search button
    Then the search results should display the record for "Admin"
