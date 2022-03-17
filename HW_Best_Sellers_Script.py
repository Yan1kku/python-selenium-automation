from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

actual_text = driver.find_element(By.XPATH, "//*[@id='zg_banner_text']").text
expected_text = 'Amazon Best Sellers'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'


sleep(8)

driver.quit()