import json
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.execute_script("document.body.style.zoom='70%'")

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
time.sleep(10)

desired_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "(//button[@class='dt-button buttons-collection ms-1 btn btn-primary btn-icon rounded-pill dropdown-toggle hide-arrow waves-effect waves-light custom_more'])[1]")))  # Replace "desired-element-id" with the actual ID of the desired element
driver.execute_script("arguments[0].scrollIntoView();", desired_element)

# Perform the move to element operation
actions = webdriver.ActionChains(driver)
actions.move_to_element(desired_element).perform()


driver.quit()

