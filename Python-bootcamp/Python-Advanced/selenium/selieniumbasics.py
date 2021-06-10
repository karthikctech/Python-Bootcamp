from selenium import webdriver

chrome_driver_path = "//home//linux/Python-bootcamp//Python-Advanced//selenium//chromedriver_linux64//chromedriver"

driver = webdriver.Chrome(executable_path = chrome_driver_path)

driver.get("https://www.flipkart.com/comfold-corner-desk-engineered-wood-study-table/p/itmfg2qnqxhs3yaa?pid=OSTFGYYJHVR2NWDJ&lid=LSTOSTFGYYJHVR2NWDJAIWCOF&marketplace=FLIPKART&store=wwe%2Fki7%2Fl1t&spotlightTagId=BestvalueId_wwe%2Fki7%2Fl1t&srno=b_1_1&otracker=hp_omu_Home%2BMakeover_4_10.dealCard.OMU_SUPUX4CZ7PE2_7&otracker1=hp_omu_WHITELISTED_neon%2Fmerchandising_Home%2BMakeover_NA_dealCard_cc_4_NA_view-all_7&fm=neon%2Fmerchandising&iid=196e6edc-89d8-4adb-8b89-90020dc1d6a0.OSTFGYYJHVR2NWDJ.SEARCH&ppt=browse&ppn=browse&ssid=g9dq4w6i4w0000001623205983366")

# sk = driver.find_element_by_id("container")
# print(sk.text)

# heading = driver.find_element_by_class_name("B_NuCI")

# print(heading.text)

# anchor_tag = driver.find_element_by_css_selector("_1rH5Jn a")

# print(anchor_tag)

driver.get("https://www.python.org")

# Sk = driver.find_element_by_name("q")

# print(Sk.tag_name)

# print(Sk.get_attribute("placeholder"))

event_times = find_element_by_css_selector(".event_widget time")
# below code used to print particular anchor_tag
event_names = find_element_by_css_selector("event_widget a")

# so print above line code in dictonary

events= {}

for i in range(len(event_times)):
    events[i] = {
        "time":event_times[i].text,
        "name":event_names[i],text
    }

print(events)

driver.close()

driver.quit()
