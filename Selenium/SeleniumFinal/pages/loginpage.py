from selenium.webdriver.common.by import By
from pages.basepage import BasePage


class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")

    def login(self, username="standard_user", password="secret_sauce"):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def read_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)