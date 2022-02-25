from behave import then
from selenium.webdriver.common.by import By

RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")

@then('Verify search results are shown for {expected_result}')
def verify_result(context, expected_result):
    actual_result = context.driver.find_element(*RESULT).text
    assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'