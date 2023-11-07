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
driver.execute_script("document.body.style.zoom='70%'")
login = driver.find_element(By.ID, "sign-in")
login.submit()
if "dashboard" in driver.current_url:
    print("Login successful Your credentials are correct!")
else:
    print("Login failed. Please check your credentials.")

time.sleep(5)
# Accessing investor deal from sidebar
target_element = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[7]')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[7]')))
button.click()
try:
    deal = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[7]/ul/li[1]')
    driver.execute_script("arguments[0].scrollIntoView();", deal)
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[7]/ul/li[1]')))
    button.click()
    time.sleep(2)
except Exception as e:
    print("An error occurred:", str(e))
driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[4]/section/div/div/ul/li[7]').click()
time.sleep(2)

payment_plan = driver.find_element(By.XPATH,'//*[@id="approvalTab"]/li[1]')
driver.execute_script("arguments[0].scrollIntoView();", payment_plan)
payment_plan.click()
time.sleep(4)

element = driver.find_element(By.XPATH, "(//button[@id='first-contact-person'])[1]")
driver.execute_script("arguments[0].click();", element)
time.sleep(2)
dropdown_element = driver.find_element(By.XPATH, '//*[@id="role_id"]')
dropdown = Select(dropdown_element)
dropdown.select_by_index(1)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(2)
dropdown_e = driver.find_element(By.XPATH, '//*[@id="user"]')
dropdown = Select(dropdown_e)
dropdown.select_by_index(3)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(2)
# checking to required signature
checkbox = driver.find_element(By.XPATH,'//*[@id="is_required"]')

# Check the checkbox by clicking on it
checkbox.click()
time.sleep(5)
driver.execute_script("document.body.style.zoom='70%'")
button = driver.find_element(By.XPATH, '//*[@id="create-sign-form"]/div/div[2]/div/button[1]')
driver.execute_script("arguments[0].click();", button)
driver.quit()

