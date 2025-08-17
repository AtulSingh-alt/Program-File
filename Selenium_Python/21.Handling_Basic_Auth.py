import time

from selenium import webdriver

username = "admin"
password = "admin"
driver = webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(5)

#https://username:password@domain/path
