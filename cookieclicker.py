from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# set up the browseer so that we can be able to use selenium
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(" https://orteil.dashnet.org/cookieclicker/")


cookie_id ="bigCookie"
cookies ='cookies'
product_price_prefix ="productPrice"
product_prefix ="product"


WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="langSelect-EN"]'))
)

language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

WebDriverWait(driver,10).until(
    EC.presence_of_all_elements_located((By.ID, cookie_id))
)
cookie = driver.find_element(By.ID, cookie_id)
cookie.click()

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies).text.split( " ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    print(cookies_count)

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue
        product_price = int( product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID,product_prefix + str(i))
            product.click()
            break



time.sleep(10)
