import time
from collections import Counter
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
# Define the initial URL
driver.get("https://dev.j7konnect.com/login")
driver.maximize_window()
email = driver.find_element(By.NAME, "email")
email.send_keys("dummy.com")
password = driver.find_element(By.NAME, "password")
password.send_keys("dummy")
time.sleep(2)
driver.execute_script("document.body.style.zoom='100%'")
login = driver.find_element(By.ID, "sign-in")
login.submit()
if "dashboard" in driver.current_url:
    print("Login successful Your credentials are correct!")
else:
    print("Login failed. Please check your credentials.")
time.sleep(5)

url = 'https://dev.j7konnect.com/permissions'
driver.get(url)
time.sleep(5)
element = driver.find_element(By.XPATH, '//*[@id="permissions-table_length"]/label/select/option[5]')
element.click()
time.sleep(12)
table_locator = '//*[@id="permissions-table"]'
table = driver.find_element(By.XPATH,table_locator)
header_cells = table.find_elements(By.TAG_NAME,"th")
th_texts = set()
duplicates = []
for th in header_cells:
    text = th.text
    if text in th_texts:
        duplicates.append(text)
    else:
        th_texts.add(text)
if duplicates:
    print("There are few group duplications found")
    for duplicate in duplicates:
        print(duplicate)
else:
    print("No duplication found")

driver.quit()





