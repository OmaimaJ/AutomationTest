# Created by Omaima Uchiha at 5/10/2021
Feature: registration

  Scenario Outline:
    Given launch chrome browser
    When The AutomationPractice site is open
    And The Sign In link is clicked
    And Email is entered to register an account '<email>'
    And the create an account button is clicked
    And registration page loads
    And select title
    And First name '<firstname>'
    And Last name '<lastname>'
    And Password '<Password>'
    And Date Of Birth '<Date>'
    And Date Of Month '<Month>'
    And Date Of Year '<Year>'
    And select newspaper
    And select optin
    And Address '<Address>'
    And City '<City>'
    And State '<State>'
    And Zip/postal Code '<ZipCode>'
    And Phone Number '<phoneNumber>'
    And the Register button is clicked
    Then The user account page loads
    Examples:
      | email                 | firstname | lastname | Password        | Date  | Month | Year  | Address           | City     | State      | ZipCode | phoneNumber |
      | example12@email.com   | Sasuke    | Uchiha   | password        | 15    | 5     | 1999  | Example street 19 | Debrecen | California | 12345   | 1234567     |
      | example_e12@email.com | Bob       | Example  | anotherpassword | 23    | 6     | 2000  | Test plaza  9     | Budapest | Texas      | 98765   | 9876654     |
      | xx@y.com              | a         | empty    | thirdpassword   | 14    | 7     | 2020  | Example street 99 | Budapest | Texas      | 33333   | 1922574     |
      | xxx@y.com             | a         | b        | empty           | 14    | 7     | 2020  | Example street 99 | Budapest | Texas      | 44444   | 1922574     |
      | x@yyy.com             | a         | b        | thirdpassword   | empty | empty | empty | empty             | empty    | Texas      | empty   | empty       |
