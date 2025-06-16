from faker import Faker

fake = Faker()

class Payloads:

    @staticmethod
    def create_order():
        return {
            "status": "OPEN",
            "courierId": fake.random_int(min=100, max=999),
            "customerName": fake.first_name(),
            "customerPhone": '1245369874',
            "comment": fake.word(),
            "id": fake.random_int(min=1, max=99)
        }

    @staticmethod
    def generate_n_orders(n):
        return [Payloads.create_order() for _ in range(n)]


