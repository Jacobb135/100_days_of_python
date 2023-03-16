from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_experimental_option("detach", True)
chrome_driver_path = r"Your_Chrome_driver_path"
driver = webdriver.Chrome(options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
driver.implicitly_wait(7)
english = driver.find_element(By.ID, value="langSelect-EN")
english.click()
cookie = driver.find_element(By.ID, value="bigCookie")
cookie_counter = int(driver.find_element(By.ID, value="cookies").text[0])
cursor_upgrade = driver.find_element(By.CLASS_NAME, value="content")
cursor_price = int(driver.find_element(By.ID, value="productPrice0").text)

start_time = time.time()
increment = 5

while True:
    if time.time() > increment + start_time:
        try:
            upgrades = driver.find_elements(By.CSS_SELECTOR, value="#upgrades .enabled")
            for item in upgrades[::-1]:
                item.click()
        except:
            print("No upgrades available")

        try:
            products = driver.find_elements(By.CSS_SELECTOR, value=".product.enabled")
            for item in products[::-1]:
                item.click()
        except:
            print("Not enough cookies")

        start_time = time.time()
        increment += 5
    cookie.click()





