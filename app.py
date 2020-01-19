from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

ChromeDrive = executable_path='/home//hadi//PycharmProjects//Test//chromedriver'
Url = 'https://divar.ir/'
Tehran = '//*[@id="app"]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/a'
SearchBox = '/html/body/div[1]/div[2]/header/div[1]/div[2]/div/div[1]/div[2]/div/input'
SearchKey = 'شتر مرغ'

driver = webdriver.Chrome(ChromeDrive)
driver.get(Url)
# button in top page Tehran
button = driver.find_element_by_xpath(Tehran)
button.click()
time.sleep(5)
# text page for search
search = driver.find_element_by_xpath(SearchBox)
#insert a text keys for search
search.send_keys(SearchKey, Keys.ENTER)
time.sleep(5)
# driver.quit()
Product = driver.find_element_by_css_selector("#app > div.col-md-12.p-none.browse > main > div.blurring.dimmable > div.browse-post-list > a:nth-child(1)")
Product.click()
time.sleep(5)
ProductPhone = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[3]/div[2]/div/button[1]')
ProductPhone.click()
time.sleep(5)
Rules = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[3]/button')
Rules.click()
time.sleep()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
#
# driver = webdriver.Firefox()
# driver.send_keys('selenium' + Keys.ENTER)
# # driver.get('https://www.google.com/')
# browser.quit()
#
