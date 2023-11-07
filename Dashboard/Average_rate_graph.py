import time
from selenium import webdriver
from selenium.webdriver.common.by import By
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
time.sleep(5)
chart_elements = driver.find_elements(By.XPATH, "(//div[@id='statistics-chart'])[1]")
data_values = []

for element in chart_elements:

    value = driver.find_element(By.XPATH, "(//*[name()='path'][@id='SvgjsPath1434'])[1]")
    data_values.append(value)
print(data_values)
time.sleep(2)
driver.quit()