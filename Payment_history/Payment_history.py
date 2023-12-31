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
driver.get("-")
driver.maximize_window()
driver.execute_script("document.body.style.zoom='75%'")

# Find the search box element and enter a search query
email = driver.find_element(By.NAME, "email")
email.send_keys("-")
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
# Accessing investor deal from sidebar

target_element = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[24]/a')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[24]/a')))
button.click()
try:
    deal = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[24]/ul/li[4]/a')
    driver.execute_script("arguments[0].scrollIntoView();", deal)
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[24]/ul/li[4]/a')))
    button.click()
    time.sleep(2)
except Exception as e:
    print("An error occurred:", str(e))
time.sleep(4)

# new payment history
driver.find_element(By.XPATH,'//*[@id="payment-voucher-table_wrapper"]/div[1]/div[2]/div/button[2]').click()
driver.find_element(By.XPATH,'//*[@id="payment-voucher-table_wrapper"]/div[1]/div[2]/div/div[2]/div/button').click()
time.sleep(3)
dropdown_element = driver.find_element(By.XPATH, '//*[@id="stakeholderAP"]')
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text('Eid Muhammad ( 1220139832035)')
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(4)

type = driver.find_element(By.XPATH, '//*[@id="stakholder_type"]')
dropdown = Select(type)
dropdown.select_by_visible_text('Customer')
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(2)
driver.execute_script("document.body.style.zoom='70%'")
driver.find_element(By.XPATH,'//*[@id="doc_number"]').send_keys('Inves-0054')
driver.find_element(By.XPATH,'//*[@id="amount_to_be_paid"]').send_keys(' 2000')
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="tax_status"]').send_keys(' ACTIVE')
driver.find_element(By.XPATH,'//*[@id="description"]').send_keys(' Ok')
time.sleep(2)
# Saving payment history

button = driver.find_element(By.XPATH, '//*[@id="saveButton"]')
driver.execute_script("arguments[0].click();", button)
time.sleep(5)


driver.quit()


