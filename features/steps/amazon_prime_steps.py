from selenium.webdriver.common.by import By
from behave import given, when, then

DELIVERY_BEFITS = (By.ID, 'prime-benefit-module-content-delivery-item')


@given('Open Amazon Prime')
def open_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


#@then('Verify user can see 3 delivery benefits')
#def verify_delivery_befits(context):
#    benefits_amount = len(context.driver.find_elements(*DELIVERY_BEFITS))
#    assert benefits_amount == 3, f'Expected 3 benefits, but got {benefits_amount}'


@then('Verify user can see {expected_amount} delivery benefits')
def verify_delivery_befits(context, expected_amount):
    benefits_amount = len(context.driver.find_elements(*DELIVERY_BEFITS))
    assert benefits_amount == int(expected_amount), f'Expected {expected_amount} benefits, but got {benefits_amount}'