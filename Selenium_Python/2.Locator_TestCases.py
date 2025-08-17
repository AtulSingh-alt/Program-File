import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)
# UserName = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='username']")))
# UserName.send_keys("Admin")
# Password = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@name='password']")))
# Password.send_keys("admin123")
# Submit = wait.until(EC.visibility_of_element_located((By.XPATH,"//button[@type='submit']")))
# Submit.click()
# time.sleep(3)
# title = driver.title
# print(title)
# assert "OrangeHRM" in title

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
time.sleep(3)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
title = driver.title
assert "OrangeHRM" in title
driver.close()