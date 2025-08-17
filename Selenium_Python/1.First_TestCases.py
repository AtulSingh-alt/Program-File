from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://selenium.dev/documentation")
driver.maximize_window()
title = driver.title
print(title)
assert "The Selenium Browser Automation Project | Selenium" in title


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# service = Service("C:/Program Files/Python313/Scripts/chromedriver.exe")
# browser = webdriver.Chrome(service=service)