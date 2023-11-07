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
    deal = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[24]/ul/li[2]')
    driver.execute_script("arguments[0].scrollIntoView();", deal)
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[24]/ul/li[2]')))
    button.click()
    time.sleep(2)
except Exception as e:
    print("An error occurred:", str(e))
time.sleep(4)
# create new voucher
driver.find_element(By.XPATH,'//*[@id="journal-vouchers-table_wrapper"]/div[1]/div[2]/div/button[2]').click()
driver.find_element(By.XPATH,'//*[@id="journal-vouchers-table_wrapper"]/div[1]/div[2]/div/div[2]/div/button').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="remarks"]').send_keys('The Major Source For Independent Artists MANAGEMENT▪️MEDIA▪️MARKETING @tharealbabyc @xsoski @djsavageway @str.quezdawg · 360 posts · 11.8K followers · 990 ...')
driver.find_element(By.XPATH, ' //*[@id="doc_number"]').send_keys(' JV-0001')

dropdown_element = driver.find_element(By.NAME, "outer-journal-voucher-entries[0][journal-voucher-entries][0][account_number]")
dropdown = Select(dropdown_element)
dropdown.select_by_index(2)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(3)

# debit amount
debit = driver.find_element(By.XPATH,'//*[@id="debit"]')
debit.send_keys('1200')
# credit
add = driver.find_element(By.XPATH, ' //*[@id="first-contact-person"]')
add.click()
add.click()
dropdown_element = driver.find_element(By.NAME,"outer-journal-voucher-entries[0][journal-voucher-entries][1][account_number]")
dropdown = Select(dropdown_element)
dropdown.select_by_index(1)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(3)
driver.execute_script("document.body.style.zoom='75%'")
credit = driver.find_element(By.NAME, 'outer-journal-voucher-entries[0][journal-voucher-entries][1][credit]')
credit.send_keys('12000')
driver.find_element(By.XPATH,'//*[@id="remarks"]').send_keys(' Journal voucher created')
time.sleep(3)
driver.execute_script("document.body.style.zoom='70%'")
button = driver.find_element(By.ID, 'saveButton')
driver.execute_script("arguments[0].click();", button)
time.sleep(10)

driver.quit()