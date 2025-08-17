import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
login_url = "https://testautomationpractice.blogspot.com/"
driver.get(login_url)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

dropdown_element = driver.find_element(By.ID,"country")
target_value = "Australia"
select = Select(dropdown_element)
# select.select_by_visible_text("Canada")
# select.select_by_index(3)
# select.select_by_value("uk")

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"Selected option is {target_value}")
        break
else:
    print(f"Option {target_value} not found")
time.sleep(4)