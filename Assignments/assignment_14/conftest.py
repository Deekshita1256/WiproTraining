import pytest
import allure
from selenium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://demoblaze.com")

    # Attach driver to the request node so the hook can access it on failure
    request.node.funcargs['driver'] = driver

    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Check if the test failed during the execution phase
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            try:
                # Capture and attach the screenshot to Allure
                screenshot = driver.get_screenshot_as_png()
                allure.attach(
                    screenshot,
                    name="Failure_Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Failed to capture screenshot: {e}")
