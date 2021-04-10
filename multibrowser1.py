from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="F:\\Users\\new\\seleniumProject1\\drivers\\chromedriver.exe")
driver.get("http://127.0.0.1:8000/accounts/login/")
driver.find_element_by_name("username").send_keys("manna")
driver.find_element_by_name("password").send_keys("manna12345")
#driver.find_element_by_name("submit").send_keys(Keys.ENTER)
time.sleep(3)
driver.close()
print("Testing Successfull")
