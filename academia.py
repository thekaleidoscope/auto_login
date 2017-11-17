import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.get('https://academia.srmuniv.ac.in/')

url1 = browser.current_url
url2 = url1

while url1 == url2:
    try:
        username = browser.find_element_by_id("Email")
        username.clear()
        username.send_keys('yadhukrishnas_su@srmuniv.edu.in') #username

        username = browser.find_element_by_name("password")
        username.clear()
        username.send_keys('password') #password

        browser.execute_script("loginform()")
        url2 = browser.current_url
        print("done")

    except:
        e = sys.exc_info()
        print(e)


    browser.close()
