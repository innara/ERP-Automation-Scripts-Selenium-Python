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
driver.get("url")
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

target_element = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[23]')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[23]')))
button.click()
try:
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[23]/ul/li[1]')))
    # Perform interaction with the element
    element.click()

except Exception as e:
    print("An error occurred:", str(e))

# Creating new investor deal
driver.find_element(By.XPATH, '//*[@id="stakeholder-table_wrapper"]/div[1]/div[2]/div/button[2]').click()
driver.find_element(By.XPATH, '//*[@id="stakeholder-table_wrapper"]/div[1]/div[2]/div/div[2]/div/button').click()
time.sleep(3)

dropdown_element = driver.find_element(By.XPATH, '//*[@id="stackholders"]')
dropdown = Select(dropdown_element)
dropdown.select_by_index(2)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="doc_number"]').send_keys('ID03546')
time.sleep(2)
driver.execute_script("document.body.style.zoom='75%'")
floor_id = Select(driver.find_element(By.XPATH, '//*[@id="all_units"]'))
floor_id.select_by_index(3)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="received_amount"]').send_keys('12000')
time.sleep(2)
driver.find_element(By.XPATH, ' //*[@id="remarks"]').send_keys(' Invested on this unit ')
# try:

attach_element = driver.find_element(By.NAME, 'attachment[]')
attach_element.send_keys(
        "C://Users/innara/Downloads/whatsapp-image-2023-06-02-at-34029-pm-1-1686551005-1687168646.jpeg")
time.sleep(15)
driver.execute_script("document.body.style.zoom='70%'")
button = driver.find_element(By.ID, 'saveButton')
driver.execute_script("arguments[0].click();", button)
time.sleep(10)
driver.quit()
