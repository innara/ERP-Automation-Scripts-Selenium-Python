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
email.send_keys("innara.karim2018@gmail.com")
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
target_element = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[6]')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[6]')))
button.click()
time.sleep(2)
# search for appoval
search = driver.find_element(By.XPATH,'//*[@id="document-approval-table_filter"]/label/input')
search.send_keys('JV-000128')
search.click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="dropdownMenuButton100"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="approveDoc"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="check_reason"]').send_keys(' Approving journal voucher')
driver.find_element(By.XPATH,'/html/body/div[9]/div/div[6]/button[1]').click()
time.sleep(2)
driver.quit()