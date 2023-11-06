from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Trang web đích
login_url = 'enter link the website you wanna login'

# Github credentials
username = "enter your username wanna try login"
password = "enter your password or pass list you wanna try login"

# Create a new WebDriver instance
driver = webdriver.Chrome()

# Head to the login page
driver.get(login_url)

# Use WebDriverWait to wait for the element to be present
# wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
# username_field = wait.until(EC.presence_of_element_located((By.ID, 'username')))
time.sleep(5)

# Find username and password fields and submit button
username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')
# submit_button = driver.find_element(By.NAME, 'submit')
submit_button = driver.find_element(By.XPATH,"//input[@type='submit'][@tyle='background-color: black'][@value='Đăng nhập']")# change the HTML on the website you wanna login

# Enter credentials and submit
# for user in username:
username_field.send_keys(username)
password_field.send_keys(password)
submit_button.click()
time.sleep(5)

# Check if login was successful (you can modify this based on your needs)
if 'Thư' in driver.page_source:
   list_acc=[]
   list_acc.append(username + password)
   
   print('đăng nhập thành công tài khoản:    '+ str(username) + '  mật khẩu:   ' + str(password) )
   print(str(list_acc))
else:
    print('Login failed')

# Close the WebDriver when done
driver.quit()
