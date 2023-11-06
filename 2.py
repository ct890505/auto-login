from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# Github credentials
username = "your_username"
password = "your_password"

chrome_options = Options()
# Không hiển thị trình duyệt khi chạy
chrome_options.add_argument("--headless")

# Đường dẫn đến tệp thực thi của ChromeDriver
driver_service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

# Head to github login page
driver.get('https://github.com/login')

# Example: Log in to Github
username_field = driver.find_element(By.ID, 'login_field')
password_field = driver.find_element(By.ID, 'password')
login_button = driver.find_element(By.NAME, 'commit')

username_field.send_keys(username)
password_field.send_keys(password)
login_button.click()

# Wait for a few seconds (you may want to use WebDriverWait for better synchronization)
driver.implicitly_wait(5)

# Do some actions on the logged-in page
# ...

# Don't forget to close the driver when done
driver.quit()
