import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

logger = logging.getLogger(__name__)

class ProductDetailsPage(BasePage):
    ADD_TO_CART_BTN = (By.XPATH, "//a[text()='Add to cart']")

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        logger.info(f"Accepted browser alert with message: {alert_text}")
        return self
