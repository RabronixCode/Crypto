from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import os
import shutil
import time
import threading

characters_to_remove = '/\\?%*:|"<>'

url = 'https://crypto.news/news/'

service = Service('C:\\Users\\User\\Desktop\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Navigate to the website
driver.get(url)

wait = WebDriverWait(driver, 20)

# Clicking cookie ACCEPT
cookie_button = driver.find_element(By.ID, "cookie-consent-button")
cookie_button.click()

i = 0
popup = True
while True:
    top_articles = driver.find_elements(By.CLASS_NAME, "post-loop__link")

    if i == len(top_articles):
        break

    # Converting time ######################################################
    top_articles_time = driver.find_elements(By.CLASS_NAME, "post-loop__date")
    datetime_str = top_articles_time[i].get_attribute("datetime")
    post_time = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    print(post_time)
    ##################################################################
    
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", top_articles[i])
    time.sleep(2)
    if popup:
        popups = driver.find_element(By.ID, "onesignal-slidedown-cancel-button")
        popups.click()
        popup = False

    title_text = top_articles[i].text
    title = title_text.translate(str.maketrans('', '', characters_to_remove))
    top_articles[i].click()
    text_elements = driver.find_elements(By.XPATH, "/html/body//article//div[@class='post-detail__content blocks']/p")
    for t in text_elements:
        with open(f"C:\\Users\\User\\Desktop\\Python\\Crypto\\Crypto_news_top_articles\\{title}.txt", "a", encoding="utf-8") as file:
            file.write(f"{t.text} \n")
    driver.back()
    i+=1

more_news_button = driver.find_element(By.XPATH, "//*[@id='menu-item-14051377']/a")
more_news_button.click()

bitcoin_news_button = driver.find_element(By.XPATH, "//*[@id='menu-item-14135096']/a")
bitcoin_news_button.click()

i = 0
popup = False
while True:
    top_articles = driver.find_elements(By.CLASS_NAME, "post-loop__link")
    if i == len(top_articles):
        break
    # Converting time ######################################################
    top_articles_time = driver.find_elements(By.CLASS_NAME, "post-loop__date")
    datetime_str = top_articles_time[i].get_attribute("datetime")
    post_time = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    print(post_time)
    ##################################################################
    
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", top_articles[i])
    time.sleep(2)
    if popup:
        popups = driver.find_element(By.ID, "onesignal-slidedown-cancel-button")
        popups.click()
        popup = False

    title_text = top_articles[i].text
    title = title_text.translate(str.maketrans('', '', characters_to_remove))
    top_articles[i].click()
    text_elements = driver.find_elements(By.XPATH, "/html/body//article//div[@class='post-detail__content blocks']/p")
    for t in text_elements:
        with open(f"C:\\Users\\User\\Desktop\\Python\\Crypto\\Bitcoin_news\\{title}.txt", "a", encoding="utf-8") as file:
            file.write(f"{t.text} \n")
    driver.back()
    i+=1

time.sleep(100)
