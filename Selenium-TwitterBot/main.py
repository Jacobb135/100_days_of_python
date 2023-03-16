from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

URL = "https://www.speedtest.net"
TWITTER = "https://www.twitter.com"
PROMISED_UP = 1000
PROMISED_DOWN = 25
TWITTER_EMAIL = "email@gmail.com"
TWITTER_PASSWORD = "password"

options = Options()
options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.promised_up = 0
        self.promised_down = 0

    def get_internet_speed(self):
        self.driver.get(URL)
        sleep(5)
        go = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go.click()
        sleep(45)
        self.promised_down = float(self.driver.find_element(By.CLASS_NAME, value="download-speed").text)
        self.promised_up = float(self.driver.find_element(By.CLASS_NAME, value="upload-speed").text)
        print(self.promised_up)
        print(self.promised_down)


    def tweet_at_provider(self):
        self.driver.get(TWITTER)
        sleep(5)
        main_page = self.driver.current_window_handle
        login_page = ""
        login = self.driver.find_element(By.LINK_TEXT, value="Log in")
        login.click()
        sleep(3)

        for handle in self.driver.window_handles:
            if handle != main_page:
                login_page = handle

        self.driver.switch_to.window(login_page)
        email = self.driver.find_element(By.CSS_SELECTOR, value="input")
        email.send_keys(TWITTER_EMAIL)
        next_button = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()
        sleep(2)
        username = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys("RickSan27602164")
        username.send_keys(Keys.ENTER)
        sleep(1)
        password = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_button.click()
        sleep(3)
        text_field = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        text_field.click()
        sleep(1)
        tweet_field = self.driver.find_element(By.CSS_SELECTOR, value="[aria-label= 'Tweet text']")
        tweet_field.send_keys(f"Hey Internet provider why is my download speed {self.promised_down} and my upload speed {self.promised_up}")
        tweet_button = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
if bot.promised_down < 1000 or bot.promised_up < 10:
    bot.tweet_at_provider()
else:
    bot.driver.quit()
