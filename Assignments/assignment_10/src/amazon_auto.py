import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def navigate_to_mobiles_and_back(self):
        mobile_link = self.driver.find_element(By.LINK_TEXT, "Mobiles")
        mobile_link.click()
        self.driver.back()

    def search_wireless_headphones(self):
        search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_button = self.driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
        search_bar.clear()
        search_bar.send_keys("Wireless Headphones")
        search_button.click()
        header = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']")
        return header.text

    def search_laptop_and_click_first(self, model):
        search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_bar.clear()
        search_bar.send_keys(model + Keys.ENTER)
        first_result = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.s-image")))
        first_result.click()

    def click_about_us_and_get_header(self):
        # Using the exact CSS selector from Exercise 4 logic
        about_us = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='www.aboutamazon']")))
        about_us.click()
        header = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        return header.text

    def search_smart_watches_and_filter_samsung(self):
        search_bar = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_bar.clear()
        search_bar.send_keys("Smart Watches" + Keys.ENTER)

        # Exercise 5 logic: Handle "Show All" and filter
        show_all = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='filter-p_123']/span/li/span/div/a/span")))
        show_all.click()
        brand_filter = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Samsung']")))
        brand_filter.click()

        time.sleep(3)  # Wait for async refresh
        products = self.driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")
        return len(products)
