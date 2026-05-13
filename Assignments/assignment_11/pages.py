from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Exercise 4: Component-Based Architecture
class SideMenuComponent:
    def __init__(self, driver):
        self.driver = driver
        self.pim_link = (By.XPATH, "//span[text()='PIM']")
        self.admin_link = (By.XPATH, "//span[text()='Admin']")

    def select_pim(self):
        self.driver.find_element(*self.pim_link).click()

# Exercise 1 & 2: Basic POM & Sync
# assignment_11/pages.py


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/ "
        self.user_field = (By.NAME, "username")
        self.pass_field = (By.NAME, "password")
        self.login_btn = (By.TAG_NAME, "button")

    def load(self):
        self.driver.get(self.url)

    def login(self, user, pwd):
        # ADD THIS: Wait explicitly for the username field to be present
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.user_field)
        )

        self.driver.find_element(*self.user_field).send_keys(user)
        self.driver.find_element(*self.pass_field).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()
        return DashboardPage(self.driver)


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu = SideMenuComponent(driver) # Component instance
        # Exercise 2: Wait for Dashboard Heading
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )

# Exercise 3 & 5: Navigation, Chaining, and List Elements
class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        # Exercise 5: List elements locator
        self.user_rows = (By.XPATH, "(//div[@class='oxd-table-card']//div[@role='cell'])[3]/div")

    def verify_user_exists(self, target_name):
        try:
            # 1. Wait for at least one cell to be visible before checking
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located(self.user_rows)
            )

            # 2. Get all elements matching the column
            elements = self.driver.find_elements(*self.user_rows)

            # 3. Check if the text matches
            return any(target_name.lower() in el.text.lower() for el in elements)
        except:
            # If the table doesn't load or elements aren't found, return False instead of crashing
            return False

