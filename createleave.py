from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from login_module import login

username = input('Please enter the username:')
password = input('Please enter the password:')

driver= login(username, password)
wait = WebDriverWait(driver, 10)




apply_leave_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h6[contains(.,'Apply Leave')]")))
apply_leave_button.click()

leave_category = bool(input("Which leave?: Press 1 for full and 0 for half " ))
if leave_category== 1:
        print("Full Leave")
        time.sleep(2)
        full_leave =driver.find_element(By.CSS_SELECTOR,".custom-control-label[for='radio2']").click()
     
        time.sleep(2)
        
        Type_of_leave= driver.find_element(By.ID,'leaveType').click
       

        Type_of_leave.select_by_visible_text('Annual Leave')
       

else: half_leave = driver.find_element(By.CSS_SELECTOR,".custom-control-label[for='radio1']").click
print("Half Leave")

