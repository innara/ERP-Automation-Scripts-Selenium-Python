import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
width = 2023.5
height = 2643.35
driver.set_window_size(width, height)
driver.get('Url')
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('Something email')
driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys('password')
driver.find_element(By.XPATH, ' //*[@id="sign-in"]').click()
time.sleep(4)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
target_element = driver.find_element(By.XPATH, '//*[@id="main-menu-navigation"]/li[7]')
driver.execute_script("arguments[0].scrollIntoView();", target_element)
wait = WebDriverWait(driver, 10)
button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-menu-navigation"]/li[7]')))
button.click()
time.sleep(2)
driver.find_element(By.XPATH ,'//*[@id="main-menu-navigation"]/li[7]/ul/li[2]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="types-table_wrapper"]/div[1]/div[2]/div/button[2]').click()
Add = driver.find_element(By.XPATH,'//*[@id="types-table_wrapper"]/div[1]/div[2]/div/div[2]/div/button')
Add.click()
# Create new type by typing name of type
driver.find_element(By.XPATH,'//*[@id="type_name"]').send_keys('Food Court')
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[4]/form/div/div[2]/div/div/div/div/div[1]/button').click()
time.sleep(2)
driver.quit()