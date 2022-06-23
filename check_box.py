from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link="https://demoqa.com/checkbox"

browser = webdriver.Chrome()
browser.get(link)

optionHome = browser.find_element (By.CSS_SELECTOR, ".rct-text>button" )
optionHome.click()

#optionDesc = browser.find_element (By.CSS_SELECTOR, "[for=tree-node-desktop]" )
#optionDesc.click()

#optionNotesbut = browser.find_element (By.CSS_SELECTOR, "#tree-node>ol>li>ol>.rct-node-parent>.rct-text>button" )
#optionNotesbut.click()

#optionNotes = browser.find_element (By.CSS_SELECTOR, "[for=tree-node-notes]" )
#optionNotes.click()

optionDocBut = browser.find_element (By.CSS_SELECTOR, "#tree-node>ol>li>ol>li:nth-of-type(2)>.rct-text>button")
optionDocBut.click()

optionWSBut = browser.find_element (By.CSS_SELECTOR, "#tree-node>ol>li>ol>li:nth-of-type(2)>ol>li>.rct-text>button")
optionWSBut.click()

optionAng = browser.find_element (By.CSS_SELECTOR, "[for=tree-node-angular]" )
optionAng.click()

time.sleep(10)
browser.quit()
#
