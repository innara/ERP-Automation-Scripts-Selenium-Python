import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
# Create a WebDriver instance for Google Chrome
driver = webdriver.Chrome()

# Navigate to Google.com
driver.get("-")
driver.maximize_window()
driver.execute_script("document.body.style.zoom='75%'")

# Find the search box element and enter a search query
email = driver.find_element(By.NAME, "email")
email .send_keys("innara.karim2018@gmail.com")
password = driver.find_element(By.NAME, "password")
password.send_keys("password")
# Close the browser
time.sleep(2)
login = driver.find_element(By.ID, "sign-in")
login.submit()
if "dashboard" in driver.current_url:
    print("Login successful Your credentials are correct!")
else:
    print("Login failed. Please check your credentials.")
driver.execute_script("document.body.style.zoom='100%'")
time.sleep(2)
target_element = driver.find_element(By.XPATH, "(//span[normalize-space()='Units'])[1]")
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//span[normalize-space()='Units'])[1]")))
button.click()

# Creating Unit
create_unit = driver.find_element(By.XPATH, "(//button[@class='dt-button buttons-collection ms-1 btn btn-primary btn-icon rounded-pill dropdown-toggle hide-arrow waves-effect waves-light custom_more'])[1]")
create_unit.click()
new_unit = driver.find_element(By.XPATH, "(//span[normalize-space()='Add New'])[1]")
new_unit.click()
time.sleep(2)
# Adding unit details in unit form
floor_id = Select(driver.find_element(By.XPATH, '//*[@id="fllor_id"]'))
floor_id.select_by_index(3)

unit_type = Select(driver.find_element(By.XPATH, '//*[@id="type_id"]'))
unit_type.select_by_index(1)

unit_name = driver.find_element(By.XPATH, '//*[@id="name"]')
unit_name.send_keys("Unit Automated")

net_area = driver.find_element(By.XPATH, '//*[@id="net_area"]')
net_area.send_keys(1200)
gross_area = driver.find_element(By.XPATH, '//*[@id="gross_area"]')
gross_area.send_keys(3000)
time.sleep(2)
Btn_click = driver.find_element(By.XPATH, '//*[@id="units_form"]/div/div[2]/div/div/div/div/div[1]/button')
Btn_click.click()
time.sleep(6)
driver.quit()
