import requests


class CustomerAPI:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        self.session = requests.Session()

    def get_customer(self, customer_id):
        return self.session.get(
            f"{self.BASE_URL}/users/{customer_id}",
            timeout=10
        )

    def create_customer(self, customer_data):
        return self.session.post(
            f"{self.BASE_URL}/users",
            json=customer_data,
            timeout=10
        )