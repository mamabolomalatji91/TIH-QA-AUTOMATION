from config import BASE_URL
import pytest

from pages.quote_page import QuotePage
from pages.customer_page import CustomerPage


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.e2e
def test_complete_customer_quote_journey(driver):

    driver.get(BASE_URL)

    # -------------------------
    # Vehicle details
    # -------------------------
    quote_page = QuotePage(driver)

    quote_page.enter_vehicle_details(
        "Comprehensive",
        "GP123456",
        "Toyota",
        "Corolla"
    )

    quote_page.click_continue()

    # -------------------------
    # Customer details
    # -------------------------
    customer_page = CustomerPage(driver)

    customer_page.enter_customer_details(
        "John",
        "Tester",
        "9001015009092",
        "john@test.com",
        "0821234567",
        "35"
    )

    customer_page.click_continue()

    # -------------------------
    # Verify successful journey
    # -------------------------
    assert "quote" in driver.current_url.lower() or \
           "success" in driver.page_source.lower()