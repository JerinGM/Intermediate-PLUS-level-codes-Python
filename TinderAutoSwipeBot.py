import selenium
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException, NoSuchWindowException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.tinder.com")
time.sleep(2)
login = driver.find_element(By.XPATH, '//*[@id="q-1355571838"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login.click()
time.sleep(5)
# moreOptions = driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/button')
# moreOptions.click()
# time.sleep(2)

loginFB = driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
loginFB.click()

# SWITCHING WINDOW
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
time.sleep(2)
email = driver.find_element(By.ID, "email")
email.send_keys("pythontest20000@gmail.com")
password = driver.find_element(By.ID, "pass")
password.send_keys("Daenerys@123")
password.send_keys(Keys.ENTER)
time.sleep(2)
# SWITCHING WINDOW BACK
driver.switch_to.window(base_window)
time.sleep(5)

allow_location_button = driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_location_button.click()

allow_notification_button = driver.find_element(By.XPATH, '//*[@id="q1211014382"]/main/div/div/div/div[3]/button[1]/div[2]/div[2]')
allow_notification_button.click()

cookie_decline = driver.find_element(By.XPATH, '//*[@id="q-1355571838"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/div[2]')
cookie_decline.click()


for i in range(100):
    time.sleep(1)
    try:
        likebutton = driver.find_element(By.XPATH, '//*[@id="q-1355571838"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span')
        likebutton.click()
        time.sleep(2)
    # except ElementClickInterceptedException:
    #     try:
    #         match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
    #         match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
    except NoSuchElementException:
        time.sleep(2)

    # except NoSuchWindowException:
    #     likebutton = driver.find_element(By.XPATH, '//*[@id="q-1355571838"]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[4]/button/span/span')
    #     likebutton.click()


driver.quit()






