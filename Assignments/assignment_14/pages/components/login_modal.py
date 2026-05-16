from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginModal(BasePage):
    USERNAME_FIELD = (By.ID, "loginusername")
    PASSWORD_FIELD = (By.ID, "loginpassword")
    LOGIN_BTN = (By.XPATH, "//button[text()='Log in']")

    def login_with_credentials(self, username, password):
        # Explicitly wait until the input element is ready to accept text
        username_el = self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
        username_el.clear()
        username_el.send_keys(username)

        password_el = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        password_el.clear()
        password_el.send_keys(password)

        self.click(self.LOGIN_BTN)

        # Wait for the validation or failure alert context to appear
        self.wait.until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text
