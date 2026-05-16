import pytest
import logging
from selenium import webdriver
from pages.home_page import HomePage

logging.basicConfig(level=logging.INFO)


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.demoblaze.com/index.html")
    yield driver
    driver.quit()


def test_exercise_1_chaining(driver):
    home = HomePage(driver)
    # Execution matches the requested goal structure precisely
    home.click_laptops().verify_laptop_list_presence()


def test_exercise_2_dynamic_list(driver):
    home = HomePage(driver)
    phones_page = home.click_phones()
    product_list = phones_page.get_all_product_names()
    assert "Samsung galaxy s6" in product_list


def test_exercise_3_synchronization_alerts(driver):
    home = HomePage(driver)
    product_page = home.click_product("Sony vaio i5")
    product_page.add_product_to_cart()


def test_exercise_4_checkout_flow(driver):
    home = HomePage(driver)

    # Setup step: Add item to trigger functional checkout
    product_page = home.click_product("Sony vaio i5")
    product_page.add_product_to_cart()

    cart = home.click_cart()
    modal = cart.click_place_order()

    customer_data = {
        "name": "Jane Doe",
        "country": "USA",
        "city": "Austin",
        "card": "1234567890",
        "month": "12",
        "year": "2028"
    }

    modal.fill_purchase_form(customer_data)
    assert cart.get_success_message() == "Thank you for your purchase!"
