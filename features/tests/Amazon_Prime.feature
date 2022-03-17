# Created by BillieJean at 3/7/2022
Feature: Test Amazon Prime page
  # Enter feature description here

  Scenario: User can see Amazon Prime delivery benefits
    Given Open Amazon Prime
    Then Verify user can see 3 delivery benefits
