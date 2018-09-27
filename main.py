import sys
from selenium import webdriver

# To Add : Argument parse

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')

name = input("Enter name of contact : ")
message = input("Enter message to send : ")

user = driver.find_elements_by_xpath('//span[@title = "{}"]'.format(name))
user[0].click()

box = driver.find_element_by_class_name('_2S1VP')
box.send_keys(message)
send_button = driver.find_element_by_class_name('_35EW6')
send_button.click() 