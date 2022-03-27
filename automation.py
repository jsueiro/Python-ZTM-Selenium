from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

# create instance of browser
chrome_browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))

# opens chrome
chrome_browser

# open browser with url
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

# search for a str in an html element
# assert with a false result gives assertion err
assert 'Selenium Easy Demo' in chrome_browser.title

# can capture elements based on class
show_message_button = chrome_browser.find_element(
    by=By.CLASS_NAME, value='btn-default')

assert 'Show Message' in chrome_browser.page_source

# input user message
user_message = chrome_browser.find_element(by=By.ID, value='user-message')

# clear input and enter text
user_message.clear()
user_message.send_keys('Hello World')

time.sleep(5)

# click button
show_message_button.click()

# grab output
output_message = chrome_browser.find_element(by=By.ID, value='display')

assert 'Hello World' in output_message.text

time.sleep(5)
chrome_browser.quit()
