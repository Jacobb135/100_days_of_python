from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("detach", True)
chrome_driver_path = r"YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(options=options)
driver.get("https://www.appbrewery.co/p/newsletter")
driver.maximize_window()
search = driver.find_element(By.ID, value="member_email")
search.send_keys("email@gmail.com")
search.send_keys(Keys.ENTER)
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)
# page_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# page_count.click()
# view_source = driver.find_element(By.LINK_TEXT, value="View source")
# view_source.click()


# event_times = driver.find_elements(By.CLASS_NAME, value="event-widget time")
# event_places = driver.find_elements(By.CLASS_NAME, value="event-widget li a")
#
# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "place": event_places[n].text
#     }

# print(events)
# driver.quit()


