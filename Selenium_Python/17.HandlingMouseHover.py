import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
actions = ActionChains(driver)
hover_element = driver.find_element(By.XPATH,"(//a[@class='dropdown-toggle'])[1]")
time.sleep(5)
actions.move_to_element(hover_element).perform()
driver.find_element(By.XPATH,"//a[normalize-space()='Frames']").click()
time.sleep(5)
