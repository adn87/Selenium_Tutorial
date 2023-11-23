from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# Commons = driver.find_element(By.LINK_TEXT, value="Commons")
# Commons.click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

fname = driver.find_element(By.NAME, value="fName")
fname.send_keys("George")
lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("Washington")
email = driver.find_element(By.NAME, value="email")
email.send_keys("dummy@gmail.com")
submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()
driver.quit()
