import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chromeOptions)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

gameOn = True

bigCookie = driver.find_element(By.ID, "cookie")

upgradeList = driver.find_elements(By.CSS_SELECTOR, "#store div")
print(upgradeList[0].get_attribute("id"))

item_ids = [item.get_attribute("id") for item in upgradeList]



timeout = time.time() + 5

while gameOn is True:
    bigCookie.click()
    if time.time() > timeout:
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            # Example' 15 - buyCursor' without '' plus the last element is empty hence the below if condition
            if element_text != "":
                # split [buycursor] [ 15] ---- taking [1] means [ 15] now stripping means [15] then removing comma
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        print(item_prices)
        new_dict = {}
        for n in range(8):
            new_dict[item_prices[n]] = item_ids[n]
        print(new_dict)

        money = driver.find_element(By.ID, "money").text
        if ',' in money:
            money = money.replace(",", "")
        money = int(money)

        affordable_upgrades = {}
        for cost, id in new_dict.items():
            if money > cost:
                affordable_upgrades[cost] = id
        print(affordable_upgrades)
        # {15: 'buyCursor', 100: 'buyGrandma'} prints this when grandma is unlocked
        # get the max value
        highest_price_affordable_upgrade = max(affordable_upgrades, default=0)
        print(highest_price_affordable_upgrade)
        # 15 incase only cursor is unlocked, 100 incase grandma is unlocked
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
        print(to_purchase_id)
        driver.find_element(by=By.ID, value=to_purchase_id).click()
        timeout = time.time() + 5

  # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > (time.time() + 300):
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

