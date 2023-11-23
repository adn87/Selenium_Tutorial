from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome Browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
driver.get("https://www.nintendo.com/us/store/products/the-legend-of-zelda-breath-of-the-wild-switch/")
path = driver.find_element(By.XPATH, value='//*[@id="main"]/section[1]/div/div[3]/div[4]/div/div/span/text()')
print(path.text)
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text
# print(f"the price is: {price_dollar}.{price_cent}")




# Closes a single tab
# driver.close()

# Quits the entire browser
driver.quit()