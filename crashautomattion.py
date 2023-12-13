from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username_input_id ='auth_id_email'
user_input_password ='auth-form-password'
login_btn_classname='curloginDropTop'
login_btn_classname ='auth-button'
# set up the browseer so that we can be able to use selenium
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


username_name ="testing@gmail.com"
login_password ="testin@!new"

# the 1xbet url
driver.get("https://india-1xbet.in/allgamesentrance/crash")
time.sleep(15)
login_btn = driver.find_element(By.CLASS_NAME,login_btn_classname)
login_btn.click()

WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, login_btn_classname))
)

# send the login details to the page
username_input = driver.find_element(By.ID, username_input_id)
username_input.send_keys(username_name)
time.sleep(5)

user_password = driver.find_element(By.ID, user_input_password)
user_password.send_keys(login_password)
time.sleep(5)

# login button




time.sleep(10)
