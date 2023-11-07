import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
# Create a WebDriver instance for Google Chrome
driver = webdriver.Chrome()
driver.execute_script("document.body.style.zoom='70%'")

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
target_element = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[22]')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[22]')))
button.click()
try:
    deal = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[22]/ul/li[1]')
    driver.execute_script("arguments[0].scrollIntoView();", deal)
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[22]/ul/li[1]')))
    button.click()
    time.sleep(2)
except Exception as e:
    print("An error occurred:", str(e))
time.sleep(4)
driver.find_element(By.XPATH, "(//button[@id='dropdownMenuButton100'])[3]").click()
time.sleep(3)
driver.find_element(By.XPATH,"(//a[@class='dropdown-item'][normalize-space()='External Stakeholder Signatures'])[2]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//button[normalize-space()='Sign Here'])[1]").click()
time.sleep(2)
driver.find_element(By.XPATH, ' //*[@id="twoFactorAuthModal"]/div/div/div[2]/div/label[1]').click()
driver.find_element(By.XPATH, "(//a[@id='nextStepAuth'])[1]").click()
time.sleep(2)

time.sleep(5)
canvas = driver.find_element(By.XPATH, "(//canvas[@id='sketchpad'])[1]")
start_x = 1
start_y = 1

# Create an ActionChains object to perform the drawing action
action_chains = ActionChains(driver)
action_chains.move_to_element_with_offset(canvas, start_x, start_y)
action_chains.click_and_hold()

# Simulate drawing motion by moving to different coordinates
# Adjust the coordinates and add more move_to_element_with_offset actions to form the desired signature
action_chains.move_to_element_with_offset(canvas, start_x + 50, start_y + 50)
action_chains.move_to_element_with_offset(canvas, start_x + 100, start_y + 100)
# ...

# Release the mouse button to complete the drawing
action_chains.release()

# Perform the drawing action
action_chains.perform()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="twoFactorAuthAppsModal"]/div/div/div[2]/div[2]/div/button[2]').click()
time.sleep(2)
driver.quit()