from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # ===== Generic element actions =====
    def get_element(self, locator, condition=EC.visibility_of_element_located):
        return self.wait.until(condition(locator))

    def click(self, locator):
        self.get_element(locator, EC.element_to_be_clickable).click()

    def type(self, locator, text):
        element = self.get_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.get_element(locator).text

    def is_visible(self, locator):
        return self.get_element(locator).is_displayed()