from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()
driver.send_keys('selenium' + Keys.ENTER)
# driver.get('https://www.google.com/')

