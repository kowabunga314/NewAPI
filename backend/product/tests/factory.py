import factory
from faker import Faker
import random

from product.models import Product


fake = Faker()


class ProductFactory(factory.Factory):
    class Meta:
        model = Product
    id = factory.Sequence(lambda n: n)
    name = fake.name()
    description = fake.text()
    profit_margin = round(random.uniform(0.2, 1.5), 2)
    sku = str(random.randint(100000, 999999))
    tags = []
    owner_id = 1
    material_costs = []


