import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
driver.get(url)
driver.find_element(By.ID,"datepicker2").click()
time.sleep(4)
current_date = datetime.now()
print(current_date)

next_day = current_date + timedelta(days=1)
print(next_day)

day = (str(next_day.day))
print(day)
current_month = datetime.now().month
current_year = current_date.year

next_month = (current_month % 12) + 1
next_month_year = f"{next_month}/{current_year}"

month_dropdown = driver.find_element(By.XPATH,"//select[@title='Change the month']")
select = Select(month_dropdown)
select.select_by_value(str(next_month_year))
year_dropdown = driver.find_element(By.XPATH,"//select[@title='Change the year']")
select = Select(year_dropdown)
select.select_by_visible_text("2024")
driver.find_element(By.LINK_TEXT,day).click()
time.sleep(4)