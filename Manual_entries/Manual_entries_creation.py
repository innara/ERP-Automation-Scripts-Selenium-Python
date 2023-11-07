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
# Find the search box element and enter a search query
email = driver.find_element(By.NAME, "email")
email.send_keys("innara.karim2018@gmail.com")
password = driver.find_element(By.NAME, "password")
password.send_keys("password")
# Close the browser
time.sleep(2)
driver.execute_script("document.body.style.zoom='70%'")
login = driver.find_element(By.ID, "sign-in")
login.submit()
if "dashboard" in driver.current_url:
    print("Login successful Your credentials are correct!")
else:
    print("Login failed. Please check your credentials.")

time.sleep(5)
# Accessing Manual entires from sidebarle
target_element = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[24]/a')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[24]/a')))
button.click()
time.sleep(3)
try:
    deal = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[24]/ul/li[3]')
    driver.execute_script("arguments[0].scrollIntoView();", deal)
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[24]/ul/li[3]')))
    button.click()
    time.sleep(2)

except Exception as e:
    print("An error occurred:", str(e))
driver.find_element(By.XPATH,'//*[@id="main-menu-navigation"]/li[24]/ul/li[3]/ul/li[2]').click()
time.sleep(5)
# Adding new manual entries
driver.find_element(By.XPATH,'//*[@id="manual-entries-table_wrapper"]/div[1]/div[2]/div/button[2]').click()
driver.find_element(By.XPATH,'//*[@id="manual-entries-table_wrapper"]/div[1]/div[2]/div/div[2]/div/button').click()
time.sleep(3)
doc = driver.find_element(By.XPATH, ' //*[@id="doc_number"]')
doc.send_keys('Me-000123')
# Adding account and amount in different accounts
dropdown_element = driver.find_element(By.NAME, 'manual-entry-entries[0][account_number]')
dropdown = Select(dropdown_element)
dropdown.select_by_index(2)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(2)
debit = driver.find_element(By.NAME, 'manual-entry-entries[0][debit]')
debit.send_keys('1000')
time.sleep(3)
driver.find_element(By.NAME,"manual-entry-entries[0][remarks]").send_keys('Debited amount from this account ')

time.sleep(3)
driver.find_element(By.XPATH, ' //*[@id="first-contact-person"]').click()
driver.execute_script("document.body.style.zoom='70%'")
time.sleep(3)
dropdown_element = driver.find_element(By.NAME, 'manual-entry-entries[1][account_number]')
dropdown = Select(dropdown_element)
dropdown.select_by_index(2)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(2)
debit = driver.find_element(By.NAME, 'manual-entry-entries[1][credit]')
debit.send_keys('10000')
time.sleep(3)
driver.find_element(By.NAME,"manual-entry-entries[1][remarks]").send_keys('credited amount from this account ')
time.sleep(3)
button = driver.find_element(By.XPATH, '//*[@id="saveButton"]')
driver.execute_script("arguments[0].click();", button)
time.sleep(10)

driver.quit()