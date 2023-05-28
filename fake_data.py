from faker import Faker

from user import *


def generate_fake_data(num_users): # Генерує та вносить у бд рандомних користувачів
    fake = Faker()
    for _ in range(num_users):
        user = User(name=fake.name(), email=fake.email())
        db.session.add(user)
    db.session.commit()
