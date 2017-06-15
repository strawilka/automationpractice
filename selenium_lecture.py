from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "http://facebook.com"
# initialize browser
browser = webdriver.Chrome()

# open browser with url
browser.get(URL)
assert "Facebook" in browser.title

# login
email_input = browser.find_element_by_css_selector("input#email")
password_input_xpath = browser.find_element_by_xpath('//input[@name="pass"]')
login_button = browser.find_element(By.CSS_SELECTOR, 'input[type=submit]')

email_input.clear()
email_input.send_keys('login')
password_input_xpath.send_keys('pass')
login_button.click()

# verify we are failed to login
assert 'Login into Facebook' in browser.title
# browser.quit()