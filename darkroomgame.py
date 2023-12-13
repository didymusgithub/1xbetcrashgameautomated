from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

disable_audio_btn = 'no'
# set up the browseer so that we can be able to use selenium
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://adarkroom.doublespeakgames.com/")

# carries out the wait operation if thge element is not yet present in the browser of a particular element
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), 'disable audio')]"))
)
clicked_btn = driver.find_element(By.ID,disable_audio_btn)
clicked_btn.click()

time.sleep(10)
driver.quit()