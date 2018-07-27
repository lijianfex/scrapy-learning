# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:09:04 2018

@author: LiJian
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# firefox plugin
# https://askubuntu.com/questions/870530/how-to-install-geckodriver-in-ubuntu

chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless

# add the option when creating driver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").click()
time.sleep(2)
driver.find_element_by_id("kw").clear()
time.sleep(2)
driver.find_element_by_id("kw").send_keys(u"赵丽颖")
time.sleep(2)
driver.find_element_by_id("su").click()
time.sleep(2)
driver.find_element_by_link_text(u"图片").click()
time.sleep(2)
driver.find_element_by_link_text(u"赵丽颖图片").click()
time.sleep(2)
driver.find_element_by_link_text(u"赵丽颖最美的七张照片").click()
time.sleep(2)

print(driver.page_source[:200])
driver.get_screenshot_as_file("./img/sreenshot2.png")
driver.close()
print('finish')