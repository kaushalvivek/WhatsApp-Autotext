import sys
from selenium import webdriver

# To Add : Argument parse
# To Add : Browser Support for Chrome

# One-time Variables
###########################
browser = "Chrome"
fire_path = "/home/kaushal/.mozilla/firefox/zzhbpihh.default"
chrome_path="/Users/vivekkaushal/Library/Application\ Support/Google/Chrome/"
###########################

if browser == "Firefox":
    browser_profile_path = fire_path
    fire_profile = webdriver.FirefoxProfile(browser_profile_path)
    driver = webdriver.Firefox(fire_profile)

elif browser == "Chrome":
    browser_profile_path = chrome_path
    chrome_profile = webdriver.ChromeOptions()
    chrome_profile.add_argument("user-data-dir="+browser_profile_path)
    driver = webdriver.Chrome(options=chrome_profile)


driver.get('https://web.whatsapp.com') 

name = input("Enter name of contact : ")
message = input("Enter message to send : ")

user = driver.find_elements_by_xpath('//span[@title = "{}"]'.format(name))
choice = 1
if len(user) > 1:
    for i in range(len(user)):
        print(i+1+". "+user[i]+'\n')
    choice = input("Which one? Type the serial number.")
user[choice-1].click()

box = driver.find_element_by_class_name('_2S1VP')
box.send_keys(message)
send_button = driver.find_element_by_class_name('_35EW6')
send_button.click()

