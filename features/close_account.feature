Feature: Close Account
  As an account holder I want to close my account
  In order to remove my account from bank

  Scenario: Successful details created
    Given there is a customer "Jez Humble"
    And "Jez Humble" has a new account
    When "Jez Humble" account is deleted
    Then then "Jez Humble" account will be closed from accounts
