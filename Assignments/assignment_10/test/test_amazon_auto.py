import unittest
import sys
import os
from selenium import webdriver

# Ensures the 'src' folder is reachable for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from assignment_10.src import AmazonPage

class TestAmazonAutomation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setup performed once before all tests."""
        cls.driver = webdriver.Edge()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.amazon = AmazonPage(cls.driver)

    def setUp(self):
        """Navigate to home page before every individual test exercise."""
        self.driver.get("https://amazon.in")

    def test_exercise_1_navigation(self):
        print("\nRunning Exercise 1...")
        self.assertIn("Amazon", self.driver.title)
        self.amazon.navigate_to_mobiles_and_back()

    def test_exercise_2_search(self):
        print("\nRunning Exercise 2...")
        header_text = self.amazon.search_wireless_headphones()
        self.assertIn("Wireless Headphones", header_text)

    def test_exercise_3_explicit_wait(self):
        print("\nRunning Exercise 3...")
        # This will search and click the first result using Explicit Wait
        self.amazon.search_laptop_and_click_first("MacBook Pro")

    def test_exercise_4_footer_css(self):
        print("\nRunning Exercise 4...")
        header_text = self.amazon.click_about_us_and_get_header()
        print(f"Captured Header: {header_text}")
        self.assertTrue(len(header_text) > 0)

    def test_exercise_5_filter_sync(self):
        print("\nRunning Exercise 5...")
        count = self.amazon.search_smart_watches_and_filter_samsung()
        print(f"Found {count} Samsung products.")
        self.assertGreater(count, 0)

    @classmethod
    def tearDownClass(cls):
        """Close browser after all tests are finished."""
        cls.driver.quit()

# if __name__ == "__main__":
#     unittest.main()
