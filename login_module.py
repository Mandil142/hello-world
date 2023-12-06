from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login(username, password):
    try:
        driver = webdriver.Chrome()
        driver.get("https://dev.bidheehrms.com")
        
        wait = WebDriverWait(driver, 10)  # Set up a 10-second maximum wait time
        
        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys(username)
        
        password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.send_keys(password)
        
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn")))
        submit_button.click()
        
        if driver.current_url == "https://dev.bidheehrms.com/admin/dashboard":
            print("Logged in successfully")
            return driver
    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()
   