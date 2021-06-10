from selenium import webdriver

chrome_driver_path = "//home//linux/Python-bootcamp//Python-Advanced//selenium//chromedriver_linux64//chromedriver"

driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("https://www.google.com")

driver.close()

driver.quit()

