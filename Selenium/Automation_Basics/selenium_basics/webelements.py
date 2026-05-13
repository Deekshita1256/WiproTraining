from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.edge.service import Service
import time

#driver = webdriver.Edge()
driver = webdriver.Edge(service = Service('../resources/msedgedriver.exe'))
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(5)

# -----------Text Input ---------------
text_input = driver.find_element(By.ID, "my-text-id")
text_input.clear()
text_input.send_keys("Selenium WebDriver Demo")

# ------------- Password Input -------------
password_input = driver.find_element(By.NAME, "my-password")
password_input.clear()
password_input.send_keys("secret123")

#--------Text Area ----------
textarea = driver.find_element(By.NAME, "my-textarea")
textarea.clear()
textarea.send_keys("This is sample message")

#-------CheckBox -------------
checkbox = driver.find_element(By.ID, "my-check-2")
checkbox.click()

#------------- RADIO BUTTON -------
radio = driver.find_element(By.ID, "my-radio-2")
radio.click()

#-------------- DROPDOWN -----------
dropdown = driver.find_element(By.NAME, "my-select")
dropdown.click()
option = driver.find_element(By.CSS_SELECTOR, "select[name='my-select'] option[value='2']")
option.click()

#------------- Multi-select -------------
multi_select = driver.find_element(By.NAME, "my-datalist")
multi_select.send_keys("New York")

#---------- File Upload ----------------
file_upload = driver.find_element(By.NAME, "my-file")
file_upload.send_keys("C:\Wipro Training\Selenium\Automation_Basics\selenium_basics\locators.py")

#----------- Range Slider --------------
range_slider = driver.find_element(By.NAME, "my-range")
driver.execute_script("argument[0].value = 10;", range_slider)

#------------- Colour Picker -----------
colour_picker = driver.find_element(By.NAME, "my-colors")
colour_picker.send_keys("#00ff00")

#------------ Date Picker --------------
data_input = driver.find_element(By.NAME, "my-date")
data_input.send_keys("2025-12-25")

#-------------- Submit Button ---------------
submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit")
time.sleep(20)
submit_btn.click()

time.sleep(10)
driver.quit()