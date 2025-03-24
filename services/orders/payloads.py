from faker import Faker

fake = Faker()

class Payloads:

    create_order = {
      "status": "OPEN",
      "courierId": fake.random_int(min=100, max=999),
      "customerName": fake.first_name(),
      "customerPhone": fake.phone_number(),
      "comment": fake.sentence(),
      "id": fake.random_int(min=100, max=999)
    }

