import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url)

# #1st way
# AlertButton = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
# AlertButton.click()
# alert = driver.switch_to.alert
# alerttext = alert.text
# print(alerttext)
# time.sleep(3)
# alert.accept()
# time.sleep(3)

# #2nd way
# AlertButton = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Confirm']")
# AlertButton.click()
# alert = driver.switch_to.alert
# alerttext = alert.text
# print(alerttext)
# time.sleep(3)
# alert.dismiss()
# time.sleep(3)

#3rd way
AlertButton = driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
AlertButton.click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
time.sleep(3)
alert.send_keys("This is selenium with Python")
alert.accept()
time.sleep(3)