import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
driver.find_element(By.ID,"react-burger-menu-btn").click()

element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//a[@id='logout_sidebar_link']")))
element.click()