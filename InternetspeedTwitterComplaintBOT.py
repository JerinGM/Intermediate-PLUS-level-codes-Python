import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISEDDOWNSPEED = 150
PROMISEDUPSPEED = 100
EMAIL = "EMAIL"
PASSWORD = "PASSWORD"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.chromeOptions = webdriver.ChromeOptions()
        self.chromeOptions.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(self.chromeOptions)
        self.down = 0.0
        self.up = 0.0

    def internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(1)
        continueButton = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        continueButton.click()
        go = self.driver.find_element(By.CLASS_NAME, "start-text")
        time.sleep(1)
        go.click()
        time.sleep(50)
        down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.down = down.text
        self.up = up.text
        print(self.down)
        print(self.up)
    def tweet(self):
        self.driver.get("https://www.twitter.com/")
        loginButton = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a')
        loginButton.click()
        time.sleep(2)
        enterEmailvalue = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        enterEmailvalue.send_keys(EMAIL)
        time.sleep(2)
        nextButton = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        nextButton.click()
        time.sleep(10)
        enterPasswordvalue = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        enterPasswordvalue.send_keys(PASSWORD)
        time.sleep(1)
        loginWithCredentials = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        loginWithCredentials.click()
        time.sleep(5)
        tweetmessage = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        tweetmessage.send_keys("DRAFT YOUR TWEET")
        tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div/span/span')
        tweet.click()


internetspeedtwitterbot = InternetSpeedTwitterBot()
internetspeedtwitterbot.internet_speed()
# CHECK IF SPEED IS LESS THEN CALL OUT THE TWEET()
internetspeedtwitterbot.tweet()



