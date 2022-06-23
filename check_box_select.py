from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link=('https://demoqa.com/checkbox')
browser=webdriver.Chrome()
browser.get(link)
#!!!!!!!!!!!!!!! Message: Select only works on <select> elements, not on <div>!!!!!!!!!!!!!!!!!!!!!!!

select=Select(browser.find_element(By.CLASS_NAME, "check-box-tree-wrapper"))
select.select_by_visible_text("Private")

#time.sleep(15)
browser.quit

