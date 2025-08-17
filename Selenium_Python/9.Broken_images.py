import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()
images = driver.find_elements(By.TAG_NAME,"img")
broken_images = []
time.sleep(4)
for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken Link found")

if broken_images:
    print("List of broken images: ")
    for broken_image in broken_images:
        print(broken_image)
else:
    print("No Broken Images found!")