import pytest

from api.customer_api import CustomerAPI


@pytest.mark.api
@pytest.mark.negative
def test_get_nonexistent_customer():

    api = CustomerAPI()

    response = api.get_customer(9999)

    assert response.status_code == 404

@pytest.mark.api
@pytest.mark.api
def test_get_customer():

    api = CustomerAPI()

    response = api.get_customer(1)

    # HTTP validation
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2

    # Response validation
    data = response.json()

    assert data["id"] == 1
    assert isinstance(data["id"], int)

    assert "name" in data
    assert isinstance(data["name"], str)

    assert "username" in data
    assert isinstance(data["username"], str)

    assert "email" in data
    assert isinstance(data["email"], str)

    assert "@" in data["email"]
@pytest.mark.api
def test_create_customer():

    api = CustomerAPI()

    customer = {
        "name": "QA Tester",
        "username": "qa_tester",
        "email": "qa@test.com"
    }

    response = api.create_customer(customer)

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "QA Tester"
    assert data["username"] == "qa_tester"
    assert data["email"] == "qa@test.com"

@pytest.mark.api
@pytest.mark.parametrize(
    "customer_id",
    [1, 2, 3, 5]
)
def test_get_multiple_customers(customer_id):

    api = CustomerAPI()

    response = api.get_customer(customer_id)

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == customer_id
    assert "name" in data
    assert "email" in data