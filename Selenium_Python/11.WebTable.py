import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,700)")
time.sleep(4)
table = driver.find_element(By.ID,"countries")
rows = table.find_elements(By.TAG_NAME,"tr")
row_count = len(rows)
print(row_count)
target_value = "Euro"
found = False
for row in rows:
    cells = row.find_elements(By.TAG_NAME,"td")
    for cell in cells:
        if target_value in cell.text:
            print(f"Found the value: {target_value}")
            found = True
            break
    if found:
        break
if not found:
    print(f"Target Value {target_value} not found")