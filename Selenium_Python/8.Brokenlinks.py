import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.eddymens.com/blog/page-with-broken-pages-for-testing-53049e870421"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)

all_links = driver.find_elements(By.TAG_NAME,"a")
print(f"Total number of links on the page : {len(all_links)}")

for link in all_links:
    href = link.get_attribute('href')
    # response = requests.get(href)
    response = requests.get(href, verify=False)
    if response.status_code >= 400:
        print(f"Broken Link: {href}(Status Code: {response.status_code})")
