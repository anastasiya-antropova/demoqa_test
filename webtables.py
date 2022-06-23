import time
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

browser=webdriver.Chrome()
browser.get("https://demoqa.com/webtables")

j=2
i=0
for i in range(j):
        butAdd=browser.find_element(By.ID, "addNewRecordButton")
        butAdd.click()

        FirstName=browser.find_element(By.ID, "firstName")
        FirstName.send_keys("Name"+str(i))
        LastName=browser.find_element(By.ID, "lastName")
        LastName.send_keys("Surname"+str(i))
        email=browser.find_element(By.ID, "userEmail")
        email.send_keys("test@tt.tt")
        age=browser.find_element(By.ID, "age")
        age.send_keys(str(random.randint(22,60)))
        salary=browser.find_element(By.ID, "salary")
        salary.send_keys(str(random.randint(5000,10000)))
        dep=browser.find_element(By.ID, "department")
        dep.send_keys("D"+str(i*2))

        butSubmit=browser.find_element(By.ID, "submit")
        butSubmit.click()
        i+=1

ex1=browser.find_element(By.NAME,'39')
#ex2=browser.find_element(CSS.SELECTOR,)

#time.sleep(25)
#browser.quit()


