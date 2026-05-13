import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from selenium.webdriver.common.by import By

from pages.product_listing_page import ProductListingPage

def test_open_amazon(driver):
    assert "amazon" in driver.current_url, "URl for amazon is not correct"
    print("\nOpened Amazon HomePage. Title and URL verified.")

@pytest.mark.parametrize("searchproduct",[
    ("wireless mouse"), ("shoes")
])
def test_search_product(driver, searchproduct):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Searching product - {searchproduct}")
    homepage.click_search_button()

    # assert driver.current_url.__contains__('wireless'), 'Search result page did not load.'
    # assert driver.title.__contains__('wireless'),'Search results page did not load.'
    assert homepage.is_amazon_page_loaded(), "Search result page not loaded"
    print(f"\nSearch results page loaded successfully - {searchproduct}")

def test_find_elements_amazon(driver):
    wait = WebDriverWait(driver, 15)

    # Single Product Title
    first_product = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a h2 span")))
    print("\nFirst Product: ", first_product.text)

    product_titles = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a h2 span")))
    print(f"\nFound {len(product_titles)} product titles on page one.")

    for i, title in enumerate(product_titles[:5], start=1):
        print(f"{i}. {title.text}")

    assert len(product_titles) > 0, "No product found on amazon search results"


@pytest.mark.parametrize(("searchproduct","brandname"), [
    ("wireless mouse",'Logitech'),
    ("shoes",'Nike')
])
def test_brand_filter(driver, searchproduct, brandname):
    homepage = HomePage(driver)

    homepage.type_search_input(searchproduct)
    print(f"Searching product - {searchproduct}")
    homepage.click_search_button()

    # assert driver.current_url.__contains__('wireless'), 'Search result page did not load.'
    # assert driver.title.__contains__('wireless'),'Search results page did not load.'
    assert homepage.is_amazon_page_loaded(), "Search result page not loaded"
    print(f"\nSearch results page loaded successfully - {searchproduct}")
    productlistingpage = ProductListingPage(driver)

    productlistingpage.select_brand_filter(brandname)

    assert productlistingpage.check_product_titles_for_brand_filter(brandname), 'Brand filter not applied properly'