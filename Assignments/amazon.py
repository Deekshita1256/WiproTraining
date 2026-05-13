import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Driver
driver = webdriver.Edge()
driver.maximize_window()
# Exercise 3: Implementing Implicit Wait at driver level
driver.implicitly_wait(10)

try:
    # --- Exercise 1: Navigation and Title Verification ---
    print("Running Exercise 1...")
    driver.get("https://amazon.in")
    assert "Amazon" in driver.title, "Title verification failed!"

    # Navigate to Mobiles and back
    mobile_link = driver.find_element(By.LINK_TEXT, "Mobiles")
    mobile_link.click()
    driver.back()
    print("Exercise 1 Complete: Title verified and navigation successful.")

    # --- Exercise 2: Basic Locators and Search ---
    print("\nRunning Exercise 2...")
    # ID for search bar, XPath for search button
    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")

    search_bar.clear()
    search_bar.send_keys("Wireless Headphones")
    search_button.click()

    header_check = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")
    assert "Wireless Headphones" in header_check.text
    print(f"Exercise 2 Complete: Search results verified for {header_check.text}")

    # --- Exercise 3: Implementing Explicit Wait ---
    print("\nRunning Exercise 3...")
    search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
    search_bar.clear()
    search_bar.send_keys("MacBook Pro")
    search_bar.send_keys(Keys.ENTER)

    # Explicit Wait for the first product image
    wait = WebDriverWait(driver, 10)
    first_result = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.s-image")))
    first_result.click()
    print("Exercise 3 Complete: Explicit wait successful, first result clicked.")

    # --- Exercise 4: Advanced Locators (CSS & Links) ---
    print("\nRunning Exercise 4...")
    driver.get("https://amazon.in")
    # CSS Selector for About Us in footer
    about_us = driver.find_element(By.CSS_SELECTOR, "a[href*='www.aboutamazon']")
    about_us.click()

    # Find element by link text on the About page (Amazon's about page varies, adjust text if needed)
    # Example: Printing a header from the about page
    content_element = driver.find_element(By.TAG_NAME, "h1")
    print(f"Exercise 4 Complete: About page header is: {content_element.text}")

    # --- Exercise 5: Element Interaction and Synchronization ---
    print("\nRunning Exercise 5...")
    driver.get("https://amazon.in")
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys("Smart Watches" + Keys.ENTER)

    # Locate Brand filter (e.g., Samsung) - Selectors may vary based on region
    show_all = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='filter-p_123']/span/li/span/div/a/span")))
    show_all.click()
    brand_filter = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Samsung']")))
    brand_filter.click()

    # Wait for the results to refresh (stale element check or wait for count update)
    time.sleep(3)  # Simple sync for refresh
    products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
    print(f"Exercise 5 Complete: Found {len(products)} products on the first page after filtering.")

finally:
    time.sleep(2)
    driver.quit()
    print("\nAll exercises completed. Browser closed.")
