import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
driver = webdriver.Chrome()
driver.get("http://mydy.dypatil.edu/rait/login/index.php?uname=pri.shi.rt15@rait.ac.in&wantsurl=")
pwd = "dypatil@123"
driver.get("http://mydy.dypatil.edu/rait/login/index.php?uname=pri.shi.rt15@rait.ac.in&wantsurl=")
password_box = driver.find_element_by_id('password')
password_box.send_keys(pwd)
login_box = driver.find_element_by_id('loginbtn')
login_box.click()
time.sleep(2)
window_before = driver.window_handles[0]
SE = driver.find_elements_by_class_name('launchbutton')
for button in SE:
    button.click()

for tab in range(1,7):
    window_before_all = driver.window_handles[0]
    window_after = driver.window_handles[tab]
    driver.switch_to.window(window_after)
    time.sleep(2)
    elem = driver.find_element_by_link_text('Presentation')
    elem.click()
    time.sleep(4)
    links = driver.find_elements_by_xpath('//*[@id="filterlist"]/div/ul/li/div/ul/li/p/a')

    for link in links:
        window_before_ppt = driver.window_handles[0]
        window_after_ppt = driver.window_handles[1]
        driver.execute_script("window.open(arguments[0]);", link.get_attribute('href'))
        driver.switch_to.window(window_after_ppt)
        time.sleep(2)
        elem = driver.find_element_by_tag_name('body')
        time.sleep(3)
        driver.execute_script("window.close()")

# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
# driver.get(link.get_attribute('href'))
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')
# time.sleep(4)

