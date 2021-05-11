# Created by Omaima Uchiha at 5/11/2021
Feature: redirect page
  redirecting user to a different page

  Scenario: User is redirected to homepage
    Given launch chrome browser
    When The AutomationPractice site has dresses loaded
    And the banner is clicked
    Then the homepage is loaded
