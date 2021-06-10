# in this section intract the wikipedia website
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "//home//linux/Python-bootcamp//Python-Advanced//selenium//chromedriver_linux64//chromedriver"

driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# total_article_numers = driver.find_element_by_css_selector("#articlecount a")

# print(total_article_numers.text)

# print(total_article_numers.click())

# to see any anchor tag full details to print that anchor name

# anchor_detail = driver.find_element_by_link_text("All portal")
# anchor_detail.click()

# automate typee in search bar
Search = driver.find_element_by_name("search")
Search.send_keys("python")
# keys are used to enter to search the python
Search.send_keys(Keys.ENTER)
