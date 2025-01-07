from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
import shutil
import time
import threading

# Set up Chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU rendering (optional, improves compatibility)
chrome_options.add_argument("--window-size=1920x1080")  # Set a virtual window size (optional)
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

characters_to_remove = '/\\?%*:|"<>'

url = 'https://crypto.news/news/'

service = Service('C:\\Users\\User\\Desktop\\chromedriver-win64\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the website
driver.get(url)
driver.set_page_load_timeout(240)

wait = WebDriverWait(driver, 120)

# UNIQUE ARTICLE LIST
unique_articles = []

# Clicking cookie ACCEPT
cookie_button = driver.find_element(By.ID, "cookie-consent-button")
cookie_button.click()

i = 0
popup = True
while True:
    top_articles = driver.find_elements(By.CLASS_NAME, "post-loop__link")
    print(i, "-----", len(top_articles), "---------------", len(unique_articles))
    if i == len(top_articles):
        break

    # Traverse the directory structure
    for root, _, files in os.walk("C:\\Users\\User\\Desktop\\Python\\Crypto"):
        for file in files:
            # Process only .txt files
            if not file.endswith(".txt"):
                continue
            file_name, file_extension = os.path.splitext(file)  # Separate name and extension
            if file_name in unique_articles:
                break
        continue
    
    unique_articles.append(top_articles[i].text)
    # Converting time ######################################################
    top_articles_time = driver.find_elements(By.CLASS_NAME, "post-loop__date")
    datetime_str = top_articles_time[i].get_attribute("datetime")
    post_time = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    #print(post_time)
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
    driver.get(url)
    i+=1

more_news_button = driver.find_element(By.XPATH, "//*[@id='menu-item-14051377']/a")
more_news_button.click()

bitcoin_news_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-item-14135096']/a")))
bitcoin_news_button.click()

i = 0
popup = False

while True:
    top_articles = driver.find_elements(By.CLASS_NAME, "post-loop__link")
    print(i, "-----", len(top_articles), "---------------", len(unique_articles))
    if i == len(top_articles):
        break

    if top_articles[i].text in unique_articles:
        i+=1
        continue
    # Traverse the directory structure
    for root, _, files in os.walk("C:\\Users\\User\\Desktop\\Python\\Crypto"):
        for file in files:
            # Process only .txt files
            if not file.endswith(".txt"):
                continue
            file_name, file_extension = os.path.splitext(file)  # Separate name and extension
            #print(top_articles[i].text, "SSSSSSSSS", file_name)
            if file_name in unique_articles:
                break
        continue
    
    unique_articles.append(top_articles[i].text)
    # Converting time ######################################################
    top_articles_time = driver.find_elements(By.CLASS_NAME, "post-loop__date")
    datetime_str = top_articles_time[i].get_attribute("datetime")
    post_time = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    #print(post_time)
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


more_news_button = driver.find_element(By.XPATH, "//*[@id='menu-item-14051377']/a")
more_news_button.click()

blockchain_news_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-item-14135097']/a")))
blockchain_news_button.click()

i = 0
popup = False
while True:

    top_articles = driver.find_elements(By.CLASS_NAME, "post-loop__link")
    print(i, "-----", len(top_articles), "---------------", len(unique_articles))
    if i == len(top_articles):
        break

    if top_articles[i].text in unique_articles:
        i+=1
        continue
    # Traverse the directory structure
    for root, _, files in os.walk("C:\\Users\\User\\Desktop\\Python\\Crypto"):
        for file in files:
            # Process only .txt files
            if not file.endswith(".txt"):
                continue
            file_name, file_extension = os.path.splitext(file)  # Separate name and extension
            #print(top_articles[i].text, "SSSSSSSSS", file_name)
            if file_name in unique_articles:
                break
        continue
    
    unique_articles.append(top_articles[i].text)
    # Converting time ######################################################
    top_articles_time = driver.find_elements(By.CLASS_NAME, "post-loop__date")
    datetime_str = top_articles_time[i].get_attribute("datetime")
    post_time = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    #print(post_time)
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
        with open(f"C:\\Users\\User\\Desktop\\Python\\Crypto\\Blockchain_news\\{title}.txt", "a", encoding="utf-8") as file:
            file.write(f"{t.text} \n")
    driver.back()
    i+=1


more_news_button = driver.find_element(By.XPATH, "//*[@id='menu-item-14051377']/a")
more_news_button.click()

ethereum_news_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-item-14135099']/a")))
ethereum_news_button.click()

i = 0
popup = False

while True:

    top_articles = driver.find_elements(By.CLASS_NAME, "post-loop__link")
    print(i, "-----", len(top_articles), "---------------", len(unique_articles))
    if i >= len(top_articles):
        break

    if top_articles[i].text in unique_articles:
        i+=1
        continue
    # Traverse the directory structure
    for root, _, files in os.walk("C:\\Users\\User\\Desktop\\Python\\Crypto"):
        for file in files:
            # Process only .txt files
            if not file.endswith(".txt"):
                continue
            file_name, file_extension = os.path.splitext(file)  # Separate name and extension
            #print(top_articles[i].text, "SSSSSSSSS", file_name)
            if file_name in unique_articles:
                break
        continue
    
    unique_articles.append(top_articles[i].text)
    # Converting time ######################################################
    top_articles_time = driver.find_elements(By.CLASS_NAME, "post-loop__date")
    datetime_str = top_articles_time[i].get_attribute("datetime")
    post_time = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    #print(post_time)
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
        with open(f"C:\\Users\\User\\Desktop\\Python\\Crypto\\Ethereum_news\\{title}.txt", "a", encoding="utf-8") as file:
            file.write(f"{t.text} \n")
    driver.back()
    i+=1


more_news_button = driver.find_element(By.XPATH, "//*[@id='menu-item-14051377']/a")
more_news_button.click()

defi_news_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-item-14135101']/a")))
defi_news_button.click()

i = 0
popup = False
while True:

    top_articles = driver.find_elements(By.CLASS_NAME, "post-loop__link")
    print(i, "-----", len(top_articles), "---------------", len(unique_articles))
    if i == len(top_articles):
        break

    if top_articles[i].text in unique_articles:
        i+=1
        continue
    # Traverse the directory structure
    for root, _, files in os.walk("C:\\Users\\User\\Desktop\\Python\\Crypto"):
        for file in files:
            # Process only .txt files
            if not file.endswith(".txt"):
                continue
            file_name, file_extension = os.path.splitext(file)  # Separate name and extension
            #print(top_articles[i].text, "SSSSSSSSS", file_name)
            if file_name in unique_articles:
                break
        continue
    
    unique_articles.append(top_articles[i].text)
    # Converting time ######################################################
    top_articles_time = driver.find_elements(By.CLASS_NAME, "post-loop__date")
    datetime_str = top_articles_time[i].get_attribute("datetime")
    post_time = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    #print(post_time)
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
        with open(f"C:\\Users\\User\\Desktop\\Python\\Crypto\\DeFi_news\\{title}.txt", "a", encoding="utf-8") as file:
            file.write(f"{t.text} \n")
    driver.back()
    i+=1


more_news_button = driver.find_element(By.XPATH, "//*[@id='menu-item-14051377']/a")
more_news_button.click()

altcoin_news_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-item-14135098']/a")))
altcoin_news_button.click()

i = 0
popup = False
while True:

    top_articles = driver.find_elements(By.CLASS_NAME, "post-loop__link")
    print(i, "-----", len(top_articles), "---------------", len(unique_articles))
    if i == len(top_articles):
        break

    if top_articles[i].text in unique_articles:
        i+=1
        continue
    # Traverse the directory structure
    for root, _, files in os.walk("C:\\Users\\User\\Desktop\\Python\\Crypto"):
        for file in files:
            # Process only .txt files
            if not file.endswith(".txt"):
                continue
            file_name, file_extension = os.path.splitext(file)  # Separate name and extension
            #print(top_articles[i].text, "SSSSSSSSS", file_name)
            if file_name in unique_articles:
                break
        continue
    
    unique_articles.append(top_articles[i].text)
    # Converting time ######################################################
    top_articles_time = driver.find_elements(By.CLASS_NAME, "post-loop__date")
    datetime_str = top_articles_time[i].get_attribute("datetime")
    post_time = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    #print(post_time)
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
        with open(f"C:\\Users\\User\\Desktop\\Python\\Crypto\\Altcoin_news\\{title}.txt", "a", encoding="utf-8") as file:
            file.write(f"{t.text} \n")
    driver.back()
    i+=1


more_news_button = driver.find_element(By.XPATH, "//*[@id='menu-item-14051377']/a")
more_news_button.click()

regulation_news_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-item-14135100']/a")))
regulation_news_button.click()

i = 0
popup = False
while True:

    top_articles = driver.find_elements(By.CLASS_NAME, "post-loop__link")
    print(i, "-----", len(top_articles), "---------------", len(unique_articles))
    if i == len(top_articles):
        break

    if top_articles[i].text in unique_articles:
        i+=1
        continue
    # Traverse the directory structure
    for root, _, files in os.walk("C:\\Users\\User\\Desktop\\Python\\Crypto"):
        for file in files:
            # Process only .txt files
            if not file.endswith(".txt"):
                continue
            file_name, file_extension = os.path.splitext(file)  # Separate name and extension
            #print(top_articles[i].text, "SSSSSSSSS", file_name)
            if file_name in unique_articles:
                break
        continue
    
    unique_articles.append(top_articles[i].text)
    # Converting time ######################################################
    top_articles_time = driver.find_elements(By.CLASS_NAME, "post-loop__date")
    datetime_str = top_articles_time[i].get_attribute("datetime")
    post_time = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    #print(post_time)
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
        with open(f"C:\\Users\\User\\Desktop\\Python\\Crypto\\Regulation_news\\{title}.txt", "a", encoding="utf-8") as file:
            file.write(f"{t.text} \n")
    driver.back()
    i+=1


more_news_button = driver.find_element(By.XPATH, "//*[@id='menu-item-14051377']/a")
more_news_button.click()

solana_news_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-item-14303087']/a")))
solana_news_button.click()

i = 0
popup = False
while True:

    top_articles = driver.find_elements(By.CLASS_NAME, "post-loop__link")
    print(i, "-----", len(top_articles), "---------------", len(unique_articles))
    if i >= len(top_articles):
        break

    if top_articles[i].text in unique_articles:
        i+=1
        continue
    # Traverse the directory structure
    for root, _, files in os.walk("C:\\Users\\User\\Desktop\\Python\\Crypto"):
        for file in files:
            # Process only .txt files
            if not file.endswith(".txt"):
                continue
            file_name, file_extension = os.path.splitext(file)  # Separate name and extension
            #print(top_articles[i].text, "SSSSSSSSS", file_name)
            if file_name in unique_articles:
                break
        continue
    
    unique_articles.append(top_articles[i].text)
    # Converting time ######################################################
    top_articles_time = driver.find_elements(By.CLASS_NAME, "post-loop__date")
    datetime_str = top_articles_time[i].get_attribute("datetime")
    post_time = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    #print(post_time)
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
        with open(f"C:\\Users\\User\\Desktop\\Python\\Crypto\\Solana_news\\{title}.txt", "a", encoding="utf-8") as file:
            file.write(f"{t.text} \n")
    driver.back()
    i+=1


more_news_button = driver.find_element(By.XPATH, "//*[@id='menu-item-14051377']/a")
more_news_button.click()

shiba_news_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-item-14303088']/a")))
shiba_news_button.click()

i = 0
popup = False
while True:

    top_articles = driver.find_elements(By.CLASS_NAME, "post-loop__link")
    print(i, "-----", len(top_articles), "---------------", len(unique_articles))
    if i == len(top_articles):
        break

    if top_articles[i].text in unique_articles:
        i+=1
        continue
    # Traverse the directory structure
    for root, _, files in os.walk("C:\\Users\\User\\Desktop\\Python\\Crypto"):
        for file in files:
            # Process only .txt files
            if not file.endswith(".txt"):
                continue
            file_name, file_extension = os.path.splitext(file)  # Separate name and extension
            #print(top_articles[i].text, "SSSSSSSSS", file_name)
            if file_name in unique_articles:
                break
        continue
    
    unique_articles.append(top_articles[i].text)
    # Converting time ######################################################
    top_articles_time = driver.find_elements(By.CLASS_NAME, "post-loop__date")
    datetime_str = top_articles_time[i].get_attribute("datetime")
    post_time = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S%z")
    #print(post_time)
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
        with open(f"C:\\Users\\User\\Desktop\\Python\\Crypto\\Shiba_news\\{title}.txt", "a", encoding="utf-8") as file:
            file.write(f"{t.text} \n")
    driver.back()
    i+=1
time.sleep(100)
