from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()

pwd = "dypatil@123"
driver.get("http://mydy.dypatil.edu/rait/login/index.php?uname=pri.shi.rt15@rait.ac.in&wantsurl=")
window_before = driver.window_handles[0]

password_box = driver.find_element_by_id('password')
password_box.send_keys(pwd)

login_box = driver.find_element_by_id('loginbtn')
login_box.click()
time.sleep(4)
window_after = driver.window_handles[0]
driver.switch_to.window(window_after)
SE = driver.find_elements_by_class_name('launchbutton')
for button in SE:
    button.click()
