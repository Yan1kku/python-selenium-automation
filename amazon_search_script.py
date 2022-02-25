from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path='C:\\Users\\BillieJean\\Desktop\\python-selenium-automation\\chromedriver.exe')

driver.get('https://www.amazon.com')


driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')

driver.find_element(By.ID, 'nav-search-submit-button').click()

expected_result = '"coffee"'
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text


assert expected_result == actual_result, f'Expected {expected_result}, but got {actual_result}'
print('Test case passed')
sleep(2)
driver.quit()