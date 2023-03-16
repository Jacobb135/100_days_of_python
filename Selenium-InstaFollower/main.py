from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_experimental_option("detach", True)

URL = "https://www.instagram.com"
SIMILAR_ACCOUNT = "lionel sanders"
USERNAME = "USERNAME"
PASSWORD = "PASSWORD!"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get(URL)

    def login(self):
        username = self.driver.find_element(By.CSS_SELECTOR, value='div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.CSS_SELECTOR, value='div._ab32:nth-child(2) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
        password.send_keys(PASSWORD)
        login = self.driver.find_element(By.CSS_SELECTOR, value='div._abak:nth-child(3)')
        login.click()

    def find_followers(self):
        search = self.driver.find_element(By.CSS_SELECTOR, value='div.x1iyjqo2 > div:nth-child(2) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)')
        search.click()
        search_bar = self.driver.find_element(By.CSS_SELECTOR, value='._aauy')
        search_bar.send_keys(SIMILAR_ACCOUNT)
        search_bar.send_keys(Keys.ENTER)
        sleep(2)
        lionel = self.driver.find_element(By.CSS_SELECTOR, value='div.x6ikm8r > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > div:nth-child(1)')
        lionel.click()
        sleep(3)
        follower_list = self.driver.find_element(By.CSS_SELECTOR, value='li.xl565be:nth-child(2) > a:nth-child(1) > div:nth-child(1)')
        follower_list.click()

    def follow(self):
        sleep(2)

        follow_button = self.driver.find_elements(By.CSS_SELECTOR, "._acan")
        follower_number = len(follow_button)

        for num in range(1, follower_number):
            follower_button = self.driver.find_element(By.XPATH, value=f"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{num}]/div[3]/button/div/div")
            # follower_button = self.driver.find_element(By.XPATH, value=f"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[4]/div[3]/button/div/div")
            follower_button.click()
            sleep(1)


bot = InstaFollower()
sleep(5)
bot.login()
sleep(5)
bot.find_followers()
bot.follow()

