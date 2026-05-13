from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductListingPage:
    PRODUCT_TITLES = (By.CSS_SELECTOR, "a h2 span")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def first_product_title(self):
        first_product = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TITLES))
        print("\nFirstProduct:", first_product.text)

    def all_products(self):
        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))
        print(f"\nFound {len(product_titles)} product titles on page one.\n")

        for i, title in enumerate(product_titles[:5], start = 1):
            print(f"{i}. {title.text}")

        return len(product_titles) > 0

    def brand_filter_locator(self, brandname):
        BRAND_FILTER = (By.XPATH, "//span[text()='" + brandname +"']/parent::a/descendant::i")
        return BRAND_FILTER

    def select_brand_filter(self, brandname):
        brand_filter = self.driver.find_element(*self.brand_filter_locator(brandname))
        brand_filter.click()

    def check_product_titles_for_brand_filter(self, brandname):
        product_titles = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_TITLES))

        for title in product_titles:
            print(title.text)
            if not title.text.__contains__(brandname):
                return False
            return True