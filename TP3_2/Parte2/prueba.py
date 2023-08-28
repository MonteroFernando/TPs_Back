from app.models.product_models import Product
from app.controllers.product_controller import ProductController


producto=ProductController().get_products()
for prod in producto:
    print (prod)