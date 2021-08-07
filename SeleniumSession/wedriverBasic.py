import time

from selenium import webdriver
driver = webdriver.Chrome(executable_path="G:\\chromedriver.exe")
driver.get("https://www.google.com/")
print(driver.title)
time.sleep(3)
driver.quit()