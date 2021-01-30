from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import csv

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

driver = webdriver.Chrome(chrome_options=option, executable_path='C:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.facebook.com/')
driver.maximize_window()


usererror ="The email address or phone number that you've entered doesn't match any account. Sign up for an account."
pwderror = "The password that you've entered is incorrect. Forgotten password?"
title = "Facebook"
with open('C://Users//Zia//Desktop//facebookusers.csv','w',encoding="utf-8", newline='') as f:
    w = csv.writer(f)
    w.writerow(["Username","Password","Text"])
    users = int(input('enter number of users please'))
    for i in range(users):
        username = input('enter the username please')
        password = input('enter the password please')
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys(username)
        driver.find_element_by_id("pass").clear()
        driver.find_element_by_id("pass").send_keys(password)
        driver.find_element_by_name("login").click()


        if(usererror == driver.find_element_by_xpath("//div[@class='_9ay7']").text):

            print('please enter a correct username')
            w.writerow([username,password,usererror])
            driver.back()
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("pass").clear()


        elif (pwderror == driver.find_element_by_xpath("//div[@class='_9ay7']").text):

            print('please enter a correct password')
            w.writerow([username, password, pwderror])
            driver.back()
            driver.find_element_by_id("email").clear()
            driver.find_element_by_id("pass").clear()

        elif(title ==driver.title):
            w.writerow([username, password, title])
            print('user successfully logged in')
            break
