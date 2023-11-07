import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
width = 2023.5
height = 2643.35
driver.set_window_size(width, height)
driver.get('SOME URL')
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('-')
driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys('password')
driver.find_element(By.XPATH, ' //*[@id="sign-in"]').click()
time.sleep(4)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
target_element = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[17]/a')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[17]/a')))
button.click()
time.sleep(2)
driver.find_element(By.XPATH ,'//*[@id="main-menu-navigation"]/li[17]/ul/li[4]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[17]/ul/li[4]/ul/li[1] ').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="user-table_wrapper"]/div[1]/div[2]/div/button[2]').click()
driver.find_element(By.XPATH, "//span[normalize-space()='Add New']").click()
time.sleep(3)

# Inserting data for creating new User
driver.find_element(By.XPATH,'//*[@id="name"]').send_keys('Amina Salaam ')
driver.find_element(By.XPATH, '//*[@id="father_name"] ').send_keys('-')
driver.find_element(By.XPATH, ' //*[@id="email"]').send_keys('Amnah@gmail.com')
driver.find_element(By.XPATH, ' //*[@id="password"]').send_keys('password')
driver.find_element(By.XPATH, '//*[@id="password-confirm"]').send_keys('password')
driver.find_element(By.XPATH, '//*[@id="contact"]').send_keys('3434565678')
driver.find_element(By.XPATH, '//*[@id="optional_contact"]').send_keys('333333333')
time.sleep(2)
attach_element = driver.find_element(By.XPATH, '//*[@id="photo_attachment"]')
time.sleep(2)
# Attach the file to the eleme
time.sleep(10)



time.sleep(5)



driver.quit()