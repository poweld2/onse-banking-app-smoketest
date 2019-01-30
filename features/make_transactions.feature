Feature: Make transactions
  As an account holder
  In order to keep my money nice and safe
  I want to deposit it into and withdraw it from my account

  Scenario: Successful deposit
    Given there is a customer "Jez Humble"
    And "Jez Humble" has a new account
    When I deposit 50 the account
    When I withdraw 20 the account
    Then then balance of the account should be 30

Feature: Change name
  As an account holder I want to change my name
  In order to keep my account up to date
  I want to update my account details

  Scenario: Successful details created
    Given there is a customer "Jez Humble"
    And "Jez Humble" has a new name
    When "Jez Blah" changes his name
    Then then "Jez Blah" will be created in a new account
