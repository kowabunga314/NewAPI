# Import all the models, so that Base has them before being
# imported by Alembic
from database.base_class import Base  # noqa
from product.models import Product  # noqa
from supply.models import MaterialCost, ProductionCost  # noqa
