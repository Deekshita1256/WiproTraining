from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time
from selenium.common.exceptions import StaleElementReferenceException

class HomePage(BasePage):
    LAPTOPS_CAT = (By.XPATH, "//a[@onclick=\"byCat('notebook')\"]")
    PHONES_CAT = (By.XPATH, "//a[@onclick=\"byCat('phone')\"]")
    PRODUCT_LINKS = (By.CLASS_NAME, "card-title")
    NAV_CART = (By.ID, "cartur")
    NAV_LOGIN = (By.ID, "login2")

    def click_laptops(self):
        self.click(self.LAPTOPS_CAT)
        return LaptopsCategoryPage(self.driver)

    def click_phones(self):
        self.click(self.PHONES_CAT)
        return CategoryPage(self.driver)

    def click_product(self, product_name):
        product_locator = (By.LINK_TEXT, product_name)
        self.click(product_locator)
        from pages.product_details_page import ProductDetailsPage
        return ProductDetailsPage(self.driver)

    def click_cart(self):
        self.click(self.NAV_CART)
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def click_login(self):
        self.click(self.NAV_LOGIN)
        from pages.components.login_modal import LoginModal
        return LoginModal(self.driver)


class CategoryPage(BasePage):
    PRODUCT_NAMES = (By.CLASS_NAME, "hrefch")

    def get_all_product_names(self):
        # Allow the dynamic DOM grid to refresh after clicking the category link
        time.sleep(1.5)

        # Implement a retry loop to catch any rapid UI re-rendering spikes
        for _ in range(3):
            try:
                elements = self.find_all(self.PRODUCT_NAMES)
                return [el.text for el in elements if el.text]
            except StaleElementReferenceException:
                time.sleep(0.5)
                continue
        raise StaleElementReferenceException("Product list element DOM updates failed to stabilize.")


class LaptopsCategoryPage(CategoryPage):
    def verify_laptop_list_presence(self):
        product_names = self.get_all_product_names()
        assert len(product_names) > 0, "Laptop list is empty!"
        return self


# Add this locator inside your HomePage class:


# Add this method inside your HomePage class:

