# Created by Omaima Uchiha at 5/11/2021
Feature: redirect to homepage


  Scenario: Another way to redirect user to homepage
    Given launch chrome browser
    When The AutomationPractice site has dresses loaded
    And the logo is clicked
    Then the homepage is loaded