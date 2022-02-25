from behave import when, given, then
from selenium.webdriver.common.by import By

RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price-whole']]")


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('Verify search result {expected_result}')
def verify_result(context, expected_result):
    actual_result = context.driver.find_element(*RESULT).text
    assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}"
