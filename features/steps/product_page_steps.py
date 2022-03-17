from selenium.webdriver.common.by import By
from behave import when, given, then
from time import sleep

ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@then('Verify user can click through colors')
def verify_color_click(context):
    expected_colors = ['Blue', 'Matte Black', 'Red', 'White', 'Defiant Black-Red', 'Midnight Black', 'Shadow Gray']
    color_options = context.driver.find_elements(*COLOR_OPTIONS)

   # Option 1
   # actual_colors = []
    #for color in color_options:
     #   color.click()
      #  current_color_name = context.driver.find_element(*CURRENT_COLOR).text
       # actual_colors += [current_color_name]

   # assert expected_colors == actual_colors, f'Actual {actual_colors} do not match expected {expected_colors}'


    #Option 2
    for i in range(len(color_options)):
        print('i:', i)
        color_options[i].click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print('current_color:', current_color)
        assert current_color == expected_colors[i]
