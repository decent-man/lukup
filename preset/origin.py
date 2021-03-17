#/usr/bin/python3.8
from selenium import webdriver
# from selenium.webdriver import Firefox
# from selenium.webdriver.FirefoxOptions import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
options.headless = True
driver = webdriver.Firefox(executable_path='/home/rakshit/Downloads/geckodriver',options=options)
# PATH = "/home/rakshit/Downloads/geckodriver"
# driver = webdriver.firefox(PATH)
url = 'https://wiki.archlinux.org/index.php/Xmodmap'
driver.get(url)
# print("========\n" + driver.current_url + "\n========")
head = driver.find_elements_by_class_name('firstHeading') [0]
contentbody = driver.find_elements_by_class_name('mw-parser-output') [0]
print("========\n" + head.text + "\n========")
print("========\n" + contentbody.text + "\n========")
# print(page)
driver.quit()
