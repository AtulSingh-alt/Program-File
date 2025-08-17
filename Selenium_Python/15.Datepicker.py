import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url="https://www.globalsqa.com/demo-site/datepicker/"
driver.get(url)

driver.find_element(By.XPATH,"(//div[contains(@class,'attention closable')])[1]")
frameLo = driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
driver.switch_to.frame(frameLo)
time.sleep(3)
driver.find_element(By.ID,"datepicker").click()

current_date = datetime.now()
next_date = current_date + timedelta(days=0)
formatted_date = next_date.strftime("%m/%d/%y")
driver.find_element(By.ID,"datepicker").send_keys(formatted_date + Keys.TAB)
time.sleep(4)
