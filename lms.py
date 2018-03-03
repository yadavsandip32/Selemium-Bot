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
time.sleep(4)
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
    time.sleep(8)
    links = driver.find_elements_by_xpath('//*[@id="filterlist"]/div/ul/li/div/ul/li/p/a')
    links[1].get_attribute('href')
    for link in links:
        # link.send_keys(Keys.COMMAND + 't')
        driver.get(link.get_attribute('href')).send_keys(Keys.COMMAND + 't')
        time.sleep(2)
    # import pdb; pdb.set_trace()
    # for link in links:
    #     print(link)





















    # ul = driver.find_element_by_xpath('//*[@id="gridiconcontainer"]/ul/li')
    #
    # element = driver.find_elements_by_xpath('//*[@id="gridiconcontainer"]/ul/li/a')
    # # wait.until(EC.element_to_be_clickable((By.ID, 'someid')))
    # for i in element:
    #     print(i.get_attribute('href'))
    # import  pdb;pdb.set_trace()
    break
