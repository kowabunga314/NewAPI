# Import all the models, so that Base has them before being
# imported by Alembic
from database.base_class import Base  # noqa
from admin.models import User
from product.models import Product, MaterialCost, ProductionCost  # noqa
# from supply.models import MaterialCost, ProductionCost  # noqa
