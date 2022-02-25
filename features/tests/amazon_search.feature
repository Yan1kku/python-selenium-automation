# Created by BillieJean at 2/23/2022
Feature: Test for Amazon search
  # Enter feature description here

  Scenario: User can search for a coffee
    Given Open Amazon
    When Search for coffee
    Then Verify search results are shown for "coffee"

    Scenario: User can search for a table
    Given Open Amazon
    When Search for table
    Then Verify search results are shown for "table"

      Scenario: User can add a product to the cart
        Given Open Amazon
        When Search for Pillow
        And Click on the first product
        And Click on Add to cart Button
        And Open cart page
        Then Verify cart has 1 item(s)
