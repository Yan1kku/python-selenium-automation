# Created by BillieJean at 3/7/2022
Feature: Tests for Amazon Main Page


  Scenario: User can see hamburger menu
  Given Open Amazon
  Then Verify hamburger menu present


  Scenario: User can see footer links
    Given Open Amazon
    Then Verify 38 links present