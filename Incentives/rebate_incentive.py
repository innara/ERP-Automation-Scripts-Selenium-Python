import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
width = 2023.5
height = 2643.35
driver.set_window_size(width, height)
driver.get('https://dev.j7konnect.com/login')
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('salah@j7global.com')
driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys('Salah123456')
driver.find_element(By.XPATH, ' //*[@id="sign-in"]').click()
time.sleep(4)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
target_element = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[21]')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[21]')))
button.click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="main-menu-navigation"]/li[21]/ul/li[1]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="stakeholder-table_wrapper"]/div[1]/div[2]/div/button[2]').click()
driver.find_element(By.XPATH, ' //*[@id="stakeholder-table_wrapper"]/div[1]/div[2]/div/div[2]/div/button').click()
# Creating rebate incentive and dealer incentive
dropdown_element = driver.find_element(By.XPATH, "//*[@id='unit_id']")


dropdown = Select(dropdown_element)

dropdown.select_by_index(2)

selected_option = dropdown.first_selected_option
print(selected_option.text)

all_options = dropdown.options
for option in all_options:
    print(option.text)

driver.find_element(By.XPATH,'//*[@id="rebate_percentage"]').send_keys(10)
time.sleep(2)
driver.find_element(By.XPATH, ' //*[@id="doc_number"]').send_keys('ID-RB-03')
Drp = driver.find_element(By.XPATH, ' //*[@id="stackholders"]')
select = Select(Drp)
select.select_by_index(1)
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="saveButton"]').click()

time.sleep(20)
driver.quit()