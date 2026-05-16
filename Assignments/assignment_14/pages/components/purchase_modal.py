import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class PurchaseModal(BasePage):
    NAME = (By.ID, "name")
    COUNTRY = (By.ID, "country")
    CITY = (By.ID, "city")
    CARD = (By.ID, "card")
    MONTH = (By.ID, "month")
    YEAR = (By.ID, "year")
    PURCHASE_BTN = (By.XPATH, "//button[text()='Purchase']")

    def fill_purchase_form(self, data_dict):
        self._fill_field(self.NAME, data_dict.get("name"), "Name")
        self._fill_field(self.COUNTRY, data_dict.get("country"), "Country")
        self._fill_field(self.CITY, data_dict.get("city"), "City")
        self._fill_field(self.CARD, data_dict.get("card"), "Card")
        self._fill_field(self.MONTH, data_dict.get("month"), "Month")
        self._fill_field(self.YEAR, data_dict.get("year"), "Year")
        self.click(self.PURCHASE_BTN)

    def _fill_field(self, locator, value, field_name):
        with allure.step(f"Typing '{value}' into field: {field_name}"):
            # Upgrade from presence verification to clickability verification
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(value)
