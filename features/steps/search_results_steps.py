from behave import then
from selenium.webdriver.common.by import By

RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//*[contains(@class, 'widgetId=search-results_1')]//span[text()='36']")


@then('Verify search results are shown for {expected_result}')
def verify_result(context, expected_result):
    actual_result = context.driver.find_element(*RESULT).text
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'