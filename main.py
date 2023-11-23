from selenium import webdriver
from selenium.webdriver.common.by import By


# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

time_events = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last > div > ul > li > time")
time = [event.text for event in time_events]
# print(time)

title_events = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget.event-widget.last  div  ul  li  a")
title = [event.text for event in title_events]
# print(title)

events = {}
for n in range(len(time_events)):
    events[n] = {
        "time": time_events[n].text,
        "title": title_events[n].text
    }
print(events)





# Closes a single tab
# driver.close()

# Quits the entire browser
driver.quit()