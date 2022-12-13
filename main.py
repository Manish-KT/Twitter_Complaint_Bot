import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os

driver = webdriver.Chrome(service=Service(executable_path="D:\chromedriver\chromedriver.exe"))
twitter_url = "https://twitter.com/compose/tweet"
speed_test_url = "https://www.speedtest.net/"

password = os.environ["password"]
username = os.environ["username"]
msg = ""


class Tweet:
    def __int__(self):
        self.message = msg

    def login(self):
        driver.get(twitter_url)
        driver.maximize_window()
        # Verification/Login
        time.sleep(3)
        driver.find_element(By.NAME, "text").send_keys(username)
        time.sleep(1)
        driver.find_element(By.NAME, "text").send_keys(Keys.ENTER)
        # time for bot verification
        time.sleep(20)
        driver.find_element(By.NAME, "password").send_keys(password)
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
        time.sleep(3)

    def try_tweet(self, msg):
        try:
            driver.find_element(By.CSS_SELECTOR, '[aria-label = "Tweet text"]').click()
            driver.find_element(By.CSS_SELECTOR, '[aria-label = "Tweet text"]').send_keys(msg)
            time.sleep(10)
        except NoSuchElementException:
            print("Element not found")


class Speed_finder:
    def __init__(self):
        self.up = 0
        self.down = 0

    def find_speed(self):
        driver.minimize_window()
        driver.get(speed_test_url)
        driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(60)
        self.up = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

        self.down = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                  '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text


speed = Speed_finder()
speed.find_speed()

tweet = Tweet()
tweet.login()
tweet.try_tweet(f"Hey Internet service provider, My internet speed is slow\nspeed = {speed.up}/{speed.down}mbps")
