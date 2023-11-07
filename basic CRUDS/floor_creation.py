import time
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# Create a WebDriver instance for Google Chrome
driver = webdriver.Chrome()
driver.execute_script("document.body.style.zoom='70%'")
# Navigate to Google.com
driver.get("some URL")
driver.maximize_window()
driver.execute_script("document.body.style.zoom='75%'")

# Find the search box element and enter a search query
email = driver.find_element(By.NAME, "email")
email.send_keys("-")
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
target_element = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[18]')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[18]')))
button.click()
time.sleep(2)

# Create new floor
Create_floor = driver.find_element(By.XPATH,"(//button[@class='dt-button buttons-collection ms-1 btn btn-primary btn-icon rounded-pill dropdown-toggle hide-arrow waves-effect waves-light custom_more'])[1]")
Create_floor.click()
time.sleep(2)
new_floor = driver.find_element(By.CSS_SELECTOR, "button[class='dt-button dropdown-item mt-1'] span")
new_floor.click()
# Adding data in form
floor_name = driver.find_element(By.XPATH, "(//input[@id='name'])[1]")
floor_name.send_keys("Floor automated")
floor_area = driver.find_element(By.XPATH, "(//input[@id='floor_area'])[1]")
floor_area.send_keys("12400")
unit_rate = driver.find_element(By.XPATH, "(//input[@id='price'])[1]")
unit_rate.send_keys("3000")

time.sleep(2)


element = driver.find_element(By.XPATH, '//*[@id="floor_form"]/div/div[2]/div/div[2]/div/div/div[1]/button')
driver.execute_script("arguments[0].scrollIntoView();", element)

if element.is_displayed():
    try:
        element.click()
        print("Created floor sucessfully without any error")
        success_message = driver.find_element(By.XPATH, "/html/body/div[3]/div[3]/div[1]/div/div/div/div/div")
        if success_message.is_displayed():
            print("Save was successful.")
        else:
            print("Unable to detect success message.")

    except ElementClickInterceptedException:
        print("Save button click intercepted.")

    except Exception as e:
        print("An error occurred:", str(e))
else:
    print("Save button element not found.")
time.sleep(3)
driver.quit()
