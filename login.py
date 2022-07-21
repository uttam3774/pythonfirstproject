import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.XPATH,".//input[@id='txtUsername']").send_keys("Admin")

driver.find_element(By.XPATH,".//input[@id='txtPassword']").send_keys("admin123")

driver.find_element(By.XPATH,".//input[@class='button']").click()

act_title=driver.title

exp_title='OrangeHRM'

if act_title==exp_title:
    print("Login test succesfull")
else:
    print("Login test Failed")


driver.close()


