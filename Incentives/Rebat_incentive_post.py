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
time.sleep(5)
print ('Rebate incentive created successfully ')

time.sleep(1)