from config import BASE_URL
import csv
from pathlib import Path

import pytest

from pages.quote_page import QuotePage
from pages.customer_page import CustomerPage


def load_customer_data():
    project_root = Path(__file__).resolve().parent.parent
    csv_path = project_root / "data" / "customers.csv"

    with open(csv_path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

@pytest.mark.boundary
@pytest.mark.regression
@pytest.mark.parametrize(
    "customer",
    load_customer_data(),
    ids=lambda customer: f"{customer['first_name']}_{customer['last_name']}"
)
def test_customer_data(driver, customer):

    driver.get(BASE_URL)

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
        customer["first_name"],
        customer["last_name"],
        customer["id_number"],
        customer["email"],
        customer["phone"],
        customer["age"]
    )

    customer_page.click_continue()

    # Validate expected result
    if customer["expected_result"] == "rejected":

        error_message = customer_page.get_error_message()

        assert error_message in [
         "Customer must be 18 years or older.",
         "Please complete all required fields.",
         "Please enter a valid email address."
]

    else:

        assert driver.current_url.endswith("result.html")