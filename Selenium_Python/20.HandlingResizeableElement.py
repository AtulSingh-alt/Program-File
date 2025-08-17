import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://demo.automationtesting.in/Resizable.html"
driver.get(url)
resizable_element = driver.find_element(By.XPATH,"//div[@class='ui-resizable-handle ui-resizable-se ui-icon ui-icon-gripsmall-diagonal-se']")
initial_element_size = driver.find_element(By.ID,"resizable")
initial_size = initial_element_size.size
print("Initial Size :", initial_size)
time.sleep(5)
action_chains = ActionChains(driver)
action_chains.click_and_hold(resizable_element).move_by_offset(100,100).release().perform()
time.sleep(5)
resized_element = initial_element_size.size
print("Resized Element:", resized_element)