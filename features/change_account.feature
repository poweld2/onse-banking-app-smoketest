
Feature: Change name
  As an account holder I want to change my name
  In order to keep my account up to date
  I want to update my account details

  Scenario: Successful details created
    Given there is a customer "Jez Humble"
    And "Jez Humble" has a new name
    When "Jez Blah" changes his name
    Then then "Jez Blah" will be created in a new account
