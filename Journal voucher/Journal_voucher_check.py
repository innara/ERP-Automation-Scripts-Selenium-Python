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
time.sleep(20)
button = driver.find_element(By.XPATH,'//*[@id="dropdownMenuButton100"]')
# Find the text you want to search for
searchText = 'Created'

# Check if the text exists within the page
if searchText in driver.page_source:
    # If the text is found, click the button
    driver.execute_script("arguments[0].click();", button)
time.sleep(6)
driver.find_element(By.XPATH,'//*[@id="checkVoucher"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="check_reason"]').send_keys("Voucher checked by uatomation")
driver.find_element(By.XPATH,'/html/body/div[9]/div/div[6]/button[1]').click()
time.sleep(3)

driver.quit()