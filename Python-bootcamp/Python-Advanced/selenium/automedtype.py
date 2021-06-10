from selenium import webdriver

chrome_driver_path = "//home//linux/Python-bootcamp//Python-Advanced//selenium//chromedriver_linux64//chromedriver"

driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

Search = driver.find_element_by_name("fName")
Search.send_keys("karthik")

Search = driver.find_element_by_name("lName")
Search.send_keys("python")

Search = driver.find_element_by_name("email")
Search.send_keys("python@gmail.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()