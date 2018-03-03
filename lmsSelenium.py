from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Firefox()

pwd = "dypatil@123"
driver.get("http://mydy.dypatil.edu/rait/login/index.php?uname=pri.shi.rt15@rait.ac.in&wantsurl=")

password_box = driver.find_element_by_id('password')
password_box.send_keys(pwd)

login_box = driver.find_element_by_id('loginbtn')
login_box.click()
time.sleep(4)
window_before = driver.window_handles[0]

SE = driver.find_elements_by_class_name('launchbutton')
for count,button in enumerate(SE,1):
    button.click()
#    driver.implicitly_wait(30)
#    window_after = driver.window_handles[count]
#    driver.switch_to.window(window_after)
#    ul = driver.find_element_by_xpath('//*[@id="gridiconcontainer"]/ul')
#
#    links = ul.find_elements_by_xpath('.//li/div/ul/li/p/a/@href')
#
#   for link in links:
#        print(links)
#
# window_after = driver.window_handles[1]
# driver.implicitly_wait(10)
# links = driver.find_element_by_xpath('//*[@id="module-276925"]/div/div/div[2]/div/a/@href').text
# driver.get(links)
#
# ul = driver.find_element_by_xpath('//*[@id="gridiconcontainer"]/ul')
#
# links = ul.find_elements_by_xpath('.//li/div/ul/li/p/a/@href')
#
# for link in links:
#     print(links)

# link = driver.find_element_by_xpath('//*[@id="inst9772"]')
# link.click()

