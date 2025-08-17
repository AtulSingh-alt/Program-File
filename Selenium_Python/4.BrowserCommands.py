import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
# driver.minimize_window()
# driver.fullscreen_window()
time.sleep(3)
driver.find_element(By.XPATH,"//div[contains(@class,'orangehrm-login-forgot')]/p").click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.close()
