
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
# Set up Edge driver
driver = webdriver.Edge(service=Service('../resources/msedgedriver.exe'))

# Open Google
driver.get("https://www.google.com")

#wait = WebDriverWait(driver, 10)

wait = WebDriverWait(driver, timeout=10, poll_frequency=0.3,
                     ignored_exceptions=[NoSuchElementException])

search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
# search_box.send_keys("Explicit Wait")
search_box.send_keys("Fluent Wait")

#google_search = driver.find_element(By.NAME, "btnK")
google_search = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
google_search.click()