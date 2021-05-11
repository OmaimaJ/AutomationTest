# Created by Omaima Uchiha at 5/11/2021
Feature: Customer service

  Scenario Outline:
    Given launch chrome browser
    When The AutomationPractice site is open
    And The contact us link is clicked
    And Select subject heading '<heading>'
    And enter email address '<email>'
    And message '<message>'
    Then click on the send button
    Examples:
      |heading  |email|message|
      | Customer service | example2@email.com | order has not arrived        |
      | -- Choose --     | example2@email.com | order has not arrived        |
      | Webmaster        | empty              | I need help placing an order |
      | Webmaster        | example2@email.com | empty                        |