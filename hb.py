from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Firefox()
browser.get('https://feekart.srmuniv.ac.in/srmopp/')

url1 = browser.current_url
url2 = url1

if url1 == url2:
    try:
        username = browser.find_element_by_id("accountname")
        username.clear()
        username.send_keys('RA1511003010077') #username

        username = browser.find_element_by_name("password")
        username.clear()
        username.send_keys('password') #password

        browser.execute_script("loginform()")
        url2 = browser.current_url
        print("done")

    except:
        print("error")

        browser.close()
