import time
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

# Fill the details in the input fields

driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Atul")
driver.find_element(By.XPATH,"//input[contains(@id,'email')]").send_keys("atul08@gmail.com")
driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("9878767657")
driver.find_element(By.ID,"textarea").send_keys("Mamura, Gali No 2, Noida, 201301")
time.sleep(5)

# Select the radio buttons
driver.find_element(By.XPATH,"//input[@id='male']").click()
time.sleep(5)

# Select the checkBoxes
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")        #for scrolling
driver.find_element(By.ID,"tuesday").click()
driver.find_element(By.ID,"friday").click()
time.sleep(5)

# Select DropDown
dropDown_element = driver.find_element(By.ID,"country")
select = Select(dropDown_element)
select.select_by_value("australia")
time.sleep(5)

# Select list box's element
listBox_element = driver.find_element(By.ID,"colors")
select1 = Select(listBox_element)
select1.select_by_visible_text("Yellow")
time.sleep(5)

# Select from Sorted List box's element
sort_listBox = driver.find_element(By.ID,"animals")
select2 = Select(sort_listBox)
select2.select_by_index(3)
time.sleep(5)

# Select from Date Picker 1's element

driver.find_element(By.ID,"datepicker").click()
current_date = datetime.now()
next_date = current_date + timedelta(days=0)
formatted_date = next_date.strftime("%m/%d/%y")
driver.find_element(By.ID,"datepicker").send_keys(formatted_date)
time.sleep(4)

# Select fromDate Picker 2's element

driver.find_element(By.ID,"txtDate").click()
time.sleep(4)
current_date = datetime.now()
next_day = current_date + timedelta(days=1)

day = (str(next_day.day))
current_month = datetime.now().month
current_year = current_date.year

next_month = (current_month % 12) + 1
next_month_year = f"{next_month}"

month_dropdown = driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']")
select = Select(month_dropdown)
select.select_by_value(str(next_month_year))
year_dropdown = driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']")
select = Select(year_dropdown)
select.select_by_visible_text("2025")
driver.find_element(By.LINK_TEXT,day).click()
time.sleep(4)

# Select from search button
driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("Alert")
time.sleep(5)
driver.find_element(By.CLASS_NAME,"wikipedia-search-button").click()
time.sleep(5)
driver.refresh()
time.sleep(5)

# Select from Dynamic Button
driver.find_element(By.NAME,"start").click()
time.sleep(5)
driver.find_element(By.NAME,"stop").click()
time.sleep(5)
driver.refresh()
time.sleep(5)

# Select from Alerts & Popups
# 1st way

AlertButton = driver.find_element(By.ID,"alertBtn")
AlertButton.click()
alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
time.sleep(3)
alert.accept()
time.sleep(3)

# 2nd way

AlertButton1 = driver.find_element(By.ID,"confirmBtn")
AlertButton1.click()
alert1 = driver.switch_to.alert
alerttext1 = alert1.text
print(alerttext1)
time.sleep(3)
alert1.accept()
time.sleep(3)

# OR

AlertButton2 = driver.find_element(By.ID,"confirmBtn")
AlertButton2.click()
alert2 = driver.switch_to.alert
alerttext2 = alert2.text
print(alerttext2)
time.sleep(3)
alert2.dismiss()
time.sleep(3)

# 3rd Way

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
AlertButton3 = driver.find_element(By.ID,"promptBtn")
AlertButton3.click()
alert3 = driver.switch_to.alert
alerttext3 = alert3.text
print(alerttext3)
time.sleep(3)
alert3.send_keys("This is selenium with Python")
alert3.accept()
time.sleep(3)

# OR

AlertButton4 = driver.find_element(By.ID,"promptBtn")
AlertButton4.click()
alert4 = driver.switch_to.alert
alerttext4 = alert4.text
print(alerttext4)
time.sleep(3)
alert4.send_keys("This is selenium with Python")
alert4.dismiss()
time.sleep(3)

# # Select New tab's element
#
# new_tab = driver.find_element(By.XPATH,"(//div[@class='widget-content']/button)[5]")
# new_tab.click()
# driver.switch_to.new_window()
# time.sleep(5)
# number_of_tabs = len(driver.window_handles)
# print(number_of_tabs)
# # tabs_value = driver.window_handles
# # print(tabs_value)
# # current_tab = driver.current_window_handle
# # print(current_tab)
# # driver.find_element(By.CLASS_NAME,"getStarted_Sjon").click()
# # time.sleep(2)
# # first_tab = driver.window_handles[0]
# # if current_tab != first_tab:
# #     driver.switch_to.window(first_tab)
# # driver.find_element(By.XPATH,"//a[contains(@data-test-id,'signup-button')]").click()
# # time.sleep(4)

# Select from Mouse Hover

actions = ActionChains(driver)
hover_element = driver.find_element(By.CLASS_NAME,"dropbtn")
time.sleep(5)
actions.move_to_element(hover_element).perform()
time.sleep(5)
driver.find_element(By.XPATH,"(//div[@class='dropdown-content']/a)[2]").click()
time.sleep(5)

# Select Double Click element
button = driver.find_element(By.XPATH,"//button[@ondblclick='myFunction1()']")
actions.double_click(button).perform()
time.sleep(5)

# Select Drag & Drop
source_element = driver.find_element(By.ID,"draggable")
destination_element = driver.find_element(By.ID,"droppable")
actions.drag_and_drop(source_element,destination_element).perform()
time.sleep(5)