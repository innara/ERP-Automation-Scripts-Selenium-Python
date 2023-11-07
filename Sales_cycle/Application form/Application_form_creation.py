import time
from selenium import webdriver
from selenium.webdriver import ActionChains
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
email.send_keys("salah@j7global.com")
password = driver.find_element(By.NAME, "password")
password.send_keys("Salah@07")
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
time.sleep(5)
target_element = driver.find_element(By.XPATH, '//*[@id="layout-menu"]/ul/li[18]/a')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[18]/a')))
button.click()
try:
    deal = driver.find_element(By.XPATH, '//*[@id="layout-menu"]/ul/li[18]/ul/li[2]/a')
    driver.execute_script("arguments[0].scrollIntoView();", deal)
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layout-menu"]/ul/li[18]/ul/li[2]/a')))
    button.click()
    time.sleep(2)
except Exception as e:
    print("An error occurred:", str(e))
time.sleep(4)


driver.find_element(By.XPATH, '//*[@id="applicationForm-table_wrapper"]/div[1]/div[2]/div/div[2]').click()
add_new = driver.find_element(By.XPATH,'//*[@id="applicationForm-table_wrapper"]/div[1]/div[2]/div/div[2]/div[2]/div/a[1]')
add_new.click()
time.sleep(2)
# selecting payment plan
dropdown_element = driver.find_element(By.XPATH, '//*[@id="sales_plan_id"]')
dropdown = Select(dropdown_element)
dropdown.select_by_index(1)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
time.sleep(3)
driver.execute_script("document.body.style.zoom='70%'")
element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//span[@id='create_sales_plan_button_span'])[1]")))
element.click()

driver.quit()