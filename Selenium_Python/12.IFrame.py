import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(3)

iframe = driver.find_element(By.ID,"mce_0_ifr")
driver.switch_to.frame(iframe)
time.sleep(3)
Text_editor = driver.find_element(By.ID,"tinymce")
Text_editor.clear()
Text_editor.send_keys("This is my selenium with Python Tutorial")
time.sleep(4)

driver.switch_to.default_content()
selenium_link = driver.find_element(By.XPATH,"//a[normalize-space()='Elemental Selenium']")
selenium_link.click()
