from selenium import webdriver

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com")

# Closes a single tab
# driver.close()

# Quits the entire browser
driver.quit()