from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# driver.get("https://www.amazon.com")

#chrome wont go away after run
chrome_Object = webdriver.ChromeOptions()
chrome_Object.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_Object)
driver.get("https://www.python.org/")
time_list = []
event_list = []

new_time_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
for item in new_time_list:
    time_list.append(item.text)
# print(time_list)

new_event_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget a")
for item in new_event_list:
    event_list.append(item.text)
event_list.remove("More")
# print(event_list)

new_dict = {}
for n in range(5):
    new_dict[n] = {
        "time": time_list[n],
        "name": event_list[n],
    }
print(new_dict)
driver.quit()