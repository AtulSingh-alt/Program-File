import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
source_element = driver.find_element(By.ID,"column-a")
destination_element = driver.find_element(By.ID,"column-b")
actions = ActionChains(driver)
actions.drag_and_drop(source_element,destination_element).perform()
time.sleep(5)
