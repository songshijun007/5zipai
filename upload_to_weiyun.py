from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
driver.get('https://www.weiyun.com/')

driver.switch_to.frame('qq_login_iframe')
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
driver.find_element_by_xpath('//*[@id="u"]').send_keys('3354059053')
driver.find_element_by_xpath('//*[@id="p"]').send_keys('hjx2577312047')
driver.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="_mod_act_panel1"]/div/div[3]/a/span').click()
driver.find_element_by_xpath('//*[@id="_mod_act_panel1"]/div/div[3]/div/ul/li[2]/span').click()
os.system('C:/Users/hejiaxiong/Desktop/upfile.exe')
