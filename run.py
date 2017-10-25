# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import sys
reload(sys)
#solve Chinese messy code
sys.setdefaultencoding('utf-8')


driver=webdriver.Chrome()

url = "file:///C:/Users/ZhangCan/Desktop/index-load-more-videp.html"
driver.get(url)
#wait = WebDriverWait(driver, 1000)
#wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'car-no')))

#create a csv file to write data
csvfile = file('csvtest.csv', 'wb')
writer = csv.writer(csvfile)
writer.writerow(['license_str', 'img_url'])

div_elements = driver.find_elements(By.XPATH, "//div[@class='event-container']")
for i in range(0, len(div_elements)):
    license_str = div_elements[i].find_element_by_class_name('car-no').text
    #print license_str
    img_src_elements = div_elements[i].find_elements_by_class_name("event-img-file")
    for j in range(0, len(img_src_elements)):
        img_url = img_src_elements[j].get_attribute("path")
        writer.writerow([license_str, img_url])

#close
csvfile.close()
driver.close()
#license_str1 = driver.find_element_by_class_name('car-no')
#print license_str1.text
#driver.find_element_by_id("kw").send_keys("python")

#driver.find_element_by_id("su").click()

#browser.implicitly_wait(40) # seconds

#browser.find_element_by_id("user").click()
#wait = WebDriverWait(driver, 1000)
#wait.until(EC.element_to_be_clickable((By.ID, 'user')))
#driver.find_element_by_id("user").click()
