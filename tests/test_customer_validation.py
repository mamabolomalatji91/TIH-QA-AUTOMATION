import pytest

from pages.quote_page import QuotePage
from pages.customer_page import CustomerPage
from config import APP_URL

@pytest.mark.negative
@pytest.mark.regression
def test_customer_under_18_is_rejected(driver):

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
    customer_page = CustomerPage(driver)

    customer_page.enter_customer_details(
        "John",
        "Tester",
        "0901015009087",
        "john@test.com",
        "0821234567",
        "17"
    )

    customer_page.click_continue()

    # Verify under-18 customer is rejected
    error_message = customer_page.get_error_message()

    assert error_message == "Customer must be 18 years or older."

    