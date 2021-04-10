from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from PIL import Image

driver = webdriver.Chrome(executable_path="D:\\seleniumProject1\\drivers\\chromedriver.exe")

driver.get("http://127.0.0.1:8000/accounts/login/")


element = driver.find_element_by_id("navbarSupportedContent");
location = element.location;
size = element.size;
driver.save_screenshot("loginImage.png");

# crop image
x = location['x'];
y = location['y'];
width = location['x']+size['width'];
height = location['y']+size['height'];
im = Image.open('logoImage.png')
im = im.crop((int(x), int(y), int(width), int(height)))
im.save('logo-section-Image.png')

driver.quit()
