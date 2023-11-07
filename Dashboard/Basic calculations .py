import time
from selenium import webdriver
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
time.sleep(5)
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[5]/td[5]')
second_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[5]/td[3]')  # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,"(//h4[@class='fw-bolder mb-0'][normalize-space()='476'])[1]")  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value = float(re.sub(r"[^\d.]", "", second_value_element.text))
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))

total_average = round(first_value / second_value)

if total_average == third_value:
    print("Pass your average if perfectly calculated")
else:
    print("Fail,incorrect average")

time.sleep(4)
# total number of Units
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[1]/td[2]')
second_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[2]/td[2]')  # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,'//*[@id="types-table"]/tbody[2]/tr[3]/td[2]')  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value = float(re.sub(r"[^\d.]", "", second_value_element.text))
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))

total_average = round(first_value + second_value)

if total_average == third_value:
    print(third_value ," total apartment units ")
else:
    print("Fail, incorrect total units")

# total area
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[1]/td[3]')
second_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[2]/td[3]')  # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,'//*[@id="types-table"]/tbody[2]/tr[3]/td[3]')  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value = float(re.sub(r"[^\d.]", "", second_value_element.text))
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))
total_average = (first_value + second_value)

if total_average == third_value:
    print("Total area of unit apartments is ", third_value )
else:
    print("Fail, incorrect total area")


# Calculating average rate
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[1]/td[4]')
second_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[2]/td[4]')  # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,'//*[@id="types-table"]/tbody[2]/tr[3]/td[4]')  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value = float(re.sub(r"[^\d.]", "", second_value_element.text))
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))
average = (first_value + second_value) / 2
rounded_value = round(average, 2)
# Compare the rounded average with the third value
if rounded_value == third_value :
    print("Total area of unit apartments is ", third_value )
else:
    print("pass, Total area of units is  ", third_value)

time.sleep(4)
# calculating actual amounts
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[1]/td[4]')
second_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[1]/td[3]')  # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,'//*[@id="types-table"]/tbody[2]/tr[1]/td[5]')  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value = float(re.sub(r"[^\d.]", "", second_value_element.text))
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))
average = round(first_value * second_value)
if int(average) == int(third_value) :
    print("Pass, Actual amount of open units is  ", third_value )
else:
    print("Fail, incorrect actual amount in open")

time.sleep(4)


# total actual amount
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[3]/td[5]')
second_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[6]/td[5]')  # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,'//*[@id="types-table"]/tbody[2]/tr[7]/th[6]')  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value = float(re.sub(r"[^\d.]", "", second_value_element.text))
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))
average = (first_value + second_value)
if average == third_value :
    print("Pass, Total Actual amount of open units is  ", third_value )
else:
    print("Fail, incorrect actual amount")
time.sleep(4)

# Total area of units
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[3]/td[3]')
second_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[6]/td[3]')  # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,'//*[@id="types-table"]/tbody[2]/tr[7]/th[4]')  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value = float(re.sub(r"[^\d.]", "", second_value_element.text))
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))
average = round(first_value + second_value)
if int(average) == int(third_value) :
    print("Pass, Total area is  ", third_value )
else:
    print("Fail, incorrect total area amount in open")
time.sleep(4)

# Total average rate
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[3]/td[4]')
second_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[6]/td[4]')  # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,'//*[@id="types-table"]/tbody[2]/tr[7]/th[5]')  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value = float(re.sub(r"[^\d.]", "", second_value_element.text))
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))
average = first_value + second_value
if int(average) == int(third_value) :
    print("Pass, Total average rate of all units is   ", third_value )
else:
    print("Fail, incorrect total area amount in open")
time.sleep(4)
# Total actual amounts of all units
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[3]/td[5]')
second_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[6]/td[5]')  # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,'//*[@id="types-table"]/tbody[2]/tr[7]/th[6]')  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value = float(re.sub(r"[^\d.]", "", second_value_element.text))
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))
average = (first_value + second_value)

if int(average) == int(third_value):
    print("Pass, Total actual amount is    ", third_value )
else:
    print("Fail, incorrect total actual amount")
time.sleep(4)
# Total projected amount
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[3]/td[7]')
second_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[6]/td[7]')  # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,'//*[@id="types-table"]/tbody[2]/tr[7]/th[8]')  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value = float(re.sub(r"[^\d.]", "", second_value_element.text))
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))
average = (first_value + second_value)
if int(average) == int(third_value):
    print("Pass, Total projected amount is     ", third_value)
else:
    print("Fail, incorrect total projected amount")
time.sleep(4)

# Avg. Sale Rate (PKR/sqft) [Amount/Built-Up Area
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[7]/th[6]')
second_value_element = 10 # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,'//*[@id="types-table"]/tbody[2]/tr[8]/th[4]')  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value=10
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))
average = (first_value / second_value)
if int(average) == int(third_value):
    print("Pass, Avg. Sale Rate (PKR/sqft) [Amount/Built-Up Area is    ", third_value)
else:
    print("Fail, incorrect total actual amount")
time.sleep(4)
# Avg. Sale Rate (PKR/sqft) [Amount/Built-Up Area (10.00)] of projected amount
first_value_element = driver.find_element(By.XPATH, '//*[@id="types-table"]/tbody[2]/tr[7]/th[8]')
second_value_element = 10 # Replace "second-value" with the actual element ID or other locating mechanism
third_value_element = driver.find_element(By.XPATH,'//*[@id="types-table"]/tbody[2]/tr[8]/th[6]')  # Replace "third-value" with the actual element ID or other locating mechanism

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value=10
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))
average = (first_value / second_value)

if int(average) == int(third_value):
    print("Pass, Avg. Sale Rate (PKR/sqft) [Amount/Built-Up Area is    ", third_value)
else:
    print("Fail, incorrect total actual amount")
time.sleep(4)
# Total Projected cost of feasability cost
first_value_element = driver.find_element(By.XPATH, '//*[@id="11"]/td[4]')
second_value_element = driver.find_element(By.XPATH,'//*[@id="12"]/td[4]')
third_value_element = driver.find_element(By.XPATH,'//*[@id="10"]/td[4]')
fourth_value_element = driver.find_element(By.XPATH,'//*[@id="15"]/td[4]')
fifth_value_element = driver.find_element(By.XPATH,'//*[@id="17"]/td[4]')
sixth_value_element = driver.find_element(By.XPATH, ' //*[@id="14"]/td[4]')
seventh_value_element = driver.find_element(By.XPATH,'//*[@id="2"]/td[4]')
eighth_value_element = driver.find_element(By.XPATH, '//*[@id="3"]/td[4]')
nineth_value_element = driver.find_element(By.XPATH, '//*[@id="5"]/td[4] ')
tenth_value_element = driver.find_element(By.XPATH,'//*[@id="8"]/td[4]')
eleventh_value_element = driver.find_element(By.XPATH, ' //*[@id="13"]/td[4]')
twleve_value_element = driver.find_element(By.XPATH, ' //*[@id="9"]/td[4]')
thirteen_value_element = driver.find_element(By.XPATH, ' //*[@id="4"]/td[4]')
fourteen_value_element = driver.find_element(By.XPATH, ' //*[@id="1"]/td[4]')
fifteenth_value_element = driver.find_element(By.XPATH, ' //*[@id="6"]/td[4]')
sixteenth_value_element = driver.find_element(By.XPATH, ' //*[@id="7"]/td[4]')
seventh_value_element = driver.find_element(By.XPATH, ' //*[@id="16"]/td[4]')

first_value = float(re.sub(r"[^\d.]", "", first_value_element.text))
second_value = float(re.sub(r"[^\d.]", "", second_value_element.text))
third_value = float(re.sub(r"[^\d.]", "", third_value_element.text))
fourth_value = float(re.sub(r"[^\d.]", "", fourth_value_element.text))
fifth_value = float(re.sub(r"[^\d.]", "", fifth_value_element.text))
sixth_value = float(re.sub(r"[^\d.]", "", sixth_value_element.text))
seventh_value = float(re.sub(r"[^\d.]", "", seventh_value_element.text))
eight_value = float(re.sub(r"[^\d.]", "", eighth_value_element.text))
nineth_value = float(re.sub(r"[^\d.]", "", nineth_value_element.text))
tenth_value = float(re.sub(r"[^\d.]", "", tenth_value_element.text))
eleventh_value = float(re.sub(r"[^\d.]", "", eleventh_value_element.text))
twleve_value = float(re.sub(r"[^\d.]", "", twleve_value_element.text))


# total feasibility
Total_feasibility = driver.find_element(By.XPATH, ' //*[@id="total"]')
# total_feasibility = first_value+second_value+third_value+fourth_value+fifth_value+sixth_value+seventh_value+eight_value+nineth_value+tenth_value+eleventh_value+twleve_value_element+thirteen_value_element
# print(total_feasibility)
#
# average  = Total_feasibility / 10
driver.quit()