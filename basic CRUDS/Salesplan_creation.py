import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
width = 2023.5
height = 2643.35
driver.set_window_size(width, height)
driver.get('URL')
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('-')
driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys('password')
driver.find_element(By.XPATH, ' //*[@id="sign-in"]').click()
time.sleep(4)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
target_element = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[20]/a')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[20]/a')))
button.click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[20]/ul/li[1]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="sales-plan-table_wrapper"]/div[1]/div[2]/div/button[2]').click()
driver.find_element(By.XPATH, ' //*[@id="sales-plan-table_wrapper"]/div[1]/div[2]/div/div[2]/div/button[1]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="create-sales-plan-form"]/div/div[1]/div[1]/div/div/div/div/div/div').click()
dropdown_element = driver.find_element(By.XPATH, '//*[@id="unit_id"]')
dropdown = Select(dropdown_element)
dropdown.select_by_index(2)
selected_option = dropdown.first_selected_option
all_options = dropdown.options
for option in all_options:
    print(option.text)
driver.find_element(By.XPATH,'//*[@id="create-sales-plan-form"]/div/div[2]/div[2]/div[2]/div/div[1]').click()
time.sleep(5)

down = driver.find_element(By.ID,'//*[@id="percentage-discount"]')
driver.execute_script("arguments[0].scrollIntoView();", down)
# Enter text into the element
down.click()
down.send_keys("12")
time.sleep(12)
driver.quit()
