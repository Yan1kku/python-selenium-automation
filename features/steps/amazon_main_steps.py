from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver


SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
HAM_MENU_ICON = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')

@given('Open Amazon')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Search for {keyword}')
def search_product(context, keyword):
    context.driver.find_element(*SEARCH_INPUT).send_keys(keyword)
    context.driver.find_element(*SEARCH_BTN).click()


@then('Verify hamburger menu present')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_MENU_ICON)


#@then('Verify 38 links present')
#def verify_fotter_links_amount(context):
 #   links = context.driver.find_elements(*FOOTER_LINKS)
  #  print(links)
   # assert len(links) == 38, f'Expected 38 links but got {len(links)}'


@then('Verify {expected_amount} links present')
def verify_footer_limks_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links_amount = len(context.driver.find_elements(*FOOTER_LINKS))
    assert links_amount == expected_amount, f'Expected {expected_amount} links but got {links_amount}'