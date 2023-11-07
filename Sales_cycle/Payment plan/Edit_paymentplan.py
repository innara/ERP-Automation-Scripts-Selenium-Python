import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a WebDriver instance for Google Chrome
driver = webdriver.Chrome()
driver.execute_script("document.body.style.zoom='70%'")
# Navigate to Google.com
driver.get("https://dev.j7konnect.com/login")
driver.maximize_window()
driver.execute_script("document.body.style.zoom='75%'")

# Find the search box element and enter a search query
email = driver.find_element(By.NAME, "email")
email.send_keys("admin@erp.com")
password = driver.find_element(By.NAME, "password")
password.send_keys("password")
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
# searching for specific salesplan
driver.find_element(By.XPATH, '//*[@id="sales-plan-table_filter"]/label/input').send_keys('PP-46')
time.sleep(5)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.XPATH, ' //*[@id="dropdownMenuButton100"]')))
element.click()
time.sleep(3)
# overlapping the element so ignoring the
element = driver.find_element(By.XPATH, '//*[@id="46"]/td[16]/div/div/div/a[1]')
element.click()
driver.find_element(By.XPATH,'//*[@id="checkbox-gt-road-facings-0"]').click()
time.sleep(5)
target_element = driver.find_element(By.XPATH, '//*[@id="create_sales_plan_button_span"]')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="create_sales_plan_button_span"]')))
button.click()

driver.quit()
