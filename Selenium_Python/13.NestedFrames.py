from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/nested_frames")

# Switching to TOP Frame
driver.switch_to.frame("frame-top")

# Switching to Middle Frame
driver.switch_to.frame("frame-middle")

content = driver.find_element(By.ID,"content").text
print("Content in the middle frame:", content)

# Switch to Default content
driver.switch_to.default_content()

#Swicth to Bottom Frame
driver.switch_to.frame("frame-bottom")

content_Bottom = driver.find_element(By.TAG_NAME,"body").text
print("Content in the bottom frame:", content_Bottom)