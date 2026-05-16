from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.components.purchase_modal import PurchaseModal

class CartPage(BasePage):
    PLACE_ORDER_BTN = (By.XPATH, "//button[text()='Place Order']")
    SUCCESS_MARKER = (By.XPATH, "//h2[text()='Thank you for your purchase!']")

    def click_place_order(self):
        self.click(self.PLACE_ORDER_BTN)
        return PurchaseModal(self.driver)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MARKER)
