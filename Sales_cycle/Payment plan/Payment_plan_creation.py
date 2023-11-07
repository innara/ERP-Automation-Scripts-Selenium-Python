import time
from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.execute_script("document.body.style.zoom='70%'")
# Navigate to Google.com
driver.get("https://dev.j7konnect.com/login")
driver.maximize_window()
driver.execute_script("document.body.style.zoom='75%'")

# Find the search box element and enter a search query
email = driver.find_element(By.NAME, "email")
email.send_keys("")
password = driver.find_element(By.NAME, "password")
password.send_keys("")
# Close the browser
time.sleep(2)
driver.execute_script("document.body.style.zoom='100%'")
login = driver.find_element(By.ID, "sign-in")
login.submit()
if "dashboard" in driver.current_url:
    print("Login successful Your credentials are correct!")
else:
    print("Login failed. Please check your credentials.")
time.sleep(5)
target_element = driver.find_element(By.XPATH, '//*[@id="layout-menu"]/ul/li[18]/a')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[18]/a')))
button.click()
try:
    deal = driver.find_element(By.XPATH, '//*[@id="layout-menu"]/ul/li[18]/ul/li[1]/a')
    driver.execute_script("arguments[0].scrollIntoView();", deal)
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[18]/ul/li[1]/a')))
    button.click()
    time.sleep(2)
except Exception as e:
    print("An error occurred:", str(e))
time.sleep(4)
new = driver.find_element(By.XPATH,'//*[@id="sales-plan-table_wrapper"]/div[1]/div[2]/div/div[2]/button')
new.click()
driver.find_element(By.XPATH,'//*[@id="sales-plan-table_wrapper"]/div[1]/div[2]/div/div[2]/div[2]/div/a[1]').click()
time.sleep(4)
# selecting unit from dropdown to create salesplan
dropdown_element = driver.find_element(By.XPATH, '//*[@id="unit_id"]')
dropdown = Select(dropdown_element)
dropdown.select_by_index(1)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(5)
# installements
Text = driver.find_element(By.XPATH, '//*[@id="installments_acard"]/div[2]/div[1]/div/div/div[3]/div/div/input')
driver.execute_script("arguments[0].click();", Text)
Text.send_keys('2')
time.sleep(5)
dropdown_el = driver.find_element(By.XPATH, '//*[@id="stackholders"]')
dropdown = Select(dropdown_el)
dropdown.select_by_index(1)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(3)
dropdown_e = driver.find_element(By.XPATH, '//*[@id="sales_source_lead_source"]')
dropdown = Select(dropdown_e)
dropdown.select_by_index(1)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(3)
try:
 driver.find_element(By.XPATH,'//*[@id="savebtn"]').click()
 time.sleep(6)

 alert = Alert(driver)

 alert_message = alert.text

 print(f"Alert Message: {alert_message}")

except NoAlertPresentException:
 print("No success alert found . The action may have failed.")

driver.quit()