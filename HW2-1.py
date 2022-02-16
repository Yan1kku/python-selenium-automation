from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path='C:\\Users\\BillieJean\\Desktop\\python-selenium-automation\\chromedriver.exe')

driver.get('https://www.amazon.com/gp/help/customer/display.html')


search = driver.find_element(By.ID, 'helpsearch')


search.clear()
search.send_keys('Cancel Order', Keys.ENTER)

actual_text = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
expected_text = 'Cancel Items or Orders'

assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

sleep(2)
driver.quit()
