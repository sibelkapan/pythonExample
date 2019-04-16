# import libraries
import urllib.request
from selenium import webdriver
import time

# specify the url
urlpage = 'https://www.tutorialspoint.com/python/python_basic_syntax.htm' 
print(urlpage)

# scrap the webpage using firefox webdriver
# run firefox webdriver from executable path of your choice
# For Firefox need geckodriver
driver = webdriver.Firefox()
# get web page
driver.get(urlpage)
# execute script to scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
# sleep for 30s
time.sleep(30)
# get all html
html = driver.page_source
print(html)
# close driver
driver.quit()
