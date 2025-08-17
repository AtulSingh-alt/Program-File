import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element(By.ID,"sunday").click()
time.sleep(4)
driver.find_element(By.ID,"sunday").click()
time.sleep(4)
checkboxes = driver.find_element(By.ID,"saturday").click()
time.sleep(4)

