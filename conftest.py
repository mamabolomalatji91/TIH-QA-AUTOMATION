import logging
from pathlib import Path

import pytest
from selenium import webdriver

from config import APP_URL


PROJECT_ROOT = Path(__file__).resolve().parent

SCREENSHOT_DIR = PROJECT_ROOT / "reports" / "screenshots"
LOG_DIR = PROJECT_ROOT / "logs"

SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)


logging.basicConfig(
    filename=LOG_DIR / "test_execution.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


@pytest.fixture
def driver():
    logging.info("Starting Chrome WebDriver")

    driver = webdriver.Chrome()
    driver.get(APP_URL)

    logging.info("Application opened: %s", APP_URL)

    yield driver

    logging.info("Closing Chrome WebDriver")
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            screenshot_path = (
                SCREENSHOT_DIR /
                f"{item.name}.png"
            )

            driver.save_screenshot(str(screenshot_path))

            logging.error(
                "Test failed: %s | Screenshot: %s",
                item.name,
                screenshot_path
            )

            print(
                f"\nScreenshot saved: {screenshot_path}"
            )