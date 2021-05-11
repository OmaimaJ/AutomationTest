# Created by Omaima Uchiha at 5/10/2021
Feature: Sign In
  User email and password are entered

  Scenario Outline:
    Given launch chrome browser
    When The AutomationPractice site is open
    And The Sign In link is clicked
    And The Email '<email>' and Password '<password>' are entered'
    And The Sign In button is clicked
    Then User account loads
    Examples:
      | email              | password |
      | x@y.com            |          |
      | X.com              | password |
      | x.com              |          |
      | example2@email.com | password |
