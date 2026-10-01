import csv


def load_customer_data():
    with open("test_data/customers.csv", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


if __name__ == "__main__":
    customers = load_customer_data()

    for customer in customers:
        print(customer)