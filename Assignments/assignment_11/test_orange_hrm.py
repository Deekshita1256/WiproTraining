import pytest
import pytest_check as check
from pages import LoginPage, PIMPage


class TestOrangeHRM:

    @pytest.fixture(autouse=True, scope="class")
    def setup_class(self, driver):
        # Attach variables to the Class itself
        TestOrangeHRM.driver = driver
        TestOrangeHRM.login_page = LoginPage(driver)

    def test_exercise_1_and_2_login(self):
        """Exercise 1 & 2: Login and Sync."""
        self.login_page.load()
        # Use TestOrangeHRM. instead of self.
        TestOrangeHRM.dashboard = self.login_page.login("Admin", "admin123")
        assert "dashboard" in self.driver.current_url.lower()

    def test_exercise_3_and_4_navigation(self):
        """Exercise 3 & 4: Sidebar and Chaining."""
        # Retrieve from Class level
        self.dashboard.menu.select_pim()
        TestOrangeHRM.pim_page = PIMPage(self.driver)
        assert "viewEmployeeList" in self.driver.current_url

    def test_exercise_5_data_verification(self):
        """Exercise 5: List Elements."""
        # Retrieve from Class level
        target_user = "Charlie"
        check.is_true(self.pim_page.verify_user_exists(target_user), f"User {target_user} missing!")

        print("Execution continued!")

