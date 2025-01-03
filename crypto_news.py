from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://crypto.news/news/'

service = Service('C:\\Users\\User\\Desktop\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get(url)

wait = WebDriverWait(driver, 20)
# Waiting for all global element hookups
driver.implicitly_wait(5)

# Clicking notification CANCEL
cancel_button = driver.find_element(By.ID, "onesignal-slidedown-cancel-button")
cancel_button.click()

# Clicking cookie ACCEPT
cookie_button = driver.find_element(By.ID, "cookie-consent-button")
cookie_button.click()

time.sleep(1000)
