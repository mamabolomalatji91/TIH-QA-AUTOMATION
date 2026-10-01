import pytest

from pages.quote_page import QuotePage
from selenium.webdriver.common.by import By
from config import APP_URL

import pytest

@pytest.mark.smoke
@pytest.mark.regression
def test_valid_insurance_quote(driver):

    
    driver.get(APP_URL)

    # Vehicle details
    quote_page = QuotePage(driver)

    quote_page.enter_vehicle_details(
        "Comprehensive",
        "GP123456",
        "Toyota",
        "Corolla"
)

    quote_page.click_continue()

    # Customer details
    driver.find_element(By.ID, "firstName").send_keys("John")
    driver.find_element(By.ID, "lastName").send_keys("Tester")
    driver.find_element(By.ID, "idNumber").send_keys("9001015009087")
    driver.find_element(By.ID, "email").send_keys("john@test.com")
    driver.find_element(By.ID, "phone").send_keys("0821234567")
    driver.find_element(By.ID, "age").send_keys("30")

    driver.find_element(By.TAG_NAME, "button").click()

    # Verify quote was generated
    quote_title = driver.find_element(By.TAG_NAME, "h1").text

    assert quote_title == "Quote Generated"
    """assert quote_title == "THIS SHOULD FAIL"""

    premium = driver.find_element(By.ID, "premium").text
    assert premium == "R1200 per month"

    

    