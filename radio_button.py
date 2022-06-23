import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get("https://demoqa.com/radio-button")

rbYes=browser.find_element(By.CSS_SELECTOR,"[for=yesRadio]")
rbYes.click()
time.sleep(5)

rbWow=browser.find_element(By.CSS_SELECTOR,"[for=impressiveRadio]")
rbWow.click()

rbNo=browser.find_element(By.CSS_SELECTOR,"[for=noRadio]")
rbNo.click()


time.sleep(10)
browser.quit()

