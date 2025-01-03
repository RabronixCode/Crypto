from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

url = 'https://crypto.news/news/'

service = Service('C:\\Users\\User\\Desktop\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get(url)

wait = WebDriverWait(driver, 20)