from app.models.product_models import Product
from app.controllers.product_controller import ProductController


producto=ProductController().get_product(1)
print (producto)